# Migration Guide: Layered Architecture → Clean Architecture

## Overview

Migrating from traditional 3-layer architecture (Controller → Service → Repository) to Clean Architecture (Enterprise → UseCase → Adapter → Framework) is a gradual process. This guide provides a step-by-step approach using the **Strangler Fig pattern**.

## Migration Complexity Assessment

```
Assessment Score:
  Low (1-5):   Direct migration, low risk
  Medium (6-10): Incremental migration, moderate risk
  High (11-15):  Phased migration over weeks/months
```

| Factor | Score | Assessment |
|--------|-------|------------|
| Codebase size | 1 (< 50K) / 2 (50-200K) / 3 (> 200K) | ____ |
| Test coverage | 1 (> 80%) / 2 (50-80%) / 3 (< 50%) | ____ |
| Team experience | 1 (Has Clean Architecture exp) / 2 (Has DDD exp) / 3 (New to DDD) | ____ |
| Business criticality | 1 (Low) / 2 (Medium) / 3 (High) | ____ |
| External dependencies | 1 (Few) / 2 (Moderate) / 3 (Many) | ____ |
| **Total** | | ____ / 15 |

## Migration Phases

### Phase 1: Preparation (1-2 weeks)

**Goals**: Understand current code, set up ArchUnit, add test coverage.

```yaml
Steps:
  1. Map current architecture:
     - Identify current layers and their responsibilities
     - Document existing dependency directions
     - Identify anti-patterns (fat services, anemic models)

  2. Add ArchUnit tests:
     - Tag existing violations with @ArchIgnore
     - Prevent new violations
     - Track violation count over time

  3. Add critical tests:
     - Add integration tests for core business flows
     - Ensure current behavior is captured before refactoring

  4. Set up multi-module project:
     - Create Maven/Gradle modules: core, usecase, adapter, framework
     - Configure module dependencies following Clean Architecture rules
```

### Phase 2: Extract Enterprise Layer (1-2 weeks)

**Goals**: Identify and extract core business entities and rules.

```
Before:                                After:
OrderService.java                      order-core/
  ├── createOrder()                        ├── entity/
  ├── payOrder()                           │   ├── Order.java
  └── cancelOrder()                        │   ├── OrderItem.java
ProcessPaymentService.java                 ├── valueobject/
  └── processPayment()                     │   ├── OrderId.java
Order.java                                 │   ├── Money.java
  ├── Long id                              │   └── OrderStatus.java
  ├── String status                        ├── exception/
  └── getters/setters                      │   └── OrderDomainException.java
                                           └── event/
                                               ├── DomainEvent.java
                                               ├── OrderCreatedEvent.java
                                               └── OrderPaidEvent.java
```

```java
// Step 1: Make Order a rich domain model (was anemic)
// BEFORE
public class Order {
    private Long id;
    private String status; // String! Not type-safe
    // only getters/setters
}

// AFTER
public class Order {
    private final OrderId id;
    private OrderStatus status; // Value Object!

    public void pay() {
        if (!status.canPay()) {
            throw new OrderDomainException("Cannot pay order in status: " + status);
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}
```

### Phase 3: Extract UseCase Layer (1-2 weeks)

**Goals**: Define Input/Output ports, create Interactors.

```java
// Step 1: Define ports
// order-usecase/src/main/java/.../port/input/CreateOrderUseCase.java
public interface CreateOrderUseCase {
    CreateOrderOutput execute(CreateOrderInput input);
}

// Step 2: Move orchestration from old Service to Interactor
// BEFORE
@Service
public class OrderService {
    @Autowired private OrderRepository orderRepo;
    @Autowired private PaymentClient paymentClient;

    @Transactional
    public OrderDTO createOrder(CreateOrderRequest req) {
        // ... 50 lines of mixed orchestration + business logic
    }
}

// AFTER
public class CreateOrderInteractor implements CreateOrderUseCase {
    private final OrderRepository orderRepo;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;

    @Override
    public CreateOrderOutput execute(CreateOrderInput input) {
        // Pure orchestration — business logic is in Enterprise entities
        OrderId orderId = OrderId.generate();
        Order order = new Order(orderId, Money.ZERO);

        input.items().forEach(item ->
            order.addItem(OrderItem.create(item)));

        Order saved = orderRepo.save(order);
        eventPublisher.publishAll(order.domainEvents());
        order.clearEvents();

        return CreateOrderOutput.from(saved);
    }
}
```

### Phase 4: Extract Adapter Layer (1-2 weeks)

**Goals**: Move implementation details to adapters.

```java
// Step 1: Extract repository implementation
// BEFORE — mixed with domain
@Repository
public class OrderRepository {
    @PersistenceContext
    private EntityManager em;

    public Order findById(Long id) {
        OrderEntity entity = em.find(OrderEntity.class, id);
        // conversion logic here
    }
}

// AFTER — adapter implements output port
@Repository
public class JpaOrderRepository implements OrderRepository {
    private final SpringDataOrderJpaRepository jpaRepo;
    private final OrderPersistenceConverter converter;

    @Override
    public Order findById(OrderId id) {
        return jpaRepo.findById(id.value())
            .map(converter::toDomain)
            .orElseThrow(() -> new OrderNotFoundException(id));
    }
}

// Step 2: Extract controller
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final CreateOrderUseCase createOrderUseCase;

    @PostMapping
    public ResponseEntity<CreateOrderResponse> create(
            @RequestBody CreateOrderRequest request) {
        CreateOrderInput input = request.toInput();
        CreateOrderOutput output = createOrderUseCase.execute(input);
        return ResponseEntity.status(201)
            .body(CreateOrderResponse.from(output));
    }
}
```

### Phase 5: DI Assembly & Verification (1 week)

**Goals**: Wire everything through Framework layer, verify architecture.

```java
@Configuration
public class UseCaseConfig {
    @Bean
    public CreateOrderUseCase createOrderUseCase(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher) {
        return new CreateOrderInteractor(
            orderRepository, paymentGateway, eventPublisher);
    }
}
```

## Migration Patterns

### Strangler Fig Pattern

```
Gradual replacement per UseCase:

Phase 2:                     Phase 3-4:                     Phase 5:
┌──────────────────┐        ┌──────────────────┐           ┌──────────────────┐
│ Old OrderService │        │ Old OrderService │           │ Old OrderService │
│ (still handles   │        │ (handles 50%     │           │ (removed!)       │
│  all use cases)  │        │  of use cases)   │           │                  │
└──────────────────┘        └──────────────────┘           └──────────────────┘
       │                            │                              │
       │ CreateOrder → new          │ CreateOrder → new            │ ALL → new
       │ PayOrder → old             │ PayOrder → new               │
                                    │ CancelOrder → old            │
```

### Branch by Abstraction

```java
// 1. Create abstraction interface
public interface OrderServiceFacade {
    OrderDTO createOrder(CreateOrderRequest req);
}

// 2. Implement both old and new
public class LegacyOrderService implements OrderServiceFacade { /* old impl */ }
public class CleanOrderService implements OrderServiceFacade { /* new impl */ }

// 3. Toggle with feature flag
@Component
public class OrderServiceRouter implements OrderServiceFacade {
    private final LegacyOrderService legacy;
    private final CleanOrderService clean;

    public OrderDTO createOrder(CreateOrderRequest req) {
        if (FeatureFlags.USE_CLEAN_ARCH_FOR_ORDERS) {
            return clean.createOrder(req);
        }
        return legacy.createOrder(req);
    }
}

// 4. Remove feature flag and legacy code when confident
```

## Common Migration Scenarios

### Scenario 1: Fat Service → Multiple Interactors

```
ORDER SERVICE (500+ lines, all logic in one class)
├── createOrder() → CreateOrderInteractor
├── payOrder() → PayOrderInteractor
├── cancelOrder() → CancelOrderInteractor
├── getOrder() → GetOrderInteractor
└── searchOrders() → SearchOrdersInteractor
```

### Scenario 2: Anemic Entity → Rich Domain Model

```java
// BEFORE — anemic model
public class Order {
    private Long id;
    private String status;       // string comparison everywhere!
    private BigDecimal amount;   // no currency!

    public void setStatus(String status) { this.status = status; }
}

// AFTER — rich domain model
public class Order {
    private final OrderId id;
    private OrderStatus status;  // value object!
    private Money amount;        // value object with currency!

    public void pay() {
        if (!status.canTransitionTo(OrderStatus.PAID)) {
            throw new OrderDomainException("...");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}
```

### Scenario 3: Direct DB Access → Repository Pattern

```java
// BEFORE — Service directly accesses DB
@Service
public class OrderService {
    @Autowired
    private JdbcTemplate jdbc;

    public OrderDTO getOrder(Long id) {
        return jdbc.queryForObject(
            "SELECT * FROM orders WHERE id = ?",
            orderRowMapper, id);
    }
}

// AFTER — Repository as port interface
public class GetOrderInteractor implements GetOrderUseCase {
    private final OrderRepository orderRepo; // interface!

    @Override
    public GetOrderOutput execute(GetOrderInput input) {
        return orderRepo.findById(input.orderId())
            .map(order -> new GetOrderOutput(...))
            .orElseThrow(() -> new OrderNotFoundException(input.orderId()));
    }
}
```

## Validation Checklist

```
Before deployment:
  □ ArchUnit tests pass for all layers
  □ No Enterprise layer imports Spring/JPA/Jackson
  □ No UseCase layer imports Adapter/Spring Web
  □ Each UseCase has its own Input Port interface
  □ Core business rules tested independently
  □ Test coverage >= 80% for Enterprise, >= 70% for UseCase
  □ All old Service classes marked @Deprecated
  □ Feature flag ready for rollback
  □ Performance benchmark — no regression

After migration:
  □ Old code removed
  □ ArchUnit in CI pipeline
  □ Team trained on Clean Architecture
  □ Documentation updated
  □ Migration documented in ADR
```

## Rollback Plan

If issues arise during migration:

1. **Toggle feature flag** → switch back to old implementation
2. **Fix issues** while production runs on old code
3. **Retry migration** with fixes applied
4. **Run both in parallel** for critical use cases during transition phase

## Time Estimates

| Phase | Small (< 50K LOC) | Medium (50-200K) | Large (> 200K) |
|-------|:---:|:---:|:---:|
| Preparation | 1 week | 2 weeks | 3 weeks |
| Extract Enterprise | 1 week | 2 weeks | 4 weeks |
| Extract UseCase | 1 week | 2 weeks | 4 weeks |
| Extract Adapter | 1 week | 2 weeks | 3 weeks |
| DI + Verification | 0.5 week | 1 week | 2 weeks |
| **Total** | **4.5 weeks** | **9 weeks** | **16 weeks** |
