# 单体多模块 — DDD 分层示例

## 适用场景

| 维度 | 描述 |
|------|------|
| 团队规模 | 8-20 人，有模块化经验 |
| 业务复杂度 | 中高，2-5 个聚合根 |
| 部署方式 | 单体 Spring Boot JAR，多 Maven 模块编译 |
| 技术栈 | Spring Boot + MyBatis/JPA + Maven 多模块 |
| 迁移起点 | 从单模块四层（06/07）拆分 |

**典型业务**：需要物理模块隔离的中型项目，团队多人并行开发。

## 目录树

```
order-system/
├── pom.xml                                  # 父 POM（dependencyManagement）
│
├── order-interface/                         # 用户接口层模块
│   ├── pom.xml
│   └── src/main/java/com/example/order/interface/
│       ├── controller/
│       │   └── OrderController.java
│       ├── dto/
│       │   ├── request/
│       │   │   ├── CreateOrderRequest.java
│       │   │   └── UpdateOrderRequest.java
│       │   └── response/
│       │       └── OrderResponse.java
│       └── converter/
│           └── OrderDtoConverter.java
│
├── order-application/                       # 应用层模块
│   ├── pom.xml
│   └── src/main/java/com/example/order/application/
│       ├── service/
│       │   └── OrderApplicationService.java
│       ├── command/
│       │   ├── CreateOrderCommand.java
│       │   └── UpdateOrderCommand.java
│       ├── query/
│       │   └── OrderDetailQuery.java
│       └── assembler/
│           └── OrderAssembler.java
│
├── order-domain/                            # 领域层模块 ★
│   ├── pom.xml
│   └── src/main/java/com/example/order/domain/
│       ├── order/
│       │   ├── entity/
│       │   │   ├── Order.java
│       │   │   └── OrderItem.java
│       │   ├── valueobject/
│       │   │   ├── Money.java
│       │   │   ├── OrderStatus.java
│       │   │   └── Address.java
│       │   ├── service/
│       │   │   └── OrderDomainService.java
│       │   ├── repository/
│       │   │   └── OrderRepository.java     # 仓储接口（只定义）
│       │   └── event/
│       │       └── OrderPlacedEvent.java
│       └── shared/
│           ├── AggregateRoot.java
│           └── DomainEvent.java
│
└── order-infrastructure/                    # 基础设施层模块
    ├── pom.xml
    └── src/main/java/com/example/order/infrastructure/
        ├── repository/
        │   └── MyBatisOrderRepository.java  # 仓储实现
        ├── persistence/
        │   ├── OrderPO.java
        │   └── OrderItemPO.java
        ├── converter/
        │   └── OrderPersistenceConverter.java  # PO ↔ DO
        └── config/
            └── RepositoryConfig.java
```

## 包结构

```
com.example.order
├── order-interface/       com.example.order.interface
├── order-application/     com.example.order.application
├── order-domain/          com.example.order.domain
└── order-infrastructure/  com.example.order.infrastructure
```

每个模块独立基础包名：`com.example.order.{layer}`

## 模块依赖

### 父 POM（order-system/pom.xml）

```xml
<groupId>com.example</groupId>
<artifactId>order-system</artifactId>
<version>1.0.0</version>
<packaging>pom</packaging>

<modules>
    <module>order-interface</module>
    <module>order-application</module>
    <module>order-domain</module>
    <module>order-infrastructure</module>
</modules>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>3.2.5</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### order-interface/pom.xml

```xml
<artifactId>order-interface</artifactId>
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-application</artifactId>
        <version>${project.version}</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
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
        <version>${project.version}</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
</dependencies>
```

### order-domain/pom.xml

```xml
<artifactId>order-domain</artifactId>
<dependencies>
    <!-- 零框架依赖，仅 JDK -->
    <!-- 可引入 javax.annotation 等标注库（非 Spring） -->
</dependencies>
```

### order-infrastructure/pom.xml

```xml
<artifactId>order-infrastructure</artifactId>
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>order-domain</artifactId>
        <version>${project.version}</version>
    </dependency>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
    </dependency>
</dependencies>
```

### 依赖关系图

```
order-interface
       ↓
order-application
       ↓
order-domain ← order-infrastructure
```

## 关键设计要点

| 要点 | 说明 |
|------|------|
| 物理隔离 | Maven 模块强制依赖方向，编译期阻止反向依赖 |
| Domain 纯净 | pom.xml 不含 Spring/JPA，可独立测试 |
| 运行组合 | Application 模块启动时同时依赖 interface + infra，运行时注入实现 |
| Infrastructure 独立 | 替换持久层只需改 infra 模块，不影响其他层 |
| 并行开发 | 不同模块可由不同开发者独立编译和测试 |

## 应用启动模块

通常主启动类放在 `order-interface` 或单独的 bootstrap 模块中：

```
order-bootstrap/
├── pom.xml
└── src/main/java/
    └── com/example/order/
        └── OrderApplication.java
```

`order-bootstrap/pom.xml` 同时依赖所有四个模块：

```xml
<dependencies>
    <dependency><groupId>com.example</groupId><artifactId>order-interface</artifactId></dependency>
    <dependency><groupId>com.example</groupId><artifactId>order-application</artifactId></dependency>
    <dependency><groupId>com.example</groupId><artifactId>order-domain</artifactId></dependency>
    <dependency><groupId>com.example</groupId><artifactId>order-infrastructure</artifactId></dependency>
</dependencies>
```

## 优点与局限

| 优点 | 局限 |
|------|------|
| Maven 强制依赖方向 | 模块数量增多，构建时间增加 |
| Domain 物理纯净 | 仍为单体部署，可伸缩性有限 |
| 可独立编译测试 | 多次 pom.xml 维护成本 |
| 清晰的团队分工边界 | 适合中小型项目，超大项目仍需微服务 |

## 演进路径

```
单体多模块 → 微服务简单（09）→ 微服务多模块（11）
```
