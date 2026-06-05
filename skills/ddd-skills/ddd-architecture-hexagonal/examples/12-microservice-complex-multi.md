# Example: 微服务复杂多模块六边形架构

最复杂的六边形架构组合：多微服务 x 多模块 x 多聚合，适用于超大型团队的分布式系统。

## 场景

50+ 人团队、15+ 微服务、每个核心服务内部使用 Maven 多模块六边形架构。服务间通过 gRPC + Kafka 通信，CQRS 读写分离，独立数据库。

## 系统全景

```
┌──────────────────────────────────────────────────────────────────┐
│                        API Gateway (Kong / Envoy)                │
└──┬──────────┬──────────┬──────────┬──────────┬───────────────────┘
   │          │          │          │          │
   ▼          ▼          ▼          ▼          ▼
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────────┐
│order │  │paymt │  │inven │  │deliv │  │notifi    │
│-svc  │  │-svc  │  │-svc  │  │-svc  │  │-svc      │
│      │  │      │  │      │  │      │  │          │
│ 6模块 │  │ 5模块 │  │ 5模块 │  │ 5模块 │  │ 4模块     │
│ CQRS  │  │ Saga │  │ CQRS  │  │ Saga │  │ 简单模块  │
└──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘  └────┬─────┘
   │         │         │         │            │
   └────┬────┴────┬────┴────┬────┴─────┬──────┘
        │         │         │          │
   ┌────▼─────────▼─────────▼──────────▼────┐
   │           Kafka Event Bus             │
   └────────────────────────────────────────┘
        │         │         │          │
   ┌────▼───┐ ┌───▼───┐ ┌───▼───┐ ┌───▼────┐
   │ Postgre│ │ Postgre│ │ Postgre│ │ MongoDB│
   │ (order)│ │(paymt) │ │(inven) │ │(notif) │
   └────────┘ └───────┘ └───────┘ └────────┘
```

## order-service 内部（最复杂 — 7 模块 + CQRS）

```
order-service/
├── pom.xml
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
│
├── order-domain/                                    # 领域核心
│   ├── pom.xml                                      # 零框架依赖
│   └── src/main/java/.../
│       ├── model/
│       │   ├── order/Order.java
│       │   ├── order/OrderId.java
│       │   ├── order/OrderItem.java
│       │   └── order/OrderStatus.java
│       ├── service/
│       │   ├── OrderPricingService.java             # 定价领域服务
│       │   └── OrderSagaCoordinator.java            # Saga 协调
│       ├── port/
│       │   ├── inbound/
│       │   │   ├── command/                         # CQRS Command 端口
│       │   │   │   ├── CreateOrderUseCase.java
│       │   │   │   ├── PayOrderUseCase.java
│       │   │   │   └── CancelOrderUseCase.java
│       │   │   └── query/                           # CQRS Query 端口
│       │   │       ├── OrderQueryUseCase.java
│       │   │       └── OrderHistoryUseCase.java
│       │   └── outbound/
│       │       ├── OrderCommandRepository.java      # 写库
│       │       ├── OrderQueryRepository.java        # 读库（CQRS 分离）
│       │       ├── PaymentGateway.java
│       │       ├── InventoryClient.java
│       │       ├── LogisticsClient.java
│       │       ├── NotificationClient.java
│       │       └── EventPublisher.java
│       └── event/
│           ├── OrderCreatedEvent.java
│           ├── OrderPaidEvent.java
│           └── OrderCancelledEvent.java
│
├── order-application/                               # 应用层
│   ├── pom.xml                                      # 依赖 order-domain
│   └── src/main/java/.../
│       ├── command/                                 # Command 处理
│       │   ├── CreateOrderCommandHandler.java
│       │   ├── PayOrderCommandHandler.java
│       │   └── CancelOrderCommandHandler.java
│       └── query/                                   # Query 处理
│           ├── OrderQueryHandler.java
│           └── OrderHistoryQueryHandler.java
│
├── order-adapter-inbound/                           # 主适配器
│   ├── pom.xml                                      # 依赖 order-application + Spring Web/gRPC
│   └── src/main/java/.../
│       ├── rest/
│       │   ├── OrderCommandController.java          # POST /orders, PUT /orders/{id}/pay
│       │   └── OrderQueryController.java            # GET /orders, GET /orders/{id}
│       ├── grpc/
│       │   └── OrderGrpcService.java
│       └── kafka/
│       │   ├── PaymentEventListener.java            # 异步驱动：支付完成 → 更新订单
│       │   └── InventoryEventListener.java          # 异步驱动：库存预留 → 确认
│       └── dto/
│           ├── CreateOrderRequest.java
│           ├── OrderResponse.java
│           └── OrderEventProtoMapper.java
│
├── order-adapter-outbound-command/                  # 次适配器 — 写
│   ├── pom.xml                                      # 依赖 order-domain + Spring Data JPA
│   └── src/main/java/.../
│       └── persistence/
│           ├── PostgresOrderCommandRepository.java
│           ├── entity/
│           │   └── OrderJpaEntity.java
│           └── mapper/OrderCommandMapper.java
│
├── order-adapter-outbound-query/                    # 次适配器 — 读
│   ├── pom.xml                                      # 依赖 order-domain + Spring Data Elasticsearch
│   └── src/main/java/.../
│       └── persistence/
│           ├── ElasticsearchOrderQueryRepository.java
│           ├── document/
│           │   └── OrderDocument.java               # ES 文档
│           └── mapper/OrderQueryMapper.java
│
├── order-adapter-outbound-external/                 # 次适配器 — 外部
│   ├── pom.xml                                      # 依赖 order-domain + gRPC/Stripe Client
│   └── src/main/java/.../
│       ├── payment/
│       │   └── StripePaymentGateway.java
│       ├── microservice/
│       │   ├── GrpcInventoryClient.java
│       │   ├── GrpcLogisticsClient.java
│       │   └── GrpcNotificationClient.java
│       └── messaging/
│           └── KafkaEventPublisher.java
│
└── order-app/                                       # 启动器
    ├── pom.xml                                      # 依赖所有模块 + Spring Boot
    ├── src/main/java/.../
    │   ├── OrderApp.java
    │   └── config/
    │       ├── AdapterConfig.java
    │       ├── UseCaseConfig.java
    │       └── CQRSConfig.java
    └── src/main/resources/
        ├── application-command.yml                  # 写库配置
        ├── application-query.yml                    # 读库配置
        └── application-external.yml                 # 外部服务配置
```

## CQRS 读写分离架构

```
                    ┌─────────────────┐
                   │   API Gateway    │
                   └────────┬────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
    ┌─────────▼─────────┐     ┌──────────▼──────────┐
    │  Command Side     │     │   Query Side         │
    │                   │     │                      │
    │ CreateOrderCmd    │     │  OrderQueryHandler   │
    │ PayOrderCmd       │     │  HistoryQueryHandler │
    │ CancelOrderCmd    │     │                      │
    │       │           │     │         │            │
    │       ▼           │     │         ▼            │
    │ OrderCommandRepo  │     │  OrderQueryRepo      │
    │       │           │     │         │            │
    └───────┼───────────┘     └─────────┼────────────┘
            │                           │
    ┌───────▼───────────┐     ┌─────────▼────────────┐
    │  PostgreSQL       │     │  Elasticsearch       │
    │  (Normalized)     │────►│  (Denormalized/View) │
    │                   │ CDC │                      │
    └───────────────────┘     └──────────────────────┘

CDC: Debezium 监听 PostgreSQL WAL → Kafka → Elasticsearch Sink
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 50+ 人 | 超大型分布式团队 |
| 微服务数量 | 15+ | 核心交易链路服务 |
| 单服务模块数 | 5-7 | CQRS 需要独立读写模块 |
| CQRS | 是 | PostgreSQL (写) + Elasticsearch (读) |
| Saga | 是 | 分布式 Saga (Orchestration) |
| 事件溯源 | 可选 | Kafka 作为事件存储 |
| CDC | 是 | Debezium 同步读写库 |
| 项目生命周期 | 超大规模成熟期 | 架构投入值得回报 |

## 端口统计（order-service）

| 类型 | 端口 | 数量 |
|------|------|------|
| Command 入站 | CreateOrder/PayOrder/CancelOrder | 3 |
| Query 入站 | OrderQuery/OrderHistory | 2 |
| 出站 Repository | CommandRepo / QueryRepo | 2 |
| 出站 External | PaymentGateway | 1 |
| 出站 Microservice | Inventory/Logistics/Notification | 3 |
| 出站 Messaging | EventPublisher | 1 |
| **合计** | | **12** |

## 关键设计决策

1. **CQRS 端口分离** — `command/` 和 `query/` 子包下分别定义入站端口
2. **读写持久化独立模块** — adapter-outbound-command 和 adapter-outbound-query 各自独立
3. **CDC 同步读写库** — Debezium 监听 PostgreSQL 变更，写入 Elasticsearch
4. **编排式 Saga** — `OrderSagaCoordinator` 作为领域服务，协调分布式事务
5. **事件驱动 + REST 混合入口** — Kafka Listener 处理异步事件，REST/gRPC 处理同步请求

## 复杂度对比矩阵

```
               简单 (Simple)        复杂 (Complex)        多模块 (Multi-Module)
单体           06-monolith-simple   07-monolith-complex   08-monolith-multi-module
(Monolith)

微服务         09-micro-simple      10-micro-complex      11-micro-multi-module
(Microservice)

微服务×多模块   —                   12-micro-complex-multi (本示例)
(Complex Multi)                     ← 最复杂组合
```

## 建议引入顺序

```
06-monolith-simple ──► 07-monolith-complex ──► 08-monolith-multi-module
                                                   │
                                                   ▼
                        09-microservice-simple ──► 10-microservice-complex
                                                      │
                                                      ▼
                                           11-microservice-multi-module
                                                      │
                                                      ▼
                                           12-microservice-complex-multi (本示例)
```
