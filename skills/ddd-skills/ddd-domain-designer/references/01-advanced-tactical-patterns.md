# 进阶战术模式 — Factory、Specification、Domain Service

## Factory（工厂）

封装复杂的聚合/实体创建逻辑。

### 何时使用
- 创建逻辑复杂
- 需要在创建时强制不变式
- 需要构建对象图

### 模式

```java
public interface OrderFactory {
    Order createFromCart(Cart cart, Customer customer);
}

public class OrderFactoryImpl implements OrderFactory {
    private final PricingService pricingService;

    public Order createFromCart(Cart cart, Customer customer) {
        if (cart.isEmpty()) throw new IllegalArgumentException("Cart is empty");

        Order order = Order.create(customer.getId());

        for (CartItem cartItem : cart.getItems()) {
            order.addItem(cartItem.getProductId(),
                Quantity.of(cartItem.getQuantity()), cartItem.getUnitPrice());
        }

        if (customer.getDefaultAddress() != null) {
            order.setShippingAddress(customer.getDefaultAddress());
        }

        return order;
    }
}
```

## Specification（规约模式）

封装可组合的业务规则，用于查询或验证。

```java
public interface Specification<T> {
    boolean isSatisfiedBy(T candidate);
    Specification<T> and(Specification<T> other);
    Specification<T> or(Specification<T> other);
    Specification<T> not();
}

public class OrderAmountSpec implements Specification<Order> {
    private final Money minAmount;

    public boolean isSatisfiedBy(Order order) {
        return order.getTotal().greaterThan(minAmount);
    }
}

public class CustomerVIPSpec implements Specification<Customer> {
    public boolean isSatisfiedBy(Customer customer) {
        return customer.isVIP();
    }
}

// 组合使用
var spec = new OrderAmountSpec(Money.cny(100))
    .and(new OrderStatusSpec(OrderStatus.DRAFT));
var eligibleOrders = orderRepo.findAll().stream()
    .filter(spec::isSatisfiedBy).toList();
```

## Domain Service（领域服务）

无法自然归属于某个实体或值对象的无状态操作。

### 何时使用
- 操作涉及多个聚合
- 操作需要外部信息
- 重要的业务逻辑不属于任何一个实体

```java
public interface PricingService {
    Money calculateDiscount(Order order, Customer customer);
}

public class PricingServiceImpl implements PricingService {
    public Money calculateDiscount(Order order, Customer customer) {
        Money discount = Money.zero();

        if (order.itemCount() > 10) {
            discount = discount.add(order.getTotal().multiply(0.05));
        }
        if (customer.isVIP()) {
            discount = discount.add(order.getTotal().multiply(0.10));
        }

        Money maxDiscount = order.getTotal().multiply(0.20);
        return discount.isGreaterThan(maxDiscount) ? maxDiscount : discount;
    }
}
```

```java
public interface ShippingCostCalculator {
    Money calculate(List<OrderItem> items, Address destination);
}

public class ShippingCostCalculatorImpl implements ShippingCostCalculator {
    public Money calculate(List<OrderItem> items, Address destination) {
        Money baseRate = Money.usd(5.99);
        Money perItemRate = Money.usd(1.50);
        Money total = baseRate.add(perItemRate.multiply(items.size()));

        if (!destination.getCountry().equals("US")) {
            total = total.add(Money.usd(15.00));
        }
        return total;
    }
}
```

## Aggregate 完整模式（含 reconstitute）

```java
public class Order extends AggregateRoot<OrderId> {
    private CustomerId customerId;
    private List<OrderItem> items = new ArrayList<>();
    private OrderStatus status = OrderStatus.DRAFT;
    private Address shippingAddress;

    // Factory method
    public static Order create(CustomerId customerId) {
        Order order = new Order(OrderId.generate(), customerId);
        order.addDomainEvent(new OrderCreated(order.getId(), customerId));
        return order;
    }

    // Reconstitution method (for persistence loading)
    public static Order reconstitute(OrderId id, CustomerId customerId,
            List<OrderItem> items, OrderStatus status, Address shippingAddress) {
        Order order = new Order(id, customerId);
        order.items = new ArrayList<>(items);
        order.status = status;
        order.shippingAddress = shippingAddress;
        return order;
    }

    private Order(OrderId id, CustomerId customerId) {
        super(id);
        this.customerId = customerId;
    }

    public void addItem(ProductId productId, Quantity quantity, Money unitPrice) {
        assertCanModify();
        if (quantity.value() <= 0) throw new IllegalArgumentException("Quantity must be positive");

        items.stream().filter(i -> i.getProductId().equals(productId)).findFirst()
            .ifPresentOrElse(i -> i.increaseQuantity(quantity.value()),
                () -> items.add(OrderItem.create(productId, quantity, unitPrice)));

        addDomainEvent(new OrderItemAdded(getId(), productId, quantity));
    }

    public void confirm() {
        assertStatus(OrderStatus.DRAFT);
        if (items.isEmpty()) throw new EmptyOrderException();
        if (shippingAddress == null) throw new MissingAddressException();
        this.status = OrderStatus.CONFIRMED;
        addDomainEvent(new OrderConfirmed(getId(), getTotal()));
    }

    public void cancel(String reason) {
        if (status == OrderStatus.SHIPPED || status == OrderStatus.DELIVERED)
            throw new InvalidStateException("Cannot cancel shipped/delivered order");
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelled(getId(), reason));
    }

    public Money getTotal() {
        return items.stream().map(OrderItem::getSubtotal)
            .reduce(Money.zero(), Money::add);
    }

    private void assertCanModify() {
        if (status == OrderStatus.CANCELLED)
            throw new InvalidStateException("Order is cancelled");
    }

    private void assertStatus(OrderStatus expected) {
        if (status != expected)
            throw new InvalidStateException("Expected " + expected + " but was " + status);
    }
}
```
