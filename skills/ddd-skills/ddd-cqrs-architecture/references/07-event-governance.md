# 事件驱动工程化治理

> 整合自原 `ddd-eventing-governance` 技能，覆盖 Outbox、幂等、重试死信、补偿对账、事件契约与可观测性。

## 1. 事件处理闭环

```
领域行为（同一事务）
  → 写业务数据
  → 写 Outbox 事件表
    → 发布器投递（至少一次）
      → 消费者落库去重（幂等）
        → 执行业务处理
          → 失败：重试/死信/补偿/对账
```

## 2. Outbox 方案

### 2.1 Outbox 表 DDL

```sql
-- PostgreSQL
CREATE TABLE domain_event_outbox (
    id              VARCHAR(36) PRIMARY KEY,
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_data      JSONB NOT NULL,
    schema_version  INTEGER NOT NULL DEFAULT 1,
    occurred_at     TIMESTAMP NOT NULL,
    published       BOOLEAN NOT NULL DEFAULT FALSE,
    published_at    TIMESTAMP,
    retry_count     INTEGER NOT NULL DEFAULT 0,
    last_error      TEXT,
    correlation_id  VARCHAR(36),
    trace_id        VARCHAR(36),
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),

    INDEX idx_outbox_published (published, created_at),
    INDEX idx_outbox_aggregate (aggregate_id),
    INDEX idx_outbox_type (event_type, occurred_at)
);
```

```sql
-- MySQL
CREATE TABLE domain_event_outbox (
    id              VARCHAR(36) NOT NULL,
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_data      JSON NOT NULL,
    schema_version  INT NOT NULL DEFAULT 1,
    occurred_at     DATETIME NOT NULL,
    published       TINYINT NOT NULL DEFAULT 0,
    published_at    DATETIME,
    retry_count     INT NOT NULL DEFAULT 0,
    last_error      TEXT,
    correlation_id  VARCHAR(36),
    trace_id        VARCHAR(36),
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    INDEX idx_outbox_published (published, created_at),
    INDEX idx_outbox_aggregate (aggregate_id)
);
```

### 2.2 发布策略对比

| 策略 | 机制 | 延迟 | 复杂度 | 适用场景 |
|------|------|:--:|:--:|---------|
| **轮询发布** | 定时任务扫 Outbox 表 | 1-5s | 低 | 中小流量，简单可靠 |
| **CDC (Debezium)** | 监听 binlog/WAL 变更 | < 100ms | 中 | 高流量，低延迟要求 |
| **事务提交后回调** | TransactionSynchronization | < 10ms | 低 | Spring 项目首选 |

### 2.3 轮询发布器实现

```java
@Component
public class OutboxPublisher {
    private final DomainEventOutboxMapper outboxMapper;
    private final ApplicationEventPublisher eventPublisher;
    private final int BATCH_SIZE = 100;
    private final int MAX_RETRY = 5;

    @Scheduled(fixedDelay = 2000)
    public void publishUnpublishedEvents() {
        List<EventOutboxRecord> records = outboxMapper
            .findUnpublished(BATCH_SIZE);

        for (EventOutboxRecord record : records) {
            try {
                DomainEvent event = deserialize(record);
                eventPublisher.publishEvent(event);
                outboxMapper.markPublished(record.getId());
            } catch (Exception e) {
                handlePublishFailure(record, e);
            }
        }
    }

    private void handlePublishFailure(EventOutboxRecord record, Exception e) {
        if (record.getRetryCount() >= MAX_RETRY) {
            outboxMapper.markDead(record.getId(), e.getMessage());
            alertDeadLetter(record);
        } else {
            outboxMapper.incrementRetry(record.getId(), e.getMessage());
        }
    }
}
```

### 2.4 事务中写入 Outbox（同一事务保证）

```java
@Service
public class OrderApplicationService {
    private final OrderRepository orderRepository;
    private final DomainEventOutboxMapper outboxMapper;

    @Transactional
    public void payOrder(PayOrderCommand cmd) {
        // 1. 执行业务操作
        Order order = orderRepository.findById(cmd.getOrderId()).orElseThrow();
        order.pay();

        // 2. 提取领域事件
        List<DomainEvent> events = order.getDomainEvents();

        // 3. 持久化聚合（业务数据）
        orderRepository.save(order);

        // 4. 同一事务写入 Outbox
        for (DomainEvent event : events) {
            EventOutboxRecord record = EventOutboxRecord.from(event);
            outboxMapper.insert(record);
        }
    }
}
```

## 3. 幂等策略

### 3.1 消费幂等表 DDL

```sql
-- PostgreSQL
CREATE TABLE event_consumption_record (
    event_id        VARCHAR(36) NOT NULL,
    consumer_group  VARCHAR(100) NOT NULL,
    consumed_at     TIMESTAMP NOT NULL DEFAULT NOW(),
    status          VARCHAR(20) NOT NULL DEFAULT 'PROCESSED',
    PRIMARY KEY (event_id, consumer_group)
);
```

```sql
-- MySQL
CREATE TABLE event_consumption_record (
    event_id        VARCHAR(36) NOT NULL,
    consumer_group  VARCHAR(100) NOT NULL,
    consumed_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status          VARCHAR(20) NOT NULL DEFAULT 'PROCESSED',
    PRIMARY KEY (event_id, consumer_group)
);
```

### 3.2 幂等消费模板

```java
@Component
public class IdempotentEventHandler {
    private final EventConsumptionRecordMapper recordMapper;

    @EventListener
    @Transactional
    public void handleOrderPaid(OrderPaidEvent event) {
        String eventId = event.getEventId();

        // 幂等检查：数据库唯一约束防重
        if (recordMapper.exists(eventId, "order-consumer")) {
            log.info("Duplicate event ignored: {}", eventId);
            return;
        }

        try {
            // 执行业务处理
            doHandleOrderPaid(event);

            // 记录消费
            recordMapper.insert(eventId, "order-consumer", "PROCESSED");

        } catch (Exception e) {
            // 记录失败（不阻挡重试）
            recordMapper.insert(eventId, "order-consumer", "FAILED_RETRY");
            throw e;
        }
    }
}
```

### 3.3 策略对比

| 策略 | 机制 | 可靠性 | 性能 | 适用 |
|------|------|:--:|:--:|------|
| **事件表 + 唯一约束** | DB UNIQUE(event_id, consumer) | ★★★ | ★★☆ | 金融、订单等关键业务 |
| **状态机Guard** | if alreadyPaid() return | ★★★ | ★★★ | 状态驱动的业务 |
| **Redis SETNX + TTL** | SETNX event:xxx EX 3600 | ★★☆ | ★★★ | 非关键通知 |
| **业务幂等** | UPDATE stock=stock-1 WHERE stock>=1 | ★★★ | ★★★ | 简单原子操作 |

## 4. 重试与死信策略

### 4.1 重试策略配置

| 参数 | 默认值 | 说明 |
|------|:--:|------|
| 最大重试次数 | 3 | 超过则进入死信 |
| 初始退避 | 1s | 首次重试延迟 |
| 退避倍数 | 2 | 指数退避：1s → 2s → 4s |
| 最大退避 | 60s | 退避上限 |
| 最大重试时长 | 5min | 超时则标记失败 |
| 死信告警 | 是 | 进入死信立即告警 |

### 4.2 死信策略

```
死信处理流程：
  消费失败 → 重试耗尽 → 写入死信表/死信队列
    → 钉钉/飞书/邮件告警
      → 人工排查（对账工具查询 eventId 全链路）
        → 修复后手动重放 或 标记为跳过

死信表 DDL：
  CREATE TABLE event_dead_letter (
      id VARCHAR(36) PRIMARY KEY,
      event_id VARCHAR(36) NOT NULL,
      event_type VARCHAR(200),
      consumer_group VARCHAR(100),
      error_message TEXT,
      error_stack TEXT,
      retry_count INT,
      dead_at TIMESTAMP DEFAULT NOW(),
      status VARCHAR(20) DEFAULT 'PENDING',  -- PENDING/RESOLVED/SKIPPED
      resolved_at TIMESTAMP,
      resolved_by VARCHAR(100),
      INDEX idx_dlq_status (status, dead_at)
  );
```

### 4.3 对账机制

```java
@Component
public class EventReconciliationJob {
    private final OutboxMapper outboxMapper;
    private final ConsumptionRecordMapper consumptionMapper;
    private final DeadLetterMapper deadLetterMapper;

    @Scheduled(cron = "0 0 3 * * ?")  // 每天凌晨3点
    public void reconcile() {
        // 1. 扫描超过24小时未发布的事件
        List<EventOutboxRecord> stuckEvents = outboxMapper
            .findStuckEvents(Duration.ofHours(24));

        // 2. 扫描已发布但无消费记录的事件
        List<EventOutboxRecord> unconsumedEvents = outboxMapper
            .findPublishedButNotConsumed();

        // 3. 生成对账报告
        ReconciliationReport report = ReconciliationReport.builder()
            .stuckPublishEvents(stuckEvents)
            .unconsumedEvents(unconsumedEvents)
            .deadLetterCount(deadLetterMapper.countPending())
            .build();

        // 4. 差异自动修复（安全操作）
        for (EventOutboxRecord event : stuckEvents) {
            if (event.getRetryCount() < 10) {
                outboxMapper.resetForRetry(event.getId());
            }
        }

        // 5. 发送对账报告
        alertService.sendReconciliationReport(report);
    }
}
```

## 5. 事件契约与版本策略

### 5.1 事件契约字段规范

每个领域事件必须包含以下字段：

```json
{
  "eventId": "uuid",
  "eventType": "OrderPaid",
  "aggregateId": "ORD-2024-001",
  "aggregateType": "Order",
  "occurredAt": "2024-03-15T10:30:00Z",
  "schemaVersion": 2,
  "correlationId": "corr-xxx",
  "traceId": "trace-xxx",
  "payload": {
    "orderId": "ORD-2024-001",
    "customerId": "CUS-001",
    "totalAmount": { "amount": "99.00", "currency": "CNY" },
    "items": [...]
  }
}
```

### 5.2 版本兼容策略

| 策略 | 做法 | 适用 |
|------|------|------|
| **只增字段** | 新增字段设默认值，旧消费者忽略新字段 | 兼容升级 |
| **升级主版本** | 破坏性变更发布到新 topic，旧 topic 保留 | API 签名变化 |
| **双写过渡** | 同时发布 v1 和 v2，待消费者升级后下线 v1 | 平滑迁移 |

### 5.3 版本降级处理

```java
// 消费者兼容多版本
@EventHandler
public void on(OrderPaidEventV2 event) {
    // V2 fields
    String paymentMethod = event.getPaymentMethod();  // V2 新增

    // Legacy V1 fields still work
    Money amount = event.getTotalAmount();
}
```

## 6. 可观测性

### 6.1 追踪传播

```java
// 生产者端：传递 traceId + correlationId
public class EventOutboxRecord {
    public static EventOutboxRecord from(DomainEvent event) {
        return EventOutboxRecord.builder()
            .traceId(MDC.get("traceId"))         // 当前请求 traceId
            .correlationId(UUID.randomUUID().toString())
            .build();
    }
}

// 消费者端：恢复上下文
@EventListener
public void handle(DomainEvent event) {
    MDC.put("traceId", event.getTraceId());
    MDC.put("correlationId", event.getCorrelationId());
    try {
        doHandle(event);
    } finally {
        MDC.clear();
    }
}
```

### 6.2 关键指标

| 指标 | 说明 | 告警阈值 |
|------|------|:--:|
| `events.published.rate` | 事件发布速率 | — |
| `events.publish.failures` | 发布失败数 | > 10/min |
| `events.consumed.rate` | 消费速率 | — |
| `events.consume.failures` | 消费失败数 | > 5/min |
| `events.dead_letter.count` | 死信积压数 | > 0 |
| `events.lag.seconds` | 端到端延迟 p95 | > 60s |
| `outbox.stuck.count` | 超过5分钟未发布事件 | > 0 |

### 6.3 事件全链路查询

```sql
-- 按 eventId 查询全链路
SELECT
    e.id,
    e.event_type,
    e.occurred_at AS published_time,
    c.consumed_at,
    CASE
        WHEN e.published = FALSE THEN 'STUCK'
        WHEN c.event_id IS NULL THEN 'PUBLISHED_NOT_CONSUMED'
        WHEN d.id IS NOT NULL THEN 'DEAD_LETTER(' || d.status || ')'
        ELSE 'CONSUMED'
    END AS status
FROM domain_event_outbox e
LEFT JOIN event_consumption_record c
    ON e.id = c.event_id
LEFT JOIN event_dead_letter d
    ON e.id = d.event_id
WHERE e.aggregate_id = :aggregateId
ORDER BY e.occurred_at;
```

## 7. 验收清单

- [ ] Outbox 表已创建，与业务表在同一数据库
- [ ] 业务操作与 Outbox 写入在同一事务
- [ ] 发布策略已选定（轮询/CDC/回调）并实现
- [ ] 消费幂等表已创建，有唯一约束
- [ ] 所有消费者实现幂等检查
- [ ] 重试次数、退避策略已配置
- [ ] 死信表/队列已创建
- [ ] 死信告警已配置（钉钉/飞书/邮件）
- [ ] 对账任务已配置（定时扫描未消费事件）
- [ ] 事件契约包含 eventId/aggregateId/schemaVersion/correlationId/traceId
- [ ] 版本兼容策略已明确（只增字段/双写/新 topic）
- [ ] traceId 在生产者和消费者间正确传播
- [ ] 关键指标已接入监控（发布延迟/失败率/死信积压）
- [ ] 事件全链路查询可用（按 aggregateId 或 eventId）
