# Example: 微服务复杂六边形架构

多聚合 + Saga + 多适配器的微服务六边形架构，每个服务内部结构复杂，适用于核心业务域。

## 场景

负责核心交易链路的 order-service，包含 4 个聚合根、跨聚合 Saga、多外部依赖。服务本身领域复杂度高，但仍是单模块部署。

## 目录树 & 包结构

```
order-service/
├── pom.xml
├── src/main/java/com/example/order/
│   ├── OrderServiceApplication.java
│   │
│   ├── domain/
│   │   ├── model/
│   │   │   ├── order/
│   │   │   │   ├── Order.java                       # 聚合根 1
│   │   │   │   ├── OrderId.java
│   │   │   │   ├── OrderItem.java
│   │   │   │   ├── OrderStatus.java
│   │   │   │   └── OrderCreatedEvent.java
│   │   │   ├── payment/
│   │   │   │   ├── Payment.java                     # 聚合根 2
│   │   │   │   ├── PaymentId.java
│   │   │   │   ├── PaymentMethod.java
│   │   │   │   └── PaymentCompletedEvent.java
│   │   │   ├── delivery/
│   │   │   │   ├── Delivery.java                    # 聚合根 3
│   │   │   │   ├── DeliveryId.java
│   │   │   │   └── DeliveryStatus.java
│   │   │   ├── invoice/
│   │   │   │   ├── Invoice.java                     # 聚合根 4
│   │   │   │   ├── InvoiceId.java
│   │   │   │   └── InvoiceNumber.java
│   │   │   └── shared/
│   │   │       ├── Money.java
│   │   │       ├── CustomerId.java
│   │   │       ├── ProductId.java
│   │   │       └── Address.java
│   │   ├── service/
│   │   │   ├── OrderPaymentSaga.java                # Saga 编排
│   │   │   ├── DeliverySchedulingService.java       # 领域服务
│   │   │   └── InvoiceGenerationService.java        # 领域服务
│   │   ├── port/
│   │   │   ├── inbound/
│   │   │   │   ├── CreateOrderUseCase.java
│   │   │   │   ├── PayOrderUseCase.java
│   │   │   │   ├── TrackDeliveryUseCase.java
│   │   │   │   ├── GenerateInvoiceUseCase.java
│   │   │   │   └── CancelOrderUseCase.java
│   │   │   └── outbound/
│   │   │       ├── OrderRepository.java
│   │   │       ├── PaymentRepository.java
│   │   │       ├── DeliveryRepository.java
│   │   │       ├── InvoiceRepository.java
│   │   │       ├── PaymentGateway.java              # 外部支付
│   │   │       ├── LogisticsProvider.java           # 外部物流
│   │   │       ├── InventoryClient.java             # 库存服务（跨服务）
│   │   │       ├── NotificationPort.java            # 通知（跨服务）
│   │   │       └── EventPublisher.java              # 事件总线
│   │   └── event/
│   │       └── handler/
│   │           ├── PaymentCompletedEventHandler.java
│   │           └── InventoryReservedEventHandler.java
│   │
│   ├── application/
│   │   └── service/
│   │       ├── CreateOrderServiceImpl.java
│   │       ├── PayOrderServiceImpl.java
│   │       ├── CancelOrderServiceImpl.java
│   │       └── SagaOrchestratorImpl.java            # Saga 执行者
│   │
│   ├── adapter/
│   │   ├── inbound/
│   │   │   ├── rest/
│   │   │   │   ├── OrderController.java
│   │   │   │   └── PaymentController.java
│   │   │   ├── grpc/
│   │   │   │   └── OrderGrpcService.java
│   │   │   └── kafka/
│   │   │       ├── InventoryEventListener.java      # 驱动型入口（异步事件）
│   │   │       └── PaymentEventListener.java
│   │   └── outbound/
│   │       ├── persistence/
│   │       │   ├── PostgresOrderRepository.java
│   │       │   ├── PostgresPaymentRepository.java
│   │       │   ├── PostgresDeliveryRepository.java
│   │       │   ├── PostgresInvoiceRepository.java
│   │       │   └── entity/ (JPA Entities)
│   │       ├── external/
│   │       │   ├── StripePaymentGateway.java
│   │       │   └── FedExLogisticsProvider.java
│   │       ├── microservice/
│   │       │   ├── RestInventoryClient.java         # HTTP 调用 inventory-service
│   │       │   └── GrpcNotificationAdapter.java     # gRPC 调用 notification-service
│   │       └── messaging/
│   │           └── KafkaEventPublisher.java
│   │
│   └── configuration/
│       ├── AdapterConfig.java
│       ├── UseCaseConfig.java
│       └── SagaConfig.java
│
└── src/test/
    ├── java/
    │   ├── domain/
    │   │   ├── OrderTest.java
    │   │   └── OrderPaymentSagaTest.java
    │   ├── application/
    │   │   └── SagaOrchestratorImplTest.java
    │   └── adapter/
    │       ├── rest/OrderControllerTest.java
    │       └── microservice/RestInventoryClientTest.java
    └── resources/
        └── contract/                                 # CDC 契约测试
            └── inventory-service.yaml
```

## 依赖关系

```
adapter/inbound/ (REST/gRPC/Kafka)
    │ 依赖 UseCase 接口
    ▼
application/service/
    │ 依赖端口接口 + Saga 编排
    ▼
domain/
    ├── port/inbound/  (被 application 实现)
    ├── port/outbound/ (被 adapter/outbound 实现)
    ├── model/         (Order/Payment/Delivery/Invoice 4 个聚合根)
    ├── service/       (Saga/领域服务)
    └── event/handler/ (领域事件处理器)
    │
    │ 实现
    ▼
adapter/outbound/
    ├── persistence/    → PostgreSQL
    ├── external/       → Stripe / FedEx
    ├── microservice/   → inventory-service / notification-service
    └── messaging/      → Kafka
```

```
Saga 编排示例:

OrderPaymentSaga {
    1. ReserveInventory → inventory-service (出站端口)
    2. ChargePayment    → Stripe (出站端口)
    3. ConfirmDelivery  → FedEx (出站端口)
    4. GenerateInvoice  → 领域服务 (本地)
    5. PublishEvents    → Kafka (出站端口)
}
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 5-15 人/服务 | 核心服务需要较多人力 |
| 聚合根数量 | 4+ | 复杂业务域，多聚合在同一服务内 |
| Saga 编排 | 是 | 跨聚合 + 跨服务的事务协调 |
| 外部依赖 | 8+ | 支付/物流/其他微服务/消息队列 |
| 服务间通信 | 同步+异步 | REST + gRPC + Kafka 混合 |

## 关键设计决策

1. **跨服务调用通过端口抽象** — `InventoryClient` 是端口而非直接 HTTP 调用，可替换为 gRPC 或消息
2. **Saga 作为领域服务** — 协调跨聚合一致性，补偿事务
3. **事件驱动入口** — Kafka Listener 作为主适配器，异步驱动业务
4. **CDC 契约测试** — 验证对其他微服务的调用契约

## 端口统计

| 端口类型 | 数量 | 说明 |
|----------|------|------|
| 入站端口 (UseCase) | 5 | Create/Pay/Track/Generate/Cancel |
| 出站端口 (Repository) | 4 | Order/Payment/Delivery/Invoice |
| 出站端口 (External) | 2 | PaymentGateway/LogisticsProvider |
| 出站端口 (Microservice) | 2 | InventoryClient/NotificationPort |
| 出站端口 (Messaging) | 1 | EventPublisher |
| **合计** | **14** | 单服务端口数反映了领域复杂度 |
