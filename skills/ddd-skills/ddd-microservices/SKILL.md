---
name: ddd-microservices
description: "Provides comprehensive guidance for DDD in microservices including bounded contexts, service boundaries, event-driven architecture, and microservice patterns. Use when the user asks about DDD microservices, needs to design microservices with DDD, or implement microservice architectures."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use DDD to define microservice boundaries (bounded contexts, aggregates, domain events)
- Design inter-service contracts and event-driven communication
- Implement cross-service consistency, querying, and operational strategies
- Decide between synchronous (REST/gRPC) and asynchronous (events/messaging) communication

## How to use this skill

### Workflow

1. **Map bounded contexts** to identify natural service boundaries
2. **Define aggregates** within each service for data consistency
3. **Design communication**: synchronous for queries and strong consistency; asynchronous (domain events) for decoupling
4. **Ensure data ownership**: each service owns its database; share data via APIs or events

### 1. Bounded Context to Service Mapping

```
E-Commerce Domain:
├── Order Service        ← Order bounded context
│   ├── Order aggregate
│   └── OrderPlaced event
├── Inventory Service    ← Inventory bounded context
│   ├── Product aggregate
│   └── StockReserved event
├── Payment Service      ← Payment bounded context
│   ├── Payment aggregate
│   └── PaymentCompleted event
└── Notification Service ← Cross-cutting
    └── Subscribes to all domain events
```

### 2. Synchronous Communication (Feign/gRPC)

```java
@FeignClient(name = "inventory-service")
public interface InventoryClient {
    @GetMapping("/api/products/{id}/stock")
    StockInfo getStock(@PathVariable String id);
}
```

### 3. Asynchronous Communication (Domain Events)

```java
// Order Service publishes
@Transactional
public void placeOrder(PlaceOrderCommand cmd) {
    Order order = Order.create(cmd);
    orderRepository.save(order);
    eventPublisher.publish(new OrderPlacedEvent(order.getId(), order.getItems()));
}

// Inventory Service subscribes
@EventListener
public void onOrderPlaced(OrderPlacedEvent event) {
    inventoryService.reserveStock(event.getItems());
}
```

### 4. Database per Service

```
Order Service      → order_db (PostgreSQL)
Inventory Service  → inventory_db (PostgreSQL)
Payment Service    → payment_db (PostgreSQL)
```

## Best Practices

- Define bounded contexts clearly before splitting into services; avoid premature decomposition
- Use domain events to express cross-aggregate and cross-service facts; ensure idempotency and ordering
- Define clear SLAs, data ownership, and failure boundaries for each service
- Prefer eventual consistency with compensating transactions (Saga pattern) over distributed transactions

## Resources

- Building Microservices by Sam Newman
- Domain-Driven Design by Eric Evans
- https://microservices.io/

## Keywords

ddd microservices, bounded context, aggregate, domain events, service boundary, Saga pattern, CQRS, database per service, eventual consistency, API gateway
