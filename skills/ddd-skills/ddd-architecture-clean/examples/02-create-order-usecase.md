# Example: CreateOrder UseCase Implementation

## Files in this UseCase

```
order-usecase/
├── port/
│   ├── input/
│   │   └── CreateOrderUseCase.java       ← Input Port (interface)
│   └── output/
│       ├── OrderRepository.java          ← Output Port (interface)
│       ├── EventPublisher.java           ← Output Port (interface)
│       └── InventoryGateway.java         ← Output Port (interface)
├── interactor/
│   └── CreateOrderInteractor.java        ← UseCase Implementation
└── dto/
    ├── CreateOrderInput.java             ← Input DTO
    └── CreateOrderOutput.java            ← Output DTO
```

## Input Port

```java
package com.example.usecase.port.input;

import com.example.usecase.dto.input.CreateOrderInput;
import com.example.usecase.dto.output.CreateOrderOutput;

/**
 * ★ Input Port — UseCase interface.
 * One UseCase = One Port (Interface Segregation Principle).
 */
public interface CreateOrderUseCase {
    CreateOrderOutput execute(CreateOrderInput input);
}
```

## Input DTO

```java
package com.example.usecase.dto.input;

import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import java.math.BigDecimal;
import java.util.Currency;
import java.util.List;

/**
 * UseCase-specific input data.
 * No HTTP/DTO framework types — pure data carrier.
 */
public record CreateOrderInput(
    @NotBlank String customerId,
    @NotEmpty List<@Valid OrderItemInput> items
) {
    /**
     * Nested record for each order item.
     */
    public record OrderItemInput(
        @NotBlank String productId,
        @Min(1) int quantity,
        @NotNull BigDecimal unitPrice,
        @NotBlank String currency
    ) {}
}
```

## Output DTO

```java
package com.example.usecase.dto.output;

import com.example.core.entity.Order;
import com.example.core.event.OrderCreatedEvent;
import com.example.core.valueobject.Money;
import com.example.core.valueobject.OrderId;
import com.example.core.valueobject.OrderStatus;

/**
 * UseCase-specific output data.
 * Created from the entity after the UseCase executes.
 */
public record CreateOrderOutput(
    OrderId orderId,
    Money totalAmount,
    OrderStatus status,
    int itemCount
) {
    public static CreateOrderOutput from(Order order) {
        return new CreateOrderOutput(
            order.id(),
            order.totalAmount(),
            order.status(),
            order.items().size()
        );
    }
}
```

## Output Ports

```java
package com.example.usecase.port.output;

import com.example.core.entity.Order;
import com.example.core.valueobject.OrderId;
import java.util.Optional;

/**
 * ★ Output Port — what the UseCase needs from outside.
 * Implemented by the Adapter layer.
 */
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
    void delete(OrderId id);
}

public interface EventPublisher {
    void publish(DomainEvent event);
    void publishAll(List<DomainEvent> events);
}

public interface InventoryGateway {
    boolean reserveStock(ProductId productId, int quantity);
    void releaseStock(ProductId productId, int quantity);
}
```

## Interactor (UseCase Implementation)

```java
package com.example.usecase.interactor;

import com.example.core.entity.Order;
import com.example.core.entity.OrderItem;
import com.example.core.valueobject.*;
import com.example.core.exception.OrderDomainException;
import com.example.usecase.dto.input.CreateOrderInput;
import com.example.usecase.dto.output.CreateOrderOutput;
import com.example.usecase.port.input.CreateOrderUseCase;
import com.example.usecase.port.output.OrderRepository;
import com.example.usecase.port.output.EventPublisher;
import com.example.usecase.port.output.InventoryGateway;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Currency;
import java.util.List;

/**
 * ★ Interactor — implements CreateOrder UseCase.
 * Orchestrates the flow: validate → create → persist → publish events.
 * Does NOT contain business logic (that's in the Entity).
 */
public class CreateOrderInteractor implements CreateOrderUseCase {

    private static final Logger log = LoggerFactory.getLogger(CreateOrderInteractor.class);

    private final OrderRepository orderRepository;
    private final EventPublisher eventPublisher;
    private final InventoryGateway inventoryGateway;

    public CreateOrderInteractor(
            OrderRepository orderRepository,
            EventPublisher eventPublisher,
            InventoryGateway inventoryGateway) {
        this.orderRepository = orderRepository;
        this.eventPublisher = eventPublisher;
        this.inventoryGateway = inventoryGateway;
    }

    @Override
    public CreateOrderOutput execute(CreateOrderInput input) {
        // 1. Validate input (basic validation via records, detailed validation here)
        validateInput(input);

        // 2. Create the Order entity (Enterprise Business Rules)
        OrderId orderId = OrderId.generate();
        CustomerId customerId = CustomerId.of(input.customerId());
        Order order = Order.create(orderId, customerId);

        // 3. Add items (delegates to Entity behavior)
        for (CreateOrderInput.OrderItemInput itemInput : input.items()) {
            OrderItem item = OrderItem.create(
                ProductId.of(itemInput.productId()),
                itemInput.quantity(),
                Money.of(itemInput.unitPrice(), Currency.getInstance(itemInput.currency()))
            );
            order.addItem(item);
        }

        // 4. Reserve inventory (through Output Port)
        for (CreateOrderInput.OrderItemInput itemInput : input.items()) {
            boolean reserved = inventoryGateway.reserveStock(
                ProductId.of(itemInput.productId()),
                itemInput.quantity()
            );
            if (!reserved) {
                // Rollback previous reservations
                rollbackReservations(input);
                throw new OrderDomainException(
                    "Insufficient stock for product: " + itemInput.productId());
            }
        }

        // 5. Submit the order (entity handles state transition)
        order.submit();

        // 6. Persist (through Output Port)
        Order savedOrder = orderRepository.save(order);

        // 7. Publish domain events (through Output Port)
        eventPublisher.publishAll(order.domainEvents());
        order.clearEvents();

        // 8. Return result
        log.info("Order created: {} for customer {}",
            savedOrder.id().value(), input.customerId());

        return CreateOrderOutput.from(savedOrder);
    }

    private void validateInput(CreateOrderInput input) {
        if (input.customerId() == null || input.customerId().isBlank()) {
            throw new IllegalArgumentException("Customer ID is required");
        }
        if (input.items() == null || input.items().isEmpty()) {
            throw new IllegalArgumentException("At least one item is required");
        }
        for (CreateOrderInput.OrderItemInput item : input.items()) {
            if (item.unitPrice().compareTo(java.math.BigDecimal.ZERO) <= 0) {
                throw new IllegalArgumentException(
                    "Unit price must be positive for product: " + item.productId());
            }
        }
    }

    private void rollbackReservations(CreateOrderInput input) {
        for (CreateOrderInput.OrderItemInput itemInput : input.items()) {
            try {
                inventoryGateway.releaseStock(
                    ProductId.of(itemInput.productId()),
                    itemInput.quantity()
                );
            } catch (Exception e) {
                log.warn("Failed to rollback inventory for product: {}", itemInput.productId(), e);
            }
        }
    }
}
```

## Unit Test

```java
package com.example.usecase.interactor;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.*;

class CreateOrderInteractorTest {

    private InMemoryOrderRepository orderRepo;
    private SpyEventPublisher eventPublisher;
    private SpyInventoryGateway inventoryGateway;
    private CreateOrderInteractor interactor;

    @BeforeEach
    void setUp() {
        orderRepo = new InMemoryOrderRepository();
        eventPublisher = new SpyEventPublisher();
        inventoryGateway = new SpyInventoryGateway();
        interactor = new CreateOrderInteractor(
            orderRepo, eventPublisher, inventoryGateway);
    }

    @Test
    void shouldCreateOrder() {
        var input = new CreateOrderInput(
            "CUST-001",
            List.of(new OrderItemInput("PROD-001", 2, new BigDecimal("10.00"), "USD"))
        );

        var output = interactor.execute(input);

        assertThat(output.orderId()).isNotNull();
        assertThat(output.status()).isEqualTo(OrderStatus.SUBMITTED);
        assertThat(output.itemCount()).isEqualTo(1);
        assertThat(output.totalAmount()).isEqualTo(Money.of(20, "USD"));
    }

    @Test
    void shouldReserveInventory() {
        var input = validInput();
        interactor.execute(input);

        assertThat(inventoryGateway.reservations())
            .containsEntry("PROD-001", 2);
    }

    @Test
    void shouldPublishEvents() {
        var input = validInput();
        interactor.execute(input);

        assertThat(eventPublisher.publishedEvents())
            .hasSize(2) // OrderCreated + OrderSubmitted
            .anyMatch(e -> e instanceof OrderCreatedEvent)
            .anyMatch(e -> e instanceof OrderSubmittedEvent);
    }

    @Test
    void shouldPersistOrder() {
        var input = validInput();
        var output = interactor.execute(input);

        var saved = orderRepo.findById(output.orderId());
        assertThat(saved).isPresent();
        assertThat(saved.get().status()).isEqualTo(OrderStatus.SUBMITTED);
    }

    @Test
    void shouldFailForEmptyItems() {
        var input = new CreateOrderInput("CUST-001", List.of());
        assertThatThrownBy(() -> interactor.execute(input))
            .isInstanceOf(IllegalArgumentException.class);
    }

    @Test
    void shouldFailWhenStockInsufficient() {
        inventoryGateway.shouldFailFor("PROD-001");

        var input = validInput();
        assertThatThrownBy(() -> interactor.execute(input))
            .isInstanceOf(OrderDomainException.class)
            .hasMessageContaining("Insufficient stock");
    }

    @Test
    void shouldRollbackReservationsOnFailure() {
        inventoryGateway.shouldFailFor("PROD-002");

        var input = new CreateOrderInput("CUST-001", List.of(
            new OrderItemInput("PROD-001", 1, BigDecimal.TEN, "USD"),
            new OrderItemInput("PROD-002", 1, BigDecimal.TEN, "USD") // this fails
        ));

        assertThatThrownBy(() -> interactor.execute(input))
            .isInstanceOf(OrderDomainException.class);

        // PROD-001 reservation should be rolled back
        assertThat(inventoryGateway.releasedStock())
            .containsEntry("PROD-001", 1);
    }

    private CreateOrderInput validInput() {
        return new CreateOrderInput(
            "CUST-001",
            List.of(new OrderItemInput("PROD-001", 2, new BigDecimal("10.00"), "USD"))
        );
    }
}
```

## In-Memory Test Doubles

```java
// InMemoryOrderRepository.java
public class InMemoryOrderRepository implements OrderRepository {
    private final Map<OrderId, Order> store = new HashMap<>();

    @Override
    public Order save(Order order) {
        store.put(order.id(), order);
        return order;
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public void delete(OrderId id) {
        store.remove(id);
    }

    public void clear() { store.clear(); }
}

// SpyEventPublisher.java
public class SpyEventPublisher implements EventPublisher {
    private final List<DomainEvent> events = new ArrayList<>();

    @Override
    public void publish(DomainEvent event) {
        events.add(event);
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        this.events.addAll(events);
    }

    public List<DomainEvent> publishedEvents() { return List.copyOf(events); }
    public void clear() { events.clear(); }
}

// SpyInventoryGateway.java
public class SpyInventoryGateway implements InventoryGateway {
    private final Map<String, Integer> reservations = new HashMap<>();
    private final Map<String, Integer> released = new HashMap<>();
    private final Set<String> failFor = new HashSet<>();

    @Override
    public boolean reserveStock(ProductId productId, int quantity) {
        if (failFor.contains(productId.value())) {
            return false;
        }
        reservations.merge(productId.value(), quantity, Integer::sum);
        return true;
    }

    @Override
    public void releaseStock(ProductId productId, int quantity) {
        released.merge(productId.value(), quantity, Integer::sum);
    }

    public void shouldFailFor(String productId) {
        failFor.add(productId);
    }

    public Map<String, Integer> reservations() { return Map.copyOf(reservations); }
    public Map<String, Integer> releasedStock() { return Map.copyOf(released); }
}
```

## Key Points

| Concept | How It's Applied Here |
|---------|----------------------|
| **Dependency Rule** | Interactor depends on Enterprise (Order) and Output Ports (interfaces), not on implementations |
| **Single Responsibility** | Interactor only orchestrates; entity contains business rules |
| **Interface Segregation** | Each UseCase gets its own Input Port interface |
| **Dependency Inversion** | Output Ports defined in UseCase layer, implemented in Adapter layer |
| **Event Sourcing** | Domain events collected in entity, published after persistence |
