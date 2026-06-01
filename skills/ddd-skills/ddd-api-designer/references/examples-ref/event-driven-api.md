# 事件驱动 API 设计

领域事件通过异步消息在限界上下文间传播：
- 事件命名：{Aggregate}.{Action}.Occurred（如 Order.Paid.Occurred）
- 事件契约：eventId + eventType + aggregateId + occurredAt + payload
- 投递保障：至少一次投递（At-Least-Once），消费者实现幂等去重
- 事件 API：POST /api/v1/events/publish — 发布事件
