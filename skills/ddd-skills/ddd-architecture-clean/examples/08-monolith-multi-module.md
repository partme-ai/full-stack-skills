# 08 — 单体 Clean 架构（多模块版）

> 每层一个 Maven 模块，编译期强制依赖方向，适合需要物理隔离的单体项目。

## 目录树

```
order-platform/
├── pom.xml                               # 父 POM（module 聚合）
│
├── order-enterprise/                     # 模块1: Enterprise Business Rules
│   ├── pom.xml                           # 零外部依赖
│   └── src/main/java/com/example/order/enterprise/
│       ├── entity/
│       │   ├── Order.java
│       │   └── OrderItem.java
│       ├── vo/
│       │   ├── OrderId.java
│       │   ├── Money.java
│       │   └── OrderStatus.java
│       └── event/
│           ├── DomainEvent.java
│           └── OrderCreatedEvent.java
│
├── order-usecase/                        # 模块2: Application Business Rules
│   ├── pom.xml                           # 只依赖 order-enterprise
│   └── src/main/java/com/example/order/usecase/
│       ├── port/input/
│       │   ├── CreateOrderUseCase.java
│       │   └── QueryOrderUseCase.java
│       ├── port/output/
│       │   ├── OrderRepository.java
│       │   └── PaymentGateway.java
│       ├── dto/
│       │   ├── CreateOrderRequest.java
│       │   ├── CreateOrderResponse.java
│       │   └── OrderSummaryDTO.java
│       └── interactor/
│           ├── CreateOrderInteractor.java
│           └── QueryOrderInteractor.java
│
├── order-adapter/                        # 模块3: Interface Adapters
│   ├── pom.xml                           # 依赖 order-usecase + order-enterprise
│   └── src/main/java/com/example/order/adapter/
│       ├── controller/
│       │   └── OrderController.java
│       ├── repository/
│       │   ├── OrderJpaEntity.java
│       │   ├── OrderJpaRepository.java
│       │   └── OrderRepositoryImpl.java
│       └── gateway/
│           └── AlipayGatewayImpl.java
│
├── order-boot/                           # 模块4: Frameworks & Drivers
│   ├── pom.xml                           # 依赖 order-adapter + Spring Boot
│   └── src/main/java/com/example/order/boot/
│       ├── OrderApplication.java         # @SpringBootApplication
│       └── config/
│           ├── UseCaseConfig.java        # @Configuration: Bean 装配
│           ├── PersistenceConfig.java
│           └── SecurityConfig.java
│
├── order-acceptance/                     # 模块5: 验收测试（可选）
│   ├── pom.xml                           # 依赖 order-boot (test scope)
│   └── src/test/java/com/example/order/acceptance/
│       └── OrderAcceptanceTest.java
│
└── order-arch-test/                      # 模块6: 架构测试（可选）
    ├── pom.xml                           # 依赖所有模块 (test scope)
    └── src/test/java/com/example/order/arch/
        └── DependencyRuleTest.java
```

## Maven 依赖关系

```xml
<!-- order-enterprise/pom.xml -->
<!-- 零外部依赖，只含 Java 标准库 -->
<dependencies>
    <!-- 无 -->
</dependencies>

<!-- order-usecase/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-enterprise</artifactId>
    </dependency>
</dependencies>

<!-- order-adapter/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-usecase</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
</dependencies>

<!-- order-boot/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-adapter</artifactId>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-usecase</artifactId>
    </dependency>
    <!-- Spring Boot Starter -->
</dependencies>
```

## 依赖方向图

```
┌────────────────────────────────────────────┐
│              order-boot                     │
│   SpringBoot App + DI Config               │
│   依赖: adapter, usecase, enterprise        │
└────────────────┬───────────────────────────┘
                 │
┌────────────────▼───────────────────────────┐
│              order-adapter                   │
│   Controller, Repository Impl, Gateway      │
│   依赖: usecase, enterprise                 │
└────────────────┬───────────────────────────┘
                 │
┌────────────────▼───────────────────────────┐
│              order-usecase                  │
│   Interactor, Port (in/out), DTO           │
│   依赖: enterprise                          │
└────────────────┬───────────────────────────┘
                 │
┌────────────────▼───────────────────────────┐
│            order-enterprise                 │
│   Entity, Value Object, Domain Event       │
│   零外部依赖                                │
└────────────────────────────────────────────┘
```

## 编译期强制 vs 运行时检查

| 机制 | 简单版（06） | 多模块版（08） |
|------|------------|---------------|
| 分层隔离 | 包名约定 | Maven 模块依赖 |
| 违规检测 | ArchUnit 运行时 | **编译期报错** |
| usecase 引用 Spring | ArchUnit 拦截 | Maven 不解析类，编译失败 |
| 循环依赖 | 可能发生 | Maven 拒绝构建 |
| 构建速度 | 快 | 增量构建后可接受 |

## 适用场景

| 维度 | 说明 |
|------|------|
| 团队规模 | 8-25 人，多团队协作 |
| 项目复杂度 | 3-8 个聚合根，30-80 个 UseCase |
| 隔离要求 | 需要编译期强制分层隔离 |
| 演进方向 | 可进一步拆分为领域模块 + 微服务 |
| 典型业务 | 企业级中台、大型电商、金融核心系统 |

## 优缺点

| ✅ 优点 | ❌ 缺点 |
|---------|---------|
| 编译期强制依赖方向，杜绝腐化 | 模块数多，构建配置复杂 |
| 各模块可独立构建、测试 | 新人上手成本较高 |
| 为微服务拆分提供天然的模块边界 | 跨模块测试配置繁琐 |
| 适合大型团队并行开发 | 单体中过度模块化增加维护成本 |
