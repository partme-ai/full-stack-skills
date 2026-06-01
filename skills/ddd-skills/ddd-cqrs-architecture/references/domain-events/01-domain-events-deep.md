# 领域事件深入 — 事件驱动设计原则

## 事件生命周期

```
领域行为 → 构建 DomainEvent → 持久化 → EventBus 发布
                                        ↓
                               ┌────────┴────────┐
                               ↓                  ↓
                        本地处理器 (同步)      MQ 外发 (异步)
                        (同一进程)             (跨服务)
                                                ↓
                                          外部处理器
                                          (幂等 + 补偿)
```

## 发布策略对比

| 策略 | 延迟 | 复杂度 | 场景 |
|------|:----:|:------:|------|
| 轮询发布（定时扫表） | 1-5s | 低 | 中小流量 |
| CDC（Debezium binlog） | < 100ms | 中 | 高流量低延迟 |
| 事务提交回调 | < 10ms | 低 | Spring 项目 |

## 幂等设计代码示例

```java
// 策略 1: 事件去重表 — UNIQUE 约束防重
@Transactional
public void handle(OrderPaidEvent event) {
    eventRecordDao.insert(new EventRecord(event.getEventId()));
    // 业务处理...
}

// 策略 2: 状态机守卫 — 状态不可逆，已处理则跳过
public void pay() {
    if (this.status == OrderStatus.PAID) return;
    this.status = OrderStatus.PAID;
    addDomainEvent(new OrderPaidEvent(this.id));
}
```

## 领域事件设计原则

1. 事件用过去时命名（OrderPaidEvent, OrderShippedEvent）
2. 事件体包含足够上下文，但不含敏感数据
3. 事件版本向后兼容（仅新增字段，不删除/重命名）
4. 事件消费者必须幂等（at-least-once 投递）
5. 聚合内强一致，聚合间最终一致
