# 微服务多模块 — DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 15-40 人，每子域一个团队 |
| 业务复杂度 | 高，每服务内部复杂需多模块隔离 |
| 部署方式 | Docker/K8s，每个服务独立部署 |
| 技术栈 | Spring Boot + Spring Cloud + Kafka + MyBatis/JPA |
| 迁移起点 | 从单体多模块（08）按子域拆分，或微服务简单（09）加强内部隔离 |

**典型业务**：大型电商（订单/商品/支付/用户/物流各域重叠少），金融系统（账户/交易/风控/清算独立性强）。

## 目录树

```
ecommerce-platform/
├── pom.xml                                    # 根聚合 POM
│
├── order-service/                             # 订单微服务（多模块）
│   ├── pom.xml                                # 服务级 POM
│   ├── order-interface/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/interface/
│   │       ├── controller/
│   │       │   └── OrderController.java
│   │       ├── dto/
│   │       │   ├── request/
│   │       │   └── response/
│   │       └── converter/
│   │           └── OrderDtoConverter.java
│   ├── order-application/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/application/
│   │       ├── service/
│   │       │   └── OrderApplicationService.java
│   │       ├── command/
│   │       ├── query/
│   │       └── event/handler/
│   │           └── PaymentCompletedHandler.java
│   ├── order-domain/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/domain/
│   │       └── order/
│   │           ├── entity/
│   │           │   ├── Order.java
│   │           │   └── OrderItem.java
│   │           ├── valueobject/
│   │           │   ├── Money.java
│   │           │   ├── OrderStatus.java
│   │           │   └── Address.java
│   │           ├── service/
│   │           │   └── OrderDomainService.java
│   │           ├── repository/
│   │           │   └── OrderRepository.java
│   │           └── event/
│   │               ├── OrderPlacedEvent.java
│   │               └── OrderConfirmedEvent.java
│   ├── order-infrastructure/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/order/infrastructure/
│   │       ├── repository/
│   │       │   └── MyBatisOrderRepository.java
│   │       ├── persistence/
│   │       │   ├── OrderPO.java
│   │       │   └── OrderItemPO.java
│   │       ├── messaging/
│   │       │   ├── KafkaEventPublisher.java
│   │       │   └── KafkaEventSubscriber.java
│   │       ├── external/
│   │       │   ├── ProductServiceClient.java
│   │       │   └── PaymentServiceClient.java
│   │       └── config/
│   │           └── OrderInfraConfig.java
│   └── order-bootstrap/                       # 服务启动模块
│       ├── pom.xml
│       └── src/main/java/com/example/order/
│           └── OrderServiceApplication.java
│
├── product-service/                           # 商品微服务（多模块）
│   ├── pom.xml
│   ├── product-interface/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/interface/
│   │       ├── controller/
│   │       │   └── ProductController.java
│   │       ├── dto/
│   │       └── converter/
│   ├── product-application/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/application/
│   │       ├── service/
│   │       │   └── ProductApplicationService.java
│   │       ├── command/
│   │       ├── query/
│   │       └── event/handler/
│   │           └── OrderPlacedHandler.java
│   ├── product-domain/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/domain/
│   │       └── product/
│   │           ├── entity/
│   │           │   ├── Product.java
│   │           │   └── Category.java
│   │           ├── valueobject/
│   │           │   ├── Price.java
│   │           │   ├── Sku.java
│   │           │   └── Stock.java
│   │           ├── service/
│   │           │   └── InventoryDomainService.java
│   │           ├── repository/
│   │           │   └── ProductRepository.java
│   │           └── event/
│   │               └── InventoryDeductedEvent.java
│   ├── product-infrastructure/
│   │   ├── pom.xml
│   │   └── src/main/java/com/example/product/infrastructure/
│   │       ├── repository/
│   │       │   └── MyBatisProductRepository.java
│   │       ├── persistence/
│   │       │   ├── ProductPO.java
│   │       │   └── CategoryPO.java
│   │       ├── messaging/
│   │       │   ├── KafkaEventPublisher.java
│   │       │   └── KafkaEventSubscriber.java
│   │       └── config/
│   │           └── ProductInfraConfig.java
│   └── product-bootstrap/
│       ├── pom.xml
│       └── src/main/java/com/example/product/
│           └── ProductServiceApplication.java
│
├── payment-service/                           # 支付微服务（多模块）
│   ├── pom.xml
│   ├── payment-interface/
│   ├── payment-application/
│   ├── payment-domain/
│   ├── payment-infrastructure/
│   └── payment-bootstrap/
│
└── shared-events/                             # 共享事件定义（类型 Schema）
    ├── pom.xml
    └── src/main/java/com/example/shared/
        ├── OrderPlacedEvent.java
        ├── OrderConfirmedEvent.java
        ├── InventoryDeductedEvent.java
        └── PaymentCompletedEvent.java
```

## 包结构

```
com.example.order.{layer}     — 订单服务四层
com.example.product.{layer}   — 商品服务四层
com.example.payment.{layer}   — 支付服务四层
com.example.shared            — 共享事件 Schema
```

## 模块依赖

### 服务级 POM（order-service/pom.xml）

```xml
<groupId>com.example</groupId>
<artifactId>order-service</artifactId>
<version>1.0.0</version>
<packaging>pom</packaging>

<modules>
    <module>order-interface</module>
    <module>order-application</module>
    <module>order-domain</module>
    <module>order-infrastructure</module>
    <module>order-bootstrap</module>
</modules>
```

### order-interface/pom.xml

```xml
<artifactId>order-interface</artifactId>
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-application</artifactId>
    </dependency>
</dependencies>
```

### order-application/pom.xml

```xml
<artifactId>order-application</artifactId>
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-domain</artifactId>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>shared-events</artifactId>
    </dependency>
</dependencies>
```

### order-domain/pom.xml

```xml
<artifactId>order-domain</artifactId>
<dependencies>
    <!-- 零框架依赖，仅 JDK -->
</dependencies>
```

### order-infrastructure/pom.xml

```xml
<artifactId>order-infrastructure</artifactId>
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-domain</artifactId>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>shared-events</artifactId>
    </dependency>
    <!-- 技术依赖 -->
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
    </dependency>
</dependencies>
```

### order-bootstrap/pom.xml

```xml
<artifactId>order-bootstrap</artifactId>
<dependencies>
    <dependency><groupId>com.example</groupId><artifactId>order-interface</artifactId></dependency>
    <dependency><groupId>com.example</groupId><artifactId>order-application</artifactId></dependency>
    <dependency><groupId>com.example</groupId><artifactId>order-domain</artifactId></dependency>
    <dependency><groupId>com.example</groupId><artifactId>order-infrastructure</artifactId></dependency>
</dependencies>
```

## 依赖关系图

```
order-bootstrap
  ├── order-interface ──▶ order-application
  ├── order-application ──▶ order-domain
  ├── order-domain       (零依赖)
  └── order-infrastructure ──▶ order-domain

product-bootstrap
  ├── product-interface ──▶ product-application
  ├── product-application ──▶ product-domain
  ├── product-domain       (零依赖)
  └── product-infrastructure ──▶ product-domain

shared-events  ◀── 所有 application 和 infrastructure 模块依赖
```

## 关键设计要点

| 要点 | 说明 |
|------|------|
| 双层模块化 | 服务级 Maven 模块 + 服务内四层 Maven 模块 |
| Domain 物理隔离 | 每服务 Domain 独立 jar，编译期保证零框架依赖 |
| 独立部署 | 每个 bootstrap 模块生成独立可执行 JAR |
| 共享事件 | shared-events 仅定义事件 POJO，不包含行为 |
| 构建效率 | 修改单服务只需 build 该服务及其子模块 |
| 团队分工 | 每个服务团队独立维护自己的 4 个子模块 |

## 优点与局限

| 优点 | 局限 |
|------|------|
| 编译期强制分层约束 | Maven 模块数量多，pom.xml 维护成本高 |
| 每层可独立测试和发布 | 新服务创建需复制 5 个 pom.xml |
| 团队间物理隔离 | 构建时间随模块增多变长 |
| 清晰的服务边界 | 共享事件 Schema 需要多服务协调变更 |

## 演进路径

```
微服务多模块 → 微服务复杂多模块（12，共享 Kernel）
```
