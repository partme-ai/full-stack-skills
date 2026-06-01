# Example 12 — 微服务复杂多模块规模（Microservice Complex Multi-Module）

> 最复杂的场景：一个微服务包含多个限界上下文，每个上下文内部采用 Maven 多模块洋葱分层。适合大型企业级微服务，上下文紧密耦合无法拆分。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 10-25 人（一个大服务团队） |
| 限界上下文 | 3-5 个（同一服务内） |
| 部署单元 | 独立容器化部署 |
| Maven 模块 | 15-30 个 |
| 数据库 | 每个上下文独立 Database，且独立 Schema |
| 代码量 | 500+ 个类 |

## 目录树

```
fulfillment-service/
├── pom.xml                                    # 父 POM（聚合所有上下文）
│
├── shared/                                    # 共享内核（独立模块）
│   ├── pom.xml
│   └── src/main/java/.../
│       ├── domain/
│       │   ├── Money.java
│       │   ├── DomainEvent.java
│       │   └── Address.java
│       └── annotation/
│           └── ValueObject.java
│
├── order/                                     # 上下文 1: 订单
│   ├── pom.xml                                # 上下文父 POM
│   ├── order-domain/
│   │   ├── pom.xml
│   │   └── src/main/java/.../
│   │       ├── model/Order.java, OrderId.java, OrderStatus.java
│   │       ├── repository/OrderRepository.java
│   │       ├── service/PricingService.java
│   │       └── event/OrderPlacedEvent.java, OrderPaidEvent.java
│   ├── order-application/
│   │   ├── pom.xml
│   │   └── src/main/java/.../
│   │       ├── service/PlaceOrderUseCase.java, impl/PlaceOrderService.java
│   │       ├── command/PlaceOrderCommand.java
│   │       └── dto/OrderDTO.java
│   ├── order-infrastructure/
│   │   ├── pom.xml
│   │   └── src/main/java/.../
│   │       ├── data/entity/OrderPO.java
│   │       ├── data/repository/OrderRepositoryImpl.java
│   │       ├── data/mapper/OrderMapper.java
│   │       └── messaging/OrderEventPublisher.java
│   ├── order-api-rest/
│   │   ├── pom.xml
│   │   └── src/main/java/.../
│   │       ├── controller/OrderController.java
│   │       ├── dto/request/CreateOrderRequest.java
│   │       ├── dto/response/OrderResponse.java
│   │       └── assembler/OrderAssembler.java
│   └── order-composition/
│       ├── pom.xml
│       └── src/main/java/.../
│           └── config/OrderContextConfig.java
│
├── inventory/                                 # 上下文 2: 库存（同上结构）
│   ├── pom.xml
│   ├── inventory-domain/
│   ├── inventory-application/
│   ├── inventory-infrastructure/
│   ├── inventory-api-rest/
│   └── inventory-composition/
│
├── logistics/                                 # 上下文 3: 物流（同上结构）
│   ├── pom.xml
│   ├── logistics-domain/
│   ├── logistics-application/
│   ├── logistics-infrastructure/
│   ├── logistics-api-rest/
│   └── logistics-composition/
│
├── payment/                                   # 上下文 4: 支付（同上结构）
│   ├── pom.xml
│   ├── payment-domain/
│   ├── payment-application/
│   ├── payment-infrastructure/
│   ├── payment-api-rest/
│   └── payment-composition/
│
└── service-composition/                       # 服务级 DI 根
    ├── pom.xml                                # 依赖所有上下文
    └── src/main/java/.../
        ├── FulfillmentServiceApplication.java # Spring Boot 入口
        └── config/
            ├── AggregatedServiceConfig.java
            └── CrossContextSagaConfig.java
```

## 完整依赖图

```
┌──────────────────────────────────────────────────────────────────┐
│                    service-composition/                           │
│           FulfillmentServiceApplication + DI 根                   │
└──┬───────────┬────────────┬────────────┬─────────────┬───────────┘
   │           │            │            │             │
   ▼           ▼            ▼            ▼             ▼
┌──────┐  ┌──────┐    ┌──────┐    ┌──────┐      ┌──────────┐
│order │  │inven-│    │logis-│    │paym- │      │ service  │
│comp. │  │tory  │    │tics  │    │ent   │      │ shared   │
│      │  │comp. │    │comp. │    │comp. │      │  module  │
└──┬───┘  └──┬───┘    └──┬───┘    └──┬───┘      └────┬─────┘
   │         │            │           │               │
   │    ←── 每个上下文内部洋葱依赖 ──→ │               │
   │         │            │           │               │
   ▼         ▼            ▼           ▼               │
 ┌───────────────────────────────────┐                │
 │   各上下文 domain（零框架依赖）      │◄───────────────┘
 └───────────────────────────────────┘
```

**三层依赖隔离**：
1. **上下文内**：composition → api/infra → application → domain（经典洋葱）
2. **上下文间**：仅通过 Application Service + Domain Event（不直接引用对方 Domain）
3. **服务间**：通过 Kafka / REST / gRPC（API Gateway 统一对外）

## 上下文间协调示例

```java
// order-application/service/impl/PlaceOrderService.java
public class PlaceOrderService implements PlaceOrderUseCase {
    private final OrderRepository orderRepo;

    // 跨上下文仅通过 Application 接口协调
    private final ReserveInventoryUseCase inventory;    // 库存 Application 接口
    private final CreateShipmentUseCase logistics;       // 物流 Application 接口

    @Override
    @Transactional
    public OrderDTO execute(PlaceOrderCommand cmd) {
        // 1. 订单领域逻辑
        Order order = Order.create(...);
        orderRepo.save(order);

        // 2. 协调库存上下文（通过 Application Service，不跨 Domain）
        inventory.reserve(new ReserveCommand(order.getId(), cmd.getItems()));

        // 3. 协调物流上下文
        logistics.createShipment(new CreateShipmentCommand(order.getId()));

        return OrderAssembler.toDTO(order);
    }
}
```

## Maven 模块统计

| 上下文 | 模块数 | 说明 |
|--------|:-----:|------|
| shared | 1 | 共享模型 |
| order | 5 | domain/app/infra/api-rest/composition |
| inventory | 5 | 同上 |
| logistics | 5 | 同上 |
| payment | 5 | 同上 |
| service-composition | 1 | 汇总装配 |
| **总计** | **22** | modules |

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| 所有 domain 模块零 Spring 依赖 | ✅ | 22 个模块中的 4 个 domain 模块 |
| 上下文间间接协调 | ✅ | 仅通过 Application 接口 |
| 编译期分层强制 | ✅ | 逆向依赖 = 编译失败 |
| 服务内 Saga | ✅ | 跨上下文事务本地协调 |
| 测试隔离 | ✅ | 每个上下文独立测试套件 |

## 何时选择此结构

- **仅当**：业务逻辑 500+ 类，3+ 个紧密耦合的上下文，团队 > 10 人
- 企业级微服务，需要极强的代码组织和编译期约束
- 上下文紧密耦合但需要独立演进（不同团队负责不同上下文）

## 风险提示

- 22 个 Maven 模块 → 构建时间长，CI/CD 复杂度高
- 过度设计风险：大多数项目用 Example 09（简单微服务）或 Example 10（复杂微服务）即可
- 版本管理困难：一个 shared 模块变更需要 rebuild 所有上游
- 运维成本：模块边界需要持续 Code Review 维护
- **强烈建议**：先考虑拆分上下文为独立微服务（降低复杂度）
