# DDD 反模式速查 — 含修复路径


## P0 反模式（必须修复）

### 贫血模型
```java
// ❌ 反模式
@Entity public class Order { private Long id; private String status; /* only getter/setter */ }
@Service public class OrderService { public void pay(Long id) { /* all logic here */ } }

// ✅ 修复
@Entity public class Order {
    private OrderStatus status;
    public void pay() { if (!status.canPay()) throw new OrderException(...); this.status = OrderStatus.PAID; }
}
```

### 领域层框架依赖
```java
// ❌ Domain 层 import org.springframework.stereotype.Service
// ✅ Domain 层只用 Java 标准库
```

### 跨聚合直接引用
```java
// ❌ class Order { Customer customer; }
// ✅ class Order { CustomerId customerId; }
```

### 循环依赖
```java
// ❌ Module A → Module B → Module A
// ✅ 依赖方向: Interface → App → Domain ← Infrastructure
```

## P1 反模式（应该修复）

### Repository 返回 DTO
```java
// ❌ public OrderDTO findById(Long id);  // Repository 返回 DTO
// ✅ public Optional<Order> findById(OrderId id);  // 返回聚合根
```

### Controller 业务逻辑
```java
// ❌ Controller 中有 if/else 业务判断
// ✅ Controller 只做协议转换，业务在 Domain + Application
```

### Application Service 中有 SQL
```java
// ❌ AppService 中调用 jdbcTemplate.query()
// ✅ SQL 操作在 Infrastructure Repository
```

## 修复顺序建议

```
Phase 1: 修复 P0（阻止合并）
  1. 领域层去框架化
  2. 切断循环依赖
  3. 修复跨聚合引用

Phase 2: 修复 P1（下个版本前）
  4. Repository 返回聚合根
  5. Controller 去业务化
  6. App 层去 SQL

Phase 3: 优化 P2（持续改进）
  7. 聚合瘦身
  8. 补充领域事件
  9. 值对象替换原始类型
```

