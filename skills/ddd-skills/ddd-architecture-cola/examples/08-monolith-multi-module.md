# COLA 项目规模示例：单体多模块项目

> 适用场景：中型单体应用，需要 Maven 多模块强制隔离依赖方向，5-15 人团队，对架构约束要求高。

## 项目目录树

```
order-system/                                   # 父 POM，packaging=pom
├── pom.xml                                     # 父 POM，定义 modules + dependencyManagement
│
├── order-start/                                # 启动模块
│   ├── pom.xml                                 # 依赖所有其他模块，含 spring-boot-maven-plugin
│   └── src/main/java/com/example/order/
│       ├── OrderApplication.java               # @SpringBootApplication + @EnableCola
│       └── config/
│           ├── CorsConfig.java
│           └── SwaggerConfig.java
│
├── order-adapter/                              # 适配层模块
│   ├── pom.xml                                 # 依赖 order-app、order-domain
│   └── src/main/java/com/example/order/adapter/
│       ├── web/
│       │   ├── OrderController.java
│       │   └── dto/
│       │       ├── OrderCreateRequest.java
│       │       └── OrderResponse.java
│       ├── rpc/
│       │   └── OrderQueryFacade.java
│       └── advice/
│           └── GlobalExceptionHandler.java
│
├── order-app/                                  # 应用层模块
│   ├── pom.xml                                 # 依赖 order-domain、order-infrastructure
│   └── src/main/java/com/example/order/app/
│       ├── executor/
│       │   ├── command/
│       │   │   └── OrderCreateCmdExe.java
│       │   └── query/
│       │       └── OrderGetQryExe.java
│       ├── model/
│       │   ├── command/
│       │   │   └── OrderCreateCmd.java
│       │   └── query/
│       │       └── OrderGetQry.java
│       ├── service/
│       │   └── OrderPlacementService.java
│       └── assembler/
│           └── OrderAssembler.java
│
├── order-domain/                               # 领域层模块 ★ 零 external 依赖
│   ├── pom.xml                                 # 零外部依赖（仅 lombok、validation-api）
│   └── src/main/java/com/example/order/domain/
│       ├── model/
│       │   ├── Order.java                      # 聚合根
│       │   ├── OrderItem.java                  # 实体
│       │   ├── OrderId.java                    # 值对象
│       │   ├── OrderStatus.java
│       │   ├── Money.java
│       │   └── event/
│       │       ├── OrderCreatedEvent.java
│       │       └── OrderPaidEvent.java
│       ├── repository/
│       │   └── OrderRepository.java            # 仓储接口
│       ├── gateway/
│       │   └── InventoryGateway.java           # 防腐层接口
│       └── ability/
│           └── PriceCalculationAbility.java
│
├── order-infrastructure/                       # 基础设施层模块
│   ├── pom.xml                                 # 依赖 order-domain
│   └── src/main/java/com/example/order/infrastructure/
│       ├── config/
│       │   ├── DataSourceConfig.java
│       │   └── CacheConfig.java
│       ├── persistence/
│       │   ├── OrderRepositoryImpl.java
│       │   ├── OrderMapper.java
│       │   ├── OrderPO.java
│       │   └── OrderConverter.java
│       └── gatewayimpl/
│           └── InventoryGatewayImpl.java
│
└── order-common/                               # 公共模块（可选）
    ├── pom.xml                                 # 无内部模块依赖
    └── src/main/java/com/example/order/common/
        ├── constant/
        │   └── BizConstants.java
        ├── exception/
        │   ├── BizException.java
        │   └── ErrorCode.java
        └── context/
            └── UserContext.java
```

## 各模块的包结构说明

| 模块 | 包路径 | 内容 | Maven ArtifactId |
|------|--------|------|-----------------|
| **启动模块** | `com.example.order` | Application 启动类 + 全局配置 | `order-start` |
| **适配层** | `com.example.order.adapter` | Controller / RPC / DTO / ExceptionHandler | `order-adapter` |
| **应用层** | `com.example.order.app` | Executor / Service / Assembler / Model | `order-app` |
| **领域层** | `com.example.order.domain` | Entity / VO / Aggregate / Repository 接口 | `order-domain` |
| **基础设施层** | `com.example.order.infrastructure` | RepositoryImpl / Mapper / PO / GatewayImpl | `order-infrastructure` |
| **公共模块** | `com.example.order.common` | 常量 / 异常基类 / 上下文 / 工具 | `order-common` |

## COLA 四层职责分工

| 层 | 对应模块 | 职责 | Maven 依赖约束 |
|----|---------|------|---------------|
| **Adapter** | `order-adapter` | HTTP/RPC 协议适配，DTO 转换 | 可引用 app + domain + common |
| **Application** | `order-app` | 用例编排，事务管理，扩展点 | 可引用 domain + infrastructure + common |
| **Domain** ★ | `order-domain` | 核心业务规则 | **零外部依赖**，仅可引用 common |
| **Infrastructure** | `order-infrastructure` | 持久化、外部服务、组件 | 可引用 domain + common |
| **启动** | `order-start` | 启动入口、全局配置 | 引用所有其他模块 |
| **公共** | `order-common` | 常量、异常、上下文 | 无项目内依赖 |

## 模块间依赖关系图

```
┌──────────────────────────────────────────────────────────────────┐
│                        order-start                               │
│          (启动模块 — 引用所有其他模块)                               │
└────┬───────────┬──────────┬──────────┬──────────┬───────────────┘
     │           │          │          │          │
     ▼           ▼          ▼          ▼          ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ adapter │ │   app   │ │ domain  │ │  infra  │ │ common  │
│         │ │         │ │    ★    │ │         │ │         │
└────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └─────────┘
     │           │           │           │           ▲
     │      ┌────┘           │           │           │
     │      │                │           │           │
     ▼      ▼                ▼           ▼           │
┌───────────────────────────────────────────────────┐│
│              Maven 依赖关系图                      ││
│                                                   ││
│  adapter ───→ app ───→ domain ←─── infrastructure ││
│     │         │         ▲              │          ││
│     └────┬────┘         │              │          ││
│          └──────────────┼──────────────┘          ││
│                         └── common ←──────────────┘│
└────────────────────────────────────────────────────┘
```

**硬约束**（由 Maven compile-scope 依赖保证）：
- `order-domain` 的 pom.xml 中不出现 `order-adapter`、`order-app`、`order-infrastructure`、`spring-boot-starter`、`mybatis-spring-boot-starter` 等依赖
- `order-app` 不直接引用 `order-adapter`
- `order-infrastructure` 不引用 `order-app`、`order-adapter`

**验证方式**：
```xml
<!-- order-domain/pom.xml: 领域层只能依赖这些 -->
<dependency>
    <groupId>com.example.order</groupId>
    <artifactId>order-common</artifactId>
</dependency>
<!-- 不允许出现 spring-boot-starter、mybatis、jpa 等 -->
```

## 适用场景

- 需要 Maven 模块编译时强制依赖约束（比 ArchUnit 更早发现问题）
- 团队 5-15 人，多人并行开发同一项目
- 业务复杂度中等，单一 Bounded Context 但有丰富行为
- 需要确保架构不被新手开发者破坏
- 单个 Git 仓库管理，不想拆分为多仓库

## 优点

- Maven 编译时即发现依赖违规（比 ArchUnit 运行时更早）
- 各模块独立编译，仅需重新编译变更模块
- 团队可按模块分工（Domain 资深开发 / Infra 一般开发）
- 为未来微服务拆分做模块级准备

## 缺点

- 模块间接口变化影响编译范围增大
- Maven 多模块构建时间比单模块长
- 新手需要理解模块间的接口抽象（如 Repository 接口在 Domain，实现在 Infra）
- Common 模块容易变成"垃圾桶"（需严格控制内容）
