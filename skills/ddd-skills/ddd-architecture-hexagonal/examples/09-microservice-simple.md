# Example: 微服务简单六边形架构

单微服务内的六边形架构，每个服务独立部署，是六边形 + 微服务的最小组合。

## 场景

微服务架构下，单个服务（如 order-service）内部采用六边形架构。服务间通过 API Gateway 通信，服务内部端口适配器隔离。

## 目录树 & 包结构

```
order-service/                                      # 独立部署单元
├── pom.xml
├── Dockerfile
├── src/main/java/com/example/order/
│   ├── OrderServiceApplication.java                # SpringBoot 入口
│   ├── domain/                                     # 领域核心
│   │   ├── model/
│   │   │   ├── Order.java                          # 聚合根
│   │   │   ├── OrderId.java                        # 值对象
│   │   │   └── OrderStatus.java                    # 枚举
│   │   ├── port/
│   │   │   ├── inbound/
│   │   │   │   ├── CreateOrderUseCase.java
│   │   │   │   └── GetOrderUseCase.java
│   │   │   └── outbound/
│   │   │       ├── OrderRepository.java
│   │   │       └── NotificationPort.java           # 通知其他服务
│   │   └── event/
│   │       └── OrderCreatedEvent.java
│   ├── application/
│   │   └── service/
│   │       ├── CreateOrderServiceImpl.java
│   │       └── GetOrderServiceImpl.java
│   ├── adapter/
│   │   ├── inbound/
│   │   │   └── rest/
│   │   │       └── OrderController.java            # REST API
│   │   └── outbound/
│   │       ├── persistence/
│   │       │   ├── PostgresOrderRepository.java
│   │       │   └── OrderJpaEntity.java
│   │       └── notification/
│   │           └── KafkaNotificationAdapter.java   # 发事件给其他服务
│   └── configuration/
│       └── ServiceConfig.java
│
├── src/main/resources/
│   ├── application.yml                              # 服务配置
│   └── db/migration/
│       └── V1__create_order_table.sql
│
└── src/test/java/com/example/order/                 # 分层测试
    ├── domain/
    │   └── OrderTest.java                           # 领域层单元测试（零 Mock）
    ├── application/
    │   └── CreateOrderServiceImplTest.java          # 应用层测试（Mock 端口）
    └── adapter/
        └── rest/
            └── OrderControllerTest.java             # 适配器集成测试
```

## 微服务全景图

```
                    ┌─────────────┐
                    │ API Gateway │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
    │order-service│ │user-service │ │payment-svc   │
    │  (本示例)    │ │ (六边形)    │ │ (六边形)    │
    │             │ │             │ │             │
    │ domain ──── │ │ domain ──── │ │ domain ──── │ │
    │   port ◄────┼─┤   port ◄────┼─┤   port ◄─── │ │
    │ app ◄───────│ │ app ◄───────│ │ app ◄───────│ │
    │ adapter ──► │ │ adapter ──► │ │ adapter ──► │ │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
    ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
    │  Postgres   │ │  Postgres   │ │  Postgres   │
    │  (独立DB)   │ │  (独立DB)   │ │  (独立DB)   │
    └─────────────┘ └─────────────┘ └─────────────┘
                    ┌─────────────┐
                    │    Kafka    │
                    └─────────────┘
```

## 依赖关系

```
                    服务外部
┌───────────────────────────────────────────────────┐
│                                                   │
│  API Gateway ──► REST Controller                  │
│                                                   │
│  ┌───────────── adapter/inbound/ ───────────────┐ │
│  │  OrderController                             │ │
│  │    │ 依赖 UseCase 接口                       │ │
│  │    ▼                                         │ │
│  │  CreateOrderUseCase (domain/port/inbound/)   │ │
│  └──────────────────────────────────────────────┘ │
│                                                   │
│  ┌───────────── application/ ───────────────────┐ │
│  │  CreateOrderServiceImpl                      │ │
│  │    │ 依赖出站端口                             │ │
│  │    ▼                                         │ │
│  │  OrderRepository (domain/port/outbound/)     │ │
│  └──────────────────────────────────────────────┘ │
│                                                   │
│  ┌───────────── adapter/outbound/ ──────────────┐ │
│  │  PostgresOrderRepository → PostgreSQL        │ │
│  │  KafkaNotificationAdapter → Kafka            │ │
│  └──────────────────────────────────────────────┘ │
│                                                   │
└───────────────────────────────────────────────────┘
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 3-8 人/服务 | 小团队负责单服务 |
| 部署单元 | 独立容器/Pod | Kubernetes 部署 |
| 数据库 | 服务自有（Database per Service） | 不跨服务共享 DB |
| 服务间通信 | 同步（REST/gRPC）+ 异步（Kafka） | 通过端口抽象远程调用 |
| 领域复杂度 | 低-中 | 单服务 1-2 个聚合根 |

## 关键设计决策

1. **服务间调用通过端口抽象** — 对其他服务的依赖定义为出站端口（`NotificationPort`），而非直接 HTTP 调用
2. **数据库隔离** — 每个服务独享数据库，通过事件实现最终一致性
3. **API Gateway 作为统一入口** — 主适配器只暴露 REST，Gateway 负责路由/限流/认证
4. **轻量级六边形** — 单服务内结构简单，避免过度抽象

## 与其他示例的关系

```
09-microservice-simple (本示例)
    │  服务内部复杂度增加
    ▼
10-microservice-complex (多聚合 + Saga)
    │  团队规模扩大
    ▼
11-microservice-multi-module (Maven 多模块微服务)
    │  多服务 + 多模块
    ▼
12-microservice-complex-multi (最复杂组合)
```
