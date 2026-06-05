# Example: Repository Implementation (Adapter Layer)

## Overview

This example shows the complete chain from Output Port interface → JPA Entity → Repository Implementation → Unit Test.

## Package Structure

```
order-adapter/
├── repository/
│   ├── JpaOrderRepository.java          ← Implements OrderRepository Output Port
│   └── entity/
│       └── OrderEntity.java             ← JPA persistence entity
├── converter/
│   └── OrderPersistenceConverter.java   ← Domain ↔ Persistence mapping
└── gateway/
    └── EventPublisherAdapter.java       ← Implements EventPublisher Output Port
```

## Step 1: Output Port (UseCase Layer — what adapter implements)

```java
// File: order-usecase/src/main/java/.../port/output/OrderRepository.java
package com.example.usecase.port.output;

import com.example.core.entity.Order;
import com.example.core.valueobject.OrderId;
import java.util.Optional;

/**
 * ★ Output Port — defined in UseCase layer.
 * The Adapter implements this interface.
 */
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
    void delete(OrderId id);
    boolean existsByCustomerId(CustomerId customerId);
}
```

## Step 2: JPA Entity (Adapter Layer)

```java
// File: order-adapter/src/main/java/.../repository/entity/OrderEntity.java
package com.example.adapter.repository.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.Instant;

/**
 * ★ JPA Entity — lives in the Adapter layer.
 * This is SEPARATE from the domain Order entity.
 * Framework annotations are confined here.
 */
@Entity
@Table(name = "orders")
public class OrderEntity {

    @Id
    @Column(length = 36)
    private String id;

    @Column(name = "customer_id", length = 36, nullable = false)
    private String customerId;

    @Column(name = "total_amount", precision = 19, scale = 2, nullable = false)
    private BigDecimal totalAmount;

    @Column(name = "currency", length = 3, nullable = false)
    private String currency;

    @Enumerated(EnumType.STRING)
    @Column(name = "status", length = 20, nullable = false)
    private OrderStatus status;

    @Column(name = "created_at", nullable = false)
    private Instant createdAt;

    @Column(name = "updated_at", nullable = false)
    private Instant updatedAt;

    @Version
    private Long version;

    // JPA requires default constructor
    protected OrderEntity() {}

    public OrderEntity(String id, String customerId,
                       BigDecimal totalAmount, String currency,
                       OrderStatus status,
                       Instant createdAt, Instant updatedAt) {
        this.id = id;
        this.customerId = customerId;
        this.totalAmount = totalAmount;
        this.currency = currency;
        this.status = status;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    // ── Getters (used by converter) ──
    public String getId() { return id; }
    public String getCustomerId() { return customerId; }
    public BigDecimal getTotalAmount() { return totalAmount; }
    public String getCurrency() { return currency; }
    public OrderStatus getStatus() { return status; }
    public Instant getCreatedAt() { return createdAt; }
    public Instant getUpdatedAt() { return updatedAt; }
    public Long getVersion() { return version; }

    public void setStatus(OrderStatus status) { this.status = status; }
    public void setUpdatedAt(Instant updatedAt) { this.updatedAt = updatedAt; }
}

/**
 * JPA Entity for order items (part of Order aggregate).
 */
@Entity
@Table(name = "order_items")
public class OrderItemEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "order_id", length = 36, nullable = false)
    private String orderId;

    @Column(name = "product_id", length = 36, nullable = false)
    private String productId;

    @Column(nullable = false)
    private int quantity;

    @Column(name = "unit_price", precision = 19, scale = 2, nullable = false)
    private BigDecimal unitPrice;

    @Column(name = "unit_currency", length = 3, nullable = false)
    private String unitCurrency;

    protected OrderItemEntity() {}

    // Constructor, getters...
}
```

## Step 3: Spring Data JPA Repository

```java
// File: order-adapter/src/main/java/.../repository/SpringDataOrderJpaRepository.java
package com.example.adapter.repository;

import com.example.adapter.repository.entity.OrderEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * ★ Spring Data JPA Repository — framework-specific.
 * Not to be confused with the domain Output Port.
 */
@Repository
public interface SpringDataOrderJpaRepository extends JpaRepository<OrderEntity, String> {
    boolean existsByCustomerId(String customerId);
}
```

## Step 4: Persistence Converter

```java
// File: order-adapter/src/main/java/.../converter/OrderPersistenceConverter.java
package com.example.adapter.converter;

import com.example.core.entity.Order;
import com.example.core.entity.OrderItem;
import com.example.core.valueobject.*;
import com.example.adapter.repository.entity.OrderEntity;
import org.springframework.stereotype.Component;

import java.util.Currency;
import java.util.stream.Collectors;

/**
 * ★ Converter — maps between Domain Entity and JPA Entity.
 * This is the ONLY place that knows about both representations.
 */
@Component
public class OrderPersistenceConverter {

    public OrderEntity toPersistence(Order order) {
        return new OrderEntity(
            order.id().value(),
            order.customerId().value(),
            order.totalAmount().amount(),
            order.totalAmount().currency().getCurrencyCode(),
            order.status(),
            order.createdAt(),
            order.updatedAt()
        );
    }

    public Order toDomain(OrderEntity entity) {
        // Reconstruct domain entity from persistence state
        OrderId id = OrderId.from(entity.getId());
        CustomerId customerId = CustomerId.of(entity.getCustomerId());
        Order order = Order.reconstruct(
            id,
            customerId,
            Money.of(entity.getTotalAmount(), Currency.getInstance(entity.getCurrency())),
            entity.getStatus(),
            entity.getCreatedAt(),
            entity.getUpdatedAt()
        );

        // Note: OrderItems would be loaded via a separate query or join
        return order;
    }
}
```

## Step 5: Repository Implementation (Impl)

```java
// File: order-adapter/src/main/java/.../repository/JpaOrderRepository.java
package com.example.adapter.repository;

import com.example.core.entity.Order;
import com.example.core.valueobject.CustomerId;
import com.example.core.valueobject.OrderId;
import com.example.usecase.port.output.OrderRepository;
import com.example.adapter.converter.OrderPersistenceConverter;
import com.example.adapter.repository.entity.OrderEntity;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

/**
 * ★ Repository Implementation — Adapter Layer.
 * Implements the Output Port defined in the UseCase layer.
 * All JPA/framework concerns are confined to this class.
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
    @Transactional
    public Order save(Order order) {
        OrderEntity entity = converter.toPersistence(order);
        OrderEntity saved = jpaRepo.save(entity);
        return converter.toDomain(saved);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.value())
            .map(converter::toDomain);
    }

    @Override
    @Transactional
    public void delete(OrderId id) {
        jpaRepo.deleteById(id.value());
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByCustomerId(CustomerId customerId) {
        return jpaRepo.existsByCustomerId(customerId.value());
    }
}
```

## Step 6: Repository Integration Test

```java
// File: order-adapter/src/test/java/.../repository/JpaOrderRepositoryTest.java
package com.example.adapter.repository;

import com.example.core.entity.Order;
import com.example.core.valueobject.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;
import org.springframework.context.annotation.Import;
import org.springframework.test.context.ActiveProfiles;

import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

/**
 * ★ Integration test for the repository implementation.
 * Uses a real (in-memory) database via @DataJpaTest.
 */
@DataJpaTest
@Import({JpaOrderRepository.class, OrderPersistenceConverter.class})
@ActiveProfiles("test")
class JpaOrderRepositoryTest {

    @Autowired
    private JpaOrderRepository repository;

    @Autowired
    private TestEntityManager em;

    @Test
    void shouldSaveAndFindOrder() {
        Order order = givenOrder();

        repository.save(order);

        Optional<Order> found = repository.findById(order.id());
        assertThat(found).isPresent();
        assertThat(found.get().id()).isEqualTo(order.id());
        assertThat(found.get().status()).isEqualTo(OrderStatus.DRAFT);
        assertThat(found.get().totalAmount()).isEqualTo(Money.of(100, "USD"));
    }

    @Test
    void shouldDeleteOrder() {
        Order order = givenOrder();
        repository.save(order);

        repository.delete(order.id());

        assertThat(repository.findById(order.id())).isEmpty();
    }

    @Test
    void shouldReturnEmptyForMissingOrder() {
        Optional<Order> found = repository.findById(OrderId.generate());
        assertThat(found).isEmpty();
    }

    private Order givenOrder() {
        return Order.create(
            OrderId.generate(),
            CustomerId.of("CUST-001")
        );
    }
}
```

## Event Publisher Adapter

```java
// File: order-adapter/src/main/java/.../gateway/EventPublisherAdapter.java
package com.example.adapter.gateway;

import com.example.core.event.DomainEvent;
import com.example.usecase.port.output.EventPublisher;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * ★ Driven Adapter — implements EventPublisher Output Port.
 * Uses RabbitMQ for production, configurable per profile.
 */
@Component
public class EventPublisherAdapter implements EventPublisher {

    private static final Logger log = LoggerFactory.getLogger(EventPublisherAdapter.class);
    private static final String EXCHANGE = "domain.events";

    private final RabbitTemplate rabbitTemplate;
    private final ObjectMapper objectMapper;

    public EventPublisherAdapter(RabbitTemplate rabbitTemplate, ObjectMapper objectMapper) {
        this.rabbitTemplate = rabbitTemplate;
        this.objectMapper = objectMapper;
    }

    @Override
    public void publish(DomainEvent event) {
        try {
            String json = objectMapper.writeValueAsString(event);
            String routingKey = event.getClass().getSimpleName();
            rabbitTemplate.convertAndSend(EXCHANGE, routingKey, json);
            log.info("Published event: {} (key={})", event.eventId(), routingKey);
        } catch (JsonProcessingException e) {
            log.error("Failed to serialize event: {}", event.eventId(), e);
            throw new EventPublishException("Failed to publish event", e);
        }
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        events.forEach(this::publish);
    }
}
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Separate JPA Entity from Domain Entity** | Domain Order is pure POJO; JPA OrderEntity has @Entity annotation. Prevents framework leak. |
| **Converter in Adapter layer** | Only the adapter knows about both representations. UseCase layer only sees Domain types. |
| **Output Port as interface** | UseCase defines what it needs; Adapter implements it. Full Dependency Inversion. |
| **@Transactional at repository level** | Transaction management is an infrastructure concern, not domain. |
| **Spring Data JPA confined to Adapter** | No @Repository or JPA annotations leak into UseCase or Enterprise layers. |
