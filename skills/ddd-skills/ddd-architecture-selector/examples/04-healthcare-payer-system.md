# Case Study: Healthcare Payer System Architecture Selection

## Project Context

| Dimension | Detail |
|-----------|--------|
| **Team** | 10 developers (split across 2 squads: claims, provider network) |
| **DDD Experience** | Intermediate — team lead has DDD experience, 3 members trained |
| **Business Complexity** | High: claims adjudication rules, network contract management, regulatory compliance |
| **Tech Stack** | .NET 8 + C# + Entity Framework + SQL Server + RabbitMQ |
| **Infra Change Frequency** | Medium: potential DB migration (SQL Server → Cosmos DB for claims) |
| **Entry Points** | REST API + MQ events (from provider portal) + Batch (nightly claims processing) |
| **Ecosystem** | International (.NET ecosystem, no Chinese ecosystem preference) |
| **CQRS Need** | Moderate — claims processing is write-heavy, reporting is read-heavy |

## Decision Process

### Step 1: Matrix Evaluation

```
Business Complexity: High            → Onion / Hexagonal / Clean all fit
Team Size: 10                        → Onion (5-15) best match
Tech Stack: .NET 8 + EF Core         → Onion has strong .NET ecosystem alignment
Ecosystem: International              → Onion / Hexagonal
CQRS Need: Moderate                   → L1 adequate
Infra Change: Medium (DB swap)       → Onion's domain isolation handles this
```

### Step 2: Decision Tree Result

1. Business complexity: High → not simple CRUD
2. .NET ecosystem + intermediate DDD team → **Onion Architecture** primary recommendation
3. EF Core's DbContext pattern maps naturally to Onion's Repository + UnitOfWork
4. Moderate CQRS need → CQRS L1 — Model Separation

### Step 3: CQRS Assessment

- Read/write disparity: Moderate (claims reports are heavy read)
- **Recommendation: CQRS L1** — Model Separation
  - CommandService for write operations (claims submission, adjudication)
  - QueryService for read operations (claims status, provider reports)
  - Shared SQL Server database initially, project for DB separation later

### Step 4: Domain Classification

| Domain | Type | Architecture | Priority |
|--------|------|-------------|----------|
| Claims Adjudication | Core | Onion (rich domain model) | P0 |
| Provider Network | Core | Onion (rich domain model) | P0 |
| Member Eligibility | Core | Onion | P0 |
| Claims Payment | Core | Onion | P0 |
| User Auth | Generic | Layered (ASP.NET Identity) | P2 |
| Report Generation | Supporting | Simple Onion (read-only) | P2 |

## Final Recommendation

```
Primary Architecture: Onion Architecture
CQRS Level: L1 — Model Separation
Layering Strategy: Domain-centric with Core → Infrastructure dependency

Module Structure:
  ├── Claims.Domain / Claims.Core / Claims.Application / Claims.Infrastructure
  ├── Provider.Domain / Provider.Core / Provider.Application / Provider.Infrastructure
  ├── Member.Domain / Member.Core / Member.Application / Member.Infrastructure
  └── Payment.Domain / Payment.Core / Payment.Application / Payment.Infrastructure

Shared: Common.Domain (base types, domain primitives)
```

## Rationale

1. **Onion Architecture** aligns naturally with .NET's dependency inversion (interface-based DI)
2. **Domain Model as innermost circle** matches claims adjudication rule complexity
3. **EF Core Repositories** map to Onion's Repository pattern at Infrastructure layer
4. **CQRS L1** handles the moderate read/write disparity without Event Sourcing overhead
5. **Separate modules per domain** allows 2 squads to work in parallel
6. **DB migration support** — Onion's domain isolation means swapping SQL Server → Cosmos DB requires only Infrastructure changes

## Next Steps

1. Proceed to [ddd-architecture-onion](../ddd-architecture-onion/) for implementation
2. Claims Adjudication as first implementation module (highest domain complexity)
3. Set up dependency validation (NetArchTest) to enforce Onion layering
4. Revisit CQRS L2 evaluation when claims volume exceeds 1M/month
