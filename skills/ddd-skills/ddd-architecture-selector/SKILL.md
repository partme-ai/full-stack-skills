---
name: ddd-architecture-selector
description: Architecture selection decision guide — help users choose from 5 DDD architectures (Layered/Onion/Hexagonal/Clean/COLA) with decision matrix, team size mapping, domain classification (core/generic/supporting), microservice splitting recommendation, and CQRS level suggestion. Use when user asks about architecture selection, 架构选型, COLA vs 六边形, cleaner architecture vs onion, 微服务拆分, or which architecture to use.
license: Apache-2.0
---

# DDD Architecture Selector

Architecture selection decision guide that evaluates 5 DDD architecture patterns (Layered, Onion, Hexagonal, Clean, COLA) against project context — team size, business complexity, tech stack, infrastructure change frequency, and ecosystem preference.

## Workflow

### Step 1: Collect Project Context
- Team size & DDD experience level
- Business complexity (simple CRUD / moderate / high)
- Technical stack (Spring Boot / Go / Node.js / .NET / Python)
- Infrastructure change frequency (low / medium / high)
- Multi-entry needs (REST + CLI + MQ + gRPC?)
- Test coverage requirements (unit / integration / E2E)
- Ecosystem preference (Chinese community / international)

### Step 2: Run Decision Matrix
- Compare 5 architectures across 7+ dimensions

### Step 3: Apply Decision Tree
- Complexity → Team Size → Tech Stack → Recommended Architecture

### Step 4: Recommend CQRS Level
- L0: None, L1: Model Separation, L2: DB Separation, L3: Event Sourcing

### Step 5: Classify Domain Types
- Core / Generic / Supporting → Apply different architectures per domain

### Step 6: Suggest Microservice Splitting
- One BC → One Service, with merge/split rules

### Step 7: Route to Specific Architecture Skill
- Link to detailed implementation guidance

## When to Use (and When NOT to)

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| Starting a new project: need architecture decision | Architecture already decided → go directly to that skill |
| Comparing multiple DDD architectures | Just need DDD learning → use `ddd-architecture-awesome` |
| Team unsure which approach fits best | Need architecture evaluation of existing project → use `ddd-architecture-evaluator` |
| Planning microservice splitting strategy | Need domain modeling after selection → use `ddd-domain-designer` |
| Evaluating CQRS necessity | Non-DDD project evaluation (consider standard MVC) |
| Chinese enterprise team making tech decisions | Simple CRUD with no DDD needed → use standard MVC |
| Team size / DDD maturity unknown | Need code review of existing DDD code → use `ddd-code-reviewer` |

## Boundary

| Category | Description | Alternative |
|----------|-------------|------------|
| ✅ **Handles** | New project architecture selection (5 DDD architectures) | — |
| ✅ **Handles** | Architecture comparison for migration decisions | — |
| ✅ **Handles** | CQRS / Event Sourcing necessity assessment | — |
| ✅ **Handles** | Domain classification (Core / Generic / Supporting) | — |
| ✅ **Handles** | Microservice splitting based on bounded contexts | — |
| ✅ **Handles** | Team size → architecture mapping | — |
| ⚠️ **Requires** | Basic project context: team size, business complexity, tech stack | — |
| ⚠️ **Requires** | Domain expert or product owner involvement for classification | — |
| ❌ **Out of Scope** | Architecture already decided — do not use this skill | [ddd-architecture-layered](../ddd-architecture-layered/) / [onion](../ddd-architecture-onion/) / [hexagonal](../ddd-architecture-hexagonal/) / [clean](../ddd-architecture-clean/) / [cola](../ddd-architecture-cola/) |
| ❌ **Out of Scope** | Just need DDD learning & concepts — should not use this skill | [ddd-architecture-awesome](../ddd-architecture-awesome/) |
| ❌ **Out of Scope** | Evaluate existing architecture health & quality — do not use | [ddd-architecture-evaluator](../ddd-architecture-evaluator/) |
| ❌ **Out of Scope** | Domain modeling / aggregate design after selection — not use | [ddd-domain-designer](../ddd-domain-designer/) |
| ❌ **Out of Scope** | Code review for DDD compliance — do not use this skill | [ddd-code-reviewer](../ddd-code-reviewer/) |
| ❌ **Out of Scope** | Non-DDD / standard MVC projects — not use this skill | Use standard MVC guides (not DDD skills) |

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## Rules

1. Architecture selection must evaluate at least 5 dimensions.
2. Never recommend Event Sourcing as default — only after L2 CQRS success.
3. Team size and domain complexity must be the primary selection factors.

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

| Architecture | Best For | Avoid When |
|-------------|----------|------------|
| **Layered** | Simple CRUD, small teams, traditional MVC migration | Complex business rules, frequent infra changes |
| **Onion** | High test coverage, changing infrastructure | CRUD-heavy apps, teams with no abstraction experience |
| **Hexagonal** | Multi-entry systems, microservice standardization | Simple single-entry CRUD, quick prototypes |
| **Clean** | Large enterprise systems, strict physical isolation | Small teams (<5), rapid MVP iterations |
| **COLA** | Chinese Spring Boot ecosystem, engineering standards | Non-Java stacks, international teams |

## 3-Step Decision Tree

### Step 1: Assess Business Complexity

```
Business Complexity?
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
    ├── Enterprise / international team?              → CLEAN ARCHITECTURE
    ├── Chinese enterprise, per-service standards?     → COLA (multi-module)
    ├── Mixed tech stack per service?                 → HEXAGONAL per service
    └── Need microservice + standard per module?      → COLA + HEXAGONAL hybrid
```

### Step 2: Match Team Size

| Team Size | Recommended Architecture | Rationale |
|-----------|------------------------|-----------|
| 1-5 | Layered or COLA simplified | Lowest ceremony, fastest delivery |
| 5-15 | Hexagonal / Onion / COLA (single module) | Balance abstraction and productivity |
| 15-50 | Clean / COLA (multi-module) | Physical isolation, parallel team work |
| 50+ | Microservices + Hexagonal per service | Autonomous teams, independent deploy |

**Evolution Path**: Team grows → upgrade architecture progressively: 1-5 (Layered) → 5-15 (Hexagonal) → 15-50 (Clean/COLA) → 50+ (Microservices+Hex).

### Step 3: Final Recommendation

| If you have... | Then choose... | Why |
|---------------|---------------|-----|
| Spring Boot + MyBatis + Chinese team | **COLA** | Ecosystem match, Chinese docs, scaffolding |
| Multi-entry (REST + CLI + MQ + gRPC) | **Hexagonal** | Adapter pattern handles multiple entry points |
| Strict module physical isolation, large enterprise | **Clean** | Entity → UseCase → Adapter enforced isolation |
| Infrastructure changes often (DB, MQ swap) | **Hexagonal** or **Onion** | Port/Adapter makes swapping trivial |
| Rapid prototype → evolve DDD later | **Layered** → upgrade | Lowest startup cost, clear evolution path |
| Complex business rules + TDD | **Hexagonal** | Domain layer independently testable |
| Team new to DDD, incremental adoption | **Layered** | Closest to traditional 3-tier, gentlest learning curve |
| Microservice internal architecture standard | **Hexagonal** + **COLA** per service | Port isolation + engineering standards |
| Read-heavy, complex queries | **CQRS L2** | Read/write separation, independent optimization |
| Full audit trail needed | **Event Sourcing** (L3) | Event stream naturally supports audit |

## Domain Partitioning + Microservice Splitting

### Domain Classification (Core / Generic / Supporting)

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

| Selected | Next Skill |
|----------|-----------|
| Layered | [ddd-architecture-layered](../ddd-architecture-layered/) |
| Onion | [ddd-architecture-onion](../ddd-architecture-onion/) |
| Hexagonal | [ddd-architecture-hexagonal](../ddd-architecture-hexagonal/) |
| Clean | [ddd-architecture-clean](../ddd-architecture-clean/) |
| COLA | [ddd-architecture-cola](../ddd-architecture-cola/) |

Related: [ddd-cqrs-architecture](../ddd-cqrs-architecture/), [ddd-domain-designer](../ddd-domain-designer/), [ddd-architecture-evaluator](../ddd-architecture-evaluator/)

## Gotchas

See [references/gotchas.md](references/gotchas.md) for 15 pitfalls.

## FAQ

See [references/faq.md](references/faq.md) for 15 Q&A.

## Security & Safety

This skill is pure documentation. It does not collect user data, does not access external services or networks, and contains no executable scripts.

## References

See [references/](references/) for deep comparisons, microservice/domain, clean+DDD+hexagonal, ddd4j analysis, gotchas, FAQ, external resources, and 5 case studies.
