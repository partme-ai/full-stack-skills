# UseCase Input/Output Ports

## Location: `{project}-usecase/port/input/` and `{project}-usecase/port/output/`

The UseCase layer defines two types of ports:

| Port Type | Location | Purpose | Direction |
|-----------|----------|---------|-----------|
| **Input Port** | `port/input/` | UseCase interfaces — what the app **offers** | Called by adapters (inward) |
| **Output Port** | `port/output/` | Repository/Gateway interfaces — what the app **needs** | Implemented by adapters (outward) |

## Input Port (UseCase Interface)

```java
package com.example.usecase.port.input;

/**
 * ★ Input Port — defines what the application offers.
 * Each UseCase gets its own Input Port interface
 * (Interface Segregation Principle).
 */
public interface CreateOrderUseCase {
    /**
     * @param input  UseCase-specific input data
     * @return       UseCase-specific output data
     */
    CreateOrderOutput execute(CreateOrderInput input);
}

public interface PayOrderUseCase {
    PayOrderOutput execute(PayOrderInput input);
}

public interface CancelOrderUseCase {
    CancelOrderOutput execute(CancelOrderInput input);
}
```

## Input DTOs (UseCase-specific)

```java
package com.example.usecase.dto.input;

import com.example.core.valueobject.OrderId;
import java.util.List;

public record CreateOrderInput(
    String customerId,
    List<OrderItemInput> items
) {
    public record OrderItemInput(
        String productId,
        int quantity,
        MoneyInput unitPrice
    ) {}
}

public record PayOrderInput(
    OrderId orderId,
    String paymentMethodId
) {}

public record CancelOrderInput(
    OrderId orderId,
    String reason
) {}
```

## Output DTOs (UseCase-specific)

```java
package com.example.usecase.dto.output;

import com.example.core.valueobject.Money;
import com.example.core.valueobject.OrderId;
import com.example.core.valueobject.OrderStatus;

public record CreateOrderOutput(
    OrderId orderId,
    Money totalAmount,
    OrderStatus status
) {}

public record PayOrderOutput(
    OrderId orderId,
    OrderStatus status,
    String transactionId
) {}
```

## Output Port (Repository/Gateway Interface)

```java
package com.example.usecase.port.output;

import com.example.core.valueobject.OrderId;
import java.util.Optional;

/**
 * ★ Output Port — defines what the application needs
 * from the outside world. Implemented by infrastructure layer.
 */
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
    void delete(OrderId id);
}

public interface PaymentGateway {
    PaymentResult charge(Money amount, PaymentMethod method);
    RefundResult refund(PaymentId paymentId, Money amount);
}

public interface EventPublisher {
    void publish(DomainEvent event);
    void publishAll(List<DomainEvent> events);
}

public interface NotificationPort {
    void sendEmail(Email to, String subject, String body);
}
```

## Port Design Rules

| Rule | Description |
|------|-------------|
| **One UseCase = One Port** | Each UseCase gets its own Input Port interface |
| **Technology-agnostic** | No framework types in port signatures |
| **Domain types only** | Parameter types must be from Enterprise or simple Java types |
| **No `@` annotations** | Ports are pure interfaces, no annotations |
| **Output Ports reflect real needs** | Define exactly what the UseCase needs, not what the DB can do |

## Clean Architecture Compatibility

```yaml
Clean Architecture:
  Enterprise Layer: core/entity    (no interfaces, just business rules)
  UseCase Layer:    usecase/port/   (Interfaces)
                    usecase/interactor/ (Implementations)

  Dependency Rule:
    Controller (Adapter) → Input Port (UseCase interface)
    Interactor (UseCase)  → Output Port (Repository interface)
    Repository Impl (Infra) → implements Output Port
```

> **Key insight**: In Clean Architecture, the `Input Port` defines the contract for what a UseCase does, while the `Output Port` defines the contract for what the UseCase needs from outside. Both are owned by the UseCase layer.
