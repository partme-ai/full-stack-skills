---
name: ddd-event-driven
description: "Provides comprehensive guidance for event-driven architecture including domain events, event sourcing, CQRS, and event patterns. Use when the user asks about event-driven architecture, needs to implement event-driven systems, or work with domain events."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use domain events to decouple aggregates and services
- Design event sourcing systems where state is derived from an event stream
- Implement CQRS (Command Query Responsibility Segregation)
- Choose and integrate message brokers (Kafka, RabbitMQ, etc.)
- Ensure reliable event delivery with outbox patterns

## How to use this skill

### Workflow

1. **Identify domain events** that represent "facts that have happened" within aggregates
2. **Design the event flow**: publication, transport (message bus), and consumption
3. **Choose the pattern**: simple domain events, event sourcing, or full CQRS
4. **Implement delivery guarantees**: at-least-once delivery with idempotent consumers

### 1. Domain Event Definition

```java
public record OrderPlacedEvent(
    String orderId,
    String customerId,
    BigDecimal totalAmount,
    Instant occurredAt
) implements DomainEvent {}
```

### 2. Publishing Domain Events

```java
public class Order extends AggregateRoot {
    public void place(List<OrderItem> items) {
        // Business logic...
        this.status = OrderStatus.PLACED;
        registerEvent(new OrderPlacedEvent(this.id, this.customerId, this.total, Instant.now()));
    }
}
```

### 3. Event Sourcing Pattern

```java
public class Account {
    private BigDecimal balance = BigDecimal.ZERO;
    private final List<DomainEvent> changes = new ArrayList<>();

    public void apply(MoneyDepositedEvent event) {
        this.balance = this.balance.add(event.amount());
    }

    public static Account reconstitute(List<DomainEvent> events) {
        Account account = new Account();
        events.forEach(account::apply);
        return account;
    }
}
```

### 4. CQRS Overview

```
Write Side:                          Read Side:
Command → Aggregate → Events    →    Event Handler → Read Model (View)
                              (message bus)
```

### 5. Outbox Pattern for Reliable Delivery

```java
// Save event to outbox table in the same transaction as the aggregate
@Transactional
public void placeOrder(PlaceOrderCommand cmd) {
    Order order = Order.place(cmd);
    orderRepository.save(order);
    outboxRepository.save(new OutboxEntry("OrderPlaced", serialize(order.events())));
}
// A separate poller publishes outbox entries to the message broker
```

## Best Practices

- Name events in past tense; include the aggregate ID and essential data only — avoid large payloads or sensitive information
- Guarantee at-least-once delivery with idempotent consumers; use an outbox table with polling for reliable publishing
- Define an explicit event versioning and compatibility strategy (additive fields, new topics)
- Start with simple domain events before adopting full event sourcing; the complexity trade-off must be justified

## Resources

- Domain-Driven Design by Eric Evans
- Martin Fowler on Event Sourcing: https://martinfowler.com/eaaDev/EventSourcing.html
- CQRS: https://martinfowler.com/bliki/CQRS.html

## Keywords

event-driven architecture, domain events, event sourcing, CQRS, outbox pattern, message broker, Kafka, RabbitMQ, eventual consistency, idempotent consumers
