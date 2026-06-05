# Example 06 — 单体简单规模（Monolith Simple）

> 单模块 Maven/Gradle 项目，所有洋葱层放在同一个模块的不同 package 中。适合 1-3 人团队、单一限界上下文。

## 适用场景

| 条件 | 说明 |
|------|------|
| 团队规模 | 1-3 人 |
| 限界上下文 | 1 个 |
| 部署单元 | 1 个 JAR/WAR |
| 数据库 | 1 个 RDBMS |
| 外部集成 | < 3 个 |

## 目录树

```
order-system/
├── pom.xml / build.gradle                    # 单模块依赖管理
├── src/main/java/com/example/order/
│   ├── core/
│   │   ├── domain/                            # Domain 层
│   │   │   ├── model/
│   │   │   │   ├── Order.java                 # 聚合根
│   │   │   │   ├── OrderId.java               # 值对象
│   │   │   │   ├── OrderItem.java             # 实体
│   │   │   │   └── OrderStatus.java           # 枚举
│   │   │   ├── service/
│   │   │   │   └── PricingService.java         # 领域服务
│   │   │   ├── repository/
│   │   │   │   └── OrderRepository.java        # 仓储接口
│   │   │   └── event/
│   │   │       ├── OrderCreatedEvent.java
│   │   │       └── OrderPaidEvent.java
│   │   └── application/                       # Application 层
│   │       └── service/
│   │           ├── OrderApplicationService.java
│   │           └── impl/
│   │               └── OrderApplicationServiceImpl.java
│   ├── infrastructure/                        # Infrastructure 层
│   │   ├── data/
│   │   │   ├── entity/
│   │   │   │   └── OrderPO.java               # JPA Entity
│   │   │   ├── repository/
│   │   │   │   └── OrderRepositoryImpl.java
│   │   │   └── mapper/
│   │   │       └── OrderMapper.java            # PO ⇄ Domain
│   │   └── messaging/
│   │       └── KafkaEventPublisher.java
│   ├── api/                                   # API 层
│   │   ├── controller/
│   │   │   └── OrderController.java
│   │   ├── dto/
│   │   │   ├── request/
│   │   │   │   └── CreateOrderRequest.java
│   │   │   └── response/
│   │   │       └── OrderResponse.java
│   │   └── assembler/
│   │       └── OrderDTOAssembler.java
│   └── composition/                           # Composition 层
│       └── config/
│           └── OrderModuleConfig.java
└── src/test/java/com/example/order/
    ├── core/domain/model/OrderTest.java        # Domain 单元测试
    ├── core/application/...                    # Application Mock 测试
    └── infrastructure/...                      # Infrastructure 集成测试
```

## 包结构与依赖方向

```
┌──────────────────────────────────────────┐
│  composition/                             │
│  config/OrderModuleConfig.java            │ ← 组装所有 Bean
└──────────┬───────────────────────────────┘
           │ 依赖所有模块
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌──────────┐ ┌──────────────┐
│  api/    │ │infrastructure│
│controller│ │    /data      │
│  /dto    │ │  /messaging   │
└────┬─────┘ └───┬──────────┘
     │           │
     │           │ 实现 Domain 接口
     ▼           ▼
┌──────────────────────────────┐
│      core/application/       │
│  OrderApplicationService     │
└──────────────┬───────────────┘
               │ 依赖 Domain
               ▼
┌──────────────────────────────┐
│       core/domain/           │ ★ 核心（零框架依赖）
│  Order, OrderRepository,     │
│  PricingService              │
└──────────────────────────────┘
```

**依赖规则**：所有箭头指向 `core/domain`，内层不知道外层存在。

## Maven 依赖关系

```xml
<!-- 单模块，所有依赖在同一个 pom.xml -->
<dependencies>
    <!-- Domain 层零框架依赖（纯 Java） -->
    <!-- Application 层引入 JSR-330 -->
    <dependency>
        <groupId>jakarta.inject</groupId>
        <artifactId>jakarta.inject-api</artifactId>
    </dependency>

    <!-- Infrastructure 层引入具体实现 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.kafka</groupId>
        <artifactId>spring-kafka</artifactId>
    </dependency>

    <!-- API 层引入 Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

## 合规检查

| 检查项 | 状态 | 说明 |
|--------|:----:|------|
| Domain 层零框架依赖 | ✅ | 仅使用 `java.*` 和 `jakarta.inject` |
| Repository 接口在 Domain | ✅ | `OrderRepository` 在 `core/domain/repository` |
| Repository 实现在 Infra | ✅ | `OrderRepositoryImpl` 在 `infrastructure/data` |
| Application 层纯编排 | ✅ | `OrderApplicationServiceImpl` 无业务判断 |
| DTO 仅在 API 层 | ✅ | Request/Response 在 `api/dto` |
| DI 集中在 composition | ✅ | `OrderModuleConfig` 装配所有 Bean |

## 何时选择此结构

- 项目起步，团队小，业务简单
- 后续可能拆分，但当前单模块够用
- 希望用 package 约定模拟模块边界，为未来拆分做准备
