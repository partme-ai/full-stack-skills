# Example: 单体简单六边形架构

单一 SpringBoot 模块内的六边形包结构，适用于小型项目快速落地。

## 场景

5 人以下团队、单数据库、单一 REST API 入口的系统，无需 Maven 多模块即可获得端口/适配器隔离的好处。

## 目录树 & 包结构

```
order-service/
└── src/main/java/com/example/order/
    ├── OrderApplication.java                        # SpringBoot 入口
    ├── web/                                         # 主适配器（Primary Adapters）
    │   └── OrderController.java                     # POST /orders, GET /orders/{id}
    ├── application/                                 # 应用层
    │   ├── service/
    │   │   ├── CreateOrderService.java              # implements CreateOrderUseCase
    │   │   └── GetOrderService.java                 # implements GetOrderUseCase
    │   └── dto/
    │       ├── CreateOrderRequest.java              # 入站 DTO
    │       └── OrderResponse.java                   # 出站 DTO
    ├── domain/                                      # 领域核心（零框架依赖）
    │   ├── model/
    │   │   ├── Order.java                           # 聚合根
    │   │   ├── OrderId.java                         # 值对象
    │   │   ├── OrderItem.java                       # 实体
    │   │   └── OrderStatus.java                     # 枚举
    │   ├── port/                                    # ★ 端口定义
    │   │   ├── inbound/
    │   │   │   ├── CreateOrderUseCase.java          # 入站端口
    │   │   │   └── GetOrderUseCase.java             # 入站端口
    │   │   └── outbound/
    │   │       ├── OrderRepository.java             # 出站端口（持久化）
    │   │       └── EventPublisher.java              # 出站端口（消息）
    │   └── event/
    │       └── OrderCreatedEvent.java               # 领域事件
    └── infrastructure/                              # 次适配器（Secondary Adapters）
        ├── persistence/
        │   ├── JpaOrderRepository.java              # implements OrderRepository
        │   ├── OrderJpaEntity.java                  # JPA Entity
        │   └── OrderMapper.java                     # Domain ⇄ PO 映射
        ├── messaging/
        │   └── KafkaEventPublisher.java             # implements EventPublisher
        └── config/
            └── BeanConfig.java                      # DI 装配
```

## 依赖关系

```
web (Controller)          → application (Service, DTO)  → domain (Model, Port)
infrastructure (Adapter)  → domain (Model, Port)        → 外部（DB, MQ）
```

```
┌── web/ ──────────────────────────┐
│  OrderController                 │  主适配器：协议转换
└──────────────┬───────────────────┘
               │ 依赖
               ▼
┌── application/ ──────────────────┐
│  CreateOrderService              │  应用服务：用例编排
│  (implements CreateOrderUseCase) │
└──────────┬───────────────────────┘
           │ 依赖（注入端口接口）
           ▼
┌── domain/ ───────────────────────┐
│  port/inbound/CreateOrderUseCase │  ★ 入站端口（接口）
│  port/outbound/OrderRepository   │  ★ 出站端口（接口）
│  model/Order (Aggregate Root)    │  领域逻辑
└──────────────────────────────────┘
           ▲
           │ 实现
┌── infrastructure/ ───────────────┐
│  JpaOrderRepository              │  次适配器：JPA 实现
│  KafkaEventPublisher             │  次适配器：Kafka 实现
└──────────────────────────────────┘
```

## 适用场景

| 维度 | 值 | 说明 |
|------|------|------|
| 团队规模 | 1-5 人 | 小团队无需多模块 |
| 入口数量 | 1 个 (REST) | 单入口无需多主适配器 |
| 外部依赖 | 1 DB + 1 MQ | 简单基础设施 |
| 领域复杂度 | 低 | 1-2 个聚合根 |
| 项目生命周期 | MVP → 早期产品 | 后续可演进到多模块 |

## 关键设计决策

1. **单模块内包隔离** — 用 package 可见性替代 Maven module 隔离，简化构建
2. **端口仍在 domain 包内** — 保持端口定义的领域纯粹性
3. **infrastructure 包实现所有出站端口** — 技术实现集中管理
4. **Controller 直接依赖 UseCase 接口** — 不引入应用层中间件

## 演进路径

```
单模块六边形 (本示例)
    │  团队增长 / 入口增加
    ▼
Maven 多模块六边形 (08-monolith-multi-module)
    │  服务拆分
    ▼
微服务六边形 (09-12)
```
