# 领域事件 vs 集成事件 + 事件分发器模式

## 领域事件（Domain Events）

- 限于界上下文内部
- 细粒度、底层
- 触发内部流程
- 用领域语言命名

```java
public class OrderItemQuantityIncreased extends DomainEvent {
    private final OrderId orderId;
    private final ProductId productId;
    private final int oldQuantity;
    private final int newQuantity;

    public OrderItemQuantityIncreased(OrderId orderId, ProductId productId,
            int oldQuantity, int newQuantity) {
        super(orderId.getValue());
        this.orderId = orderId;
        this.productId = productId;
        this.oldQuantity = oldQuantity;
        this.newQuantity = newQuantity;
    }
}
```

## 集成事件（Integration Events）

- 跨限界上下文
- 粗粒度
- 发布到消息中间件
- 版本化 schema

```java
public class OrderConfirmedIntegrationEvent {
    private final String eventType = "sales.order.confirmed";
    private final String eventId;
    private final String version = "1.0";
    private final Instant occurredAt;
    private final OrderConfirmedPayload payload;

    public static OrderConfirmedIntegrationEvent from(Order order) {
        return new OrderConfirmedIntegrationEvent(
            UUID.randomUUID().toString(), Instant.now(),
            new OrderConfirmedPayload(
                order.getId().getValue(),
                order.getCustomerId().getValue(),
                order.getTotal(),
                order.getItems(),
                order.getShippingAddress()
            )
        );
    }
}
```

## 发布集成事件

```java
@Component
public class PublishOrderConfirmedIntegrationEvent {
    private final MessageBroker broker;
    private final OrderRepository orderRepo;

    @EventListener
    public void handle(OrderConfirmed domainEvent) {
        Order order = orderRepo.findById(domainEvent.getOrderId()).orElse(null);
        if (order == null) return;

        var integrationEvent = OrderConfirmedIntegrationEvent.from(order);
        broker.publish("order-events", integrationEvent);
    }
}
```

## 事件分发器（Event Dispatcher）模式

```java
public class EventDispatcher {
    private final Map<String, List<EventHandler<?>>> handlers = new HashMap<>();

    public <T extends DomainEvent> void register(String eventType, EventHandler<T> handler) {
        handlers.computeIfAbsent(eventType, k -> new ArrayList<>()).add(handler);
    }

    public void dispatch(DomainEvent event) {
        handlers.getOrDefault(event.getEventType(), List.of())
            .forEach(h -> h.handle(event));
    }

    public void dispatchAll(List<DomainEvent> events) {
        events.forEach(this::dispatch);
    }
}

// 注册
var dispatcher = new EventDispatcher();
dispatcher.register("order.created", new OrderCreatedHandler());
dispatcher.register("order.confirmed", new OrderConfirmedHandler());
dispatcher.register("order.confirmed", new PublishOrderConfirmedIntegrationEvent(broker, repo));
dispatcher.register("order.shipped", new SendShippingNotificationHandler(repo, notifier));
```

## 事件流全貌

```
领域行为（同一事务）
  → 写业务数据
  → 在聚合上 addDomainEvent()
  → 事务提交后 EventDispatcher.dispatchAll(events)
       ├── 内部 Handler（同一进程，同步）
       └── 集成事件发布器 → MQ（异步）
```

## 领域事件 vs 集成事件对照

| 维度 | 领域事件 | 集成事件 |
|------|---------|---------|
| 范围 | 限界上下文内 | 跨限界上下文 |
| 粒度 | 细粒度 | 粗粒度 |
| 传输 | 进程内 EventBus/Spring Events | MQ（Kafka/RabbitMQ） |
| Schema | 内部约定 | 版本化 + 向后兼容 |
| 命名 | OrderItemAdded | sales.order.confirmed |
