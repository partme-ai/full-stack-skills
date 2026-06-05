# Example 09 — 微服务简单规模（Microservice Simple）

> 单个微服务内部应用洋葱架构。每个微服务独立部署，服务间通过 API 调用或消息通信。适合 3-5 人团队负责一个服务。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 3-5 人（一个微服务团队） |
| 限界上下文 | 1 个 = 1 个微服务 |
| 部署单元 | 独立容器化部署 |
| 数据库 | 每个服务独立 Database |
| 通信方式 | REST/gRPC（同步）+ Kafka（异步） |

## 目录树

```
order-service/                                 # 订单微服务
├── docker-compose.yml                         # 本地开发环境
├── Dockerfile
├── pom.xml
├── src/main/java/com/example/order/
│   ├── core/
│   │   ├── domain/                            # Domain 层
│   │   │   ├── model/
│   │   │   │   ├── Order.java
│   │   │   │   ├── OrderId.java
│   │   │   │   ├── OrderItem.java
│   │   │   │   └── OrderStatus.java
│   │   │   ├── service/
│   │   │   │   └── PricingService.java
│   │   │   ├── repository/
│   │   │   │   └── OrderRepository.java
│   │   │   └── event/
│   │   │       ├── OrderCreatedEvent.java
│   │   │       └── OrderPaidEvent.java
│   │   └── application/                       # Application 层
│   │       ├── service/
│   │       │   ├── PlaceOrderUseCase.java
│   │       │   └── impl/PlaceOrderService.java
│   │       ├── command/
│   │       │   └── PlaceOrderCommand.java
│   │       └── dto/
│   │           └── OrderDTO.java
│   ├── infrastructure/                        # Infrastructure 层
│   │   ├── data/
│   │   │   ├── entity/OrderPO.java
│   │   │   ├── repository/OrderRepositoryImpl.java
│   │   │   └── mapper/OrderMapper.java
│   │   ├── external/
│   │   │   ├── ProductServiceClient.java       # 调用商品服务 API
│   │   │   └── PaymentServiceClient.java       # 调用支付服务 API
│   │   ├── messaging/
│   │   │   ├── KafkaConfig.java
│   │   │   ├── OrderEventPublisher.java
│   │   │   └── ProductEventListener.java      # 监听商品变更事件
│   │   └── config/
│   │       └── ServiceClientConfig.java
│   ├── api/                                   # API 层
│   │   ├── controller/
│   │   │   └── OrderController.java
│   │   ├── dto/
│   │   │   ├── request/CreateOrderRequest.java
│   │   │   └── response/OrderResponse.java
│   │   └── assembler/
│   │       └── OrderDTOAssembler.java
│   └── composition/                           # Composition 层
│       ├── OrderServiceApplication.java       # Spring Boot 入口
│       └── config/
│           └── OrderServiceConfig.java
│
└── src/test/
    └── java/com/example/order/
        ├── core/domain/model/OrderTest.java
        ├── core/application/PlaceOrderServiceTest.java
        └── integration/OrderServiceIT.java
```

## 微服务间依赖方向

```
┌──────────────┐     REST/gRPC      ┌──────────────┐
│ order-service│ ──────────────────→│product-service│
│              │←─ OrderCreated ─── │              │
└──────┬───────┘    (Kafka)         └──────────────┘
       │
       │ REST/gRPC
       ▼
┌──────────────┐
│payment-service│
│              │
└──────────────┘

★ 服务间通过 API Contract / Protobuf / Avro Schema 定义接口
★ 服务间仅通过 ID 引用对方的实体
★ 跨服务事务：Saga 模式（编排/协同）
```

## 服务内部依赖方向

```
composition → api / infrastructure → application → domain ★
                                               ↑
             Kafka Event (外部消息) ────────────┘
             REST/gRPC Request ─────────────────┘
```

**注意**：微服务内部的洋葱架构与单体完全相同，外部的分布式通信不影响内部结构。

## 微服务特有配置

```java
// infrastructure/external/ProductServiceClient.java
@Component
public class ProductServiceClient {
    private final RestTemplate restTemplate;

    // 调用其他微服务时，Application 层通过 Domain 接口调用
    public ProductInfo getProductInfo(ProductId productId) {
        return restTemplate.getForObject(
            "http://product-service/api/products/{id}",
            ProductInfo.class, productId.getValue()
        );
    }
}

// infrastructure/messaging/ProductEventListener.java
@Component
public class ProductEventListener {
    @KafkaListener(topics = "product-events")
    public void handleProductEvent(ProductEvent event) {
        // 维护本地缓存或投影，避免实时调用
        if (event instanceof ProductRemovedEvent) {
            // 标记相关订单
        }
    }
}
```

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| 服务内部洋葱合规 | ✅ | Domain 层零框架依赖 |
| 服务间接口契约 | ✅ | ProductServiceClient 基于 API Contract |
| 数据库独立 | ✅ | 每个服务独立 Database |
| 跨服务事务 Saga | ⚠️ | 需要实现补偿逻辑 |
| 服务发现与负载均衡 | ⚠️ | 基础设施层处理 |

## 何时选择此结构

- 微服务数量 < 10，每服务团队 < 5 人
- 每服务业务独立性强，变化频率不同
- 需要独立部署和扩缩容
- 团队已有容器化和服务治理经验
