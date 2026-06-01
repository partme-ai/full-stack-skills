# 09 — 微服务 Clean 架构（简单版）

> 单个微服务内按包名划分四层，适用单体拆分后的第一个独立微服务。

## 目录树

```
order-service/                              # 独立微服务
├── Dockerfile
├── pom.xml
├── src/main/java/com/example/order/
│   ├── enterprise/                         # Enterprise Business Rules
│   │   ├── entity/
│   │   │   └── Order.java
│   │   ├── vo/
│   │   │   ├── OrderId.java
│   │   │   ├── Money.java
│   │   │   └── OrderStatus.java
│   │   └── event/
│   │       ├── DomainEvent.java
│   │       └── OrderCreatedEvent.java
│   │
│   ├── usecase/                            # Application Business Rules
│   │   ├── port/input/
│   │   │   ├── CreateOrderUseCase.java
│   │   │   └── QueryOrderUseCase.java
│   │   ├── port/output/
│   │   │   ├── OrderRepository.java
│   │   │   └── EventBus.java              # 发布事件到 MQ
│   │   ├── dto/
│   │   │   ├── CreateOrderRequest.java
│   │   │   └── OrderDTO.java
│   │   └── interactor/
│   │       ├── CreateOrderInteractor.java
│   │       └── QueryOrderInteractor.java
│   │
│   ├── adapter/                            # Interface Adapters
│   │   ├── controller/
│   │   │   └── OrderController.java
│   │   ├── repository/
│   │   │   ├── OrderJpaEntity.java
│   │   │   └── OrderRepositoryImpl.java
│   │   ├── messaging/
│   │   │   ├── KafkaEventBus.java
│   │   │   └── OrderEventConsumer.java    # 消费其他服务事件
│   │   └── client/                        # 外部服务调用适配器
│   │       └── InventoryServiceClient.java
│   │
│   └── framework/                          # Frameworks & Drivers
│       └── config/
│           ├── OrderApplication.java
│           ├── UseCaseConfig.java
│           ├── PersistenceConfig.java
│           ├── KafkaConfig.java
│           └── FeignClientConfig.java
│
├── src/main/resources/
│   ├── application.yml
│   └── db/migration/                       # Flyway 迁移脚本
│       └── V1__create_order_table.sql
│
└── src/test/java/com/example/order/
    ├── enterprise/entity/OrderTest.java
    ├── usecase/interactor/CreateOrderInteractorTest.java
    ├── adapter/repository/OrderRepositoryImplTest.java
    ├── integration/
    │   └── OrderServiceIntegrationTest.java
    └── architecture/
        └── ArchitectureTest.java
```

## 服务拓扑

```
                    ┌──────────────┐
                    │  API Gateway │
                    └──────┬───────┘
                           │ HTTP/REST
          ┌────────────────┼────────────────┐
          │                │                │
    ┌─────▼─────┐   ┌─────▼─────┐   ┌─────▼─────┐
    │  order    │   │ payment   │   │ inventory │
    │  service  │   │  service  │   │  service  │
    └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
          │                │                │
          └────────────────┼────────────────┘
                           │ Async Events
                    ┌──────▼───────┐
                    │    Kafka     │
                    └──────────────┘

每个微服务内部使用整洁架构四层结构
```

## 依赖方向（微服务内 + 微服务间）

**微服务内**（同 06-monolith-simple）：
```
framework ──► adapter ──► usecase ──► enterprise
```

**微服务间**：
```
order ◄──► payment (通过 REST API 同步调用 + Kafka 异步事件)
order ◄──► inventory (通过 REST API 同步调用 + Kafka 异步事件)
禁止：微服务间直接共享代码/实体，只通过 API Contract 通信
```

## 微服务特有关注点

### 1. 远程调用适配器

```java
// adapter/client/InventoryServiceClient.java
@Component
public class InventoryServiceClient implements ReserveInventoryPort {
    private final InventoryFeignClient feignClient;

    @Override
    public ReserveResult reserve(ReserveCommand cmd) {
        // 将领域命令转为 HTTP DTO
        var request = InventoryReserveRequest.from(cmd);
        var response = feignClient.reserve(request);
        return response.toDomain();  // 转回领域对象
    }
}
```

### 2. 事件总线适配器

```java
// adapter/messaging/KafkaEventBus.java
@Component
public class KafkaEventBus implements EventBus {
    private final KafkaTemplate<String, DomainEvent> kafka;

    @Override
    public void publish(DomainEvent event) {
        kafka.send("order-events", event.getAggregateId(), event);
    }
}
```

### 3. 分布式事务

- **Saga 编排**：由 UseCase Interactor 编排本地事务 + 补偿逻辑
- **Outbox 模式**：领域事件先写本地 outbox 表，再异步投递到 Kafka
- **幂等消费**：消费者按 eventId 去重

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 4-10 人/服务 |
| 项目复杂度 | 1-2 个聚合根/服务，< 15 个 UseCase/服务 |
| 服务数 | 3-8 个微服务 |
| 通信方式 | REST（同步）+ Kafka（异步） |
| 部署方式 | Docker + K8s，独立部署 |
| 典型业务 | 从单体拆分出的核心领域微服务（订单/支付/库存） |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| 独立部署、扩展、技术栈选择 | 分布式复杂度（网络、事务、一致性） |
| 整洁架构保证微服务内部质量 | 重复的四层结构模板代码 |
| 清晰的服务边界 | 需额外处理服务发现、配置中心 |
| 适合小团队独立交付 | 跨服务调试困难 |
