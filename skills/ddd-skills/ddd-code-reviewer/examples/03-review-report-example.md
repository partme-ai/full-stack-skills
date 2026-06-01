# DDD Code Review Report — Order Service

**Project**: partme-order-service
**Review Date**: 2026-05-29
**Scope**: Order aggregate, Payment aggregate, Application services

## Overall Score: 62/100 (🟠 C)

### Dimension Breakdown

| Dimension | Score | Weight | Weighted | Status |
|-----------|:-----:|:------:|:--------:|:------:|
| Layering Compliance | 55/100 | 30% | 16.5/30 | ⚠️ |
| Domain Model Quality | 50/100 | 30% | 15.0/30 | ⚠️ |
| Naming Conventions | 80/100 | 15% | 12.0/15 | ✅ |
| Code Structure | 70/100 | 15% | 10.5/15 | ⚠️ |
| Test Coverage | 80/100 | 10% | 8.0/10 | ✅ |
| **Total** | | **100%** | **62/100** | **🟠 C** |

---

### 1. Layering Compliance (16.5/30)

| Check Item | Result | Note |
|------------|:------:|------|
| Domain zero framework dependency | ❌ | `Order.java:1` imports `javax.persistence.Entity` |
| No reverse dependency | ✅ | Domain does not import infrastructure |
| App layer no SQL | ❌ | `OrderAppService.java:45` calls `orderMapper.selectByStatus()` |
| Controller no business logic | ✅ | Controller only does protocol conversion |
| Repository returns aggregate root | ⚠️ | `OrderSummaryRepository` returns DTO instead of Aggregate |
| No circular dependencies | ✅ | Modules layering is clean |

### 2. Domain Model Quality (15.0/30)

| Check Item | Result | Note |
|------------|:------:|------|
| Rich model coverage | ⚠️ | 3/5 entities have business methods (60%) |
| Value Object usage | ❌ | Only `Money` used. `status` is `String`, `email` is `String` |
| Aggregate design | ⚠️ | `OrderAggregate` has 6 entities (exceeds 5 limit) |
| Domain events | ❌ | No domain events found. `pay()` does not emit `OrderPaidEvent` |
| VO immutability | ⚠️ | `Address` has setters |

### 3. Naming Conventions (12.0/15)

| Check Item | Result | Note |
|------------|:------:|------|
| Aggregate Root naming | ✅ | `Order`, `Payment`, `Product` |
| Repository naming | ✅ | `OrderRepository`, `PaymentRepository` |
| Domain Service naming | ⚠️ | `OrderUtilService` → should be `OrderPricingService` |
| Domain Event naming (past tense) | ❌ | `OrderPay` → should be `OrderPaid` |
| Package by aggregate | ✅ | Organized as `domain/order/`, `domain/payment/` |

### 4. Code Structure (10.5/15)

| Check Item | Result | Note |
|------------|:------:|------|
| Aggregate Root < 200 lines | ✅ | All under 200 lines |
| Service < 100 lines | ❌ | `OrderService.java` is 487 lines |
| Cyclomatic complexity < 10 | ⚠️ | `OrderService.calculateDiscount()` has complexity 15 |
| Package organization | ✅ | Aggregates have clear boundaries |
| Exception handling | ⚠️ | Mixed domain exceptions and runtime exceptions |

### 5. Test Coverage (8.0/10)

| Check Item | Result | Note |
|------------|:------:|------|
| Domain unit test coverage | ✅ | ~85% methods tested |
| Aggregate root behavior tests | ⚠️ | `Order.confirm()` edge cases not tested |
| Domain event assertion | ✅ | Events verified in `Order.create()` test |

---

### Anti-Pattern List

| Severity | Anti-Pattern | File:Line | Fix Suggestion |
|:---------:|-------------|-----------|---------------|
| P0 | Domain layer framework dependency | `Order.java:1` | Remove `@Entity`, use POJO + separate JPA entity |
| P0 | God Service | `OrderService.java:45-320` | Split into `OrderPricingService` + `OrderFulfillmentService` |
| P0 | Missing domain events | `Order.java:55-70` | Add `OrderPaidEvent` to `pay()` method |
| P1 | App layer has SQL | `OrderAppService.java:45` | Move `orderMapper` call to Repository implementation |
| P1 | Controller business logic | `OrderController.java:88-92` | Move status check into `Order.pay()` |
| P1 | Mutable Value Object | `Address.java` | Make fields final, remove setters |
| P2 | Oversized aggregate | `OrderAggregate` | Split off `OrderLog` into separate aggregate |

### Improvement Suggestions

**Immediate (P0)**:
1. Remove `javax.persistence.Entity` from `Order.java` — 0.5h
2. Extract God Service `OrderService` → 2 domain services — 2h
3. Add `OrderPaidEvent` to `Order.pay()` — 1h

**Short-term (P1)**:
1. Move SQL from `OrderAppService.java` to `JpaOrderRepository` — 1h
2. Replace `String status` with `OrderStatus` Value Object — 1.5h
3. Make `Address` immutable (final fields, no setters) — 0.5h

**Long-term (P2)**:
1. Split `OrderLog` from `OrderAggregate` — 3h
2. Add integration tests for repository implementations — 4h
3. Add ArchUnit tests to CI pipeline — 2h

---

### Summary

The project has a solid structural foundation (correct package organization, good naming conventions) but suffers from critical DDD violations: the domain layer is contaminated with JPA annotations, business logic is centralized in a God Service, and key domain events are missing. A focused 2-day refactoring sprint can bring this to a B grade.
