---
name: ddd-clean-architecture
description: Provides comprehensive guidance for clean architecture including layer separation, dependency rules, and architectural patterns. Use when the user asks about clean architecture, needs to implement clean architecture principles, or structure applications with clean architecture.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 按 Clean Architecture 分层（Entities, Use Cases, Interface Adapters, Frameworks）
- 遵守依赖规则：内层不依赖外层；业务核心不依赖框架与 IO
- 组织项目包与测试边界

## How to use this skill

1. **层**：最内 Entities；次内 Use Cases（应用逻辑）；再外 Interface Adapters（Presenter、Gateway 实现）；最外 Frameworks（Web、DB、UI）。
2. **依赖**：只允许由外向内；Use Cases 定义 Gateway 接口，外层实现。
3. **测试**：核心用单元测试；外层用集成测试或 E2E。

## Best Practices

- 业务规则集中在 Entities 与 Use Cases；避免在 Controller 或 DB 层写业务。
- 用接口隔离 IO；便于替换与测试。
- 与 DDD 结合：Entities/Use Cases 可对应聚合与领域服务。

## Keywords

clean architecture, dependency rule, use case, entity, 整洁架构, 依赖规则
