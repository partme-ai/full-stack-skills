# Entity & Value Object — 实体与值对象

## 对比速查

| 维度 | 实体 (Entity) | 值对象 (Value Object) |
|------|-------------|---------------------|
| **标识** | 有唯一 ID | 无 ID |
| **相等性** | 通过 ID 判断 | 通过所有属性值判断 |
| **可变性** | 可变 | **不可变** |
| **生命周期** | 独立生命周期 | 无独立生命周期，用完即扔 |
| **持久化** | 通常持久化 | 嵌入实体或序列化 |
| **行为** | 丰富的业务行为 | 数据初始化 + 整体替换 |
| **关系** | 引用其他实体和值对象 | 尽量只引用值对象 |

## 实体

### 四种形态

| 形态 | 说明 | 示例 |
|------|------|------|
| **业务形态** | 事件风暴中的领域对象 | Order, Customer |
| **代码形态** | 实体类（充血模型） | `class Order { void pay() {} }` |
| **运行形态** | DO（领域对象），有唯一 ID | `Order(id=123, status=PAID)` |
| **数据库形态** | 1 个实体 → 0/1/多个持久化对象 | Order → orders 表 + order_items 表 |

### 代码模板

```java
// 充血模型：行为在实体内部
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private OrderStatus status;
    private Money totalAmount;

    public void pay() {
        if (!status.canPay()) {
            throw new OrderException("Cannot pay order in " + status);
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}
```

### 实体与持久化对象的映射

| 场景 | 映射关系 | 说明 |
|------|----------|------|
| 常规 | 1:1 | 一个实体对应一张表 |
| 纯内存实体 | 1:0 | 如折扣实体，基于多个价格配置计算生成 |
| 复合实体 | 1:N | 如权限实体 = user 表 + role 表 |
| 宽表实体 | N:1 | 如 Customer + Account 共享一张宽表 |

## 值对象

### 设计原则

```
值对象 = 无 ID + 不可变 + 概念完整的属性集合

设计检查：
1. 这个对象是否由属性定义（而非身份）？
2. 修改这个对象的属性是否意味着它是一个不同的东西？
3. 两个实例所有属性相同，是否应该被视为相等？

全部 YES → Value Object
```

### 代码示例

```java
// ✅ 不可变值对象
public record Money(BigDecimal amount, Currency currency) {
    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Currency mismatch");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }
}

// ✅ 不可变值对象
public record Address(String province, String city, String district, String street) {
    // 无 setter，无 ID
}
```

### 两种代码形态

| 形态 | 适用场景 | 示例 |
|------|----------|------|
| **单一属性** | 简单值 | `String name` |
| **属性集合 (Class)** | 多个相关属性 | `Address address` |

### 两种持久化方式

| 方式 | 做法 | 优点 | 缺点 |
|------|------|------|------|
| **属性嵌入** | 值对象字段直接作为实体表列 | 查询方便 | 实体表列数增多 |
| **序列化大对象** | 值对象序列化为 JSON 存入一个字段 | 表结构简化 | 无法查询值对象内部字段 |

### 示例对比

```sql
-- 方式 1: 属性嵌入
CREATE TABLE person (
    id       BIGINT PRIMARY KEY,
    name     VARCHAR(50),
    province VARCHAR(20),  -- address.province
    city     VARCHAR(20),  -- address.city
    district VARCHAR(20),  -- address.district
    street   VARCHAR(100)  -- address.street
);

-- 方式 2: 序列化大对象
CREATE TABLE person (
    id      BIGINT PRIMARY KEY,
    name    VARCHAR(50),
    address JSON  -- {"province":"...","city":"...","district":"...","street":"..."}
);
```

## 实体 vs 值对象 — 决策流程

```
这是一个领域对象。问：

1. 它需要唯一标识，且标识在其生命周期内保持不变吗？
   ├── YES → 2. 它的状态会随时间改变吗？
   │         ├── YES → Entity
   │         └── NO  → 3. 它是否描述了另一个对象？
   │                   ├── YES → Value Object
   │                   └── NO  → Entity（不可变实体）
   └── NO  → Value Object

快速判断：
  "这是 THE 同一个东西吗？" → Entity（身份比较）
  "这和那个有相同的值吗？" → Value Object（结构相等）
```

## 领域建模 vs 数据建模

```
传统方式（数据建模优先）：
  设计表 → 设计实体 → 每个表一个实体 → 主表关联从表 → 表爆炸

DDD 方式（领域建模优先）：
  领域建模 → 识别 Entity 和 VO → VO 嵌入实体 → 减少表数量 → 简化数据库
```

| 对比维度 | 数据建模优先 | 领域建模优先 (DDD) |
|----------|-------------|-------------------|
| 起点 | 数据库表 | 业务领域 |
| 实体粒度 | 每表一实体 | 按业务聚合 |
| 表数量 | 多（范式化） | 少（VO 嵌入） |
| 业务表达 | 被数据模型限制 | 领域模型主导 |

## 常见错误

| 错误 | 纠正 |
|------|------|
| 值对象加了 ID 和 setter | 值对象 = 无 ID + 不可变 |
| 把 Address、Money 设计成 Entity | 属性相同即相等 → VO |
| 值对象嵌套值对象有 setter | 整体替换，不要局部修改 |
| Entity 只有 getter/setter | 充血模型：行为在 Entity 内部 |
| 实体 ID 用数据库自增 | 使用 UUID 或业务编号 |
