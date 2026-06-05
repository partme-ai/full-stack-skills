# Example 08 — 单体多模块规模（Monolith Multi-Module）

> Maven/Gradle 多模块单体。将洋葱各层拆分为独立 Maven 模块（domain/app/infra/api/composition），通过模块依赖强制执行分层规则。适合 5-12 人团队、需要编译期强制依赖约束。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 5-12 人 |
| 限界上下文 | 2-3 个 |
| 部署单元 | 1 个 Spring Boot JAR |
| 数据库 | 1 个 RDBMS |
| 模块数 | 5-15 个 Maven 模块 |

## 目录树

```
ecommerce/
├── pom.xml                                    # 父 POM（版本管理）
├── ecommerce-domain/                          # ★ Module: domain（零框架依赖）
│   ├── pom.xml                                # 不依赖 Spring Boot
│   └── src/main/java/com/example/ec/domain/
│       ├── model/
│       │   ├── order/
│       │   │   ├── Order.java                 # 聚合根
│       │   │   ├── OrderId.java
│       │   │   ├── OrderItem.java
│       │   │   └── OrderStatus.java
│       │   ├── product/
│       │   │   ├── Product.java
│       │   │   └── ProductId.java
│       │   └── shared/
│       │       ├── Money.java
│       │       └── ValueObject.java
│       ├── service/
│       │   └── PricingService.java            # 领域服务接口
│       ├── repository/
│       │   ├── OrderRepository.java           # 仓储接口
│       │   └── ProductRepository.java
│       └── event/
│           ├── DomainEvent.java
│           └── OrderPlacedEvent.java
│
├── ecommerce-application/                     # ★ Module: application（编排层）
│   ├── pom.xml                                # 仅依赖 domain 模块
│   └── src/main/java/com/example/ec/application/
│       ├── service/
│       │   ├── PlaceOrderUseCase.java         # 应用服务接口
│       │   └── ProductQueryService.java
│       ├── command/
│       │   └── PlaceOrderCommand.java
│       └── dto/
│           ├── OrderDTO.java
│           └── ProductDTO.java
│
├── ecommerce-infrastructure/                  # ★ Module: infrastructure
│   ├── pom.xml                                # 依赖 domain + application
│   └── src/main/java/com/example/ec/infra/
│       ├── data/
│       │   ├── entity/
│       │   │   ├── OrderPO.java               # JPA Entity
│       │   │   └── ProductPO.java
│       │   ├── repository/
│       │   │   ├── OrderRepositoryImpl.java
│       │   │   └── ProductRepositoryImpl.java
│       │   ├── mapper/
│       │   │   └── EntityDomainMapper.java
│       │   └── config/
│       │       └── JpaConfig.java
│       ├── messaging/
│       │   ├── KafkaConfig.java
│       │   └── KafkaEventPublisher.java
│       └── external/
│           └── PaymentGatewayClient.java
│
├── ecommerce-api-rest/                        # ★ Module: API（REST 适配器）
│   ├── pom.xml                                # 依赖 domain + application + infra
│   └── src/main/java/com/example/ec/api/
│       ├── controller/
│       │   ├── OrderController.java
│       │   └── ProductController.java
│       ├── dto/
│       │   ├── request/
│       │   │   └── PlaceOrderRequest.java
│       │   └── response/
│       │       └── OrderResponse.java
│       ├── assembler/
│       │   └── OrderAssembler.java
│       └── advice/
│           └── GlobalExceptionHandler.java
│
├── ecommerce-api-grpc/                        # ★ Module: API（gRPC 适配器，可选）
│   ├── pom.xml
│   └── src/main/java/.../
│       └── proto/
│           └── OrderServiceGrpc.java
│
├── ecommerce-api-mq/                          # ★ Module: API（MQ 适配器，可选）
│   ├── pom.xml
│   └── src/main/java/.../
│       └── listener/
│           └── OrderEventListener.java
│
└── ecommerce-composition/                     # ★ Module: composition（DI 根）
    ├── pom.xml                                # 依赖所有模块
    └── src/main/java/com/example/ec/
        ├── CompositionApp.java                # Spring Boot 启动类
        └── config/
            ├── OrderModuleConfig.java
            ├── ProductModuleConfig.java
            └── MessagingConfig.java
```

## 模块依赖图

```
┌────────────────────────────────────────────┐
│          ecommerce-composition/             │ ← Spring Boot 启动 + DI 组装
└───┬────────┬──────────┬──────────┬─────────┘
    │        │          │          │
    ▼        ▼          ▼          ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────────────┐
│api-  │ │api-  │ │api-  │ │infrastructure│
│rest  │ │grpc  │ │mq    │ │              │
└──┬───┘ └──┬───┘ └──┬───┘ └──────┬───────┘
   │        │        │            │
   └────────┼────────┴────────────┘
            ▼
┌──────────────────────┐
│ecommerce-application/│ ← 编排层
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  ecommerce-domain/   │ ★ 核心（零框架依赖）
└──────────────────────┘
```

**关键约束**：多模块通过 Maven `<dependency>` 强制执行：
- `domain` 不依赖任何其他模块
- `application` 仅依赖 `domain`
- `infrastructure` 依赖 `domain`，实现其接口
- `api-*` 依赖 `domain` + `application` + `infrastructure`
- `composition` 依赖所有模块

## Maven 父 POM 示例

```xml
<modules>
    <module>ecommerce-domain</module>
    <module>ecommerce-application</module>
    <module>ecommerce-infrastructure</module>
    <module>ecommerce-api-rest</module>
    <module>ecommerce-api-grpc</module>
    <module>ecommerce-api-mq</module>
    <module>ecommerce-composition</module>
</modules>
```

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| domain 模块零 Spring 依赖 | ✅ | pom.xml 中无 spring-boot-starter |
| application 仅依赖 domain | ✅ | Maven 依赖可视 |
| 编译期强制执行分层 | ✅ | 逆向依赖 = 编译失败 |
| API 适配器可插拔 | ✅ | rest/grpc/mq 各自独立模块 |
| DI 集中组装 | ✅ | composition 模块统筹 |

## 何时选择此结构

- 需要编译期强制执行分层规则（防止团队成员引入逆向依赖）
- 多入口系统：REST + gRPC + MQ 消费者
- 大型团队，需要严格模块边界
- 基础设施可能切换（DB/消息队列/缓存）

## 风险提示

- 模块过多增加 Maven 构建复杂度
- domain 模块变更 → 需要 rebuild 所有下游模块
- 过度拆分导致每个模块代码量过少
- composition 模块可能成为"大泥球"（所有配置集中）
