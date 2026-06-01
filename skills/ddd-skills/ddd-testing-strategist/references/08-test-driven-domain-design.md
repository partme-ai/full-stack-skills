# Test-Driven Domain Design (TDDD)

## What is TDDD?

TDDD = Test-Driven Development applied to DDD domain modeling. The key difference from classical TDD:

| Aspect | Classical TDD | TDDD |
|--------|-------------|------|
| Test unit | Method / Function | Domain behavior (state transition) |
| Focus | Implementation correctness | Business invariant preservation |
| Refactor target | Code structure | Domain model (extract VO, identify aggregate) |
| Mock scope | System dependencies | Domain ports (Repository, Gateway) |
| Test language | Technical (assertEquals) | Business (assertOrderCanBePaid) |
| Test naming | `testAdd()` | `pay_should_change_status_to_paid_when_draft` |

## TDDD Workflow

```
┌─────────────────────────────────────────────────────────┐
│ Step 1: RED — Write a failing business behavior test     │
│  - Test a domain invariant or state transition           │
│  - No Mock, no Spring, pure domain logic                 │
│  - Example: "a paid order cannot be paid again"          │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Step 2: GREEN — Write minimal domain code to pass       │
│  - Only implement the current test's behavior           │
│  - Do NOT add extra "nice to have" logic                │
│  - Do NOT think about persistence or framework          │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Step 3: REFACTOR — Improve domain model                 │
│  - Extract Value Objects (e.g., Money, OrderStatus)     │
│  - Identify aggregate boundaries                        │
│  - Add Repository interfaces (still no implementation)  │
│  - Rename to ubiquitous language terms                  │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Step 4: REPEAT — Cover all state transitions            │
│  - Each state transition = one test class               │
│  - Happy path + all boundary conditions                 │
│  - Domain events verified for each transition           │
└─────────────────────────────────────────────────────────┘
```

## TDDD Complete Example: Order Payment

### Step 1: RED — Write the test

```java
class OrderPayTest {
    @Test
    void pay_should_change_status_to_paid_when_draft() {
        Order order = Order.create(CustomerId.from("cust-1"));
        order.pay();
        assertEquals(OrderStatus.PAID, order.getStatus());
    }

    @Test
    void pay_should_emit_orderPaid_event() {
        Order order = Order.create(CustomerId.from("cust-1"));
        order.pay();
        assertThat(order.getDomainEvents())
            .anyMatch(e -> e instanceof OrderPaidEvent);
    }

    @Test
    void pay_should_fail_when_already_paid() {
        Order order = Order.create(CustomerId.from("cust-1"));
        order.pay();
        assertThrows(OrderException.class, order::pay);
    }

    @Test
    void pay_should_fail_when_cancelled() {
        Order order = Order.create(CustomerId.from("cust-1"));
        order.cancel("test");
        assertThrows(OrderException.class, order::pay);
    }
}
```

### Step 2: GREEN — Minimal domain code

```java
public class Order {
    private OrderStatus status = OrderStatus.DRAFT;
    private final List<DomainEvent> events = new ArrayList<>();
    private final OrderId id;
    private final CustomerId customerId;

    private Order(CustomerId customerId) {
        this.id = OrderId.generate();
        this.customerId = customerId;
        events.add(new OrderCreatedEvent(this.id, this.customerId));
    }

    public static Order create(CustomerId customerId) {
        return new Order(customerId);
    }

    public void pay() {
        if (status == OrderStatus.PAID) {
            throw new OrderException("Order already paid");
        }
        if (status == OrderStatus.CANCELLED) {
            throw new OrderException("Cancelled order cannot be paid");
        }
        this.status = OrderStatus.PAID;
        events.add(new OrderPaidEvent(this.id));
    }

    public void cancel(String reason) {
        if (status == OrderStatus.SHIPPED) {
            throw new OrderException("Cannot cancel shipped order");
        }
        this.status = OrderStatus.CANCELLED;
        events.add(new OrderCancelledEvent(this.id, reason));
    }
    // getters...
}
```

### Step 3: REFACTOR — Extract concepts

```java
// Extract status machine
public enum OrderStatus {
    DRAFT(true, true, false, false),
    PAID(false, false, true, false),
    SHIPPED(false, false, false, false),
    CANCELLED(false, true, false, false);

    private final boolean canPay;
    private final boolean canCancel;
    private final boolean canShip;
    private final boolean canRefund;

    OrderStatus(boolean canPay, boolean canCancel, boolean canShip, boolean canRefund) {
        this.canPay = canPay;
        this.canCancel = canCancel;
        this.canShip = canShip;
        this.canRefund = canRefund;
    }
    // accessors...
}

// Simplify pay() method
public void pay() {
    if (!status.canPay()) {
        throw new OrderException("Order cannot be paid in status: " + status);
    }
    this.status = OrderStatus.PAID;
    events.add(new OrderPaidEvent(this.id));
}

// Add Repository interface
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
}
```

### Step 4: REPEAT — Cover cancel, ship, refund transitions

```java
class OrderCancelTest {
    @Test void cancel_changes_status_when_draft() { ... }
    @Test void cancel_emits_orderCancelled_event() { ... }
    @Test void cancel_fails_when_shipped() { ... }
}

class OrderShipTest {
    @Test void ship_changes_status_when_paid() { ... }
    @Test void ship_emits_orderShipped_event() { ... }
    @Test void ship_fails_when_draft() { ... }
}

class OrderRefundTest {
    @Test void refund_changes_status_when_paid() { ... }
    @Test void refund_emits_orderRefunded_event() { ... }
    @Test void refund_fails_when_draft() { ... }
}
```

## When to Use TDDD

| Use TDDD | Don't Use TDDD |
|----------|---------------|
| Building a new aggregate root | Implementing simple CRUD |
| Complex business rules with state machines | Writing Repository implementations |
| Domain logic with multiple invariants | Configuring framework dependencies |
| Event Sourcing aggregate design | UI / API layer development |
| When you're unsure about model boundaries | When domain model is already stable |
