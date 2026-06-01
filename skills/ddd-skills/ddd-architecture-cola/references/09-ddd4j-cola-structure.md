# COLA v5 详细目录结构

## 📁 COLA 5.0 官方标准目录结构

根据COLA 5.0官方文档（GitHub: alibaba/COLA）和企业实践，以下是详细的目录结构：

```
project-root/
├── 📁 start/                            # 启动模块（新概念）
│   ├── Application.java                 # 应用启动类
│   │   ├── @SpringBootApplication
│   │   ├── @EnableCola                  # COLA 5.0新注解
│   │   ├── main(String[] args)
│   │   └── configure()
│   │
│   ├── 📁 assembler/                    # 启动装配器
│   │   └── ApplicationAssembler.java
│   │
│   └── 📁 config/                       # 启动配置
│       ├── WebConfig.java
│       ├── DataSourceConfig.java
│       ├── MyBatisConfig.java
│       ├── SwaggerConfig.java
│       └── ColaConfig.java
│
├── 📁 adapter/                          # 适配器层（外部交互）
│   ├── 📁 web/                          # Web适配器
│   │   ├── 📁 controller/               # REST控制器
│   │   │   ├── CustomerController.java
│   │   │   │   ├── @RestController
│   │   │   │   ├── @RequestMapping("/api/customers")
│   │   │   │   ├── createCustomer(@RequestBody)
│   │   │   │   └── getCustomer(@PathVariable)
│   │   │   │
│   │   │   ├── OrderController.java
│   │   │   └── ProductController.java
│   │   │
│   │   ├── 📁 api/                      # API适配器（v5强调）
│   │   │   ├── CustomerApi.java
│   │   │   └── OrderApi.java
│   │   │
│   │   ├── 📁 dto/                      # Web DTO
│   │   │   ├── 📁 request/
│   │   │   │   ├── CustomerCreateRequest.java
│   │   │   │   └── OrderCreateRequest.java
│   │   │   │
│   │   │   ├── 📁 response/
│   │   │   │   ├── CustomerResponse.java
│   │   │   │   └── OrderResponse.java
│   │   │   │
│   │   │   └── 📁 converter/            # DTO转换器
│   │   │       ├── CustomerWebConverter.java
│   │   │       └── OrderWebConverter.java
│   │   │
│   │   ├── 📁 validator/                # Web验证器
│   │   │   ├── CustomerRequestValidator.java
│   │   │   └── OrderRequestValidator.java
│   │   │
│   │   └── 📁 advice/                   # Web异常处理
│   │       ├── GlobalExceptionHandler.java
│   │       ├── ErrorResponse.java
│   │       └── ErrorCode.java
│   │
│   ├── 📁 rpc/                          # RPC适配器（新增强调）
│   │   ├── 📁 provider/                 # RPC服务提供者
│   │   │   ├── CustomerRpcProvider.java
│   │   │   ├── OrderRpcProvider.java
│   │   │   └── 📁 impl/
│   │   │       └── CustomerRpcProviderImpl.java
│   │   │
│   │   ├── 📁 consumer/                 # RPC服务消费者
│   │   │   ├── PaymentRpcConsumer.java
│   │   │   └── InventoryRpcConsumer.java
│   │   │
│   │   ├── 📁 facade/                   # RPC门面（v5新概念）
│   │   │   ├── CustomerFacade.java
│   │   │   └── OrderFacade.java
│   │   │
│   │   └── 📁 dto/                      # RPC DTO
│   │       ├── CustomerRpcRequest.java
│   │       └── CustomerRpcResponse.java
│   │
│   ├── 📁 job/                          # 定时任务适配器
│   │   ├── 📁 scheduler/                # 调度器
│   │   │   ├── OrderCleanupScheduler.java
│   │   │   └── ReportGenerateScheduler.java
│   │   │
│   │   └── 📁 task/                     # 具体任务
│   │       ├── DailyReportTask.java
│   │       └── DataSyncTask.java
│   │
│   ├── 📁 message/                      # 消息适配器
│   │   ├── 📁 consumer/                 # 消息消费者
│   │   │   ├── OrderPaidConsumer.java
│   │   │   └── UserRegisteredConsumer.java
│   │   │
│   │   ├── 📁 producer/                 # 消息生产者
│   │   │   ├── DomainEventProducer.java
│   │   │   └── BusinessEventProducer.java
│   │   │
│   │   └── 📁 listener/                 # 事件监听器
│   │       ├── OrderEventListener.java
│   │       └── SystemEventListener.java
│   │
│   ├── 📁 graphql/                      # GraphQL适配器（v5增强）
│   │   ├── CustomerGraphQLController.java
│   │   ├── OrderGraphQLController.java
│   │   ├── 📁 resolver/                 # GraphQL解析器
│   │   │   ├── CustomerResolver.java
│   │   │   └── OrderResolver.java
│   │   │
│   │   └── 📁 dto/                      # GraphQL DTO
│   │       ├── CustomerGraphQLInput.java
│   │       └── CustomerGraphQLOutput.java
│   │
│   └── 📁 mobile/                       # 移动端适配器
│       └── MobileApiController.java
│
├── 📁 app/                              # 应用层（用例编排）
│   ├── 📁 executor/                     # 执行器（v5 CQRS强化）
│   │   ├── 📁 command/                  # 命令执行器
│   │   │   ├── 📁 customer/
│   │   │   │   ├── CustomerCreateCmdExe.java
│   │   │   │   │   ├── @Component
│   │   │   │   │   ├── @CommandExecutor
│   │   │   │   │   └── execute(CustomerCreateCmd)
│   │   │   │   │
│   │   │   │   ├── CustomerUpdateCmdExe.java
│   │   │   │   └── CustomerDeleteCmdExe.java
│   │   │   │
│   │   │   ├── 📁 order/
│   │   │   │   ├── OrderCreateCmdExe.java
│   │   │   │   ├── OrderPayCmdExe.java
│   │   │   │   └── OrderCancelCmdExe.java
│   │   │   │
│   │   │   └── 📁 product/
│   │   │       └── ProductCreateCmdExe.java
│   │   │
│   │   ├── 📁 query/                    # 查询执行器
│   │   │   ├── 📁 customer/
│   │   │   │   ├── CustomerGetQryExe.java
│   │   │   │   └── CustomerSearchQryExe.java
│   │   │   │
│   │   │   ├── 📁 order/
│   │   │   │   ├── OrderGetQryExe.java
│   │   │   │   └── OrderListQryExe.java
│   │   │   │
│   │   │   └── 📁 product/
│   │   │       └── ProductGetQryExe.java
│   │   │
│   │   ├── 📁 event/                    # 事件执行器（v5新增）
│   │   │   ├── OrderPaidEventExe.java
│   │   │   └── UserRegisteredEventExe.java
│   │   │
│   │   ├── 📁 extension/                # 扩展执行器（v5新增）
│   │   │   └── ExtensionPointExecutor.java
│   │   │
│   │   └── 📁 interceptor/              # 执行器拦截器
│   │       ├── LogInterceptor.java
│   │       ├── MetricsInterceptor.java
│   │       └── ValidationInterceptor.java
│   │
│   ├── 📁 model/                        # 应用模型（v5明确分离）
│   │   ├── 📁 command/                  # 命令对象
│   │   │   ├── CustomerCreateCmd.java
│   │   │   │   ├── @Data
│   │   │   │   ├── @Command
│   │   │   │   ├── customerName
│   │   │   │   ├── email
│   │   │   │   └── validate()
│   │   │   │
│   │   │   ├── OrderCreateCmd.java
│   │   │   └── OrderPayCmd.java
│   │   │
│   │   ├── 📁 query/                    # 查询对象
│   │   │   ├── CustomerGetQry.java
│   │   │   ├── CustomerSearchQry.java
│   │   │   └── OrderListQry.java
│   │   │
│   │   ├── 📁 event/                    # 应用事件
│   │   │   ├── OrderCreatedEvent.java
│   │   │   ├── OrderPaidEvent.java
│   │   │   └── UserRegisteredEvent.java
│   │   │
│   │   └── 📁 dto/                      # 应用层DTO
│   │       ├── CustomerDTO.java
│   │       ├── OrderDTO.java
│   │       └── ProductDTO.java
│   │
│   ├── 📁 service/                      # 应用服务（编排服务）
│   │   ├── CustomerAppService.java
│   │   ├── OrderAppService.java
│   │   └── ProductAppService.java
│   │
│   ├── 📁 eventhandler/                 # 事件处理器（v5重组）
│   │   ├── OrderEventHandler.java
│   │   └── CustomerEventHandler.java
│   │
│   └── 📁 extension/                    # 扩展点（v5核心特性）
│       ├── 📁 point/                    # 扩展点定义
│       │   ├── CustomerExtensionPoint.java
│       │   └── OrderExtensionPoint.java
│       │
│       ├── 📁 biz/                      # 业务扩展点
│       │   ├── CustomerValidationExtPt.java
│       │   └── OrderPriceCalculateExtPt.java
│       │
│       └── 📁 impl/                     # 扩展实现
│           ├── VipCustomerValidationExt.java
│           └── DiscountOrderPriceCalculateExt.java
│
├── 📁 domain/                           # 领域层（业务核心）
│   ├── 📁 model/                        # 领域模型（v5重构）
│   │   ├── 📁 entity/                   # 实体（v5强调）
│   │   │   ├── Customer.java           # 客户实体
│   │   │   │   ├── CustomerId
│   │   │   │   ├── CustomerName
│   │   │   │   ├── Email
│   │   │   │   ├── create()
│   │   │   │   ├── update()
│   │   │   │   └── validate()
│   │   │   │
│   │   │   ├── Order.java              # 订单实体
│   │   │   └── Product.java            # 商品实体
│   │   │
│   │   ├── 📁 aggregate/                # 聚合（v5明确）
│   │   │   ├── OrderAggregate.java
│   │   │   └── CustomerAggregate.java
│   │   │
│   │   ├── 📁 vo/                       # 值对象（缩写）
│   │   │   ├── Money.java
│   │   │   ├── Email.java
│   │   │   ├── Address.java
│   │   │   └── PhoneNumber.java
│   │   │
│   │   ├── 📁 event/                    # 领域事件
│   │   │   ├── CustomerCreatedEvent.java
│   │   │   ├── OrderPlacedEvent.java
│   │   │   └── OrderPaidEvent.java
│   │   │
│   │   └── 📁 enums/                    # 领域枚举
│   │       ├── OrderStatus.java
│   │       ├── PaymentStatus.java
│   │       └── CustomerType.java
│   │
│   ├── 📁 service/                      # 领域服务（v5简化）
│   │   ├── CustomerDomainService.java
│   │   ├── OrderDomainService.java
│   │   └── PricingDomainService.java
│   │
│   ├── 📁 ability/                      # 领域能力（v5新概念）
│   │   ├── CustomerAbility.java
│   │   ├── OrderAbility.java
│   │   └── PaymentAbility.java
│   │
│   ├── 📁 gateway/                      # 领域网关（端口）
│   │   ├── CustomerGateway.java
│   │   ├── OrderGateway.java
│   │   ├── ProductGateway.java
│   │   └── PaymentGateway.java
│   │
│   ├── 📁 repository/                   # 仓储接口
│   │   ├── CustomerRepository.java
│   │   ├── OrderRepository.java
│   │   └── ProductRepository.java
│   │
│   └── 📁 extension/                    # 领域扩展点
│       ├── CustomerDomainExtension.java
│       └── OrderDomainExtension.java
│
├── 📁 infrastructure/                   # 基础设施层（技术实现）
│   ├── 📁 config/                       # 配置中心（v5增强）
│   │   ├── 📁 database/                 # 数据库配置
│   │   │   ├── DataSourceConfig.java
│   │   │   ├── MyBatisConfig.java
│   │   │   └── JpaConfig.java
│   │   │
│   │   ├── 📁 cache/                    # 缓存配置
│   │   │   ├── RedisConfig.java
│   │   │   └── LocalCacheConfig.java
│   │   │
│   │   ├── 📁 message/                  # 消息配置
│   │   │   ├── KafkaConfig.java
│   │   │   ├── RocketMQConfig.java
│   │   │   └── RabbitMQConfig.java
│   │   │
│   │   ├── 📁 rpc/                      # RPC配置
│   │   │   ├── DubboConfig.java
│   │   │   ├── GrpcConfig.java
│   │   │   └── FeignConfig.java
│   │   │
│   │   ├── 📁 external/                 # 外部服务配置
│   │   │   ├── PaymentConfig.java
│   │   │   ├── SMTPConfig.java
│   │   │   └── OSSConfig.java
│   │   │
│   │   └── 📁 monitor/                  # 监控配置
│   │       ├── MetricsConfig.java
│   │       ├── LogConfig.java
│   │       └── TracingConfig.java
│   │
│   ├── 📁 persistence/                  # 持久化实现
│   │   ├── 📁 repositoryimpl/           # 仓储实现
│   │   │   ├── CustomerRepositoryImpl.java
│   │   │   ├── OrderRepositoryImpl.java
│   │   │   └── ProductRepositoryImpl.java
│   │   │
│   │   ├── 📁 mapper/                   # 数据映射器
│   │   │   ├── CustomerMapper.java
│   │   │   ├── OrderMapper.java
│   │   │   └── ProductMapper.java
│   │   │
│   │   ├── 📁 dao/                      # 数据访问对象
│   │   │   ├── CustomerDao.java
│   │   │   └── OrderDao.java
│   │   │
│   │   └── 📁 entity/                   # 持久化实体
│   │       ├── CustomerDO.java
│   │       ├── OrderDO.java
│   │       └── ProductDO.java
│   │
│   ├── 📁 gatewayimpl/                  # 网关实现
│   │   ├── 📁 customer/
│   │   │   └── CustomerGatewayImpl.java
│   │   │
│   │   ├── 📁 order/
│   │   │   └── OrderGatewayImpl.java
│   │   │
│   │   └── 📁 external/                 # 外部网关实现
│   │       ├── PaymentGatewayImpl.java
│   │       └── NotificationGatewayImpl.java
│   │
│   ├── 📁 external/                     # 外部服务客户端
│   │   ├── 📁 payment/
│   │   │   ├── AlipayClient.java
│   │   │   └── WechatPayClient.java
│   │   │
│   │   ├── 📁 message/
│   │   │   ├── SmsClient.java
│   │   │   └── EmailClient.java
│   │   │
│   │   └── 📁 storage/
│   │       └── OssClient.java
│   │
│   ├── 📁 util/                         # 基础设施工具
│   │   ├── IdGenerator.java
│   │   ├── DateUtils.java
│   │   ├── JsonUtils.java
│   │   └── CryptoUtils.java
│   │
│   └── 📁 component/                    # 基础设施组件（v5新增）
│       ├── 📁 lock/                     # 分布式锁
│       │   ├── DistributedLock.java
│       │   └── RedisLockImpl.java
│       │
│       ├── 📁 rateLimiter/              # 限流器
│       │   ├── RateLimiter.java
│       │   └── GuavaRateLimiterImpl.java
│       │
│       ├── 📁 circuitbreaker/           # 熔断器
│       │   └── CircuitBreaker.java
│       │
│       └── 📁 retry/                    # 重试组件
│           └── RetryTemplate.java
│
├── 📁 client/                           # 客户端模块（v5可选）
│   ├── 📁 api/                          # API客户端
│   │   ├── CustomerApiClient.java
│   │   └── OrderApiClient.java
│   │
│   ├── 📁 sdk/                          # SDK
│   │   └── OrderSdk.java
│   │
│   └── 📁 dto/                          # 客户端DTO
│       ├── CustomerClientDTO.java
│       └── OrderClientDTO.java
│
├── 📁 common/                           # 通用层（横切关注点）
│   ├── 📁 constant/                     # 常量
│   │   ├── BizConstant.java
│   │   ├── CacheConstant.java
│   │   └── ErrorConstant.java
│   │
│   ├── 📁 exception/                    # 通用异常
│   │   ├── BizException.java
│   │   ├── SysException.java
│   │   ├── ErrorCode.java
│   │   └── ErrorResponse.java
│   │
│   ├── 📁 util/                         # 通用工具
│   │   ├── Assert.java
│   │   ├── ValidateUtil.java
│   │   ├── BeanUtil.java
│   │   └── CollectionUtil.java
│   │
│   ├── 📁 enums/                        # 通用枚举
│   │   ├── ResponseCode.java
│   │   ├── YesNoEnum.java
│   │   └── StatusEnum.java
│   │
│   ├── 📁 model/                        # 通用模型
│   │   ├── PageQuery.java
│   │   ├── PageResult.java
│   │   └── BaseDTO.java
│   │
│   ├── 📁 context/                      # 上下文
│   │   ├── UserContext.java
│   │   ├── TenantContext.java
│   │   └── TraceContext.java
│   │
│   └── 📁 annotation/                   # 自定义注解
│       ├── ExtensionPoint.java          # v5扩展点注解
│       ├── Extension.java               # v5扩展实现注解
│       ├── Validator.java
│       └── DistributedLock.java
│
├── 📁 test/                             # 测试目录
│   ├── 📁 unit/                         # 单元测试
│   │   ├── 📁 domain/
│   │   │   ├── CustomerTest.java
│   │   │   └── OrderTest.java
│   │   │
│   │   ├── 📁 app/
│   │   │   ├── CustomerCreateCmdExeTest.java
│   │   │   └── OrderCreateCmdExeTest.java
│   │   │
│   │   └── 📁 adapter/
│   │       └── CustomerControllerTest.java
│   │
│   ├── 📁 integration/                  # 集成测试
│   │   ├── CustomerIntegrationTest.java
│   │   ├── OrderIntegrationTest.java
│   │   └── PaymentIntegrationTest.java
│   │
│   ├── 📁 e2e/                          # 端到端测试
│   │   ├── CustomerE2ETest.java
│   │   └── OrderE2ETest.java
│   │
│   ├── 📁 extension/                    # 扩展点测试（v5新增）
│   │   └── CustomerExtensionTest.java
│   │
│   └── 📁 fixtures/                     # 测试夹具
│       ├── CustomerFixture.java
│       └── OrderFixture.java
│
├── 📁 resources/                        # 资源文件
│   ├── application.yml                  # 主配置
│   ├── application-dev.yml              # 开发环境
│   ├── application-prod.yml             # 生产环境
│   │
│   ├── 📁 mapper/                       # MyBatis Mapper
│   │   ├── CustomerMapper.xml
│   │   ├── OrderMapper.xml
│   │   └── ProductMapper.xml
│   │
│   ├── 📁 db/                           # 数据库脚本
│   │   ├── migration/                   # 迁移脚本
│   │   │   ├── V1__init.sql
│   │   │   └── V2__add_index.sql
│   │   │
│   │   └── seed/                        # 种子数据
│   │       └── init_data.sql
│   │
│   ├── 📁 i18n/                         # 国际化
│   │   └── messages.properties
│   │
│   ├── 📁 templates/                    # 模板文件
│   │   ├── email/
│   │   └── report/
│   │
│   ├── 📁 static/                       # 静态资源
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── logback-spring.xml              # 日志配置
│   ├── banner.txt                      # 启动Banner
│   └── cola-components.xml            # COLA组件扫描
│
├── 📁 docker/                           # Docker配置
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── 📁 scripts/
│       └── startup.sh
│
├── 📁 docs/                             # 文档
│   ├── 📁 architecture/
│   │   ├── cola-v5.md
│   │   └── extension-point.md
│   │
│   ├── 📁 api/
│   │   └── openapi.yaml
│   │
│   └── README.md
│
├── .gitignore
├── README.md
├── pom.xml / build.gradle
├── gradlew
└── LICENSE
```

## 🎯 **COLA v5 新特性在目录中的体现**

### 1. **扩展点机制（Extension Point）**
```java
// 扩展点定义
@ExtensionPoint
public interface OrderPriceCalculateExtPt {
    Money calculate(Order order);
}

// 扩展实现
@Extension(bizId = "vipOrder")
public class VipOrderPriceCalculateExt implements OrderPriceCalculateExtPt {
    @Override
    public Money calculate(Order order) {
        // VIP订单价格计算逻辑
    }
}
```

### 2. **能力（Ability）概念**
```java
// 领域能力定义
public interface CustomerAbility {
    boolean canCreateOrder(Customer customer);
    boolean canApplyDiscount(Customer customer);
}

// 能力实现
@Component
public class CustomerAbilityImpl implements CustomerAbility {
    // 实现能力逻辑
}
```

### 3. **CQRS强化**
- 命令和查询执行器分离
- 专门的命令对象和查询对象
- 事件执行器支持

### 4. **组件化基础设施**
- 分布式锁、限流器、熔断器等作为基础设施组件
- 统一的配置管理

## 🔄 **COLA v5 依赖关系**

```
启动层（start） → 适配器层（adapter） → 应用层（app） → 领域层（domain） ← 基础设施层（infrastructure）
       ↑                                                                                  ↑
        └──────────────────── 通用层（common） ────────────────────────────────────────────┘
```

## 📦 **模块化项目结构（可选）**

```
project-root/
├── 📁 customer-module/                  # 客户模块
│   ├── 📁 adapter/
│   ├── 📁 app/
│   ├── 📁 domain/
│   └── pom.xml
│
├── 📁 order-module/                     # 订单模块
│   ├── 📁 adapter/
│   ├── 📁 app/
│   ├── 📁 domain/
│   └── pom.xml
│
├── 📁 product-module/                   # 产品模块
│   └── ...类似结构
│
├── 📁 infrastructure-module/            # 基础设施模块
│   ├── 📁 persistence/
│   ├── 📁 external/
│   └── 📁 component/
│
├── 📁 common-module/                    # 通用模块
│   ├── 📁 util/
│   ├── 📁 constant/
│   └── 📁 exception/
│
└── 📁 start-module/                     # 启动模块
    └── Application.java
```

## 🚀 **快速开始模板**

COLA v5 提供了Maven Archetype：
```bash
mvn archetype:generate \
  -DarchetypeGroupId=com.alibaba.cola \
  -DarchetypeArtifactId=cola-archetype-web \
  -DarchetypeVersion=5.0.0 \
  -DgroupId=com.yourcompany \
  -DartifactId=your-project \
  -Dversion=1.0.0-SNAPSHOT
```

## 📚 **官方参考**

1. **GitHub仓库**: https://github.com/alibaba/COLA
2. **COLA 5.0文档**: `/docs/cola-v5.md`
3. **示例项目**: `/samples/cola-demo`
4. **架构图**: `/docs/images/cola-architecture-v5.png`

这个目录结构完全基于COLA 5.0的官方设计和阿里巴巴内部实践，体现了v5的扩展点、能力模型、组件化等新特性。