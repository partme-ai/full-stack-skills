# Example: 微服务多模块六边形架构

微服务 + Maven 多模块的组合，每个微服务内部按六边形模块拆分，适用于大型团队。

## 场景

核心服务（order-service）内部使用 Maven 多模块，通过编译期约束保证架构边界；同时作为独立服务在 Kubernetes 集群中部署。

## 服务内部模块结构

```
order-service/
├── pom.xml                                              # 父 POM
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── order-domain/                                        # domain 模块
│   ├── pom.xml                                          # 零框架依赖
│   └── src/main/java/com/example/order/domain/
│       ├── model/
│       │   ├── order/Order.java
│       │   ├── order/OrderId.java
│       │   └── payment/Payment.java
│       ├── port/
│       │   ├── inbound/
│       │   │   ├── CreateOrderUseCase.java
│       │   │   └── GetOrderUseCase.java
│       │   └── outbound/
│       │       ├── OrderRepository.java
│       │       ├── PaymentGateway.java
│       │       └── EventPublisher.java
│       └── event/
│           └── OrderCreatedEvent.java
│
├── order-application/                                   # application 模块
│   ├── pom.xml                                          # 依赖 order-domain
│   └── src/main/java/com/example/order/application/
│       ├── service/
│       │   ├── CreateOrderServiceImpl.java
│       │   └── GetOrderServiceImpl.java
│       └── dto/OrderDTO.java
│
├── order-adapter-inbound/                               # 主适配器模块
│   ├── pom.xml                                          # 依赖 order-application + Spring Web
│   └── src/main/java/com/example/order/adapter/inbound/
│       ├── rest/
│       │   └── OrderController.java
│       └── grpc/
│           └── OrderGrpcService.java
│
├── order-adapter-outbound/                              # 次适配器模块
│   ├── pom.xml                                          # 依赖 order-domain + Spring Data/Kafka/Stripe
│   └── src/main/java/com/example/order/adapter/outbound/
│       ├── persistence/
│       │   ├── PostgresOrderRepository.java
│       │   └── entity/OrderJpaEntity.java
│       ├── external/
│       │   └── StripePaymentGateway.java
│       └── messaging/
│           └── KafkaEventPublisher.java
│
├── order-adapter-outbound-inventory/                    # 跨服务适配器模块（可选独立）
│   ├── pom.xml                                          # 依赖 order-domain + gRPC Client
│   └── src/main/java/.../adapter/outbound/microservice/
│       └── GrpcInventoryClient.java
│
└── order-app/                                           # 启动器模块
    ├── pom.xml                                          # 依赖所有模块 + Spring Boot
    └── src/main/java/com/example/order/
        ├── OrderApp.java
        └── config/
            ├── AdapterConfig.java
            └── UseCaseConfig.java
```

## 跨服务调用架构

```
┌───────────────────────────────────────────────────────────┐
│ Kubernetes Cluster                                        │
│                                                           │
│  ┌─ order-service ──────────────────────────────────────┐ │
│  │                                                       │ │
│  │  order-app (启动器)                                   │ │
│  │    ├── order-domain          (端口 + 领域模型)       │ │
│  │    ├── order-application     (UseCase 实现)          │ │
│  │    ├── order-adapter-inbound (REST/gRPC 入口)        │ │
│  │    └── order-adapter-outbound                        │ │
│  │         ├── PostgreSQL                               │ │
│  │         ├── Kafka                                    │ │
│  │         └── Stripe API                               │ │
│  └──────────────────────────────────────────────────────┘ │
│                           │ gRPC                          │
│  ┌─ inventory-service ──┐                                │
│  │  (同样六边形多模块)    │                                │
│  │  domain/application/  │                                │
│  │  adapter-inbound/     │ ← 暴露 gRPC Inventory API     │
│  │  adapter-outbound/    │                                │
│  └───────────────────────┘                                │
│                                                           │
│  ┌─ payment-service ─────┐                                │
│  │  (同样六边形多模块)    │                                │
│  │  domain/application/  │                                │
│  │  adapter-inbound/     │                                │
│  │  adapter-outbound/    │ ← Stripe, PayPal              │
│  └───────────────────────┘                                │
└───────────────────────────────────────────────────────────┘
```

## 模块依赖图（单服务内部）

```
                     ┌──────────────────┐
                     │    order-app     │  ← 依赖所有模块
                     │   (SpringBoot)   │
                     └──┬───┬───┬───┬──┘
                        │   │   │   │
           ┌────────────┼───┼───┼───┼────────────┐
           │            │   │   │   │            │
    ┌──────▼──────┐ ┌───▼───▼───▼───▼───┐ ┌──────▼──────────────┐
    │order-domain │ │order-application  │ │order-adapter-outbound│
    │ (零框架依赖) │ │(只依赖 domain)    │ │(依赖 domain + 框架)  │──────► PostgreSQL
    └──────▲──────┘ └────────▲──────────┘ └────────▲─────────────┘───────► Kafka
           │                │                     │                    ───► Stripe
           │         ┌──────┴──────┐              │
           │         │order-adapter│──────────────┘
           │         │ -inbound    │  (仅注入时依赖 application)
           │         │             │──────► HTTP Client (外部)
           │         └─────────────┘──────► gRPC Server (外部)
           │
    ┌──────┴──────────────┐
    │order-adapter-       │  ← 独立的跨服务调用模块
    │outbound-inventory   │──────► gRPC → inventory-service
    └─────────────────────┘
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 8-20 人/服务 | 大团队需要模块级并行开发 |
| 服务数量 | 5-20 | 多个微服务各用多模块六边形 |
| 模块数量/服务 | 5-7 | domain/application/adapter-in/out/app + 可选 |
| 跨服务通信 | gRPC + Kafka | 同步远程调用 + 异步事件 |
| 领域复杂度 | 中-高 | 多聚合 + Saga |
| 项目生命周期 | 成熟期多团队 | 需要强制架构边界 |

## 关键设计决策

1. **跨服务适配器作为独立模块** — `order-adapter-outbound-inventory` 独立模块，便于 gRPC → REST HTTP 切换
2. **每个服务独立 Git 仓库** — 服务间解耦，独立 CI/CD
3. **共享 Kernel 放在独立库** — 公共 DTO/事件定义用独立 Maven 依赖
4. **app 模块作为组装层** — 不包含业务代码，只负责 DI 和启动

## 构建脚本示例 (order-service/pom.xml)

```xml
<project>
    <groupId>com.example</groupId>
    <artifactId>order-service</artifactId>
    <packaging>pom</packaging>

    <modules>
        <module>order-domain</module>
        <module>order-application</module>
        <module>order-adapter-inbound</module>
        <module>order-adapter-outbound</module>
        <module>order-adapter-outbound-inventory</module>
        <module>order-app</module>
    </modules>
</project>
```

## 对比维度

| 维度 | 单模块微服务 (09/10) | 多模块微服务 (11) |
|------|---------------------|-------------------|
| 构建复杂度 | 低 | 中（每服务 5-7 个 pom.xml） |
| 边界保护 | 约定 | 强制（编译期） |
| 团队并行度 | 模块内 | 模块间 |
| IDE 导入 | 简单 | 需 import multi-module project |
| 新人上手 | 快 | 需要理解多模块结构 |
| 适合团队规模 | 3-8 人 | 8-20 人 |
