---
name: ddd-domain-designer
description: Domain-driven design complete workflow — event-storming-driven 6-step domain modeling process, aggregate design 5-principles + 6-rules, bounded context identification, entity/value object design patterns, domain event catalog, and code mapping. Use when user asks about domain modeling, 领域建模, aggregate design, 聚合设计, bounded context, 限界上下文, or needs to design DDD domain model.
license: Apache-2.0
---

# DDD Domain Designer

Domain design full workflow — from event storming results to code-ready domain models, aggregates, and bounded contexts.

## Workflow

This skill covers the **complete domain design pipeline** from business understanding to code-ready models:

```
Business Requirements → [Event Storming] → 6-Step Process → Code-Ready Domain Models
```

Step 1: 产品愿景 — FOR [用户] WHO [需求]…UNLIKE [替代方案] 模板。产出：愿景墙。
Step 2: 场景分析 — 梳理用户旅程，捕获领域事件(橙色)/命令(蓝色)/角色(黄色)。产出：事件时间线。
Step 3: 领域建模 — 提取实体/值对象 → 聚类为聚合 → 划分限界上下文。产出：聚合清单。
Step 4: 微服务拆分 — 评估各BC独立部署价值。一个BC = 一个潜在微服务。产出：上下文映射图。
Step 5: 详细设计 — 确定聚合根、实体、值对象、领域事件(过去式命名)、不变式。
Step 6: 开发测试 — 聚合为单位组织开发测试，每聚合一个Repository接口。

详见 [references/ddd-tactical.md](references/ddd-tactical.md)

## When to Use

**Use when**: designing domain models from event storming outputs, identifying aggregates/bounded contexts, mapping DO/DTO/VO/PO, selecting value object persistence strategies, designing domain events and invariants.

**Not for**: no event storming input → `ddd-event-storming` | basic DDD concepts → `ddd-architecture-awesome` | review existing models → `ddd-code-reviewer` | generate API → `ddd-api-designer` | simple CRUD (skip domain modeling)

## Boundary

**擅长**：
- 从事件风暴结果到领域模型设计（聚合、限界上下文、实体/值对象）
- 聚合设计 6 原则落地：一致性边界、小聚合、ID引用
- 限界上下文划分和 7 种上下文映射模式
- 领域对象→代码对象映射（DO/DTO/VO/PO）
- 值对象持久化策略选择（Inline/JSON/Embeddable）
- 领域事件设计与发布策略、领域不变式识别

**需条件**：已有事件风暴输出或明确业务需求、已选定架构模式、有统一语言(UL)、领域专家可复核。

**不适用**：无事件风暴结果→`ddd-event-storming` | 只需基础概念→`ddd-architecture-awesome` | 审查已有模型→`ddd-code-reviewer` | 从模型生成API→`ddd-api-designer` | 简单CRUD→跳过领域建模

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## 适用用户

| 用户类型 | 前置知识 |
|---------|---------|
| **后端开发** | 了解 DDD 基础概念（实体/值对象/聚合） |
| **架构师** | 有分布式系统经验，了解领域驱动设计 |
| **技术负责人** | 理解 DDD 战略设计 |
| **DDD 初学者** | 建议先看 `ddd-architecture-awesome` |

## 事件风暴驱动 6 步流程

详见 [references/ddd-tactical.md](references/ddd-tactical.md)、[references/clean-ddd-hexagonal-tactical.md](references/clean-ddd-hexagonal-tactical.md)

## Aggregate Rules / 聚合设计五步法 + 六原则

**五步法**: (1)识别实体/值对象 → (2)一致性边界分组 → (3)选择聚合根 → (4)定义不变式 → (5)领域专家复核

**六原则**:

| # | 原则 | 说明 | 审查要点 |
|---|------|------|---------|
| 1 | **一致性边界内建模真正的不变条件** | 聚合封装业务规则 | 不变式是否可能被外部破坏？ |
| 2 | **设计小聚合** | 大聚合导致并发瓶颈 | 实体 > 5 个？有无 N+1 隐患？ |
| 3 | **通过唯一标识引用其他聚合** | 聚合间只记ID，不持对象引用 | 存在直接对象引用？ |
| 4 | **边界外使用最终一致性** | 一个事务只改一个聚合 | 跨聚合用领域事件异步处理 |
| 5 | **通过应用层实现跨聚合调用** | 领域服务不直接跨聚合 | 应用层承担编排职责？ |
| 6 | **适合自己才是最好的** | 可突破原则但需记录理由 | ADR记录决策理由 |

详见 [references/advanced-tactical-patterns.md](references/advanced-tactical-patterns.md)、[references/domain-invariants.md](references/domain-invariants.md)

## 限界上下文划分

**划分依据**: 语言变化点、团队组织边界(康威定律)、变更频率差异、独立部署需求、业务能力域(核心/支撑/通用)。

**7种映射模式**: Partnership(高耦合) | Shared Kernel(高) | Customer-Supplier(中) | Conformist(中) | Anti-Corruption Layer(低) | Open Host Service(低) | Published Language(低)

详见 [references/bounded-context-mapping.md](references/bounded-context-mapping.md)

## 领域对象 → 代码对象映射

**四类对象**: PO(持久化→Infrastructure) | DO(领域对象→Domain, 充血模型) | DTO(传输对象→Interface/App) | VO(视图对象→Interface)

**转换链**: VO ↔ DTO ↔ DO ↔ PO (Repository托管DO↔PO; Assembler转换DO→DTO; BFF组装DTO→VO)

详见 [references/code-model-mapping.md](references/code-model-mapping.md)

## 与 ddd-event-storming 的关系

推荐流程: `event-storming`(探索) → `domain-designer`(详细设计) → `(架构Skill)`(落地实现)

## Gotchas

1. **聚合过大**(10+实体) → 小聚合原则，推荐1-5个
2. **缺少一致性边界**(单事务改2聚合根) → 单事务只改一个聚合
3. **值对象被当成实体**(Address有ID) → 属性相等则为VO，设为不可变
4. **聚合根ID用自增ID** → 应用UUID或业务编号(领域事件/分布式唯一标识需要)
5. **领域事件命名不规范** → 过去式("OrderPaid"非"PayOrder")
6. **领域层依赖框架注解** → Domain层纯POJO，零框架依赖
7. **直接对象引用跨聚合** → 只持聚合B的ID
8. **跨聚合事务** → 最终一致性+发件箱模式(Outbox Pattern)
9. **聚合根行为泄漏到Service** → 业务逻辑内聚在聚合根方法，Service只做编排
10. **忽略统一语言(UL)** → 代码术语与业务语言保持一致

详见 [references/ddd-tactical.md](references/ddd-tactical.md)

## 验证指南

自检清单: 不变式文档化? | 聚合根ID用业务标识? | 跨聚合ID引用? | 单事务改一聚合? | 值对象不可变? | 实体充血模型? | 领域事件过去式? | 每事件有发布者/消费者? | VO持久化策略选定? | BC边界明确? | 统一语言建立? | 聚合大小合理(≤5实体)?

## FAQ

- **聚合含多少实体？** 1-5个，超5个评估拆分。
- **聚合根可以是VO？** 不可，聚合根必须是实体（有独立生命周期和全局唯一ID）。
- **领域服务 vs 应用服务？** 领域服务:业务规则(如计算折扣)。应用服务:技术编排(如创建订单后通知)。
- **BC = 微服务？** 理想对应一个微服务，可根据团队/部署频率调整。BC至少是模块边界。
- **实体 vs VO 怎么分？** 有独立ID→实体。不可变且属性相等→VO。不满足则重新建模。
- **跨聚合查询怎么做？** 应用层组合Repository查询，或在CQRS查询侧创建读模型/物化视图。
- **值对象一定用类封装？** 简单值可用基础类型；有验证/行为的建议类封装(Email, Money)。
- **没有领域专家怎么办？** 从资深业务人员/产品经理中寻找担任领域专家角色。
- **同实体可在多个BC存在？** 可以，但每个BC中有不同含义和属性(如"用户"在权限BC="账号"，在订单BC="买家")。
- **发件箱模式(Outbox Pattern)？** 同本地事务写领域事件到EventOutbox表，后台进程读取发布到MQ，确保至少一次投递。

## Keywords

`DDD domain design`, `领域建模`, `aggregate design`, `聚合设计`, `bounded context`, `限界上下文`, `entity`, `value object`, `值对象`, `domain event`, `领域事件`, `event storming`, `aggregate root`, `聚合根`, `consistency boundary`, `一致性边界`, `context mapping`, `上下文映射`, `Anti-Corruption Layer`, `防腐层`, `ubiquitous language`, `代码映射`, `DO DTO VO PO`, `六边形架构`, `领域服务`, `聚合反模式`, `领域不变式`, `持久化策略`, `最终一致性`, `outbox pattern`, `CQRS`, `BC划分决策树`

## References

| File | Purpose |
|------|---------|
| [references/clean-ddd-hexagonal-strategic.md](references/clean-ddd-hexagonal-strategic.md) | DDD 战略设计—限界上下文、上下文映射、集成模式 |
| [references/clean-ddd-hexagonal-tactical.md](references/clean-ddd-hexagonal-tactical.md) | DDD 战术设计—Entity/VO/Aggregate/Repository/Domain Event |
| [references/ddd-tactical.md](references/ddd-tactical.md) | 战术模式补充—聚合内部构造、实体/值对象代码模板 |
| [references/code-model-mapping.md](references/code-model-mapping.md) | 代码模型目录结构、对象映射表、分层策略 |
| [references/advanced-tactical-patterns.md](references/advanced-tactical-patterns.md) | 进阶战术—Factory/Specification/Domain Service |
| [references/domain-event-catalog.md](references/domain-event-catalog.md) | 领域事件设计指南—分类、数据结构、发布策略 |
| [references/bounded-context-mapping.md](references/bounded-context-mapping.md) | 7种映射模式详解—决策树、Mermaid模板、代码示例 |
| [references/persistence-strategies.md](references/persistence-strategies.md) | 值对象持久化策略—Inline/JSON/Embeddable决策树 |
| [references/domain-invariants.md](references/domain-invariants.md) | 领域不变式设计—分类、实现模式、规格模式、文档模板 |
| [references/guides/partme-13-code-model-1.md](references/guides/partme-13-code-model-1.md) | 代码模型(上)—DDD微服务代码模型设计 |
| [references/guides/partme-14-code-model-2.md](references/guides/partme-14-code-model-2.md) | 代码模型(下)—领域模型与代码模型一致性保证 |

## Examples

| File | Domain |
|------|--------|
| [examples/ecommerce-domain.md](examples/ecommerce-domain.md) | 电商平台 |
| [examples/banking-domain.md](examples/banking-domain.md) | 银行系统 |
| [examples/insurance-domain.md](examples/insurance-domain.md) | 保险业务 |
| [examples/order-fulfillment-domain.md](examples/order-fulfillment-domain.md) | 订单履约 |
| [examples/healthcare-domain.md](examples/healthcare-domain.md) | 医疗健康 |
| [examples/payment-domain.md](examples/payment-domain.md) | 支付系统 |
| [examples/logistic-domain.md](examples/logistic-domain.md) | 物流运输 |

## Security & Safety

This skill is pure documentation. It does not collect user data, does not access external services or networks, and contains no executable scripts.
