# DDD Core Concepts Reference

Detailed explanation of all Domain-Driven Design strategic and tactical patterns.

## Strategic Design Patterns

### 1. Bounded Context (限界上下文)

A bounded context is an explicit boundary within which a domain model exists. Inside the boundary, all terms and concepts have specific, well-defined meanings.

**Key Characteristics:**
- Each bounded context has its own ubiquitous language
- Models are consistent within the context
- Different contexts may have different models for the same business concept

**Example: E-commerce System**

```
Bounded Context: Order Management
  - "Customer" means: buyer with shipping address, payment methods
  - "Product" means: item with price, stock availability

Bounded Context: Customer Relations
  - "Customer" means: person with contact history, support tickets
  - "Product" means: item with warranty info, support documentation
```

**Identifying Bounded Contexts:**
1. Listen to how domain experts talk about the business
2. Identify when the same word means different things
3. Look for natural organizational boundaries
4. Find areas that can evolve independently

### 2. Ubiquitous Language (统一语言)

A language structured around the domain model and used by all team members to connect all activities of the team with the software.

**Rules:**
- Used in code: class names, method names, variable names
- Used in conversations: team discussions, planning meetings
- Used in documentation: specs, user stories, API docs
- Reflects the business, NOT technical implementation

**Example:**
```
BAD (Technical Language):
  OrderService.processPendingOrderStatusUpdate()

GOOD (Domain Language):
  Order.submit()
  Order.confirmPayment()
  Order.cancel(returnReason)
```

### 3. Context Mapping (上下文映射)

The relationships and interactions between bounded contexts.

**Relationship Patterns:**

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Partnership** | Teams cooperate, evolve together | Close collaboration, shared goals |
| **Shared Kernel** | Share a subset of the model | When duplication cost > coordination cost |
| **Customer-Supplier** | Upstream defines, downstream consumes | Clear dependency direction |
| **Conformist** | Downstream conforms to upstream model | No leverage to negotiate |
| **Anticorruption Layer** | Translation layer between contexts | Protecting context from external model |
| **Open Host Service** | Protocol for any integration | Multiple consumers, standardized API |
| **Published Language** | Well-documented interchange format | Cross-team communication |
| **Separate Ways** | No integration, independent evolution | Integration cost > benefit |

### 4. Core Domain / Subdomain Classification

| Type | Description | Investment Level | Example |
|------|-------------|-----------------|---------|
| **Core Domain** | What makes your business unique | Maximum investment | Order pricing algorithm |
| **Supporting Subdomain** | Supports core, but not unique | Moderate investment | Customer notification service |
| **Generic Subdomain** | Common capability, could be bought | Minimal investment | Authentication, logging |

## Tactical Design Patterns

### 1. Entity (实体)

An object defined by its identity, which remains consistent through state changes.

**Rules:**
- Identity is immutable and unique
- Equality is based on identity, not attributes
- Has a lifecycle (created, modified, archived/deleted)

```java
// Entity: defined by identity
public class Order {
    private OrderId id;        // Identity - NEVER changes
    private OrderStatus status; // Mutable state
    private List<OrderLine> lines;
    
    // Behavior, not just getters/setters
    public void addItem(Product product, Quantity qty) {
        // Business rule: can't add to shipped order
        if (this.status == OrderStatus.SHIPPED) {
            throw new OrderAlreadyShippedException(this.id);
        }
        // ... add logic
    }
}
```

### 2. Value Object (值对象)

An object defined by its attributes, with no conceptual identity.

**Rules:**
- Immutable — create a new instance instead of modifying
- Equality based on all attributes
- Replaceable — entirely replace one value object with another
- Self-validating — validates on construction

```java
// Value Object: defined by attributes
@Value // Lombok: makes it immutable
public class Money {
    BigDecimal amount;
    Currency currency;
    
    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new CurrencyMismatchException();
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }
}
```

### 3. Aggregate (聚合)

A cluster of domain objects treated as a single unit.

**Rules:**
- One aggregate = one transaction boundary
- Reference other aggregates by ID only (not direct object reference)
- The aggregate root is the only entry point
- All invariants within the aggregate must be enforced atomically

```
Aggregate: Order (Aggregate Root: Order entity)
├── Order (root)
│   ├── orderId: OrderId
│   ├── customerId: CustomerId  ← Reference by ID
│   ├── status: OrderStatus
│   └── totalAmount: Money
├── OrderLine (entity)
│   ├── productId: ProductId    ← Reference by ID
│   ├── quantity: Quantity
│   └── unitPrice: Money
└── ShippingAddress (value object)
    ├── street: String
    ├── city: String
    └── zipCode: String
```

### 4. Repository (仓储)

An abstraction for aggregate persistence. One repository per aggregate root.

```java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(Order order);
    List<Order> findByCustomerId(CustomerId customerId);
}
```

### 5. Domain Service (领域服务)

A stateless operation that doesn't naturally belong to any entity or value object.

**When to use a Domain Service:**
- The operation spans multiple aggregates
- The concept doesn't fit as a method on any entity
- Stateless operation

```java
public class PricingService {
    public Money calculateTotal(Order order, List<Discount> applicableDiscounts) {
        // Logic that involves multiple rules, external data
        // Doesn't naturally belong to Order or Discount
    }
}
```

### 6. Domain Event (领域事件)

Something meaningful that happened in the domain.

**Naming convention:** `{Aggregate}{Action}Event` in past tense

```java
public class OrderPlacedEvent {
    private OrderId orderId;
    private CustomerId customerId;
    private Money totalAmount;
    private Instant occurredAt;
}

public class PaymentConfirmationFailedEvent {
    private OrderId orderId;
    private String failureReason;
    private Instant occurredAt;
}
```

### 7. Specification (规约)

An encapsulated business rule that can be combined with others.

```java
public class ActiveOrderSpecification implements Specification<Order> {
    @Override
    public boolean isSatisfiedBy(Order order) {
        return order.getStatus() != OrderStatus.CANCELLED 
            && order.getStatus() != OrderStatus.DELIVERED;
    }
}

public class HighValueOrderSpecification implements Specification<Order> {
    private final Money threshold;
    
    @Override
    public boolean isSatisfiedBy(Order order) {
        return order.getTotalAmount().isGreaterThan(threshold);
    }
}

// Combine specifications
var spec = new ActiveOrderSpecification()
    .and(new HighValueOrderSpecification(new Money("1000", USD)));
```

## The Dependency Rule (CRITICAL)

```
Infrastructure → Application → Domain
   (adapters)     (use cases)    (core)

Dependencies ALWAYS point inward:
- Infrastructure depends on Application and Domain
- Application depends on Domain
- Domain depends on NOTHING external
```

**Domain layer MUST NOT have dependencies on:**
- Database frameworks (JPA, JDBC, MongoDB drivers)
- HTTP libraries (Spring MVC annotations, RestTemplate)
- Messaging (Kafka, RabbitMQ clients)
- Any infrastructure concern

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Anemic Domain Model | Logic in services, entities are data bags | Move behavior into domain objects |
| Repository per Entity | Breaks aggregate boundaries | One repository per aggregate root |
| God Aggregate | Too large, performance issues | Split into smaller aggregates |
| Direct Entity References | Cross-aggregate coupling | Reference by ID only |
| CRUD Thinking | Modeling data, not behavior | Focus on business operations |
| Premature CQRS | Unnecessary complexity | Start simple, evolve when needed |
| Framework-First Design | Domain polluted by framework concerns | Domain should be framework-agnostic |