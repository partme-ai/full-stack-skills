# 11 — 微服务 Clean 架构（多模块版）

> 单微服务按四层拆分为 Maven 模块，编译期强制依赖方向。

## 目录树

```
order-service/
├── pom.xml                                  # 父 POM
├── Dockerfile
│
├── order-enterprise/                        # 模块1: Enterprise
│   ├── pom.xml                              # 零框架依赖
│   └── src/main/java/com/example/order/enterprise/
│       ├── entity/Order.java
│       ├── entity/OrderItem.java
│       ├── vo/OrderId.java
│       ├── vo/Money.java
│       ├── vo/OrderStatus.java
│       ├── event/DomainEvent.java
│       └── event/OrderCreatedEvent.java
│
├── order-usecase/                           # 模块2: Application
│   ├── pom.xml                              # 只依赖 order-enterprise
│   └── src/main/java/com/example/order/usecase/
│       ├── port/input/
│       │   ├── CreateOrderUseCase.java
│       │   └── QueryOrderUseCase.java
│       ├── port/output/
│       │   ├── OrderRepository.java
│       │   └── EventBus.java
│       ├── dto/
│       │   ├── CreateOrderRequest.java
│       │   └── CreateOrderResponse.java
│       └── interactor/
│           ├── CreateOrderInteractor.java
│           └── QueryOrderInteractor.java
│
├── order-adapter/                           # 模块3: Adapters
│   ├── pom.xml                              # 依赖 usecase + enterprise + Spring
│   └── src/main/java/com/example/order/adapter/
│       ├── controller/OrderController.java
│       ├── repository/
│       │   ├── OrderJpaEntity.java
│       │   ├── OrderJpaRepository.java
│       │   └── OrderRepositoryImpl.java
│       └── messaging/
│           ├── KafkaEventBus.java
│           └── OrderEventConsumer.java
│
├── order-client/                            # 模块4: 对外 API（可选）
│   ├── pom.xml                              # 只含 DTO，无内部依赖
│   └── src/main/java/com/example/order/client/
│       ├── dto/
│       │   ├── CreateOrderRequest.java
│       │   └── OrderResponse.java
│       └── api/
│           └── OrderServiceApi.java         # Feign Interface
│
├── order-boot/                              # 模块5: Boot & Config
│   ├── pom.xml                              # 依赖所有模块
│   └── src/main/java/com/example/order/boot/
│       ├── OrderApplication.java
│       └── config/
│           ├── UseCaseConfig.java
│           ├── PersistenceConfig.java
│           └── KafkaConfig.java
│
└── order-integration-test/                  # 模块6: 集成测试
    ├── pom.xml                              # 依赖所有模块 (test scope)
    └── src/test/java/com/example/order/it/
        ├── OrderServiceIntegrationTest.java
        └── KafkaEventIntegrationTest.java
```

## 模块依赖关系

```
┌──────────────────┐
│   order-client   │  ← 对外暴露的 API 契约（纯 DTO + Feign Interface）
└────────┬─────────┘     无内部依赖，可独立发布给消费者
         │
┌────────▼─────────┐
│   order-boot     │  ← Spring Boot 启动 + DI 配置
└────────┬─────────┘     依赖: adapter, usecase, enterprise, client
         │
┌────────▼─────────┐
│  order-adapter   │  ← Controller, Repository Impl, Kafka Adapter
└────────┬─────────┘     依赖: usecase, enterprise
         │
┌────────▼─────────┐
│  order-usecase   │  ← Interactor, Port 接口
└────────┬─────────┘     依赖: enterprise
         │
┌────────▼─────────┐
│ order-enterprise │  ← Entity, VO, Domain Event
└──────────────────┘     零外部依赖
```

## Maven 模块职责矩阵

| 模块 | 分层 | Spring 依赖 | 可独立构建 | 可独立测试 |
|------|------|------------|-----------|-----------|
| `order-enterprise` | Enterprise | ❌ 无 | ✅ | ✅ 纯单元测试 |
| `order-usecase` | Application | ❌ 无 | ✅ | ✅ Mock 端口 |
| `order-adapter` | Interface Adapters | ✅ Web+JPA+Kafka | ✅ | ✅ Testcontainers |
| `order-client` | 对外 API | ❌ 无 | ✅ | N/A |
| `order-boot` | Frameworks | ✅ Spring Boot | ✅ | ✅ 集成测试 |
| `order-integration-test` | 测试 | ✅ 所有 | ✅ | ✅ 全链路 |

## 微服务特有关系

### client 模块：API 契约独立发布

```
order-service 发布时:
  order-client-1.0.1.jar → Maven 仓库

payment-service 依赖:
  <dependency>
    <groupId>com.example</groupId>
    <artifactId>order-client</artifactId>
    <version>1.0.1</version>
  </dependency>
```

其他服务通过 `order-client` 获得类型安全的 Feign 接口，无需手写 HTTP 调用。

### 独立构建优化

```bash
# 只构建 usecase 层（不触发 adapter 的 JPA/Kafka 编译）
cd order-usecase && mvn test -pl .

# 全量构建（含集成测试）
mvn verify -pl order-integration-test
```

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 8-20 人/服务，模块级独立开发 |
| 项目复杂度 | 2-4 个聚合根/服务，15-30 个 UseCase/服务 |
| 隔离要求 | 编译期强制四层隔离 + 模块间 API 契约化 |
| 发布策略 | 各模块独立版本，API 契约独立演进 |
| 典型业务 | 平台型微服务、多消费者 SaaS API |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| 编译期绝对隔离，零腐化风险 | 6 个模块维护成本高 |
| API 契约独立发布，消费者解耦 | 模块间版本依赖管理复杂 |
| 各层独立编译、测试、发布 | 新人需要理解完整的模块图 |
| 天然适配 CI/CD 增量构建 | 小服务过度工程化风险 |
