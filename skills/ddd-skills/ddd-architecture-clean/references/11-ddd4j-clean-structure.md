# 整洁架构详细目录结构参考

## 📁 项目根目录结构

```
project-root/
├── 📁 src/                              # 源代码目录
│   ├── 📁 domain/                       # 领域层（最内层）
│   │   ├── 📁 entities/                 # 业务实体（核心业务对象）
│   │   │   ├── User.java               # 用户实体
│   │   │   │   ├── id: UserId          # 值对象作为ID
│   │   │   │   ├── name: UserName      # 值对象
│   │   │   │   ├── email: Email        # 值对象
│   │   │   │   └── validate(): void    # 业务规则
│   │   │   │
│   │   │   ├── Order.java              # 订单实体
│   │   │   │   ├── orderId: OrderId
│   │   │   │   ├── items: List<OrderItem>
│   │   │   │   ├── status: OrderStatus
│   │   │   │   ├── calculateTotal(): Money
│   │   │   │   └── place(): void
│   │   │   │
│   │   │   ├── Product.java
│   │   │   └── 📁 aggregates/           # 聚合根（可选）
│   │   │       └── OrderAggregate.java
│   │   │
│   │   ├── 📁 valueobjects/             # 值对象
│   │   │   ├── 📁 common/              # 通用值对象
│   │   │   │   ├── Money.java
│   │   │   │   │   ├── amount: BigDecimal
│   │   │   │   │   ├── currency: Currency
│   │   │   │   │   ├── add(Money): Money
│   │   │   │   │   └── equals(): boolean
│   │   │   │   │
│   │   │   │   ├── Email.java
│   │   │   │   ├── PhoneNumber.java
│   │   │   │   └── Address.java
│   │   │   │
│   │   │   ├── 📁 user/                # 用户相关值对象
│   │   │   │   ├── UserId.java
│   │   │   │   ├── UserName.java
│   │   │   │   └── Password.java
│   │   │   │
│   │   │   └── 📁 order/               # 订单相关值对象
│   │   │       ├── OrderId.java
│   │   │       ├── OrderItem.java
│   │   │       └── OrderStatus.java
│   │   │
│   │   ├── 📁 services/                 # 领域服务
│   │   │   ├── UserRegistrationService.java
│   │   │   │   └── register(UserRegistrationCommand): User
│   │   │   │
│   │   │   ├── OrderProcessingService.java
│   │   │   └── PricingService.java
│   │   │
│   │   ├── 📁 events/                   # 领域事件
│   │   │   ├── DomainEvent.java         # 基础接口
│   │   │   │   ├── occurredOn(): Instant
│   │   │   │   └── getAggregateId(): String
│   │   │   │
│   │   │   ├── UserEvents.java
│   │   │   │   ├── UserCreatedEvent.java
│   │   │   │   └── UserUpdatedEvent.java
│   │   │   │
│   │   │   ├── OrderEvents.java
│   │   │   │   ├── OrderPlacedEvent.java
│   │   │   │   ├── OrderPaidEvent.java
│   │   │   │   └── OrderCancelledEvent.java
│   │   │   │
│   │   │   └── 📁 handlers/            # 领域事件处理器
│   │   │       └── DomainEventHandler.java
│   │   │
│   │   ├── 📁 repositories/             # 仓储接口
│   │   │   ├── UserRepository.java
│   │   │   │   └── extends Repository<User, UserId>
│   │   │   │
│   │   │   ├── OrderRepository.java
│   │   │   └── Specification.java      # 规约模式
│   │   │
│   │   ├── 📁 policies/                 # 业务规则/策略
│   │   │   ├── DiscountPolicy.java
│   │   │   ├── ShippingPolicy.java
│   │   │   └── ValidationPolicy.java
│   │   │
│   │   └── 📁 exceptions/               # 领域异常
│   │       ├── DomainException.java     # 基础领域异常
│   │       ├── BusinessRuleException.java
│   │       ├── ValidationException.java
│   │       └── AggregateNotFoundException.java
│   │
│   ├── 📁 application/                  # 应用层（用例层）
│   │   ├── 📁 usecases/                 # 用例/交互器
│   │   │   ├── 📁 user/                 # 用户相关用例
│   │   │   │   ├── CreateUserUseCase.java
│   │   │   │   │   ├── execute(CreateUserCommand): CreateUserResult
│   │   │   │   │   └── validate(CreateUserCommand): void
│   │   │   │   │
│   │   │   │   ├── UpdateUserUseCase.java
│   │   │   │   ├── GetUserUseCase.java
│   │   │   │   ├── AuthenticateUserUseCase.java
│   │   │   │   └── 📁 commands/        # 命令对象
│   │   │   │       ├── CreateUserCommand.java
│   │   │   │       ├── UpdateUserCommand.java
│   │   │   │       └── AuthenticateCommand.java
│   │   │   │
│   │   │   ├── 📁 order/                # 订单相关用例
│   │   │   │   ├── CreateOrderUseCase.java
│   │   │   │   ├── ProcessOrderUseCase.java
│   │   │   │   ├── CancelOrderUseCase.java
│   │   │   │   └── 📁 commands/
│   │   │   │       └── CreateOrderCommand.java
│   │   │   │
│   │   │   ├── 📁 payment/              # 支付相关用例
│   │   │   │   └── ProcessPaymentUseCase.java
│   │   │   │
│   │   │   └── 📁 interfaces/           # 用例接口
│   │   │       ├── UseCase.java         # 标记接口
│   │   │       └── CommandHandler.java
│   │   │
│   │   ├── 📁 services/                 # 应用服务（协调用例）
│   │   │   ├── UserApplicationService.java
│   │   │   │   ├── createUser(): UserDTO
│   │   │   │   ├── updateUser(): UserDTO
│   │   │   │   └── getUser(): UserDTO
│   │   │   │
│   │   │   ├── OrderApplicationService.java
│   │   │   └── PaymentApplicationService.java
│   │   │
│   │   ├── 📁 ports/                    # 端口（接口）
│   │   │   ├── 📁 input/                # 输入端口（驱动端）
│   │   │   │   ├── UserInputPort.java
│   │   │   │   ├── OrderInputPort.java
│   │   │   │   └── PaymentInputPort.java
│   │   │   │
│   │   │   ├── 📁 output/               # 输出端口（被驱动端）
│   │   │   │   ├── UserOutputPort.java
│   │   │   │   ├── OrderOutputPort.java
│   │   │   │   ├── PaymentOutputPort.java
│   │   │   │   ├── NotificationOutputPort.java
│   │   │   │   └── EventPublisherPort.java
│   │   │   │
│   │   │   └── 📁 gateways/             # 网关接口
│   │   │       ├── IdGeneratorGateway.java
│   │   │       ├── DateTimeGateway.java
│   │   │       └── CryptoGateway.java
│   │   │
│   │   ├── 📁 dto/                      # 数据传输对象
│   │   │   ├── 📁 request/              # 请求DTO
│   │   │   │   ├── CreateUserRequest.java
│   │   │   │   ├── UpdateUserRequest.java
│   │   │   │   └── CreateOrderRequest.java
│   │   │   │
│   │   │   ├── 📁 response/             # 响应DTO
│   │   │   │   ├── UserResponse.java
│   │   │   │   ├── OrderResponse.java
│   │   │   │   └── ApiResponse.java     # 通用响应
│   │   │   │
│   │   │   └── 📁 internal/             # 内部DTO
│   │   │       ├── UserDTO.java
│   │   │       └── OrderDTO.java
│   │   │
│   │   ├── 📁 mappers/                  # 对象映射器
│   │   │   ├── UserMapper.java
│   │   │   ├── OrderMapper.java
│   │   │   └── ProductMapper.java
│   │   │
│   │   └── 📁 exceptions/               # 应用层异常
│   │       ├── ApplicationException.java
│   │       ├── UseCaseException.java
│   │       └── ValidationException.java
│   │
│   ├── 📁 infrastructure/               # 基础设施层（最外层）
│   │   ├── 📁 persistence/              # 持久化实现
│   │   │   ├── 📁 repositories/         # 仓储实现
│   │   │   │   ├── UserRepositoryImpl.java
│   │   │   │   │   └── implements UserRepository
│   │   │   │   │
│   │   │   │   ├── OrderRepositoryImpl.java
│   │   │   │   └── 📁 jpa/             # JPA具体实现
│   │   │   │       ├── JpaUserRepository.java
│   │   │   │       └── JpaOrderRepository.java
│   │   │   │
│   │   │   ├── 📁 entities/             # 持久化实体
│   │   │   │   ├── UserEntity.java
│   │   │   │   │   ├── @Entity
│   │   │   │   │   ├── @Table
│   │   │   │   │   └── toDomain(): User
│   │   │   │   │
│   │   │   │   ├── OrderEntity.java
│   │   │   │   └── 📁 converters/      # 类型转换器
│   │   │   │       ├── EmailConverter.java
│   │   │   │       └── MoneyConverter.java
│   │   │   │
│   │   │   ├── 📁 mappers/              # 持久化映射器
│   │   │   │   ├── UserPersistenceMapper.java
│   │   │   │   └── OrderPersistenceMapper.java
│   │   │   │
│   │   │   └── 📁 migrations/           # 数据库迁移
│   │   │       ├── V1__init.sql
│   │   │       └── V2__add_indexes.sql
│   │   │
│   │   ├── 📁 web/                      # Web层实现
│   │   │   ├── 📁 controllers/          # 控制器
│   │   │   │   ├── UserController.java
│   │   │   │   │   ├── @RestController
│   │   │   │   │   ├── @RequestMapping("/api/users")
│   │   │   │   │   ├── createUser(@RequestBody): ResponseEntity
│   │   │   │   │   └── getUser(@PathVariable): ResponseEntity
│   │   │   │   │
│   │   │   │   ├── OrderController.java
│   │   │   │   └── PaymentController.java
│   │   │   │
│   │   │   ├── 📁 filters/              # 过滤器
│   │   │   │   ├── LoggingFilter.java
│   │   │   │   └── AuthenticationFilter.java
│   │   │   │
│   │   │   ├── 📁 interceptors/         # 拦截器
│   │   │   │   └── PerformanceInterceptor.java
│   │   │   │
│   │   │   ├── 📁 advice/               # 异常处理
│   │   │   │   ├── GlobalExceptionHandler.java
│   │   │   │   └── ErrorResponse.java
│   │   │   │
│   │   │   └── 📁 validation/           # Web层验证
│   │   │       └── CustomValidators.java
│   │   │
│   │   ├── 📁 external/                 # 外部服务适配器
│   │   │   ├── 📁 payment/              # 支付服务
│   │   │   │   ├── StripePaymentAdapter.java
│   │   │   │   └── PayPalPaymentAdapter.java
│   │   │   │
│   │   │   ├── 📁 notification/         # 通知服务
│   │   │   │   ├── EmailNotificationAdapter.java
│   │   │   │   ├── SMSNotificationAdapter.java
│   │   │   │   └── PushNotificationAdapter.java
│   │   │   │
│   │   │   ├── 📁 messaging/            # 消息队列
│   │   │   │   ├── RabbitMQAdapter.java
│   │   │   │   ├── KafkaAdapter.java
│   │   │   │   └── EventPublisherAdapter.java
│   │   │   │
│   │   │   └── 📁 storage/              # 存储服务
│   │   │       ├── S3StorageAdapter.java
│   │   │       └── LocalStorageAdapter.java
│   │   │
│   │   ├── 📁 config/                   # 配置类
│   │   │   ├── 📁 persistence/          # 持久化配置
│   │   │   │   ├── JpaConfig.java
│   │   │   │   ├── DataSourceConfig.java
│   │   │   │   └── TransactionConfig.java
│   │   │   │
│   │   │   ├── 📁 web/                  # Web配置
│   │   │   │   ├── WebConfig.java
│   │   │   │   ├── SecurityConfig.java
│   │   │   │   └── SwaggerConfig.java
│   │   │   │
│   │   │   ├── 📁 external/             # 外部服务配置
│   │   │   │   ├── PaymentConfig.java
│   │   │   │   ├── NotificationConfig.java
│   │   │   │   └── MessagingConfig.java
│   │   │   │
│   │   │   ├── UseCaseConfig.java       # 用例配置
│   │   │   ├── BeanConfig.java          # Bean配置
│   │   │   └── ModuleConfig.java        # 模块配置
│   │   │
│   │   ├── 📁 security/                 # 安全实现
│   │   │   ├── JwtTokenProvider.java
│   │   │   ├── PasswordEncoderImpl.java
│   │   │   └── SecurityContextImpl.java
│   │   │
│   │   └── 📁 logging/                  # 日志实现
│   │       ├── LoggingAdapter.java
│   │       └── AuditLogger.java
│   │
│   ├── 📁 interfaces/                   # 接口适配器层（可选分离）
│   │   ├── 📁 adapters/                 # 适配器
│   │   │   ├── 📁 web/                  # Web适配器
│   │   │   │   ├── UserWebAdapter.java
│   │   │   │   └── OrderWebAdapter.java
│   │   │   │
│   │   │   ├── 📁 cli/                  # 命令行适配器
│   │   │   │   └── CommandLineAdapter.java
│   │   │   │
│   │   │   └── 📁 message/              # 消息适配器
│   │   │       ├── KafkaConsumerAdapter.java
│   │   │       └── RabbitMQConsumerAdapter.java
│   │   │
│   │   └── 📁 presenters/               # 展示器
│   │       ├📁 UserPresenter.java
│   │       └📁 OrderPresenter.java
│   │
│   └── MainApplication.java             # 应用启动类
│       ├── @SpringBootApplication
│       ├── main()
│       └── configure()
│
├── 📁 test/                             # 测试目录
│   ├── 📁 unit/                         # 单元测试
│   │   ├── 📁 domain/                   # 领域层测试
│   │   │   ├── 📁 entities/
│   │   │   │   ├── UserTest.java
│   │   │   │   └── OrderTest.java
│   │   │   │
│   │   │   ├── 📁 valueobjects/
│   │   │   │   ├── MoneyTest.java
│   │   │   │   └── EmailTest.java
│   │   │   │
│   │   │   ├── 📁 services/
│   │   │   │   └── UserRegistrationServiceTest.java
│   │   │   │
│   │   │   └── 📁 events/
│   │   │       └── DomainEventTest.java
│   │   │
│   │   ├── 📁 application/              # 应用层测试
│   │   │   ├── 📁 usecases/
│   │   │   │   ├── CreateUserUseCaseTest.java
│   │   │   │   └── CreateOrderUseCaseTest.java
│   │   │   │
│   │   │   ├── 📁 services/
│   │   │   │   └── UserApplicationServiceTest.java
│   │   │   │
│   │   │   └── 📁 ports/
│   │   │       └── MockUserOutputPort.java
│   │   │
│   │   └── 📁 infrastructure/           # 基础设施层测试
│   │       ├── 📁 persistence/
│   │       │   └── UserRepositoryImplTest.java
│   │       │
│   │       └── 📁 web/
│   │           └── UserControllerTest.java
│   │
│   ├── 📁 integration/                  # 集成测试
│   │   ├── UserIntegrationTest.java
│   │   ├── OrderIntegrationTest.java
│   │   └── PaymentIntegrationTest.java
│   │
│   ├── 📁 acceptance/                   # 验收测试
│   │   ├── UserAcceptanceTest.java
│   │   └── OrderAcceptanceTest.java
│   │
│   ├── 📁 e2e/                          # 端到端测试
│   │   ├── ApiE2ETest.java
│   │   └── UserJourneyTest.java
│   │
│   └── 📁 fixtures/                     # 测试夹具
│       ├── UserFixture.java
│       ├── OrderFixture.java
│       └── TestDataFactory.java
│
├── 📁 resources/                        # 资源文件
│   ├── application.yml                  # 主配置文件
│   ├── application-dev.yml              # 开发环境配置
│   ├── application-prod.yml             # 生产环境配置
│   ├── application-test.yml             # 测试环境配置
│   │
│   ├── 📁 db/                           # 数据库相关
│   │   ├── migration/                   # 迁移脚本
│   │   │   ├── V1__init_schema.sql
│   │   │   └── V2__add_data.sql
│   │   │
│   │   └── seed/                        # 种子数据
│   │       └── initial_data.sql
│   │
│   ├── 📁 i18n/                         # 国际化
│   │   ├── messages.properties
│   │   ├── messages_en.properties
│   │   └── messages_zh.properties
│   │
│   ├── 📁 templates/                    # 模板文件
│   │   ├── email/
│   │   │   ├── welcome.html
│   │   │   └── order-confirmation.html
│   │   │
│   │   └── reports/
│   │       └── invoice-template.html
│   │
│   ├── 📁 static/                       # 静态资源
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── logback-spring.xml              # 日志配置
│   └── banner.txt                       # Spring Boot Banner
│
├── 📁 docker/                           # Docker配置
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.dev.yml
│   └── 📁 scripts/
│       ├── wait-for-it.sh
│       └── init-db.sh
│
├── 📁 docs/                             # 文档
│   ├── 📁 architecture/                 # 架构文档
│   │   ├── clean-architecture.md       # 整洁架构说明
│   │   ├── layers.md                   # 各层职责说明
│   │   ├── 📁 decisions/               # 架构决策记录
│   │   │   ├── 001-use-clean-architecture.md
│   │   │   └── 002-value-objects-for-ids.md
│   │   │
│   │   └── 📁 diagrams/                 # 架构图
│   │       ├── clean-architecture.png
│   │       ├── dependency-flow.png
│   │       └── component-diagram.png
│   │
│   ├── 📁 api/                          # API文档
│   │   ├── openapi.yaml                # OpenAPI规范
│   │   ├── postman/
│   │   │   ├── collection.json
│   │   │   └── environment.json
│   │   │
│   │   └── 📁 examples/                 # API示例
│   │       ├── create-user.http
│   │       └── create-order.http
│   │
│   ├── 📁 domain/                       # 领域文档
│   │   ├── domain-model.md             # 领域模型说明
│   │   ├── glossary.md                 # 术语表
│   │   └── business-rules.md           # 业务规则
│   │
│   ├── 📁 deployment/                   # 部署文档
│   │   ├── deployment-guide.md
│   │   └── production-checklist.md
│   │
│   └── README.md                        # 项目总览
│
├── 📁 scripts/                          # 脚本文件
│   ├── build.sh                        # 构建脚本
│   ├── deploy.sh                       # 部署脚本
│   ├── test.sh                         # 测试脚本
│   ├── 📁 code-quality/                # 代码质量
│   │   ├── checkstyle.xml
│   │   ├── sonar-project.properties
│   │   └── pmd-ruleset.xml
│   │
│   └── 📁 database/                     # 数据库脚本
│       ├── backup.sh
│       └── restore.sh
│
├── .gitignore                          # Git忽略配置
├── README.md                           # 项目说明
├── pom.xml / build.gradle              # 构建配置
├── gradlew / gradlew.bat               # Gradle包装器
├── Makefile                            # Make命令
├── LICENSE                             # 许可证
├── CHANGELOG.md                        # 变更日志
└── CONTRIBUTING.md                     # 贡献指南
```

## 🏗 整洁架构层级关系

### 依赖规则（由内向外）
```
Entities ← Use Cases ← Interface Adapters ← Frameworks & Drivers
   ↑           ↑              ↑                     ↑
 领域层     应用层       接口适配器层        基础设施层
```

### 各层职责说明

#### 1. **领域层 (Domain Layer)**
- 核心业务逻辑和规则
- 独立于框架和技术
- 包含：实体、值对象、领域服务、领域事件

#### 2. **应用层 (Application Layer)**
- 用例和业务流程
- 协调领域对象完成特定任务
- 包含：用例、应用服务、DTO、端口接口

#### 3. **接口适配器层 (Interface Adapters)**
- 转换数据格式
- 适配外部系统和框架
- 包含：控制器、展示器、网关实现

#### 4. **基础设施层 (Infrastructure Layer)**
- 技术细节实现
- 框架和工具的具体使用
- 包含：数据库访问、外部API调用、消息队列

## 🔄 依赖注入配置示例

```java
// Infrastructure Config
@Configuration
public class BeanConfig {
    
    @Bean
    public UserRepository userRepository(JpaUserRepository jpaRepo) {
        return new UserRepositoryImpl(jpaRepo);
    }
    
    @Bean
    public CreateUserUseCase createUserUseCase(
        UserRepository userRepository,
        EventPublisher eventPublisher) {
        return new CreateUserUseCase(userRepository, eventPublisher);
    }
    
    @Bean
    public UserController userController(CreateUserUseCase useCase) {
        return new UserController(useCase);
    }
}
```

## 📦 模块化变体（大型项目）

```
project-root/
├── 📁 core/                            # 核心模块
│   ├── 📁 domain/                      # 领域模块
│   │   ├── src/main/java/com/example/domain/
│   │   └── build.gradle
│   │
│   └── 📁 application/                 # 应用模块
│       ├── src/main/java/com/example/application/
│       └── build.gradle
│
├── 📁 adapters/                        # 适配器模块
│   ├── 📁 web/                         # Web适配器
│   │   ├── src/main/java/com/example/web/
│   │   └── build.gradle
│   │
│   ├── 📁 persistence/                 # 持久化适配器
│   │   ├── src/main/java/com/example/persistence/
│   │   └── build.gradle
│   │
│   └── 📁 messaging/                   # 消息适配器
│       ├── src/main/java/com/example/messaging/
│       └── build.gradle
│
├── 📁 infrastructure/                  # 基础设施模块
│   ├── 📁 config/                      # 配置模块
│   │   └── build.gradle
│   │
│   └── 📁 external/                    # 外部服务模块
│       └── build.gradle
│
├── 📁 starter/                         # 启动模块
│   └── build.gradle
│
└── settings.gradle                     # 模块配置
```

## 🎯 关键实践建议

### 1. **依赖方向控制**
- 使用依赖注入框架（Spring, Dagger等）
- 遵循依赖倒置原则（DIP）
- 内层定义接口，外层实现

### 2. **测试策略**
- 领域层：纯单元测试，无外部依赖
- 应用层：用例测试，可模拟外部依赖
- 基础设施层：集成测试和端到端测试

### 3. **包结构组织**
- 按功能分包，而不是按技术分包
- 每个包有明确的职责边界
- 避免循环依赖

### 4. **代码规范**
- 领域对象保持纯净，无框架注解
- 使用值对象封装原始类型
- 避免贫血模型，将行为放在实体中

### 5. **配置管理**
- 将配置外部化
- 不同环境使用不同配置文件
- 敏感信息使用环境变量或配置中心

这个目录结构提供了清晰的整洁架构实现，可以根据项目需求和技术栈进行调整。每个层都有明确的职责和依赖关系，确保了代码的可维护性和可测试性。