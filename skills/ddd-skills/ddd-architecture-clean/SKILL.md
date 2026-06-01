---
name: ddd-architecture-clean
description: Comprehensive guidance for Clean Architecture (整洁架构) — Robert C. Martin's Clean Architecture with Enterprise Business Rules, Use Cases, Interface Adapters, and Frameworks layers. Covers core entities, use case interactors, dependency rules, and full implementation steps with Java/Spring Boot examples. Use when user asks about Clean Architecture, 整洁架构, Robert Martin, Uncle Bob, use case driven architecture, or needs to implement DDD with clean architecture.
license: Apache-2.0
---

# DDD Architecture — Clean

> Clean Architecture by Robert C. Martin (Uncle Bob): UseCase-centric, strict dependency rule — source code dependencies must point only inward.

## Quick Start

直接说明你的需求，例如： "帮我建整洁架构项目骨架" / "订单模块实现 CreateOrder UseCase，从实体到控制器" / "检查项目依赖方向是否正确" / "从三层迁移到整洁架构，先迁订单"。

信息不足时我先给参考版本，再列出需要补充的具体信息。

## Workflow

### Step 1: 确认基础概念
确保团队对 DDD 实体、值对象、聚合根有一致理解。不清晰则先参考 `ddd-architecture-awesome`。

### Step 2: 定义 Enterprise Business Rules
识别聚合根 → 设计实体 + 值对象 → 实现业务规则 → 定义领域事件。参考 [01-core-entities](references/01-core-entities.md)、[order-entity example](examples/01-order-entity.md)

### Step 3: 定义 UseCase 端口
为每个 UseCase 定义独立 Input Port → Output Port → UseCase DTO。参考 [02-usecase-ports](references/02-usecase-ports.md)

### Step 4: 实现 UseCase Interactor
编写 Interactor → 编排实体 + 端口调用 → 发布领域事件。参考 [03-interactors](references/03-interactors.md)、[create-order example](examples/02-create-order-usecase.md)

### Step 5: 实现适配器层
Controller → Presenter → Repository Impl → Gateway Impl → DI 配置。参考 [04-adapters](references/04-adapters.md)、[05-framework-config](references/05-framework-config.md)

### Step 6: 验证与测试
Enterprise 单元测试 → UseCase 集成测试 → Adapter 集成测试 → ArchUnit 验证。参考 [06-dependency-rules](references/06-dependency-rules.md)、[07-testing-strategy](references/07-testing-strategy.md)

## When to Use / When NOT to

| ✅ 适用 | ❌ 不适用 |
|----------|-----------|
| 企业级核心系统（订单、支付、库存） | 临时脚本、小工具 |
| 业务规则独立于交付机制 | 前端重后端轻的简单 CRUD |
| 需要严格模块物理隔离（15-50 人团队） | 团队 < 5 人、需快速迭代 |
| 微服务内部标准化架构 | 简单三层架构已足够 |
| UseCase 驱动的复杂业务编排 | 无复杂业务逻辑的管理后台 |

## Boundary

| 类别 | 能力 | 说明 |
|------|------|------|
| ✅ 擅长 | 严格分层的企业级系统 | 15-50 人团队，模块间强隔离 |
| ✅ 擅长 | UseCase 驱动设计 | 每个用例独立 Interactor + Port |
| ✅ 擅长 | 依赖规则自动化检查 | ArchUnit 全自动验证分层合规 |
| ✅ 擅长 | 多语言落地 | Java/Go/TypeScript/C# 均可实现 |
| ⚠️ 需条件 | 团队理解 Interactor 模式 | 否则学习成本高，需培训 |
| ⚠️ 需条件 | 项目有一定规模 | 小项目用 Layered/Onion 更合适 |
| ⚠️ 需条件 | 需配合 DDD 领域模型 | 单独使用 Clean Architecture 过于抽象 |
| ❌ 超出范围 | 简单 CRUD 项目 | 用 `ddd-architecture-layered` |
| ❌ 超出范围 | 中文 Spring Boot 生态 | 用 `ddd-architecture-cola` |
| ❌ 超出范围 | 需要可视化环状模型 | 用 `ddd-architecture-onion` |
| ❌ 超出范围 | 需要端口适配器概念 | 用 `ddd-architecture-hexagonal` |

## 受众说明

| 用户类型 | 使用方式 |
|---------|---------|
| **后端架构师 / 技术负责人** | 直接使用，选型并按照 Workflow 6 步落地 |
| **Java 开发者** | 参考 examples/ 代码模板，按步骤实现 UseCase |
| **DDD 初学者** | 先读 `ddd-architecture-awesome` 了解概念，再回来看本 Skill |
| **多语言团队（Go/TypeScript/C#）** | 架构规则通用，参考 references/ 中语言无关的部分 |

定制化：触发时说明你的技术栈（Java/Go/TS）、模块名称（如订单/支付），我会针对性地生成代码模板。

## 核心架构

```
Enterprise ← UseCase ← Adapter ← Framework
```

详细原理（四层结构、架构对比、数据流转）参考 [architecture-principles](references/architecture-principles.md)。目录结构参考 [directory-structure](references/directory-structure.md)。

## 开发规范

| 规范 | 说明 | 违规示例 |
|------|------|---------|
| Entity 零框架依赖 | 不可 import Spring/JPA/Jackson | `@Entity` 出现在 `core/entity/` |
| 每个 UseCase 独立端口 | 一个 UseCase = 一个 Input Port 接口 | 多个 UseCase 共享同一个接口 |
| Interactor 只编排不做业务 | 业务 if/else 必须在 Entity 中 | Interactor 中有状态机判断 |
| Output Port 在 UseCase 定义 | Repository 接口定义在 usecase 层 | Adapter 定义 Repository 接口 |
| 数据转换在 Adapter 层 | Controller DTO 不可穿越到 UseCase | `@RequestBody` DTO 直接传入 Interactor |
| 事务在 Framework 层管理 | @Transactional 只在 adapter/repository | Entity 方法上有 @Transactional |

详细规范请参考 [references/06-dependency-rules.md](references/06-dependency-rules.md)。

## Gotchas

| # | 陷阱 | 现象 | 正确做法 |
|---|------|------|---------|
| 1 | UseCase 包含业务逻辑 | Interactor 中有 if/else 状态判断 | 抽到 Entity/Domain Service |
| 2 | Input Port 共享 | 多个 UseCase 共用一个接口 | 每个 UseCase 独立 Input Port |
| 3 | Controller DTO 穿越层 | 框架 DTO 传入 UseCase 层 | Adapter 层完成 DTO ↔ Domain 转换 |
| 4 | Entity 上有 @Entity 注解 | JPA 注解泄露到 Enterprise 层 | 在 Adapter 层创建独立的 JPA Entity |
| 5 | Interactor 直接调 Adapter | 跳过 Output Port 调用实现类 | 通过 Output Port 接口调用 |
| 6 | Output Port 放在 Adapter 层 | UseCase 依赖 Adapter 包 | Output Port 接口定义在 UseCase 层 |
| 7 | UseCase 返回 Entity 对象 | Interactor 返回 `Order` 而非 DTO | 返回 UseCase 专属 Output DTO |
| 8 | 过度设计简单查询 | 读操作也走完整 Input→Interactor→Output | 简单查询直接走 Repository |
| 9 | Adapter 包含业务逻辑 | Controller 中有 if/else | 业务逻辑全在 Enterprise 层 |
| 10 | 缺少 ArchUnit 检查 | 依赖违规无法自动发现 | CI 中集成 ArchUnit 测试 |
| 11 | 领域对象可变 | ValueObject 有 setter 方法 | 所有值对象不可变 (record/final) |
| 12 | UseCase 粒度不当 | Interactor 过大 (200+ 行) | 一个 Interactor 只做一个业务操作 |
| 13 | 忽略领域事件 | 关键操作后无事件发布 | 状态变更必须产生领域事件 |
| 14 | 事务在 UseCase 层 | Interactor 上有 @Transactional | 事务在 Adapter/Repository 层 |
| 15 | Entity 构造函数暴露 | Entity 用 public 构造函数 | 使用 static factory 方法（如 Order.create()） |

## FAQ

| # | 问题 | 回答 |
|---|------|------|
| 1 | Clean Architecture 和六边形架构有什么区别？ | 整洁架构以 UseCase 为组织核心，强调四层严格隔离；六边形以 Port/Adapter 为抽象，强调驱动/被驱动端口对称性。核心目标一致：内层不依赖外层。 |
| 2 | 什么时候用 Interactor vs Domain Service？ | Interactor 在 UseCase 层做编排（调 Entity + 调 Port）；Domain Service 在 Enterprise 层封装跨实体的业务规则（如 PricingService）。 |
| 3 | Service 在哪里写业务逻辑？ | 都没有。Entity 中有业务方法（pay/cancel），DomainService 封装跨实体规则，Interactor 只编排不决策。 |
| 4 | 每个 UseCase 都要有独立的 Input Port 吗？ | 是。这遵循接口隔离原则（ISP）。IOrderService 这种大接口是反模式。 |
| 5 | 一个 UseCase 有多个输出怎么办？ | 每个输出独立为一个 Output Port。如 OrderRepository 为持久化，EventPublisher 为事件，PaymentGateway 为支付。 |
| 6 | Entity 层可以引用 Repository 接口吗？ | 不可以。Enterprise 层不能知道任何 Output Port 的存在。Repository 接口在 UseCase 层定义。 |
| 7 | 简单查询也走 UseCase 层吗？ | 不。纯读操作可以直接调用 Repository（查询不改变状态）。写操作必须走 UseCase。 |
| 8 | 如何组织多个 UseCase？ | 按业务聚合组织：`order/usecase/` 下放所有 Order 相关的 CreateOrder/PayOrder/CancelOrder。 |
| 9 | Interactor 中如何做事务？ | Framework 层通过声明式事务（@Transactional）包裹 Interactor 调用。 |
| 10 | JPA Entity 和 Domain Entity 要分开吗？ | 要。JPA Entity（@Entity）在 Adapter 层，Domain Entity（纯 POJO）在 Enterprise 层。通过 Converter 转换。 |
| 11 | 项目从三层架构迁移要多久？ | 小型 (6 周) / 中型 (12 周) / 大型 (20 周)。使用 Strangler Fig 模式按 UseCase 逐步迁移。 |
| 12 | 如何保证依赖规则不被破坏？ | 在 Framework 模块中写 ArchUnit 测试（参考 examples/04-archunit-test.md），CI 中每次提交自动检查。 |
| 13 | 值对象和实体的区别？ | 值对象不可变、无 ID、按属性相等（如 Money）；实体可变、有唯一 ID、按 ID 相等（如 Order）。 |
| 14 | 领域事件是同步还是异步发布？ | Interactor 中同步收集事件并发布到 EventPublisher Port。异步处理由 Adapter 实现（写消息队列）。 |
| 15 | 适配器层可以有多个实现吗？ | 可以。一个 Output Port 可以有多个 Adapter 实现：JPA/MyBatis/InMemory，通过 Spring Profile 切换。 |

## Keywords

Clean Architecture, 整洁架构, Robert C. Martin, Uncle Bob, Enterprise Business Rules, Use Case, Interactor, Input Port, Output Port, Interface Adapter, Dependency Rule, 依赖倒置, 接口隔离, DDD, 领域驱动设计, 分层架构, 严格分层, 用例驱动, 领域模型, 实体, 值对象, 聚合根, 领域事件, ArchUnit, 依赖规则检查

## References
### Internal

| 文件 | 内容 |
|------|------|
| [references/architecture-principles.md](references/architecture-principles.md) | 四层结构、依赖规则、架构对比、数据流转、目录结构 |
| [references/01-core-entities.md](references/01-core-entities.md) | Enterprise 层实体、值对象、领域事件、异常模板与测试 |
| [references/02-usecase-ports.md](references/02-usecase-ports.md) | Input/Output Port 定义、DTO 设计、端口设计规则 |
| [references/03-interactors.md](references/03-interactors.md) | Interactor 实现模板、复杂编排、查询 Interactor、测试 |
| [references/04-adapters.md](references/04-adapters.md) | Controller、Repository Impl、Gateway 适配器实现 |
| [references/05-framework-config.md](references/05-framework-config.md) | Spring DI 配置、Security、Persistence、多 Profile |
| [references/06-dependency-rules.md](references/06-dependency-rules.md) | 依赖规则矩阵、ArchUnit 全量测试集、CI 集成 |
| [references/07-testing-strategy.md](references/07-testing-strategy.md) | 分层测试策略、Test Doubles、覆盖率目标 |
| [references/08-migration-guide.md](references/08-migration-guide.md) | 三层→整洁架构迁移指南、Strangler Fig 模式 |
| [examples/01-order-entity.md](examples/01-order-entity.md) | 完整 Order 实体代码 + 状态机 + 单元测试 |
| [examples/02-create-order-usecase.md](examples/02-create-order-usecase.md) | 完整 CreateOrder UseCase 实现 + 测试 + Test Doubles |
| [examples/03-repository-implementation.md](examples/03-repository-implementation.md) | Repository Adapter JPA 实现 + 集成测试 |
| [examples/04-archunit-test.md](examples/04-archunit-test.md) | 完整 ArchUnit 依赖规则测试套件 |
| [examples/05-domain-event-handling.md](examples/05-domain-event-handling.md) | 领域事件定义、发布、消费完整实现 |
| [examples/06-monolith-simple.md](examples/06-monolith-simple.md) | 单体 Clean 简单版：单模块包级四层，目录树+依赖方向+ArchUnit |
| [examples/07-monolith-complex.md](examples/07-monolith-complex.md) | 单体 Clean 复杂版：多聚合+多 Interactor，共享内核+领域隔离 |
| [examples/08-monolith-multi-module.md](examples/08-monolith-multi-module.md) | 单体 Clean 多模块版：Maven 模块级分层，编译期强制依赖方向 |
| [examples/09-microservice-simple.md](examples/09-microservice-simple.md) | 微服务 Clean 简单版：包级四层+事件总线+Kafka 适配器 |
| [examples/10-microservice-complex.md](examples/10-microservice-complex.md) | 微服务 Clean 复杂版：CQRS + Saga + Outbox + 多子域 |
| [examples/11-microservice-multi-module.md](examples/11-microservice-multi-module.md) | 微服务 Clean 多模块版：6 模块+API 契约独立发布 |
| [examples/12-microservice-complex-multi.md](examples/12-microservice-complex-multi.md) | 微服务 Clean 复杂多模块：8 模块+全模式矩阵+子域编排 |

### External

- [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — Robert C. Martin (2012)
- [Clean Architecture: A Craftsman's Guide](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/) — Robert C. Martin (2017)
- [Domain-Driven Design: The Blue Book](https://www.domainlanguage.com/ddd/blue-book/) — Eric Evans (2003)
- [Get Your Hands Dirty on Clean Architecture](https://reflectoring.io/book/) — Tom Hombergs
- [thombergs/buckpal](https://github.com/thombergs/buckpal) — Java Reference Implementation
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — Alistair Cockburn
### DDD Skills 生态

| 前置/后续 | Skill |
|-----------|-------|
| ← 前置 | [ddd-architecture-selector](../ddd-architecture-selector/) — 架构选型 |
| → 后续 | [ddd-domain-designer](../ddd-domain-designer/) — 领域建模 |
| → 后续 | [ddd-code-reviewer](../ddd-code-reviewer/) — 代码审查 |
| → 后续 | [ddd-architecture-evaluator](../ddd-architecture-evaluator/) — 架构评估 |
| 🔗 相关 | [ddd-architecture-hexagonal](../ddd-architecture-hexagonal/) — 六边形架构 |
| 🔗 相关 | [ddd-architecture-layered](../ddd-architecture-layered/) — 分层架构 |

## 🧭 DDD Skills Journey

> 📍 **You are here: `ddd-architecture-clean` — Step 3: 整洁架构落地**

`awesome(入门)` → `selector(选型)` → **`clean(整洁架构)`** + `layered/onion/hexagonal/cola` → `domain-designer/cqrs/api-designer` → `code-reviewer` → `testing/devops/evaluator` → `architecture-doc`

**← [selector](../ddd-architecture-selector/) | → [domain-designer](../ddd-domain-designer/) | 🔗 [api-designer](../ddd-api-designer/) · [testing-strategist](../ddd-testing-strategist/) | 🏠 [awesome](../ddd-architecture-awesome/)

---

## Security & Stability

- 所有代码模板为教育用途。生产环境请用环境变量替换占位凭证。
- 整洁架构的依赖规则（只能向内）天然阻止领域代码访问 I/O — 内置安全优势。
- Interactor 模式确保每个 UseCase 可独立测试，无需框架或数据库依赖。
- 不包含可执行脚本。本 Skill 仅提供架构指导和代码生成模式。
