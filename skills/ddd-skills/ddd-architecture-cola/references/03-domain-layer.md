# COLA v5 领域层详解

## 领域层目录结构

```
{project}-domain/
├── model/                         # 领域模型
│   ├── entity/                    # 实体 + 聚合根（充血模型）
│   ├── vo/                        # 值对象（不可变）
│   ├── aggregate/                 # 聚合（v5 明确分离）
│   ├── event/                     # 领域事件
│   └── enums/                     # 领域枚举
├── service/                       # 领域服务（跨实体的复杂业务逻辑）
├── ability/                       # 领域能力（v5 新概念）
├── gateway/                       # 领域网关（端口，与外部交互的抽象）
├── repository/                    # 仓储接口（数据持久化抽象）
└── extension/                     # 领域扩展点
```

## 核心实现规则

### 1. 零框架依赖（P0）

Domain 层绝不允许出现以下 import：
```java
// ❌ 禁止
import org.springframework.stereotype.Service;
import javax.persistence.Entity;
import jakarta.persistence.*;
import org.apache.ibatis.annotations.Mapper;

// ✅ 允许
import java.util.Optional;
import java.math.BigDecimal;
import java.time.LocalDateTime;
```

### 2. 充血模型

```java
// Order 是聚合根（Aggregate Root），包含业务行为
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;       // 枚举/值对象，不是 String
    private Money totalAmount;        // 值对象，不是 BigDecimal
    private List<OrderItem> items;    // 实体集合

    // 业务行为在实体中
    public void pay() {
        if (!status.canPay()) {
            throw new OrderDomainException("当前状态不可支付");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }

    public void cancel(String reason) {
        if (status.isFinalState()) {
            throw new OrderDomainException("终态订单不可取消");
        }
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelledEvent(this.id, reason));
    }
}
```

### 3. 值对象不可变

```java
public class Money {
    private final BigDecimal amount;
    private final Currency currency;

    public Money(BigDecimal amount, Currency currency) {
        this.amount = amount.setScale(2, RoundingMode.HALF_UP);
        this.currency = currency;
    }

    // 无 setter，操作返回新对象
    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("币种不一致");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public BigDecimal getAmount() { return amount; }
    public Currency getCurrency() { return currency; }

    @Override
    public boolean equals(Object o) { /* 按值比较 */ }
    @Override
    public int hashCode() { /* 按值计算 */ }
}
```

### 4. 仓储接口

```java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    Order save(Order order);
    void delete(OrderId id);
    // 查询方法使用值对象作为参数
    Page<Order> findByStatus(OrderStatus status, Pageable pageable);
}
```

### 5. 领域网关（防腐层）

```java
// 定义在 domain，实现在 infrastructure
public interface ProductGateway {
    ProductInfo getProduct(ProductId productId);
    InventoryInfo checkInventory(ProductId productId, int quantity);
}
```

### 6. 领域能力（v5 新特性）

```java
public interface OrderAbility {
    boolean canBeCancelled(Order order);
    boolean canApplyPromotion(Order order, String promotionId);
}
```

## 领域层最佳实践

- **聚合大小**：一个聚合 ≤ 5 个实体，过大考虑拆分
- **聚合间引用**：通过 ID 引用，不是对象引用
- **一致性边界**：聚合内强一致，聚合间最终一致（通过领域事件）
- **仓储接口**：只定义在 Domain，不在 Domain 层实现
- **领域事件**：关键业务操作必须发布领域事件
