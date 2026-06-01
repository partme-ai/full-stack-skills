# Example 07 — 单体复杂规模（Monolith Complex）

> 单模块多限界上下文。通过顶层包名（订单/商品/用户）划分上下文，每个上下文内部独立应用洋葱分层。适合 3-8 人团队、多个限界上下文但部署为单体。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 3-8 人 |
| 限界上下文 | 3-5 个（订单、商品、用户、库存、支付） |
| 部署单元 | 1 个 JAR/WAR |
| 数据库 | 1 个 RDBMS（多 Schema） |
| 外部集成 | 5-10 个 |

## 目录树

```
ecommerce-platform/
├── pom.xml
├── src/main/java/com/example/ec/
│   ├── shared/                                 # 共享内核
│   │   ├── domain/
│   │   │   └── model/
│   │   │       ├── Money.java                  # 共享值对象
│   │   │       └── DomainEvent.java            # 基础事件接口
│   │   └── infrastructure/
│   │       └── messaging/
│   │           └── EventPublisher.java
│   │
│   ├── order/                                  # 订单上下文
│   │   ├── core/domain/
│   │   │   ├── model/
│   │   │   │   ├── Order.java                  # 聚合根
│   │   │   │   ├── OrderItem.java
│   │   │   │   └── OrderStatus.java
│   │   │   ├── service/
│   │   │   │   └── PricingService.java
│   │   │   ├── repository/
│   │   │   │   └── OrderRepository.java
│   │   │   └── event/
│   │   │       └── OrderPlacedEvent.java       # 集成事件（通知其他上下文）
│   │   ├── core/application/
│   │   │   └── service/
│   │   │       ├── PlaceOrderUseCase.java
│   │   │       └── impl/PlaceOrderService.java
│   │   ├── infrastructure/data/
│   │   │   ├── entity/OrderPO.java
│   │   │   ├── repository/OrderRepositoryImpl.java
│   │   │   └── mapper/OrderMapper.java
│   │   ├── api/controller/OrderController.java
│   │   └── composition/config/OrderBoundedContextConfig.java
│   │
│   ├── product/                                # 商品上下文
│   │   ├── core/domain/
│   │   │   ├── model/
│   │   │   │   ├── Product.java
│   │   │   │   ├── ProductId.java
│   │   │   │   └── Category.java
│   │   │   ├── repository/
│   │   │   │   └── ProductRepository.java
│   │   │   └── event/
│   │   │       └── ProductCreatedEvent.java
│   │   ├── core/application/
│   │   │   └── service/
│   │   │       └── impl/ProductManagementService.java
│   │   ├── infrastructure/data/...
│   │   ├── api/controller/ProductController.java
│   │   └── composition/config/ProductBoundedContextConfig.java
│   │
│   ├── user/                                   # 用户上下文
│   │   ├── core/domain/
│   │   │   ├── model/
│   │   │   │   ├── User.java
│   │   │   │   ├── Email.java
│   │   │   │   └── Address.java
│   │   │   ├── repository/
│   │   │   │   └── UserRepository.java
│   │   │   └── event/
│   │   │       └── UserRegisteredEvent.java
│   │   ├── core/application/...
│   │   ├── infrastructure/data/...
│   │   ├── api/controller/UserController.java
│   │   └── composition/config/UserBoundedContextConfig.java
│   │
│   ├── inventory/                              # 库存上下文
│   │   ├── core/domain/...
│   │   ├── core/application/...
│   │   ├── infrastructure/...
│   │   └── api/...
│   │
│   └── payment/                                # 支付上下文
│       ├── core/domain/...
│       ├── core/application/...
│       ├── infrastructure/...
│       └── api/...
│
└── composition/
    └── config/
        └── AppConfig.java                      # 汇总装配所有上下文
```

## 上下文间依赖方向

```
  ┌─────────┐      ★ 跨上下文仅通过 ID 引用和事件通信
  │  order  │────→ 引用 ProductId, UserId
  └────┬────┘
       │
  ┌────▼────┐
  │ payment │──→ 引用 OrderId
  └────┬────┘
       │
  ┌────▼─────────┐
  │  inventory    │──→ 引用 ProductId, OrderId
  └───────────────┘

  ┌──────┐
  │ user │  ← 被引用，不依赖其他上下文
  └──────┘

  ┌─────────┐
  │ product │  ← 被引用，不依赖其他上下文
  └─────────┘
```

**规则**：
- 上下文间仅通过 ID 值对象引用（如 `ProductId` 放在 `shared/domain`）
- 跨上下文事务通过领域事件 + 最终一致性
- 每个上下文独立配置自己的 DI（避免循环依赖）

## 上下文内依赖方向（每个上下文独立）

```
每个上下文内部：
  composition → api / infrastructure → application → domain ★
```

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| 上下文隔离 | ✅ | 每个上下文独立 domain/application/infra/api |
| 跨上下文仅 ID 引用 | ✅ | order 只引用 ProductId，不引用 Product 实体 |
| shared 内核最小化 | ✅ | 仅 Money, DomainEvent，无业务逻辑 |
| 共享事件放 shared | ⚠️ | 集成事件建议各上下文独立定义 |
| 测试隔离 | ✅ | 每个上下文独立测试 |

## 何时选择此结构

- 业务复杂度高但运维资源有限（只有 1 个部署单元）
- 多个限界上下文需要隔离，但微服务运维成本过高
- 单体内部先做模块化，为未来微服务拆分打基础
- 团队已按上下文分工（order 小团队、product 小团队等）

## 风险提示

- 共享内核容易膨胀：`shared/` 中的公共代码需严格审查
- 上下文边界可能被打破：需要 Code Review 防止直接引用对方领域对象
- 数据库耦合：单 Schema 下容易写跨上下文 JOIN，建议多 Schema
