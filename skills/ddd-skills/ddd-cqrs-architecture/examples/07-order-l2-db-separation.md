# L2 数据库分离完整示例 — 事件同步

> 所属级别: L2（数据库分离） | Command DB + Query DB | 领域事件同步

## 业务场景

订单支付 → 发布 OrderPaidEvent → 异步同步到 Elasticsearch 查询库

## 架构图

```
POST /orders/{id}/pay
       ↓
OrderCommandService
       ↓
Order.pay() → OrderPaidEvent → Outbox 表
       ↓
 Outbox Poller / CDC
       ↓
    MQ (Kafka/RabbitMQ)
       ↓
OrderPaidEventHandler → ES / Read DB
       ↓
OrderQueryService ← Elasticsearch / Read DB
```

## 写侧

### 领域事件

```java
public class OrderPaidEvent extends DomainEvent {
    private final String orderId;
    private final BigDecimal totalAmount;
    private final LocalDateTime paidAt;

    public OrderPaidEvent(String orderId, BigDecimal totalAmount) {
        super(orderId);
        this.orderId = orderId;
        this.totalAmount = totalAmount;
        this.paidAt = LocalDateTime.now();
    }
}
```

### 聚合行为

```java
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;

    public void pay() {
        if (this.status != OrderStatus.PENDING_PAYMENT) {
            throw new OrderException("订单状态不可支付: " + this.status);
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id.getValue(), this.totalAmount));
    }
}
```

### Outbox 写入（同一事务）

```java
@Service
public class OrderCommandService {
    private final OrderRepository orderRepository;
    private final OutboxRepository outboxRepository;

    @Transactional
    public void payOrder(PayOrderCommand command) {
        Order order = orderRepository.findById(new OrderId(command.getOrderId()))
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));
        order.pay();
        orderRepository.save(order);
        // 领域事件由仓储自动写入 outbox 表（同一事务）
    }
}
```

## 读侧

### 事件处理器 → 写查询库

```java
@Component
public class OrderPaidEventHandler {
    private final OrderReadRepository readRepo;

    @Async
    @Transactional
    public void handleOrderPaidEvent(OrderPaidEvent event) {
        // 幂等检查
        if (readRepo.existsById(event.getOrderId())) {
            return;  // 已处理
        }
        OrderDocument doc = new OrderDocument();
        doc.setOrderId(event.getOrderId());
        doc.setStatus("PAID");
        doc.setTotalAmount(event.getTotalAmount());
        doc.setPaidAt(event.getPaidAt());
        doc.setUpdatedAt(LocalDateTime.now());
        readRepo.save(doc);
    }
}
```

### 查询服务

```java
@Service
public class OrderQueryService {
    private final OrderReadRepository readRepo;
    private final ElasticsearchRestTemplate esTemplate;

    public OrderDocument getOrder(String orderId) {
        return readRepo.findById(orderId)
            .orElseThrow(() -> new OrderNotFoundException(orderId));
    }

    public Page<OrderDocument> search(OrderSearchQuery query, Pageable pageable) {
        NativeSearchQuery searchQuery = new NativeSearchQueryBuilder()
            .withQuery(QueryBuilders.boolQuery()
                .filter(QueryBuilders.termQuery("customerId", query.getCustomerId()))
                .filter(QueryBuilders.rangeQuery("paidAt")
                    .gte(query.getStartDate()).lte(query.getEndDate())))
            .withPageable(pageable)
            .build();
        return esTemplate.search(searchQuery, OrderDocument.class)
            .map(SearchHit::getContent);
    }
}
```

## 同步延迟监控

```java
@Component
public class SyncLagMonitor {
    private final JdbcTemplate writeDb;
    private final JdbcTemplate readDb;

    @Scheduled(fixedRate = 60000)
    public void checkSyncLag() {
        // 对比写库最新事件时间和读库最新记录时间
        Instant latestWrite = writeDb.queryForObject(
            "SELECT MAX(occurred_at) FROM domain_event_outbox", Instant.class);
        Instant latestRead = readDb.queryForObject(
            "SELECT MAX(updated_at) FROM order_projection", Instant.class);
        Duration lag = Duration.between(latestRead, latestWrite);
        if (lag.getSeconds() > 30) {
            // 告警：同步延迟超过 30 秒
        }
    }
}
```

## 适用场景

- 读负载大，需要独立的查询优化策略
- Command DB (MySQL/PostgreSQL) + Query DB (Elasticsearch/MongoDB)
- 可以接受秒级最终一致性
- 需要复杂的搜索功能（全文检索、聚合统计）
