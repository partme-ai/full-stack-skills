---
name: ddd-microservices
description: Provides comprehensive guidance for DDD in microservices including bounded contexts, service boundaries, event-driven architecture, and microservice patterns. Use when the user asks about DDD microservices, needs to design microservices with DDD, or implement microservice architectures.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用 DDD 划分微服务边界（限界上下文、聚合、领域事件）
- 设计服务间契约与事件驱动交互
- 落地跨服务的一致性、查询与运维策略

## How to use this skill

1. **边界**：按限界上下文拆服务；每个服务内用聚合、实体、值对象建模。
2. **通信**：同步（REST/gRPC）用于查询与强一致；异步（领域事件/消息）用于解耦与最终一致。
3. **数据**：每服务独立数据库；通过 API 或事件同步关键数据，避免共享库。

## Best Practices

- 先划清限界上下文再切服务，避免过早拆分。
- 用领域事件表达跨聚合、跨服务的事实；保证幂等与顺序。
- 明确每个服务的 SLA、数据归属与故障边界。

## Keywords

ddd microservices, bounded context, aggregate, domain events, service boundary, 微服务, 限界上下文, 领域事件
