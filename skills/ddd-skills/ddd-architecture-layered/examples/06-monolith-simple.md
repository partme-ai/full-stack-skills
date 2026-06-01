# 单体简单项目 — DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 3-8 人，DDD 初学者 |
| 业务复杂度 | 单一聚合根（如订单），CRUD 为主但含状态机 |
| 部署方式 | 单体 Spring Boot JAR，单数据库 |
| 技术栈 | Spring Boot + MyBatis/JPA + Maven |
| 迁移起点 | 传统三层（Controller/Service/DAO）逐步演进 |

**典型业务**：订单管理、用户注册登录、简单审批流。

## 目录树

```
order-simple/
├── pom.xml
└── src/
    └── main/
        └── java/
            └── com/example/order/
                ├── OrderApplication.java              # Spring Boot 入口
                │
                ├── interface/                          # 用户接口层
                │   ├── controller/
                │   │   └── OrderController.java
                │   ├── dto/
                │   │   ├── request/
                │   │   │   ├── CreateOrderRequest.java
                │   │   │   └── UpdateOrderRequest.java
                │   │   └── response/
                │   │       └── OrderResponse.java
                │   └── converter/
                │       └── OrderDtoConverter.java      # DTO ↔ Command 转换
                │
                ├── application/                        # 应用层
                │   ├── service/
                │   │   └── OrderApplicationService.java
                │   ├── command/
                │   │   ├── CreateOrderCommand.java
                │   │   └── UpdateOrderCommand.java
                │   └── query/
                │       └── OrderQuery.java
                │
                ├── domain/                             # 领域层 ★（零框架依赖）
                │   ├── order/
                │   │   ├── entity/
                │   │   │   ├── Order.java              # 聚合根（充血模型）
                │   │   │   └── OrderItem.java          # 实体
                │   │   ├── valueobject/
                │   │   │   ├── Money.java
                │   │   │   ├── OrderStatus.java        # 状态枚举
                │   │   │   └── Address.java
                │   │   ├── service/
                │   │   │   └── OrderDomainService.java # 跨实体逻辑
                │   │   ├── repository/
                │   │   │   └── OrderRepository.java    # 仓储接口（只定义）
                │   │   └── event/
                │   │       └── OrderPlacedEvent.java   # 领域事件
                │   └── shared/
                │       └── BaseEntity.java             # 公共基类
                │
                └── infrastructure/                     # 基础设施层
                    ├── repository/
                    │   └── MyBatisOrderRepository.java # 仓储实现
                    ├── persistence/
                    │   ├── OrderPO.java                # 持久化对象
                    │   └── OrderItemPO.java
                    └── config/
                        └── DddConfiguration.java       # DI 配置
```

## 包结构

```
com.example.order
├── interface        → 依赖 application
├── application      → 依赖 domain
├── domain           → 零依赖（仅 JDK）
└── infrastructure   → 依赖 domain
```

## 模块依赖

```xml
<!-- 单模块 pom.xml，无父子模块划分 -->
<groupId>com.example</groupId>
<artifactId>order-simple</artifactId>
<version>1.0.0</version>
<packaging>jar</packaging>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>3.0.3</version>
    </dependency>
    <!-- 编译期依赖方向靠包结构和 ArchUnit 约束，非 Maven 模块 -->
</dependencies>
```

**依赖方向**：`Interface → Application → Domain ← Infrastructure`

- Interface 依赖 Application（注入 AppService）
- Application 依赖 Domain（调用 Repository 接口、领域实体）
- Domain 零依赖（纯 JDK 类型）
- Infrastructure 依赖 Domain（实现 Repository 接口）

由于是单模块，依赖方向依赖**约定优于配置**，配合 ArchUnit 测试强制约束。实际运行时 Spring DI 容器自动注入 Infrastructure 实现到 Domain 接口。

## 关键设计要点

| 要点 | 说明 |
|------|------|
| 分层物理隔离 | 单模块下靠包名隔离，ArchUnit 编译期校验 |
| Domain 充血模型 | 业务方法在实体内部，不依赖 Spring 注解 |
| Repository 接口 | 定义在 Domain 层，实现在 Infra 层 |
| Application 薄层 | 只做编排，不含 if/else 业务判断 |
| Interface 协议转换 | Controller 只负责 DTO 转换和参数校验 |

## 优点与局限

| 优点 | 局限 |
|------|------|
| 结构简单，学习曲线低 | 包名约束弱，依赖方向易被破坏 |
| 快速启动，适合 PoC | 所有层共享同一 classpath |
| 部署简单，一个 JAR | 无物理模块隔离，Domain 可能被污染 |
| 适合小团队快速迭代 | 规模增长后需拆分为多模块 |

## 演进路径

```
单模块四层 → 多模块四层（08）→ 微服务多模块（11/12）
```
