# 12 — 微服务 Clean 架构（复杂多模块版）

> 多子域 + 多模块 + CQRS + Saga + Outbox + API 契约独立发布。Clean Architecture 微服务的最高复杂度形态。

## 目录树

```
order-service/
├── pom.xml                                     # 父 POM
├── Dockerfile
├── docker-compose.yml                          # 本地开发：MySQL + Kafka + Redis
│
├── order-shared/                               # 模块1: 共享内核
│   ├── pom.xml
│   └── src/main/java/com/example/order/shared/
│       ├── domain/
│       │   ├── Identifier.java
│       │   ├── Money.java
│       │   └── DomainEvent.java
│       └── event/
│           └── EventPublisher.java
│
├── order-domain/                               # 模块2: 领域层（Enterprise）
│   ├── pom.xml
│   └── src/main/java/com/example/order/domain/
│       ├── order/
│       │   ├── entity/Order.java
│       │   ├── entity/OrderItem.java
│       │   ├── vo/OrderId.java
│       │   ├── vo/OrderStatus.java
│       │   └── event/
│       │       ├── OrderCreatedEvent.java
│       │       └── OrderPaidEvent.java
│       ├── delivery/
│       │   ├── entity/Delivery.java
│       │   ├── vo/DeliveryId.java
│       │   └── vo/DeliveryStatus.java
│       └── invoice/
│           ├── entity/Invoice.java
│           ├── vo/InvoiceId.java
│           └── vo/InvoiceStatus.java
│
├── order-usecase/                              # 模块3: 用例层（Application）
│   ├── pom.xml
│   └── src/main/java/com/example/order/usecase/
│       ├── order/
│       │   ├── port/input/
│       │   │   ├── CreateOrderUseCase.java
│       │   │   ├── PayOrderUseCase.java
│       │   │   └── CancelOrderUseCase.java
│       │   ├── port/output/
│       │   │   ├── OrderRepository.java
│       │   │   └── PaymentPort.java
│       │   ├── dto/
│       │   │   ├── CreateOrderRequest.java
│       │   │   └── OrderResponse.java
│       │   └── interactor/
│       │       ├── CreateOrderInteractor.java
│       │       └── PayOrderSagaInteractor.java
│       ├── delivery/
│       │   ├── port/input/
│       │   │   ├── ScheduleDeliveryUseCase.java
│       │   │   └── TrackDeliveryUseCase.java
│       │   ├── port/output/
│       │   │   └── DeliveryRepository.java
│       │   └── interactor/
│       │       └── ScheduleDeliveryInteractor.java
│       └── invoice/
│           ├── port/input/
│           │   └── GenerateInvoiceUseCase.java
│           ├── port/output/
│           │   └── InvoiceRepository.java
│           └── interactor/
│               └── GenerateInvoiceInteractor.java
│
├── order-adapter-persistence/                  # 模块4A: 持久化适配
│   ├── pom.xml
│   └── src/main/java/com/example/order/adapter/persistence/
│       ├── order/
│       │   ├── OrderJpaEntity.java
│       │   ├── OrderItemJpaEntity.java
│       │   ├── OrderJpaRepository.java
│       │   └── OrderRepositoryImpl.java
│       ├── delivery/
│       │   ├── DeliveryJpaEntity.java
│       │   └── DeliveryRepositoryImpl.java
│       └── invoice/
│           ├── InvoiceJpaEntity.java
│           └── InvoiceRepositoryImpl.java
│
├── order-adapter-web/                          # 模块4B: Web 适配
│   ├── pom.xml
│   └── src/main/java/com/example/order/adapter/web/
│       ├── order/
│       │   └── OrderController.java
│       ├── delivery/
│       │   └── DeliveryController.java
│       └── invoice/
│           └── InvoiceController.java
│
├── order-adapter-messaging/                    # 模块4C: 消息适配
│   ├── pom.xml
│   └── src/main/java/com/example/order/adapter/messaging/
│       ├── publisher/
│       │   └── KafkaEventPublisher.java
│       └── consumer/
│           ├── PaymentEventConsumer.java
│           └── InventoryEventConsumer.java
│
├── order-query/                                # 模块5: CQRS 查询端
│   ├── pom.xml
│   └── src/main/java/com/example/order/query/
│       ├── dto/
│       │   ├── OrderSummaryDTO.java
│       │   └── OrderDetailDTO.java
│       ├── port/
│       │   ├── QueryOrderPort.java
│       │   └── QueryDeliveryPort.java
│       ├── interactor/
│       │   ├── QueryOrderInteractor.java
│       │   └── QueryDeliveryInteractor.java
│       └── adapter/
│           ├── controller/
│           │   ├── OrderQueryController.java
│           │   └── DeliveryQueryController.java
│           └── persistence/
│               └── OrderReadRepository.java
│
├── order-client/                               # 模块6: API 契约
│   ├── pom.xml
│   └── src/main/java/com/example/order/client/
│       ├── dto/
│       │   ├── CreateOrderRequest.java
│       │   └── OrderResponse.java
│       ├── api/
│       │   └── OrderServiceApi.java
│       └── event/
│           └── OrderEventSchema.java
│
├── order-boot/                                 # 模块7: 启动配置
│   ├── pom.xml
│   └── src/main/java/com/example/order/boot/
│       ├── OrderApplication.java
│       └── config/
│           ├── UseCaseConfig.java
│           ├── PersistenceConfig.java
│           ├── KafkaConfig.java
│           └── SwaggerConfig.java
│
└── order-integration-test/                     # 模块8: 集成测试
    ├── pom.xml
    └── src/test/java/com/example/order/it/
        ├── OrderSagaIntegrationTest.java
        ├── EventDrivenIntegrationTest.java
        └── CqrsIntegrationTest.java
```

## 模块依赖图

```
┌─────────────────────────────────────────────────────────────┐
│                      order-boot                              │
│   Spring Boot App + DI Config                               │
│   依赖: 所有模块                                              │
└──┬──────────┬──────────┬──────────┬──────────┬──────────────┘
   │          │          │          │          │
   ▼          ▼          ▼          ▼          ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│adapter│ │adapter│ │adapter│ │query │ │  client  │
│web    │ │persist│ │msging │ │      │ │          │
└──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──────────┘
   │        │        │        │
   └────────┼────────┼────────┘
            │        │
            ▼        ▼
      ┌──────────────┐
      │  order-usecase│
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐        ┌──────────────┐
      │ order-domain │◄───────│ order-shared │
      └──────────────┘        └──────────────┘

依赖方向始终向内：boot → adapters → usecase → domain → shared
```

## 子域间通信（微服务内）

```
┌──────────────────────────────────────────────────────┐
│                   Order Service                       │
│                                                       │
│  ┌──────────┐   event    ┌──────────┐   event        │
│  │  order   │───────────►│ delivery │───────────►    │
│  │  created │            │ schedule │               │
│  └──────────┘            └──────────┘               │
│        │                      │                      │
│        │ event                │ event                │
│        ▼                      ▼                      │
│  ┌──────────┐           ┌──────────┐                │
│  │ invoice  │           │inventory │ (external)      │
│  │ generate │           │  reserve │                │
│  └──────────┘           └──────────┘                │
│                                                       │
│  同一服务内子域通过 In-Memory EventBus 通信             │
└──────────────────────────────────────────────────────┘
```

### 服务内事件总线

```java
// order-shared/event/EventPublisher.java
public interface EventPublisher {
    void publish(DomainEvent event);
    <T extends DomainEvent> void subscribe(Class<T> type, Consumer<T> handler);
}

// order-boot/config/UseCaseConfig.java
@Bean
public EventPublisher eventPublisher() {
    var bus = new InMemoryEventBus();
    // order created → schedule delivery
    bus.subscribe(OrderCreatedEvent.class, deliveryScheduler::onOrderCreated);
    // order paid → generate invoice
    bus.subscribe(OrderPaidEvent.class, invoiceGenerator::onOrderPaid);
    return bus;
}
```

## 对比：12 种规模选型矩阵

| # | 名称 | 模块数 | 聚合/服务 | 适用团队 | 关键特征 |
|---|------|--------|----------|---------|---------|
| 06 | 单体简单 | 1 | 1-3 | 3-8人 | 包级分层，单模块 |
| 07 | 单体复杂 | 1 | 3-8 | 8-20人 | 多领域包隔离 |
| 08 | 单体多模块 | 4-6 | 3-8 | 8-25人 | 编译期强制分层 |
| 09 | 微服务简单 | 1/服务 | 1-2/服务 | 4-10人/服务 | 包级分层，独立部署 |
| 10 | 微服务复杂 | 1/服务 | 3-5/服务 | 8-20人/服务 | CQRS + Saga + Outbox |
| 11 | 微服务多模块 | 5-6/服务 | 2-4/服务 | 8-20人/服务 | 编译期强制 + API 契约 |
| 12 | 微服务复杂多模块 | 7-8/服务 | 3-5/服务 | 10-30人/服务 | 全模式：子域+模块+CQRS+Saga+API |

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 10-30 人/服务 |
| 项目复杂度 | 3-5 个子域/服务，20-50 个 UseCase |
| 架构模式 | Clean Architecture + DDD + CQRS + Event-Driven + Saga + Outbox |
| 通信方式 | 服务内 In-Memory EventBus + 服务间 Kafka |
| 部署方式 | Docker + K8s + 独立 CI/CD 管道 |
| 典型业务 | 大型电商订单中台、金融交易核心、保险理赔系统 |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| 编译期 100% 架构合规 | 8 个模块维护成本极高 |
| 子域隔离 + 分层隔离，双重保护 | 新人需要极长时间上手 |
| API 契约独立版本演进 | 过度工程化风险（小团队不适用） |
| 全链路可测试 | 构建时间较长，需要模块级缓存优化 |
