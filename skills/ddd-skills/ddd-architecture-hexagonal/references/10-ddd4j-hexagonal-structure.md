# 六边形架构详细目录结构参考

## 📁 项目根目录结构

```
project-root/
├── 📁 src/                              # 源代码目录
│   ├── 📁 application/                  # 应用层（用例层）
│   │   ├── 📁 ports/                    # 端口定义（接口）
│   │   │   ├── 📁 inbound/             # 入站端口（驱动端）
│   │   │   │   ├── UserService.java    # 用户服务接口
│   │   │   │   ├── OrderService.java   # 订单服务接口
│   │   │   │   └── PaymentService.java # 支付服务接口
│   │   │   │
│   │   │   └── 📁 outbound/            # 出站端口（被驱动端）
│   │   │       ├── UserRepository.java    # 用户仓储接口
│   │   │       ├── OrderRepository.java   # 订单仓储接口
│   │   │       ├── PaymentProvider.java   # 支付提供商接口
│   │   │       └── NotificationService.java # 通知服务接口
│   │   │
│   │   ├── 📁 services/                 # 应用服务实现
│   │   │   ├── UserServiceImpl.java
│   │   │   ├── OrderServiceImpl.java
│   │   │   └── PaymentServiceImpl.java
│   │   │
│   │   ├── 📁 usecases/                 # 具体用例
│   │   │   ├── user/                    # 用户相关用例
│   │   │   │   ├── CreateUserUseCase.java
│   │   │   │   ├── UpdateUserUseCase.java
│   │   │   │   └── GetUserUseCase.java
│   │   │   │
│   │   │   ├── order/                   # 订单相关用例
│   │   │   │   ├── CreateOrderUseCase.java
│   │   │   │   ├── ProcessOrderUseCase.java
│   │   │   │   └── CancelOrderUseCase.java
│   │   │   │
│   │   │   └── 📁 dto/                  # 数据传输对象
│   │   │       ├── UserDTO.java
│   │   │       ├── OrderDTO.java
│   │   │       └── PaymentDTO.java
│   │   │
│   │   └── 📁 exception/                # 应用层异常
│   │       ├── ApplicationException.java
│   │       ├── ValidationException.java
│   │       └── BusinessRuleException.java
│   │
│   ├── 📁 domain/                       # 领域层（核心业务逻辑）
│   │   ├── 📁 models/                   # 领域模型/实体
│   │   │   ├── User.java               # 用户聚合根
│   │   │   ├── Order.java              # 订单聚合根
│   │   │   ├── OrderItem.java          # 值对象/实体
│   │   │   ├── Product.java            # 实体
│   │   │   └── Address.java            # 值对象
│   │   │
│   │   ├── 📁 valueobjects/             # 值对象
│   │   │   ├── Email.java
│   │   │   ├── Money.java
│   │   │   ├── Quantity.java
│   │   │   └── DateRange.java
│   │   │
│   │   ├── 📁 events/                   # 领域事件
│   │   │   ├── DomainEvent.java        # 基础事件接口
│   │   │   ├── UserCreatedEvent.java
│   │   │   ├── OrderPlacedEvent.java
│   │   │   └── PaymentProcessedEvent.java
│   │   │
│   │   ├── 📁 services/                 # 领域服务
│   │   │   ├── UserRegistrationService.java
│   │   │   ├── OrderValidationService.java
│   │   │   └── PricingService.java
│   │   │
│   │   ├── 📁 repositories/             # 领域仓储接口
│   │   │   ├── IUserRepository.java
│   │   │   ├── IOrderRepository.java
│   │   │   └── IProductRepository.java
│   │   │
│   │   └── 📁 exception/                # 领域层异常
│   │       ├── DomainException.java
│   │       └── InvalidStateException.java
│   │
│   ├── 📁 infrastructure/               # 基础设施层（适配器实现）
│   │   ├── 📁 adapters/                 # 适配器实现
│   │   │   ├── 📁 inbound/             # 入站适配器（驱动适配器）
│   │   │   │   ├── 📁 web/             # Web适配器
│   │   │   │   │   ├── 📁 controllers/ # REST控制器
│   │   │   │   │   │   ├── UserController.java
│   │   │   │   │   │   ├── OrderController.java
│   │   │   │   │   │   └── PaymentController.java
│   │   │   │   │   │
│   │   │   │   │   ├── 📁 dto/         # 请求/响应DTO
│   │   │   │   │   │   ├── request/
│   │   │   │   │   │   └── response/
│   │   │   │   │   │
│   │   │   │   │   ├── 📁 filters/     # Web过滤器
│   │   │   │   │   ├── 📁 interceptors/# 拦截器
│   │   │   │   │   └── 📁 exception/   # Web异常处理
│   │   │   │   │
│   │   │   │   ├── 📁 cli/             # 命令行适配器
│   │   │   │   │   └── CommandLineInterface.java
│   │   │   │   │
│   │   │   │   ├── 📁 messaging/       # 消息适配器
│   │   │   │   │   ├── MessageConsumer.java
│   │   │   │   │   └── EventSubscriber.java
│   │   │   │   │
│   │   │   │   └── 📁 scheduled/       # 定时任务适配器
│   │   │   │       └── ScheduledTasks.java
│   │   │   │
│   │   │   └── 📁 outbound/            # 出站适配器（被驱动适配器）
│   │   │       ├── 📁 persistence/     # 持久化适配器
│   │   │       │   ├── 📁 repositories/ # 仓储实现
│   │   │       │   │   ├── UserRepositoryImpl.java
│   │   │       │   │   ├── OrderRepositoryImpl.java
│   │   │       │   │   └── ProductRepositoryImpl.java
│   │   │       │   │
│   │   │       │   ├── 📁 mappers/     # 数据映射器
│   │   │       │   │   ├── UserMapper.java
│   │   │       │   │   ├── OrderMapper.java
│   │   │       │   │   └── ProductMapper.java
│   │   │       │   │
│   │   │       │   └── 📁 entities/    # 持久化实体
│   │   │       │       ├── UserEntity.java
│   │   │       │       ├── OrderEntity.java
│   │   │       │       └── ProductEntity.java
│   │   │       │
│   │   │       ├── 📁 external/        # 外部服务适配器
│   │   │       │   ├── PaymentProviderAdapter.java
│   │   │       │   ├── EmailServiceAdapter.java
│   │   │       │   ├── SMSServiceAdapter.java
│   │   │       │   └── ThirdPartyApiClient.java
│   │   │       │
│   │   │       ├── 📁 messaging/       # 消息适配器
│   │   │       │   ├── EventPublisher.java
│   │   │       │   ├── MessageProducer.java
│   │   │       │   └── QueueSender.java
│   │   │       │
│   │   │       └── 📁 cache/           # 缓存适配器
│   │   │           ├── RedisCacheAdapter.java
│   │   │           └── LocalCacheAdapter.java
│   │   │
│   │   ├── 📁 config/                   # 配置类
│   │   │   ├── DatabaseConfig.java
│   │   │   ├── WebConfig.java
│   │   │   ├── SecurityConfig.java
│   │   │   ├── CacheConfig.java
│   │   │   └── BeanConfig.java
│   │   │
│   │   ├── 📁 database/                 # 数据库相关
│   │   │   ├── 📁 migrations/          # 数据库迁移脚本
│   │   │   │   ├── V1__init.sql
│   │   │   │   ├── V2__add_users.sql
│   │   │   │   └── V3__add_orders.sql
│   │   │   │
│   │   │   └── 📁 enums/               # 数据库枚举
│   │   │       ├── OrderStatus.java
│   │   │       └── UserRole.java
│   │   │
│   │   └── 📁 security/                 # 安全相关
│   │       ├── JwtTokenProvider.java
│   │       ├── SecurityUtils.java
│   │       └── PasswordEncoder.java
│   │
│   ├── 📁 shared/                       # 共享组件
│   │   ├── 📁 kernel/                   # 核心共享
│   │   │   ├── BaseEntity.java
│   │   │   ├── AggregateRoot.java
│   │   │   ├── ValueObject.java
│   │   │   └── Identifier.java
│   │   │
│   │   ├── 📁 utils/                    # 工具类
│   │   │   ├── DateUtils.java
│   │   │   ├── StringUtils.java
│   │   │   ├── Validator.java
│   │   │   └── ObjectMapperUtils.java
│   │   │
│   │   ├── 📁 constants/                # 常量定义
│   │   │   ├── AppConstants.java
│   │   │   ├── ErrorCodes.java
│   │   │   └── ValidationMessages.java
│   │   │
│   │   └── 📁 exception/                # 全局异常
│   │       ├── GlobalException.java
│   │       ├── ErrorResponse.java
│   │       └── ExceptionHandler.java
│   │
│   └── MainApplication.java             # 应用启动类
│
├── 📁 test/                             # 测试目录
│   ├── 📁 unit/                         # 单元测试
│   │   ├── 📁 domain/                   # 领域层测试
│   │   │   ├── UserTest.java
│   │   │   ├── OrderTest.java
│   │   │   └── services/
│   │   │
│   │   ├── 📁 application/              # 应用层测试
│   │   │   ├── services/
│   │   │   └── usecases/
│   │   │
│   │   └── 📁 infrastructure/           # 基础设施层测试
│   │       ├── adapters/
│   │       └── mappers/
│   │
│   ├── 📁 integration/                  # 集成测试
│   │   ├── RepositoryIntegrationTest.java
│   │   ├── ServiceIntegrationTest.java
│   │   └── ControllerIntegrationTest.java
│   │
│   ├── 📁 e2e/                          # 端到端测试
│   │   └── ApiE2ETest.java
│   │
│   └── 📁 acceptance/                   # 验收测试
│       └── UserAcceptanceTest.java
│
├── 📁 resources/                        # 资源文件
│   ├── application.properties           # 主配置文件
│   ├── application-dev.properties       # 开发环境配置
│   ├── application-prod.properties      # 生产环境配置
│   ├── application-test.properties      # 测试环境配置
│   ├── 📁 db/                           # 数据库相关
│   │   ├── migration/                   # Flyway/Liquibase迁移
│   │   └── seed/                        # 种子数据
│   ├── 📁 i18n/                         # 国际化
│   │   ├── messages.properties
│   │   ├── messages_en.properties
│   │   └── messages_zh.properties
│   ├── 📁 templates/                    # 模板文件
│   │   ├── email/
│   │   └── reports/
│   └── logback-spring.xml              # 日志配置
│
├── 📁 docker/                           # Docker相关
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose-dev.yml
│   └── 📁 scripts/                      # Docker脚本
│
├── 📁 docs/                             # 文档
│   ├── architecture/                    # 架构文档
│   │   ├── hexagonal-architecture.md
│   │   ├── decision-records/           # 架构决策记录
│   │   └── diagrams/                   # 架构图
│   ├── api/                            # API文档
│   │   ├── swagger.yaml
│   │   └── postman-collection.json
│   └── deployment/                     # 部署文档
│
├── 📁 scripts/                          # 脚本文件
│   ├── build.sh
│   ├── deploy.sh
│   ├── migrate.sh
│   └── code-quality/
│
├── 📁 build/                            # 构建输出（生成）
│
├── .gitignore                          # Git忽略配置
├── README.md                           # 项目说明
├── pom.xml / build.gradle              # 构建配置
├── Makefile                            # Make命令
├── LICENSE                             # 许可证
└── CHANGELOG.md                        # 变更日志
```

## 🔄 依赖关系说明

### 核心原则
1. **领域层**：无外部依赖，纯业务逻辑
2. **应用层**：依赖领域层，定义用例和端口
3. **基础设施层**：依赖应用层（通过端口），实现具体技术细节
4. **共享组件**：被所有层使用

### 依赖方向
```
外部适配器 → 应用层端口 ← 应用服务 → 领域层
    ↑                             ↓
基础设施层                      领域模型
    ↓                             ↑
外部适配器 → 基础设施端口 ← 应用服务
```

## 📦 模块化变体（可选）

对于大型项目，可以使用模块化结构：

```
project-root/
├── 📁 modules/
│   ├── 📁 user-module/           # 用户模块
│   │   ├── src/
│   │   │   ├── main/
│   │   │   └── test/
│   │   └── build.gradle
│   │
│   ├── 📁 order-module/          # 订单模块
│   │   ├── src/
│   │   │   ├── main/
│   │   │   └── test/
│   │   └── build.gradle
│   │
│   └── 📁 payment-module/        # 支付模块
│       ├── src/
│       │   ├── main/
│       │   └── test/
│       └── build.gradle
│
├── 📁 shared/                     # 共享模块
│   ├── kernel/
│   └── utils/
│
└── build.gradle                  # 根构建文件
```

## 🎯 关键目录说明

### 1. **ports/ 目录**
- **inbound/**: 定义应用对外提供的服务接口
- **outbound/**: 定义应用依赖的外部服务接口

### 2. **adapters/ 目录**
- **inbound/**: 将外部请求转换为应用理解的格式
- **outbound/**: 将应用请求转换为外部系统理解的格式

### 3. **领域层组织结构**
- **models/**: 聚合根和实体
- **valueobjects/**: 不可变的值对象
- **events/**: 领域事件
- **services/**: 领域服务（无状态的业务逻辑）

### 4. **测试策略**
- **单元测试**: 每个层独立测试
- **集成测试**: 端口与适配器集成测试
- **端到端测试**: 完整业务流程测试

## 🛠 最佳实践建议

1. **严格依赖方向**: 内层不依赖外层
2. **接口隔离**: 每个适配器实现特定端口
3. **依赖注入**: 通过构造函数注入依赖
4. **持续集成**: 每层都有对应的测试
5. **文档完整**: 每个端口和适配器都有文档说明

这个目录结构提供了清晰的六边形架构实现，可以根据项目规模和技术栈进行调整。