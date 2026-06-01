# Example 11 — 微服务多模块规模（Microservice Multi-Module）

> 单个微服务内部采用 Maven 多模块拆分洋葱各层。编译期强制执行分层约束，适合对代码质量要求严格的大团队。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 4-8 人（一个服务团队） |
| 限界上下文 | 1 个（= 1 个微服务） |
| 部署单元 | 独立容器化部署 |
| 模块数 | 4-7 个 Maven 模块 / 微服务 |
| 代码规范 | 编译期强制分层 |

## 目录树

```
order-service/
├── pom.xml                                    # 父 POM
├── order-domain/                              # Module 1: 领域层
│   ├── pom.xml
│   └── src/main/java/.../
│       ├── model/
│       │   ├── Order.java
│       │   ├── OrderId.java
│       │   └── OrderItem.java
│       ├── repository/
│       │   └── OrderRepository.java            # 仓储接口
│       ├── service/
│       │   └── PricingService.java
│       ├── event/
│       │   ├── OrderCreatedEvent.java
│       │   └── OrderPaidEvent.java
│       └── external/
│           └── ProductService.java             # 外部服务接口
│
├── order-application/                         # Module 2: 应用层
│   ├── pom.xml                                # 仅依赖 order-domain
│   └── src/main/java/.../
│       ├── service/
│       │   ├── PlaceOrderUseCase.java
│       │   └── impl/PlaceOrderService.java
│       ├── command/
│       │   └── PlaceOrderCommand.java
│       ├── query/
│       │   └── OrderQueryService.java
│       └── dto/
│           └── OrderDTO.java
│
├── order-infrastructure/                      # Module 3: 基础设施层
│   ├── pom.xml                                # 依赖 domain + application
│   └── src/main/java/.../
│       ├── data/
│       │   ├── entity/OrderPO.java
│       │   ├── repository/OrderRepositoryImpl.java
│       │   ├── mapper/OrderMapper.java
│       │   └── config/JpaConfig.java
│       ├── messaging/
│       │   ├── KafkaConfig.java
│       │   └── KafkaOrderEventPublisher.java
│       └── client/
│           └── ProductServiceClient.java
│
├── order-api-rest/                            # Module 4: REST API
│   ├── pom.xml                                # 依赖 domain + app + infra
│   └── src/main/java/.../
│       ├── controller/
│       │   └── OrderController.java
│       ├── dto/
│       │   ├── request/CreateOrderRequest.java
│       │   └── response/OrderResponse.java
│       ├── assembler/
│       │   └── OrderAssembler.java
│       └── advice/
│           └── OrderExceptionHandler.java
│
├── order-api-grpc/                            # Module 5: gRPC API（可选）
│   ├── pom.xml
│   └── src/main/java/.../
│       └── service/
│           └── OrderGrpcService.java
│
├── order-api-mq/                              # Module 6: MQ Consumer API（可选）
│   ├── pom.xml
│   └── src/main/java/.../
│       └── listener/
│           └── PaymentEventListener.java
│
└── order-composition/                         # Module 7: DI 根
    ├── pom.xml                                # 依赖所有模块
    └── src/main/java/.../
        ├── OrderServiceApplication.java       # Spring Boot 入口
        └── config/
            ├── DomainConfig.java
            ├── InfrastructureConfig.java
            └── ApiConfig.java
```

## 模块依赖图

```
┌────────────────────────────────────────────┐
│         order-composition                   │ ← 启动入口 + DI 根
└──┬───────┬─────────┬───────────┬───────────┘
   │       │         │           │
   ▼       ▼         ▼           ▼
┌─────┐ ┌─────┐ ┌─────┐ ┌────────────────┐
│rest │ │grpc │ │ mq  │ │ infrastructure │
│api  │ │api  │ │api  │ │                │
└──┬──┘ └──┬──┘ └──┬──┘ └───────┬────────┘
   │       │       │            │
   └───────┴───────┴────────────┘
                │
                ▼
┌────────────────────────────┐
│   order-application         │ ← 仅依赖 domain
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│    order-domain             │ ★ 零框架依赖
└────────────────────────────┘
```

## Maven 依赖约束示例

```xml
<!-- order-domain/pom.xml -->
<dependencies>
    <!-- 零框架依赖：无 spring-boot-starter -->
</dependencies>

<!-- order-application/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-domain</artifactId>
    </dependency>
    <!-- 允许 JSR-330 -->
</dependencies>

<!-- order-infrastructure/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-domain</artifactId>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-application</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.kafka</groupId>
        <artifactId>spring-kafka</artifactId>
    </dependency>
</dependencies>
```

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| domain 模块零 Spring 依赖 | ✅ | pom.xml 无 spring-boot-starter |
| 编译期分层强制 | ✅ | 逆向依赖 = 编译失败 |
| API 适配器独立模块 | ✅ | rest/grpc/mq 可独立部署/修改 |
| composition 集中 DI | ✅ | 单一模块装配 |

## 何时选择此结构

- 微服务代码量大（>100 个类），需要模块拆分
- 多 API 入口（同时支持 REST、gRPC 和 MQ）
- 需要编译期预防分层违规
- 团队需要严格的代码组织约定

## 风险提示

- Maven 模块过多 → 构建时间增加
- 每个微服务都多模块 → 仓库数量 × 模块数 = 维护成本爆炸
- 仅在代码量足够大的服务中使用（<50 个类的服务不需要）
