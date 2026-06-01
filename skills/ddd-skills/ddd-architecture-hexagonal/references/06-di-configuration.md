# DI Configuration — 依赖注入配置

## 概述

六边形架构的依赖注入（DI）配置层负责将端口与适配器进行装配。DI 配置位于独立模块（`configuration` 模块或 `start` 模块），是整个架构中唯一知道所有实现类的层。

## Spring Boot 配置

### Java Config（推荐）

```java
// configuration/config/BeanConfig.java
@Configuration
public class BeanConfig {

    // 出站适配器装配

    @Bean
    public OrderRepository orderRepository(JpaOrderRepository jpaRepo, OrderMapper mapper) {
        return new PostgresOrderRepository(jpaRepo, mapper);
    }

    @Bean
    public PaymentGateway paymentGateway(StripeClient stripeClient) {
        return new StripePaymentGateway(stripeClient);
    }

    @Bean
    public EventPublisher eventPublisher(RabbitTemplate rabbitTemplate, ObjectMapper objectMapper) {
        return new RabbitMQEventPublisher(rabbitTemplate, objectMapper);
    }

    // 应用服务装配

    @Bean
    public CreateOrderUseCase createOrderUseCase(
            OrderRepository orderRepository,
            ProductRepository productRepository,
            OrderPricingService pricingService,
            EventPublisher eventPublisher) {
        return new CreateOrderService(orderRepository, productRepository, pricingService, eventPublisher);
    }

    @Bean
    public PayOrderUseCase payOrderUseCase(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher) {
        return new PayOrderService(orderRepository, paymentGateway, eventPublisher);
    }
}
```

### 环境配置切换

```java
// configuration/config/DevConfig.java
@Configuration
@Profile("dev")
public class DevConfig {

    @Bean
    public OrderRepository orderRepository() {
        return new InMemoryOrderRepository();  // 开发环境用内存实现
    }

    @Bean
    public PaymentGateway paymentGateway() {
        return new FakePaymentGateway();  // 开发环境用模拟支付
    }
}
```

### 多环境适配器映射

```yaml
# application-dev.yml
adapter:
  persistence: inmemory
  payment: fake
  messaging: inmemory

# application-prod.yml
adapter:
  persistence: postgres
  payment: stripe
  messaging: rabbitmq
```

## 领域服务注入

```java
// configuration/config/DomainServiceConfig.java
@Configuration
public class DomainServiceConfig {

    @Bean
    public OrderPricingService orderPricingService(DiscountPolicy discountPolicy) {
        return new OrderPricingService(discountPolicy);
    }

    @Bean
    public DiscountPolicy discountPolicy() {
        return new VolumeDiscountPolicy();  // 可替换为 SeasonalDiscountPolicy
    }
}

// 完整 Bean 依赖图
// DiscountPolicy → OrderPricingService
// OrderPricingService → CreateOrderService
// OrderRepository, ProductRepository, EventPublisher → CreateOrderService
// CreateOrderService → OrderController
```

## 非 Spring 环境

```java
// Pure Java DI — 手动构造
public class ApplicationContext {
    public static CreateOrderUseCase createOrderUseCase() {
        var jpaRepo = new JpaOrderRepository();
        var mapper = new OrderMapper();
        var orderRepo = new PostgresOrderRepository(jpaRepo, mapper);
        var pricingService = new OrderPricingService(new VolumeDiscountPolicy());
        var eventPublisher = new RabbitMQEventPublisher(/* ... */);
        return new CreateOrderService(orderRepo, pricingService, eventPublisher);
    }
}
```

## 适配器可替换性

六边形架构的核心优势在于适配器的可替换性。DI 配置是实现这一优势的关键。

```java
// 只需修改 DI 配置，即可切换整个后端存储
// 从 Postgres 切换到 MongoDB：

// Before:
// @Bean
// public OrderRepository orderRepository() {
//     return new PostgresOrderRepository(jpaRepo, mapper);
// }

// After:
@Bean
public OrderRepository orderRepository(MongoTemplate mongoTemplate) {
    return new MongoOrderRepository(mongoTemplate);
}

// Domain 层代码 — 零修改！
// Application 层代码 — 零修改！
// Adapter 层代码 — 新增 MongoOrderRepository 实现
```

## DI 配置检查清单

- [ ] Domain 层代码没有任何 DI 注解（无 `@Autowired`、`@Inject`、`@Resource`）
- [ ] 应用服务通过构造函数注入（而非字段注入）
- [ ] 每个出站端口在 DI 配置中都有对应的适配器实现
- [ ] 每个入站端口在 DI 配置中都有对应的应用服务实现
- [ ] 不同环境可以通过 Profile/Config 切换适配器实现
- [ ] 没有循环依赖
- [ ] 基础设施相关的 Bean 定义集中在配置模块

## 常见 DI 模式

| 模式 | 适用场景 | 示例 |
|------|---------|------|
| 策略模式 | 同一端口多个实现 | `DiscountPolicy` → `VolumeDiscountPolicy` / `SeasonalDiscountPolicy` |
| 装饰器模式 | 增强端口功能 | `LoggingEventPublisher` 包装 `RabbitMQEventPublisher` |
| 工厂模式 | 复杂创建逻辑 | `PaymentGatewayFactory.create("stripe")` |
| 代理模式 | 延迟初始化 | `LazyPaymentGateway` 代理 `StripePaymentGateway` |
