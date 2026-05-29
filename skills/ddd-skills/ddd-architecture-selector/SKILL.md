---
name: ddd-architecture-selector
description: Architecture selection decision guide — help users choose from 5 DDD architectures (Layered/Onion/Hexagonal/Clean/COLA) with decision matrix, team size mapping, domain classification (core/generic/supporting), microservice splitting recommendation, and CQRS level suggestion. Use when user asks about architecture selection, 架构选型, COLA vs 六边形, cleaner architecture vs onion, 微服务拆分, or which architecture to use.
license: Apache-2.0
---

# DDD Architecture Selector

Architecture selection decision guide that evaluates 5 DDD architecture patterns (Layered, Onion, Hexagonal, Clean, COLA) against project context — team size, business complexity, tech stack, infrastructure change frequency, and ecosystem preference.

## Workflow

```
1. Collect Project Context
   ├── Team size & DDD experience level
   ├── Business complexity (simple CRUD / moderate / high)
   ├── Technical stack (Spring Boot / Go / Node.js / .NET / Python)
   ├── Infrastructure change frequency (low / medium / high)
   ├── Multi-entry needs (REST + CLI + MQ + gRPC?)
   ├── Test coverage requirements (unit / integration / E2E)
   └── Ecosystem preference (Chinese community / international)

2. Run Decision Matrix
   └── Compare 5 architectures across 7+ dimensions

3. Apply Decision Tree
   └── Complexity → Team Size → Tech Stack → Recommended Architecture

4. Recommend CQRS Level
   └── L0: None, L1: Model Separation, L2: DB Separation, L3: Event Sourcing

5. Classify Domain Types
   └── Core / Generic / Supporting → Apply different architectures per domain

6. Suggest Microservice Splitting
   └── One BC → One Service, with merge/split rules

7. Route to Specific Architecture Skill
   └── Link to detailed implementation guidance
```

## When to Use (and When NOT to)

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| Starting a new project: need architecture decision | Already decided on architecture — go directly to that skill |
| Comparing multiple DDD architectures | Just need DDD learning — use `ddd-architecture-awesome` |
| Team unsure which approach fits best | Simple CRUD no DDD needed — use standard MVC |
| Planning microservice splitting strategy | Evaluating existing architecture health — use `ddd-architecture-evaluator` |
| Evaluating CQRS necessity | Non-DDD project evaluation |
| Chinese enterprise team decision | Need domain modeling after selection — use `ddd-domain-designer` |

**ALWAYS trigger when user mentions:**
- `架构选型` / `选架构` / `哪种架构` / `architecture selection`
- `COLA vs 六边形` / `整洁架构 vs 洋葱` / `Layered vs Hexagonal`
- `微服务拆分` / `怎么拆微服务` / `domain partitioning`
- `团队5人用什么架构` / `team size architecture`
- `CQRS 要不要` / `分层策略` / `项目结构怎么定`
- Questions comparing multiple DDD architecture styles

## 5-Architecture Decision Matrix

| Dimension | Layered | Onion | Hexagonal | Clean | COLA |
|-----------|:--:|:--:|:--:|:--:|:--:|
| **Learning Cost** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ |
| **Business Complexity Fit** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| **CRUD Efficiency** | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★☆ |
| **Infrastructure Replaceability** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ |
| **Test Friendliness** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| **Chinese Community** | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★★ |
| **Code Generation Support** | Good | Poor | Poor | Poor | Excellent |
| **Module Physical Isolation** | Low | Medium | Medium | High | High |
| **Evolution Path Clarity** | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| **Team Size Fit** | 1-5 | 5-15 | 5-15 | 15-50 | 5-50 |
| **Origin** | Martin Fowler | Jeffrey Palermo (2008) | Alistair Cockburn (2005) | Robert C. Martin (2012) | Alibaba (2018) |

### Dimension Details

| Architecture | Best For | Avoid When |
|-------------|----------|------------|
| **Layered** | Simple CRUD, small teams, traditional MVC migration | Complex business rules, frequent infra changes |
| **Onion** | High test coverage required, changing infrastructure | CRUD-heavy apps, teams with no abstraction experience |
| **Hexagonal** | Multi-entry systems, microservice standardization | Simple single-entry CRUD, quick prototypes |
| **Clean** | Large enterprise systems, strict physical isolation | Small teams, rapid MVP iterations |
| **COLA** | Chinese Spring Boot ecosystem, need engineering standards | Non-Java stacks, international teams |

### Architecture Selection Flowchart

```
Project Business Complexity?
│
├── Simple CRUD (80%+ CRUD operations)
│   └── Planning DDD adoption in future?
│       ├── No  → LAYERED ARCHITECTURE
│       └── Yes → COLA Simplified (single module)
│
├── Moderate (core business logic with rules)
│   ├── Chinese ecosystem / Spring Boot + MyBatis?   → COLA
│   ├── Value domain layer purity most?               → HEXAGONAL
│   ├── Multi-entry system (REST + CLI + MQ)?         → HEXAGONAL
│   ├── Infrastructure changes often?                 → HEXAGONAL / ONION
│   └── .NET / Python stack?                          → ONION
│
└── High (multiple BCs, microservices)
    ├── Enterprise / international team?               → CLEAN ARCHITECTURE
    ├── Chinese enterprise, per-service standards?     → COLA (multi-module)
    ├── Mixed tech stack per service?                  → HEXAGONAL per service
    └── Need microservice + standard per module?       → COLA + HEXAGONAL hybrid
```

### Team Size → Architecture Mapping

```
Team 1-5   → Layered (simple CRUD) or COLA simplified
Team 5-15  → Hexagonal / Onion / COLA (single module)
Team 15-50 → Clean / COLA (multi-module)
Team 50+   → Microservices + Hexagonal per service (COLA or Clean internally)

Progression Path:
  Team grows → upgrade architecture
  1-5 (Layered) → 5-15 (Hexagonal) → 15-50 (Clean/COLA) → 50+ (Microservices+Hex)
```

## Domain Partitioning Guide

### Three Domain Types — Apply Different Architectures

| Domain Type | Investment Strategy | Architecture Recommendation | Examples |
|-------------|-------------------|---------------------------|----------|
| **Core Domain** (核心域) | Max investment, build in-house | Hexagonal / Clean / COLA with rich domain model | Order management, Payment processing, Pricing engine |
| **Generic Domain** (通用域) | Purchase or open-source reuse | Layered or off-the-shelf SaaS | Authentication, Authorization, Notification |
| **Supporting Domain** (支撑域) | Outsource or low priority | Layered or simple CRUD | Reports, Admin dashboard, Data export |

**Key rule**: Don't apply Hexagonal or Clean to generic/supporting domains — it wastes effort. Reserve complex architectures for Core domains only.

### Microservice Splitting Rules

1. **Default**: One Bounded Context → One Microservice
2. **Split when**: Different deployment cadence, different scaling needs, different team ownership
3. **Merge when**: Strong transactional consistency needed, small context (< 2 weeks dev), same team
4. **Start conservative**: Fewer services, split as needed (proven by need, not anticipation)
5. **Communication**: Events for eventual consistency, RPC for strong consistency (rare)

## CQRS Level Suggestion

| Level | Description | Cost | Architecture Support | When to Use |
|-------|-------------|------|---------------------|-------------|
| **L0 — None** | Single model, single DB | Zero | All architectures (default) | Simple CRUD, no read/write conflict |
| **L1 — Model Separation** | CommandService + QueryService, shared DB | Low | All architectures | Moderate read/write disparity |
| **L2 — DB Separation** | Command DB + Read DB (ES/slave), sync via events | Medium | Hexagonal / Clean / COLA | High read volume, complex queries |
| **L3 — Event Sourcing** | Event Store + Projections, full event replay | High | Hexagonal / Clean | Audit trail, temporal queries, compliance |

**Recommendation**: Start at L0, prove need for higher levels. L2+ should only be adopted alongside Hexagonal or Clean architectures for proper port isolation.

## Architecture Skill Navigation

| Selected Architecture | Next Skill | Key Content |
|----------------------|-----------|-------------|
| Layered | [ddd-architecture-layered](../ddd-architecture-layered/) | DDD 4-layer: Interface → App → Domain → Infra |
| Onion | [ddd-architecture-onion](../ddd-architecture-onion/) | Core → Application → Infrastructure nesting |
| Hexagonal | [ddd-architecture-hexagonal](../ddd-architecture-hexagonal/) | Ports & Adapters, UseCase interfaces |
| Clean | [ddd-architecture-clean](../ddd-architecture-clean/) | Entity → UseCase → Adapter → Framework |
| COLA | [ddd-architecture-cola](../ddd-architecture-cola/) | COLA v5 creator + validator integrated |

**Related skills**:
- [ddd-cqrs-architecture](../ddd-cqrs-architecture/) — CQRS deep-dive after level selection
- [ddd-domain-designer](../ddd-domain-designer/) — Domain modeling after architecture selection

## Architecture Selection Report Template

When providing results, output in this structure:

```markdown
## Architecture Selection Report

### Project Context Summary
- Team: {size}, DDD experience: {level}
- Business complexity: {simple/moderate/high}
- Technical stack: {stack}
- Infrastructure change frequency: {low/medium/high}

### Recommendation
- **Primary**: {architecture name}
- **CQRS Level**: {none/L1/L2/L3}
- **Layering Strategy**: {strict/loose}

### Decision Rationale
1. {reason 1 — matches team size}
2. {reason 2 — matches business complexity}
3. {reason 3 — ecosystem preference}

### Domain Partitioning
| Domain | Type | Bounded Context | Architecture | Priority |
|--------|------|-----------------|-------------|----------|
| Order | Core | Order BC | Hexagonal | P0 |
| Auth | Generic | User BC | Layered | P2 |

### Next Steps
1. Proceed to [{architecture skill}]
2. Consider [{related skill}] for CQRS / domain modeling
```

## If-Then Scenario Quick Match

| If you have... | Then choose... | Why |
|---------------|---------------|-----|
| Spring Boot + MyBatis + Chinese team | **COLA** | Best ecosystem match, Chinese docs, scaffolding |
| Multi-entry (REST + CLI + MQ + gRPC) | **Hexagonal** | Adapter pattern naturally handles multiple entry points |
| Strict module physical isolation, large enterprise | **Clean** | Entity → UseCase → Adapter enforced isolation |
| Infrastructure changes often (DB, MQ swap) | **Hexagonal** or **Onion** | Port/Adapter makes swapping trivial |
| Rapid prototype → evolve DDD later | **Layered** → upgrade | Lowest startup cost, clear evolution path |
| Complex business rules + TDD | **Hexagonal** | Domain layer independently testable |
| Team new to DDD, incremental adoption | **Layered** | Closest to traditional 3-tier, gentlest learning curve |
| Microservice internal architecture standard | **Hexagonal** + **COLA** per service | Port isolation + engineering standards |
| Read-heavy, complex queries | **CQRS L2** | Read/write separation, independent optimization |
| Full audit trail needed | **Event Sourcing** (L3) | Event stream naturally supports audit |

## Gotchas — Common Pitfalls

- **Trend-chasing**: COLA is hot in Chinese community, but that doesn't mean it fits your project. A 2-person startup using COLA is over-engineering. Decision matrix beats community popularity every time.
- **CQRS forgotten**: Architecture selection without CQRS assessment is incomplete. Systems with high read/write disparity (reporting, search) must consider CQRS — it's independent of architecture choice.
- **Domain classification skipped**: Picking an architecture without Core/Generic/Supporting classification leads to uniform over-engineering. Core domains deserve rich models; generic ones don't.
- **Team capability mismatch**: Choosing Hexagonal when the team doesn't understand Port/Adapter, or Clean when nobody has used Interactor pattern. Pick an architecture the team can actually implement.
- **Single selection forever**: Assuming architecture is fixed once chosen. Real projects evolve: Layered → Hexagonal → CQRS as business complexity grows. Plan for evolution.
- **Dependency rule violations across all architectures**: Domain importing framework libraries, controllers directly calling repositories — these are P0 violations regardless of architecture choice.

## FAQ

**Q: 团队5人和50人的架构选择逻辑有什么本质区别？**
A: 5人团队的核心痛点是"快速交付"，推荐 Layered 或 COLA 简化版。50人团队的核心痛点是"协调成本"，推荐 Clean 或多模块 COLA 实现物理隔离。

**Q: CQRS 一定要和 Hexagonal/Clean 搭配吗？**
A: 理论上可以独立使用。但实践中 CQRS L2+（DB 分离）涉及同步机制（领域事件 → MQ → Query DB），只有 Hexagonal 或 Clean 的端口隔离能干净处理这种复杂度。Layered 搭配 CQRS 容易导致架构混乱。

**Q: 选好了架构，同一个项目里多个模块可以用不同架构吗？**
A: 可以。微服务架构下每个服务独立选型完全合理：Core 域用 Hexagonal，Generic 域用 Layered。COLA 官方也支持"Domain + App + Adapter + Infra"四层的模块级差异化。

**Q: 有没有推荐的从 Layered 到 Hexagonal 的渐进迁移路径？**
A: 推荐三步：Phase 1 在现有 Layered 中识别聚合边界，Phase 2 引入 Repository 接口（依赖倒置），Phase 3 逐步将 Service 层重构为 UseCase + Port。整个迁移不需要重写，Strangler Fig 模式。

**Q: COLA 和 Clean Architecture 的核心区别是什么？**
A: COLA 更工程化（有脚手架、代码生成、ArchUnit 自动化检查），Clean 更学术化（强调 Entity → UseCase 的层次纯度）。COLA 适合国内 Spring Boot 团队，Clean 适合国际化大型团队。

**Q: 微服务拆分粒度太细或太粗怎么办？**
A: 太细 → 合并事务边界（2个服务需要强一致性 → 合并）。太粗 → 按部署节奏和团队归属拆分。基本原则：一个 BC 一个服务，BC 大小由领域事件流自然界定。

## Keywords

架构选型, architecture selection, DDD architecture, Layered architecture, Onion architecture, Hexagonal architecture, Clean architecture, COLA, 分层架构, 洋葱架构, 六边形架构, 整洁架构, 微服务拆分, domain partitioning, CQRS level, 决策矩阵, decision matrix, 团队规模, team size, 域三分法, core domain, generic domain, supporting domain, bounded context, 限界上下文

## References

### Architecture Comparison & Deep Dives
- [references/architecture-deep-comparison.md](references/architecture-deep-comparison.md) — Hexagonal / Clean / COLA deep comparison, migration paths, DTO/VO/DO boundaries
- [references/comparison-matrix.md](references/comparison-matrix.md) — Quick decision matrix and scenario selection table
- [references/cheatsheet.md](references/cheatsheet.md) — Complexity ladder, universal dependency rule, per-architecture When-to-Use/When-NOT
- [references/per-architecture-guide.md](references/per-architecture-guide.md) — Each architecture's detailed decision path, upgrade route, common traps, unique advantages
- [references/reference-implementations.md](references/reference-implementations.md) — 6 languages × 5 architectures reference implementation repos and original papers

### Microservice & Domain Partitioning
- [references/partme-08-microservice-models.md](references/partme-08-microservice-models.md) — Microservice splitting models from PartMe DDD practice
- [references/partme-10-ddd-middle-platform.md](references/partme-10-ddd-middle-platform.md) — DDD middle platform architecture design
- [references/partme-19-principles.md](references/partme-19-principles.md) — DDD design principles and layered boundary guidelines
- [references/partme-20-distributed-qa.md](references/partme-20-distributed-qa.md) — Distributed architecture Q&A and common pitfalls

### clean-ddd-hexagonal Integration
- [references/clean-ddd-hexagonal-layers.md](references/clean-ddd-hexagonal-layers.md) — Complete four-layer structure with code templates
- [references/clean-ddd-hexagonal-strategic.md](references/clean-ddd-hexagonal-strategic.md) — DDD strategic patterns: bounded contexts, context mapping, subdomains
- [references/clean-ddd-hexagonal-hexagonal.md](references/clean-ddd-hexagonal-hexagonal.md) — Hexagonal Architecture ports & adapters reference with code examples
- [references/clean-ddd-hexagonal-cqrs.md](references/clean-ddd-hexagonal-cqrs.md) — CQRS & Domain Events: commands, queries, read models, outbox pattern

### Third-Party Deep Analysis
- [references/ddd4j-architecture-deep-dive.md](references/ddd4j-architecture-deep-dive.md) — DDD4J architecture selection deep dive and practical case studies

### Case Studies
- [examples/ecommerce-platform.md](examples/ecommerce-platform.md) — E-commerce platform architecture selection case
- [examples/fintech-billing.md](examples/fintech-billing.md) — Fintech billing system architecture selection case
- [examples/saas-startup-evolution.md](examples/saas-startup-evolution.md) — SaaS startup architecture evolution case
- [examples/enterprise-logistics.md](examples/enterprise-logistics.md) — Enterprise logistics platform architecture selection case

---

## Skill Boundary

### ✅ Handles
1. New project architecture selection guidance (5 DDD architectures)
2. Architecture comparison for migration decisions
3. CQRS and Event Sourcing necessity assessment
4. Domain classification (Core / Generic / Supporting)
5. Microservice splitting based on bounded contexts
6. Team size → architecture mapping

### ⚠️ Prerequisites
1. Basic project context: team size, business complexity, tech stack
2. Domain expert or product owner involvement for classification

### ❌ Out of Scope
1. Architecture already decided → use corresponding Architecture Skill directly
2. Just need DDD learning → use `ddd-architecture-awesome`
3. Evaluate existing architecture quality → use `ddd-architecture-evaluator`
4. Domain modeling after selection → use `ddd-domain-designer`

## Security & Stability

- Architecture selection is non-invasive analysis. It does NOT execute code or access systems.
- Technology recommendations are pattern-based, not vendor-specific. Choices depend on existing infrastructure.
- No executable scripts bundled. This skill provides decision frameworks and comparison matrices only.
