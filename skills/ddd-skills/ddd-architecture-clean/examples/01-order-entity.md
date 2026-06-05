# Example: Order Entity (Enterprise Business Rules Layer)

## File: `order-core/src/main/java/com/example/core/entity/Order.java`

A complete rich domain model for an Order entity following Clean Architecture principles.

```java
package com.example.core.entity;

import com.example.core.valueobject.*;
import com.example.core.exception.OrderDomainException;
import com.example.core.event.*;

import java.time.Instant;
import java.util.*;

/**
 * ★ Order — Core Enterprise Business Rule Entity.
 * Zero framework dependencies. Pure business logic.
 */
public class Order {

    private final OrderId id;
    private final CustomerId customerId;
    private final List<OrderItem> items;
    private Money totalAmount;
    private OrderStatus status;
    private final List<DomainEvent> domainEvents;
    private final Instant createdAt;
    private Instant updatedAt;

    // ── Constructor (factory method preferred) ──

    private Order(OrderId id, CustomerId customerId) {
        this.id = Objects.requireNonNull(id, "OrderId must not be null");
        this.customerId = Objects.requireNonNull(customerId, "CustomerId must not be null");
        this.items = new ArrayList<>();
        this.totalAmount = Money.ZERO;
        this.status = OrderStatus.DRAFT;
        this.domainEvents = new ArrayList<>();
        this.createdAt = Instant.now();
        this.updatedAt = this.createdAt;
    }

    /**
     * ★ Static factory — preferred over public constructor.
     * Enforces creation rules and records the OrderCreated event.
     */
    public static Order create(OrderId id, CustomerId customerId) {
        Order order = new Order(id, customerId);
        order.addEvent(new OrderCreatedEvent(id, customerId));
        return order;
    }

    // ── Business Behavior (Rich Domain Model) ──

    /**
     * Add an item to this order.
     * Items can only be added while the order is in DRAFT status.
     */
    public void addItem(OrderItem item) {
        assertDraftStatus("add items");
        this.items.add(Objects.requireNonNull(item, "Item must not be null"));
        recalculateTotal();
        this.updatedAt = Instant.now();
    }

    /**
     * Remove an item from this order.
     * Only allowed in DRAFT status.
     */
    public void removeItem(ProductId productId) {
        assertDraftStatus("remove items");
        boolean removed = this.items.removeIf(item -> item.productId().equals(productId));
        if (!removed) {
            throw new OrderDomainException(
                "Product " + productId.value() + " not found in order " + id.value());
        }
        recalculateTotal();
        this.updatedAt = Instant.now();
    }

    /**
     * Submit the order — transitions from DRAFT to SUBMITTED.
     * Validates that the order has at least one item.
     */
    public void submit() {
        assertDraftStatus("submit");
        if (items.isEmpty()) {
            throw new OrderDomainException("Cannot submit empty order " + id.value());
        }
        this.status = OrderStatus.SUBMITTED;
        this.updatedAt = Instant.now();
        addEvent(new OrderSubmittedEvent(id, customerId, totalAmount));
    }

    /**
     * Pay for this order. Requires SUBMITTED status.
     */
    public void pay(PaymentId paymentId) {
        assertStatus(OrderStatus.SUBMITTED, "pay");
        this.status = OrderStatus.PAID;
        this.updatedAt = Instant.now();
        addEvent(new OrderPaidEvent(id, paymentId));
    }

    /**
     * Cancel the order. Allowed from DRAFT or SUBMITTED.
     */
    public void cancel(String reason) {
        if (status == OrderStatus.PAID || status == OrderStatus.CANCELLED) {
            throw new OrderDomainException(
                "Cannot cancel order " + id.value() + " in status " + status);
        }
        this.status = OrderStatus.CANCELLED;
        this.updatedAt = Instant.now();
        addEvent(new OrderCancelledEvent(id, reason));
    }

    /**
     * Ship the order (triggered by warehouse system).
     */
    public void ship(TrackingId trackingId) {
        assertStatus(OrderStatus.PAID, "ship");
        this.status = OrderStatus.SHIPPED;
        this.updatedAt = Instant.now();
        addEvent(new OrderShippedEvent(id, trackingId));
    }

    /**
     * Mark as delivered.
     */
    public void deliver() {
        assertStatus(OrderStatus.SHIPPED, "deliver");
        this.status = OrderStatus.DELIVERED;
        this.updatedAt = Instant.now();
        addEvent(new OrderDeliveredEvent(id));
    }

    // ── Internal Helpers ──

    private void recalculateTotal() {
        this.totalAmount = items.stream()
            .map(OrderItem::subtotal)
            .reduce(Money.ZERO, Money::add);
    }

    private void assertDraftStatus(String action) {
        if (this.status != OrderStatus.DRAFT) {
            throw new OrderDomainException(
                "Cannot " + action + " on order " + id.value()
                + " in status " + status + " (must be DRAFT)");
        }
    }

    private void assertStatus(OrderStatus expected, String action) {
        if (this.status != expected) {
            throw new OrderDomainException(
                "Cannot " + action + " order " + id.value()
                + " in status " + status + " (must be " + expected + ")");
        }
    }

    private void addEvent(DomainEvent event) {
        this.domainEvents.add(Objects.requireNonNull(event));
    }

    // ── Getters (no setters — behavior is in methods) ──

    public OrderId id()               { return id; }
    public CustomerId customerId()    { return customerId; }
    public List<OrderItem> items()    { return Collections.unmodifiableList(items); }
    public Money totalAmount()        { return totalAmount; }
    public OrderStatus status()       { return status; }
    public Instant createdAt()        { return createdAt; }
    public Instant updatedAt()        { return updatedAt; }

    public List<DomainEvent> domainEvents() {
        return Collections.unmodifiableList(domainEvents);
    }

    public void clearEvents() {
        domainEvents.clear();
    }

    // ── equals/hashCode based on identity ──

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Order order = (Order) o;
        return id.equals(order.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return "Order{id=" + id.value()
            + ", status=" + status
            + ", total=" + totalAmount
            + ", items=" + items.size()
            + "}";
    }
}
```

## Unit Test

```java
package com.example.core.entity;

import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.*;

class OrderTest {

    @Test
    void shouldCreateOrder() {
        Order order = Order.create(OrderId.generate(), CustomerId.of("CUST-001"));
        assertThat(order.status()).isEqualTo(OrderStatus.DRAFT);
        assertThat(order.items()).isEmpty();
        assertThat(order.totalAmount()).isEqualTo(Money.ZERO);
        assertThat(order.domainEvents()).hasSize(1);
    }

    @Test
    void shouldAddItem() {
        Order order = givenDraftOrder();
        order.addItem(new OrderItem(ProductId.of("PROD-001"), 2, Money.of(10, "USD")));

        assertThat(order.items()).hasSize(1);
        assertThat(order.totalAmount()).isEqualTo(Money.of(20, "USD"));
    }

    @Test
    void shouldSubmit() {
        Order order = givenDraftOrder();
        order.addItem(new OrderItem(ProductId.of("PROD-001"), 1, Money.of(10, "USD")));
        order.submit();

        assertThat(order.status()).isEqualTo(OrderStatus.SUBMITTED);
    }

    @Test
    void shouldNotSubmitEmptyOrder() {
        Order order = givenDraftOrder();
        assertThatThrownBy(order::submit)
            .isInstanceOf(OrderDomainException.class)
            .hasMessageContaining("Cannot submit empty order");
    }

    @Test
    void shouldPay() {
        Order order = givenSubmittedOrder();
        order.pay(PaymentId.generate());

        assertThat(order.status()).isEqualTo(OrderStatus.PAID);
    }

    @Test
    void shouldNotPayWhenNotSubmitted() {
        Order order = givenDraftOrder();
        assertThatThrownBy(() -> order.pay(PaymentId.generate()))
            .isInstanceOf(OrderDomainException.class);
    }

    @Test
    void shouldCancelDraftOrder() {
        Order order = givenDraftOrder();
        order.cancel("Changed mind");
        assertThat(order.status()).isEqualTo(OrderStatus.CANCELLED);
    }

    @Test
    void shouldNotCancelPaidOrder() {
        Order order = givenSubmittedOrder();
        order.pay(PaymentId.generate());

        assertThatThrownBy(() -> order.cancel("No reason"))
            .isInstanceOf(OrderDomainException.class);
    }

    @Test
    void shouldEmitEventsThroughLifecycle() {
        Order order = givenDraftOrder();
        order.addItem(new OrderItem(ProductId.of("PROD-001"), 1, Money.of(10, "USD")));
        order.submit();
        order.pay(PaymentId.generate());

        assertThat(order.domainEvents())
            .extracting("class")
            .containsExactly(
                OrderCreatedEvent.class,
                OrderSubmittedEvent.class,
                OrderPaidEvent.class
            );
    }

    private Order givenDraftOrder() {
        return Order.create(OrderId.generate(), CustomerId.of("CUST-001"));
    }

    private Order givenSubmittedOrder() {
        Order order = givenDraftOrder();
        order.addItem(new OrderItem(ProductId.of("PROD-001"), 1, Money.of(10, "USD")));
        order.submit();
        order.clearEvents(); // start fresh
        return order;
    }
}
```

## State Machine

```
                    ┌──────────┐
                    │  DRAFT   │
                    └────┬─────┘
                         │ submit()
                    ┌────▼─────┐
                    │SUBMITTED │
                    └────┬─────┘
                         │ pay()
                    ┌────▼─────┐
                    │  PAID    │
                    └────┬─────┘
                         │ ship()
                    ┌────▼─────┐
                    │ SHIPPED  │
                    └────┬─────┘
                         │ deliver()
                    ┌────▼──────┐
                    │ DELIVERED │
                    └───────────┘
    cancel() allowed: DRAFT, SUBMITTED
```
