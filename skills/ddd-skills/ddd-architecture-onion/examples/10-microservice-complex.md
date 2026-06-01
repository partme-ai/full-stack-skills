# Example 10 — 微服务复杂规模（Microservice Complex）

> 一个微服务内部包含多个限界上下文，每个上下文在服务内独立应用洋葱分层。适合业务关联紧密无法拆分的场景。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 6-12 人（一个服务团队） |
| 限界上下文 | 2-4 个（同一服务内） |
| 部署单元 | 独立容器化部署 |
| 数据库 | 每个上下文独立 Schema 或 Table Prefix |
| 通信方式 | 内部直接方法调用，外部 REST/gRPC + Kafka |

## 目录树

```
fulfillment-service/                           # 履约微服务（含订单、库存、物流）
├── pom.xml
├── Dockerfile
├── src/main/java/com/example/fulfillment/
│   ├── shared/                                # 共享内核（同服务内）
│   │   └── domain/
│   │       ├── Money.java
│   │       ├── DomainEvent.java
│   │       └── Address.java
│   │
│   ├── order/                                 # 上下文 1: 订单
│   │   ├── core/
│   │   │   ├── domain/
│   │   │   │   ├── model/
│   │   │   │   │   ├── Order.java
│   │   │   │   │   ├── OrderId.java
│   │   │   │   │   └── OrderStatus.java
│   │   │   │   ├── repository/
│   │   │   │   │   └── OrderRepository.java
│   │   │   │   └── event/
│   │   │   │       └── OrderPaidEvent.java
│   │   │   └── application/
│   │   │       └── service/
│   │   │           ├── PlaceOrderUseCase.java
│   │   │           └── impl/PlaceOrderService.java
│   │   ├── infrastructure/data/
│   │   │   ├── entity/OrderPO.java
│   │   │   └── repository/OrderRepositoryImpl.java
│   │   ├── api/controller/OrderController.java
│   │   └── composition/config/OrderContextConfig.java
│   │
│   ├── inventory/                             # 上下文 2: 库存
│   │   ├── core/
│   │   │   ├── domain/
│   │   │   │   ├── model/
│   │   │   │   │   ├── Inventory.java
│   │   │   │   │   └── StockLevel.java
│   │   │   │   ├── repository/
│   │   │   │   │   └── InventoryRepository.java
│   │   │   │   └── event/
│   │   │   │       └── StockReservedEvent.java
│   │   │   └── application/
│   │   │       └── service/
│   │   │           └── impl/ReserveStockService.java
│   │   ├── infrastructure/data/
│   │   │   └── repository/InventoryRepositoryImpl.java
│   │   ├── api/controller/InventoryController.java
│   │   └── composition/config/InventoryContextConfig.java
│   │
│   └── logistics/                             # 上下文 3: 物流
│       ├── core/
│       │   ├── domain/
│       │   │   ├── model/
│       │   │   │   ├── Shipment.java
│       │   │   │   └── TrackingNumber.java
│       │   │   ├── repository/
│       │   │   │   └── ShipmentRepository.java
│       │   │   └── event/
│       │   │       └── ShipmentCreatedEvent.java
│       │   └── application/
│       │       └── service/
│       │           └── impl/CreateShipmentService.java
│       ├── infrastructure/data/
│       │   └── repository/ShipmentRepositoryImpl.java
│       ├── api/controller/LogisticsController.java
│       └── composition/config/LogisticsContextConfig.java
│
├── composition/
│   ├── FulfillmentServiceApplication.java     # 服务入口
│   └── config/
│       └── ServiceContextConfig.java           # 汇总所有上下文
│
└── src/test/
    └── java/com/example/fulfillment/
        ├── order/core/domain/model/OrderTest.java
        ├── inventory/core/domain/model/InventoryTest.java
        ├── logistics/core/domain/model/ShipmentTest.java
        └── integration/
            ├── OrderIntegrationIT.java
            └── FulfillmentSagaIT.java          # 跨上下文 Saga 集成测试
```

## 服务内上下文依赖方向

```
┌──────────────────────────────────────────────┐
│             composition/                      │ ← 汇总装配
└─────┬─────────┬──────────┬───────────────────┘
      │         │          │
  ┌───▼───┐ ┌───▼────┐ ┌──▼──────┐
  │ order │ │inventory│ │logistics│
  │ ctx   │ │  ctx    │ │ ctx     │
  └───┬───┘ └───┬────┘ └──┬──────┘
      │         │          │
      │    同步调用          │
      └────────┼───────────┘
               │
      通过 Application Service 协调
      （不可直接调用对方 Domain）
```

**规则**：
- 同一服务内的上下文通过 Application Service 协调（同步）
- 对外提供统一的 API 入口
- 每个上下文独立 Database Schema
- 跨上下文事务用 Saga（比纯微服务更简单，可本地加锁）

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| 上下文内部洋葱合规 | ✅ | 每个 ctx 独立 domain/app/infra |
| 上下文间仅通过 AppService 协调 | ✅ | 不跨上下文直接访问 Domain |
| 共享内核最小 | ✅ | shared 仅 Money/Address |
| DB 按上下文隔离 | ✅ | Schema per context |

## 何时选择此结构

- 多个业务模块关联紧密（如订单-库存-履约不可拆分）
- 需要独立部署但拆分为多个微服务会引入过多网络开销
- 过渡期架构：先做内部分层，后续再拆分为独立微服务

## 风险提示

- 服务内上下文边界容易模糊（比跨服务更难约束）
- 共享数据库可能产生隐式耦合
- 服务过大可能成为新单体
