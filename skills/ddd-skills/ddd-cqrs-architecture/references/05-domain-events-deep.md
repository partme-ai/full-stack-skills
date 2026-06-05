# 领域事件深度参考

## 领域事件识别方法

捕捉业务专家口中的关键词：
- "如果发生……，则……"
- "当做完……的时候，请通知……"
- "发生……时，则……"

---

## 事件设计 5 步法

### Step 1: 从业务流程中提取事件

```
业务描述 → 过去式事件

"用户提交订单后，系统扣减库存，然后等待支付"
→ 订单已提交（OrderSubmitted）
→ 库存已扣减（InventoryDeducted）

"支付成功后，订单状态变更为已支付，发送通知"
→ 支付已完成（PaymentCompleted）
→ 订单已支付（OrderPaid）
→ 通知已发送（NotificationSent）
```

### Step 2: 确定事件上下文

```java
public class OrderPaid extends DomainEvent {
    private final OrderId orderId;
    private final Money paidAmount;
    private final PaymentMethod paymentMethod;
    private final LocalDateTime paidAt;

    // 必须包含足够消费方使用的数据
    // 但不包含敏感信息（信用卡号等）
}
```

### Step 3: 确定发布策略

```
事件发布位置决策：
├── 同一事务内（聚合内强一致）
│   └── order.pay() 后 addDomainEvent(OrderPaid)
├── 同一进程内微服务内
│   └── Outbox 表 + 定时轮询发布
└── 跨微服务
    └── Outbox → MQ（Kafka/RabbitMQ）
```

### Step 4: 设计消费者幂等

```java
@EventListener
@Transactional
public void onOrderPaid(OrderPaidEvent event) {
    // Step 1: 幂等检查
    if (eventRecordDao.exists(event.getEventId())) {
        log.info("Duplicate event ignored: {}", event.getEventId());
        return;
    }
    // Step 2: 业务处理
    orderReadModel.updateStatus(event.getOrderId(), "PAID");
    // Step 3: 记录消费
    eventRecordDao.insert(new EventRecord(event.getEventId()));
}
```

### Step 5: 事件版本管理

```java
// V1 原始字段
class OrderPaid extends DomainEvent {
    private OrderId orderId;
    private Money amount;
}

// V2 新增字段（向后兼容）
class OrderPaid extends DomainEvent {
    private OrderId orderId;
    private Money amount;
    private PaymentMethod paymentMethod;  // V2 新增，旧消费者忽略
}
```

---

## 事件持久化实现（Outbox 模式）

```sql
-- 与业务表在同一数据库，同一事务写入
CREATE TABLE domain_event_outbox (
    id              VARCHAR(36) PRIMARY KEY,
    aggregate_id    VARCHAR(36) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_data      JSONB NOT NULL,
    occurred_at     TIMESTAMP NOT NULL,
    published       BOOLEAN NOT NULL DEFAULT FALSE,
    retry_count     INTEGER NOT NULL DEFAULT 0,
    INDEX idx_unpublished (published, created_at)
);
```

```java
@Transactional
public void payOrder(PayOrderCommand cmd) {
    Order order = orderRepo.findById(cmd.getOrderId()).orElseThrow();
    order.pay();                                    // 执行业务
    orderRepo.save(order);                         // 持久化聚合
    for (DomainEvent event : order.getDomainEvents()) {
        outboxRepo.save(OutboxRecord.from(event));  // 同一事务写 Outbox
    }
}
```

---

## 发布策略对比

| 策略 | 延迟 | 复杂度 | 实现 |
|------|:----:|:----:|------|
| **轮询发布** | 1-5s | 低 | `@Scheduled(fixedDelay=2000)` 扫 Outbox 表 |
| **CDC (Debezium)** | < 100ms | 中 | 监听 binlog → Kafka → Consumer |
| **事务提交回调** | < 10ms | 低 | `TransactionSynchronization.afterCommit()` |

---

## 承保业务流程案例

```
投保微服务 → 生成缴费通知单事件 → 收款微服务订阅并缴费
收款微服务 → 缴费已完成事件 → 投保微服务转保单
投保微服务 → 保单已生成事件 → 保单微服务保存
保单微服务 → 事件扇出 → 佣金/收付费/再保/财务等微服务
```

---

## 为什么用最终一致性

- 一次事务最多只能更改一个聚合的状态
- 涉及多个聚合状态变更时，用领域事件实现最终一致
- 切断领域模型之间的强依赖关系
- 实现 1 个发布方 → N 个订阅方

---

## 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| 事件不含足够上下文 | 消费者需要反查数据库 | 事件体包含消费方需要的全部数据 |
| 事件和业务不在同一事务 | 业务成功但事件丢失 | Outbox 模式，事务内写入 |
| 消费者不幂等 | 重复消费导致数据错误 | 事件去重表 + UNIQUE 约束 |
| 事件版本不兼容 | 升级后消费者解析失败 | 只增字段，不删不改 |
