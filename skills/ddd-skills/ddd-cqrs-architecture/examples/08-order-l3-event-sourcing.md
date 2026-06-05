# L3 Event Sourcing 完整示例

> 所属级别: L3（Event Sourcing） | EventStore + Projection | 完整审计追踪

## 业务场景

订单创建 → 支付 → 发货 → 完成 — 以事件流作为唯一真相源

## 架构图

```
Command → Aggregate → EventStream → EventStore (Append-Only)
                                           ↓
                                     ┌─────┴─────┐
                                     ↓           ↓
                               Projector A  Projector B
                                     ↓           ↓
                             OrderView    OrderSearch
                             (MySQL)      (ES)
```

## Event Store

```java
public interface EventStore {
    void appendEvents(
        String aggregateId,
        List<DomainEvent> events,
        int expectedVersion
    );
    List<DomainEvent> loadEvents(String aggregateId);
    List<DomainEvent> loadEventsByType(
        String eventType,
        LocalDateTime since
    );
}

@Repository
public class JdbcEventStore implements EventStore {
    private final JdbcTemplate jdbc;
    private final ObjectMapper objectMapper;

    @Override
    public void appendEvents(
            String aggregateId,
            List<DomainEvent> events,
            int expectedVersion) {
        for (DomainEvent event : events) {
            int inserted = jdbc.update("""
                INSERT INTO events (event_id, aggregate_id, aggregate_type,
                    event_type, event_data, version, occurred_at)
                SELECT ?, ?, ?, ?, ?, ?, ?
                WHERE (SELECT MAX(version) FROM events
                       WHERE aggregate_id = ?) = ?
                """,
                event.getEventId(), aggregateId, "Order",
                event.getClass().getSimpleName(),
                toJson(event), expectedVersion + 1, event.getOccurredAt(),
                aggregateId, expectedVersion
            );
            if (inserted == 0) {
                throw new ConcurrencyConflictException(aggregateId, expectedVersion);
            }
        }
    }

    @Override
    public List<DomainEvent> loadEvents(String aggregateId) {
        return jdbc.query("""
            SELECT * FROM events
            WHERE aggregate_id = ?
            ORDER BY version ASC
            """,
            new EventRowMapper(), aggregateId
        );
    }
}
```

## Event-Sourced Aggregate

```java
public abstract class EventSourcedAggregate {
    private String id;
    private int version;
    private final List<DomainEvent> pendingEvents = new ArrayList<>();

    protected void apply(DomainEvent event) {
        pendingEvents.add(event);
        when(event);     // 应用事件改变状态
    }

    protected abstract void when(DomainEvent event);

    public void loadFromHistory(List<DomainEvent> events) {
        events.forEach(e -> {
            when(e);
            this.version = e.getVersion();
        });
    }

    public List<DomainEvent> getPendingEvents() {
        return Collections.unmodifiableList(pendingEvents);
    }

    public int getVersion() { return version; }
    public String getId() { return id; }
}

public class Order extends EventSourcedAggregate {
    private OrderStatus status;
    private Money totalAmount;
    private CustomerId customerId;

    public static Order create(CreateOrderCommand cmd) {
        Order order = new Order();
        order.apply(new OrderCreatedEvent(
            UUID.randomUUID().toString(), cmd.getCustomerId(), cmd.getItems()));
        return order;
    }

    public void pay() {
        apply(new OrderPaidEvent(this.id));
    }

    public void ship(TrackingNumber tracking) {
        if (status != OrderStatus.PAID) {
            throw new OrderException("已支付才能发货");
        }
        apply(new OrderShippedEvent(this.id, tracking));
    }

    @Override
    protected void when(DomainEvent event) {
        if (event instanceof OrderCreatedEvent e) {
            this.id = e.getAggregateId();
            this.status = OrderStatus.CREATED;
            this.customerId = new CustomerId(e.getCustomerId());
        } else if (event instanceof OrderPaidEvent) {
            this.status = OrderStatus.PAID;
        } else if (event instanceof OrderShippedEvent) {
            this.status = OrderStatus.SHIPPED;
        }
    }
}
```

## Command Handler

```java
@Service
public class OrderCommandHandler {
    private final EventStore eventStore;

    @Transactional
    public void handlePayOrder(PayOrderCommand command) {
        List<DomainEvent> events = eventStore.loadEvents(command.getOrderId());
        Order order = new Order();
        order.loadFromHistory(events);
        order.pay();
        eventStore.appendEvents(
            command.getOrderId(),
            order.getPendingEvents(),
            order.getVersion()
        );
    }
}
```

## Projection

```java
@Component
public class OrderProjection {
    private final JdbcTemplate jdbc;

    @EventListener
    public void onOrderCreated(OrderCreatedEvent event) {
        jdbc.update("""
            INSERT INTO order_projection
                (order_id, status, customer_id, total_amount, created_at)
            VALUES (?, 'CREATED', ?, ?, ?)
            """,
            event.getAggregateId(), event.getCustomerId(),
            event.getTotalAmount(), event.getOccurredAt());
    }

    @EventListener
    public void onOrderPaid(OrderPaidEvent event) {
        jdbc.update(
            "UPDATE order_projection SET status = 'PAID', paid_at = ? WHERE order_id = ?",
            event.getOccurredAt(), event.getAggregateId());
    }

    @EventListener
    public void onOrderShipped(OrderShippedEvent event) {
        jdbc.update(
            "UPDATE order_projection SET status = 'SHIPPED', tracking_no = ? WHERE order_id = ?",
            event.getTrackingNumber().getValue(), event.getAggregateId());
    }
}
```

## Snapshot 策略

```java
@Component
public class OrderSnapshotter {
    private final EventStore eventStore;
    private final JdbcTemplate jdbc;

    // 每 100 个事件创建快照
    private static final int SNAPSHOT_INTERVAL = 100;

    @Scheduled(fixedRate = 3600000)
    public void createSnapshot(String aggregateId) {
        List<DomainEvent> events = eventStore.loadEvents(aggregateId);
        if (events.size() % SNAPSHOT_INTERVAL == 0) {
            Order order = new Order();
            order.loadFromHistory(events);
            jdbc.update("""
                INSERT INTO aggregate_snapshots
                    (aggregate_id, aggregate_type, snapshot_data, version, created_at)
                VALUES (?, 'Order', ?, ?, ?)
                """,
                aggregateId, serialize(order), order.getVersion(), Instant.now());
        }
    }
}
```

## Events DDL

```sql
CREATE TABLE events (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_id        VARCHAR(36) NOT NULL UNIQUE,
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_data      JSON NOT NULL,
    version         INT NOT NULL,
    occurred_at     DATETIME NOT NULL,
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_aggregate_version (aggregate_id, version),
    INDEX idx_events_type_time (event_type, occurred_at)
);

CREATE TABLE aggregate_snapshots (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    snapshot_data   JSON NOT NULL,
    version         INT NOT NULL,
    created_at      DATETIME NOT NULL,
    INDEX idx_snapshot_aggregate (aggregate_id, version)
);
```

## 适用场景

- 需要完整审计追踪（金融、合规）
- 时间旅行查询（"某时间点的状态是什么"）
- 事件重放（从零重建系统状态）
- 事件驱动分析（事件流 → 数据分析）
