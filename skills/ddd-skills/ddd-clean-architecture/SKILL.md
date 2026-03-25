---
name: ddd-clean-architecture
description: "Provides comprehensive guidance for clean architecture including layer separation, dependency rules, and architectural patterns. Use when the user asks about clean architecture, needs to implement clean architecture principles, or structure applications with clean architecture."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Structure an application following Clean Architecture layers (Entities, Use Cases, Interface Adapters, Frameworks)
- Enforce the dependency rule: inner layers never depend on outer layers
- Organize project packages and define clear test boundaries
- Combine Clean Architecture with Domain-Driven Design patterns

## How to use this skill

### Workflow

1. **Define Entities** (innermost layer) containing enterprise-wide business rules
2. **Define Use Cases** (application layer) containing application-specific business logic
3. **Create Interface Adapters** (presenters, gateways) that convert data between layers
4. **Implement Frameworks** (outermost layer) for web, database, and UI concerns

### Layer Structure

```
com.example.app/
├── entity/              # Entities — business rules, no dependencies
├── usecase/             # Use Cases — application logic, depends only on entity
│   ├── port/            # Input/output port interfaces
│   └── interactor/      # Use case implementations
├── adapter/             # Interface Adapters — presenters, gateways
│   ├── controller/      # Web controllers
│   ├── presenter/       # Response formatting
│   └── gateway/         # Gateway implementations
└── framework/           # Frameworks — DB, web server, external APIs
    ├── web/
    └── persistence/
```

### Use Case Example

```java
// Use case port (input boundary)
public interface CreateOrderUseCase {
    OrderOutput execute(CreateOrderInput input);
}

// Use case interactor
public class CreateOrderInteractor implements CreateOrderUseCase {
    private final OrderGateway orderGateway;
    private final PaymentGateway paymentGateway;

    public CreateOrderInteractor(OrderGateway orderGateway, PaymentGateway paymentGateway) {
        this.orderGateway = orderGateway;
        this.paymentGateway = paymentGateway;
    }

    @Override
    public OrderOutput execute(CreateOrderInput input) {
        Order order = Order.create(input.getItems());
        paymentGateway.charge(order.totalAmount());
        orderGateway.save(order);
        return OrderOutput.from(order);
    }
}
```

### Gateway Interface (defined in Use Case layer)

```java
public interface OrderGateway {
    void save(Order order);
    Optional<Order> findById(String id);
}
```

## Best Practices

- Concentrate business rules in Entities and Use Cases; avoid placing business logic in controllers or database layers
- Use interfaces to isolate I/O; this makes the core easy to replace and test
- Entities and Use Cases map naturally to DDD aggregates and domain services
- Test core layers with unit tests; test outer layers with integration or E2E tests

## Resources

- Clean Architecture by Robert C. Martin
- https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

## Keywords

clean architecture, dependency rule, use case, entity, interface adapter, gateway, layer separation, DDD, testability
