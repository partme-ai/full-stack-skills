# 02 — Application Layer: Interfaces & Orchestration

> 应用层（Application Layer）位于 Domain 外围，负责用例编排、事务管理、跨聚合协调。

## 职责

- 定义应用服务接口（契约）
- 实现应用服务（编排领域对象，不包含业务逻辑）
- 管理事务边界（`@Transactional`）
- 发布领域事件
- 调用外部微服务

## 核心原则

```
Domain 层：业务逻辑（if/else，规则校验）
Application 层：编排逻辑（先调 A，再调 B，最后调 C）
              — 不包含业务逻辑判断
```

## 代码模板

### Application Service Interface（应用服务接口）

```java
// core/application/service/OrderApplicationService.java
public interface OrderApplicationService {
    OrderDTO createOrder(CreateOrderCommand command);
    void payOrder(PayOrderCommand command);
    void cancelOrder(CancelOrderCommand command);
    OrderDTO getOrder(String orderId);
}
```

### Application Service Implementation（应用服务实现）

```java
// core/application/service/OrderApplicationServiceImpl.java
public class OrderApplicationServiceImpl implements OrderApplicationService {
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;
    private final OrderAssembler orderAssembler;

    public OrderApplicationServiceImpl(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher,
            OrderAssembler orderAssembler) {
        this.orderRepository = orderRepository;
        this.paymentGateway = paymentGateway;
        this.eventPublisher = eventPublisher;
        this.orderAssembler = orderAssembler;
    }

    @Override
    @Transactional
    public OrderDTO createOrder(CreateOrderCommand command) {
        // 1. 创建领域对象
        OrderId orderId = OrderId.generate();
        Order order = Order.create(orderId, new CustomerId(command.getCustomerId()));

        // 2. 添加商品（调用 Domain 方法）
        for (CreateOrderCommand.Item item : command.getItems()) {
            order.addItem(
                new ProductId(item.getProductId()),
                Money.of(item.getUnitPrice(), "CNY"),
                item.getQuantity()
            );
        }

        // 3. 提交订单（调用 Domain 方法）
        order.submit();

        // 4. 持久化
        orderRepository.save(order);

        // 5. 发布领域事件
        order.getDomainEvents().forEach(eventPublisher::publish);

        // 6. 返回 DTO（不暴露 Domain 对象）
        return orderAssembler.toDTO(order);
    }

    @Override
    @Transactional
    public void payOrder(PayOrderCommand command) {
        Order order = orderRepository.findById(new OrderId(command.getOrderId()))
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));

        // 调用 Domain 层的支付方法（含业务规则）
        order.pay(paymentGateway);
        orderRepository.save(order);
        order.getDomainEvents().forEach(eventPublisher::publish);
    }

    @Override
    @Transactional
    public void cancelOrder(CancelOrderCommand command) {
        Order order = orderRepository.findById(new OrderId(command.getOrderId()))
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));
        order.cancel();
        orderRepository.save(order);
        order.getDomainEvents().forEach(eventPublisher::publish);
    }

    @Override
    @Transactional(readOnly = true)
    public OrderDTO getOrder(String orderId) {
        Order order = orderRepository.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        return orderAssembler.toDTO(order);
    }
}
```

### Command / DTO（命令对象）

```java
// core/application/dto/CreateOrderCommand.java
public class CreateOrderCommand {
    private String customerId;
    private List<Item> items;

    public static class Item {
        private String productId;
        private BigDecimal unitPrice;
        private int quantity;
        // getter/setter...
    }
    // getter/setter...
}

// core/application/dto/OrderDTO.java
public class OrderDTO {
    private String orderId;
    private String customerId;
    private String status;
    private List<OrderItemDTO> items;
    private BigDecimal totalAmount;
    private LocalDateTime createdAt;
    // getter/setter...
}
```

### Event Publisher Interface（事件发布接口）

```java
// core/application/event/EventPublisher.java
public interface EventPublisher {
    void publish(DomainEvent event);
    void publishAll(List<DomainEvent> events);
}
```

## 规范检查清单

- [ ] Application Service 不含 if/else 业务逻辑
- [ ] 事务注解在 Application 层
- [ ] 返回值是 DTO，不暴露 Domain 实体
- [ ] 所有依赖通过构造器注入
- [ ] 跨聚合操作通过 Application 编排
- [ ] 领域事件在事务提交后发布
