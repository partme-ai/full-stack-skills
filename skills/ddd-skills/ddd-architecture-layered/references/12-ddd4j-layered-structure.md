# 标准 DDD 架构详细目录结构

## 📁 DDD 经典分层架构目录结构

```
project-root/
├── 📁 src/
│   ├── 📁 domain/                           # 领域层（核心）
│   │   ├── 📁 model/                        # 领域模型
│   │   │   ├── 📁 aggregate/                # 聚合
│   │   │   │   ├── 📁 order/                # 订单聚合
│   │   │   │   │   ├── Order.java           # 聚合根
│   │   │   │   │   │   ├── OrderId
│   │   │   │   │   │   ├── CustomerId
│   │   │   │   │   │   ├── OrderItems
│   │   │   │   │   │   ├── OrderStatus
│   │   │   │   │   │   ├── place()
│   │   │   │   │   │   ├── pay()
│   │   │   │   │   │   ├── cancel()
│   │   │   │   │   │   └── calculateTotal()
│   │   │   │   │   │
│   │   │   │   │   ├── OrderItem.java       # 实体（属于订单聚合）
│   │   │   │   │   └── OrderStatus.java     # 值对象
│   │   │   │   │
│   │   │   │   ├── 📁 customer/             # 客户聚合
│   │   │   │   │   ├── Customer.java        # 聚合根
│   │   │   │   │   ├── CustomerId.java
│   │   │   │   │   └── CustomerName.java
│   │   │   │   │
│   │   │   │   └── 📁 product/              # 产品聚合
│   │   │   │       └── Product.java
│   │   │   │
│   │   │   ├── 📁 entity/                   # 独立实体
│   │   │   │   ├── Payment.java
│   │   │   │   └── Invoice.java
│   │   │   │
│   │   │   ├── 📁 valueobject/              # 值对象
│   │   │   │   ├── Money.java
│   │   │   │   ├── Email.java
│   │   │   │   ├── Address.java
│   │   │   │   ├── PhoneNumber.java
│   │   │   │   └── Quantity.java
│   │   │   │
│   │   │   ├── 📁 service/                  # 领域服务
│   │   │   │   ├── OrderService.java
│   │   │   │   │   ├── placeOrder(Customer, List<Product>): Order
│   │   │   │   │   └── calculateDiscount(Order): Money
│   │   │   │   │
│   │   │   │   ├── CustomerService.java
│   │   │   │   └── PricingService.java
│   │   │   │
│   │   │   ├── 📁 event/                    # 领域事件
│   │   │   │   ├── DomainEvent.java         # 基础接口
│   │   │   │   ├── OrderPlacedEvent.java
│   │   │   │   ├── OrderPaidEvent.java
│   │   │   │   ├── CustomerRegisteredEvent.java
│   │   │   │   └── 📁 publisher/            # 事件发布者
│   │   │   │       └── DomainEventPublisher.java
│   │   │   │
│   │   │   ├── 📁 specification/            # 规约模式
│   │   │   │   ├── Specification.java       # 规约接口
│   │   │   │   ├── CustomerSpecification.java
│   │   │   │   └── OrderSpecification.java
│   │   │   │
│   │   │   ├── 📁 policy/                   # 业务策略
│   │   │   │   ├── DiscountPolicy.java
│   │   │   │   ├── ShippingPolicy.java
│   │   │   │   └── TaxPolicy.java
│   │   │   │
│   │   │   ├── 📁 factory/                  # 工厂模式
│   │   │   │   ├── OrderFactory.java
│   │   │   │   ├── CustomerFactory.java
│   │   │   │   └── ProductFactory.java
│   │   │   │
│   │   │   ├── 📁 repository/               # 仓储接口
│   │   │   │   ├── OrderRepository.java
│   │   │   │   ├── CustomerRepository.java
│   │   │   │   └── ProductRepository.java
│   │   │   │
│   │   │   └── 📁 exception/                # 领域异常
│   │   │       ├── DomainException.java
│   │   │       ├── BusinessRuleException.java
│   │   │       ├── InvalidEntityStateException.java
│   │   │       └── AggregateNotFoundException.java
│   │   │
│   │   ├── 📁 boundedcontext/               # 限界上下文（可选，大型系统）
│   │   │   ├── 📁 ordercontext/            # 订单上下文
│   │   │   │   ├── model/
│   │   │   │   └── service/
│   │   │   │
│   │   │   ├── 📁 customermanagement/      # 客户管理上下文
│   │   │   │   └── model/
│   │   │   │
│   │   │   └── 📁 inventorycontext/        # 库存上下文
│   │   │       └── model/
│   │   │
│   │   └── 📁 sharedkernel/                # 共享内核（可选）
│   │       ├── Money.java
│   │       ├── Address.java
│   │       └── Email.java
│   │
│   ├── 📁 application/                      # 应用层
│   │   ├── 📁 service/                      # 应用服务
│   │   │   ├── OrderApplicationService.java
│   │   │   │   ├── placeOrder(PlaceOrderCommand): OrderId
│   │   │   │   ├── payOrder(PayOrderCommand): void
│   │   │   │   └── cancelOrder(CancelOrderCommand): void
│   │   │   │
│   │   │   ├── CustomerApplicationService.java
│   │   │   └── ProductApplicationService.java
│   │   │
│   │   ├── 📁 command/                      # 命令对象（CQRS模式）
│   │   │   ├── PlaceOrderCommand.java
│   │   │   ├── PayOrderCommand.java
│   │   │   ├── CancelOrderCommand.java
│   │   │   └── RegisterCustomerCommand.java
│   │   │
│   │   ├── 📁 query/                        # 查询对象（CQRS模式）
│   │   │   ├── GetOrderQuery.java
│   │   │   ├── GetCustomerQuery.java
│   │   │   └── SearchProductsQuery.java
│   │   │
│   │   ├── 📁 handler/                      # 命令/查询处理器
│   │   │   ├── 📁 commandhandler/
│   │   │   │   ├── PlaceOrderCommandHandler.java
│   │   │   │   ├── PayOrderCommandHandler.java
│   │   │   │   └── RegisterCustomerCommandHandler.java
│   │   │   │
│   │   │   └── 📁 queryhandler/
│   │   │       ├── GetOrderQueryHandler.java
│   │   │       └── GetCustomerQueryHandler.java
│   │   │
│   │   ├── 📁 dto/                          # 数据传输对象
│   │   │   ├── OrderDTO.java
│   │   │   ├── CustomerDTO.java
│   │   │   ├── ProductDTO.java
│   │   │   └── OrderItemDTO.java
│   │   │
│   │   ├── 📁 eventhandler/                 # 应用事件处理器
│   │   │   ├── OrderPlacedEventHandler.java
│   │   │   ├── OrderPaidEventHandler.java
│   │   │   └── CustomerRegisteredEventHandler.java
│   │   │
│   │   ├── 📁 coordinator/                  # 协调器/工作流
│   │   │   ├── OrderProcessingCoordinator.java
│   │   │   └── CustomerOnboardingCoordinator.java
│   │   │
│   │   ├── 📁 validator/                    # 应用层验证器
│   │   │   ├── OrderValidator.java
│   │   │   └── CustomerValidator.java
│   │   │
│   │   └── 📁 exception/                    # 应用层异常
│   │       ├── ApplicationException.java
│   │       └── CommandValidationException.java
│   │
│   ├── 📁 infrastructure/                   # 基础设施层
│   │   ├── 📁 persistence/                  # 持久化
│   │   │   ├── 📁 repository/               # 仓储实现
│   │   │   │   ├── 📁 jpa/                  # JPA实现
│   │   │   │   │   ├── JpaOrderRepository.java
│   │   │   │   │   ├── JpaCustomerRepository.java
│   │   │   │   │   └── JpaProductRepository.java
│   │   │   │   │
│   │   │   │   ├── 📁 mybatis/              # MyBatis实现
│   │   │   │   │   ├── MyBatisOrderRepository.java
│   │   │   │   │   └── MyBatisCustomerRepository.java
│   │   │   │   │
│   │   │   │   └── 📁 memory/               # 内存实现（测试用）
│   │   │   │       └── InMemoryOrderRepository.java
│   │   │   │
│   │   │   ├── 📁 entity/                   # 持久化实体
│   │   │   │   ├── OrderEntity.java
│   │   │   │   ├── CustomerEntity.java
│   │   │   │   ├── ProductEntity.java
│   │   │   │   └── OrderItemEntity.java
│   │   │   │
│   │   │   ├── 📁 mapper/                   # 领域对象-持久化对象映射
│   │   │   │   ├── OrderMapper.java
│   │   │   │   ├── CustomerMapper.java
│   │   │   │   └── ProductMapper.java
│   │   │   │
│   │   │   ├── 📁 dao/                      # 数据访问对象
│   │   │   │   ├── OrderDao.java
│   │   │   │   └── CustomerDao.java
│   │   │   │
│   │   │   ├── 📁 specificationimpl/        # 规约实现
│   │   │   │   └── JpaSpecificationExecutorImpl.java
│   │   │   │
│   │   │   └── 📁 converter/                # 类型转换器
│   │   │       ├── MoneyConverter.java
│   │   │       ├── EmailConverter.java
│   │   │       └── AddressConverter.java
│   │   │
│   │   ├── 📁 messaging/                    # 消息传递
│   │   │   ├── 📁 eventpublisher/          # 事件发布者实现
│   │   │   │   ├── KafkaEventPublisher.java
│   │   │   │   ├── RabbitMQEventPublisher.java
│   │   │   │   └── DomainEventPublisherImpl.java
│   │   │   │
│   │   │   ├── 📁 eventconsumer/           # 事件消费者
│   │   │   │   ├── OrderEventConsumer.java
│   │   │   │   └── CustomerEventConsumer.java
│   │   │   │
│   │   │   └── 📁 queue/                   # 消息队列
│   │   │       ├── MessageQueue.java
│   │   │       └── QueueMessage.java
│   │   │
│   │   ├── 📁 external/                     # 外部服务集成
│   │   │   ├── 📁 payment/                  # 支付服务
│   │   │   │   ├── PaymentService.java
│   │   │   │   ├── AlipayPaymentService.java
│   │   │   │   ├── WechatPaymentService.java
│   │   │   │   └── StripePaymentService.java
│   │   │   │
│   │   │   ├── 📁 notification/             # 通知服务
│   │   │   │   ├── EmailService.java
│   │   │   │   ├── SMSService.java
│   │   │   │   └── PushNotificationService.java
│   │   │   │
│   │   │   ├── 📁 shipping/                 # 物流服务
│   │   │   │   └── ShippingService.java
│   │   │   │
│   │   │   └── 📁 identity/                 # 身份验证服务
│   │   │       └── IdentityService.java
│   │   │
│   │   ├── 📁 cache/                        # 缓存
│   │   │   ├ 📁 redis/
│   │   │   │   ├── RedisCache.java
│   │   │   │   └── RedisOrderCache.java
│   │   │   │
│   │   │   ├── 📁 local/
│   │   │   │   └── GuavaCache.java
│   │   │   │
│   │   │   └── CacheProvider.java
│   │   │
│   │   ├── 📁 config/                       # 配置
│   │   │   ├── PersistenceConfig.java
│   │   │   ├── MessagingConfig.java
│   │   │   ├── ExternalServiceConfig.java
│   │   │   ├── CacheConfig.java
│   │   │   └── SecurityConfig.java
│   │   │
│   │   ├── 📁 security/                     # 安全
│   │   │   ├── JwtTokenProvider.java
│   │   │   ├── PasswordEncoder.java
│   │   │   └── SecurityContext.java
│   │   │
│   │   └── 📁 util/                         # 基础设施工具
│   │       ├── IdGenerator.java
│   │       ├── DateUtils.java
│   │       ├── JsonUtils.java
│   │       └── ValidationUtils.java
│   │
│   ├── 📁 interfaces/                       # 接口层（表示层/适配器层）
│   │   ├── 📁 web/                          # Web接口
│   │   │   ├── 📁 controller/               # REST控制器
│   │   │   │   ├── OrderController.java
│   │   │   │   │   ├── @RestController
│   │   │   │   │   ├── @RequestMapping("/api/orders")
│   │   │   │   │   ├── placeOrder(@RequestBody)
│   │   │   │   │   ├── getOrder(@PathVariable)
│   │   │   │   │   └── cancelOrder(@PathVariable)
│   │   │   │   │
│   │   │   │   ├── CustomerController.java
│   │   │   │   └── ProductController.java
│   │   │   │
│   │   │   ├── 📁 dto/                      # Web DTO
│   │   │   │   ├── 📁 request/
│   │   │   │   │   ├── PlaceOrderRequest.java
│   │   │   │   │   ├── PayOrderRequest.java
│   │   │   │   │   └── RegisterCustomerRequest.java
│   │   │   │   │
│   │   │   │   ├── 📁 response/
│   │   │   │   │   ├── OrderResponse.java
│   │   │   │   │   ├── CustomerResponse.java
│   │   │   │   │   └── ApiResponse.java
│   │   │   │   │
│   │   │   │   └── 📁 assembler/            # DTO装配器
│   │   │   │       ├── OrderAssembler.java
│   │   │   │       └── CustomerAssembler.java
│   │   │   │
│   │   │   ├── 📁 filter/                   # 过滤器
│   │   │   │   ├── AuthenticationFilter.java
│   │   │   │   ├── LoggingFilter.java
│   │   │   │   └── CorsFilter.java
│   │   │   │
│   │   │   ├── 📁 interceptor/              # 拦截器
│   │   │   │   ├── PerformanceInterceptor.java
│   │   │   │   └── ValidationInterceptor.java
│   │   │   │
│   │   │   ├── 📁 advice/                   # 异常处理
│   │   │   │   ├── GlobalExceptionHandler.java
│   │   │   │   ├── ErrorResponse.java
│   │   │   │   └── ErrorCode.java
│   │   │   │
│   │   │   └── 📁 validation/               # Web验证
│   │   │       └── RequestValidator.java
│   │   │
│   │   ├── 📁 rpc/                          # RPC接口
│   │   │   ├── 📁 provider/
│   │   │   │   └── OrderRpcProvider.java
│   │   │   │
│   │   │   └── 📁 consumer/
│   │   │       └── PaymentRpcConsumer.java
│   │   │
│   │   ├── 📁 cli/                          # 命令行接口
│   │   │   └── CommandLineInterface.java
│   │   │
│   │   ├── 📁 graphql/                      # GraphQL接口
│   │   │   ├── OrderGraphQLController.java
│   │   │   └── CustomerGraphQLController.java
│   │   │
│   │   └── 📁 batch/                        # 批处理接口
│   │       └── BatchJobController.java
│   │
│   ├── 📁 shared/                           # 共享组件
│   │   ├── 📁 kernel/                       # 共享内核
│   │   │   ├── BaseEntity.java
│   │   │   ├── AggregateRoot.java
│   │   │   ├── ValueObject.java
│   │   │   ├── Entity.java
│   │   │   └── Identifier.java
│   │   │
│   │   ├── 📁 util/                         # 共享工具
│   │   │   ├── Assert.java
│   │   │   ├── ValidationUtils.java
│   │   │   ├── ObjectMapperUtils.java
│   │   │   └── StringUtils.java
│   │   │
│   │   ├── 📁 constant/                     # 常量
│   │   │   ├── AppConstants.java
│   │   │   ├── ErrorConstants.java
│   │   │   └── ValidationConstants.java
│   │   │
│   │   ├── 📁 exception/                    # 共享异常
│   │   │   ├── SystemException.java
│   │   │   ├── ValidationException.java
│   │   │   └── ErrorCode.java
│   │   │
│   │   └── 📁 annotation/                   # 共享注解
│   │       ├── DomainService.java
│   │       ├── ApplicationService.java
│   │       └── ValueObject.java
│   │
│   └── Application.java                     # 应用启动类
│       ├── @SpringBootApplication
│       └── main()
│
├── 📁 test/                                 # 测试目录
│   ├── 📁 unit/                             # 单元测试
│   │   ├── 📁 domain/                       # 领域层测试
│   │   │   ├── 📁 aggregate/
│   │   │   │   ├── OrderTest.java
│   │   │   │   └── CustomerTest.java
│   │   │   │
│   │   │   ├── 📁 valueobject/
│   │   │   │   ├── MoneyTest.java
│   │   │   │   └── EmailTest.java
│   │   │   │
│   │   │   ├── 📁 service/
│   │   │   │   └── OrderServiceTest.java
│   │   │   │
│   │   │   └── 📁 event/
│   │   │       └── DomainEventTest.java
│   │   │
│   │   ├── 📁 application/                  # 应用层测试
│   │   │   ├── 📁 service/
│   │   │   │   └── OrderApplicationServiceTest.java
│   │   │   │
│   │   │   ├── 📁 handler/
│   │   │   │   └── PlaceOrderCommandHandlerTest.java
│   │   │   │
│   │   │   └── 📁 dto/
│   │   │       └── OrderDTOTest.java
│   │   │
│   │   └── 📁 interfaces/                   # 接口层测试
│   │       └── OrderControllerTest.java
│   │
│   ├── 📁 integration/                      # 集成测试
│   │   ├── OrderIntegrationTest.java
│   │   ├── CustomerIntegrationTest.java
│   │   └── PaymentIntegrationTest.java
│   │
│   ├── 📁 acceptance/                       # 验收测试
│   │   ├── OrderAcceptanceTest.java
│   │   └── CustomerAcceptanceTest.java
│   │
│   ├── 📁 e2e/                              # 端到端测试
│   │   ├── OrderE2ETest.java
│   │   └── CustomerE2ETest.java
│   │
│   └── 📁 fixtures/                         # 测试夹具
│       ├── OrderFixture.java
│       ├── CustomerFixture.java
│       └── TestDataFactory.java
│
├── 📁 resources/                            # 资源文件
│   ├── application.yml                      # 主配置文件
│   ├── application-dev.yml                  # 开发环境
│   ├── application-test.yml                 # 测试环境
│   ├── application-prod.yml                 # 生产环境
│   │
│   ├── 📁 db/                               # 数据库脚本
│   │   ├── migration/                       # 迁移脚本
│   │   │   ├── V1__init_schema.sql
│   │   │   ├── V2__create_tables.sql
│   │   │   └── V3__add_constraints.sql
│   │   │
│   │   └── seed/                            # 种子数据
│   │       └── initial_data.sql
│   │
│   ├── 📁 mapper/                           # MyBatis Mapper XML
│   │   ├── OrderMapper.xml
│   │   ├── CustomerMapper.xml
│   │   └── ProductMapper.xml
│   │
│   ├── 📁 i18n/                             # 国际化
│   │   ├── messages.properties
│   │   ├── messages_en.properties
│   │   └── messages_zh.properties
│   │
│   ├── 📁 templates/                        # 模板文件
│   │   ├── email/
│   │   │   ├── order-confirmation.html
│   │   │   └── welcome.html
│   │   │
│   │   └── report/
│   │       └── invoice.html
│   │
│   ├── logback-spring.xml                  # 日志配置
│   └── banner.txt                          # 启动Banner
│
├── 📁 docker/                               # Docker配置
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── 📁 scripts/
│       └── startup.sh
│
├── 📁 docs/                                 # 文档
│   ├── 📁 architecture/                     # 架构文档
│   │   ├── ddd-architecture.md             # DDD架构说明
│   │   ├── bounded-contexts.md             # 限界上下文
│   │   ├── aggregate-design.md             # 聚合设计
│   │   ├── 📁 decisions/                   # 架构决策记录
│   │   │   ├── ADR-001-ddd-adoption.md
│   │   │   ├── ADR-002-cqrs-implementation.md
│   │   │   └── ADR-003-event-sourcing.md
│   │   │
│   │   └── 📁 diagrams/                     # 架构图
│   │       ├── domain-model.png
│   │       ├── bounded-contexts.png
│   │       └── aggregate-structure.png
│   │
│   ├── 📁 domain/                           # 领域文档
│   │   ├── domain-model.md                  # 领域模型
│   │   ├── ubiquitous-language.md           # 通用语言
│   │   ├── glossary.md                      # 术语表
│   │   └── business-rules.md                # 业务规则
│   │
│   ├── 📁 api/                              # API文档
│   │   ├── openapi.yaml
│   │   └── 📁 postman/
│   │       └── collection.json
│   │
│   └── README.md
│
├── .gitignore
├── README.md
├── pom.xml / build.gradle
└── LICENSE
```

## 🏗 **DDD 经典四层架构**

### **依赖方向：**
```
接口层（Interfaces） → 应用层（Application） → 领域层（Domain） ← 基础设施层（Infrastructure）
```

### **各层职责详解：**

#### **1. 领域层（Domain Layer）**
- **核心业务逻辑**
- 包含：实体、值对象、聚合、领域服务、领域事件
- **无任何外部依赖**，纯业务逻辑

#### **2. 应用层（Application Layer）**
- **用例协调**
- 业务流程编排
- 事务管理
- 安全性检查

#### **3. 接口层（Interfaces Layer）**
- **用户界面**
- API端点
- 数据转换（DTO转换）
- 输入验证

#### **4. 基础设施层（Infrastructure Layer）**
- **技术实现**
- 持久化、消息、缓存等
- 外部服务集成

## 📦 **按限界上下文组织（大型项目）**

```
project-root/
├── 📁 contexts/                            # 限界上下文
│   ├── 📁 order-management/                # 订单管理上下文
│   │   ├── 📁 domain/
│   │   ├── 📁 application/
│   │   ├── 📁 interfaces/
│   │   └── 📁 infrastructure/
│   │
│   ├── 📁 customer-management/             # 客户管理上下文
│   │   ├── 📁 domain/
│   │   ├── 📁 application/
│   │   └── ...
│   │
│   └── 📁 product-catalog/                 # 产品目录上下文
│       └── ...
│
├── 📁 shared/                              # 共享内核
│   ├── 📁 kernel/
│   └── 📁 common/
│
└── 📁 api-gateway/                         # API网关
```

## 🔄 **CQRS + 事件溯源变体**

```
project-root/
├── 📁 write-side/                          # 写端
│   ├── 📁 domain/
│   ├── 📁 application/
│   ├── 📁 infrastructure/
│   └── 📁 interfaces/
│
├── 📁 read-side/                           # 读端
│   ├── 📁 query/
│   │   ├── 📁 model/                       # 查询模型
│   │   │   ├── OrderView.java
│   │   │   └── CustomerView.java
│   │   │
│   │   ├── 📁 handler/                     # 查询处理器
│   │   └── 📁 repository/                  # 查询仓储
│   │
│   └── 📁 projection/                      # 投影
│       ├── OrderProjection.java
│       └── CustomerProjection.java
│
├── 📁 events/                              # 事件存储
│   ├── EventStore.java
│   └── EventStream.java
│
└── 📁 event-handlers/                      # 事件处理器
    ├── OrderEventHandler.java
    └── CustomerEventHandler.java
```

## 🎯 **DDD核心模式在目录中的体现**

### **1. 聚合模式**
```java
// 聚合根示例
public class Order extends AggregateRoot {
    private OrderId id;
    private CustomerId customerId;
    private List<OrderItem> items;
    private OrderStatus status;
    
    // 业务方法
    public void place() {
        // 业务规则验证
        this.status = OrderStatus.PLACED;
        registerEvent(new OrderPlacedEvent(this.id));
    }
}
```

### **2. 仓储模式**
```java
// 仓储接口（领域层）
public interface OrderRepository {
    Order findById(OrderId id);
    void save(Order order);
    void delete(OrderId id);
}

// 仓储实现（基础设施层）
@Repository
public class JpaOrderRepository implements OrderRepository {
    private final OrderJpaRepository jpaRepository;
    private final OrderMapper mapper;
    
    @Override
    public Order findById(OrderId id) {
        OrderEntity entity = jpaRepository.findById(id.getValue());
        return mapper.toDomain(entity);
    }
}
```

### **3. 领域事件模式**
```java
// 领域事件
public class OrderPlacedEvent extends DomainEvent {
    private final OrderId orderId;
    private final CustomerId customerId;
    private final Money totalAmount;
    
    // 事件处理方法
}
```

## 📚 **权威依据**

### **DDD经典书籍参考：**
1. **《领域驱动设计：软件核心复杂性应对之道》** - Eric Evans
    - 核心概念：实体、值对象、聚合、仓储、工厂

2. **《实现领域驱动设计》** - Vaughn Vernon
    - 详细分层架构实现
    - 聚合设计原则

3. **《领域驱动设计精粹》** - Vaughn Vernon
    - 战略设计和战术设计
    - 限界上下文映射

### **官方模式定义：**
- **四层架构**：Eric Evans 原始定义
- **六边形架构**：Alistair Cockburn（与DDD结合）
- **整洁架构**：Robert C. Martin（DDD实现方式）

## 🛠 **项目模板和生成器**

### **Spring Boot DDD Starter**
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
</dependency>
<dependency>
    <groupId>org.fuin.ddd4j</groupId>
    <artifactId>ddd-4-java-core</artifactId>
    <version>0.7.0</version>
</dependency>
```

### **DDD项目生成器**
```bash
# 使用Maven Archetype
mvn archetype:generate \
  -DarchetypeGroupId=com.ddd \
  -DarchetypeArtifactId=ddd-archetype \
  -DarchetypeVersion=1.0.0
```

这个目录结构基于Eric Evans和Vaughn Vernon的DDD经典理论，结合了现代Java开发实践，是经过验证的企业级DDD项目标准结构。