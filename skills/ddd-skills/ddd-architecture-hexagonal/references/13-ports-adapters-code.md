# 六边形端口与适配器 — 完整代码参考

## 入站端口（UseCase 接口）

```java
// domain/port/inbound/CreateOrderUseCase.java
public interface CreateOrderUseCase {
    OrderCreatedResult execute(CreateOrderCommand command);
}

public interface PayOrderUseCase {
    PaymentResult execute(PayOrderCommand command);
}

public interface GetOrderUseCase {
    OrderDTO execute(GetOrderQuery query);
}
```

## 出站端口（Repository/External 接口）

```java
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

// domain/port/outbound/NotificationPort.java
public interface NotificationPort {
    void sendEmail(Email to, EmailTemplate template);
    void sendSMS(PhoneNumber to, String message);
}
```

## 应用服务（实现入站端口）

```java
// application/service/CreateOrderService.java
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;
    private final EventPublisher eventPublisher;

    @Override
    @Transactional
    public OrderCreatedResult execute(CreateOrderCommand command) {
        Order order = Order.create(command.getCustomerId());
        for (ItemCmd item : command.getItems()) {
            Product product = productRepository.findById(item.getProductId())
                .orElseThrow(() -> new ProductNotFoundException(item.getProductId()));
            order.addItem(product.getId(), item.getQuantity(), product.getPrice());
        }
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
        return OrderCreatedResult.from(order);
    }
}
```

## 入站适配器（Controller）

```java
// adapter/inbound/web/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final CreateOrderUseCase createOrder;
    private final GetOrderUseCase getOrder;
    private final PayOrderUseCase payOrder;

    @PostMapping
    public ResponseEntity<CreateOrderResponse> create(@RequestBody CreateOrderRequest request) {
        var cmd = request.toCommand();
        var result = createOrder.execute(cmd);
        return ResponseEntity.status(201).body(CreateOrderResponse.from(result));
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderDTO> get(@PathVariable String id) {
        var order = getOrder.execute(new GetOrderQuery(id));
        if (order == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(order);
    }
}
```

## 出站适配器（Repository 实现）

```java
// adapter/outbound/persistence/PostgresOrderRepository.java
@Repository
public class PostgresOrderRepository implements OrderRepository {
    private final JpaOrderRepository jpaRepo;
    private final OrderMapper mapper;

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }

    @Override
    public void save(Order order) {
        OrderPO po = mapper.toPO(order);
        jpaRepo.save(po);
    }

    @Override
    public void delete(Order order) {
        jpaRepo.deleteById(order.getId().getValue());
    }
}
```

## 端口命名约定

| 类型 | 模式 | 示例 |
|------|------|------|
| Driver Port (入站) | `I{Action}UseCase` | `IPlaceOrderUseCase`, `IGetOrderUseCase` |
| Driven Port (出站) | `I{Resource}Repository` | `IOrderRepository` |
| Driven Port (出站) | `I{Resource}Gateway` | `IPaymentGateway` |
| Driven Port (出站) | `I{Resource}Service` | `INotificationService` |

## 端口粒度原则

- 入站端口：一个 UseCase 一个接口
- 出站端口：一个外部依赖一个接口
- 不要为"未来可能"创建端口——等实际需要时再抽
- 小项目可以直接用 UseCase handler 的 public 方法作为 driver port，不需要单独的接口

## 关键规则

1. 端口在领域层/应用层定义，适配器在基础设施层实现
2. 所有依赖指向核心：Infrastructure → Application → Domain
3. 入站适配器把 HTTP 请求转为端口调用
4. 出站适配器实现仓储/网关接口
5. 领域层零框架依赖——"Create your application to work without either a UI or a database"
