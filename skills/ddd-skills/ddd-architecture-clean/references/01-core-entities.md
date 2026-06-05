# Enterprise Business Rules — Core Entities

## Location: `{project}-core/entity/`

The **Enterprise Business Rules** layer (innermost) contains:
- Core entities with business behavior (rich domain model)
- Value objects that encapsulate concepts
- Domain exceptions for business rule violations
- Domain events representing meaningful business occurrences

## Key Principle

> Entities must be framework-free. No Spring/JPA/Jackson annotations. Pure Java/Kotlin/C#.

## Entity Template

```java
package com.example.core.entity;

import com.example.core.valueobject.Money;
import com.example.core.valueobject.OrderId;
import com.example.core.valueobject.OrderStatus;
import com.example.core.exception.OrderDomainException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * ★ Core Entity — zero framework dependencies.
 * Enterprise Business Rules are completely isolated from
 * frameworks, databases, and delivery mechanisms.
 */
public class Order {
    private final OrderId id;
    private Money totalAmount;
    private OrderStatus status;
    private final List<OrderItem> items;
    private final List<DomainEvent> domainEvents;

    // Constructor — always initialize to valid state
    public Order(OrderId id, Money totalAmount) {
        this.id = id;
        this.totalAmount = totalAmount;
        this.status = OrderStatus.DRAFT;
        this.items = new ArrayList<>();
        this.domainEvents = new ArrayList<>();
        addDomainEvent(new OrderCreatedEvent(this.id, this.totalAmount));
    }

    // Business behavior, not just getters/setters
    public void pay() {
        if (!this.status.canTransitionTo(OrderStatus.PAID)) {
            throw new OrderDomainException(
                "Order " + id.value() + " cannot transition from "
                + status + " to " + OrderStatus.PAID);
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }

    public void cancel() {
        if (!this.status.canTransitionTo(OrderStatus.CANCELLED)) {
            throw new OrderDomainException("Order already " + status);
        }
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelledEvent(this.id));
    }

    public void addItem(OrderItem item) {
        this.items.add(item);
        this.totalAmount = this.totalAmount.add(item.subtotal());
    }

    public Money calculateTotal() {
        return items.stream()
            .map(OrderItem::subtotal)
            .reduce(Money.ZERO, Money::add);
    }

    // Getters without setters — immutability by design
    public OrderId id() { return id; }
    public Money totalAmount() { return totalAmount; }
    public OrderStatus status() { return status; }
    public List<OrderItem> items() { return Collections.unmodifiableList(items); }

    // Domain events for side effects
    public List<DomainEvent> domainEvents() {
        return Collections.unmodifiableList(domainEvents);
    }
    public void clearEvents() { domainEvents.clear(); }

    private void addDomainEvent(DomainEvent event) {
        domainEvents.add(event);
    }
}
```

## Value Object Template

```java
package com.example.core.valueobject;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Currency;
import java.util.Objects;

/**
 * ★ Value Object — immutable by definition.
 * Two Money objects with same amount+currency are equal.
 */
public final class Money {
    public static final Money ZERO = new Money(BigDecimal.ZERO, Currency.getInstance("USD"));

    private final BigDecimal amount;
    private final Currency currency;

    public Money(BigDecimal amount, Currency currency) {
        this.amount = amount.setScale(2, RoundingMode.HALF_UP);
        this.currency = Objects.requireNonNull(currency);
    }

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Currency mismatch");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public Money subtract(Money other) { /* ... */ }
    public Money multiply(int factor) { /* ... */ }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Money money = (Money) o;
        return amount.compareTo(money.amount) == 0
            && currency.equals(money.currency);
    }

    @Override
    public int hashCode() {
        return Objects.hash(amount.stripTrailingZeros(), currency);
    }

    public BigDecimal amount() { return amount; }
    public Currency currency() { return currency; }
}
```

## Domain Exception Template

```java
package com.example.core.exception;

/**
 * Base domain exception — all enterprise rule violations
 * use this or its subclasses.
 */
public class DomainException extends RuntimeException {
    public DomainException(String message) {
        super(message);
    }
}

public class OrderDomainException extends DomainException {
    public OrderDomainException(String message) {
        super(message);
    }
}

public class BusinessRuleViolation extends DomainException {
    public BusinessRuleViolation(String rule, String detail) {
        super("Business rule violated: " + rule + " — " + detail);
    }
}
```

## Domain Event Templates

```java
package com.example.core.event;

import java.time.Instant;
import java.util.UUID;

public abstract class DomainEvent {
    private final UUID eventId;
    private final Instant occurredOn;

    protected DomainEvent() {
        this.eventId = UUID.randomUUID();
        this.occurredOn = Instant.now();
    }

    public UUID eventId() { return eventId; }
    public Instant occurredOn() { return occurredOn; }
}

public class OrderCreatedEvent extends DomainEvent {
    private final OrderId orderId;
    private final Money totalAmount;
    public OrderCreatedEvent(OrderId orderId, Money totalAmount) {
        this.orderId = orderId;
        this.totalAmount = totalAmount;
    }
    public OrderId orderId() { return orderId; }
    public Money totalAmount() { return totalAmount; }
}
```

## Testing

```java
class OrderTest {
    @Test
    void shouldCreateOrder() {
        var order = new Order(new OrderId("ORD-001"), Money.ZERO);
        assertThat(order.status()).isEqualTo(OrderStatus.DRAFT);
        assertThat(order.domainEvents()).hasSize(1);
    }

    @Test
    void shouldPayOrder() {
        var order = new Order(new OrderId("ORD-001"), new Money(new BigDecimal("99.00")));
        order.pay();
        assertThat(order.status()).isEqualTo(OrderStatus.PAID);
    }

    @Test
    void shouldNotPayCancelledOrder() {
        var order = new Order(new OrderId("ORD-001"), Money.ZERO);
        order.cancel();
        assertThatThrownBy(() -> order.pay())
            .isInstanceOf(OrderDomainException.class);
    }
}
```
