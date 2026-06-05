# 05 — Composition Root: Dependency Injection Assembly

> Composition Root 是洋葱架构中唯一知道所有具体实现类的模块，负责装配整个依赖图。

## 核心原则

1. **集中原则**：所有 DI 配置放在 composition 模块，禁止在各层使用 `@Autowired` + 组件扫描
2. **唯一知情者**：Composition Root 是唯一 import 所有模块具体类型的代码位置
3. **组合而非分散**：不要在 Controller 中 `new Service()`，不要在 Service 中 `new Repository()`

## 代码模板

### Spring Boot @Configuration

```java
// composition/config/OrderModuleConfig.java
@Configuration
public class OrderModuleConfig {

    @Bean
    public OrderRepository orderRepository(JpaOrderRepository jpaRepo, OrderMapper mapper) {
        return new OrderRepositoryImpl(jpaRepo, mapper);
    }

    @Bean
    public OrderApplicationService orderApplicationService(
            OrderRepository orderRepository,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher,
            OrderAssembler orderAssembler) {
        return new OrderApplicationServiceImpl(
            orderRepository, paymentGateway, eventPublisher, orderAssembler);
    }

    @Bean
    public OrderController orderController(
            OrderApplicationService orderAppService) {
        return new OrderController(orderAppService);
    }
}

// composition/config/InfrastructureConfig.java
@Configuration
public class InfrastructureConfig {

    @Bean
    public PaymentGateway paymentGateway(RestTemplate restTemplate) {
        return new PaymentGatewayImpl(restTemplate);
    }

    @Bean
    public EventPublisher eventPublisher(KafkaTemplate<String, Object> kafkaTemplate,
                                          ObjectMapper objectMapper) {
        return new KafkaEventPublisher(kafkaTemplate, objectMapper);
    }

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
        return mapper;
    }
}
```

### 手动 DI（无框架）

```java
// composition/config/ManualCompositionRoot.java
public class ManualCompositionRoot {
    private final OrderController orderController;

    public ManualCompositionRoot() {
        // 1. Infrastructure
        JpaOrderRepository jpaRepo = new JpaOrderRepository();
        OrderMapper mapper = new OrderMapper();
        OrderRepository orderRepo = new OrderRepositoryImpl(jpaRepo, mapper);

        PaymentGateway paymentGateway = new PaymentGatewayImpl(new RestTemplate());
        EventPublisher eventPublisher = new KafkaEventPublisher(/* config */);

        // 2. Application
        OrderApplicationService orderAppService = new OrderApplicationServiceImpl(
            orderRepo, paymentGateway, eventPublisher, new OrderAssembler()
        );

        // 3. API
        this.orderController = new OrderController(orderAppService);
    }

    public OrderController getOrderController() {
        return orderController;
    }
}
```

### Spring Boot Application（启动类）

```java
// composition/Application.java
@SpringBootApplication(scanBasePackages = {
    "com.example.composition.config",
    "com.example.infrastructure.data",
    "com.example.infrastructure.messaging"
})
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Application Runner

```java
// composition/runner/OrderDemoRunner.java
@Component
public class OrderDemoRunner implements CommandLineRunner {
    private final OrderApplicationService orderAppService;

    public OrderDemoRunner(OrderApplicationService orderAppService) {
        this.orderAppService = orderAppService;
    }

    @Override
    public void run(String... args) {
        // 创建订单
        CreateOrderCommand command = new CreateOrderCommand();
        command.setCustomerId("CUST-001");
        // ... set items
        OrderDTO order = orderAppService.createOrder(command);
        System.out.println("订单创建成功: " + order.getOrderId());
    }
}
```

### Maven 模块依赖配置

```xml
<!-- composition/pom.xml -->
<project>
    <artifactId>order-composition</artifactId>
    <dependencies>
        <!-- composition 依赖所有模块 -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>order-api</artifactId>
        </dependency>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>order-infrastructure</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
    </dependencies>
</project>
```

### 模块依赖关系图

```
core (domain + application interfaces)
  ↑                   ↑
api ───→ composition ←─── infrastructure
              ↑
         spring-boot start
```

## 规范检查清单

- [ ] DI 配置集中在 composition 模块
- [ ] Domain 层无任何 DI 注解
- [ ] Infrastructure 层的 `@Repository` 仅标记实现类
- [ ] API 层的 `@RestController` 仅定义端点
- [ ] 构造器注入（非字段注入）
- [ ] 无循环依赖
