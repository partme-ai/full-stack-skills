# DDD 经典分层架构目录结构参考

## 目录

- [1. 单体工程目录结构](#1-单体工程目录结构)
- [2. 大型微服务工程目录结构](#2-大型微服务工程目录结构)
- [3. DDD 经典分层架构原则与依赖关系](#3-ddd-经典分层架构原则与依赖关系)
- [4. DDD 核心概念](#4-ddd-核心概念)

---

## 1. 单体工程目录结构

**适用场景**：中小型应用，单个业务领域，团队规模 5-15 人

以一个订单管理系统为例：

```
order-management-system/
├── pom.xml
├── README.md
│
├── src/main/java/
│   └── com/example/order/
│       │
│       ├── OrderApplication.java             # 应用启动类
│       │
│       ├── interfaces/                       # 接口层（用户界面层）
│       │   ├── web/                          # Web接口
│       │   │   ├── controller/
│       │   │   │   ├── OrderController.java
│       │   │   │   │   ├── @RestController
│       │   │   │   │   ├── @RequestMapping("/api/orders")
│       │   │   │   │   ├── placeOrder(@RequestBody)
│       │   │   │   │   ├── getOrder(@PathVariable)
│       │   │   │   │   └── cancelOrder(@PathVariable)
│       │   │   │   │
│       │   │   │   ├── CustomerController.java
│       │   │   │   └── ProductController.java
│       │   │   │
│       │   │   ├── dto/
│       │   │   │   ├── request/
│       │   │   │   │   ├── PlaceOrderRequest.java
│       │   │   │   │   ├── PayOrderRequest.java
│       │   │   │   │   └── RegisterCustomerRequest.java
│       │   │   │   │
│       │   │   │   ├── response/
│       │   │   │   │   ├── OrderResponse.java
│       │   │   │   │   ├── CustomerResponse.java
│       │   │   │   │   └── ApiResponse.java
│       │   │   │   │
│       │   │   │   └── assembler/
│       │   │   │       ├── OrderAssembler.java
│       │   │   │       └── CustomerAssembler.java
│       │   │   │
│       │   │   ├── filter/
│       │   │   │   ├── AuthenticationFilter.java
│       │   │   │   └── LoggingFilter.java
│       │   │   │
│       │   │   └── advice/
│       │   │       └── GlobalExceptionHandler.java
│       │   │
│       │   └── rpc/                          # RPC接口（可选）
│       │       ├── OrderRpcProvider.java
│       │       └── PaymentRpcConsumer.java
│       │
│       ├── application/                      # 应用层（用例编排）
│       │   ├── service/
│       │   │   ├── OrderApplicationService.java
│       │   │   │   ├── placeOrder(PlaceOrderCommand): OrderId
│       │   │   │   ├── payOrder(PayOrderCommand): void
│       │   │   │   └── cancelOrder(CancelOrderCommand): void
│       │   │   │
│       │   │   ├── CustomerApplicationService.java
│       │   │   └── ProductApplicationService.java
│       │   │
│       │   ├── command/                      # 命令对象（CQRS）
│       │   │   ├── PlaceOrderCommand.java
│       │   │   ├── PayOrderCommand.java
│       │   │   └── CancelOrderCommand.java
│       │   │
│       │   ├── query/                        # 查询对象（CQRS）
│       │   │   ├── GetOrderQuery.java
│       │   │   ├── OrderListQuery.java
│       │   │   └── CustomerQuery.java
│       │   │
│       │   ├── handler/                      # 命令/查询处理器
│       │   │   ├── commandhandler/
│       │   │   │   ├── PlaceOrderCommandHandler.java
│       │   │   │   ├── PayOrderCommandHandler.java
│       │   │   │   └── CancelOrderCommandHandler.java
│       │   │   │
│       │   │   └── queryhandler/
│       │   │       ├── GetOrderQueryHandler.java
│       │   │       └── OrderListQueryHandler.java
│       │   │
│       │   ├── dto/                          # 应用层DTO
│       │   │   ├── OrderDTO.java
│       │   │   ├── CustomerDTO.java
│       │   │   └── ProductDTO.java
│       │   │
│       │   └── eventhandler/                 # 应用事件处理器
│       │       ├── OrderPlacedEventHandler.java
│       │       ├── OrderPaidEventHandler.java
│       │       └── CustomerRegisteredEventHandler.java
│       │
│       ├── domain/                           # 领域层（核心业务逻辑）
│       │   ├── model/                        # 领域模型
│       │   │   ├── aggregate/                # 聚合
│       │   │   │   ├── order/
│       │   │   │   │   ├── Order.java        # 聚合根
│       │   │   │   │   │   ├── OrderId
│       │   │   │   │   │   ├── CustomerId
│       │   │   │   │   │   ├── OrderItems
│       │   │   │   │   │   ├── OrderStatus
│       │   │   │   │   │   ├── place()
│       │   │   │   │   │   ├── pay()
│       │   │   │   │   │   ├── cancel()
│       │   │   │   │   │   └── calculateTotal()
│       │   │   │   │   │
│       │   │   │   │   └── OrderItem.java    # 实体
│       │   │   │   │
│       │   │   │   ├── customer/
│       │   │   │   │   ├── Customer.java    # 聚合根
│       │   │   │   │   └── CustomerId.java
│       │   │   │   │
│       │   │   │   └── product/
│       │   │   │       └── Product.java     # 聚合根
│       │   │   │
│       │   │   ├── valueobject/              # 值对象
│       │   │   │   ├── Money.java
│       │   │   │   ├── Email.java
│       │   │   │   ├── Address.java
│       │   │   │   ├── PhoneNumber.java
│       │   │   │   └── Quantity.java
│       │   │   │
│       │   │   └── event/                    # 领域事件
│       │   │       ├── DomainEvent.java
│       │   │       ├── OrderPlacedEvent.java
│       │   │       ├── OrderPaidEvent.java
│       │   │       └── CustomerRegisteredEvent.java
│       │   │
│       │   ├── service/                      # 领域服务
│       │   │   ├── OrderDomainService.java
│       │   │   ├── PricingDomainService.java
│       │   │   └── InventoryDomainService.java
│       │   │
│       │   ├── repository/                   # 仓储接口
│       │   │   ├── OrderRepository.java
│       │   │   ├── CustomerRepository.java
│       │   │   └── ProductRepository.java
│       │   │
│       │   ├── specification/                # 规约模式
│       │   │   ├── Specification.java
│       │   │   ├── CustomerSpecification.java
│       │   │   └── OrderSpecification.java
│       │   │
│       │   └── factory/                      # 工厂模式
│       │       ├── OrderFactory.java
│       │       └── CustomerFactory.java
│       │
│       ├── infrastructure/                   # 基础设施层（技术实现）
│       │   ├── persistence/                  # 持久化
│       │   │   ├── repository/
│       │   │   │   ├── JpaOrderRepository.java
│       │   │   │   ├── JpaCustomerRepository.java
│       │   │   │   └── MyBatisProductRepository.java
│       │   │   │
│       │   │   ├── entity/                   # 持久化实体
│       │   │   │   ├── OrderEntity.java
│       │   │   │   ├── CustomerEntity.java
│       │   │   │   └── ProductEntity.java
│       │   │   │
│       │   │   ├── mapper/
│       │   │   │   ├── OrderMapper.java
│       │   │   │   └── CustomerMapper.java
│       │   │   │
│       │   │   └── dao/
│       │   │       ├── OrderDao.java
│       │   │       └── CustomerDao.java
│       │   │
│       │   ├── messaging/                    # 消息传递
│       │   │   ├── eventpublisher/
│       │   │   │   ├── KafkaEventPublisher.java
│       │   │   │   └── DomainEventPublisherImpl.java
│       │   │   │
│       │   │   └── eventconsumer/
│       │   │       └── OrderEventConsumer.java
│       │   │
│       │   ├── external/                     # 外部服务集成
│       │   │   ├── payment/
│       │   │   │   ├── PaymentService.java
│       │   │   │   ├── AlipayPaymentService.java
│       │   │   │   └── WechatPaymentService.java
│       │   │   │
│       │   │   └── notification/
│       │   │       ├── EmailService.java
│       │   │       └── SMSService.java
│       │   │
│       │   ├── cache/                        # 缓存
│       │   │   ├── RedisCache.java
│       │   │   └── CacheProvider.java
│       │   │
│       │   ├── config/
│       │   │   ├── PersistenceConfig.java
│       │   │   ├── MessagingConfig.java
│       │   │   └── CacheConfig.java
│       │   │
│       │   └── security/
│       │       ├── JwtTokenProvider.java
│       │       └── PasswordEncoder.java
│       │
│       └── shared/                           # 共享组件
│           ├── kernel/
│           │   ├── AggregateRoot.java
│           │   ├── ValueObject.java
│           │   └── Entity.java
│           │
│           ├── util/
│           │   ├── Assert.java
│           │   └── ValidationUtils.java
│           │
│           └── constant/
│               └── AppConstants.java
│
├── src/test/java/
│   ├── unit/
│   │   ├── domain/
│   │   │   ├── OrderTest.java
│   │   │   └── CustomerTest.java
│   │   ├── application/
│   │   │   └── OrderApplicationServiceTest.java
│   │   └── interfaces/
│   │       └── OrderControllerTest.java
│   │
│   └── integration/
│       ├── OrderIntegrationTest.java
│       └── PaymentIntegrationTest.java
│
├── src/main/resources/
│   ├── application.yml
│   ├── application-dev.yml
│   ├── application-prod.yml
│   ├── db/migration/
│   │   ├── V1__init_schema.sql
│   │   └── V2__create_tables.sql
│   └── mapper/
│       ├── OrderMapper.xml
│       └── CustomerMapper.xml
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── docs/
│   ├── architecture/
│   │   └── ddd-architecture.md
│   └── api/
│       └── openapi.yaml
│
└── .gitignore
```

**单体工程 Maven 模块依赖关系**：

```
src/main/java/
    └── com/example/order/
        interfaces（接口层）
            ↓ 依赖
        application（应用层）
            ↓ 依赖
        domain（领域层）
            ↑ 依赖（通过接口）
        infrastructure（基础设施层）
            ↓ 依赖
        shared（共享组件）
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
│       ├── kernel/
│       │   ├── AggregateRoot.java
│       │   ├── ValueObject.java
│       │   └── Entity.java
│       ├── util/
│       │   ├── Assert.java
│       │   └── ValidationUtils.java
│       ├── constant/
│       │   └── AppConstants.java
│       └── exception/
│           └── SystemException.java
│
├── services/                            # 微服务目录
│   │
│   ├── user-service/                    # 用户服务
│   │   ├── user-service-api/            # 服务 API 模块
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/api/
│   │   │           ├── UserService.java
│   │   │           ├── dto/
│   │   │           │   ├── UserDTO.java
│   │   │           │   └── RegisterUserRequest.java
│   │   │           └── facade/
│   │   │               └── UserFacade.java
│   │   │
│   │   ├── user-service-domain/         # 领域模块
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/domain/
│   │   │           ├── model/
│   │   │           │   ├── aggregate/
│   │   │           │   │   └── User.java
│   │   │           │   ├── valueobject/
│   │   │           │   │   ├── UserId.java
│   │   │           │   │   ├── Email.java
│   │   │           │   │   └── PhoneNumber.java
│   │   │           │   └── event/
│   │   │           │       └── UserRegisteredEvent.java
│   │   │           │
│   │   │           ├── service/
│   │   │           │   ├── UserDomainService.java
│   │   │           │   └── AuthenticationDomainService.java
│   │   │           │
│   │   │           ├── repository/
│   │   │           │   └── UserRepository.java
│   │   │           │
│   │   │           └── specification/
│   │   │               └── UserSpecification.java
│   │   │
│   │   ├── user-service-application/    # 应用模块
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/application/
│   │   │           ├── service/
│   │   │           │   └── UserApplicationService.java
│   │   │           │
│   │   │           ├── command/
│   │   │           │   ├── RegisterUserCommand.java
│   │   │           │   └── LoginCommand.java
│   │   │           │
│   │   │           ├── query/
│   │   │           │   └── GetUserQuery.java
│   │   │           │
│   │   │           ├── handler/
│   │   │           │   ├── commandhandler/
│   │   │           │   │   ├── RegisterUserCommandHandler.java
│   │   │           │   │   └── LoginCommandHandler.java
│   │   │           │   │
│   │   │           │   └── queryhandler/
│   │   │           │       └── GetUserQueryHandler.java
│   │   │           │
│   │   │           └── eventhandler/
│   │   │               └── UserRegisteredEventHandler.java
│   │   │
│   │   ├── user-service-infrastructure/ # 基础设施模块
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/infrastructure/
│   │   │           ├── persistence/
│   │   │           │   ├── repository/
│   │   │           │   │   └── JpaUserRepository.java
│   │   │           │   ├── entity/
│   │   │           │   │   └── UserEntity.java
│   │   │           │   └── mapper/
│   │   │           │       └── UserMapper.java
│   │   │           │
│   │   │           ├── messaging/
│   │   │           │   ├── eventpublisher/
│   │   │           │   │   └── KafkaUserEventPublisher.java
│   │   │           │   │
│   │   │           │   └── eventconsumer/
│   │   │           │       └── UserEventConsumer.java
│   │   │           │
│   │   │           ├── external/
│   │   │           │   ├── notification/
│   │   │           │   │   ├── EmailService.java
│   │   │           │   │   └── SMSService.java
│   │   │           │   │
│   │   │           │   └── verification/
│   │   │           │       └── SmsVerificationService.java
│   │   │           │
│   │   │           ├── cache/
│   │   │           │   └── RedisUserCache.java
│   │   │           │
│   │   │           └── config/
│   │   │               ├── PersistenceConfig.java
│   │   │               └── MessagingConfig.java
│   │   │
│   │   ├── user-service-interfaces/     # 接口模块
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/user/interfaces/
│   │   │           ├── web/
│   │   │           │   ├── controller/
│   │   │           │   │   ├── UserController.java
│   │   │           │   │   └── AuthController.java
│   │   │           │   │
│   │   │           │   ├── dto/
│   │   │           │   │   ├── request/
│   │   │           │   │   │   ├── RegisterUserRequest.java
│   │   │           │   │   │   └── LoginRequest.java
│   │   │           │   │   │
│   │   │           │   │   └── response/
│   │   │           │   │       ├── UserResponse.java
│   │   │           │   │       └── TokenResponse.java
│   │   │           │   │
│   │   │           │   └── assembler/
│   │   │           │       └── UserAssembler.java
│   │   │           │
│   │   │           └── rpc/
│   │   │               ├── UserRpcProvider.java
│   │   │               └── OrderRpcConsumer.java
│   │   │
│   │   └── user-service-start/           # 启动模块
│   │       └── src/main/java/
│   │           └── com/ecommerce/user/
│   │               └── UserApplication.java
│   │
│   │   └── pom.xml
│   │
│   ├── order-service/                   # 订单服务
│   │   ├── order-service-api/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/api/
│   │   │           ├── OrderService.java
│   │   │           └── dto/
│   │   │               ├── OrderDTO.java
│   │   │               └── PlaceOrderRequest.java
│   │   │
│   │   ├── order-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/domain/
│   │   │           ├── model/
│   │   │           │   ├── aggregate/
│   │   │           │   │   ├── Order.java       # 聚合根
│   │   │           │   │   ├── OrderItem.java   # 实体
│   │   │           │   │   └── Cart.java        # 聚合根
│   │   │           │   │
│   │   │           │   ├── valueobject/
│   │   │           │   │   ├── Money.java
│   │   │           │   │   ├── Address.java
│   │   │           │   │   └── OrderStatus.java
│   │   │           │   │
│   │   │           │   └── event/
│   │   │           │       ├── OrderPlacedEvent.java
│   │   │           │       ├── OrderPaidEvent.java
│   │   │           │       └── OrderCancelledEvent.java
│   │   │           │
│   │   │           ├── service/
│   │   │           │   ├── OrderDomainService.java
│   │   │           │   ├── PricingDomainService.java
│   │   │           │   └── PaymentDomainService.java
│   │   │           │
│   │   │           ├── repository/
│   │   │           │   ├── OrderRepository.java
│   │   │           │   └── CartRepository.java
│   │   │           │
│   │   │           └── specification/
│   │   │               └── OrderSpecification.java
│   │   │
│   │   ├── order-service-application/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/application/
│   │   │           ├── service/
│   │   │           │   ├── OrderApplicationService.java
│   │   │           │   └── CartApplicationService.java
│   │   │           │
│   │   │           ├── command/
│   │   │           │   ├── PlaceOrderCommand.java
│   │   │           │   ├── PayOrderCommand.java
│   │   │           │   └── CancelOrderCommand.java
│   │   │           │
│   │   │           ├── query/
│   │   │           │   ├── GetOrderQuery.java
│   │   │           │   └── OrderListQuery.java
│   │   │           │
│   │   │           ├── handler/
│   │   │           │   ├── commandhandler/
│   │   │           │   │   ├── PlaceOrderCommandHandler.java
│   │   │           │   │   ├── PayOrderCommandHandler.java
│   │   │           │   │   └── CancelOrderCommandHandler.java
│   │   │           │   │
│   │   │           │   └── queryhandler/
│   │   │           │       ├── GetOrderQueryHandler.java
│   │   │           │       └── OrderListQueryHandler.java
│   │   │           │
│   │   │           ├── coordinator/
│   │   │           │   └── OrderProcessingCoordinator.java
│   │   │           │
│   │   │           └── eventhandler/
│   │   │               ├── OrderPlacedEventHandler.java
│   │   │               └── OrderPaidEventHandler.java
│   │   │
│   │   ├── order-service-infrastructure/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/infrastructure/
│   │   │           ├── persistence/
│   │   │           │   ├── repository/
│   │   │           │   │   ├── JpaOrderRepository.java
│   │   │           │   │   └── JpaCartRepository.java
│   │   │           │   ├── entity/
│   │   │           │   │   ├── OrderEntity.java
│   │   │           │   │   └── CartEntity.java
│   │   │           │   └── mapper/
│   │   │           │       ├── OrderMapper.java
│   │   │           │       └── CartMapper.java
│   │   │           │
│   │   │           ├── messaging/
│   │   │           │   ├── eventpublisher/
│   │   │           │   │   └── KafkaOrderEventPublisher.java
│   │   │           │   │
│   │   │           │   └── eventconsumer/
│   │   │           │       ├── PaymentEventConsumer.java
│   │   │           │       └── UserEventConsumer.java
│   │   │           │
│   │   │           ├── external/
│   │   │           │   ├── payment/
│   │   │           │   │   ├── PaymentGatewayClient.java
│   │   │           │   │   └── AlipayClient.java
│   │   │           │   │
│   │   │           │   ├── inventory/
│   │   │           │   │   └── InventoryServiceClient.java
│   │   │           │   │
│   │   │           │   └── notification/
│   │   │           │       └── NotificationServiceClient.java
│   │   │           │
│   │   │           ├── cache/
│   │   │           │   └── RedisOrderCache.java
│   │   │           │
│   │   │           └── config/
│   │   │               ├── PersistenceConfig.java
│   │   │               ├── MessagingConfig.java
│   │   │               └── ExternalServiceConfig.java
│   │   │
│   │   ├── order-service-interfaces/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/order/interfaces/
│   │   │           ├── web/
│   │   │           │   ├── controller/
│   │   │           │   │   ├── OrderController.java
│   │   │           │   │   └── CartController.java
│   │   │           │   │
│   │   │           │   ├── dto/
│   │   │           │   │   ├── request/
│   │   │           │   │   │   ├── PlaceOrderRequest.java
│   │   │           │   │   │   └── PayOrderRequest.java
│   │   │           │   │   │
│   │   │           │   │   ├── response/
│   │   │           │   │   │   ├── OrderResponse.java
│   │   │           │   │   │   └── CartResponse.java
│   │   │           │   │   │
│   │   │           │   │   └── assembler/
│   │   │           │   │       └── OrderAssembler.java
│   │   │           │   │
│   │   │           │   └── advice/
│   │   │           │       └── GlobalExceptionHandler.java
│   │   │           │
│   │   │           └── rpc/
│   │   │               ├── OrderRpcProvider.java
│   │   │               └── ProductRpcConsumer.java
│   │   │
│   │   └── order-service-start/
│   │       └── src/main/java/
│   │           └── com/ecommerce/order/
│   │               └── OrderApplication.java
│   │
│   │   └── pom.xml
│   │
│   ├── product-service/                 # 商品服务
│   │   ├── product-service-api/
│   │   ├── product-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/product/domain/
│   │   │           ├── model/
│   │   │           │   ├── aggregate/
│   │   │           │   │   ├── Product.java
│   │   │           │   │   └── Category.java
│   │   │           │   │
│   │   │           │   ├── valueobject/
│   │   │           │   │   ├── Money.java
│   │   │           │   │   └── Quantity.java
│   │   │           │   │
│   │   │           │   └── event/
│   │   │           │       └── ProductCreatedEvent.java
│   │   │           │
│   │   │           ├── service/
│   │   │           │   ├── ProductDomainService.java
│   │   │           │   └── InventoryDomainService.java
│   │   │           │
│   │   │           └── repository/
│   │   │               └── ProductRepository.java
│   │   │
│   │   ├── product-service-application/
│   │   ├── product-service-infrastructure/
│   │   ├── product-service-interfaces/
│   │   └── product-service-start/
│   │
│   ├── payment-service/                 # 支付服务
│   │   ├── payment-service-api/
│   │   ├── payment-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/payment/domain/
│   │   │           ├── model/
│   │   │           │   ├── aggregate/
│   │   │           │   │   └── Payment.java
│   │   │           │   │
│   │   │           │   ├── valueobject/
│   │   │           │   │   ├── Money.java
│   │   │           │   │   └── PaymentStatus.java
│   │   │           │   │
│   │   │           │   └── event/
│   │   │           │       └── PaymentCompletedEvent.java
│   │   │           │
│   │   │           ├── service/
│   │   │           │   └── PaymentDomainService.java
│   │   │           │
│   │   │           └── repository/
│   │   │               └── PaymentRepository.java
│   │   │
│   │   ├── payment-service-application/
│   │   ├── payment-service-infrastructure/
│   │   ├── payment-service-interfaces/
│   │   └── payment-service-start/
│   │
│   ├── inventory-service/               # 库存服务
│   │   ├── inventory-service-api/
│   │   ├── inventory-service-domain/
│   │   │   └── src/main/java/
│   │   │       └── com/ecommerce/inventory/domain/
│   │   │           ├── model/
│   │   │           │   ├── aggregate/
│   │   │           │   │   └── Inventory.java
│   │   │           │   │
│   │   │           │   └── event/
│   │   │           │       └── InventoryDeductedEvent.java
│   │   │           │
│   │   │           ├── service/
│   │   │           │   └── InventoryDomainService.java
│   │   │           │
│   │   │           └── repository/
│   │   │               └── InventoryRepository.java
│   │   │
│   │   ├── inventory-service-application/
│   │   ├── inventory-service-infrastructure/
│   │   ├── inventory-service-interfaces/
│   │   └── inventory-service-start/
│   │
│   └── notification-service/            # 通知服务
│       ├── notification-service-api/
│       ├── notification-service-domain/
│       ├── notification-service-application/
│       ├── notification-service-infrastructure/
│       ├── notification-service-interfaces/
│       └── notification-service-start/
│
│
├── gateway/                             # 网关服务
│   ├── gateway-start/
│   │   └── src/main/java/
│   │       └── com/ecommerce/gateway/
│   │           └── GatewayApplication.java
│   ├── gateway-interfaces/
│   │   └── src/main/java/
│   │       └── com/ecommerce/gateway/interfaces/
│   │           ├── web/
│   │           │   ├── controller/
│   │           │   │   └── GatewayController.java
│   │           │   └── filter/
│   │           │       ├── AuthFilter.java
│   │           │       ├── RateLimitFilter.java
│   │           │       └── RoutingFilter.java
│   │           └── rpc/
│   └── pom.xml
│
│
├── shared/                              # 共享服务
│   │
│   ├── auth-service/                    # 认证授权服务
│   │   ├── auth-service-api/
│   │   ├── auth-service-domain/
│   │   ├── auth-service-application/
│   │   ├── auth-service-infrastructure/
│   │   ├── auth-service-interfaces/
│   │   └── auth-service-start/
│   │
│   └── config-service/                  # 配置中心（可选）
│       └── config-service-start/
│
│
├── docs/                                # 文档
│   ├── architecture/
│   │   ├── ddd-architecture.md
│   │   ├── bounded-contexts.md
│   │   └── microservices.md
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
3. **共享组件**：`platform-common` 提供通用能力
4. **网关统一入口**：`gateway` 服务处理路由、认证、限流
5. **独立数据库**：每个服务拥有自己的数据库 schema
6. **模块化设计**：每个服务内部按 DDD 四层架构组织

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

## 3. DDD 经典分层架构原则与依赖关系

### 3.1 经典四层架构

DDD 经典分层架构由 Eric Evans 在《领域驱动设计》一书中提出：

```
┌─────────────────────────────────────────────────────────┐
│                    接口层 (Interfaces)                    │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │
│  │   Web   │  │   RPC   │  │   CLI   │  │ GraphQL │   │
│  │Controller│  │Provider │  │   API   │  │Resolver │   │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │
└────────────────────────┬────────────────────────────────┘
                         │
                         ↓ 依赖
┌─────────────────────────────────────────────────────────┐
│                   应用层 (Application)                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │Application│  │ Command  │  │  Query   │  │Event    │ │
│  │ Service   │  │ Handler  │  │ Handler  │  │Handler  │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
└────────────────────────┬────────────────────────────────┘
                         │
                         ↓ 依赖
┌─────────────────────────────────────────────────────────┐
│                    领域层 (Domain)                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │ Aggregate│  │  Entity  │  │Value Obj.│  │Domain   │ │
│  │   Root   │  │          │  │          │  │Service  │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │ Repository│  │ Specifi. │  │ Factory  │               │
│  │(Interface)│  │   cation │  │          │               │
│  └──────────┘  └──────────┘  └──────────┘               │
└────────────────────────┬────────────────────────────────┘
                         ↑
                         │ 实现接口
┌────────────────────────┴────────────────────────────────┐
│                 基础设施层 (Infrastructure)                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │Repository│  │ Messaging│  │  Cache   │  │External │ │
│  │ Impl.    │  │ Publisher │  │ Provider │  │Service  │ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
└─────────────────────────────────────────────────────────┘
```

### 3.2 依赖规则

**核心规则**：依赖只能由外向内，领域层不依赖任何外层

```java
// ✓ 正确：接口层 依赖 应用层
@RestController
public class OrderController {
    @Autowired
    private OrderApplicationService orderApplicationService;  // 应用层
}

// ✓ 正确：应用层 依赖 领域层
@Service
public class OrderApplicationService {
    @Autowired
    private OrderRepository orderRepository;  // 领域层接口
}

// ✓ 正确：基础设施层 实现 领域层接口
@Repository
public class JpaOrderRepository implements OrderRepository {  // 领域层接口
    // 基础设施层实现
}

// ✗ 错误：领域层不能依赖应用层
@Entity
public class Order {
    @Autowired
    private OrderApplicationService appService;  // 错误！
}

// ✗ 错误：领域层不能依赖基础设施层
@Entity
public class Order {
    @Autowired
    private OrderMapper orderMapper;  // 错误！
}
```

### 3.3 各层职责

| 层级 | 职责 | 典型组件 | 依赖方向 |
|------|------|----------|----------|
| **Interfaces** | 外部交互、数据转换 | Controller、DTO、Filter、Advice | → Application |
| **Application** | 用例编排、流程协调 | ApplicationService、Command/Query Handler | → Domain |
| **Domain** | 核心业务逻辑 | Aggregate、Entity、ValueObject、DomainService | → （只定义接口） |
| **Infrastructure** | 技术实现、外部集成 | Repository Impl、Event Publisher、External Client | ← Domain（实现接口） |

### 3.4 CQRS 模式实现

DDD 架构通常结合 CQRS（Command Query Responsibility Segregation）模式：

```java
// 命令（Command）- 修改状态
public class PlaceOrderCommand {
    private String customerId;
    private List<OrderItemDTO> items;
    private Address shippingAddress;
}

@Component
public class PlaceOrderCommandHandler {

    @Autowired
    private OrderRepository orderRepository;

    @Autowired
    private ProductRepository productRepository;

    public OrderId handle(PlaceOrderCommand command) {
        // 1. 创建领域对象
        Customer customer = customerRepository.findById(new CustomerId(command.getCustomerId()));
        Order order = Order.place(customer, command.getItems());

        // 2. 调用领域服务
        order.validate();

        // 3. 持久化
        orderRepository.save(order);

        return order.getId();
    }
}

// 查询（Query）- 读取状态
public class GetOrderQuery {
    private String orderId;
}

@Component
public class GetOrderQueryHandler {

    @Autowired
    private OrderQueryRepository orderQueryRepository;  // 独立的查询仓储

    public OrderDTO handle(GetOrderQuery query) {
        // 直接查询，可以跳过领域模型
        return orderQueryRepository.findById(query.getOrderId());
    }
}
```

---

## 4. DDD 核心概念

### 4.1 聚合（Aggregate）和聚合根（Aggregate Root）

**目的**：定义一致性边界和数据修改边界

```java
// 聚合根：Order
@Entity
public class Order extends AggregateRoot {

    private OrderId orderId;
    private CustomerId customerId;
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

    public void place() {
        // 业务规则验证
        if (items.isEmpty()) {
            throw new OrderException("订单不能为空");
        }

        // 状态变更
        this.status = OrderStatus.PLACED;

        // 发布领域事件
        registerEvent(new OrderPlacedEvent(this.orderId));
    }

    private void recalculateTotal() {
        this.totalAmount = this.items.stream()
            .map(OrderItem::getSubTotal)
            .reduce(Money.ZERO, Money::add);
    }
}

// 聚合内的实体：OrderItem
@Entity
public class OrderItem {

    private OrderItemId itemId;
    private ProductId productId;
    private Money unitPrice;
    private int quantity;
    private Money subTotal;

    // 只能通过聚合根操作
    protected OrderItem(Product product, int quantity) {
        this.productId = product.getId();
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

### 4.2 实体（Entity）和值对象（Value Object）

```java
// 实体：有唯一标识，可变
@Entity
public class Customer {

    private CustomerId id;  // 唯一标识

    private String name;
    private Email email;
    private PhoneNumber phone;

    // 可变性：状态可以改变
    public void changeName(String newName) {
        if (newName == null || newName.isEmpty()) {
            throw new IllegalArgumentException("姓名不能为空");
        }
        this.name = newName;
    }

    // 相等性：通过 ID 判断
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Customer customer = (Customer) obj;
        return id.equals(customer.id);
    }
}

// 值对象：无唯一标识，不可变
@ValueObject
public class Email {

    private final String value;  // final，不可变

    public Email(String value) {
        if (!isValid(value)) {
            throw new IllegalArgumentException("无效的邮箱地址");
        }
        this.value = value;
    }

    private boolean isValid(String value) {
        return value != null && value.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }

    // 相等性：通过所有属性判断
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Email email = (Email) obj;
        return value.equals(email.value);
    }

    @Override
    public int hashCode() {
        return value.hashCode();
    }
}

// 另一个值对象示例：Money
@ValueObject
public class Money {

    private final BigDecimal amount;
    private final String currency;

    public Money(BigDecimal amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("货币类型不同");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public Money multiply(double multiplier) {
        return new Money(
            this.amount.multiply(BigDecimal.valueOf(multiplier)),
            this.currency
        );
    }

    public static Money ZERO = new Money(BigDecimal.ZERO, "CNY");
}
```

### 4.3 仓储（Repository）模式

```java
// 1. 定义仓储接口（位于领域层）
public interface OrderRepository {

    /**
     * 保存订单
     */
    void save(Order order);

    /**
     * 根据 ID 查找订单
     */
    Optional<Order> findById(OrderId orderId);

    /**
     * 查找客户的订单列表
     */
    List<Order> findByCustomerId(CustomerId customerId);

    /**
     * 删除订单
     */
    void delete(OrderId orderId);
}

// 2. 实现仓储（位于基础设施层）
@Repository
public class JpaOrderRepository implements OrderRepository {

    @Autowired
    private OrderJpaRepository jpaRepository;

    @Autowired
    private OrderMapper mapper;

    @Override
    public void save(Order order) {
        OrderEntity entity = mapper.toEntity(order);
        jpaRepository.save(entity);

        // 发布领域事件
        for (DomainEvent event : order.getDomainEvents()) {
            eventPublisher.publish(event);
        }
        order.clearDomainEvents();
    }

    @Override
    public Optional<Order> findById(OrderId orderId) {
        OrderEntity entity = jpaRepository.findById(orderId.getValue());
        return entity != null
            ? Optional.of(mapper.toDomain(entity))
            : Optional.empty();
    }

    @Override
    public List<Order> findByCustomerId(CustomerId customerId) {
        List<OrderEntity> entities = jpaRepository.findByCustomerId(customerId.getValue());
        return entities.stream()
            .map(mapper::toDomain)
            .collect(Collectors.toList());
    }

    @Override
    public void delete(OrderId orderId) {
        jpaRepository.deleteById(orderId.getValue());
    }
}
```

### 4.4 领域事件（Domain Event）

```java
// 1. 定义领域事件
@Data
public class OrderPlacedEvent implements DomainEvent {

    private final OrderId orderId;
    private final CustomerId customerId;
    private final Money totalAmount;
    private final LocalDateTime occurredOn;

    public OrderPlacedEvent(OrderId orderId, CustomerId customerId, Money totalAmount) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.totalAmount = totalAmount;
        this.occurredOn = LocalDateTime.now();
    }
}

// 2. 在聚合根中发布事件
@Entity
public class Order extends AggregateRoot {

    private List<DomainEvent> domainEvents = new ArrayList<>();

    public void place() {
        // 业务逻辑
        this.status = OrderStatus.PLACED;

        // 发布领域事件
        registerEvent(new OrderPlacedEvent(
            this.orderId,
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

// 3. 事件处理器（位于应用层）
@Component
public class OrderPlacedEventHandler {

    @Autowired
    private NotificationService notificationService;

    @Autowired
    private CustomerServiceClient customerServiceClient;

    @EventListener
    public void handle(OrderPlacedEvent event) {
        // 发送订单确认邮件
        notificationService.sendOrderConfirmation(
            event.getCustomerId(),
            event.getOrderId()
        );

        // 更新客户统计信息
        customerServiceClient.incrementOrderCount(event.getCustomerId());
    }
}
```

### 4.5 领域服务（Domain Service）

```java
// 当业务逻辑不适合放在实体或值对象中时，使用领域服务
@DomainService
public class PricingDomainService {

    @Autowired
    private ProductRepository productRepository;

    @Autowired
    private DiscountPolicy discountPolicy;

    /**
     * 计算订单价格（涉及多个实体，不适合放在 Order 中）
     */
    public Money calculateOrderPrice(Order order, Customer customer) {
        // 基础价格
        Money basePrice = order.getBasePrice();

        // 应用客户折扣
        Money discount = discountPolicy.calculateDiscount(customer, basePrice);

        // 返回最终价格
        return basePrice.subtract(discount);
    }
}
```

### 4.6 规约（Specification）模式

```java
// 1. 定义规约接口
public interface Specification<T> {

    boolean isSatisfiedBy(T candidate);

    and Specification<T> and(Specification<T> other);
    or Specification<T> or(Specification<T> other);
    not Specification<T> not();
}

// 2. 抽象基类
public abstract class AbstractSpecification<T> implements Specification<T> {

    @Override
    public and Specification<T> and(Specification<T> other) {
        return new AndSpecification<>(this, other);
    }

    @Override
    public or Specification<T> or(Specification<T> other) {
        return new OrSpecification<>(this, other);
    }

    @Override
    public not Specification<T> not() {
        return new NotSpecification<>(this);
    }
}

// 3. 具体规约
public class CustomerCanPlaceOrderSpecification extends AbstractSpecification<Customer> {

    private final OrderRepository orderRepository;

    @Override
    public boolean isSatisfiedBy(Customer customer) {
        // 检查用户是否激活
        if (!customer.isActive()) {
            return false;
        }

        // 检查用户是否有过多未支付订单
        List<Order> unpaidOrders = orderRepository.findUnpaidByCustomer(customer.getId());
        if (unpaidOrders.size() >= 3) {
            return false;
        }

        return true;
    }
}

// 4. 使用规约
@Service
public class OrderApplicationService {

    @Autowired
    private CustomerCanPlaceOrderSpecification canPlaceOrderSpec;

    public void placeOrder(PlaceOrderCommand command) {
        Customer customer = customerRepository.findById(command.getCustomerId());

        // 使用规约进行业务规则验证
        if (!canPlaceOrderSpec.isSatisfiedBy(customer)) {
            throw new OrderException("当前用户不能下单");
        }

        // 继续下单流程
    }
}
```

### 4.7 工厂（Factory）模式

```java
// 当创建复杂对象或聚合时，使用工厂
@Factory
public class OrderFactory {

    private final ProductRepository productRepository;

    /**
     * 创建订单（涉及复杂的创建逻辑）
     */
    public Order createOrder(Customer customer, List<CreateOrderItemRequest> items) {
        // 验证
        if (items == null || items.isEmpty()) {
            throw new IllegalArgumentException("订单明细不能为空");
        }

        // 创建订单
        Order order = new Order(
            OrderId.generate(),
            customer.getId(),
            OrderStatus.PENDING
        );

        // 添加明细
        for (CreateOrderItemRequest item : items) {
            Product product = productRepository.findById(item.getProductId());

            // 验证库存
            if (!product.hasStock(item.getQuantity())) {
                throw new InsufficientStockException(product.getId());
            }

            order.addItem(product, item.getQuantity());
        }

        return order;
    }
}
```

---

## 总结

DDD 经典分层架构的核心价值：

1. **关注点分离**：四层架构各司其职，降低耦合
2. **领域为核心**：领域层独立，不依赖任何外部技术
3. **依赖倒置**：通过接口隔离领域层和基础设施层
4. **业务语言统一**：代码结构直接反映业务概念
5. **可测试性**：各层可独立测试，领域层完全可单元测试
6. **可扩展性**：无论是单体应用还是微服务，架构模式一致

DDD 战略模式（限界上下文、上下文映射）与战术模式（聚合、实体、值对象、仓储）的结合，帮助团队构建易于理解、易于维护、易于演化的企业级应用。

**权威参考**：
- 《领域驱动设计》- Eric Evans
- 《实现领域驱动设计》- Vaughn Vernon
- 《领域驱动设计精粹》- Vaughn Vernon
