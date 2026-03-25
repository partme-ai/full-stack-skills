---
name: ddd-cola
description: "Provides comprehensive guidance for COLA architecture including adapter layer, application layer, domain layer, and infrastructure layer. Use when the user asks about COLA, needs to implement COLA architecture, structure applications with COLA, or work with COLA patterns."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Structure a project using COLA architecture (Adapter, Application, Domain, Infrastructure)
- Apply COLA's layered architecture with clear responsibilities per layer
- Implement domain-driven design with COLA while keeping the domain layer pure and dependency-inverted
- Organize Java/Spring Boot projects following COLA V5 conventions

## How to use this skill

### Workflow

1. **Understand the layer responsibilities**: Adapter handles I/O; Application orchestrates use cases; Domain holds business logic; Infrastructure implements persistence and external services
2. **Set up the package structure** following COLA conventions
3. **Enforce dependency direction**: Domain depends on nothing; Application depends on Domain; Adapter and Infrastructure depend on Application and Domain
4. **Define ports in Domain or Application**, implement them in Infrastructure

### Layer Structure

```
com.example.app/
├── adapter/
│   ├── controller/        # HTTP/RPC/message inbound handlers
│   └── scheduler/         # Scheduled tasks
├── app/
│   ├── executor/          # Use case executors (command handlers)
│   └── service/           # Application services (orchestration, transactions)
├── domain/
│   ├── model/             # Entities, Value Objects, Aggregates
│   │   ├── entity/
│   │   └── valueobject/
│   ├── service/           # Domain services
│   └── gateway/           # Repository and external service interfaces (ports)
└── infrastructure/
    ├── persistence/       # Repository implementations (JPA, MyBatis)
    ├── external/          # External API clients
    └── config/            # Spring configuration and bean wiring
```

### Dependency Direction

```
Adapter → Application → Domain ← Infrastructure
```

### Example: Use Case Executor

```java
// Domain gateway (port)
public interface OrderGateway {
    void save(Order order);
    Optional<Order> findById(String id);
}

// Application executor
@Component
public class CreateOrderExecutor {
    private final OrderGateway orderGateway;

    public CreateOrderExecutor(OrderGateway orderGateway) {
        this.orderGateway = orderGateway;
    }

    @Transactional
    public OrderDto execute(CreateOrderCmd cmd) {
        Order order = Order.create(cmd.getItems(), cmd.getCustomerId());
        orderGateway.save(order);
        return OrderDto.from(order);
    }
}

// Infrastructure implementation
@Repository
public class OrderGatewayImpl implements OrderGateway {
    private final OrderMapper orderMapper;

    @Override
    public void save(Order order) {
        orderMapper.insert(OrderDO.fromDomain(order));
    }
}
```

## Best Practices

- Domain logic belongs exclusively in the Domain layer; Application layer only orchestrates and manages transaction boundaries
- Define ports (interfaces) in Domain or Application; Infrastructure implements them
- Avoid business logic in the Adapter layer; DTOs and domain objects are converted at the boundary
- Follow COLA naming conventions: `Cmd` for commands, `Executor` for handlers, `Gateway` for ports

## Resources

- COLA GitHub: https://github.com/alibaba/COLA
- COLA architecture guide: https://blog.csdn.net/significantfrank/article/details/110934799

## Keywords

cola, cola architecture, clean object-oriented layered architecture, COLA V5, adapter layer, application layer, domain layer, infrastructure layer, DDD, dependency inversion
