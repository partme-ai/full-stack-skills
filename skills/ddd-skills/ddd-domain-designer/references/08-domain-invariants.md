# 领域不变式设计指南

## 什么是不变式

不变式（Invariant）是聚合内必须始终成立的业务规则。聚合根作为聚合的管理者，负责在每次状态变更后验证所有不变式。

**核心原则**：聚合封装不变式。边界之外的任何东西都不能破坏聚合内的业务规则。

## 不变式分类

| 类型 | 描述 | 示例 |
|------|------|------|
| **状态不变式** | 聚合状态必须在合法状态机内 | Order 状态流转：DRAFT → PAID → SHIPPED → DELIVERED |
| **值不变式** | 聚合内数据的取值范围/关系 | OrderItem.quantity > 0 且 OrderItem.price ≥ 0 |
| **组合不变式** | 多个实体间的约束关系 | 已支付订单不能修改商品列表 |
| **总量不变式** | 聚合内数据的累计约束 | 订单总金额 = Σ(商品单价 × 数量) |
| **时间不变式** | 时间维度的约束 | 订单超时未支付自动取消 |

## 不变式实现模式

### 1. 方法内校验（最常用）

```java
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;
    private List<OrderItem> items;
    private Money totalAmount;

    public void addItem(ProductId productId, Money unitPrice, int quantity) {
        // 不变式 1：只有 DRAFT 状态的订单可添加商品
        if (status != OrderStatus.DRAFT) {
            throw new OrderException("只能修改草稿订单");
        }
        // 不变式 2：数量必须为正
        if (quantity <= 0) {
            throw new OrderException("数量必须大于 0");
        }
        // 不变式 3：单价不能为负
        if (unitPrice.isNegative()) {
            throw new OrderException("单价不能为负");
        }
        items.add(new OrderItem(productId, unitPrice, quantity));
        recalculateTotal();
    }

    private void recalculateTotal() {
        // 不变式 4：总金额 = Σ(单价 × 数量)
        this.totalAmount = items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }
}
```

### 2. 规格模式（Specification Pattern）

适用于复杂且可复用的不变式。

```java
public class OrderCanBePaidSpecification implements Specification<Order> {
    @Override
    public boolean isSatisfiedBy(Order order) {
        return order.getStatus() == OrderStatus.DRAFT
            && order.getTotalAmount().isPositive()
            && !order.getItems().isEmpty();
    }
}

public class Order {
    public void pay(Specification<Order> canBePaidSpec) {
        if (!canBePaidSpec.isSatisfiedBy(this)) {
            throw new OrderException("订单不满足支付条件");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}
```

### 3. 领域服务校验

跨多个聚合根的不变式通过领域服务实现。

```java
public class OrderPricingService {
    public Money calculateDiscount(Order order, Customer customer) {
        // 不变式：VIP 客户折扣不超过 20%，普通客户不超过 10%
        if (customer.isVIP() && order.getDiscount().percent() > 20) {
            throw new PricingException("VIP 客户折扣不能超过 20%");
        }
        if (!customer.isVIP() && order.getDiscount().percent() > 10) {
            throw new PricingException("普通客户折扣不能超过 10%");
        }
        // ... 计算逻辑
    }
}
```

## 不变式文档化模板

每个聚合应附带不变式文档：

```markdown
## Order 聚合不变式

| ID | 类型 | 描述 | 检查时机 | 违反处理 |
|----|------|------|---------|---------|
| INV-01 | 状态 | 只有 DRAFT 状态的订单可修改 | addItem(), removeItem() | OrderException |
| INV-02 | 值 | OrderItem.quantity > 0 | addItem() | IllegalArgumentException |
| INV-03 | 组合 | 已支付订单不可取消（需走退款流程） | cancel() | OrderException |
| INV-04 | 总量 | 订单总金额 = Σ(单价 × 数量) | recalculateTotal() | 无异常（自动修复）|
| INV-05 | 时间 | 订单 30 分钟内未支付自动取消 | 定时任务 | OrderCancelled 事件 |
```

## 反模式

| 反模式 | 问题 | 修复 |
|--------|------|------|
| **不变式在应用层** | 业务规则散落在 Service 中 | 移到聚合根方法 |
| **不变式在数据库** | 仅靠数据库约束保证 | 在领域层显式校验 |
| **不变式缺失** | 聚合无校验逻辑 | 按模板补充不变式文档 |
| **过度校验** | 非关键路径也校验 | 区分 P0/P1/P2 级别 |
