---
name: ddd-hexagonal-architecture
description: "Provides comprehensive guidance for hexagonal architecture including ports and adapters, domain isolation, and dependency inversion. Use when the user asks about hexagonal architecture, needs to implement ports and adapters pattern, or structure applications with hexagonal architecture."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Design applications using the hexagonal (ports and adapters) architecture
- Isolate the domain layer from external systems (databases, APIs, messaging)
- Implement dependency inversion so the domain defines interfaces and adapters implement them
- Draw or implement hexagonal architecture diagrams and layering
- Test the domain in isolation using in-memory or mock adapters

## How to use this skill

### Workflow

1. **Define the domain model** with entities, value objects, and domain services
2. **Define ports** (interfaces) in the domain layer for all external interactions
3. **Implement adapters** that fulfill those port contracts (inbound: HTTP, messaging; outbound: DB, APIs)
4. **Wire dependencies** so all arrows point inward toward the domain

### 1. Port Definition (Domain Layer)

```java
// Domain port — no framework dependencies
public interface UserRepository {
    Optional<User> findById(UserId id);
    void save(User user);
}

public interface EventPublisher {
    void publish(DomainEvent event);
}
```

### 2. Inbound Adapter (HTTP Controller)

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final CreateUserUseCase createUserUseCase;

    public UserController(CreateUserUseCase createUserUseCase) {
        this.createUserUseCase = createUserUseCase;
    }

    @PostMapping
    public ResponseEntity<UserDto> create(@RequestBody CreateUserRequest request) {
        User user = createUserUseCase.execute(request.toCommand());
        return ResponseEntity.ok(UserDto.from(user));
    }
}
```

### 3. Outbound Adapter (Database)

```java
@Repository
public class JpaUserRepository implements UserRepository {
    private final SpringDataUserRepository springRepo;

    @Override
    public Optional<User> findById(UserId id) {
        return springRepo.findById(id.value()).map(UserEntity::toDomain);
    }

    @Override
    public void save(User user) {
        springRepo.save(UserEntity.fromDomain(user));
    }
}
```

### 4. Package Structure

```
com.example.app/
├── domain/
│   ├── model/         # Entities, Value Objects
│   ├── port/          # Repository and service interfaces
│   └── service/       # Domain services
├── application/
│   └── usecase/       # Use cases orchestrating domain logic
├── adapter/
│   ├── inbound/       # HTTP controllers, message consumers
│   └── outbound/      # Database, HTTP clients, message publishers
└── config/            # Dependency injection wiring
```

## Best Practices

- The domain layer must have zero framework dependencies; it should be testable with in-memory or mock adapters
- One port can have multiple adapters (e.g., different storage backends, different transports)
- Combine with COLA or Clean Architecture: the hexagon is essentially "one domain layer + many adapters"
- Keep DTOs at the adapter boundary; the domain never exposes persistence or transport models

## Resources

- Original article by Alistair Cockburn: https://alistair.cockburn.us/hexagonal-architecture/
- DDD and hexagonal architecture: https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/

## Keywords

hexagonal architecture, ports and adapters, domain isolation, dependency inversion, inbound adapter, outbound adapter, clean boundaries, DDD
