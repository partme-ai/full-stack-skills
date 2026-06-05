# 领域事件处理示例

> 展示整洁架构中领域事件的定义、发布与消费的完整实现。

## 1. Enterprise 层 — 领域事件定义

```java
// core/event/DomainEvent.java — 抽象基类（零框架依赖）
public abstract class DomainEvent {
    private final String eventId;
    private final String aggregateId;
    private final Instant occurredOn;

    protected DomainEvent(String aggregateId) {
        this.eventId = UUID.randomUUID().toString();
        this.aggregateId = aggregateId;
        this.occurredOn = Instant.now();
    }

    public String getEventId() { return eventId; }
    public String getAggregateId() { return aggregateId; }
    public Instant getOccurredOn() { return occurredOn; }
}

// core/event/OrderCreatedEvent.java
public class OrderCreatedEvent extends DomainEvent {
    private final OrderId orderId;
    private final Money totalAmount;
    private final List<OrderItem> items;

    public OrderCreatedEvent(Order order) {
        super(order.getId().getValue());
        this.orderId = order.getId();
        this.totalAmount = order.getTotalAmount();
        this.items = new ArrayList<>(order.getItems());
    }

    public OrderId getOrderId() { return orderId; }
    public Money getTotalAmount() { return totalAmount; }
    public List<OrderItem> getItems() { return items; }
}

// core/event/OrderPaidEvent.java
public class OrderPaidEvent extends DomainEvent {
    private final OrderId orderId;
    private final Money paidAmount;

    public OrderPaidEvent(Order order) {
        super(order.getId().getValue());
        this.orderId = order.getId();
        this.paidAmount = order.getPaidAmount();
    }
}
```

## 2. UseCase 层 — 事件发布端口

```java
// usecase/port/output/EventPublisher.java
public interface EventPublisher {
    void publish(DomainEvent event);
}

// usecase/port/output/EventBus.java — 批量发布（性能优化）
public interface EventBus {
    void publishAll(List<DomainEvent> events);
}
```

## 3. Enterprise 层 — 实体中产生事件

```java
// core/entity/Order.java
public class Order {
    private OrderId id;
    private OrderStatus status;
    private List<DomainEvent> domainEvents = new ArrayList<>();

    // 公有工厂方法（非公开构造函数）
    public static Order create(OrderId id, CustomerId customerId, List<OrderItem> items) {
        Order order = new Order(id, customerId, items);
        order.status = OrderStatus.CREATED;
        order.addDomainEvent(new OrderCreatedEvent(order));
        return order;
    }

    public void pay(Money amount) {
        if (status != OrderStatus.CREATED) {
            throw new OrderDomainException("只有 CREATED 状态的订单可以支付");
        }
        this.paidAmount = amount;
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this));
    }

    // 内部收集事件，Interactor 通过 drain 获取
    private void addDomainEvent(DomainEvent event) {
        this.domainEvents.add(event);
    }

    public List<DomainEvent> drainEvents() {
        var events = List.copyOf(this.domainEvents);
        this.domainEvents.clear();
        return events;
    }
}
```

## 4. UseCase 层 — Interactor 发布事件

```java
// usecase/interactor/PayOrderInteractor.java
public class PayOrderInteractor implements PayOrderUseCase {
    private final OrderRepository orderRepository;
    private final EventPublisher eventPublisher;

    public PayOrderInteractor(OrderRepository orderRepository, EventPublisher eventPublisher) {
        this.orderRepository = orderRepository;
        this.eventPublisher = eventPublisher;
    }

    @Override
    public PayOrderOutput execute(PayOrderInput input) {
        // 1. 加载实体
        Order order = orderRepository.findById(new OrderId(input.getOrderId()))
            .orElseThrow(() -> new OrderDomainException("订单不存在"));

        // 2. 执行业务方法（内部产生事件）
        order.pay(new Money(input.getAmount()));

        // 3. 持久化
        orderRepository.save(order);

        // 4. 发布领域事件（Interactor 只编排不处理事件）
        order.drainEvents().forEach(eventPublisher::publish);

        // 5. 返回 DTO
        return new PayOrderOutput(order.getId().getValue(), order.getStatus().name());
    }
}
```

## 5. Adapter 层 — 事件发布实现

```java
// adapter/event/RabbitMqEventPublisher.java
@Component
public class RabbitMqEventPublisher implements EventPublisher {
    @Autowired
    private RabbitTemplate rabbitTemplate;

    @Override
    public void publish(DomainEvent event) {
        // 同步发布到消息队列
        String routingKey = event.getClass().getSimpleName();
        rabbitTemplate.convertAndSend("domain-events", routingKey, event);
    }
}

// adapter/event/InMemoryEventPublisher.java — 测试用
public class InMemoryEventPublisher implements EventPublisher {
    private final List<DomainEvent> publishedEvents = new ArrayList<>();

    @Override
    public void publish(DomainEvent event) {
        publishedEvents.add(event);
    }

    public List<DomainEvent> getPublishedEvents() { return List.copyOf(publishedEvents); }
    public void clear() { publishedEvents.clear(); }
}
```

## 6. 事件消费（在 Adapter 层）

```java
// adapter/listener/OrderEventListener.java
@Component
public class OrderEventListener {
    private final PaymentGateway paymentGateway;
    private final NotificationService notificationService;

    @EventListener
    public void handleOrderPaid(OrderPaidEvent event) {
        // 异步处理：发发票、通知仓库、更新物流
        notificationService.sendOrderConfirmation(event.getOrderId());
    }
}
```

## 验证要点

- **依赖规则**：EventPublisher 接口在 UseCase 层，实现类在 Adapter 层
- **实体不依赖事件基础设施**：Entity 只用 `List<DomainEvent>` 收集，不 import 任何消息中间件
- **Interactor 不处理事件**：只负责 drain 和 publish，具体处理在 Adapter 层
- **Drain 模式**：Entity 的 drainEvents() 在持久化后调用，确保不丢失事件
- **可测试性**：InMemoryEventPublisher 让单元测试零依赖
