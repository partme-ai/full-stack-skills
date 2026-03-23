---
name: ddd-hexagonal-architecture
description: Provides comprehensive guidance for hexagonal architecture including ports and adapters, domain isolation, and dependency inversion. Use when the user asks about hexagonal architecture, needs to implement ports and adapters pattern, or structure applications with hexagonal architecture.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 用“端口与适配器”隔离领域与外部（DB、API、消息）
- 实现依赖倒置：领域定义端口，适配器实现
- 画/实现六边形架构图与分层

## How to use this skill

1. **端口**：领域侧定义接口（如 Repository、EventPublisher）；应用或适配器调用。
2. **适配器**：入站（HTTP、消息消费者）与出站（DB、HTTP 客户端、消息发送）实现端口。
3. **依赖**：所有依赖指向领域；领域不依赖框架或 IO。

## Best Practices

- 领域层零框架依赖；测试时用内存或 mock 适配器。
- 一个端口可对应多种适配器（如多种存储、多种传输）。
- 与 COLA/Clean Architecture 可结合：六边形即“一层领域 + 多适配器”。

## Keywords

hexagonal architecture, ports and adapters, 六边形架构, 端口与适配器, dependency inversion
