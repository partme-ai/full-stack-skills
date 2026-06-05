# Case Study: Fintech Billing System Architecture Selection

## Project Context

| Dimension | Detail |
|-----------|--------|
| **Team** | 25 developers (split across 3 squads: billing, invoice, collection) |
| **DDD Experience** | Intermediate — 5 developers with DDD project experience |
| **Business Complexity** | High: complex billing rules, multi-currency, proration, tax calculation |
| **Tech Stack** | Java 17 + Spring Boot + PostgreSQL + Kafka |
| **Infra Change Frequency** | Low (regulated industry, changes are slow and audited) |
| **Entry Points** | REST API + Kafka events (from upstream order system) + Scheduled jobs |
| **Ecosystem** | International (no Chinese ecosystem preference) |
| **CQRS Need** | High — billing has heavy audit requirements, complex queries |
| **Compliance** | SOX compliance, full audit trail required |

## Decision Process

### Step 1: Matrix Evaluation

```
Business Complexity: High            → Hexagonal / Clean / COLA
Team Size: 25 (3 squads)             → Clean (best isolation), COLA also fits
Tech Stack: Java + Spring Boot + Kafka → Clean has strong Java support
Ecosystem: International              → Clean / Hexagonal preferred
Compliance: SOX audit trail          → CQRS L3 (Event Sourcing) needed
Entry Points: Multi (REST + Kafka + Scheduler) → Hexagonal
```

### Step 2: Decision Tree Result

1. Business complexity: High → enterprise-level architecture needed
2. International team + strict module isolation requirement → **Clean Architecture** primary recommendation
3. Audit trail → CQRS L3 with Event Sourcing

### Step 3: CQRS Assessment

- Read/write disparity: High (billing generates many read reports)
- Audit requirement: SOX compliance demands full audit trail
- **Recommendation: CQRS L3 — Event Sourcing**
  - Command side: Event Store (Kafka as event log)
  - Query side: Materialized views (PostgreSQL projections)
  - All billing operations recorded as event streams

### Step 4: Domain Classification

| Domain | Type | Architecture | Priority |
|--------|------|-------------|----------|
| Billing Engine | Core | Clean + Event Sourcing | P0 |
| Invoice Generation | Core | Clean + Event Sourcing | P0 |
| Collection Management | Core | Clean | P0 |
| Tax Calculation | Core | Clean | P0 |
| Customer Management | Generic | Layered | P2 |
| Report Generation | Supporting | Simple Clean (read-only) | P2 |

## Final Recommendation

```
Primary Architecture: Clean Architecture + Event Sourcing (CQRS L3)
Layering Strategy: Strict (physical module isolation)

Squad Structure:
  Squad A (Billing): Billing-core + Billing-usecase + Billing-adapter + Billing-framework
  Squad B (Invoice): Invoice-core + Invoice-usecase + Invoice-adapter + Invoice-framework
  Squad C (Collection): Collection-core + Collection-usecase + Collection-adapter + Collection-framework

Shared Kernel: Money, Currency, Rate (across all squads)
```

## Rationale

1. **Clean Architecture** provides the strictest module isolation, essential for 3 squads working in parallel
2. **Event Sourcing** meets SOX compliance requirement for full audit trail
3. **Separate modules per squad** allows independent development and deployment
4. **Generic domains simplified** to Layered to conserve effort
5. **Kafka as event store** aligns with existing infrastructure

## Next Steps

1. Proceed to [ddd-architecture-clean](../ddd-architecture-clean/) for Clean Architecture implementation
2. Follow with [ddd-cqrs-architecture](../ddd-cqrs-architecture/) for Event Sourcing deep-dive
3. Billing Engine as first implementation (highest complexity Core domain)
4. Define shared kernel module for Money, Currency value objects
5. Set up ArchUnit + commit hooks for dependency rule enforcement
