# COLA 项目规模示例：单体复杂项目

> 适用场景：中型单体应用，多聚合根，多业务上下文，5-15 人团队，有复杂业务编排需求。

## 项目目录树

```
mall-service/                                     # 单体项目，多聚合
├── pom.xml
├── src/main/java/com/example/mall/
│   ├── MallApplication.java                      # @SpringBootApplication + @EnableCola
│   │
│   ├── adapter/                                  # 适配层
│   │   ├── web/
│   │   │   ├── order/
│   │   │   │   └── OrderController.java
│   │   │   ├── product/
│   │   │   │   └── ProductController.java
│   │   │   ├── customer/
│   │   │   │   └── CustomerController.java
│   │   │   ├── payment/
│   │   │   │   └── PaymentController.java
│   │   │   └── dto/
│   │   │       ├── common/
│   │   │       │   ├── PageRequest.java
│   │   │       │   └── ApiResponse.java
│   │   │       ├── order/
│   │   │       │   ├── OrderCreateRequest.java
│   │   │       │   └── OrderResponse.java
│   │   │       └── product/
│   │   │           └── ProductResponse.java
│   │   ├── job/                                  # 定时任务
│   │   │   ├── OrderExpireJob.java
│   │   │   └── DailyReportJob.java
│   │   ├── message/                              # MQ 消费者
│   │   │   ├── PaymentResultConsumer.java
│   │   │   └── InventoryChangeConsumer.java
│   │   └── rpc/                                  # RPC 接口
│   │       └── OrderQueryFacade.java
│   │
│   ├── app/                                      # 应用层
│   │   ├── executor/
│   │   │   ├── command/
│   │   │   │   ├── order/
│   │   │   │   │   ├── OrderCreateCmdExe.java
│   │   │   │   │   ├── OrderCancelCmdExe.java
│   │   │   │   │   └── OrderPayCmdExe.java
│   │   │   │   ├── product/
│   │   │   │   │   └── ProductDeductStockCmdExe.java
│   │   │   │   └── customer/
│   │   │   │       └── CustomerRegisterCmdExe.java
│   │   │   ├── query/
│   │   │   │   ├── order/
│   │   │   │   │   ├── OrderDetailQryExe.java
│   │   │   │   │   └── OrderListQryExe.java
│   │   │   │   └── product/
│   │   │   │       └── ProductSearchQryExe.java
│   │   │   └── event/
│   │   │       └── handler/
│   │   │           ├── PaymentCompletedHandler.java
│   │   │           └── InventoryDeductedHandler.java
│   │   ├── model/
│   │   │   ├── command/
│   │   │   │   ├── order/
│   │   │   │   │   ├── OrderCreateCmd.java
│   │   │   │   │   ├── OrderCancelCmd.java
│   │   │   │   │   └── OrderPayCmd.java
│   │   │   │   └── product/
│   │   │   │       └── ProductDeductStockCmd.java
│   │   │   ├── query/
│   │   │   │   ├── order/
│   │   │   │   │   ├── OrderDetailQry.java
│   │   │   │   │   └── OrderListQry.java
│   │   │   │   └── product/
│   │   │   │       └── ProductSearchQry.java
│   │   │   └── dto/
│   │   │       ├── OrderDTO.java
│   │   │       └── ProductDTO.java
│   │   ├── service/                              # 非 CQRS 的服务编排
│   │   │   ├── OrderPlacementService.java        # 下单流程编排：校验+锁库存+创建订单+发事件
│   │   │   └── PaymentReconciliationService.java # 对账编排
│   │   └── extension/                            # COLA 扩展点
│   │       ├── point/
│   │       │   └── PaymentMethodExtPt.java       # 支付方式扩展点
│   │       └── impl/
│   │           ├── AlipayPaymentExtension.java
│   │           └── WechatPaymentExtension.java
│   │
│   ├── domain/                                   # 领域层 ★
│   │   ├── order/                                # 订单聚合
│   │   │   ├── Order.java                       # 聚合根
│   │   │   ├── OrderItem.java                   # 实体
│   │   │   ├── OrderId.java                     # 值对象
│   │   │   ├── OrderStatus.java                 # 枚举
│   │   │   ├── event/
│   │   │   │   ├── OrderCreatedEvent.java
│   │   │   │   ├── OrderPaidEvent.java
│   │   │   │   └── OrderCancelledEvent.java
│   │   │   └── repository/
│   │   │       └── OrderRepository.java
│   │   ├── product/                              # 商品聚合
│   │   │   ├── Product.java
│   │   │   ├── ProductId.java
│   │   │   ├── Stock.java                       # 值对象
│   │   │   ├── Category.java
│   │   │   └── repository/
│   │   │       └── ProductRepository.java
│   │   ├── customer/                             # 客户聚合
│   │   │   ├── Customer.java
│   │   │   ├── CustomerId.java
│   │   │   ├── Address.java
│   │   │   └── repository/
│   │   │       └── CustomerRepository.java
│   │   ├── payment/                              # 支付领域（弱实体）
│   │   │   ├── Payment.java
│   │   │   ├── PaymentId.java
│   │   │   ├── PaymentResult.java
│   │   │   └── repository/
│   │   │       └── PaymentRepository.java
│   │   ├── shared/                               # 共享值对象
│   │   │   ├── Money.java
│   │   │   ├── Quantity.java
│   │   │   └── Pageable.java
│   │   ├── gateway/                              # 防腐层接口
│   │   │   ├── InventoryGateway.java
│   │   │   └── PaymentGateway.java
│   │   └── ability/                              # 领域能力 (v5)
│   │       ├── StockReservationAbility.java
│   │       └── PriceCalculationAbility.java
│   │
│   └── infrastructure/                           # 基础设施层
│       ├── config/
│       │   ├── DataSourceConfig.java
│       │   ├── CacheConfig.java
│       │   ├── MQConfig.java
│       │   └── RpcConfig.java
│       ├── persistence/
│       │   ├── order/
│       │   │   ├── OrderRepositoryImpl.java
│       │   │   ├── OrderMapper.java
│       │   │   ├── OrderPO.java
│       │   │   └── OrderConverter.java
│       │   ├── product/
│       │   │   ├── ProductRepositoryImpl.java
│       │   │   ├── ProductMapper.java
│       │   │   ├── ProductPO.java
│       │   │   └── ProductConverter.java
│       │   ├── customer/
│       │   │   ├── CustomerRepositoryImpl.java
│       │   │   ├── CustomerMapper.java
│       │   │   ├── CustomerPO.java
│       │   │   └── CustomerConverter.java
│       │   └── payment/
│       │       ├── PaymentRepositoryImpl.java
│       │       ├── PaymentMapper.java
│       │       ├── PaymentPO.java
│       │       └── PaymentConverter.java
│       ├── gatewayimpl/
│       │   ├── InventoryGatewayImpl.java         # 调用外部库存系统
│       │   └── PaymentGatewayImpl.java           # 调用微信/支付宝
│       ├── external/
│       │   ├── WechatPayClient.java
│       │   ├── AlipayClient.java
│       │   └── LogisticsClient.java
│       └── component/
│           ├── DistributedLock.java
│           └── RateLimiter.java
```

## 包结构说明

| 包 | 内容 | 说明 |
|----|------|------|
| `adapter/` | 按业务域分组的 Controller + 消息消费者 + 定时任务 + RPC Facade | 多协议适配入口 |
| `app/` | 按业务域分组的 Executor + Service + Extension | 复杂业务编排，扩展点路由 |
| `domain/` | 按聚合根分组的 Entity/VO/Repository 接口 + Shared 共享值对象 | 多聚合，聚合间通过 ID 引用 |
| `infrastructure/` | 按业务域分组的 RepositoryImpl/Mapper/PO + 公共组件 | 持久化实现 + 外部服务 + 基础设施组件 |

## COLA 四层职责分工

| 层 | 职责 | 复杂单体特殊注意 |
|----|------|----------------|
| **Adapter** | 多协议适配 (HTTP/MQ/RPC/Job) | 按业务域分 controller 包，避免单文件过大 |
| **Application** | 跨聚合业务编排、事件驱动流程 | `app/service/` 承担 Saga 编排，Executor 只做单聚合操作 |
| **Domain** ★ | 多聚合独立建模，聚合间通过 ID 间接引用 | 严禁跨聚合对象直接引用 (如 `Order.getCustomer()`) |
| **Infrastructure** | 多数据源、外部服务调用、分布式组件 | PO 与 Domain 必须分离，用 Converter 转换 |

## 模块间依赖关系

```
         ┌─────────────────────────────────┐
         │           adapter                │
         │  HTTP / MQ / RPC / Job          │
         └───────────────┬─────────────────┘
                         │ depends
                         ▼
         ┌─────────────────────────────────┐
         │             app                  │
         │  Executor / Service / Extension  │
         └───────┬─────────────────────────┘
                 │ depends
                 ▼
         ┌─────────────────────────────────┐
         │           domain  ★              │
         │  Order / Product / Customer /    │
         │  Payment / Shared               │
         └─────────────────────────────────┘
                         ▲
                         │ depends
         ┌───────────────┴─────────────────┐
         │        infrastructure            │
         │  RepositoryImpl / Gateway /      │
         │  External / Component            │
         └─────────────────────────────────┘
```

依赖方向：`adapter → app → domain ← infrastructure`

聚合间依赖约束：订单聚合通过 `ProductId` 引用商品，不直接持有 `Product` 对象。

## 适用场景

- 项目总代码量 5-15 万行
- 多个 Bounded Context 但共享同一数据库（演进阶段）
- 有复杂业务编排（下单流程涉及订单+库存+支付+物流）
- 团队 5-15 人，后端开发 3-8 人
- 业务规则较复杂，多聚合交互频繁
- 未来可能拆分为微服务，但目前各聚合内聚在单体中

## 优点

- 多聚合在单体中紧密协作，无需 RPC 开销
- 事务管理简单（同数据库本地事务）
- 相比单聚合单体，代码组织更清晰
- 为未来微服务拆分做包级别准备

## 缺点

- App 层编排可能随着业务增长变得复杂（需引入 Saga 模式）
- 单 jar 体积增大，冷启动耗时增加
- 多团队协作时 Git 冲突增加
- 无法独立部署单一聚合
