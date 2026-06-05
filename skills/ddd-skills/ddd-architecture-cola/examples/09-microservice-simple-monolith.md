# COLA 项目规模示例：微服务简单的单体项目

> 适用场景：微服务架构，每个微服务内部采用 COLA 单体结构（非多模块），服务边界清晰，业务简单。

## 项目目录树

```
├── order-service/                              # 订单微服务 (COLA 单体)
│   ├── pom.xml
│   └── src/main/java/com/example/order/
│       ├── OrderApplication.java
│       ├── adapter/
│       │   ├── web/OrderController.java         # 对前端暴露 REST
│       │   └── rpc/OrderQueryFacade.java         # 对其他微服务暴露 Dubbo/gRPC
│       ├── app/
│       │   ├── executor/command/OrderCreateCmdExe.java
│       │   └── executor/query/OrderGetQryExe.java
│       ├── domain/
│       │   ├── Order.java
│       │   ├── OrderItem.java
│       │   └── repository/OrderRepository.java
│       └── infrastructure/
│           ├── persistence/OrderRepositoryImpl.java
│           └── external/ProductServiceClient.java  # 调用商品微服务
│
├── product-service/                            # 商品微服务 (COLA 单体)
│   ├── pom.xml
│   └── src/main/java/com/example/product/
│       ├── ProductApplication.java
│       ├── adapter/
│       │   ├── web/ProductController.java
│       │   └── rpc/ProductRpcFacade.java
│       ├── app/
│       │   ├── executor/command/ProductCreateCmdExe.java
│       │   └── executor/query/ProductSearchQryExe.java
│       ├── domain/
│       │   ├── Product.java
│       │   ├── Stock.java
│       │   └── repository/ProductRepository.java
│       └── infrastructure/
│           ├── persistence/ProductRepositoryImpl.java
│           └── search/ProductElasticsearchRepo.java
│
├── customer-service/                           # 客户微服务 (COLA 单体)
│   ├── pom.xml
│   └── src/main/java/com/example/customer/
│       ├── CustomerApplication.java
│       ├── adapter/
│       │   └── web/CustomerController.java
│       ├── app/
│       │   └── executor/command/CustomerRegisterCmdExe.java
│       ├── domain/
│       │   ├── Customer.java
│       │   └── repository/CustomerRepository.java
│       └── infrastructure/
│           └── persistence/CustomerRepositoryImpl.java
│
├── gateway-service/                            # API 网关 (可选)
│   └── ...
│
└── common/                                     # 公共组件（共享 DTO、工具类）
    ├── common-api/                             # 服务间通信 DTO
    │   ├── OrderDTO.java
    │   └── ProductDTO.java
    └── common-util/
        ├── ApiResponse.java
        └── BizException.java
```

## 各服务的包结构说明

每个微服务内部采用与示例 06 相同的 COLA 单体包结构：

| 微服务 | Adapter 协议 | 领域聚合 | 对外依赖 |
|--------|-------------|---------|---------|
| `order-service` | REST + Dubbo RPC | Order + OrderItem | product-service, customer-service |
| `product-service` | REST + Dubbo RPC | Product + Stock | — (被调用方) |
| `customer-service` | REST | Customer | — (被调用方) |

## COLA 四层职责分工

| 层 | 职责 | 微服务环境特殊注意 |
|----|------|------------------|
| **Adapter** | REST (对外) + RPC/Dubbo (服务间) + MQ Consumer | Adapter 同时暴露 Web API 和 RPC API |
| **Application** | 单聚合用例编排 | 涉及调用其他微服务时通过 Gateway/防腐层，不在 Executor 直接调用 |
| **Domain** ★ | 服务内的业务规则 | 聚合不可直接引用其他微服务的 Domain 对象 |
| **Infrastructure** | 本地持久化 + 外部微服务调用 | external/ 封装对其他微服务的调用，不暴露技术细节 |

## 服务间依赖关系

```
                    ┌──────────────────┐
                    │   order-service  │
                    │                  │
                    │  adapter (REST)  │←─ 前端请求
                    │  adapter (RPC)   │←─ 其他服务调用
                    │  app             │
                    │  domain          │
                    │  infra (DB +     │
                    │    FeignClient   │─────── 调用 ───────┐
                    │  → ProductSvc)   │                    │
                    └──────────────────┘                    │
                                                            ▼
┌──────────────────┐        ┌──────────────────┐  ┌──────────────────┐
│ customer-service │        │ product-service  │  │   common-api     │
│                  │        │                  │  │                  │
│  adapter (REST)  │        │  adapter (REST)  │  │  共享 DTO         │
│  app             │        │  adapter (RPC)   │  │  OrderDTO        │
│  domain          │        │  app             │  │  ProductDTO      │
│  infra           │        │  domain          │  │  ApiResponse     │
└──────────────────┘        │  infra           │  └──────────────────┘
                            └──────────────────┘
```

**依赖原则**：
- 每个微服务独立数据库，不共享表
- 服务间通过 RPC/MQ 通信，不直接访问对方数据库
- `common-api` 发布为 Maven 坐标，各服务通过依赖引用共享 DTO
- 服务内的 COLA 分层规则不变：Domain 仍然零框架依赖

## 适用场景

- 微服务已经拆分完成，每个服务职责单一
- 每个微服务代码量 < 3 万行
- 每个微服务内业务逻辑相对简单（1-2 个聚合）
- 服务间通过 RPC (Dubbo/gRPC) 或 MQ (RocketMQ/Kafka) 通信
- 团队 10-30 人，每个服务由 2-3 人小团队负责

## 优点

- 每个服务简单，新人快速上手
- 独立部署、独立扩缩容
- 单模块构建快，CI 效率高
- 技术栈可按服务选择（如商品服务用 Elasticsearch，订单服务用 MySQL）

## 缺点

- 服务内无法用编译时约束防止架构腐化（单模块）
- `common-api` 修改影响所有服务
- 需要处理分布式事务（Saga/最终一致性）
- 服务数量增多后运维成本高
