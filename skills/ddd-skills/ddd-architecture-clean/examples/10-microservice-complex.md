# 10 — 微服务 Clean 架构（复杂版）

> 单微服务内含多聚合根 + 多 Interactor + 领域事件 + CQRS + Saga 编排。

## 目录树

```
order-service/
├── Dockerfile
├── pom.xml
├── src/main/java/com/example/order/
│   ├── shared/                              # 微服务内共享内核
│   │   ├── domain/
│   │   │   ├── Identifier.java
│   │   │   ├── Money.java
│   │   │   └── DomainEvent.java
│   │   └── event/
│   │       └── EventPublisher.java
│   │
│   ├── order/                               # 订单子域
│   │   ├── enterprise/
│   │   │   ├── entity/Order.java
│   │   │   ├── entity/OrderItem.java
│   │   │   ├── vo/OrderId.java
│   │   │   ├── vo/OrderStatus.java
│   │   │   └── event/
│   │   │       ├── OrderCreatedEvent.java
│   │   │       ├── OrderPaidEvent.java
│   │   │       └── OrderCancelledEvent.java
│   │   ├── usecase/
│   │   │   ├── port/input/
│   │   │   │   ├── CreateOrderUseCase.java
│   │   │   │   ├── PayOrderUseCase.java
│   │   │   │   └── CancelOrderUseCase.java
│   │   │   ├── port/output/
│   │   │   │   ├── OrderRepository.java
│   │   │   │   └── PaymentPort.java
│   │   │   ├── dto/
│   │   │   │   ├── CreateOrderRequest.java
│   │   │   │   └── OrderDTO.java
│   │   │   └── interactor/
│   │   │       ├── CreateOrderInteractor.java
│   │   │       └── PayOrderSagaInteractor.java  # Saga 编排器
│   │   ├── adapter/
│   │   │   ├── controller/OrderController.java
│   │   │   ├── repository/
│   │   │   │   ├── OrderJpaEntity.java
│   │   │   │   └── OrderRepositoryImpl.java
│   │   │   └── messaging/
│   │   │       ├── OrderEventPublisher.java
│   │   │       └── PaymentEventConsumer.java
│   │   └── framework/
│   │       └── config/OrderDomainConfig.java
│   │
│   ├── fulfillment/                          # 履约子域
│   │   ├── enterprise/
│   │   │   ├── entity/FulfillmentOrder.java
│   │   │   ├── vo/FulfillmentId.java
│   │   │   ├── vo/FulfillmentStatus.java
│   │   │   └── event/
│   │   │       └── FulfillmentStartedEvent.java
│   │   ├── usecase/
│   │   │   ├── port/input/
│   │   │   │   ├── StartFulfillmentUseCase.java
│   │   │   │   └── CompleteFulfillmentUseCase.java
│   │   │   ├── port/output/
│   │   │   │   └── FulfillmentRepository.java
│   │   │   └── interactor/
│   │   │       └── StartFulfillmentInteractor.java
│   │   └── adapter/repository/
│   │       └── FulfillmentRepositoryImpl.java
│   │
│   └── query/                               # CQRS 查询端
│       ├── dto/
│       │   ├── OrderSummaryDTO.java
│       │   └── OrderDetailDTO.java
│       ├── port/
│       │   ├── QueryOrderUseCase.java
│       │   └── QueryFulfillmentUseCase.java
│       ├── interactor/
│       │   ├── QueryOrderInteractor.java
│       │   └── QueryFulfillmentInteractor.java
│       └── adapter/
│           ├── controller/
│           │   ├── OrderQueryController.java
│           │   └── FulfillmentQueryController.java
│           └── repository/
│               ├── OrderReadRepository.java
│               └── FulfillmentReadRepository.java
│
├── src/main/resources/
│   ├── application.yml
│   ├── application-kafka.yml
│   └── db/migration/
│       ├── V1__create_order_table.sql
│       ├── V2__create_outbox_table.sql
│       └── V3__create_fulfillment_table.sql
│
└── src/test/java/com/example/order/
    ├── order/usecase/interactor/
    │   ├── CreateOrderInteractorTest.java
    │   └── PayOrderSagaInteractorTest.java
    ├── integration/
    │   ├── OrderSagaIntegrationTest.java
    │   └── EventPublishingIntegrationTest.java
    └── architecture/
        └── ArchitectureTest.java
```

## 核心模式

### 1. CQRS 分离

```
┌─────────────────────────────────────────────────┐
│                   Order Service                  │
│                                                  │
│  ┌──────────────────┐   ┌──────────────────┐    │
│  │  Command Side    │   │   Query Side     │    │
│  │                  │   │                  │    │
│  │ OrderController  │   │ OrderQueryCtrl   │    │
│  │      │           │   │      │           │    │
│  │      ▼           │   │      ▼           │    │
│  │ Interactor       │   │ QueryInteractor  │    │
│  │      │           │   │      │           │    │
│  │      ▼           │   │      ▼           │    │
│  │ OrderRepository  │   │ OrderReadRepo    │    │
│  │   (JPA Entity)   │   │  (Native SQL)    │    │
│  └──────────────────┘   └──────────────────┘    │
│                                                  │
│  同一张 MySQL 表，但读写使用不同数据模型          │
└─────────────────────────────────────────────────┘
```

### 2. Saga 编排

```java
// order/usecase/interactor/PayOrderSagaInteractor.java
public class PayOrderSagaInteractor implements PayOrderUseCase {

    @Override
    public PayOrderResponse execute(PayOrderRequest request) {
        // Step 1: 锁定库存（调用 inventory service）
        var reserveResult = reserveInventoryPort.reserve(request);
        if (reserveResult.isFailure()) return PayOrderResponse.failed();

        // Step 2: 扣款（调用 payment service）
        var paymentResult = paymentPort.charge(request);
        if (paymentResult.isFailure()) {
            // 补偿: 释放库存
            releaseInventoryPort.release(request.getOrderId());
            return PayOrderResponse.failed();
        }

        // Step 3: 更新订单状态
        var order = orderRepository.findById(request.getOrderId());
        order.markAsPaid();
        orderRepository.save(order);

        // Step 4: 发布事件
        eventPublisher.publish(new OrderPaidEvent(order));

        return PayOrderResponse.success(order);
    }
}
```

### 3. Outbox 模式（事件可靠性）

```java
// Saga Interactor 发布事件时同步写 outbox
order.markAsPaid();
order.addEvent(new OrderPaidEvent(order));  // 添加到 outbox 列表
orderRepository.save(order);                 // 事务提交，事件落表

// OutboxScheduler 异步轮询投递到 Kafka
@Scheduled(fixedDelay = 1000)
public void publishOutboxEvents() {
    var events = outboxRepository.findUnpublished(100);
    events.forEach(e -> {
        kafkaTemplate.send(e.getTopic(), e.getPayload());
        outboxRepository.markAsPublished(e.getId());
    });
}
```

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 8-20 人/服务 |
| 项目复杂度 | 3-5 个聚合根/服务，15-40 个 UseCase/服务 |
| 架构模式 | CQRS + Saga + Outbox + Event-Driven |
| 通信方式 | REST（同步）+ Kafka（异步事件总线） |
| 典型业务 | 复杂电商订单、物流履约、保险理赔 |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| CQRS 读写分离，性能可独立优化 | 架构复杂度高，需团队有成熟 DDD 经验 |
| Saga 保证跨服务数据一致性 | 最终一致性增加业务复杂度 |
| 事件驱动解耦，可扩展性强 | Outbox 调度器增加运维负担 |
| 子域内整洁架构，子域间事件通信 | 需要可靠的消息基础设施 |
