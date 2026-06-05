# 值对象持久化策略

## 概述

值对象（Value Object）在 DDD 中是不变的对象集合，持久化方式直接影响领域模型的纯净度和数据库性能。本参考文档覆盖三种主流持久化策略及其选择决策树。

## 三种策略对比

| 策略 | 描述 | 适用场景 | 优势 | 劣势 |
|------|------|---------|------|------|
| **Inline（内嵌）** | VO 属性扁平化到实体表 | 单一值对象、属性少 | 查询高效、无 JOIN | 破坏 VO 概念完整性 |
| **JSON（序列化大对象）** | VO 序列化为 JSON 存入单列 | 多值集合、结构灵活 | 保持 VO 语义、简化表设计 | 不可索引查询、类型安全弱 |
| **Embeddable（可嵌入）** | ORM 原生嵌入支持 | ORM 框架（JPA/Hibernate） | 语义完整、ORM 原生 | 仅限 ORM 场景 |

## 决策树

```
VO 需要独立查询？
├── 是 → 考虑独立表（转为实体）或 JSON（有限查询）
│   ├── 需要 SQL JOIN 查询 → 转为实体 + 独立表
│   └── 仅按主实体查询 → JSON 序列化
└── 否 → 单一值还是集合？
    ├── 单一值 → Inline 内嵌
    │   ├── ORM 可用 → Embeddable（推荐）
    │   └── 无 ORM → 扁平化为字段
    └── 集合值 → JSON 序列化
        ├── 固定数量且 ≤ 3 → Inline 多列
        └── 可变数量 → JSON 大对象
```

## 详细策略

### 1. Inline 内嵌

VO 的所有属性作为实体表的独立列存储。

```java
// VO
public class Address {
    private final String street;
    private final String city;
    private final String zipCode;
    // constructor, getters, equals, hashCode
}

// 实体表列：street, city, zip_code
CREATE TABLE person (
    id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    street VARCHAR(200),
    city VARCHAR(100),
    zip_code VARCHAR(20)
);
```

**适用**：地址、货币金额（单字段）等单值 VO。

### 2. JSON 序列化

VO 序列化为 JSON 字符串存入单列。

```java
// VO 集合
public class OrderItem {
    private final ProductId productId;
    private final Money unitPrice;
    private final int quantity;
}

// 实体表列：items TEXT (JSON)
CREATE TABLE order_ (
    id BIGINT PRIMARY KEY,
    items TEXT
);
-- items: [{"productId":"P001","unitPrice":99.00,"quantity":2}, ...]
```

**适用**：订单明细、通讯地址列表等可变数量 VO 集合。

### 3. Embeddable（JPA 示例）

```java
@Embeddable
public class Address {
    private String street;
    private String city;
    private String zipCode;
}

@Entity
public class Person {
    @Id
    private Long id;
    private String name;
    @Embedded
    private Address address;
}
```

**适用**：JPA/Hibernate 项目，ORM 原生支持，保持 VO 概念完整。

## 常见问题

**Q: VO 持久化后可以修改吗？**
A: 不可。VO 在设计上不可变，持久化更新应整体替换而非修改字段。

**Q: 多个实体引用同一个 VO 如何存储？**
A: 每个实体各自存储自己的 VO 副本（值语义，非共享引用）。

**Q: JSON 策略如何保证类型安全？**
A: 使用强类型序列化库（Jackson/FastJSON 配置）结合 DTO 校验。
