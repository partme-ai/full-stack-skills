# Port Definitions — 端口定义规范

## 概述

端口（Port）是六边形架构的核心抽象。端口是定义在领域层（Domain）或应用层（Application）的接口（Interface），规定了业务核心与外部世界之间的通信契约。

## 端口类型

### 入站端口（Inbound / Driver Port）

入站端口定义"外部世界如何使用你的系统"。每个入站端口对应一个用例（UseCase）。

**命名规范**：`{Action}UseCase`

```java
// 入站端口 — 创建订单用例
public interface CreateOrderUseCase {
    OrderCreatedResult execute(CreateOrderCommand command);
}

// 入站端口 — 查询订单用例
public interface GetOrderUseCase {
    OrderDTO execute(GetOrderQuery query);
}

// 入站端口 — 支付订单用例
public interface PayOrderUseCase {
    PaymentResult execute(PayOrderCommand command);
}
```

### 出站端口（Outbound / Driven Port）

出站端口定义"你的系统如何使用外部世界"。每个出站端口对应一种外部依赖（数据库、消息队列、外部 API 等）。

**命名规范**：`{Resource}Repository` / `{Resource}Gateway` / `{Resource}Port`

```java
// 出站端口 — 订单仓储
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(Order order);
}

// 出站端口 — 支付网关
public interface PaymentGateway {
    PaymentResult charge(Money amount, PaymentMethod method);
    RefundResult refund(PaymentId paymentId, Money amount);
}

// 出站端口 — 通知服务
public interface NotificationPort {
    void sendEmail(Email to, EmailTemplate template);
    void sendSMS(PhoneNumber to, String message);
}

// 出站端口 — 事件发布
public interface EventPublisher {
    void publish(DomainEvent event);
    void publishAll(List<DomainEvent> events);
}
```

## 端口粒度原则

| 原则 | 说明 | 违反示例 |
|------|------|---------|
| **单一职责** | 一个端口只做一件事 | `OrderRepository` 同时包含订单和用户操作 |
| **用例粒度** | 入站端口按用例拆分 | `OrderUseCase` 包含 10+ 方法 → 拆分为 `CreateOrderUseCase`、`PayOrderUseCase` |
| **依赖粒度** | 出站端口按外部依赖拆分 | 一个端口包含 DB + MQ + 邮件 → 拆分为独立端口 |
| **不过度设计** | 不为"未来可能"提前抽象 | 日志、序列化库不需要端口抽象 |

## 端口位置

```
{project}-domain/
├── port/
│   ├── inbound/           # ★ 入站端口（UseCase 接口）
│   │   ├── CreateOrderUseCase.java
│   │   ├── PayOrderUseCase.java
│   │   └── QueryOrderUseCase.java
│   └── outbound/          # ★ 出站端口（Repository/External 接口）
│       ├── OrderRepository.java
│       ├── PaymentGateway.java
│       ├── NotificationPort.java
│       └── EventPublisher.java
```

## 端口设计检查清单

- [ ] 端口是否定义在 Domain 层（而非 Adapter 层）？
- [ ] 端口方法是否使用领域类型（而非技术类型如 `String`、`Map`）？
- [ ] 端口是否避免了 SQL/HTTP/MQ 相关的参数？
- [ ] 端口是否足够小（≤ 5 个方法）？
- [ ] 方法返回值是否为 `Optional` 而非 `null`？
- [ ] 入站端口是否以动词开头（`Create`、`Pay`、`Cancel`）？
- [ ] 出站端口是否以资源名词开头（`OrderRepository`、`PaymentGateway`）？

## Strong vs Weak Port

### Weak Port（技术泄漏）
```java
// ❌ 泄漏了 SQL 概念
public interface OrderRepository {
    List<Order> findByQuery(String sql, Map<String, Object> params);
}
```

### Strong Port（纯净抽象）
```java
// ✅ 纯领域概念
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    List<Order> findByCustomerId(CustomerId customerId, Page page);
    List<Order> findByStatus(OrderStatus status);
    void save(Order order);
}
```

## 目录放置约定

| 代码风格 | 端口位置 | 适配器位置 |
|---------|---------|-----------|
| DDD 风格 | `domain/port/inbound/`、`domain/port/outbound/` | `adapter/inbound/`、`adapter/outbound/` |
| 应用层风格 | `application/ports/driver/`、`application/ports/driven/` | `infrastructure/adapters/driver/`、`infrastructure/adapters/driven/` |
| 混合风格 | 聚合仓储在 `domain/{aggregate}/repository/`，应用端口在 `application/ports/` | `infrastructure/` 或 `adapter/` |

推荐 DDD 风格：将 all ports 定义在 `domain/port/` 下，保持领域层所有权清晰。
