# DDD Code Review Checklist

Quick reference checklist for DDD code review sessions.

## P0 — Must Fix (Block Merge)

### Domain Purity
- [ ] Domain layer has ZERO Spring Framework imports
- [ ] Domain layer has ZERO JPA/Hibernate imports (`javax.persistence`, `jakarta.persistence`)
- [ ] Domain layer has ZERO MyBatis imports
- [ ] Domain layer has ZERO JDBC imports (`java.sql`)

### Dependency Direction
- [ ] Domain does not depend on Infrastructure
- [ ] Domain does not depend on Application
- [ ] Domain does not depend on Adapter
- [ ] No circular dependencies between modules
- [ ] Application layer does not depend on Adapter layer

### Anti-Patterns
- [ ] No God Service (> 500 lines, all business logic in one class)
- [ ] No Anemic Model (Entity with only getters/setters, no behavior)
- [ ] No Cross-Aggregate Direct References (use ID references only)
- [ ] No business logic in Controller layer
- [ ] Repository returns Aggregate Root, NOT DTO

## P1 — Should Fix (Before Next Release)

### Domain Model Quality
- [ ] Core aggregates have rich behavior methods
- [ ] Value Objects used instead of primitive types (Money, Email, Phone)
- [ ] Value Objects are immutable (final fields, no setters)
- [ ] Aggregate boundaries are reasonable (≤ 5 entities per aggregate)
- [ ] Domain Services only for cross-entity operations within same aggregate

### Naming Conventions
- [ ] Aggregate Root named after business concept (Order, not OrderEntity)
- [ ] Repository named `{Aggregate}Repository`
- [ ] Domain Service named `{BusinessConcept}Service` (OrderPricingService)
- [ ] Domain Events named in past tense (OrderPaid, not OrderPay)
- [ ] Package structure organized by aggregate, not by layer

### Layer Responsibility
- [ ] Application Service only orchestrates (no business if/else)
- [ ] Application Service has NO SQL/Database access
- [ ] Adapter layer has NO business logic
- [ ] Infrastructure Repository correctly maps PO ↔ Domain

## P2 — Nice to Have

### Domain Events
- [ ] Key business actions publish domain events
- [ ] Domain events carry complete context (not just IDs)
- [ ] Event handlers are idempotent

### Code Quality
- [ ] Aggregate Root class < 200 lines
- [ ] Service class < 100 lines
- [ ] Method cyclomatic complexity < 10
- [ ] No magic strings — use enums/constants

### Testing
- [ ] Aggregate Root has unit tests for all behavior methods
- [ ] Domain Service has unit tests with mocked repositories
- [ ] Repository has integration test with real database
- [ ] Domain events are verified in aggregate tests

## Common Fix Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| `order.setStatus("PAID")` in Service | `order.pay()` in Aggregate Root |
| `OrderService.pay(orderId)` 500 lines | Split into `OrderPricingService`, `OrderFulfillmentService` |
| `order.customer = customerObject` | `order.customerId = customer.getId()` |
| `import org.springframework.stereotype.Service` in Domain | Remove Spring dependency, use plain Java |
| `JdbcTemplate` in AppService | Move to Repository implementation |
| `if(status == "DRAFT")` in Controller | Move to Aggregate Root method |
