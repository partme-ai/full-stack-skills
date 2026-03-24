---
name: spring-cloud
description: Provides comprehensive guidance for Spring Cloud microservices including service discovery, configuration management, load balancing, circuit breakers, API gateways, and distributed tracing. Use when the user asks about Spring Cloud, needs to build microservices, implement service discovery, or work with Spring Cloud components.
---

# Spring Cloud 微服务开发指南

## 概述

Spring Cloud 是一套完整的微服务解决方案，提供了服务注册与发现、配置管理、网关、负载均衡、熔断器等组件。

## 核心组件

### 1. 服务注册与发现（Eureka）

**Eureka Server**：

```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServerApplication.class, args);
    }
}
```

**application.yml**：

```yaml
server:
  port: 8761

eureka:
  instance:
    hostname: localhost
  client:
    register-with-eureka: false
    fetch-registry: false
    service-url:
      defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
```

**Eureka Client**：

```java
@SpringBootApplication
@EnableEurekaClient
public class UserServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }
}
```

**application.yml**：

```yaml
spring:
  application:
    name: user-service

eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
```

### 2. 配置中心（Config Server）

**Config Server**：

```java
@SpringBootApplication
@EnableConfigServer
public class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}
```

**application.yml**：

```yaml
server:
  port: 8888

spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/example/config-repo
          search-paths: '{application}'
```

**Config Client**：

```yaml
spring:
  application:
    name: user-service
  cloud:
    config:
      uri: http://localhost:8888
      name: user-service
      profile: dev
```

### 3. API 网关（Gateway）

**Gateway 配置**：

```java
@SpringBootApplication
public class GatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }
}
```

**application.yml**：

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - StripPrefix=1
        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - StripPrefix=1
```

**路由配置类**：

```java
@Configuration
public class GatewayConfig {
    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("user-service", r -> r
                .path("/api/users/**")
                .uri("lb://user-service"))
            .route("order-service", r -> r
                .path("/api/orders/**")
                .uri("lb://order-service"))
            .build();
    }
}
```

### 4. 负载均衡（LoadBalancer）

**使用 RestTemplate**：

```java
@Configuration
public class RestTemplateConfig {
    @Bean
    @LoadBalanced
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

**使用 WebClient**：

```java
@Configuration
public class WebClientConfig {
    @Bean
    @LoadBalanced
    public WebClient.Builder webClientBuilder() {
        return WebClient.builder();
    }
}
```

**服务调用**：

```java
@Service
public class OrderService {
    private final RestTemplate restTemplate;
    
    public OrderService(@LoadBalanced RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }
    
    public User getUser(Long userId) {
        return restTemplate.getForObject(
            "http://user-service/api/users/{id}",
            User.class,
            userId
        );
    }
}
```

### 5. 熔断器（Circuit Breaker）

**依赖**：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
</dependency>
```

**配置**：

```yaml
resilience4j:
  circuitbreaker:
    instances:
      userService:
        registerHealthIndicator: true
        slidingWindowSize: 10
        failureRateThreshold: 50
        waitDurationInOpenState: 10000
```

**使用**：

```java
@Service
public class OrderService {
    private final CircuitBreaker circuitBreaker;
    private final RestTemplate restTemplate;
    
    public OrderService(
        CircuitBreakerRegistry circuitBreakerRegistry,
        RestTemplate restTemplate
    ) {
        this.circuitBreaker = circuitBreakerRegistry.circuitBreaker("userService");
        this.restTemplate = restTemplate;
    }
    
    public User getUser(Long userId) {
        return circuitBreaker.executeSupplier(() ->
            restTemplate.getForObject(
                "http://user-service/api/users/{id}",
                User.class,
                userId
            )
        );
    }
}
```

### 6. 服务调用（Feign）

**依赖**：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```

**启用 Feign**：

```java
@SpringBootApplication
@EnableFeignClients
public class OrderServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderServiceApplication.class, args);
    }
}
```

**定义 Feign Client**：

```java
@FeignClient(name = "user-service")
public interface UserServiceClient {
    @GetMapping("/api/users/{id}")
    User getUserById(@PathVariable Long id);
    
    @PostMapping("/api/users")
    User createUser(@RequestBody User user);
}
```

**使用**：

```java
@Service
public class OrderService {
    private final UserServiceClient userServiceClient;
    
    public OrderService(UserServiceClient userServiceClient) {
        this.userServiceClient = userServiceClient;
    }
    
    public Order createOrder(Long userId, Order order) {
        User user = userServiceClient.getUserById(userId);
        // 创建订单逻辑
        return order;
    }
}
```

### 7. 分布式追踪（Sleuth）

**依赖**：

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**配置**：

```yaml
spring:
  sleuth:
    sampler:
      probability: 1.0
```

## 微服务架构示例

### 项目结构

```
microservices/
├── eureka-server/          # 服务注册中心
├── config-server/          # 配置中心
├── gateway/                # API 网关
├── user-service/           # 用户服务
├── order-service/          # 订单服务
└── product-service/        # 商品服务
```

### 服务间调用

**同步调用（Feign）**：

```java
@FeignClient(name = "user-service")
public interface UserServiceClient {
    @GetMapping("/api/users/{id}")
    User getUserById(@PathVariable Long id);
}
```

**异步调用（消息队列）**：

```java
@Service
public class OrderService {
    private final RabbitTemplate rabbitTemplate;
    
    public void publishOrderEvent(Order order) {
        rabbitTemplate.convertAndSend("order.exchange", "order.created", order);
    }
}
```

## 最佳实践

### 1. 服务拆分

- 按业务领域拆分
- 保持服务独立性
- 避免服务间强耦合

### 2. 配置管理

- 使用配置中心统一管理
- 区分环境配置
- 支持动态刷新

### 3. 服务治理

- 使用网关统一入口
- 实现服务熔断和降级
- 监控服务健康状态

### 4. 数据管理

- 每个服务独立数据库
- 使用 Saga 模式处理分布式事务
- 避免跨服务直接访问数据库

## 常用依赖

```xml
<!-- Eureka Client -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

<!-- Gateway -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>
</dependency>

<!-- Feign -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>

<!-- Circuit Breaker -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-circuitbreaker-resilience4j</artifactId>
</dependency>
```

## 示例 Prompt

- "如何使用 Spring Cloud 构建微服务架构？"
- "Spring Cloud Gateway 如何配置路由？"
- "如何在 Spring Cloud 中使用 Feign 进行服务调用？"
- "Spring Cloud 中如何实现服务熔断？"
- "如何配置 Spring Cloud Config 配置中心？"
