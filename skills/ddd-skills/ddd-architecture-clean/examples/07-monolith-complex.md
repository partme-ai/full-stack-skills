# 07 — 单体 Clean 架构（复杂版）

> 多聚合根 + 多 Interactor，单模块内按领域划分子包，每个领域独立四层。

## 目录树

```
order-service/
├── src/main/java/com/example/
│   └── order/
│       ├── shared/                          # 共享内核
│       │   ├── domain/
│       │   │   ├── Identifier.java          # 通用 ID 基类
│       │   │   ├── Money.java
│       │   │   └── DomainEvent.java
│       │   └── event/
│       │       └── EventPublisher.java      # 事件发布端口
│       │
│       ├── order/                           # 订单领域
│       │   ├── enterprise/
│       │   │   ├── entity/
│       │   │   │   ├── Order.java           # 聚合根
│       │   │   │   └── OrderItem.java
│       │   │   ├── vo/
│       │   │   │   ├── OrderId.java
│       │   │   │   └── OrderStatus.java
│       │   │   └── event/
│       │   │       ├── OrderCreatedEvent.java
│       │   │       └── OrderPaidEvent.java
│       │   ├── usecase/
│       │   │   ├── port/input/
│       │   │   │   ├── CreateOrderUseCase.java
│       │   │   │   ├── PayOrderUseCase.java
│       │   │   │   └── QueryOrderUseCase.java
│       │   │   ├── port/output/
│       │   │   │   └── OrderRepository.java
│       │   │   ├── dto/
│       │   │   │   ├── CreateOrderRequest.java
│       │   │   │   ├── CreateOrderResponse.java
│       │   │   │   └── OrderDTO.java
│       │   │   └── interactor/
│       │   │       ├── CreateOrderInteractor.java
│       │   │       ├── PayOrderInteractor.java
│       │   │       └── QueryOrderInteractor.java
│       │   ├── adapter/
│       │   │   ├── controller/
│       │   │   │   └── OrderController.java
│       │   │   ├── repository/
│       │   │   │   ├── OrderJpaEntity.java
│       │   │   │   ├── OrderItemJpaEntity.java
│       │   │   │   └── OrderRepositoryImpl.java
│       │   │   └── presenter/
│       │   │       └── OrderPresenter.java
│       │   └── framework/
│       │       └── config/
│       │           └── OrderDomainConfig.java
│       │
│       ├── payment/                         # 支付领域
│       │   ├── enterprise/
│       │   │   ├── entity/
│       │   │   │   └── Payment.java         # 聚合根
│       │   │   ├── vo/
│       │   │   │   ├── PaymentId.java
│       │   │   │   └── PaymentStatus.java
│       │   │   └── event/
│       │   │       └── PaymentCompletedEvent.java
│       │   ├── usecase/
│       │   │   ├── port/input/
│       │   │   │   └── ProcessPaymentUseCase.java
│       │   │   ├── port/output/
│       │   │   │   ├── PaymentRepository.java
│       │   │   │   └── PaymentGateway.java
│       │   │   ├── dto/
│       │   │   │   └── PaymentRequest.java
│       │   │   └── interactor/
│       │   │       └── ProcessPaymentInteractor.java
│       │   ├── adapter/
│       │   │   ├── controller/
│       │   │   │   └── PaymentController.java
│       │   │   ├── repository/
│       │   │   │   └── PaymentRepositoryImpl.java
│       │   │   └── gateway/
│       │   │       └── AlipayGatewayImpl.java
│       │   └── framework/
│       │       └── config/
│       │           └── PaymentDomainConfig.java
│       │
│       └── inventory/                       # 库存领域
│           ├── enterprise/
│           │   ├── entity/
│           │   │   └── Inventory.java
│           │   └── vo/
│           │       ├── SkuId.java
│           │       └── Quantity.java
│           ├── usecase/
│           │   ├── port/input/
│           │   │   ├── ReserveInventoryUseCase.java
│           │   │   └── ReleaseInventoryUseCase.java
│           │   ├── port/output/
│           │   │   └── InventoryRepository.java
│           │   └── interactor/
│           │       ├── ReserveInventoryInteractor.java
│           │       └── ReleaseInventoryInteractor.java
│           ├── adapter/
│           │   └── repository/
│           │       └── InventoryRepositoryImpl.java
│           └── framework/
│               └── config/
│                   └── InventoryDomainConfig.java
│
├── src/test/java/com/example/order/
│   ├── order/enterprise/entity/OrderTest.java
│   ├── order/usecase/interactor/
│   │   ├── CreateOrderInteractorTest.java
│   │   └── PayOrderInteractorTest.java
│   ├── payment/usecase/interactor/
│   │   └── ProcessPaymentInteractorTest.java
│   ├── architecture/
│   │   └── ArchitectureTest.java
│   └── integration/
│       └── OrderPaymentIntegrationTest.java
│
└── pom.xml
```

## 领域间交互规则

```
┌──────────────────────────────────────────────────────┐
│                   shared 共享内核                      │
│  DomainEvent, Money, Identifier                      │
└──┬─────────────────┬──────────────────┬──────────────┘
   │                 │                  │
   ▼                 ▼                  ▼
┌──────────┐   ┌──────────┐   ┌──────────────┐
│  order   │   │ payment  │   │  inventory   │
│ 领域     │◄──│ 领域     │──►│  领域         │
│          │   │          │   │              │
└──────────┘   └──────────┘   └──────────────┘
    │               │                │
    └─────── 通过事件异步通信 ────────┘
```

- **领域间不得直接依赖**：order 不能 import payment 的类
- **共享内核**：shared 包放跨领域共用类型（Money、DomainEvent）
- **领域通信**：通过领域事件异步解耦（OrderCreated → ReserveInventory）
- **UseCase 编排跨领域**：上级编排 Interactor 可依赖多个领域的 output port

## 依赖方向（领域内 + 领域间）

```
framework ──► adapter ──► usecase ──► enterprise
   │              │            │
   └── 仅依赖适配层 ─┴── 仅依赖端口 ─┘

领域间：
order ──► shared ◄── payment ──► shared ◄── inventory
   └── 不得互相 import ──────────┘
```

## ArchUnit 验证（领域隔离）

```java
@ArchTest
static final ArchRule no_domain_dependency = classes()
    .that().resideInAPackage("..order..")
    .should().onlyDependOnClassesThat()
    .resideInAnyPackage(
        "..order..",          // 同领域
        "..shared..",         // 共享内核
        "java.."
    );

@ArchTest
static final ArchRule order_not_depend_payment = noClasses()
    .that().resideInAPackage("..order..")
    .should().dependOnClassesThat()
    .resideInAPackage("..payment..");
```

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 8-20 人，多团队协作 |
| 项目复杂度 | 3-8 个聚合根，20-60 个 UseCase |
| 领域数 | 3-6 个核心领域 |
| 部署方式 | 单体部署 |
| 演进方向 | 复杂版 → 多模块版（08）→ 领域拆分微服务 |
| 典型业务 | 中型电商平台（订单+支付+库存+物流）、SaaS 后台 |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| 领域隔离清晰，适合多人并行开发 | 编译期无法防止领域间直接依赖 |
| 事件驱动解耦，领域独立性强 | shared 包膨胀风险（垃圾场效应） |
| 为微服务拆分做好领域边界准备 | 共享内核变更影响所有领域 |
| 单一构建，CI 简单 | 领域边界依赖 ArchUnit 人工维护 |
