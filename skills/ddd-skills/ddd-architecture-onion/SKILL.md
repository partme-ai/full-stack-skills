---
name: ddd-architecture-onion
description: Comprehensive guidance for Onion Architecture (洋葱架构) — Jeffrey Palermo's onion architecture with domain-centric layered isolation, dependency inversion from outer to inner rings. Covers domain core, application interfaces, infrastructure implementation, and API adapters with full Java/Spring Boot examples. Use when user asks about onion architecture, 洋葱架构, Jeffrey Palermo, concentric architecture, or needs layered domain isolation.
license: Apache-2.0
---

# DDD Architecture — Onion (洋葱架构)

基于 Jeffrey Palermo（2008）提出的同心圆架构模型，以 Domain 为圆心，依赖方向严格指向内层。

## Workflow

### Step 1: 适用性检查 — 判断项目是否适合洋葱架构 | 参考：SKILL.md When to Use
### Step 2: 搭建目录骨架 — 创建四层模块 core/infrastructure/api/composition | 参考：references/04
### Step 3: 编写 Domain 核心 — 聚合根、值对象、Repository 接口、领域事件（零框架依赖）| 参考：references/01
### Step 4: 编写 Application 接口 — 应用服务接口契约，纯编排不含业务逻辑 | 参考：references/02
### Step 5: 编写 Infrastructure 实现 — 实现 Domain 层 Repository/MQ/外部客户端 | 参考：references/03
### Step 6: 编写 API 适配器 — Controller、DTO、Assembler、全局异常处理 | 参考：references/04
### Step 7: 配置 DI 组装 — composition 模块集中装配 | 参考：references/05
### Step 8: 编写测试 — Domain 层单测 → Application Mock → Infra 集成测试 | 参考：references/06
### Step 9: Gotchas 检查 — 对照常见陷阱逐条验证 | 参考：各 references 陷阱章节
### Step 10: 迁移（如适用） — 三层→洋葱渐进迁移 | 参考：references/07

## When to Read (触发条件)

| 用户问题 | 加载动作 |
|---------|---------|
| "帮我用洋葱架构搭建项目" | 打开 SKILL.md + references/01-05 |
| "Repository 接口应该放哪？" | 打开 references/01-domain-model |
| "洋葱架构怎么测试？" | 打开 references/06-testing |
| "从三层怎么迁到洋葱？" | 打开 references/07-migration-from-layered |
| "洋葱和六边形有什么区别？" | 打开 references/08-comparison |
| "洋葱支持 CQRS 吗？" | 打开 examples/example-04-cqrs-onion |
| "多入口怎么设计？" | 打开 examples/example-03-multi-entry |
| "DI 怎么配置 Spring Boot？" | 打开 references/05-di-composition |

## When to Use

| ✅ 适用场景 | ❌ 不适用 |
|-----------|----------|
| 基础设施频繁变更（DB/MQ/缓存厂商更换） | 简单 CRUD 项目（过度设计） |
| 单元测试覆盖率要求 > 80% | 两周交付的原型/PoC |
| 多入口系统（REST + CLI + MQ + gRPC） | 单入口 + 单数据库的简单服务 |
| 团队有接口抽象和 DI 设计能力 | 团队不熟悉依赖倒置 |
| 业务规则复杂，需要严格隔离 | 三层架构够用 |

### Boundary

| 区域 | 归属 |
|------|------|
| 三层→洋葱迁移 | ✅ 本 Skill（references/07-migration） |
| 洋葱 vs 六边形 vs 整洁对比 | ✅ 本 Skill（references/08-comparison） |
| 选型决策 | ❌ 用 `ddd-architecture-selector` |
| 领域建模 | ❌ 用 `ddd-domain-designer` |
| 代码审查 | ❌ 用 `ddd-code-reviewer` |
| COLA 项目 | ❌ 用 `ddd-architecture-cola` |

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## 核心原理：同心圆依赖规则

所有依赖关系指向圆心（Domain），内层定义接口，外层实现接口。

```
Infrastructure → API/Adapters → Application → Domain Core ★
所有依赖指向圆心，内层零框架依赖。
```

### Jeffrey Palermo 四原则

1. **应用核心独立于基础设施** — Domain 层不 import 任何框架/数据库类
2. **内层定义接口，外层实现** — 如 `OrderRepository` 接口在 Domain，实现在 Infrastructure
3. **依赖指向圆心** — Infrastructure → Application → Domain，不允许逆向
4. **外层知道内层，内层不知道外层** — Domain 对 Infrastructure 一无所知

## Rules

| # | 规则 | 检测方式 | 级别 |
|---|------|---------|:----:|
| 1 | Domain 层零框架依赖 | 搜索 Domain 包中的框架 import | P0 |
| 2 | Repository 接口在 Domain，实现在 Infra | 检查接口/实现位置 | P0 |
| 3 | Application 层纯编排，不含业务 if/else | 代码审查 | P0 |
| 4 | 值对象不可变（final 字段，无 setter） | ValueObject 类检查 | P1 |
| 5 | 跨聚合通过 ID 引用 | 聚合根字段类型检查 | P1 |
| 6 | DTO 在 API 层定义，不泄露到 Domain | 检查 Domain 中 DTO import | P0 |
| 7 | Composition Root 集中管理 DI | 检查各层是否有 `new` 依赖 | P1 |

详见 [references/08-comparison.md](references/08-comparison.md) 了解洋葱 vs 六边形 vs 整洁架构的详细对比。

## 目录结构

```
{project}/
├── {project}-core/domain/          # 领域模型（零框架依赖）
├── {project}-core/application/     # 应用服务接口
├── {project}-infrastructure/       # Repository 实现、MQ、外部集成
├── {project}-api/                  # Controller、DTO、Assembler
└── {project}-composition/          # DI 组装
```

### 模块依赖规则

| 模块 | 可依赖 | 不可依赖 |
|------|--------|---------|
| core/domain | 无（纯 Java） | Spring/JPA/MyBatis |
| core/application | domain | infrastructure, api |
| infrastructure | core | api |
| api | core, infrastructure | — |
| composition | 所有模块 | — |

## 开发规范（详见各 references）

| # | 规范 | 违规示例 |
|---|------|---------|
| 1 | Domain 零框架依赖 | `import org.springframework.stereotype.Service` |
| 2 | Repository 接口在 Domain | 接口和实现都在 Infra |
| 3 | Application 只编排不实现 | AppService 包含业务判断 |
| 4 | 事务边界在 Application | Controller 或 Repository 开事务 |
| 5 | 跨聚合通过领域事件 | 聚合 A 直接引用聚合 B |
| 6 | 值对象不可变 | ValueObject 有 setter |
| 7 | 实体充血模型 | 实体只有 getter/setter |
| 8 | DTO 在 API 层定义 | Domain 中有 DTO import |
| 9 | Composition Root 最外层 | 各层自己 `new` 依赖 |
| 10 | 严格分层 | API 直接调用 Infrastructure |

## Gotchas — (详见各 references 陷阱章节)

15 条核心陷阱：Domain 层框架泄露 / Repository 接口位置 / Application 过厚 / 过度抽象 / Composition Root 分散 / 值对象可变 / 聚合根过大 / 跨聚合直接引用 / Controller 含业务逻辑 / DTO 泄露 / PO 注解 / 缺少事件 / 事务跨聚合 / Infra 侵入测试

## FAQ — (详见 references/08-comparison.md 和各层 references)

涵盖：洋葱 vs 六边形、Domain 框架限制、值对象 vs 实体、Repository 接口位置、聚合大小、迁移策略、CQRS 兼容、测试层次、微服务适配、事件跨服务等。

## Keywords

```
onion architecture, 洋葱架构, Jeffrey Palermo, domain-centric architecture,
layered isolation, dependency inversion, 依赖倒置, concentric layers,
core/domain, application interfaces, infrastructure implementation,
API adapters, composition root, DI assembly, domain model,
repository pattern, aggregate root, value object, domain service,
DDD layered, clean architecture comparison, hexagonal comparison
```

## References

| 文件 | 用途 |
|------|------|
| [references/01-domain-model.md](references/01-domain-model.md) | 领域层设计详解：聚合根、值对象、领域服务 |
| [references/02-application-interfaces.md](references/02-application-interfaces.md) | 应用层接口设计：服务编排与事务边界 |
| [references/03-infrastructure-implementation.md](references/03-infrastructure-implementation.md) | 基础设施层实现：Repository、MQ、外部集成 |
| [references/04-api-adapters.md](references/04-api-adapters.md) | API 适配层：Controller、DTO、Assembler |
| [references/05-di-composition.md](references/05-di-composition.md) | DI 组装：Composition Root 配置 |
| [references/06-testing.md](references/06-testing.md) | 测试策略：单元测试、集成测试、契约测试 |
| [references/07-migration-from-layered.md](references/07-migration-from-layered.md) | 从三层架构迁移到洋葱架构的完整路径 |
| [references/08-comparison.md](references/08-comparison.md) | 洋葱 vs 六边形 vs 整洁架构详细对比 |

## Examples

### 业务场景示例

| 示例 | 说明 |
|------|------|
| [examples/example-01-order-payment.md](examples/example-01-order-payment.md) | 订单支付完整示例（含 Domain/Application/Infra/API） |
| [examples/example-02-product-catalog.md](examples/example-02-product-catalog.md) | 产品目录管理示例（含多聚合协作） |
| [examples/example-03-multi-entry.md](examples/example-03-multi-entry.md) | 多入口系统示例（REST + MQ + CLI 三种适配器） |
| [examples/example-04-cqrs-onion.md](examples/example-04-cqrs-onion.md) | CQRS + 洋葱融合示例（Command/Query 分离） |
| [examples/example-05-user-registration.md](examples/example-05-user-registration.md) | 用户注册 + 邮件验证示例 |

### 项目规模示例

| 示例 | 说明 |
|------|------|
| [examples/06-monolith-simple.md](examples/06-monolith-simple.md) | 单体简单：单模块项目，一个限界上下文 |
| [examples/07-monolith-complex.md](examples/07-monolith-complex.md) | 单体复杂：单模块多限界上下文，内部隔离 |
| [examples/08-monolith-multi-module.md](examples/08-monolith-multi-module.md) | 单体多模块：Maven 多模块强制分层 |
| [examples/09-microservice-simple.md](examples/09-microservice-simple.md) | 微服务简单：单服务单上下文洋葱 |
| [examples/10-microservice-complex.md](examples/10-microservice-complex.md) | 微服务复杂：单服务多上下文内部隔离 |
| [examples/11-microservice-multi-module.md](examples/11-microservice-multi-module.md) | 微服务多模块：单服务 Maven 多模块洋葱 |
| [examples/12-microservice-complex-multi.md](examples/12-microservice-complex-multi.md) | 微服务复杂多模块：多上下文 Maven 多模块 |

Primary Sources: [Onion Architecture Part 1-4](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) — Jeffrey Palermo (2008) · [DDD Blue Book](https://www.domainlanguage.com/ddd/blue-book/) — Eric Evans (2003) · [Implementing DDD](https://www.domainlanguage.com/ddd/blue-book/) — Vaughn Vernon (2013)

Implementation: [Microsoft DDD Microservice](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice) · [Testcontainers](https://testcontainers.com/)

## Output

回答始终包含：适用性判断 → 目录结构 → 每层代码模板 → DI 装配 → 测试骨架 → Gotchas 合规检查。详细参考 references/ 和 examples/ 文件。

---

## 技能旅程

> 📍 当前：洋葱架构落地

← **上一步**：[selector](../ddd-architecture-selector/)
→ **下一步**：[domain-designer](../ddd-domain-designer/)
🔗 **相关**：[cqrs-architecture](../ddd-cqrs-architecture/) | [code-reviewer](../ddd-code-reviewer/)
🏠 **首页**：[awesome](../ddd-architecture-awesome/)

> 核心口诀：内层定义接口，外层实现接口，依赖指向圆心。

## Security & Safety

This skill is pure documentation. It contains no executable scripts, collects no user data, accesses no external services or networks.

## 验证清单

- [ ] Domain 层无框架 import
- [ ] Repository 接口在 Domain 层
- [ ] Repository 实现在 Infrastructure 层
- [ ] Application 层无业务 if/else
- [ ] 值对象不可变
- [ ] 跨聚合通过 ID 引用
- [ ] DTO 只定义在 API 层
- [ ] DI 集中在 composition 模块
- [ ] 领域事件已发布
