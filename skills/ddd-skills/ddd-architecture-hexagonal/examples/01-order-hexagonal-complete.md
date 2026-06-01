# Example: 完整六边形订单示例

本示例展示一个订单创建和支付流程的完整六边形架构实现，涵盖 Domain、Application、Adapter 三层。

## 领域模型

```java
// ─── 值对象 ───

// domain/model/order/OrderId.java
public final class OrderId {
    private final String value;

    private OrderId(String value) { this.value = value; }

    public static OrderId generate() {
        return new OrderId("ORD-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase());
    }

    public static OrderId of(String value) { return new OrderId(value); }
    public String getValue() { return value; }

    @Override
    public boolean equals(Object o) { /* ... */ }
    @Override
    public int hashCode() { /* ... */ }
}

// domain/model/order/OrderStatus.java
public enum OrderStatus {
    DRAFT, PAID, SHIPPED, DELIVERED, CANCELLED;

    public boolean canTransitionTo(OrderStatus target) {
        return switch (this) {
            case DRAFT -> target == PAID || target == CANCELLED;
            case PAID -> target == SHIPPED || target == CANCELLED;
            case SHIPPED -> target == DELIVERED;
            default -> false;
        };
    }

    public boolean canPay() { return this == DRAFT; }
}

// ─── 聚合根 ───

// domain/model/order/Order.java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private CustomerId customerId;
    private Money totalAmount;
    private OrderStatus status;
    private List<OrderItem> items;
    private LocalDateTime createdAt;

    protected Order() {}

    public static Order create(CustomerId customerId) {
        Order order = new Order();
        order.id = OrderId.generate();
        order.customerId = customerId;
        order.status = OrderStatus.DRAFT;
        order.items = new ArrayList<>();
        order.totalAmount = Money.ZERO;
        order.createdAt = LocalDateTime.now();
        order.addDomainEvent(new OrderCreatedEvent(order.id, customerId));
        return order;
    }

    public void addItem(ProductId productId, int quantity, Money unitPrice) {
        if (status != OrderStatus.DRAFT) throw new OrderException("只能向草稿添加商品");
        items.add(new OrderItem(productId, quantity, unitPrice));
        recalculateTotal();
    }

    public void pay(PaymentId paymentId) {
        if (!status.canPay()) throw new OrderException("当前状态不可支付");
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id, this.totalAmount, paymentId));
    }

    public void cancel(String reason) {
        if (status == OrderStatus.DELIVERED || status == OrderStatus.CANCELLED) {
            throw new OrderException("已发货或已取消的订单不可取消");
        }
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelledEvent(this.id, reason));
    }

    private void recalculateTotal() {
        this.totalAmount = items.stream()
                .map(OrderItem::getSubtotal)
                .reduce(Money.ZERO, Money::add);
    }

    public OrderId getId() { return id; }
    public OrderStatus getStatus() { return status; }
    public Money getTotalAmount() { return totalAmount; }
    public List<OrderItem> getItems() { return Collections.unmodifiableList(items); }
}
```

## 端口定义

```java
// domain/port/inbound/CreateOrderUseCase.java
public interface CreateOrderUseCase {
    OrderCreatedResult execute(CreateOrderCommand command);
}

// domain/port/inbound/PayOrderUseCase.java
public interface PayOrderUseCase {
    PaymentResult execute(PayOrderCommand command);
}

// domain/port/inbound/GetOrderUseCase.java
public interface GetOrderUseCase {
    OrderDTO execute(GetOrderQuery query);
}

// domain/port/outbound/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(Order order);
}

// domain/port/outbound/PaymentGateway.java
public interface PaymentGateway {
    PaymentResult charge(Money amount, PaymentMethod method);
    RefundResult refund(PaymentId paymentId, Money amount);
}

// domain/port/outbound/EventPublisher.java
public interface EventPublisher {
    void publish(DomainEvent event);
    void publishAll(List<DomainEvent> events);
}
```

## 应用服务

```java
// application/service/CreateOrderService.java
@ApplicationService
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;
    private final EventPublisher eventPublisher;

    public CreateOrderService(OrderRepository orderRepository,
                              ProductRepository productRepository,
                              EventPublisher eventPublisher) {
        this.orderRepository = orderRepository;
        this.productRepository = productRepository;
        this.eventPublisher = eventPublisher;
    }

    @Override
    @Transactional
    public OrderCreatedResult execute(CreateOrderCommand command) {
        Order order = Order.create(command.getCustomerId());
        for (var item : command.getItems()) {
            Product product = productRepository.findById(item.getProductId())
                    .orElseThrow(() -> new ProductNotFoundException(item.getProductId()));
            order.addItem(product.getId(), item.getQuantity(), product.getPrice());
        }
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
        return OrderCreatedResult.from(order);
    }
}

// application/service/PayOrderService.java
@ApplicationService
public class PayOrderService implements PayOrderUseCase {
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;

    // ... 注入 + execute 实现
}
```

## 主适配器（REST Controller）

```java
// adapter/inbound/web/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final CreateOrderUseCase createOrder;
    private final PayOrderUseCase payOrder;
    private final GetOrderUseCase getOrder;

    public OrderController(CreateOrderUseCase createOrder,
                           PayOrderUseCase payOrder,
                           GetOrderUseCase getOrder) {
        this.createOrder = createOrder;
        this.payOrder = payOrder;
        this.getOrder = getOrder;
    }

    @PostMapping
    public ResponseEntity<CreateOrderResponse> create(@RequestBody @Valid CreateOrderRequest req) {
        var result = createOrder.execute(req.toCommand());
        return ResponseEntity.status(201).body(CreateOrderResponse.from(result));
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderDTO> get(@PathVariable String id) {
        var order = getOrder.execute(new GetOrderQuery(id));
        if (order == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(order);
    }

    @PostMapping("/{id}/pay")
    public ResponseEntity<PaymentResponse> pay(@PathVariable String id,
                                                @RequestBody @Valid PayOrderRequest req) {
        var result = payOrder.execute(new PayOrderCommand(id, req.getPaymentMethod()));
        return ResponseEntity.ok(PaymentResponse.from(result));
    }
}
```

## 次适配器（JPA 实现）

```java
// adapter/outbound/persistence/PostgresOrderRepository.java
@Repository
public class PostgresOrderRepository implements OrderRepository {
    private final JpaOrderRepository jpaRepo;
    private final OrderMapper mapper;

    public PostgresOrderRepository(JpaOrderRepository jpaRepo, OrderMapper mapper) {
        this.jpaRepo = jpaRepo;
        this.mapper = mapper;
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }

    @Override
    public void save(Order order) {
        var po = mapper.toPO(order);
        jpaRepo.save(po);
    }

    @Override
    public void delete(Order order) {
        jpaRepo.deleteById(order.getId().getValue());
    }
}

// adapter/outbound/persistence/mapper/OrderMapper.java
@Component
public class OrderMapper {
    public OrderPO toPO(Order domain) {
        // Domain → PO 转换
        OrderPO po = new OrderPO();
        po.setId(domain.getId().getValue());
        po.setCustomerId(domain.getCustomerId().getValue());
        po.setStatus(domain.getStatus().name());
        po.setTotalAmount(domain.getTotalAmount().getAmount());
        po.setCurrency(domain.getTotalAmount().getCurrencyCode());
        po.setCreatedAt(domain.getCreatedAt());
        return po;
    }

    public Order toDomain(OrderPO po) {
        // PO → Domain 转换（通过工厂方法重建）
        Order order = Order.create(CustomerId.of(po.getCustomerId()));
        // ... 恢复状态
        return order;
    }
}
```

## DI 配置

```java
// configuration/config/BeanConfig.java
@Configuration
public class BeanConfig {
    @Bean
    public OrderRepository orderRepository(JpaOrderRepository jpaRepo, OrderMapper mapper) {
        return new PostgresOrderRepository(jpaRepo, mapper);
    }

    @Bean
    public PaymentGateway paymentGateway(StripeClient stripeClient) {
        return new StripePaymentGateway(stripeClient);
    }

    @Bean
    public CreateOrderUseCase createOrderUseCase(
            OrderRepository orderRepository,
            ProductRepository productRepository,
            EventPublisher eventPublisher) {
        return new CreateOrderService(orderRepository, productRepository, eventPublisher);
    }

    @Bean
    public PayOrderUseCase payOrderUseCase(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher) {
        return new PayOrderService(orderRepository, paymentGateway, eventPublisher);
    }
}
```

## 单元测试

```java
// 领域层测试 — 零 Mock
@Test
void should_create_order_and_transition_status() {
    var order = Order.create(CustomerId.of("cust-001"));
    assertEquals(OrderStatus.DRAFT, order.getStatus());

    order.pay(PaymentId.of("PAY-001"));
    assertEquals(OrderStatus.PAID, order.getStatus());
    assertTrue(order.getDomainEvents().stream()
            .anyMatch(e -> e instanceof OrderPaidEvent));
}

// 应用层测试 — Mock 端口
@Test
void should_create_order_via_usecase() {
    var orderRepo = mock(OrderRepository.class);
    var productRepo = mock(ProductRepository.class);
    var eventPub = mock(EventPublisher.class);
    var service = new CreateOrderService(orderRepo, productRepo, eventPub);

    when(productRepo.findById(any())).thenReturn(Optional.of(mock(Product.class)));
    var result = service.execute(validCommand());

    assertNotNull(result.getOrderId());
    verify(orderRepo).save(any(Order.class));
}
```

## 数据流转

```
HTTP POST /api/v1/orders
  │
  ▼
OrderController.create()          ← 主适配器
  │  请求 → DTO → Command
  ▼
CreateOrderService.execute()      ← 应用服务（实现入站端口）
  │  Order.create()               ← 领域模型
  │  productRepository.findById() ← 出站端口调用
  │  order.addItem()              ← 领域模型行为
  │  orderRepository.save()       ← 出站端口调用
  ▼
PostgresOrderRepository.save()    ← 次适配器实现
  │  mapper.toPO() → jpaRepo.save()
  ▼
Database
```
