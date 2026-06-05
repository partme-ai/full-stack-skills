# 01 — Domain Layer: Domain Model Design

> 领域层（Domain Layer）是洋葱架构的核心，零外部依赖，承载所有业务规则。

## 职责

- 定义业务实体、值对象、聚合根
- 实现充血模型的业务方法
- 定义 Repository 接口（纯抽象，无实现）
- 定义领域事件
- 定义领域服务

## 代码模板

### Aggregate Root（聚合根）

```java
// core/domain/model/order/Order.java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private CustomerId customerId;
    private Money totalAmount;
    private List<OrderItem> items;
    private OrderStatus status;
    private LocalDateTime createdAt;

    // 私有构造器，通过工厂方法创建
    private Order(OrderId id, CustomerId customerId) {
        this.id = id;
        this.customerId = customerId;
        this.items = new ArrayList<>();
        this.status = OrderStatus.DRAFT;
        this.createdAt = LocalDateTime.now();
    }

    // 工厂方法
    public static Order create(OrderId id, CustomerId customerId) {
        Order order = new Order(id, customerId);
        order.addDomainEvent(new OrderCreatedEvent(id, customerId));
        return order;
    }

    // 充血业务方法
    public void addItem(ProductId productId, Money price, int quantity) {
        if (quantity <= 0) {
            throw new DomainException("数量必须大于0");
        }
        if (this.status != OrderStatus.DRAFT) {
            throw new DomainException("只能向草稿订单添加商品");
        }
        this.items.add(new OrderItem(productId, price, quantity));
        this.totalAmount = calculateTotal();
    }

    public void submit() {
        if (this.items.isEmpty()) {
            throw new DomainException("不能提交空订单");
        }
        if (this.status != OrderStatus.DRAFT) {
            throw new DomainException("只能提交草稿订单");
        }
        this.status = OrderStatus.SUBMITTED;
        this.addDomainEvent(new OrderSubmittedEvent(this.id));
    }

    public void pay(PaymentGateway gateway) {
        if (this.status != OrderStatus.SUBMITTED) {
            throw new DomainException("当前状态不可支付");
        }
        gateway.charge(this.id, this.totalAmount);
        this.status = OrderStatus.PAID;
        this.addDomainEvent(new OrderPaidEvent(this.id, this.totalAmount));
    }

    private Money calculateTotal() {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }

    // getter — 只读暴露
    public OrderId getId() { return id; }
    public Money getTotalAmount() { return totalAmount; }
    public OrderStatus getStatus() { return status; }
    public List<OrderItem> getItems() { return Collections.unmodifiableList(items); }
}
```

### Value Object（值对象）

```java
// core/domain/model/shared/Money.java
public final class Money implements ValueObject {
    private final BigDecimal amount;
    private final Currency currency;

    public static final Money ZERO = new Money(BigDecimal.ZERO, Currency.getInstance("CNY"));

    private Money(BigDecimal amount, Currency currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public static Money of(BigDecimal amount, String currencyCode) {
        return new Money(amount, Currency.getInstance(currencyCode));
    }

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("货币单位不匹配");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public Money multiply(int times) {
        return new Money(this.amount.multiply(BigDecimal.valueOf(times)), this.currency);
    }

    // 值对象必须实现 equals/hashCode
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Money money = (Money) o;
        return amount.compareTo(money.amount) == 0 && currency.equals(money.currency);
    }

    @Override
    public int hashCode() {
        return Objects.hash(amount.stripTrailingZeros(), currency);
    }
}
```

### Repository Interface（仓储接口）

```java
// core/domain/repository/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(OrderId id);
    Page<Order> findByCustomerId(CustomerId customerId, Pageable pageable);
}
```

### Domain Service（领域服务）

```java
// core/domain/service/OrderPricingService.java
public class OrderPricingService {
    private final DiscountPolicy discountPolicy;

    public OrderPricingService(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }

    public Money calculateFinalPrice(Order order) {
        Money subtotal = order.getTotalAmount();
        Discount discount = discountPolicy.applyTo(order);
        return subtotal.subtract(discount.getAmount());
    }
}
```

### Domain Event（领域事件）

```java
// core/domain/event/OrderPaidEvent.java
public class OrderPaidEvent extends DomainEvent {
    private final OrderId orderId;
    private final Money paidAmount;
    private final LocalDateTime paidAt;

    public OrderPaidEvent(OrderId orderId, Money paidAmount) {
        this.orderId = orderId;
        this.paidAmount = paidAmount;
        this.paidAt = LocalDateTime.now();
    }

    public OrderId getOrderId() { return orderId; }
    public Money getPaidAmount() { return paidAmount; }
    public LocalDateTime getPaidAt() { return paidAt; }
}
```

## 规范检查清单

- [ ] 无任何框架 import（Spring/JPA/MyBatis）
- [ ] 实体采用充血模型（业务方法在实体内部）
- [ ] 值对象不可变（final 字段，无 setter）
- [ ] Repository 接口定义在 Domain 层
- [ ] 聚合根负责一致性边界
- [ ] 跨聚合通过 ID 引用（非对象引用）
- [ ] 关键业务操作发布领域事件
- [ ] 领域异常使用自定义异常（非 RuntimeException 裸抛）
