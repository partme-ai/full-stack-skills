# Rich Domain Model Refactoring Examples

## Example 1: Order Payment — From Anemic to Rich

### Before: Anemic Model ❌

```java
// Order.java — Pure data carrier
@Entity
@Table(name = "orders")
public class Order {
    private Long id;
    private String status;       // Bare string: "DRAFT", "PAID", etc.
    private BigDecimal totalAmount;
    private Long customerId;
    // 50+ lines of getters/setters only
}

// OrderService.java — God Service, 487 lines
@Service
public class OrderService {
    @Autowired
    private OrderMapper orderMapper;
    @Autowired
    private PaymentMapper paymentMapper;

    @Transactional
    public void pay(Long orderId) {                    // ALL logic in Service
        Order order = orderMapper.selectById(orderId);
        if (order == null) {
            throw new RuntimeException("Order not found");
        }
        if (!"DRAFT".equals(order.getStatus())) {      // Raw string comparison
            throw new RuntimeException("Invalid status");
        }
        // ... 30 more lines of business logic
        order.setStatus("PAID");                       // Public setter
        orderMapper.update(order);
    }
}
```

### After: Rich Domain Model ✅

```java
// Order.java — Rich aggregate root
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;          // Value Object, not String
    private Money totalAmount;           // Value Object, not BigDecimal
    private CustomerId customerId;       // ID reference, not Long
    private List<OrderItem> items;

    // No public constructor — use factory method
    private Order(OrderId id, CustomerId customerId) {
        super(id);
        this.customerId = customerId;
        this.status = OrderStatus.DRAFT;
        this.items = new ArrayList<>();
    }

    // Factory method with domain event
    public static Order create(OrderId id, CustomerId customerId) {
        Order order = new Order(id, customerId);
        order.addDomainEvent(new OrderCreated(id, customerId));
        return order;
    }

    // Rich behavior — not getter/setter
    public void pay() {
        if (!status.canTransitionTo(OrderStatus.PAID)) {
            throw new OrderDomainException(
                "Cannot pay order in status: " + status
            );
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaid(this.id, this.totalAmount));
    }

    public void cancel(String reason) {
        if (status.isFinalState()) {
            throw new OrderDomainException(
                "Cannot cancel order in final state: " + status
            );
        }
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelled(this.id, reason));
    }
}

// OrderStatus.java — Immutable Value Object
public final class OrderStatus {
    public static final OrderStatus DRAFT = new OrderStatus("DRAFT", 0);
    public static final OrderStatus CONFIRMED = new OrderStatus("CONFIRMED", 1);
    public static final OrderStatus PAID = new OrderStatus("PAID", 2);
    public static final OrderStatus SHIPPED = new OrderStatus("SHIPPED", 3);
    public static final OrderStatus DELIVERED = new OrderStatus("DELIVERED", 4);
    public static final OrderStatus CANCELLED = new OrderStatus("CANCELLED", -1);

    private final String name;
    private final int order;  // For state transition validation

    private OrderStatus(String name, int order) {
        this.name = name;
        this.order = order;
    }

    public boolean canTransitionTo(OrderStatus target) {
        // DRAFT → CONFIRMED → PAID → SHIPPED → DELIVERED (forward)
        // Any → CANCELLED (except DELIVERED)
        return (target == CANCELLED && this != DELIVERED)
            || (target.order > this.order && target.order - this.order == 1);
    }

    // No setters — immutability
}
```

---

## Example 2: Customer Registration — Guard Conditions

### Before: Anemic ❌

```java
// CustomerService.java — Business logic leaked into service
@Service
public class CustomerService {
    @Autowired
    private CustomerMapper customerMapper;

    public void register(String email, String name) {
        // Validation in Service
        if (email == null || !email.contains("@")) {
            throw new RuntimeException("Invalid email");
        }
        if (name == null || name.length() < 2) {
            throw new RuntimeException("Name too short");
        }
        // Business rule in Service
        Customer existing = customerMapper.findByEmail(email);
        if (existing != null) {
            throw new RuntimeException("Email already registered");
        }
        customerMapper.insert(email, name, "ACTIVE");
    }
}
```

### After: Rich ✅

```java
// Customer.java — Rich aggregate root with self-validation
public class Customer extends AggregateRoot<CustomerId> {
    private Email email;           // Value Object
    private PersonName name;       // Value Object
    private CustomerStatus status;
    private final List<CustomerDomainEvent> events = new ArrayList<>();

    private Customer(CustomerId id, Email email, PersonName name) {
        super(id);
        this.email = email;
        this.name = name;
        this.status = CustomerStatus.ACTIVE;
    }

    public static Customer register(CustomerId id, Email email, PersonName name) {
        // Domain logic encapsulated in entity
        Customer customer = new Customer(id, email, name);
        customer.addDomainEvent(new CustomerRegistered(id, email));
        return customer;
    }
}

// Email.java — Self-validating Value Object
public final class Email {
    private final String value;

    public Email(String value) {
        if (value == null || !value.matches("^[\\w.-]+@[\\w.-]+\\.\\w{2,}$")) {
            throw new InvalidEmailException(value);
        }
        this.value = value.toLowerCase();
    }

    public String getValue() { return value; }
    // No setter — immutability
}

// CustomerRepository.java — Interface in domain
public interface CustomerRepository {
    boolean existsByEmail(Email email);
    void save(Customer customer);
    Optional<Customer> findById(CustomerId id);
}
```

---

## Example 3: Value Object Introduction

### Before: Primitive Obsession ❌

```java
public class Order {
    private Long id;
    private String receiverName;      // Raw string
    private String receiverPhone;     // Raw string — no validation
    private String province;          // Raw string
    private String city;              // Raw string
    private String street;            // Raw string
    private String zipCode;           // Raw string — no format check
    private BigDecimal price;         // Raw BigDecimal — no currency
}
```

### After: Value Objects ✅

```java
public class Order extends AggregateRoot<OrderId> {
    private ShippingAddress shippingAddress;  // Value Object
    private Money total;                       // Value Object

    // When setting shipping address:
    public void setShippingAddress(ShippingAddress address) {
        if (this.status != OrderStatus.DRAFT) {
            throw new OrderDomainException("Can only set address in DRAFT status");
        }
        this.shippingAddress = address;
    }
}

// ShippingAddress.java — Immutable Value Object
public final class ShippingAddress {
    private final String receiverName;
    private final PhoneNumber phone;       // Nested Value Object
    private final String province;
    private final String city;
    private final String street;
    private final ZipCode zipCode;         // Nested Value Object

    public ShippingAddress(
            String receiverName,
            PhoneNumber phone,
            String province,
            String city,
            String street,
            ZipCode zipCode) {
        // Guard conditions
        if (receiverName == null || receiverName.isBlank()) {
            throw new IllegalArgumentException("receiverName required");
        }
        this.receiverName = receiverName;
        this.phone = phone;
        this.province = province;
        this.city = city;
        this.street = street;
        this.zipCode = zipCode;
    }
    // No setters — immutability
}

// ZipCode.java — Self-validating Value Object
public final class ZipCode {
    private final String value;
    public ZipCode(String value) {
        if (value == null || !value.matches("\\d{5}(-\\d{4})?")) {
            throw new InvalidZipCodeException(value);
        }
        this.value = value;
    }
    public String getValue() { return value; }
}

// Money.java — Value Object with behavior
public final class Money {
    private final BigDecimal amount;
    private final Currency currency;

    public Money(BigDecimal amount, Currency currency) {
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new InvalidMoneyException("Amount cannot be negative");
        }
        this.amount = amount;
        this.currency = currency;
    }

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new CurrencyMismatchException(this.currency, other.currency);
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public Money multiply(int factor) {
        return new Money(this.amount.multiply(BigDecimal.valueOf(factor)), this.currency);
    }
}
```

## Refactoring Impact Summary

| Metric | Before | After | Improvement |
|--------|:------:|:-----:|:-----------:|
| Business logic in entity | 0% | 100% | Core domain encapsulated |
| Value Object coverage | 0/7 fields | 6/7 fields | 86% primitive reduction |
| Service line count | 487 lines | 42 lines | 91% reduction (pure orchestration) |
| Testability | Mock-heavy, fragile | Pure unit tests, no mocks | Faster, more reliable tests |
| Domain events emitted | 0 | 4 | Observable domain operations |
| JPA dependency in domain | Yes | No | Clean domain, DIP satisfied |
