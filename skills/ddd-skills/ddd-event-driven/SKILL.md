---
name: ddd-event-driven
description: Provides comprehensive guidance for event-driven architecture including domain events, event sourcing, CQRS, and event patterns. Use when the user asks about event-driven architecture, needs to implement event-driven systems, or work with domain events.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用领域事件解耦聚合/服务、驱动异步流程
- 设计事件溯源（Event Sourcing）或 CQRS
- 选型与使用消息中间件（Kafka、RabbitMQ 等）

## How to use this skill

1. **领域事件**：在聚合内发布“已发生的事实”；由应用层或基础设施投递到消息总线。
2. **事件溯源**：以事件流为事实来源；聚合状态由重放事件得到；需快照与版本策略。
3. **CQRS**：写模型与读模型分离；写侧发事件，读侧订阅并物化视图。

## Best Practices

- 事件命名用过去式、携带聚合 ID 与关键数据；避免大对象与敏感信息。
- 保证至少一次投递与幂等消费；必要时用 outbox 表与轮询发布。
- 明确事件版本与兼容策略（兼容字段、新主题）。

## Keywords

event-driven, domain events, event sourcing, CQRS, 事件驱动, 领域事件, 事件溯源
