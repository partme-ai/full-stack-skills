# Case Study: SaaS Startup Architecture Evolution

## Project Context

| Dimension | Phase 1 (0-6 months) | Phase 2 (6-18 months) | Phase 3 (18+ months) |
|-----------|---------------------|----------------------|----------------------|
| **Team** | 3 developers (2 backend, 1 frontend) | 8 developers | 20 developers |
| **DDD Experience** | None | 2 members trained in DDD | 5 members with DDD exp |
| **Business Complexity** | Simple CRUD + basic workflows | Moderate: subscription logic, usage metering | High: multi-product billing, partner integrations |
| **Tech Stack** | Python + Django + PostgreSQL | Python + FastAPI + PostgreSQL + Redis | Python + Go hybrid + PostgreSQL + Kafka |
| **Entry Points** | Single REST API | REST API + basic webhooks | REST API + webhooks + MQ events + scheduled jobs |
| **Funding Stage** | Pre-seed | Series A | Series B+ |

## Decision Process (Evolutionary)

### Phase 1: Pre-seed — Get to Market Fast

**Context**: MVP needs to ship in 3 months. Team of 3, no DDD knowledge.

**Decision**: Standard Layered Architecture (Django MVC)

```
No DDD, no architecture over-engineering priority.
Controller (Django views) → Service → Model (ORM)
```

**CQRS Level**: L0 — Single model, single DB

### Phase 2: Series A — Introduce Structure

**Context**: Product validated, team growing, subscription logic getting complex. Must refactor.

**Migration**: Layered → Hexagonal Architecture (progressive)

```
Phase 2a: Identify aggregates (Subscription, Usage, Invoice)
Phase 2b: Extract Repository interfaces to Domain layer
Phase 2c: Extract UseCase interfaces (Ports)
Phase 2d: Migrate controllers → Adapters (keep backward compat)
```

**CQRS Level**: L1 — Model Separation (Usage tracking is write-heavy, reporting is read-heavy)

**Architecture Decision**: **Hexagonal** chosen because:
- Python's FastAPI has good adapter pattern support
- Webhook entry points are growing
- Testability needed for subscription billing logic

### Phase 3: Series B+ — Scale and Standardize

**Context**: 20-person team, event-driven integrations, partner ecosystem.

**Evolution**: Hexagonal per microservice + CQRS L2 for high-volume paths

```
Microservices split by bounded context:
  ├── Subscription Service (Hexagonal + CQRS L1)
  ├── Usage Metering Service (Hexagonal + CQRS L2 — high write volume)
  ├── Billing Service (Hexagonal + Event Sourcing)
  ├── Invoice Service (Hexagonal)
  ├── Partner Integration Service (Hexagonal)
  └── Notification Service (Layered — Generic domain)
```

## Lessons Learned

1. **Right-time architecture**: Phase 1 Layered was the correct choice for MVP speed. Introducing Hexagonal in Phase 1 would have wasted 2-3 months.
2. **Progressive migration works**: The Strangler Fig approach (new features in Hexagonal, old in Layered) allowed continuous delivery during refactoring.
3. **CQRS upgrade driven by data**: Usage metering reached 50K writes/second → L2 DB separation was a data-driven decision, not an architectural preference.
4. **Team DDD maturity matters**: Hexagonal adoption only succeeded because 2 developers completed DDD training before Phase 2 migration.

## Final Recommendation Summary

| Phase | Architecture | CQRS | Key Decision Driver |
|-------|-------------|------|-------------------|
| Pre-seed | Layered | L0 | Speed to market |
| Series A | Hexagonal | L1 | Testability + multi-entry |
| Series B+ | Hexagonal (per service) | L1-L3 | Scalability + event-driven |

## Next Steps

1. Phase 1 → No architecture skill needed (standard Django MVC)
2. Phase 2 migration → [ddd-architecture-hexagonal](../ddd-architecture-hexagonal/) for Port/Adapter pattern
3. Phase 2 CQRS → [ddd-cqrs-architecture](../ddd-cqrs-architecture/) for L1 model separation
4. Phase 3 scaling → [ddd-architecture-evaluator](../ddd-architecture-evaluator/) for migration readiness assessment
