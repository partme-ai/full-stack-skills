---
name: ddd-cola
description: Provides comprehensive guidance for COLA architecture including adapter layer, application layer, domain layer, and infrastructure layer. Use when the user asks about COLA, needs to implement COLA architecture, structure applications with COLA, or work with COLA patterns.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 使用 COLA 架构框架进行项目开发（Adapter → App → Domain ← Infrastructure）
- 应用 COLA 的分层架构模式，明确适配层、应用层、领域层、基础设施层职责
- 实现基于 COLA 的领域驱动设计，保持领域层纯净、依赖倒置

## How to use this skill

1. **分层**：Adapter 处理 HTTP/RPC/消息入站与出站；Application 编排用例、事务；Domain 承载实体、值对象、领域服务；Infrastructure 实现仓储、外部服务。
2. **依赖方向**：Domain 不依赖外层；Application 依赖 Domain；Adapter/Infrastructure 依赖 Application 与 Domain。
3. **包结构**：按 layer 分包（如 `adapter/controller`、`app/executor`、`domain/model`、`infrastructure/persistence`），或按模块再分子包。

## Best Practices

- 领域逻辑只放在 Domain 层；Application 只做编排与事务边界。
- 用接口在 Domain 或 Application 定义端口，Infrastructure 实现。
- 避免在 Adapter 中写业务逻辑；DTO 与领域对象在边界做转换。

## Keywords

cola, cola architecture, clean object-oriented layered architecture, 分层架构, COLA 框架, DDD COLA, adapter layer, application layer, domain layer, infrastructure layer
