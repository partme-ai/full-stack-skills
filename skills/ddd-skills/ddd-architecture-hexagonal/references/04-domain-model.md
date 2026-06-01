# Domain Model — 领域模型设计

## 概述

领域模型是六边形架构的核心，位于最内层，零外部依赖。领域模型包含聚合根（Aggregate Root）、实体（Entity）、值对象（Value Object）、领域服务（Domain Service）和领域事件（Domain Event）。

## 聚合根

聚合根是聚合的入口点，外部只能通过聚合根访问聚合内部。

```java
// domain/model/order/Order.java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private CustomerId customerId;
    private Money totalAmount;
    private OrderStatus status;
    private List<OrderItem> items;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // 只有无参构造 + Builder（框架需要）或全参构造
    protected Order() {}

    // 工厂方法
    public static Order create(CustomerId customerId) {
        Order order = new Order();
        order.id = OrderId.generate();
        order.customerId = customerId;
        order.status = OrderStatus.DRAFT;
        order.items = new ArrayList<>();
        order.totalAmount = Money.ZERO;
        order.createdAt = LocalDateTime.now();
        order.addDomainEvent(new OrderCreatedEvent(order.id, customerId));
        return order;
    }

    // 行为方法（充血模型）
    public void addItem(ProductId productId, Quantity quantity, Money unitPrice) {
        if (status != OrderStatus.DRAFT) {
            throw new OrderException("只能向草稿订单添加商品");
        }
        var item = new OrderItem(productId, quantity, unitPrice);
        items.add(item);
        recalculateTotal();
    }

    public void pay() {
        if (!status.canTransitionTo(OrderStatus.PAID)) {
            throw new OrderException("当前状态不可支付");
        }
        this.status = OrderStatus.PAID;
        this.updatedAt = LocalDateTime.now();
        addDomainEvent(new OrderPaidEvent(this.id, this.totalAmount));
    }

    public void cancel(String reason) {
        if (status == OrderStatus.DELIVERED || status == OrderStatus.CANCELLED) {
            throw new OrderException("已发货或已取消的订单不可取消");
        }
        this.status = OrderStatus.CANCELLED;
        this.updatedAt = LocalDateTime.now();
        addDomainEvent(new OrderCancelledEvent(this.id, reason));
    }

    private void recalculateTotal() {
        this.totalAmount = items.stream()
                .map(OrderItem::getSubtotal)
                .reduce(Money.ZERO, Money::add);
    }

    // Getter（无 Setter — 通过行为方法修改状态）
    public OrderId getId() { return id; }
    public OrderStatus getStatus() { return status; }
    public Money getTotalAmount() { return totalAmount; }
    public List<OrderItem> getItems() { return Collections.unmodifiableList(items); }
}
```

## 实体

```java
// domain/model/order/OrderItem.java
public class OrderItem {
    private ProductId productId;
    private Quantity quantity;
    private Money unitPrice;

    // 值对象作为实体属性
    OrderItem(ProductId productId, Quantity quantity, Money unitPrice) {
        this.productId = productId;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    public Money getSubtotal() {
        return unitPrice.multiply(quantity.getValue());
    }

    // Getter
    public ProductId getProductId() { return productId; }
    public Quantity getQuantity() { return quantity; }
    public Money getUnitPrice() { return unitPrice; }
}
```

## 值对象

```java
// domain/model/shared/Money.java
public final class Money {
    private final BigDecimal amount;
    private final Currency currency;

    private Money(BigDecimal amount, Currency currency) {
        // 不变式验证
        if (amount == null || currency == null) {
            throw new IllegalArgumentException("金额和货币不能为空");
        }
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("金额不能为负");
        }
        this.amount = amount;
        this.currency = currency;
    }

    // 工厂方法
    public static Money of(BigDecimal amount, String currencyCode) {
        return new Money(amount, Currency.getInstance(currencyCode));
    }

    public static Money of(double amount, String currencyCode) {
        return new Money(BigDecimal.valueOf(amount), Currency.getInstance(currencyCode));
    }

    public static final Money ZERO = new Money(BigDecimal.ZERO, Currency.getInstance("CNY"));

    // 行为方法
    public Money add(Money other) {
        validateSameCurrency(other);
        return new Money(amount.add(other.amount), currency);
    }

    public Money subtract(Money other) {
        validateSameCurrency(other);
        return new Money(amount.subtract(other.amount), currency);
    }

    public Money multiply(int multiplier) {
        return new Money(amount.multiply(BigDecimal.valueOf(multiplier)), currency);
    }

    public long toCents() {
        return amount.multiply(BigDecimal.valueOf(100)).longValue();
    }

    // equals & hashCode（基于所有字段）
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

    private void validateSameCurrency(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("货币不匹配");
        }
    }

    public BigDecimal getAmount() { return amount; }
    public String getCurrencyCode() { return currency.getCurrencyCode(); }
}
```

## 领域服务

当业务逻辑不属于单个实体或值对象时，使用领域服务。

```java
// domain/service/OrderPricingService.java
public class OrderPricingService {
    private final DiscountPolicy discountPolicy;

    public OrderPricingService(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }

    public Money calculateFinalPrice(Order order, CustomerGrade customerGrade) {
        var subtotal = order.getTotalAmount();
        var discount = discountPolicy.calculateDiscount(subtotal, customerGrade);
        var tax = calculateTax(subtotal.subtract(discount));
        return subtotal.subtract(discount).add(tax);
    }

    private Money calculateTax(Money taxableAmount) {
        return taxableAmount.multiply(13)  // 13% VAT
                .divide(100);
    }
}
```

## 领域事件

```java
// domain/event/OrderCreatedEvent.java
public class OrderCreatedEvent extends DomainEvent {
    private final OrderId orderId;
    private final CustomerId customerId;

    public OrderCreatedEvent(OrderId orderId, CustomerId customerId) {
        this.orderId = orderId;
        this.customerId = customerId;
    }

    public OrderId getOrderId() { return orderId; }
    public CustomerId getCustomerId() { return customerId; }
}

// domain/event/OrderPaidEvent.java
public class OrderPaidEvent extends DomainEvent {
    private final OrderId orderId;
    private final Money amount;

    public OrderPaidEvent(OrderId orderId, Money amount) {
        this.orderId = orderId;
        this.amount = amount;
    }

    public OrderId getOrderId() { return orderId; }
    public Money getAmount() { return amount; }
}
```

## 领域模型设计原则

| 原则 | 说明 | 反例 |
|------|------|------|
| **充血模型** | 行为在实体中，不在 Service 中 | 实体只有 getter/setter，逻辑在 OrderService |
| **封装不变式** | 聚合保证自身状态一致性 | 外部直接修改 Order.status |
| **值对象不可变** | 值对象创建后不能修改 | Money 有 setter 方法 |
| **聚合间 ID 引用** | 聚合之间通过 ID 引用，不直接引用对象 | `Order` 持有 `User` 对象引用 |
| **聚合内强一致** | 同一聚合内的事务一致性 | 跨聚合在同一个事务中操作 |
| **聚合间最终一致** | 不同聚合通过事件同步 | 订单和库存在一个事务中更新 |
