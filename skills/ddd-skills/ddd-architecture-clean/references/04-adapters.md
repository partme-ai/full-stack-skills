# Interface Adapters Layer

## Location: `{project}-adapter/`

The **Interface Adapters** layer converts data between the UseCase layer (DTOs) and the outside world (HTTP, DB, MQ). It consists of:

| Sub-module | Responsibility |
|------------|---------------|
| `controller/` | REST/gRPC controllers — receive HTTP, call Input Ports |
| `presenter/` | Response format conversion — Output DTO → HTTP response |
| `repository/` | DB implementation — implements Output Ports |
| `gateway/` | External API implementation — implements Output Ports |
| `converter/` | DTO/PO ↔ Entity/VO conversion |

## Controller Template

```java
package com.example.adapter.controller;

import com.example.usecase.port.input.CreateOrderUseCase;
import com.example.usecase.port.input.GetOrderUseCase;
import com.example.usecase.dto.input.CreateOrderInput;
import com.example.usecase.dto.input.GetOrderInput;
import com.example.usecase.dto.output.CreateOrderOutput;
import com.example.usecase.dto.output.GetOrderOutput;
import com.example.core.valueobject.OrderId;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

/**
 * ★ Controller — Interface Adapter.
 * Converts HTTP requests → UseCase calls → HTTP responses.
 */
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

    private final CreateOrderUseCase createOrderUseCase;
    private final GetOrderUseCase getOrderUseCase;

    public OrderController(
            CreateOrderUseCase createOrderUseCase,
            GetOrderUseCase getOrderUseCase) {
        this.createOrderUseCase = createOrderUseCase;
        this.getOrderUseCase = getOrderUseCase;
    }

    @PostMapping
    public ResponseEntity<CreateOrderResponse> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {

        // Convert HTTP request → UseCase Input DTO
        CreateOrderInput input = request.toInput();

        // Call UseCase through Input Port
        CreateOrderOutput output = createOrderUseCase.execute(input);

        // Convert Output DTO → HTTP response via Presenter
        CreateOrderResponse response = CreateOrderResponse.from(output);

        return ResponseEntity.status(201).body(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<GetOrderResponse> getOrder(
            @PathVariable String id) {

        GetOrderInput input = new GetOrderInput(OrderId.of(id));
        GetOrderOutput output = getOrderUseCase.execute(input);
        GetOrderResponse response = GetOrderResponse.from(output);

        return ResponseEntity.ok(response);
    }
}
```

## Request/Response DTOs

```java
package com.example.adapter.dto.request;

import com.example.usecase.dto.input.CreateOrderInput;
import jakarta.validation.constraints.*;
import java.util.List;

public record CreateOrderRequest(
    @NotBlank String customerId,
    @NotEmpty List<CreateOrderRequestItem> items
) {
    public CreateOrderInput toInput() {
        return new CreateOrderInput(
            this.customerId,
            this.items.stream()
                .map(i -> new CreateOrderInput.OrderItemInput(
                    i.productId, i.quantity, new CreateOrderInput.MoneyInput(
                        String.valueOf(i.unitPrice), "USD")))
                .toList()
        );
    }

    public record CreateOrderRequestItem(
        @NotBlank String productId,
        @Min(1) int quantity,
        @NotNull Double unitPrice
    ) {}
}

package com.example.adapter.dto.response;

public record CreateOrderResponse(
    String orderId,
    String totalAmount,
    String status
) {
    public static CreateOrderResponse from(CreateOrderOutput output) {
        return new CreateOrderResponse(
            output.orderId().value(),
            output.totalAmount().amount().toPlainString(),
            output.status().name()
        );
    }
}
```

## Repository Implementation (Output Port Adapter)

```java
package com.example.adapter.repository;

import com.example.core.entity.Order;
import com.example.core.valueobject.OrderId;
import com.example.usecase.port.output.OrderRepository;
import com.example.adapter.converter.OrderPersistenceConverter;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

/**
 * ★ Repository Implementation — Driven Adapter.
 * Implements the Output Port defined in the UseCase layer.
 */
@Repository
@Transactional
public class JpaOrderRepository implements OrderRepository {

    private final SpringDataOrderJpaRepository jpaRepo;
    private final OrderPersistenceConverter converter;

    public JpaOrderRepository(
            SpringDataOrderJpaRepository jpaRepo,
            OrderPersistenceConverter converter) {
        this.jpaRepo = jpaRepo;
        this.converter = converter;
    }

    @Override
    public Order save(Order order) {
        OrderEntity entity = converter.toPersistence(order);
        OrderEntity saved = jpaRepo.save(entity);
        return converter.toDomain(saved);
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.value())
            .map(converter::toDomain);
    }

    @Override
    public void delete(OrderId id) {
        jpaRepo.deleteById(id.value());
    }
}
```

## Persistence Entity (Framework Layer)

```java
package com.example.adapter.repository.entity;

import com.example.core.valueobject.OrderStatus;
import jakarta.persistence.*;
import java.math.BigDecimal;

/**
 * ★ JPA Entity — lives in the Adapter/Infrastructure layer.
 * Separate from the Domain Entity. Framework annotations
 * are confined to this layer.
 */
@Entity
@Table(name = "orders")
public class OrderEntity {

    @Id
    private String id;

    @Enumerated(EnumType.STRING)
    private OrderStatus status;

    private BigDecimal totalAmount;
    private String currency;

    private String customerId;

    @Version
    private Long version;

    // JPA requires default constructor
    protected OrderEntity() {}

    public OrderEntity(String id, OrderStatus status,
                       BigDecimal totalAmount, String currency,
                       String customerId) {
        this.id = id;
        this.status = status;
        this.totalAmount = totalAmount;
        this.currency = currency;
        this.customerId = customerId;
    }

    // Getters and setters...
}
```

## Persistence Converter

```java
package com.example.adapter.converter;

import com.example.core.entity.Order;
import com.example.core.valueobject.Money;
import com.example.core.valueobject.OrderId;
import com.example.core.valueobject.OrderStatus;
import com.example.adapter.repository.entity.OrderEntity;
import org.springframework.stereotype.Component;

import java.util.Currency;

@Component
public class OrderPersistenceConverter {

    public OrderEntity toPersistence(Order order) {
        return new OrderEntity(
            order.id().value(),
            order.status(),
            order.totalAmount().amount(),
            order.totalAmount().currency().getCurrencyCode(),
            order.customerId()  // assuming Order has customerId
        );
    }

    public Order toDomain(OrderEntity entity) {
        return new Order(
            new OrderId(entity.getId()),
            new Money(entity.getTotalAmount(),
                Currency.getInstance(entity.getCurrency()))
        );
    }
}
```

## External Gateway Adapter

```java
package com.example.adapter.gateway;

import com.example.core.valueobject.Money;
import com.example.usecase.port.output.PaymentGateway;
import org.springframework.stereotype.Component;

@Component
public class StripePaymentGateway implements PaymentGateway {

    private final StripeClient stripeClient;

    public StripePaymentGateway(StripeClient stripeClient) {
        this.stripeClient = stripeClient;
    }

    @Override
    public PaymentResult charge(Money amount, PaymentMethod method) {
        try {
            StripePaymentIntent intent = stripeClient.paymentIntents.create(
                PaymentIntentCreateParams.builder()
                    .setAmount(amount.amount().longValue())
                    .setCurrency(amount.currency().getCurrencyCode())
                    .setPaymentMethod(method.id())
                    .setConfirm(true)
                    .build()
            );
            return PaymentResult.success(PaymentId.from(intent.getId()));
        } catch (StripeException e) {
            return PaymentResult.failed(e.getMessage());
        }
    }

    @Override
    public RefundResult refund(PaymentId paymentId, Money amount) {
        // Implementation...
        return null;
    }
}
```

## Adapter Anti-patterns

| Anti-pattern | Problem | Solution |
|---|---|---|
| **Business logic in Controller** | Controller contains if/else business rules | Move to UseCase/Entity |
| **Framework annotations in domain** | Domain knows about JPA/Spring | Keep domain POJO, annotations only in adapter |
| **Repository returns Entity directly** | Breaks persistence mapping | Always convert PO ↔ Domain in adapter |
| **Conversions in Controller** | Violates SRP | Use dedicated converter/assembler |
