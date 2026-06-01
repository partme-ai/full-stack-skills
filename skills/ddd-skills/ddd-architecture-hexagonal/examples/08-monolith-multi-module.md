# Example: 单体多模块六边形架构

Maven 多模块的六边形架构，通过编译期依赖约束强制边界，适用于中大型团队。

## 场景

10-30 人团队、多入口（REST + gRPC + Kafka Consumer）、多外部依赖，需要通过 Maven 模块边界强制依赖规则，防止 Adapter 代码泄漏到 Domain。

## Maven 模块结构

```
order-system/
├── pom.xml                                    # 父 POM（版本管理）
├── order-domain/                              # domain — 零框架依赖
│   ├── pom.xml                                # 仅依赖 Java stdlib + ArchUnit
│   └── src/main/java/com/example/order/domain/
│       ├── model/
│       │   ├── order/
│       │   │   ├── Order.java                 # 聚合根
│       │   │   ├── OrderId.java               # 值对象
│       │   │   ├── OrderItem.java             # 实体
│       │   │   └── OrderStatus.java           # 枚举
│       │   └── payment/
│       │       ├── Payment.java               # 聚合根
│       │       ├── PaymentId.java             # 值对象
│       │       └── PaymentMethod.java         # 值对象
│       ├── service/
│       │   └── OrderPaymentSaga.java          # 领域服务
│       ├── port/
│       │   ├── inbound/
│       │   │   ├── CreateOrderUseCase.java
│       │   │   ├── PayOrderUseCase.java
│       │   │   └── QueryOrderUseCase.java
│       │   └── outbound/
│       │       ├── OrderRepository.java
│       │       ├── PaymentRepository.java
│       │       ├── PaymentGateway.java
│       │       └── EventPublisher.java
│       └── event/
│           ├── OrderCreatedEvent.java
│           └── PaymentCompletedEvent.java
│
├── order-application/                         # application — 仅依赖 domain
│   ├── pom.xml                                # 依赖 order-domain
│   └── src/main/java/com/example/order/application/
│       └── service/
│           ├── CreateOrderServiceImpl.java    # implements CreateOrderUseCase
│           ├── PayOrderServiceImpl.java       # implements PayOrderUseCase
│           └── QueryOrderServiceImpl.java     # implements QueryOrderUseCase
│
├── order-adapter-inbound/                     # 主适配器 — 依赖 application
│   ├── pom.xml                                # 依赖 order-application + Spring Web/gRPC
│   └── src/main/java/com/example/order/adapter/inbound/
│       ├── rest/
│       │   └── OrderController.java
│       ├── grpc/
│       │   └── OrderGrpcService.java
│       └── kafka/
│       │   └── OrderKafkaConsumer.java        # Kafka 驱动入口
│       └── dto/
│           ├── CreateOrderRequest.java
│           └── OrderResponse.java
│
├── order-adapter-outbound/                    # 次适配器 — 依赖 domain
│   ├── pom.xml                                # 依赖 order-domain + Spring Data JPA/Kafka/Stripe
│   └── src/main/java/com/example/order/adapter/outbound/
│       ├── persistence/
│       │   ├── PostgresOrderRepository.java
│       │   ├── PostgresPaymentRepository.java
│       │   ├── entity/
│       │   │   ├── OrderJpaEntity.java
│       │   │   └── PaymentJpaEntity.java
│       │   └── mapper/
│       │       ├── OrderMapper.java
│       │       └── PaymentMapper.java
│       ├── external/
│       │   └── StripePaymentGateway.java
│       └── messaging/
│           └── KafkaEventPublisher.java
│
└── order-app/                                 # 启动器 — 依赖所有模块
    ├── pom.xml                                # 依赖全部子模块 + Spring Boot
    └── src/main/java/com/example/order/
        ├── OrderApplication.java              # @SpringBootApplication
        └── configuration/
            └── AdapterConfig.java             # DI 装配
```

## 模块依赖图

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  order-app (启动器)                                 │
│    ↓        ↓         ↓          ↓                  │
│  domain  application adapter-in adapter-out         │
│                                                     │
└─────────────────────────────────────────────────────┘

order-domain               ← 零框架依赖（只依赖 Java stdlib）
    ↑
    │ 编译期依赖
order-application          ← 只依赖 order-domain
    ↑                       ↑
    │                       │
order-adapter-inbound      │  ← 依赖 order-application + Spring MVC/gRPC
    │                       │
    └── order-adapter-outbound ← 依赖 order-domain + Spring Data/Kafka/Stripe
```

```
Maven 依赖关系（pom.xml 约束）:

order-domain:          无内部依赖
order-application:     order-domain
order-adapter-inbound: order-application + Spring Web + Spring gRPC
order-adapter-outbound: order-domain + Spring Data JPA + Kafka Client + Stripe SDK
order-app:             order-adapter-inbound + order-adapter-outbound + Spring Boot
```

## 编译期边界验证

```java
// order-domain/pom.xml — 零框架依赖宣言
<dependencies>
    <!-- 仅 Java 标准库 + 测试框架 -->
    <dependency>
        <groupId>com.tngtech.archunit</groupId>
        <artifactId>archunit-junit5</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

```java
// ArchUnit 测试 — 验证 domain 模块纯净度
@AnalyzeClasses(packages = "com.example.order.domain")
class DomainPurityTest {
    @ArchTest
    static final ArchRule no_framework_dependency = noClasses()
        .should().dependOnClassesThat()
        .resideInAnyPackage(
            "org.springframework..",
            "jakarta.persistence..",
            "com.fasterxml.."
        );
}
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 10-30 人 | 需要编译期依赖约束 |
| 入口数量 | 3+ (REST/gRPC/Kafka) | 多入口分别独立模块 |
| 外部依赖 | 5+ | 次适配器独立模块便于替换 |
| 领域复杂度 | 中-高 | 多聚合，通过模块边界强制隔离 |
| 项目生命周期 | 成熟期 | 架构已稳定，需要强制而非建议的边界 |

## 关键设计决策

1. **domain 模块零框架依赖** — 通过 pom.xml 不引入 Spring/JPA，辅以 ArchUnit 测试验证
2. **application 只依赖 domain** — 不依赖任何框架和适配器模块
3. **adapter-inbound 和 adapter-outbound 独立** — 主/次适配器各自独立模块，可独立演进
4. **order-app 作为组装层** — 唯一包含 @SpringBootApplication 和 DI 配置的模块

## 对比单模块

| 维度 | 单模块六边形 (06) | 多模块六边形 (08) |
|------|-------------------|-------------------|
| 构建复杂度 | 低 | 中（需管理 5 个 pom.xml） |
| 边界保护 | 约定（包名） | 强制（编译期） |
| 团队并行开发 | 易冲突 | 模块级独立开发 |
| 新人学习成本 | 低 | 中（需理解模块结构） |
| 适合团队 | 1-5 人 | 10-30 人 |
