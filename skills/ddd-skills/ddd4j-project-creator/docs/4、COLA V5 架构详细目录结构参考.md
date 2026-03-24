# COLA V5 架构详细目录结构参考

## 目录

- [1. 单体工程目录结构](#1-单体工程目录结构)
- [2. 大型微服务工程目录结构](#2-大型微服务工程目录结构)
- [3. COLA V5 架构原则与依赖关系](#3-cola-v5-架构原则与依赖关系)
- [4. COLA V5 核心概念](#4-cola-v5-核心概念)

---

## 1. 单体工程目录结构

**适用场景**：中小型应用，单个业务领域，团队规模 5-15 人

以一个订单管理系统为例：

```
order-management-system/
├── pom.xml
├── README.md
│
├── order-start/                          # 启动模块
│   ├── pom.xml
│   └── src/main/java/
│       └── com/example/order/
│           └── OrderApplication.java     # @SpringBootApplication
│
├── order-adapter/                        # 适配器层模块
│   ├── pom.xml
│   └── src/main/java/
│       └── com/example/order/adapter/
│           ├── web/                      # Web适配器
│           │   ├── OrderController.java
│           │   ├── CustomerController.java
│           │   └── ProductController.java
│           │
│           ├── rpc/                      # RPC适配器
│           │   ├── OrderRpcProvider.java
│           │   └── PaymentRpcConsumer.java
│           │
│           ├── job/                      # 定时任务适配器
│           │   └── OrderCleanupScheduler.java
│           │
│           └── message/                  # 消息适配器
│               ├── OrderEventProducer.java
│               └── PaymentEventConsumer.java
│
├── order-app/                            # 应用层模块
│   ├── pom.xml
│   └── src/main/java/
│       └── com/example/order/app/
│           ├── executor/                 # 执行器（CQRS）
│           │   ├── command/
│           │   │   ├── order/
│           │   │   │   ├── OrderCreateCmdExe.java
│           │   │   │   ├── OrderPayCmdExe.java
│           │   │   │   └── OrderCancelCmdExe.java
│           │   │   └── customer/
│           │   │       └── CustomerCreateCmdExe.java
│           │   │
│           │   └── query/
│           │       ├── order/
│           │       │   ├── OrderGetQryExe.java
│           │       │   └── OrderListQryExe.java
│           │       └── customer/
│           │           └── CustomerGetQryExe.java
│           │
│           ├── model/                    # 应用模型
│           │   ├── command/
│           │   │   ├── OrderCreateCmd.java
│           │   │   └── OrderPayCmd.java
│           │   ├── query/
│           │   │   ├── OrderGetQry.java
│           │   │   └── OrderListQry.java
│           │   └── event/
│           │       └── OrderCreatedEvent.java
│           │
│           ├── service/                  # 应用服务
│           │   └── OrderAppService.java
│           │
│           └── extension/                # 扩展点
│               ├── OrderPriceCalculateExtPt.java
│               └── impl/
│                   ├── NormalPriceCalculateExt.java
│                   └── VipPriceCalculateExt.java
│
├── order-domain/                         # 领域层模块
│   ├── pom.xml
│   └── src/main/java/
│       └── com/example/order/domain/
│           ├── model/                    # 领域模型
│           │   ├── entity/
│           │   │   ├── Order.java
│           │   │   ├── OrderItem.java
│           │   │   └── Customer.java
│           │   ├── vo/
│           │   │   ├── Money.java
│           │   │   ├── Address.java
│           │   │   └── OrderStatus.java
│           │   └── event/
│           │       ├── OrderPlacedEvent.java
│           │       └── OrderPaidEvent.java
│           │
│           ├── service/                  # 领域服务
│           │   ├── OrderDomainService.java
│           │   └── PricingDomainService.java
│           │
│           ├── ability/                  # 领域能力
│           │   └── OrderAbility.java
│           │
│           ├── gateway/                  # 领域网关接口
│           │   ├── OrderGateway.java
│           │   ├── CustomerGateway.java
│           │   ├── ProductGateway.java
│           │   └── PaymentGateway.java
│           │
│           └── repository/               # 仓储接口
│               ├── OrderRepository.java
│               ├── CustomerRepository.java
│               └── ProductRepository.java
│
├── order-infrastructure/                 # 基础设施层模块
│   ├── pom.xml
│   └── src/main/java/
│       └── com/example/order/infrastructure/
│           ├── config/                   # 配置
│           │   ├── DatabaseConfig.java
│           │   ├── RedisConfig.java
│           │   └── MQConfig.java
│           │
│           ├── persistence/              # 持久化实现
│           │   ├── OrderRepositoryImpl.java
│           │   ├── CustomerRepositoryImpl.java
│           │   ├── mapper/
│           │   │   ├── OrderMapper.java
│           │   │   └── CustomerMapper.java
│           │   └── entity/
│           │       ├── OrderDO.java
│           │       └── CustomerDO.java
│           │
│           ├── gatewayimpl/              # 网关实现
│           │   ├── OrderGatewayImpl.java
│           │   ├── PaymentGatewayImpl.java
│           │   └── external/
│           │       └── AlipayGatewayImpl.java
│           │
│           ├── external/                 # 外部服务客户端
│           │   └── AlipayClient.java
│           │
│           └── component/                # 基础设施组件
│               ├── lock/
│               │   └── DistributedLock.java
│               └── rateLimiter/
│                   └── RateLimiter.java
│
├── order-common/                         # 通用模块
│   ├── pom.xml
│   └── src/main/java/
│       └── com/example/order/common/
│           ├── constant/
│           │   └── OrderConstant.java
│           ├── exception/
│           │   ├── OrderException.java
│           │   └── ErrorCode.java
│           ├── util/
│           │   └── BeanUtil.java
│           └── annotation/
│               └── ExtensionPoint.java
│
└── order-api/                            # API客户端模块（可选）
    ├── pom.xml
    └── src/main/java/
        └── com/example/order/api/
            ├── OrderApiClient.java
            └── dto/
                └── OrderDTO.java
```

**单体工程 Maven 模块依赖关系**：

```
order-start
    ↓ depends on
order-adapter → order-app → order-domain ← order-infrastructure
    ↓                                                    ↓
order-common ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ┘
    ↓ (optional)
order-api
```

**pom.xml 示例**（父 POM）：

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>order-management-system</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>order-start</module>
        <module>order-adapter</module>
        <module>order-app</module>
        <module>order-domain</module>
        <module>order-infrastructure</module>
        <module>order-common</module>
        <module>order-api</module>
    </modules>

    <properties>
        <cola.framework.version>5.0.0</cola.framework.version>
        <spring.boot.version>3.3.13</spring.boot.version>
    </properties>
</project>
```

---

## 2. 大型微服务工程目录结构

**适用场景**：大型电商平台，多个业务域，团队规模 50+ 人

```
ecommerce-platform/                      # 电商平台根目录
├── pom.xml                              # 父 POM
├── README.md
├── .gitignore
├── docker-compose.yml
│
├── platform-common/                     # 平台通用模块
│   ├── pom.xml
│   └── src/main/java/com/ecommerce/common/
│       ├── constant/
│       ├── exception/
│       ├── util/
│       └── annotation/
│
├── platform-starter/                    # COLA 组件 Starter
│   ├── pom.xml
│   └── src/main/java/com/ecommerce/starter/
│       ├── ExtensionPointAutoConfiguration.java
│       └── AbilityAutoConfiguration.java
│
│
├── services/                            # 微服务目录
│   │
│   ├── user-service/                    # 用户服务
│   │   ├── user-service-start/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/
│   │   │           └── UserApplication.java
│   │   │
│   │   ├── user-service-adapter/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/adapter/
│   │   │           ├── web/
│   │   │           │   ├── UserController.java
│   │   │           │   └── AuthController.java
│   │   │           ├── rpc/
│   │   │           │   └── UserRpcProvider.java
│   │   │           └── message/
│   │   │               └── UserEventProducer.java
│   │   │
│   │   ├── user-service-app/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/app/
│   │   │           ├── executor/
│   │   │           │   ├── command/
│   │   │           │   │   ├── UserRegisterCmdExe.java
│   │   │           │   │   └── UserLoginCmdExe.java
│   │   │           │   └── query/
│   │   │           │       └── UserGetQryExe.java
│   │   │           ├── model/
│   │   │           │   ├── command/
│   │   │           │   └── query/
│   │   │           └── extension/
│   │   │               └── UserValidationExtPt.java
│   │   │
│   │   ├── user-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/domain/
│   │   │           ├── model/
│   │   │           │   ├── entity/
│   │   │           │   │   ├── User.java
│   │   │           │   │   └── UserProfile.java
│   │   │           │   ├── vo/
│   │   │           │   │   ├── UserId.java
│   │   │           │   │   ├── Email.java
│   │   │           │   │   └── PhoneNumber.java
│   │   │           │   └── event/
│   │   │           │       └── UserRegisteredEvent.java
│   │   │           ├── service/
│   │   │           │   └── UserDomainService.java
│   │   │           ├── ability/
│   │   │           │   └── UserAbility.java
│   │   │           ├── gateway/
│   │   │           │   ├── UserGateway.java
│   │   │           │   └── SmsGateway.java
│   │   │           └── repository/
│   │   │               └── UserRepository.java
│   │   │
│   │   ├── user-service-infrastructure/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/infrastructure/
│   │   │           ├── config/
│   │   │           ├── persistence/
│   │   │           │   ├── UserRepositoryImpl.java
│   │   │           │   └── mapper/
│   │   │           │       └── UserMapper.java
│   │   │           ├── gatewayimpl/
│   │   │           │   └── SmsGatewayImpl.java
│   │   │           └── external/
│   │   │               └── SmsClient.java
│   │   │
│   │   ├── user-service-api/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/api/
│   │   │           ├── UserService.java
│   │   │           └── dto/
│   │   │               └── UserDTO.java
│   │   │
│   │   └── pom.xml
│   │
│   ├── product-service/                 # 商品服务
│   │   ├── product-service-start/
│   │   ├── product-service-adapter/
│   │   ├── product-service-app/
│   │   ├── product-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/product/domain/
│   │   │           ├── model/
│   │   │           │   ├── entity/
│   │   │           │   │   ├── Product.java
│   │   │           │   │   ├── Category.java
│   │   │           │   │   └── SKU.java
│   │   │           │   ├── vo/
│   │   │           │   │   ├── Money.java
│   │   │           │   │   └── Quantity.java
│   │   │           │   └── event/
│   │   │           │       └── ProductCreatedEvent.java
│   │   │           ├── service/
│   │   │           │   ├── ProductDomainService.java
│   │   │           │   └── InventoryDomainService.java
│   │   │           ├── ability/
│   │   │           │   └── ProductAbility.java
│   │   │           ├── gateway/
│   │   │           │   ├── ProductGateway.java
│   │   │           │   └── InventoryGateway.java
│   │   │           └── repository/
│   │   │               └── ProductRepository.java
│   │   ├── product-service-infrastructure/
│   │   ├── product-service-api/
│   │   └── pom.xml
│   │
│   ├── order-service/                   # 订单服务
│   │   ├── order-service-start/
│   │   ├── order-service-adapter/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/adapter/
│   │   │           ├── web/
│   │   │           │   ├── OrderController.java
│   │   │           │   └── CartController.java
│   │   │           ├── rpc/
│   │   │           │   ├── OrderRpcProvider.java
│   │   │           │   └── ProductRpcConsumer.java
│   │   │           ├── job/
│   │   │           │   └── OrderExpireScheduler.java
│   │   │           └── message/
│   │   │               ├── OrderEventProducer.java
│   │   │               └── PaymentEventConsumer.java
│   │   │
│   │   ├── order-service-app/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/app/
│   │   │           ├── executor/
│   │   │           │   ├── command/
│   │   │           │   │   ├── order/
│   │   │           │   │   │   ├── OrderCreateCmdExe.java
│   │   │           │   │   │   ├── OrderPayCmdExe.java
│   │   │           │   │   │   └── OrderCancelCmdExe.java
│   │   │           │   │   └── cart/
│   │   │           │   │       └── CartAddCmdExe.java
│   │   │           │   ├── query/
│   │   │           │   │   ├── order/
│   │   │           │   │   │   ├── OrderGetQryExe.java
│   │   │           │   │   │   └── OrderListQryExe.java
│   │   │           │   │   └── cart/
│   │   │           │   │       └── CartGetQryExe.java
│   │   │           │   └── event/
│   │   │           │       └── OrderPaidEventExe.java
│   │   │           ├── model/
│   │   │           │   ├── command/
│   │   │           │   ├── query/
│   │   │           │   ├── event/
│   │   │           │   └── dto/
│   │   │           ├── service/
│   │   │           │   └── OrderAppService.java
│   │   │           └── extension/
│   │   │               ├── OrderPriceCalculateExtPt.java
│   │   │               └── impl/
│   │   │                   ├── NormalPriceCalculateExt.java
│   │   │                   ├── VipPriceCalculateExt.java
│   │   │                   └── PromotionPriceCalculateExt.java
│   │   │
│   │   ├── order-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/domain/
│   │   │           ├── model/
│   │   │           │   ├── entity/
│   │   │           │   │   ├── Order.java
│   │   │           │   │   ├── OrderItem.java
│   │   │           │   │   ├── Cart.java
│   │   │           │   │   └── CartItem.java
│   │   │           │   ├── aggregate/
│   │   │           │   │   └── OrderAggregate.java
│   │   │           │   ├── vo/
│   │   │           │   │   ├── Money.java
│   │   │           │   │   ├── Address.java
│   │   │           │   │   └── OrderStatus.java
│   │   │           │   └── event/
│   │   │           │       ├── OrderCreatedEvent.java
│   │   │           │       ├── OrderPaidEvent.java
│   │   │           │       └── OrderCancelledEvent.java
│   │   │           ├── service/
│   │   │           │   ├── OrderDomainService.java
│   │   │           │   └── PricingDomainService.java
│   │   │           ├── ability/
│   │   │           │   ├── OrderAbility.java
│   │   │           │   └── PaymentAbility.java
│   │   │           ├── gateway/
│   │   │           │   ├── OrderGateway.java
│   │   │           │   ├── ProductGateway.java
│   │   │           │   ├── UserGateway.java
│   │   │           │   └── PaymentGateway.java
│   │   │           └── repository/
│   │   │               └── OrderRepository.java
│   │   │
│   │   ├── order-service-infrastructure/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/infrastructure/
│   │   │           ├── config/
│   │   │           │   ├── DatabaseConfig.java
│   │   │           │   ├── RedisConfig.java
│   │   │           │   ├── KafkaConfig.java
│   │   │           │   └── DubboConfig.java
│   │   │           ├── persistence/
│   │   │           │   ├── OrderRepositoryImpl.java
│   │   │           │   ├── CartRepositoryImpl.java
│   │   │           │   └── mapper/
│   │   │           │       ├── OrderMapper.java
│   │   │           │       └── CartMapper.java
│   │   │           ├── gatewayimpl/
│   │   │           │   ├── ProductGatewayImpl.java
│   │   │           │   ├── UserGatewayImpl.java
│   │   │           │   └── PaymentGatewayImpl.java
│   │   │           └── component/
│   │   │               ├── lock/
│   │   │               ├── rateLimiter/
│   │   │               └── circuitBreaker/
│   │   │
│   │   ├── order-service-api/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/api/
│   │   │           ├── OrderService.java
│   │   │           └── dto/
│   │   │               └── OrderDTO.java
│   │   │
│   │   └── pom.xml
│   │
│   ├── payment-service/                 # 支付服务
│   │   ├── payment-service-start/
│   │   ├── payment-service-adapter/
│   │   ├── payment-service-app/
│   │   ├── payment-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/payment/domain/
│   │   │           ├── model/
│   │   │           │   ├── entity/
│   │   │           │   │   ├── Payment.java
│   │   │           │   │   └── PaymentChannel.java
│   │   │           │   ├── vo/
│   │   │           │   │   ├── Money.java
│   │   │           │   │   └── PaymentStatus.java
│   │   │           │   └── event/
│   │   │           │       └── PaymentCompletedEvent.java
│   │   │           ├── service/
│   │   │           │   └── PaymentDomainService.java
│   │   │           ├── ability/
│   │   │           │   └── PaymentAbility.java
│   │   │           ├── gateway/
│   │   │           │   ├── AlipayGateway.java
│   │   │           │   └── WechatPayGateway.java
│   │   │           └── repository/
│   │   │               └── PaymentRepository.java
│   │   ├── payment-service-infrastructure/
│   │   ├── payment-service-api/
│   │   └── pom.xml
│   │
│   ├── inventory-service/               # 库存服务
│   │   ├── inventory-service-start/
│   │   ├── inventory-service-adapter/
│   │   ├── inventory-service-app/
│   │   ├── inventory-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/inventory/domain/
│   │   │           ├── model/
│   │   │           │   ├── entity/
│   │   │           │   │   └── Inventory.java
│   │   │           │   └── event/
│   │   │           │       └── InventoryDeductedEvent.java
│   │   │           ├── service/
│   │   │           │   └── InventoryDomainService.java
│   │   │           ├── ability/
│   │   │           │   └── InventoryAbility.java
│   │   │           ├── gateway/
│   │   │           │   └── ProductGateway.java
│   │   │           └── repository/
│   │   │               └── InventoryRepository.java
│   │   ├── inventory-service-infrastructure/
│   │   ├── inventory-service-api/
│   │   └── pom.xml
│   │
│   ├── notification-service/            # 通知服务
│   │   ├── notification-service-start/
│   │   ├── notification-service-adapter/
│   │   ├── notification-service-app/
│   │   ├── notification-service-domain/
│   │   ├── notification-service-infrastructure/
│   │   ├── notification-service-api/
│   │   └── pom.xml
│   │
│   └── search-service/                  # 搜索服务
│       ├── search-service-start/
│       ├── search-service-adapter/
│       ├── search-service-app/
│       ├── search-service-domain/
│       ├── search-service-infrastructure/
│       ├── search-service-api/
│       └── pom.xml
│
│
├── gateway/                             # 网关服务
│   ├── gateway-start/
│   │   └── src/main/java/
│   │       └── com/ecommerce/gateway/
│   │           └── GatewayApplication.java
│   ├── gateway-adapter/
│   │   └── src/main/java/
│   │       └── com/ecommerce/gateway/adapter/
│   │           ├── web/
│   │           │   └── GatewayController.java
│   │           └── filter/
│   │               ├── AuthFilter.java
│   │               ├── RateLimitFilter.java
│   │               └── RouteFilter.java
│   ├── gateway-app/
│   ├── gateway-infrastructure/
│   └── pom.xml
│
│
├── shared/                              # 共享服务
│   │
│   ├── auth-service/                    # 认证授权服务
│   │   ├── auth-service-start/
│   │   ├── auth-service-adapter/
│   │   ├── auth-service-app/
│   │   ├── auth-service-domain/
│   │   ├── auth-service-infrastructure/
│   │   └── pom.xml
│   │
│   └── config-service/                  # 配置中心（可选）
│   │   ├── config-service-start/
│   │   └── pom.xml
│
│
├── docs/                                # 文档
│   ├── architecture/
│   │   ├── microservices.md
│   │   └── cola-v5.md
│   ├── api/
│   │   ├── user-service.yaml
│   │   ├── order-service.yaml
│   │   └── payment-service.yaml
│   └── deployment/
│       └── kubernetes/
│
├── scripts/                             # 脚本
│   ├── deploy/
│   │   ├── deploy-dev.sh
│   │   └── deploy-prod.sh
│   └── db/
│       ├── init-user.sql
│       ├── init-order.sql
│       └── init-payment.sql
│
└── docker/                              # Docker 配置
    ├── docker-compose.yml
    └── kubernetes/
        ├── user-service-deployment.yaml
        ├── order-service-deployment.yaml
        └── ingress.yaml
```

**微服务架构特点**：

1. **服务独立部署**：每个服务有独立的启动模块和数据库
2. **服务间通信**：通过 RPC（Dubbo/gRPC）和消息队列（Kafka/RocketMQ）
3. **共享组件**：`platform-common` 和 `platform-starter` 提供通用能力
4. **网关统一入口**：`gateway` 服务处理路由、认证、限流
5. **独立数据库**：每个服务拥有自己的数据库 schema

**微服务依赖关系**（跨服务）：

```
┌─────────────┐      ┌─────────────┐
│  Frontend   │─────▶│   Gateway   │
└─────────────┘      └─────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
    ┌───────────┐   ┌───────────┐   ┌───────────┐
    │    User   │   │   Order   │   │  Product  │
    │  Service  │◀──▶│  Service  │◀──▶│  Service  │
    └───────────┘   └─────┬─────┘   └───────────┘
                          │
                ┌─────────┼─────────┐
                ▼         ▼         ▼
          ┌─────────┐ ┌───────┐ ┌─────────┐
          │ Payment │ │Inventory│ │Notification│
          │ Service │ │ Service│ │  Service │
          └─────────┘ └───────┘ └─────────┘
```

---

## 3. COLA V5 架构原则与依赖关系

### 3.1 CLOA（Clean Object-oriented and Layered Architecture）设计原则

COLA V5 采用"菱形"架构，强调分层和依赖方向：

```
                   ┌─────────────┐
                   │   Adapter   │  ← 适配器层（Web、RPC、Job、MQ）
                   └──────┬──────┘
                          │
                   ┌──────▼──────┐
                   │     App     │  ← 应用层（Executor、Service、Extension）
                   └──────┬──────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
 ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
 │   Domain    │   │  Domain     │   │   Domain    │  ← 领域层（核心）
 │  (Entity)   │   │ (Ability)   │   │  (Gateway)  │
 └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
        │                 │                 ▲
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                   ┌──────▼──────┐
                   │Infrastructure│ ← 基础设施层（DB、MQ、外部服务）
                   └─────────────┘
```

### 3.2 依赖规则（Dependency Rule）

**核心规则**：依赖只能由外向内，内层不依赖外层

```java
// ✓ 正确：Adapter 依赖 App
@RestController
public class OrderController {
    @Autowired
    private OrderCreateCmdExe orderCreateCmdExe;  // App层
}

// ✓ 正确：App 依赖 Domain
@Component
public class OrderCreateCmdExe {
    @Autowired
    private OrderRepository orderRepository;  // Domain层接口
}

// ✓ 正确：Infrastructure 实现 Domain 接口
@Repository
public class OrderRepositoryImpl implements OrderRepository {  // Domain层接口
    // Infrastructure层实现
}

// ✗ 错误：Domain 不能依赖 App
@Entity
public class Order {
    @Autowired
    private OrderAppService appService;  // 错误！Domain层不能依赖App层
}

// ✗ 错误：Domain 不能依赖 Infrastructure
@Entity
public class Order {
    @Autowired
    private OrderMapper orderMapper;  // 错误！Domain层不能依赖Infrastructure
}
```

### 3.3 分层职责

| 层级 | 职责 | 典型组件 | 依赖方向 |
|------|------|----------|----------|
| **Adapter** | 外部交互适配 | Controller、RPC Provider、Scheduler、Listener | → App |
| **App** | 用例编排、业务流程 | Executor（Command/Query）、AppService、Extension | → Domain |
| **Domain** | 核心业务逻辑 | Entity、VO、DomainService、Ability、Gateway接口 | → （只定义接口） |
| **Infrastructure** | 技术实现 | RepositoryImpl、GatewayImpl、ExternalClient | ← Domain（实现接口） |
| **Common** | 通用工具 | Util、Constant、Exception、Annotation | → 被所有层依赖 |

### 3.4 CQRS 模式实现

COLA V5 通过 Executor 模式实现 CQRS：

```java
// 命令（Command）- 修改状态
@Command
public class OrderCreateCmd {
    private String customerId;
    private List<OrderItemDTO> items;
    private Address address;
}

@Component
public class OrderCreateCmdExe {

    @Autowired
    private OrderRepository orderRepository;

    public void execute(OrderCreateCmd cmd) {
        // 1. 创建领域对象
        Order order = Order.create(cmd.getCustomerId(), cmd.getItems());

        // 2. 调用领域服务
        order.place();

        // 3. 持久化
        orderRepository.save(order);
    }
}

// 查询（Query）- 读取状态
@Query
public class OrderGetQry {
    private String orderId;
}

@Component
public class OrderGetQryExe {

    @Autowired
    private OrderGateway orderGateway;

    public OrderDTO execute(OrderGetQry qry) {
        // 直接查询，可以跳过领域模型
        return orderGateway.getOrderById(qry.getOrderId());
    }
}
```

---

## 4. COLA V5 核心概念

### 4.1 扩展点（Extension Point）

**目的**：实现业务逻辑的可扩展性，避免大量 if-else

```java
// 1. 定义扩展点接口（位于 app/extension）
@ExtensionPoint(bizId = "orderPriceCalculate")
public interface OrderPriceCalculateExtPt {

    /**
     * 计算订单价格
     * @param context 价格计算上下文
     * @return 计算后的价格
     */
    Money calculatePrice(PriceCalculateContext context);
}

// 2. 定义扩展上下文
@Data
public class PriceCalculateContext {
    private Order order;
    private Customer customer;
    private String promotionType;
}

// 3. 实现扩展点（位于 app/extension/impl）
@Extension(bizId = "normalOrder")  // 普通订单
public class NormalPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculatePrice(PriceCalculateContext context) {
        // 普通价格计算逻辑
        return context.getOrder().getTotalAmount();
    }
}

@Extension(bizId = "vipOrder")  // VIP 订单
public class VipPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculatePrice(PriceCalculateContext context) {
        // VIP 打折逻辑
        return context.getOrder().getTotalAmount().multiply(0.9);
    }
}

@Extension(bizId = "promotionOrder")  // 促销订单
public class PromotionPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculatePrice(PriceCalculateContext context) {
        // 促销价格计算逻辑
        return context.getOrder().getTotalAmount().multiply(0.8);
    }
}

// 4. 使用扩展点
@Service
public class OrderAppService {

    @Autowired
    private ExtensionExecutor extensionExecutor;

    public Money calculatePrice(Order order, Customer customer) {
        PriceCalculateContext context = new PriceCalculateContext(order, customer);

        // 根据业务场景自动选择对应的扩展实现
        OrderPriceCalculateExtPt extPt = extensionExecutor.execute(
            OrderPriceCalculateExtPt.class,
            customer.getOrderType(),  // bizId
            context
        );

        return extPt.calculatePrice(context);
    }
}
```

**扩展点场景示例**：

| 业务场景 | 扩展点实现 |
|----------|-----------|
| 不同用户类型注册验证 | UserValidationExtPt（NormalUserValidationExt、VipUserValidationExt） |
| 不同支付渠道处理 | PaymentProcessExtPt（AlipayProcessExt、WechatPayProcessExt） |
| 不同物流方式计费 | ShippingFeeCalculateExtPt（ExpressShippingExt、EconomyShippingExt） |
| 不同订单类型优惠 | DiscountCalculateExtPt（NewCustomerDiscountExt、LoyalCustomerDiscountExt） |

### 4.2 领域能力（Ability）

**目的**：封装跨实体的业务能力

```java
// 1. 定义领域能力（位于 domain/ability）
public interface OrderAbility {

    /**
     * 判断订单是否可以支付
     */
    boolean canPay(Order order);

    /**
     * 判断订单是否可以取消
     */
    boolean canCancel(Order order);

    /**
     * 判断用户是否可以创建订单
     */
    boolean canCreateOrder(Customer customer);
}

// 2. 实现领域能力
@Component
public class OrderAbilityImpl implements OrderAbility {

    @Autowired
    private OrderRepository orderRepository;

    @Autowired
    private CustomerRepository customerRepository;

    @Override
    public boolean canPay(Order order) {
        // 检查订单状态
        if (order.getStatus() != OrderStatus.PENDING_PAYMENT) {
            return false;
        }

        // 检查订单是否过期
        if (order.isExpired()) {
            return false;
        }

        // 检查库存
        if (!order.hasStock()) {
            return false;
        }

        return true;
    }

    @Override
    public boolean canCancel(Order order) {
        // 只有未支付和已支付的订单可以取消
        return order.getStatus() == OrderStatus.PENDING_PAYMENT
            || order.getStatus() == OrderStatus.PAID;
    }

    @Override
    public boolean canCreateOrder(Customer customer) {
        // 检查用户状态
        if (!customer.isActive()) {
            return false;
        }

        // 检查用户是否有未支付订单
        List<Order> unpaidOrders = orderRepository.findUnpaidByCustomer(customer.getId());
        if (unpaidOrders.size() >= 3) {
            return false;
        }

        return true;
    }
}

// 3. 在领域服务中使用领域能力
@Service
public class OrderDomainService {

    @Autowired
    private OrderAbility orderAbility;

    public void pay(Order order, Payment payment) {
        // 使用能力进行业务规则验证
        if (!orderAbility.canPay(order)) {
            throw new OrderException("订单当前状态不允许支付");
        }

        // 执行支付逻辑
        order.pay(payment);
    }
}
```

### 4.3 领域网关（Gateway）

**目的**：隔离外部依赖，定义领域层需要的外部能力

```java
// 1. 定义网关接口（位于 domain/gateway）
public interface PaymentGateway {

    /**
     * 发起支付
     */
    PaymentResult initiate(PaymentRequest request);

    /**
     * 查询支付状态
     */
    PaymentStatus queryStatus(String paymentId);
}

public interface ProductGateway {

    /**
     * 获取商品信息
     */
    Product getProduct(String productId);

    /**
     * 锁定库存
     */
    void lockInventory(String productId, int quantity);
}

public interface SmsGateway {

    /**
     * 发送短信
     */
    void sendSms(PhoneNumber phone, String message);
}

// 2. 在基础设施层实现网关（位于 infrastructure/gatewayimpl）
@Repository
public class PaymentGatewayImpl implements PaymentGateway {

    @Autowired
    private AlipayClient alipayClient;

    @Autowired
    private WechatPayClient wechatPayClient;

    @Override
    public PaymentResult initiate(PaymentRequest request) {
        switch (request.getChannel()) {
            case ALIPAY:
                return alipayClient.pay(request);
            case WECHAT:
                return wechatPayClient.pay(request);
            default:
                throw new UnsupportedPaymentChannelException();
        }
    }

    @Override
    public PaymentStatus queryStatus(String paymentId) {
        // 查询支付状态
    }
}

@Component
public class ProductGatewayImpl implements ProductGateway {

    @Autowired
    private ProductServiceClient productServiceClient;  // RPC 客户端

    @Override
    public Product getProduct(String productId) {
        return productServiceClient.getProduct(productId);
    }

    @Override
    public void lockInventory(String productId, int quantity) {
        productServiceClient.lockInventory(productId, quantity);
    }
}

// 3. 在应用层/领域层使用网关
@Component
public class OrderPayCmdExe {

    @Autowired
    private PaymentGateway paymentGateway;

    public void execute(OrderPayCmd cmd) {
        // 通过网关发起支付，不关心具体实现
        PaymentResult result = paymentGateway.initiate(
            new PaymentRequest(cmd.getOrderId(), cmd.getAmount(), cmd.getChannel())
        );

        if (result.isSuccess()) {
            // 支付成功处理
        }
    }
}
```

### 4.4 领域事件（Domain Event）

**目的**：实现领域内的解耦和最终一致性

```java
// 1. 定义领域事件（位于 domain/model/event）
@Data
public class OrderPaidEvent implements DomainEvent {

    private final String orderId;
    private final String customerId;
    private final Money amount;
    private final LocalDateTime occurredOn;

    public OrderPaidEvent(String orderId, String customerId, Money amount) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.amount = amount;
        this.occurredOn = LocalDateTime.now();
    }
}

// 2. 在聚合根中发布事件
@Entity
public class Order {

    private List<DomainEvent> domainEvents = new ArrayList<>();

    public void pay(Payment payment) {
        // 业务逻辑
        this.status = OrderStatus.PAID;
        this.paidTime = LocalDateTime.now();

        // 发布领域事件
        this.domainEvents.add(new OrderPaidEvent(
            this.id,
            this.customerId,
            this.totalAmount
        ));
    }

    public List<DomainEvent> getDomainEvents() {
        return Collections.unmodifiableList(domainEvents);
    }

    public void clearDomainEvents() {
        this.domainEvents.clear();
    }
}

// 3. 事件处理器（位于 app/eventhandler）
@Component
public class OrderEventHandler {

    @Autowired
    private OrderGateway orderGateway;

    @Autowired
    private NotificationGateway notificationGateway;

    @Autowired
    private CustomerGateway customerGateway;

    @EventHandler
    public void handleOrderPaidEvent(OrderPaidEvent event) {
        // 发送支付成功通知
        notificationGateway.sendPaymentSuccessNotification(event.getCustomerId());

        // 更新用户积分
        customerGateway.addPoints(event.getCustomerId(), event.getAmount());
    }
}

// 4. 在仓储中保存事件
@Repository
public class OrderRepositoryImpl implements OrderRepository {

    @Override
    public void save(Order order) {
        // 保存聚合
        orderMapper.insert(order);

        // 发布领域事件
        List<DomainEvent> events = order.getDomainEvents();
        for (DomainEvent event : events) {
            eventPublisher.publish(event);
        }

        // 清除事件
        order.clearDomainEvents();
    }
}
```

### 4.5 仓储（Repository）模式

```java
// 1. 定义仓储接口（位于 domain/repository）
public interface OrderRepository {

    /**
     * 保存订单
     */
    void save(Order order);

    /**
     * 根据 ID 查找订单
     */
    Optional<Order> findById(String orderId);

    /**
     * 查找客户的订单列表
     */
    List<Order> findByCustomerId(String customerId);

    /**
     * 删除订单
     */
    void delete(Order order);
}

// 2. 实现仓储（位于 infrastructure/persistence）
@Repository
public class OrderRepositoryImpl implements OrderRepository {

    @Autowired
    private OrderMapper orderMapper;

    @Autowired
    private OrderItemMapper orderItemMapper;

    @Override
    public void save(Order order) {
        // 保存订单主表
        orderMapper.insert(order);

        // 保存订单明细
        for (OrderItem item : order.getItems()) {
            orderItemMapper.insert(item);
        }

        // 发布领域事件
        publishDomainEvents(order);
    }

    @Override
    public Optional<Order> findById(String orderId) {
        OrderDO orderDO = orderMapper.selectById(orderId);
        if (orderDO == null) {
            return Optional.empty();
        }

        List<OrderItemDO> itemDOs = orderItemMapper.selectByOrderId(orderId);

        // 转换为领域对象
        Order order = OrderConverter.toDomain(orderDO, itemDOs);
        return Optional.of(order);
    }

    @Override
    public List<Order> findByCustomerId(String customerId) {
        List<OrderDO> orderDOs = orderMapper.selectByCustomerId(customerId);
        return orderDOs.stream()
            .map(OrderConverter::toDomain)
            .collect(Collectors.toList());
    }

    @Override
    public void delete(Order order) {
        orderMapper.deleteById(order.getId());
    }
}
```

### 4.6 聚合（Aggregate）模式

```java
// 聚合根（Aggregate Root）
@Entity
public class Order {

    private String orderId;
    private String customerId;
    private Money totalAmount;
    private OrderStatus status;
    private List<OrderItem> items;  // 包含的实体

    // 修改状态的入口点，保证不变式
    public void addItem(Product product, int quantity) {
        // 业务规则检查
        if (this.status != OrderStatus.PENDING) {
            throw new OrderException("只有待处理状态的订单可以添加商品");
        }

        // 添加明细
        OrderItem item = new OrderItem(product, quantity);
        this.items.add(item);

        // 更新总金额（保证不变式）
        recalculateTotal();
    }

    public void removeItem(String itemId) {
        // 检查状态
        if (this.status != OrderStatus.PENDING) {
            throw new OrderException("只有待处理状态的订单可以移除商品");
        }

        // 移除明细
        this.items.removeIf(item -> item.getId().equals(itemId));

        // 更新总金额
        recalculateTotal();
    }

    private void recalculateTotal() {
        this.totalAmount = this.items.stream()
            .map(OrderItem::getSubTotal)
            .reduce(Money.ZERO, Money::add);
    }

    public void place() {
        // 业务规则验证
        if (items.isEmpty()) {
            throw new OrderException("订单不能为空");
        }

        if (totalAmount.isZero()) {
            throw new OrderException("订单金额必须大于0");
        }

        // 状态变更
        this.status = OrderStatus.PLACED;

        // 发布领域事件
        this.domainEvents.add(new OrderPlacedEvent(this.orderId));
    }
}

// 聚合内的实体
@Entity
public class OrderItem {
    private String itemId;
    private String productId;
    private String productName;
    private Money unitPrice;
    private int quantity;
    private Money subTotal;

    // 只能通过聚合根操作
    protected OrderItem(Product product, int quantity) {
        this.productId = product.getId();
        this.productName = product.getName();
        this.unitPrice = product.getPrice();
        this.quantity = quantity;
        this.subTotal = unitPrice.multiply(quantity);
    }

    public void increaseQuantity(int delta) {
        this.quantity += delta;
        this.subTotal = this.unitPrice.multiply(this.quantity);
    }
}
```

---

## 总结

COLA V5 架构的核心价值：

1. **分层清晰**：Adapter → App → Domain ← Infrastructure，职责明确
2. **依赖单向**：外层依赖内层，通过接口反转依赖
3. **高度扩展**：Extension Point 机制支持业务逻辑动态扩展
4. **能力封装**：Ability 模式封装跨实体业务规则
5. **CQRS 分离**：命令和查询执行器分离，优化读写性能
6. **防腐层设计**：Gateway 隔离外部依赖，保护领域模型纯净

无论是单体应用还是微服务架构，COLA V5 都能提供一致的分层和代码组织方式，帮助团队构建可维护、可扩展的企业级应用。
