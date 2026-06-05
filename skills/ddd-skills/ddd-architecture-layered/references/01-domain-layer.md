# Domain Layer — 领域层

> 领域层是 DDD 分层架构的核心，包含所有业务逻辑和规则，**零外部依赖**。

## 职责

- 表达业务概念、业务状态和业务规则
- 实现核心业务逻辑（充血模型）
- 定义仓储接口（依赖倒置的前提）
- 定义领域事件

## 包含的子模块

```
domain/{aggregate}/
├── entity/                    # 实体 + 聚合根（充血模型）
│   ├── Order.java            # 聚合根
│   └── OrderItem.java        # 子实体
├── valueobject/               # 值对象（不可变）
│   ├── Money.java
│   ├── Address.java
│   └── OrderStatus.java
├── event/                     # 领域事件
│   └── OrderPlacedEvent.java
├── service/                   # 领域服务（多实体协作）
│   └── PricingService.java
├── repository/                # 仓储接口（只有定义）
│   └── OrderRepository.java
├── specification/             # 规约模式
├── factory/                   # 工厂模式
├── policy/                    # 业务策略
└── exception/                 # 领域异常
    ├── DomainException.java
    └── BusinessRuleException.java
```

## 关键规则

1. **零框架依赖** — 不能 import Spring/JPA/MyBatis 任何注解
2. **纯业务逻辑** — 只能使用 JDK 原生类型和领域类型
3. **充血模型** — 实体必须有业务方法，不能只有 getter/setter
4. **值对象不可变** — 所有字段 final，构造器初始化
5. **聚合间 ID 引用** — 不能直接引用其他聚合的对象

## 聚合根代码示例

```java
// 纯 POJO，无 @Entity、@Service 等注解
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;
    private Money totalAmount;
    private List<OrderItem> items;

    public void pay() {
        if (!status.canPay()) {
            throw new OrderException("当前状态不可支付");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }

    public void addItem(ProductId productId, Money price, int quantity) {
        if (quantity <= 0) {
            throw new IllegalArgumentException("数量必须大于0");
        }
        this.items.add(new OrderItem(productId, price, quantity));
        recalculateTotal();
    }

    private void recalculateTotal() {
        this.totalAmount = items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }
}
```

## 值对象代码示例

```java
public class Money {
    private final BigDecimal amount;
    private final String currency;

    public Money(BigDecimal amount, String currency) {
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("金额不能为负数");
        }
        this.amount = amount;
        this.currency = currency;
    }

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("货币类型不匹配");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    // 只有 getter，没有 setter
    public BigDecimal getAmount() { return amount; }
    public String getCurrency() { return currency; }
}
```

## 仓储接口代码示例

```java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(OrderId id);
}
```

## 领域服务代码示例

```java
// 当业务逻辑涉及多个实体时使用领域服务
public class PricingService {
    public Money calculateTotal(List<OrderItem> items) {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }

    public Money applyDiscount(Money total, DiscountPolicy policy) {
        return policy.apply(total);
    }
}
```

## 参考

- Eric Evans 《领域驱动设计》第 4-6 章
- Vaughn Vernon 《实现领域驱动设计》第 7-10 章
- [ddd4j-layered-structure.md](./ddd4j-layered-structure.md)
- [directory-structure.md](./directory-structure.md)
