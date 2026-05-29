# Aggregate Deep Dive — 聚合设计深度指南

## 聚合设计 6 原则详解

### 原则 1：在一致性边界内建模真正的不变条件

**不变量 = 无论发生什么操作都必须保持的业务规则**

```
示例：Order 聚合的不变量
├── 订单总金额 = 所有 OrderItem.subtotal 之和
├── PAID 状态的订单不能修改商品
├── CANCELLED 状态的订单不能再支付
└── 同一订单中不能有重复的 SKU
```

**方法**: 在聚合根的方法中检查不变量，失败抛异常。

```java
public void pay() {
    if (this.status != OrderStatus.DRAFT) {
        throw new OrderException("Only DRAFT orders can be paid");
    }
    this.status = OrderStatus.PAID;
}
```

### 原则 2：设计小聚合

```
聚合大小 = 直接影响并发性能

过大的后果：
├── 事务锁范围大 → 并发冲突增加
├── 加载全部关联数据 → N+1 查询
├── 修改频率不一致的数据耦合 → 无意义锁等待
└── 重构困难 → 牵一发动全身
```

**拆分决策流程**:

```
当前聚合是否过大？
├── 两个实体是否总是同时修改？
│   ├── 是 → 保留在同一聚合
│   └── 否 → 考虑拆分
├── 聚合内有实体可以独立存在吗？
│   ├── 是 → 拆分为独立聚合
│   └── 否 → 保持
└── 聚合内实体数 > 5？
    ├── 是 → 强烈建议拆
    └── 否 → 保持
```

### 原则 3：通过唯一标识引用其他聚合

```java
// ✅ 正确：ID 引用
public class Order {
    private BuyerId buyerId;       // VO，包装 Member BC 的 ID
    private List<OrderItem> items;
}

// ❌ 错误：对象引用
public class Order {
    private Member buyer;          // 直接引用了外部聚合
}
```

### 原则 4：在边界之外使用最终一致性

| 场景 | 方案 |
|------|------|
| 订单支付成功 → 扣减库存 | 领域事件：OrderPaid → InventoryDeducted |
| 订单取消 → 释放库存 | 领域事件：OrderCancelled → InventoryReleased |
| 订单签收 → 发放积分 | 领域事件：OrderDelivered → PointsAwarded |

### 原则 5：通过应用层实现跨聚合服务调用

```
聚合 A ──事件──→ 聚合 B        ✅ 领域事件解耦
应用服务协调聚合 A + 聚合 B    ✅ 编排层
聚合 A 直接调聚合 B 的领域服务  ❌ 跨聚合耦合
```

### 原则 6：适合自己才是最好的

可突破场景：
- 高性能要求 → 可适当放宽一致性约束
- 团队能力限制 → 可先采用简单设计再演进
- 全局事务需求 → 可评估 Saga 或 TCC 方案

## 聚合根选择指南

```
候选实体评估：

1. 是否有独立的生命周期？
   例：Order 有 DRAFT→PAID→SHIPPED→DELIVERED 完整生命周期

2. 是否有全局唯一标识？
   例：Order 有 orderId，全局唯一

3. 是否负责创建或修改其他实体？
   例：Order 管理 OrderItem 的添加和移除

4. 是否有专门的模块或团队管理？
   例：有专门的订单模块/订单团队

满足 ≥ 2 个条件 → 适合作为聚合根
```

## 大聚合拆分案例

### 拆分前（问题聚合）

```
电商核心聚合（过大）：
├── Product (聚合根)
│   ├── SKU (Entity)
│   ├── Category (Entity)
│   ├── Inventory (Entity)
│   ├── Price (Entity)
│   └── Review (Entity)    ← 可以和 Product 分开
```

### 拆分后

```
Product 聚合：
├── Product (聚合根)
├── SKU (Entity)
└── Price (Value Object)

Inventory 聚合：
├── Inventory (聚合根)
└── WarehouseLocation (Value Object)

Review 聚合：
├── Review (聚合根)
└── Rating (Value Object)

关联方式：
Product.id → Inventory.productId (ID 引用)
Product.id → Review.productId (ID 引用)
```
