# 微服务复杂多模块 — 共享 Kernel DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 20-60 人，多个领域专家团队 |
| 业务复杂度 | 极高，多子域 + 复杂事件驱动 + 共享领域概念 |
| 部署方式 | Docker/K8s，每服务独立部署，CI/CD 流水线 |
| 技术栈 | Spring Boot + Spring Cloud + Kafka + MyBatis/JPA + Docker Compose |
| 通信方式 | REST（同步查询/命令）+ 异步事件（Kafka）+ gRPC（高性能场景） |

**典型业务**：超大型电商平台、银行核心系统、保险理赔平台、供应链管理系统。

本架构是 DDD 分层落地的最完整形态：微服务拆分 + 每服务多模块 + 共享 Kernel（核心领域概念共享）+ 事件驱动。

## 目录树

```
ecommerce-platform/
├── pom.xml                                    # 根聚合 POM（dependencyManagement）
├── docker-compose.yml
├── README.md
│
├── shared-kernel/                             # ★ 共享内核
│   ├── pom.xml
│   └── src/main/java/com/example/shared/
│       ├── kernel/
│       │   ├── BaseEntity.java                # 实体基类
│       │   ├── AggregateRoot.java             # 聚合根基类
│       │   ├── ValueObject.java               # 值对象基类
│       │   ├── DomainEvent.java               # 领域事件基类
│       │   ├── Identifier.java                # 标识符基类
│       │   └── BusinessException.java         # 业务异常基类
│       ├── model/                             # 共享领域模型
│       │   ├── Money.java                     # 通用 Money 值对象
│       │   ├── Address.java                   # 通用地址值对象
│       │   ├── PhoneNumber.java               # 通用电话号码
│       │   └── PageResult.java                # 通用分页结果
│       ├── event/                             # 共享事件 Schema
│       │   ├── OrderPlacedEvent.java
│       │   ├── OrderConfirmedEvent.java
│       │   ├── OrderCancelledEvent.java
│       │   ├── InventoryDeductedEvent.java
│       │   ├── InventoryReleasedEvent.java
│       │   ├── PaymentCompletedEvent.java
│       │   └── ShipmentCreatedEvent.java
│       └── annotation/                        # 共享标注
│           ├── DomainService.java
│           ├── Repository.java
│           └── Factory.java
│
├── order-service/                             # 订单微服务（多模块 + 事件驱动）
│   ├── pom.xml
│   ├── order-interface/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/interface/
│   │       ├── controller/
│   │       │   ├── OrderCommandController.java    # 命令类 API
│   │       │   └── OrderQueryController.java      # 查询类 API（CQRS）
│   │       ├── dto/
│   │       │   ├── request/
│   │       │   │   ├── CreateOrderRequest.java
│   │       │   │   ├── CancelOrderRequest.java
│   │       │   │   └── OrderQueryRequest.java
│   │       │   └── response/
│   │       │       ├── OrderResponse.java
│   │       │       └── OrderDetailResponse.java
│   │       └── converter/
│   │           └── OrderDtoConverter.java
│   ├── order-application/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/application/
│   │       ├── service/
│   │       │   ├── OrderCommandService.java       # 命令服务（写）
│   │       │   └── OrderQueryService.java         # 查询服务（读）
│   │       ├── command/
│   │       │   ├── CreateOrderCommand.java
│   │       │   └── CancelOrderCommand.java
│   │       ├── query/
│   │       │   ├── OrderDetailQuery.java
│   │       │   └── OrderListQuery.java
│   │       ├── assembler/
│   │       │   └── OrderAssembler.java
│   │       ├── event/
│   │       │   └── handler/
│   │       │       ├── PaymentCompletedHandler.java
│   │       │       ├── ShipmentCreatedHandler.java
│   │       │       └── InventoryDeductedHandler.java
│   │       └── saga/                              # Saga 编排
│   │           ├── CreateOrderSaga.java
│   │           └── CancelOrderSaga.java
│   ├── order-domain/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/domain/
│   │       ├── order/
│   │       │   ├── entity/
│   │       │   │   ├── Order.java                 # 聚合根
│   │       │   │   └── OrderItem.java             # 实体
│   │       │   ├── valueobject/
│   │       │   │   ├── OrderId.java
│   │       │   │   ├── OrderStatus.java
│   │       │   │   └── OrderItemId.java
│   │       │   ├── service/
│   │       │   │   ├── OrderDomainService.java
│   │       │   │   └── OrderPricingService.java
│   │       │   ├── repository/
│   │       │   │   ├── OrderRepository.java
│   │       │   │   └── OrderReadRepository.java   # CQRS 读仓储
│   │       │   ├── event/
│   │       │   │   ├── OrderPlacedEvent.java
│   │       │   │   ├── OrderConfirmedEvent.java
│   │       │   │   └── OrderCancelledEvent.java
│   │       │   └── specification/                 # 规约模式
│   │       │       ├── OrderByStatusSpec.java
│   │       │       └── OrderByCustomerSpec.java
│   │       └── readmodel/                         # CQRS 读模型
│   │           └── OrderSummary.java
│   ├── order-infrastructure/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/infrastructure/
│   │       ├── repository/
│   │       │   ├── MyBatisOrderRepository.java
│   │       │   └── ElasticsearchOrderReadRepository.java
│   │       ├── persistence/
│   │       │   ├── po/
│   │       │   │   ├── OrderPO.java
│   │       │   │   └── OrderItemPO.java
│   │       │   └── converter/
│   │       │       └── OrderPersistenceConverter.java
│   │       ├── messaging/
│   │       │   ├── publisher/
│   │       │   │   └── KafkaEventPublisher.java
│   │       │   ├── subscriber/
│   │       │   │   └── KafkaEventSubscriber.java
│   │       │   └── outbox/                        # Outbox 模式
│   │       │       ├── EventOutbox.java
│   │       │       └── OutboxPublisher.java
│   │       ├── external/
│   │       │   ├── ProductServiceClient.java
│   │       │   └── PaymentServiceClient.java
│   │       └── config/
│   │           ├── RepositoryConfig.java
│   │           ├── KafkaConfig.java
│   │           └── CacheConfig.java
│   └── order-bootstrap/
│       ├── pom.xml
│       └── src/main/java/com/example/order/
│           └── OrderServiceApplication.java
│
├── product-service/                           # 商品微服务（多模块 + 事件驱动）
│   ├── pom.xml
│   ├── product-interface/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/interface/
│   │       ├── controller/
│   │       │   ├── ProductCommandController.java
│   │       │   └── ProductQueryController.java
│   │       ├── dto/
│   │       └── converter/
│   ├── product-application/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/application/
│   │       ├── service/
│   │       │   ├── ProductCommandService.java
│   │       │   └── ProductQueryService.java
│   │       ├── command/
│   │       ├── query/
│   │       ├── event/handler/
│   │       │   ├── OrderPlacedHandler.java
│   │       │   └── OrderCancelledHandler.java
│   │       └── saga/
│   │           └── ReserveStockSaga.java
│   ├── product-domain/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/domain/
│   │       ├── product/
│   │       │   ├── entity/
│   │       │   │   ├── Product.java
│   │       │   │   └── Category.java
│   │       │   ├── valueobject/
│   │       │   │   ├── ProductId.java
│   │       │   │   ├── Price.java
│   │       │   │   ├── Sku.java
│   │       │   │   └── Stock.java
│   │       │   ├── service/
│   │       │   │   └── InventoryDomainService.java
│   │       │   ├── repository/
│   │       │   │   ├── ProductRepository.java
│   │       │   │   └── ProductReadRepository.java
│   │       │   └── event/
│   │       │       ├── InventoryDeductedEvent.java
│   │       │       └── InventoryReleasedEvent.java
│   │       └── readmodel/
│   │           └── ProductSummary.java
│   ├── product-infrastructure/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/infrastructure/
│   │       ├── repository/
│   │       │   ├── MyBatisProductRepository.java
│   │       │   └── RedisProductReadRepository.java
│   │       ├── persistence/
│   │       │   ├── po/
│   │       │   │   ├── ProductPO.java
│   │       │   │   └── CategoryPO.java
│   │       │   └── converter/
│   │       │       └── ProductPersistenceConverter.java
│   │       ├── messaging/
│   │       │   ├── publisher/
│   │       │   │   └── KafkaEventPublisher.java
│   │       │   ├── subscriber/
│   │       │   │   └── KafkaEventSubscriber.java
│   │       │   └── outbox/
│   │       │       └── EventOutbox.java
│   │       └── config/
│   │           ├── RepositoryConfig.java
│   │           ├── KafkaConfig.java
│   │           └── RedisConfig.java
│   └── product-bootstrap/
│       ├── pom.xml
│       └── src/main/java/com/example/product/
│           └── ProductServiceApplication.java
│
├── payment-service/                           # 支付微服务（多模块 + 事件驱动）
│   ├── pom.xml
│   ├── payment-interface/
│   ├── payment-application/
│   │   ├── service/
│   │   ├── event/handler/
│   │   │   ├── OrderConfirmedHandler.java
│   │   │   └── InventoryDeductedHandler.java
│   │   └── saga/
│   │       └── PaymentSaga.java
│   ├── payment-domain/
│   │   └── payment/
│   │       ├── entity/
│   │       │   └── Payment.java
│   │       ├── valueobject/
│   │       │   ├── PaymentId.java
│   │       │   ├── PaymentMethod.java
│   │       │   └── PaymentStatus.java
│   │       ├── service/
│   │       │   └── PaymentDomainService.java
│   │       ├── repository/
│   │       │   └── PaymentRepository.java
│   │       └── event/
│   │           ├── PaymentInitiatedEvent.java
│   │           ├── PaymentCompletedEvent.java
│   │           └── PaymentRefundedEvent.java
│   ├── payment-infrastructure/
│   │   ├── repository/
│   │   │   └── MyBatisPaymentRepository.java
│   │   ├── persistence/
│   │   ├── messaging/
│   │   │   ├── publisher/
│   │   │   ├── subscriber/
│   │   │   └── outbox/
│   │   ├── external/
│   │   │   └── AlipayClient.java
│   │   └── config/
│   └── payment-bootstrap/
│
├── notification-service/
│   ├── pom.xml
│   ├── notification-interface/
│   ├── notification-application/
│   │   └── event/handler/
│   │       ├── OrderPlacedHandler.java
│   │       ├── PaymentCompletedHandler.java
│   │       └── ShipmentCreatedHandler.java
│   ├── notification-domain/
│   │   └── notification/
│   │       ├── entity/
│   │       │   └── Notification.java
│   │       ├── valueobject/
│   │       │   ├── NotificationType.java
│   │       │   └── NotificationChannel.java
│   │       └── repository/
│   │           └── NotificationRepository.java
│   ├── notification-infrastructure/
│   │   ├── repository/
│   │   ├── messaging/
│   │   │   └── subscriber/
│   │   ├── external/
│   │   │   ├── SmsClient.java
│   │   │   ├── EmailClient.java
│   │   │   └── PushClient.java
│   │   └── config/
│   └── notification-bootstrap/
│
├── api-gateway/                               # API 网关
│   ├── pom.xml
│   └── src/main/java/com/example/gateway/
│       ├── GatewayApplication.java
│       ├── filter/
│       │   ├── AuthFilter.java
│       │   └── RateLimitFilter.java
│       └── route/
│           └── RouteConfig.java
│
└── infrastructure/                            # 共享基础设施
    ├── pom.xml
    └── src/main/java/com/example/infra/
        ├── monitoring/
        │   ├── MetricsCollector.java
        │   └── HealthIndicator.java
        ├── tracing/
        │   └── TraceIdFilter.java
        └── logging/
            └── AuditLogger.java
```

## 包结构

```
com.example.shared.kernel   — 共享内核（基类 + 共享值对象 + 事件 Schema）
com.example.shared.model    — 共享领域模型
com.example.shared.event    — 共享事件定义
com.example.order.{layer}   — 订单服务四层
com.example.product.{layer} — 商品服务四层
com.example.payment.{layer} — 支付服务四层
com.example.notification.{layer} — 通知服务四层
com.example.infra           — 共享基础设施（监控/追踪/日志）
```

## 模块依赖

### 整体依赖关系图

```
              ┌─────────────────────┐
              │   shared-kernel     │  （基类/值对象/事件 Schema）
              └──────┬──────────────┘
                     │
    ┌────────────────┼────────────────────────┐
    │                │                        │
    ▼                ▼                        ▼
order-domain   product-domain         payment-domain
    │                │                        │
    ▼                ▼                        ▼
order-infra    product-infra          payment-infra
    │                │                        │
    ▼                ▼                        ▼
order-app      product-app             payment-app
    │                │                        │
    ▼                ▼                        ▼
order-interface product-interface  payment-interface
    │                │                        │
    ▼                ▼                        ▼
order-bootstrap product-bootstrap  payment-bootstrap
    │                │                        │
    └────────────────┼────────────────────────┘
                     │
                     ▼
               ┌──────────┐
               │  gateway │
               └──────────┘
```

### shared-kernel/pom.xml

```xml
<artifactId>shared-kernel</artifactId>
<dependencies>
    <!-- 零框架依赖，仅 JDK。只包含纯领域概念和标注 -->
</dependencies>
```

### 各服务 Domain 模块依赖 shared-kernel

```xml
<!-- order-domain/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>shared-kernel</artifactId>
    </dependency>
</dependencies>
```

### 根 POM 关键配置

```xml
<groupId>com.example</groupId>
<artifactId>ecommerce-platform</artifactId>
<version>1.0.0</version>
<packaging>pom</packaging>

<modules>
    <module>shared-kernel</module>
    <module>shared-infrastructure</module>
    <module>order-service</module>
    <module>product-service</module>
    <module>payment-service</module>
    <module>notification-service</module>
    <module>api-gateway</module>
</modules>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>2023.0.2</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
        <!-- 内部模块版本统一 -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>shared-kernel</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>shared-infrastructure</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## CQRS 读写分离（订单服务示例）

```
写模型（Command）                      读模型（Query）
─────────────────                    ─────────────────
interface/controller/                interface/controller/
  OrderCommandController.java          OrderQueryController.java
       │                                     │
application/service/                  application/service/
  OrderCommandService.java              OrderQueryService.java
       │                                     │
domain/order/entity/                   domain/readmodel/
  Order.java (聚合根)                    OrderSummary.java (DTO)
       │                                     │
domain/order/repository/               domain/order/repository/
  OrderRepository.java                   OrderReadRepository.java
       │                                     │
infrastructure/repository/             infrastructure/repository/
  MyBatisOrderRepository.java            ElasticsearchOrderReadRepo.java
       │                                     │
  [MySQL 主库]                            [Elasticsearch 从库]
```

## 关键设计要点

| 要点 | 说明 |
|------|------|
| Shared Kernel | 共享基类、通用值对象、事件 Schema，所有 Domain 模块依赖 |
| CQRS | 写操作走 MySQL + 聚合根，读操作走 ES/Redis + ReadModel |
| Saga 编排 | Application 层 Saga 类管理跨服务长事务补偿 |
| Outbox 模式 | Infra 层 EventOutbox 保证事件可靠投递 |
| 规约模式 | Domain 层 Specification 封装查询条件 |
| 防腐层 | Infra 层 external 包封装所有外部服务调用 |
| 共享基础设施 | 监控/追踪/日志统一模块，各服务可选依赖 |
| 独立部署 | 每个 bootstrap 模块生成独立 Docker 镜像 |

## 优点与局限

| 优点 | 局限 |
|------|------|
| 最完整的 DDD 分层落地 | 学习曲线最陡 |
| 编译期强制架构约束 | 模块数量极多（4 服务 × 5 子模块 = 20+） |
| 支持超大规模团队并行 | 构建时间可能很长 |
| Shared Kernel 减少重复 | Shared Kernel 变更需多方协调 |
| CQRS 读写性能优化 | CQRS 增加运维复杂度（ES/缓存集群） |
| Saga 保证最终一致性 | Saga 补偿逻辑复杂，需充分测试 |
| 每层可独立替换和测试 | 不适合简单 CRUD 项目 |

## 典型事件 Saga 示例

```
CreateOrderSaga（Application 层）:
  Step 1: 创建订单（Order Domain）
  Step 2: 发布 OrderPlacedEvent → Product 服务锁定库存
  Step 3: Product 发布 InventoryDeductedEvent → Payment 服务发起支付
  Step 4: Payment 发布 PaymentCompletedEvent → Order 服务确认订单
  Step 5: Order 发布 OrderConfirmedEvent → Notification 服务发送通知

  补偿:
  - Step 2 失败 → Order 取消
  - Step 3 失败 → Product 释放库存 + Order 取消
  - Step 4 失败 → Payemnt 退款 + Product 释放库存 + Order 取消
```

## 项目规模对照表

| 项目 | 模块数 | 团队 | 部署单元 | 复杂度 |
|------|--------|------|----------|--------|
| 06 单体简单 | 1 | 3-8 | 1 JAR | ★ |
| 07 单体复杂 | 1 | 5-15 | 1 JAR | ★★ |
| 08 单体多模块 | 5 | 8-20 | 1 JAR | ★★★ |
| 09 微服务简单 | ~4 | 10-30 | N JAR | ★★★ |
| 10 微服务复杂 | ~5 | 15-40 | N JAR | ★★★★ |
| 11 微服务多模块 | ~15 | 15-40 | N JAR | ★★★★★ |
| **12 微服务复杂多模块** | **20+** | **20-60** | **N JAR** | **★★★★★★** |

选择建议：根据**团队规模、业务复杂度、未来演进方向**选取匹配的项目结构，渐进式演进而非一步到位。
