# 微服务复杂 — 事件驱动 DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 15-40 人，多个自治团队 |
| 业务复杂度 | 高，跨服务业务流程（Saga） |
| 部署方式 | Docker/K8s，独立部署多服务 |
| 技术栈 | Spring Boot + Spring Cloud + Kafka/RabbitMQ + MyBatis/JPA |
| 通信方式 | REST（查询/命令） + 事件驱动（领域事件异步广播） |

**典型业务**：电商全流程（下单→扣库存→支付→发货→通知），金融交易系统（风控→授信→放款→对账）。

## 目录树

```
ecommerce-platform/
├── pom.xml
│
├── order-service/                             # 订单服务
│   ├── pom.xml
│   └── src/main/java/com/example/order/
│       ├── OrderServiceApplication.java
│       ├── interface/
│       │   ├── controller/
│       │   │   └── OrderController.java
│       │   ├── dto/
│       │   └── converter/
│       ├── application/
│       │   ├── service/
│       │   │   └── OrderApplicationService.java
│       │   ├── command/
│       │   │   ├── CreateOrderCommand.java
│       │   │   └── ConfirmOrderCommand.java
│       │   ├── query/
│       │   └── event/                         # 事件处理器（监听其他服务事件）
│       │       └── handler/
│       │           ├── PaymentCompletedHandler.java  # 支付成功 → 确认订单
│       │           ├── ShipmentCreatedHandler.java   # 发货 → 更新订单状态
│       │           └── InventoryDeductedHandler.java # 库存扣减 → 标记可支付
│       ├── domain/
│       │   └── order/
│       │       ├── entity/
│       │       │   ├── Order.java
│       │       │   └── OrderItem.java
│       │       ├── valueobject/
│       │       │   ├── Money.java
│       │       │   ├── OrderStatus.java
│       │       │   └── Address.java
│       │       ├── service/
│       │       │   └── OrderDomainService.java
│       │       ├── repository/
│       │       │   └── OrderRepository.java
│       │       └── event/
│       │           ├── OrderPlacedEvent.java         # 领域事件（发给 MQ）
│       │           ├── OrderConfirmedEvent.java
│       │           └── OrderCancelledEvent.java
│       └── infrastructure/
│           ├── repository/
│           │   └── MyBatisOrderRepository.java
│           ├── persistence/
│           │   ├── OrderPO.java
│           │   └── OrderEventLogPO.java             # 事件溯源/事件日志
│           ├── messaging/                            # 事件总线
│           │   ├── DomainEventPublisher.java         # 发布领域事件
│           │   ├── KafkaEventPublisher.java
│           │   ├── DomainEventSubscriber.java        # 订阅外部事件
│           │   └── KafkaEventSubscriber.java
│           ├── external/
│           │   ├── ProductServiceClient.java
│           │   └── PaymentServiceClient.java
│           └── config/
│               ├── KafkaConfig.java
│               └── RepositoryConfig.java
│
├── product-service/
│   ├── pom.xml
│   └── src/main/java/com/example/product/
│       ├── ...
│       ├── application/
│       │   └── event/handler/
│       │       ├── OrderPlacedHandler.java           # 下单 → 锁定库存
│       │       └── OrderCancelledHandler.java        # 取消订单 → 释放库存
│       ├── domain/product/
│       │   └── event/
│       │       ├── InventoryDeductedEvent.java
│       │       └── InventoryReleasedEvent.java
│       └── infrastructure/
│           └── messaging/
│               ├── KafkaEventPublisher.java
│               └── KafkaEventSubscriber.java
│
├── payment-service/
│   ├── pom.xml
│   └── src/main/java/com/example/payment/
│       ├── ...
│       ├── application/
│       │   └── event/handler/
│       │       ├── OrderConfirmedHandler.java        # 订单确认 → 发起支付
│       │       └── InventoryDeductedHandler.java     # 库存扣减 → 创建支付单
│       ├── domain/payment/
│       │   └── event/
│       │       ├── PaymentInitiatedEvent.java
│       │       └── PaymentCompletedEvent.java
│       └── infrastructure/
│           └── messaging/
│               ├── KafkaEventPublisher.java
│               └── KafkaEventSubscriber.java
│
├── notification-service/                     # 通知服务
│   ├── pom.xml
│   └── src/main/java/com/example/notification/
│       ├── interface/controller/
│       ├── application/
│       │   └── event/handler/
│       │       ├── OrderPlacedHandler.java
│       │       ├── PaymentCompletedHandler.java
│       │       └── ShipmentCreatedHandler.java
│       ├── domain/notification/
│       │   ├── entity/
│       │   │   └── Notification.java
│       │   └── repository/
│       │       └── NotificationRepository.java
│       └── infrastructure/
│           ├── repository/
│           ├── messaging/
│           │   └── KafkaEventSubscriber.java
│           └── external/
│               ├── SmsClient.java
│               └── EmailClient.java
│
└── shared-events/                            # 共享事件定义
    ├── pom.xml
    └── src/main/java/com/example/shared/
        ├── OrderPlacedEvent.java
        ├── OrderConfirmedEvent.java
        ├── OrderCancelledEvent.java
        ├── InventoryDeductedEvent.java
        ├── InventoryReleasedEvent.java
        ├── PaymentCompletedEvent.java
        └── ShipmentCreatedEvent.java
```

## 包结构

```
com.example.order         — 订单微服务
com.example.product       — 商品微服务
com.example.payment       — 支付微服务
com.example.notification  — 通知微服务
com.example.shared        — 共享事件类型
```

## 事件流设计

### 下单流程事件链

```
OrderPlaced           → Product 锁定库存
InventoryDeducted     → Payment 创建支付单
PaymentCompleted      → Order 确认订单
OrderConfirmed        → Notification 发送通知
```

```
order-service  ──OrderPlaced──▶  product-service
                                │
product-service ──InventoryDeducted──▶ payment-service
                                        │
payment-service ──PaymentCompleted──▶  order-service
                                       │
order-service ──OrderConfirmed──▶  notification-service
```

### Saga 补偿事件

```
OrderCancelled → Product 释放库存 + Payment 退款
```

## 模块依赖

### 事件共享模块（shared-events）

```xml
<artifactId>shared-events</artifactId>
<dependencies>
    <!-- 仅包含 POJO 事件定义，零 Spring 依赖 -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-annotations</artifactId>
    </dependency>
</dependencies>
```

### 服务依赖 shared-events

```xml
<!-- order-service/pom.xml -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>shared-events</artifactId>
    <version>${project.version}</version>
</dependency>
```

### 事件发布示例

```java
// order-service/domain/order/event/OrderPlacedEvent.java
public class OrderPlacedEvent extends DomainEvent {
    private final OrderId orderId;
    private final Money totalAmount;
    private final List<OrderItemSnapshot> items;
    // 事件只含必要数据，不含完整聚合
}

// order-service/infrastructure/messaging/KafkaEventPublisher.java
@Component
public class KafkaEventPublisher implements DomainEventPublisher {
    private final KafkaTemplate<String, String> kafkaTemplate;

    @Override
    public void publish(DomainEvent event) {
        String topic = resolveTopic(event);
        String payload = serializeToJson(event);
        kafkaTemplate.send(topic, payload);
    }
}
```

### 事件订阅示例

```java
// product-service/application/event/handler/OrderPlacedHandler.java
@Component
public class OrderPlacedHandler {

    @KafkaListener(topics = "order.placed")
    public void handle(OrderPlacedEvent event) {
        // 调用领域服务锁定库存
        inventoryDomainService.reserveStock(
            event.getItems().stream()
                .map(i -> new StockReserveCommand(i.getProductId(), i.getQuantity()))
                .toList()
        );
        // 发布 InventoryDeducted 事件到下一环节
        domainEventPublisher.publish(new InventoryDeductedEvent(event.getOrderId()));
    }
}
```

## 关键设计要点

| 要点 | 说明 |
|------|------|
| 领域事件 | Domain 层定义事件（零框架），Infra 层负责发布 |
| 事件总线 | Kafka/RabbitMQ 实现异步解耦 |
| 共享事件 | 独立 shared-events 模块，避免服务间代码重复 |
| Saga 补偿 | 事件驱动 Saga，失败时发布补偿事件回滚 |
| 幂等消费 | 事件处理器检查业务状态，防止重复执行 |
| 事件日志 | Outbox 模式确保事件可靠投递 |

## 优点与局限

| 优点 | 局限 |
|------|------|
| 服务高度解耦 | 事件流追踪困难 |
| 最终一致性保证 | 需要补偿机制处理失败 |
| 可独立演进 | 事件 Schema 需要向前兼容 |
| 弹性伸缩 | 消息中间件运维成本高 |

## 演进路径

```
微服务复杂 → 微服务多模块（11）→ 微服务复杂多模块（12）
```
