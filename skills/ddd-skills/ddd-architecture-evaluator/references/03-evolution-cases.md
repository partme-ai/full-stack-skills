# Architecture Evolution — Real-World Cases

## Case 1: E-Commerce Platform — MVC to DDD Layered

**Context**: 3-year old e-commerce platform, 15 developers, Spring Boot + MyBatis.

**Initial State**: Traditional 3-layer MVC. OrderService has 2,500 lines. Entity classes are anemic.

**Trigger for Evaluation**: New feature (flash sales) requires complex inventory logic. Monolithic OrderService is the bottleneck.

**Evaluation Result**:
- Maturity: Level 2 (Aware) — partial value objects, no aggregates
- Debt: 52 (Moderate 🟠)
- Recommendation: DDD Layered + Strangler Fig

**Evolution Phases**:

```
Phase 1 (2 weeks): Extract core aggregates
  → Order aggregate: Order(shipTo, items, total, status)
  → Inventory aggregate: Inventory(sku, quantity, reserved)
  → Cut circular dependency between Order ↔ Inventory

Phase 2 (3 weeks): Rich domain model
  → Order.pay(), Order.cancel(), Order.ship()
  → Value objects: Money, OrderStatus, ShippingAddress
  → Domain events: OrderPlaced, PaymentConfirmed

Phase 3 (4 weeks): Bounded context split
  → Order BC: order-service (new)
  → Inventory BC: inventory-service (new)
  → Payment BC: payment-service (new)
  → Event communication via RabbitMQ

Phase 4 (2 weeks): CQRS L1 for order read model
  → OrderQueryService (optimized for listing/aggregation)
  → Shared write DB, dedicated read views
```

**Outcome After 3 Months**:
- Maturity: Level 3 (Applied)
- Debt: 18 (Healthy 🟢)
- New feature delivery: 2 weeks → 4 days
- Team confidence: High

## Case 2: FinTech Core — Hexagonal Migration

**Context**: 8-year old banking core system, 50+ developers, multiple integration points.

**Initial State**: Monolith with EJB + Oracle PL/SQL stored procedures. Business logic in DB.

**Trigger for Evaluation**: Regulatory requirement changes every 6 months. Current system takes 3 months to implement any change.

**Evaluation Result**:
- Maturity: Level 1 (Ad Hoc)
- Debt: 78 (Severe 🔴)
- Recommendation: Hexagonal Architecture + Strangler Fig over 12 months

**Evolution Phases**:

```
Phase 1 (2 months): Port identification
  → Define inbound ports (UseCases) for top 5 core flows
  → Define outbound ports (AccountRepository, LedgerGateway)
  → Create anti-corruption layer for legacy EJB

Phase 2 (3 months): Account domain — first port
  → New Account aggregate in Hexagonal style
  → Parallel run: new system reads from legacy, writes to new DB
  → Canary release for account balance queries (non-critical reads)

Phase 3 (4 months): Transaction domain
  → Transaction aggregate + Event Sourcing for audit trail
  → CQRS L2: write DB (EventStore) + read DB (Postgres materialized views)
  → Integration with external settlement systems via outbound ports

Phase 4 (3 months): Full cutover
  → Migrate remaining flows (interest calculation, fee assessment)
  → Sunset legacy modules after 6-month parallel run
  → Architectural fitness monitoring dashboard
```

**Outcome After 12 Months**:
- Maturity: Level 4 (Scaled)
- Debt: 28 (Mild 🟡)
- Regulatory change implementation: 3 months → 3 weeks

## Case 3: SaaS Platform — COLA to Event-Driven

**Context**: Fast-growing SaaS startup, 20 developers, rapid feature iteration.

**Initial State**: COLA v4 architecture, well-structured, but cross-module coupling growing.

**Trigger for Evaluation**: User sync between modules causes cascading failures. Team wants decoupled event-driven architecture.

**Evaluation Result**:
- Maturity: Level 3 (Applied)
- Debt: 15 (Healthy 🟢) — well-maintained, but cross-module coupling identified
- Recommendation: Add event bus + gradually migrate to event-driven cross-BC communication

**Evolution**:
```
Phase 1 (2 weeks): Introduce DomainEventBus (in-process)
Phase 2 (4 weeks): Extract first event-driven flow (UserCreated → ProvisionTenant)
Phase 3 (6 weeks): Replace direct module calls with events
Phase 4 (ongoing): Add resilience patterns (dead letter, retry, idempotency)
```
