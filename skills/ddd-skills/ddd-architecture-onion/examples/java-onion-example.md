# 洋葱架构 — Java 代码示例


## Domain 层（核心，零依赖）

```java
// core/domain/model/Order.java
public class Order extends AggregateRoot<OrderId> {
    private Money totalAmount;
    private List<OrderItem> items;
    private OrderStatus status;

    public void pay(PaymentGateway gateway) {
        if (!status.canPay()) throw new OrderException("不可支付");
        gateway.charge(this.totalAmount);
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}

// core/domain/repository/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
}
```

## Infrastructure 层（实现接口）

```java
// infrastructure/data/repository/OrderRepositoryImpl.java
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    private final JpaOrderRepository jpaRepo;
    private final OrderMapper mapper;  // PO ↔ Domain

    @Override public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }
    @Override public void save(Order order) {
        jpaRepo.save(mapper.toPO(order));
    }
}
```

## Application 层（编排）

```java
// core/application/service/OrderApplicationService.java
public class OrderApplicationService {
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;

    @Transactional
    public OrderDTO payOrder(String orderId) {
        Order order = orderRepository.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        order.pay(paymentGateway);              // 领域逻辑
        orderRepository.save(order);            // 出站端口
        return OrderAssembler.toDTO(order);
    }
}
```

## API 层（薄适配器）

```java
// api/controller/OrderController.java
@RestController
public class OrderController {
    private final OrderApplicationService appService;

    @PostMapping("/orders/{id}/pay")
    public Result<OrderDTO> pay(@PathVariable String id) {
        return Result.success(appService.payOrder(id));
    }
}
```

## DI 组装

```java
// composition/config/OrderModuleConfig.java
@Configuration
public class OrderModuleConfig {
    @Bean public OrderRepository orderRepository(JpaOrderRepository jpa, OrderMapper m) {
        return new OrderRepositoryImpl(jpa, m);
    }
    @Bean public OrderApplicationService orderAppService(OrderRepository repo, PaymentGateway gw) {
        return new OrderApplicationService(repo, gw);
    }
}
```

## 关键规则

- 内层定义接口（Domain），外层实现接口（Infrastructure）
- 依赖永远指向圆心（Domain）
- Domain 层零 Spring/JPA/MyBatis 依赖
