# UseCase Interactors

## Location: `{project}-usecase/interactor/`

**Interactors** are the implementations of Input Ports. They orchestrate the flow:
1. Receive Input DTO
2. Load/validate Enterprise entities
3. Execute business behavior on entities
4. Persist through Output Ports
5. Publish domain events
6. Return Output DTO

## Key Rule

> Interactors do NOT contain business logic. Business logic lives in Entity/Enterprise layer.
> Interactors ORCHESTRATE — they call entities and ports.

## Standard Interactor Template

```java
package com.example.usecase.interactor;

import com.example.core.entity.Order;
import com.example.core.exception.OrderDomainException;
import com.example.core.valueobject.Money;
import com.example.core.valueobject.OrderId;
import com.example.usecase.dto.input.CreateOrderInput;
import com.example.usecase.dto.output.CreateOrderOutput;
import com.example.usecase.port.input.CreateOrderUseCase;
import com.example.usecase.port.output.OrderRepository;
import com.example.usecase.port.output.EventPublisher;
import com.example.usecase.port.output.NotificationPort;

import java.util.List;

/**
 * ★ Interactor — implements the Input Port.
 * Pure orchestration, no business logic.
 */
public class CreateOrderInteractor implements CreateOrderUseCase {

    private final OrderRepository orderRepository;
    private final EventPublisher eventPublisher;
    private final NotificationPort notificationPort;

    // Constructor injection via framework (set up in Framework layer)
    public CreateOrderInteractor(
            OrderRepository orderRepository,
            EventPublisher eventPublisher,
            NotificationPort notificationPort) {
        this.orderRepository = orderRepository;
        this.eventPublisher = eventPublisher;
        this.notificationPort = notificationPort;
    }

    @Override
    public CreateOrderOutput execute(CreateOrderInput input) {
        // 1. Create entity (Enterprise layer — encapsulates creation logic)
        OrderId orderId = OrderId.generate();
        Money total = calculateTotal(input.items());
        Order order = new Order(orderId, total);

        // 2. Add items
        for (CreateOrderInput.OrderItemInput itemInput : input.items()) {
            order.addItem(new OrderItem(
                ProductId.of(itemInput.productId()),
                itemInput.quantity(),
                new Money(itemInput.unitPrice().amount(), Currency.getInstance(itemInput.unitPrice().currency()))
            ));
        }

        // 3. Save through Output Port
        Order saved = orderRepository.save(order);

        // 4. Publish events (side effects)
        eventPublisher.publishAll(order.domainEvents());
        order.clearEvents();

        // 5. Send notification (side effect through port)
        notificationPort.sendEmail(
            Email.of(input.customerId()),
            "Order Created",
            "Your order " + orderId.value() + " has been created."
        );

        // 6. Return Output DTO
        return new CreateOrderOutput(
            saved.id(),
            saved.totalAmount(),
            saved.status()
        );
    }

    // Orchestration helper (NOT business logic)
    private Money calculateTotal(List<CreateOrderInput.OrderItemInput> items) {
        return items.stream()
            .map(item -> new Money(
                item.unitPrice().amount(),
                Currency.getInstance(item.unitPrice().currency()))
                .multiply(item.quantity()))
            .reduce(Money.ZERO, Money::add);
    }
}
```

## Complex Interactor with Transaction

```java
public class PayOrderInteractor implements PayOrderUseCase {

    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;

    public PayOrderInteractor(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher) {
        this.orderRepository = orderRepository;
        this.paymentGateway = paymentGateway;
        this.eventPublisher = eventPublisher;
    }

    @Override
    public PayOrderOutput execute(PayOrderInput input) {
        // 1. Load entity
        Order order = orderRepository.findById(input.orderId())
            .orElseThrow(() -> new OrderNotFoundException(input.orderId()));

        // 2. Charge payment (through Output Port)
        PaymentResult result = paymentGateway.charge(
            order.totalAmount(),
            PaymentMethod.fromId(input.paymentMethodId())
        );

        if (result.isFailed()) {
            throw new PaymentFailedException(result.errorMessage());
        }

        // 3. Execute business behavior on entity
        order.pay();

        // 4. Save
        orderRepository.save(order);

        // 5. Publish events
        eventPublisher.publishAll(order.domainEvents());
        order.clearEvents();

        // 6. Return result
        return new PayOrderOutput(
            order.id(),
            order.status(),
            result.transactionId()
        );
    }
}
```

## Query Interactor (Read Model)

```java
public class GetOrderInteractor implements GetOrderUseCase {

    private final OrderRepository orderRepository;

    public GetOrderInteractor(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    @Override
    public GetOrderOutput execute(GetOrderInput input) {
        return orderRepository.findById(input.orderId())
            .map(order -> new GetOrderOutput(
                order.id(),
                order.status(),
                order.totalAmount(),
                order.items().stream()
                    .map(item -> new GetOrderOutput.OrderItemOutput(
                        item.productId().value(),
                        item.quantity(),
                        item.subtotal()
                    )).toList()
            ))
            .orElseThrow(() -> new OrderNotFoundException(input.orderId()));
    }
}
```

## Testing Interactors

```java
class CreateOrderInteractorTest {

    private InMemoryOrderRepository orderRepo;
    private SpyEventPublisher eventPublisher;
    private SpyNotificationPort notificationPort;
    private CreateOrderInteractor interactor;

    @BeforeEach
    void setUp() {
        orderRepo = new InMemoryOrderRepository();
        eventPublisher = new SpyEventPublisher();
        notificationPort = new SpyNotificationPort();
        interactor = new CreateOrderInteractor(
            orderRepo, eventPublisher, notificationPort);
    }

    @Test
    void shouldCreateOrder() {
        var input = new CreateOrderInput("CUST-001", List.of(
            new OrderItemInput("PROD-001", 2, new MoneyInput("10.00", "USD"))
        ));

        var output = interactor.execute(input);

        assertThat(output.status()).isEqualTo(OrderStatus.DRAFT);
        assertThat(orderRepo.findById(output.orderId())).isPresent();
        assertThat(eventPublisher.publishedEvents()).hasSize(1);
    }

    @Test
    void shouldFailForInvalidInput() {
        var input = new CreateOrderInput("CUST-001", List.of());
        assertThatThrownBy(() -> interactor.execute(input))
            .isInstanceOf(DomainException.class);
    }
}
```

## In-Memory Test Repositories

```java
package com.example.test;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

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
```

## Interactor Anti-patterns

| Anti-pattern | Problem | Solution |
|---|---|---|
| **Fat Interactor** | Contains business if/else logic | Move to Entity/Domain Service |
| **Transaction in Interactor** | Mixes infrastructure concern | Use Framework @Transactional wrapper |
| **Accessing external APIs directly** | Breaks dependency rule | Go through Output Ports |
| **Catching and swallowing exceptions** | Hides errors | Let exceptions propagate or wrap in domain exception |
| **Returning Entity directly** | Exposes internals | Always return Output DTO |
