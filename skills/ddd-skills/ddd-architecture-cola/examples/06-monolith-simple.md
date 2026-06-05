# COLA 项目规模示例：单体简单项目

> 适用场景：小型单体应用，单一业务域，2-5 人团队，CRUD 为主，无需微服务拆分。

## 项目目录树

```
order-service/                         # 单体项目，spring-boot-maven-plugin 打包
├── pom.xml                            # 单模块，无多模块划分
├── src/
│   ├── main/java/com/example/order/
│   │   ├── OrderApplication.java      # @SpringBootApplication + @EnableCola 启动入口
│   │   │
│   │   ├── adapter/                   # 适配层
│   │   │   ├── web/
│   │   │   │   ├── OrderController.java
│   │   │   │   └── dto/
│   │   │   │       ├── OrderCreateRequest.java
│   │   │   │       └── OrderResponse.java
│   │   │   └── advice/
│   │   │       └── GlobalExceptionHandler.java
│   │   │
│   │   ├── app/                       # 应用层
│   │   │   ├── executor/
│   │   │   │   ├── command/
│   │   │   │   │   └── OrderCreateCmdExe.java
│   │   │   │   └── query/
│   │   │   │       └── OrderGetQryExe.java
│   │   │   └── model/
│   │   │       ├── command/
│   │   │       │   └── OrderCreateCmd.java
│   │   │       └── query/
│   │   │           └── OrderGetQry.java
│   │   │
│   │   ├── domain/                    # 领域层 ★ 零框架依赖
│   │   │   ├── model/
│   │   │   │   ├── Order.java         # 聚合根
│   │   │   │   ├── OrderItem.java     # 实体
│   │   │   │   ├── OrderId.java       # 值对象
│   │   │   │   ├── OrderStatus.java   # 枚举
│   │   │   │   ├── Money.java         # 值对象
│   │   │   │   └── event/
│   │   │   │       ├── OrderCreatedEvent.java
│   │   │   │       └── OrderPaidEvent.java
│   │   │   └── repository/
│   │   │       └── OrderRepository.java  # 仓储接口
│   │   │
│   │   └── infrastructure/            # 基础设施层
│   │       ├── config/
│   │       │   └── DataSourceConfig.java
│   │       ├── persistence/
│   │       │   ├── OrderRepositoryImpl.java
│   │       │   ├── OrderMapper.java       # MyBatis Mapper
│   │       │   ├── OrderPO.java           # 持久化对象
│   │       │   └── OrderConverter.java    # PO ↔ DO 转换
│   │       └── util/
│   │           └── SnowflakeIdGenerator.java
│   │
│   ├── main/resources/
│   │   ├── application.yml
│   │   └── db/migration/
│   │       └── V1__create_order_table.sql
│   └── test/java/com/example/order/
│       ├── ArchitectureComplianceTest.java  # ArchUnit 校验
│       └── domain/
│           └── OrderTest.java
```

## 包结构说明

| 包 | 内容 | 说明 |
|----|------|------|
| `adapter/` | Controller、DTO、ExceptionHandler | HTTP 协议适配，请求/响应转换 |
| `app/` | Command/Query Executor | 用例编排，事务管理 |
| `domain/` | Entity、VO、Aggregate、Repository 接口 | 核心业务逻辑，零框架依赖 |
| `infrastructure/` | RepositoryImpl、Mapper、PO、Config | 持久化实现、外部调用、配置 |

## COLA 四层职责分工

| 层 | 职责 | 禁止事项 |
|----|------|---------|
| **Adapter** | 接收 HTTP 请求，DTO 校验与转换，调用 App 层 | 禁止包含业务逻辑、禁止直接操作 Mapper |
| **Application** | 用例编排，事务边界控制，领域事件发布 | 禁止包含业务 if/else 判断 |
| **Domain** ★ | 实体行为、值对象不变性、领域事件定义 | 禁止依赖 Spring/MyBatis/JPA |
| **Infrastructure** | Repository 实现，PO↔Domain 转换，外部服务调用 | 禁止包含业务规则 |

## 模块间依赖关系

```
┌──────────┐
│  adapter  │────依赖──→┐
└──────────┘           │
                       ▼
┌──────────┐     ┌──────────┐
│    app    │────→│  domain   │←────┌──────────────────┐
└──────────┘     └──────────┘     │  infrastructure    │
                                 └──────────────────┘
```

依赖方向：`adapter → app → domain ← infrastructure`

## 适用场景

- 项目总代码量 < 5 万行
- 单一业务上下文（如订单服务只有一个 Bounded Context）
- 团队 2-5 人，后端开发 1-3 人
- 无微服务拆分需求
- 快速原型验证 / MVP 阶段
- CRUD 操作为主，业务规则较简单

## 优点

- 结构简单，新人快速上手
- 构建速度快，无模块间编译依赖
- 单 jar 部署，运维成本低
- 开发初期迭代效率高

## 缺点

- 无法按模块限制依赖方向（需 ArchUnit 强制）
- 代码量增大后包内文件过多
- 不易拆分为微服务
