# Example: 单体复杂六边形架构

多端口 + 多适配器 + 多聚合根的单体应用，适用于中大型单体系统的内部模块化。

## 场景

10-20 人团队、多入口（REST + gRPC + CLI）、多外部依赖（Postgres + Redis + RabbitMQ + Stripe），领域包含多个聚合根和跨聚合的领域服务。

## 目录树 & 包结构

```
order-management/
└── src/main/java/com/example/ordermgmt/
    ├── OrderMgmtApplication.java
    │
    ├── domain/                                          # 领域核心
    │   ├── model/
    │   │   ├── order/                                   # 聚合 1
    │   │   │   ├── Order.java                           # 聚合根
    │   │   │   ├── OrderId.java                         # 值对象
    │   │   │   ├── OrderItem.java                       # 实体
    │   │   │   ├── OrderStatus.java                     # 枚举
    │   │   │   └── OrderPaidEvent.java                  # 领域事件
    │   │   ├── payment/                                 # 聚合 2
    │   │   │   ├── Payment.java                         # 聚合根
    │   │   │   ├── PaymentId.java                       # 值对象
    │   │   │   ├── PaymentMethod.java                   # 值对象
    │   │   │   └── PaymentCompletedEvent.java           # 领域事件
    │   │   ├── inventory/                               # 聚合 3
    │   │   │   ├── Inventory.java                       # 聚合根
    │   │   │   ├── StockId.java                         # 值对象
    │   │   │   └── StockReservedEvent.java              # 领域事件
    │   │   └── shared/                                  # 共享值对象
    │   │       ├── Money.java
    │   │       ├── CustomerId.java
    │   │       └── Address.java
    │   ├── service/                                     # 领域服务（跨聚合）
    │   │   ├── OrderPaymentSaga.java                    # 订单-支付协调
    │   │   └── InventoryReservationService.java         # 库存预留
    │   ├── port/
    │   │   ├── inbound/                                 # 入站端口
    │   │   │   ├── CreateOrderUseCase.java
    │   │   │   ├── PayOrderUseCase.java
    │   │   │   ├── QueryOrderUseCase.java
    │   │   │   ├── InventoryQueryUseCase.java
    │   │   │   └── GenerateReportUseCase.java
    │   │   └── outbound/                                # 出站端口
    │   │       ├── OrderRepository.java                 # 聚合 1 持久化
    │   │       ├── PaymentRepository.java               # 聚合 2 持久化
    │   │       ├── InventoryRepository.java             # 聚合 3 持久化
    │   │       ├── PaymentGateway.java                  # 外部支付
    │   │       ├── EventPublisher.java                  # 消息发布
    │   │       ├── CacheService.java                    # 缓存抽象
    │   │       └── NotificationService.java             # 通知抽象
    │   └── specification/
    │       ├── OrderSpecification.java                  # 规格模式
    │       └── PaymentSpecification.java
    │
    ├── application/                                     # 应用层
    │   ├── service/
    │   │   ├── CreateOrderServiceImpl.java
    │   │   ├── PayOrderServiceImpl.java
    │   │   ├── InventoryQueryServiceImpl.java
    │   │   └── ReportGenerationServiceImpl.java
    │   └── dto/
    │       ├── OrderDTO.java
    │       └── PaymentDTO.java
    │
    ├── adapter/                                         # 适配器层
    │   ├── inbound/
    │   │   ├── rest/
    │   │   │   ├── OrderController.java                 # REST 入口
    │   │   │   ├── PaymentController.java
    │   │   │   └── ReportController.java
    │   │   ├── grpc/
    │   │   │   ├── OrderGrpcService.java                # gRPC 入口
    │   │   │   └── PaymentGrpcService.java
    │   │   └── cli/
    │   │       └── ReportCliCommand.java                # CLI 入口
    │   └── outbound/
    │       ├── persistence/
    │       │   ├── PostgresOrderRepository.java
    │       │   ├── PostgresPaymentRepository.java
    │       │   ├── PostgresInventoryRepository.java
    │       │   └── mapper/
    │       │       ├── OrderMapper.java
    │       │       ├── PaymentMapper.java
    │       │       └── InventoryMapper.java
    │       ├── external/
    │       │   ├── StripePaymentGateway.java            # implements PaymentGateway
    │       │   └── TwilioNotificationService.java       # implements NotificationService
    │       ├── messaging/
    │       │   └── RabbitMQEventPublisher.java          # implements EventPublisher
    │       └── cache/
    │           └── RedisCacheService.java               # implements CacheService
    │
    └── configuration/                                   # 配置层
        ├── AdapterConfig.java                           # 次适配器装配
        ├── UseCaseConfig.java                           # 应用服务装配
        └── CacheConfig.java                             # 缓存配置
```

## 依赖关系

```
adapter/inbound (REST/gRPC/CLI)
    │ 依赖 UseCase 接口
    ▼
application/service (UseCase 实现)
    │ 依赖出站端口接口
    ▼
domain/port/outbound (接口)
    │ 实现
    ▼
adapter/outbound/persistence+external+messaging+cache (适配器实现)
```

```
┌─────────────────────────────────────────────────────────────┐
│  adapter/inbound/                                           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐ │
│  │ REST (Order) │ │ gRPC (Order) │ │ CLI (Report)         │ │
│  └──────┬───────┘ └──────┬───────┘ └──────────┬───────────┘ │
│         │                │                     │             │
│  domain/port/inbound/    │                     │             │
│  ┌──────────────┐ ┌──────┴───────┐ ┌──────────┴───────────┐ │
│  │ CreateOrder  │ │ PayOrder     │ │ GenerateReport       │ │
│  │ UseCase      │ │ UseCase      │ │ UseCase              │ │
│  └──────┬───────┘ └──────┬───────┘ └──────────┬───────────┘ │
│         │                │                     │             │
│  domain/model/        domain/service/                      │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌───────────────────┐ │
│  │ Order   │ │ Payment │ │ Saga     │ │ InventoryReserve  │ │
│  │ (AR)    │ │ (AR)    │ │ Service  │ │ Service           │ │
│  └────┬────┘ └────┬────┘ └──────────┘ └───────────────────┘ │
│       │           │                                          │
│  domain/port/outbound/                                      │
│  ┌───────────┐ ┌───────────┐ ┌──────────┐ ┌──────────────┐  │
│  │ OrderRepo │ │ PaymentGwy│ │ EventPub │ │ CacheSvc     │  │
│  └─────┬─────┘ └─────┬─────┘ └────┬─────┘ └──────┬───────┘  │
│        │             │            │               │          │
│  adapter/outbound/   │            │               │          │
│  ┌─────────────┐ ┌───┴────────┐ ┌─┴──────────┐ ┌──┴───────┐ │
│  │ Postgres    │ │ Stripe     │ │ RabbitMQ   │ │ Redis    │ │
│  │ (3 repos)   │ │ Gateway    │ │ Publisher  │ │ Cache    │ │
│  └─────────────┘ └────────────┘ └────────────┘ └──────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 10-20 人 | 需要内部包级别的模块化 |
| 入口数量 | 3+ (REST/gRPC/CLI) | 多入口共享同一套业务逻辑 |
| 外部依赖 | 5+ | 支付网关、消息队列、缓存、通知 |
| 领域复杂度 | 中-高 | 3+ 聚合根、跨聚合领域服务、Saga |
| 项目生命周期 | 成长期-成熟期 | 业务复杂但暂未拆分微服务 |

## 关键设计决策

1. **多聚合根隔离** — 每个聚合有独立的 model 子包，聚合间通过领域事件松耦合
2. **领域服务处理跨聚合逻辑** — Saga 模式协调 Order ↔ Payment 一致性
3. **适配器按传递方式组织** — inbound 按协议（rest/grpc/cli），outbound 按技术（persistence/external/messaging/cache）
4. **共享值对象放在 shared 包** — Money/CustomerId 被多个聚合复用

## 演进路径

```
单体复杂六边形 (本示例)
    │  隔离有界上下文
    ▼
Maven 多模块 (08-monolith-multi-module)
    │  独立部署需求
    ▼
微服务六边形 (09-12)
```
