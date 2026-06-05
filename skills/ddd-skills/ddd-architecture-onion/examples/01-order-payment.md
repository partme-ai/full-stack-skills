# Example 01 — 订单支付完整示例（Order Payment）

> 完整的洋葱架构订单支付示例，包含 Domain / Application / Infrastructure / API / Composition 五层。

## 业务描述

用户下单并支付。一个订单包含多个商品，订单有草稿、已提交、已支付、已取消等状态。

## Domain 层

```java
// core/domain/model/order/Order.java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private CustomerId customerId;
    private Money totalAmount;
    private List<OrderItem> items;
    private OrderStatus status;
    private LocalDateTime createdAt;

    private Order(OrderId id, CustomerId customerId) {
        this.id = id;
        this.customerId = customerId;
        this.items = new ArrayList<>();
        this.status = OrderStatus.DRAFT;
        this.createdAt = LocalDateTime.now();
    }

    public static Order create(OrderId id, CustomerId customerId) {
        Order order = new Order(id, customerId);
        order.addDomainEvent(new OrderCreatedEvent(id, customerId));
        return order;
    }

    public void addItem(ProductId productId, Money price, int quantity) {
        if (status != OrderStatus.DRAFT) throw new DomainException("只能向草稿添加商品");
        this.items.add(new OrderItem(productId, price, quantity));
        this.totalAmount = calculateTotal();
    }

    public void submit() {
        if (items.isEmpty()) throw new DomainException("不能提交空订单");
        if (status != OrderStatus.DRAFT) throw new DomainException("只能提交草稿订单");
        this.status = OrderStatus.SUBMITTED;
        addDomainEvent(new OrderSubmittedEvent(this.id));
    }

    public void pay(PaymentGateway gateway) {
        if (status != OrderStatus.SUBMITTED) throw new DomainException("当前状态不可支付");
        gateway.charge(this.id, this.totalAmount);
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id, this.totalAmount));
    }

    public void cancel() {
        if (status == OrderStatus.PAID) throw new DomainException("已支付订单不可取消");
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelledEvent(this.id));
    }

    private Money calculateTotal() {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }

    public OrderId getId() { return id; }
    public Money getTotalAmount() { return totalAmount; }
    public OrderStatus getStatus() { return status; }
    public LocalDateTime getCreatedAt() { return createdAt; }
}

// core/domain/model/order/OrderItem.java
public class OrderItem {
    private ProductId productId;
    private Money unitPrice;
    private int quantity;

    public OrderItem(ProductId productId, Money unitPrice, int quantity) {
        this.productId = productId;
        this.unitPrice = unitPrice;
        this.quantity = quantity;
    }

    public Money getSubtotal() { return unitPrice.multiply(quantity); }
    public ProductId getProductId() { return productId; }
    public int getQuantity() { return quantity; }
}

// core/domain/repository/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(OrderId id);
}
```

## Application 层

```java
// core/application/service/OrderApplicationService.java
public interface OrderApplicationService {
    OrderDTO createOrder(CreateOrderCommand command);
    void payOrder(String orderId);
    void cancelOrder(String orderId);
    OrderDTO getOrder(String orderId);
}

// core/application/service/OrderApplicationServiceImpl.java
public class OrderApplicationServiceImpl implements OrderApplicationService {
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;
    private final OrderDTOAssembler assembler;

    @Override
    @Transactional
    public OrderDTO createOrder(CreateOrderCommand command) {
        Order order = Order.create(OrderId.generate(), new CustomerId(command.getCustomerId()));
        command.getItems().forEach(item ->
            order.addItem(new ProductId(item.getProductId()),
                Money.of(item.getUnitPrice(), "CNY"), item.getQuantity()));
        order.submit();
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
        return assembler.toDTO(order);
    }

    @Override
    @Transactional
    public void payOrder(String orderId) {
        Order order = orderRepository.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        order.pay(paymentGateway);
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
    }

    @Override
    @Transactional
    public void cancelOrder(String orderId) {
        Order order = orderRepository.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        order.cancel();
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
    }
}
```

## Infrastructure 层

```java
// infrastructure/data/repository/OrderRepositoryImpl.java
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    private final JpaOrderRepository jpaRepo;
    private final OrderMapper mapper;

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }

    @Override
    public void save(Order order) {
        jpaRepo.save(mapper.toPO(order));
    }
}

// infrastructure/external/PaymentGatewayImpl.java
@Component
public class PaymentGatewayImpl implements PaymentGateway {
    private final RestTemplate restTemplate;

    @Override
    public void charge(OrderId orderId, Money amount) {
        // 调用支付服务
    }
}

// infrastructure/messaging/KafkaEventPublisher.java
@Component
public class KafkaEventPublisher implements EventPublisher {
    private final KafkaTemplate<String, Object> kafkaTemplate;

    @Override
    public void publish(DomainEvent event) {
        kafkaTemplate.send(event.getClass().getSimpleName(), event);
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        events.forEach(this::publish);
    }
}
```

## API 层

```java
// api/controller/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final OrderApplicationService orderAppService;

    @PostMapping
    public ResponseEntity<ApiResponse<OrderResponse>> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {
        CreateOrderCommand command = CreateOrderRequestAssembler.toCommand(request);
        OrderDTO dto = orderAppService.createOrder(command);
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(ApiResponse.success(OrderResponseAssembler.toResponse(dto)));
    }

    @PostMapping("/{orderId}/pay")
    public ResponseEntity<ApiResponse<Void>> payOrder(@PathVariable String orderId) {
        orderAppService.payOrder(orderId);
        return ResponseEntity.ok(ApiResponse.success(null));
    }

    @GetMapping("/{orderId}")
    public ResponseEntity<ApiResponse<OrderResponse>> getOrder(@PathVariable String orderId) {
        OrderDTO dto = orderAppService.getOrder(orderId);
        return ResponseEntity.ok(ApiResponse.success(OrderResponseAssembler.toResponse(dto)));
    }
}

// api/dto/request/CreateOrderRequest.java
@Data
public class CreateOrderRequest {
    @NotBlank private String customerId;
    @NotEmpty @Valid private List<Item> items;

    @Data
    public static class Item {
        @NotBlank private String productId;
        @NotNull @Positive private BigDecimal unitPrice;
        @Min(1) private int quantity;
    }
}
```

## Composition 层

```java
// composition/config/OrderModuleConfig.java
@Configuration
public class OrderModuleConfig {
    @Bean
    public OrderRepository orderRepository(JpaOrderRepository jpa, OrderMapper m) {
        return new OrderRepositoryImpl(jpa, m);
    }

    @Bean
    public OrderApplicationService orderAppService(
            OrderRepository repo, PaymentGateway gw, EventPublisher ep, OrderDTOAssembler asm) {
        return new OrderApplicationServiceImpl(repo, gw, ep, asm);
    }

    @Bean
    public OrderController orderController(OrderApplicationService svc) {
        return new OrderController(svc);
    }
}
```
