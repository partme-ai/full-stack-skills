---
name: spring-cloud-alibaba
description: Provides comprehensive guidance for Spring Cloud Alibaba including Nacos, Sentinel, RocketMQ, and Alibaba Cloud integration. Use when the user asks about Spring Cloud Alibaba, needs to use Alibaba Cloud services, implement service discovery with Nacos, or work with Spring Cloud Alibaba components.
---

# Spring Cloud Alibaba 开发指南

## 概述

Spring Cloud Alibaba 是阿里巴巴提供的微服务解决方案，提供了 Nacos（服务注册与配置）、Sentinel（流量控制）、RocketMQ（消息队列）、Seata（分布式事务）等组件。

## 核心组件

### 1. Nacos（服务注册与配置中心）

**Nacos Server 安装**：

```bash
# 下载 Nacos
wget https://github.com/alibaba/nacos/releases/download/2.2.0/nacos-server-2.2.0.tar.gz

# 解压并启动
tar -xzf nacos-server-2.2.0.tar.gz
cd nacos/bin
sh startup.sh -m standalone
```

**服务注册**：

```java
@SpringBootApplication
@EnableDiscoveryClient
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
  cloud:
    nacos:
      discovery:
        server-addr: localhost:8848
        namespace: dev
        group: DEFAULT_GROUP
```

**配置管理**：

```yaml
spring:
  cloud:
    nacos:
      config:
        server-addr: localhost:8848
        file-extension: yaml
        namespace: dev
        group: DEFAULT_GROUP
        shared-configs:
          - data-id: common-config.yaml
            group: DEFAULT_GROUP
            refresh: true
```

**动态配置刷新**：

```java
@RestController
@RefreshScope
public class ConfigController {
    @Value("${app.name:default}")
    private String appName;
    
    @GetMapping("/config")
    public String getConfig() {
        return appName;
    }
}
```

### 2. Sentinel（流量控制）

**依赖**：

```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>
```

**配置**：

```yaml
spring:
  cloud:
    sentinel:
      transport:
        dashboard: localhost:8080
        port: 8719
      datasource:
        flow:
          nacos:
            server-addr: localhost:8848
            dataId: ${spring.application.name}-flow-rules
            groupId: SENTINEL_GROUP
            rule-type: flow
```

**流量控制**：

```java
@Service
public class UserService {
    @SentinelResource(value = "getUser", blockHandler = "getUserBlockHandler")
    public User getUser(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    public User getUserBlockHandler(Long id, BlockException ex) {
        return new User(); // 降级处理
    }
}
```

**熔断降级**：

```java
@SentinelResource(
    value = "getUser",
    fallback = "getUserFallback",
    blockHandler = "getUserBlockHandler"
)
public User getUser(Long id) {
    // 业务逻辑
}

public User getUserFallback(Long id, Throwable ex) {
    // 降级处理
    return new User();
}
```

### 3. RocketMQ（消息队列）

**依赖**：

```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
</dependency>
```

**配置**：

```yaml
spring:
  cloud:
    stream:
      rocketmq:
        binder:
          name-server: localhost:9876
        bindings:
          output:
            producer:
              group: user-service-group
```

**消息发送**：

```java
@Service
public class UserService {
    private final RocketMQTemplate rocketMQTemplate;
    
    public UserService(RocketMQTemplate rocketMQTemplate) {
        this.rocketMQTemplate = rocketMQTemplate;
    }
    
    public void sendUserCreatedEvent(User user) {
        rocketMQTemplate.convertAndSend("user-topic", user);
    }
}
```

**消息接收**：

```java
@Component
@RocketMQMessageListener(
    topic = "user-topic",
    consumerGroup = "user-consumer-group"
)
public class UserEventListener implements RocketMQListener<User> {
    @Override
    public void onMessage(User user) {
        // 处理消息
        System.out.println("Received user: " + user.getName());
    }
}
```

### 4. Seata（分布式事务）

**依赖**：

```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
</dependency>
```

**配置**：

```yaml
spring:
  cloud:
    alibaba:
      seata:
        tx-service-group: my-tx-group
        enabled: true

seata:
  enabled: true
  application-id: ${spring.application.name}
  tx-service-group: my-tx-group
  config:
    type: nacos
    nacos:
      server-addr: localhost:8848
      namespace: ""
      group: SEATA_GROUP
  registry:
    type: nacos
    nacos:
      server-addr: localhost:8848
      namespace: ""
      group: SEATA_GROUP
```

**使用 @GlobalTransactional**：

```java
@Service
public class OrderService {
    @GlobalTransactional
    public void createOrder(Order order) {
        // 1. 创建订单
        orderRepository.save(order);
        
        // 2. 扣减库存
        productService.reduceStock(order.getProductId(), order.getQuantity());
        
        // 3. 扣减余额
        accountService.deductBalance(order.getUserId(), order.getAmount());
    }
}
```

### 5. Dubbo（RPC 框架）

**依赖**：

```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-dubbo</artifactId>
</dependency>
```

**配置**：

```yaml
spring:
  cloud:
    dubbo:
      application:
        name: user-service
      registry:
        address: nacos://localhost:8848
      protocol:
        name: dubbo
        port: 20880
```

**服务提供者**：

```java
@Service
@org.apache.dubbo.config.annotation.Service
public class UserServiceImpl implements UserService {
    public User getUser(Long id) {
        return userRepository.findById(id).orElseThrow();
    }
}
```

**服务消费者**：

```java
@Service
public class OrderService {
    @org.apache.dubbo.config.annotation.Reference
    private UserService userService;
    
    public Order createOrder(Long userId, Order order) {
        User user = userService.getUser(userId);
        // 创建订单逻辑
        return order;
    }
}
```

## 微服务架构示例

### 项目结构

```
microservices/
├── nacos-server/           # Nacos 服务
├── gateway/                # API 网关
├── user-service/           # 用户服务
├── order-service/          # 订单服务
└── product-service/        # 商品服务
```

### 配置示例

**统一配置管理**：

```yaml
# Nacos 配置中心
spring:
  cloud:
    nacos:
      config:
        server-addr: localhost:8848
        file-extension: yaml
        namespace: ${spring.profiles.active}
        group: DEFAULT_GROUP
        extension-configs:
          - data-id: common-datasource.yaml
            group: DEFAULT_GROUP
            refresh: true
          - data-id: common-redis.yaml
            group: DEFAULT_GROUP
            refresh: true
```

## 最佳实践

### 1. 服务注册

- 使用 Nacos 作为服务注册中心
- 配置合适的命名空间和分组
- 设置健康检查

### 2. 配置管理

- 使用 Nacos 配置中心统一管理
- 区分环境配置（dev、test、prod）
- 支持动态刷新

### 3. 流量控制

- 使用 Sentinel 进行流量控制
- 配置限流、熔断、降级规则
- 监控服务调用情况

### 4. 分布式事务

- 使用 Seata 处理分布式事务
- 合理使用 @GlobalTransactional
- 避免长事务

## 常用依赖

```xml
<!-- Nacos Discovery -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>

<!-- Nacos Config -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>

<!-- Sentinel -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
</dependency>

<!-- RocketMQ -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
</dependency>

<!-- Seata -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
</dependency>
```

## 示例 Prompt

- "如何使用 Spring Cloud Alibaba 构建微服务架构？"
- "Nacos 如何配置服务注册和配置管理？"
- "如何在 Spring Cloud Alibaba 中使用 Sentinel 进行流量控制？"
- "Spring Cloud Alibaba 中如何使用 Seata 处理分布式事务？"
- "如何配置 RocketMQ 消息队列？"
