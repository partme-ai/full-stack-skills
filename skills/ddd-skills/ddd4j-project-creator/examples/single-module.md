# Single-Module Monolith Structure Example

## Overview

Single-module monolith is suitable for small to medium applications with a single business domain and team size of 5-15 people.

## Project Configuration

- **groupId**: `io.ddd4j.base`
- **artifactId**: `ddd4j-order`
- **version**: `1.0.0-SNAPSHOT`
- **parentVersion**: `2023.0.x.20251205-SNAPSHOT` (Spring Boot 3.3.x)
- **packageBase**: `io.ddd4j.order`
- **architecture**: DDD Classic Layered Architecture

## Directory Structure

```
ddd4j-order/
├── pom.xml
├── README.md
├── .gitignore
├── LICENSE
├── mvnw
├── mvnw.cmd
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── io/ddd4j/order/
│   │   │       ├── OrderApplication.java              # @SpringBootApplication
│   │   │       │
│   │   │       ├── interfaces/                        # 接口层
│   │   │       │   ├── web/
│   │   │       │   │   ├── controller/
│   │   │       │   │   │   ├── OrderController.java
│   │   │       │   │   │   └── CustomerController.java
│   │   │       │   │   ├── dto/
│   │   │       │   │   │   ├── request/
│   │   │       │   │   │   │   ├── PlaceOrderRequest.java
│   │   │       │   │   │   │   └── PayOrderRequest.java
│   │   │       │   │   │   └── response/
│   │   │       │   │   │       ├── OrderResponse.java
│   │   │       │   │   │       └── ApiResponse.java
│   │   │       │   │   └── advice/
│   │   │       │   │       └── GlobalExceptionHandler.java
│   │   │       │   │
│   │   │       │   └── rpc/                           # RPC接口（可选）
│   │   │       │       ├── OrderRpcProvider.java
│   │   │       │       └── PaymentRpcConsumer.java
│   │   │       │
│   │   │       ├── application/                       # 应用层
│   │   │       │   ├── service/
│   │   │       │   │   ├── OrderApplicationService.java
│   │   │       │   │   └── CustomerApplicationService.java
│   │   │       │   ├── command/
│   │   │       │   │   ├── PlaceOrderCommand.java
│   │   │       │   │   └── PayOrderCommand.java
│   │   │       │   ├── query/
│   │   │       │   │   ├── GetOrderQuery.java
│   │   │       │   │   └── OrderListQuery.java
│   │   │       │   └── eventhandler/
│   │   │       │       └── OrderPlacedEventHandler.java
│   │   │       │
│   │   │       ├── domain/                            # 领域层
│   │   │       │   ├── model/
│   │   │       │   │   ├── aggregate/
│   │   │       │   │   │   ├── order/
│   │   │       │   │   │   │   ├── Order.java         # 聚合根
│   │   │       │   │   │   │   └── OrderItem.java     # 实体
│   │   │       │   │   │   └── customer/
│   │   │       │   │   │       └── Customer.java      # 聚合根
│   │   │       │   │   ├── valueobject/
│   │   │       │   │   │   ├── Money.java
│   │   │       │   │   │   ├── Email.java
│   │   │       │   │   │   └── Address.java
│   │   │       │   │   └── event/
│   │   │       │   │       ├── OrderPlacedEvent.java
│   │   │       │   │       └── OrderPaidEvent.java
│   │   │       │   ├── service/
│   │   │       │   │   └── OrderDomainService.java
│   │   │       │   └── repository/
│   │   │       │       ├── OrderRepository.java       # 仓储接口
│   │   │       │       └── CustomerRepository.java
│   │   │       │
│   │   │       └── infrastructure/                    # 基础设施层
│   │   │           ├── persistence/
│   │   │           │   ├── repository/
│   │   │           │   │   ├── JpaOrderRepository.java
│   │   │           │   │   └── JpaCustomerRepository.java
│   │   │           │   ├── entity/
│   │   │           │   │   ├── OrderEntity.java
│   │   │           │   │   └── CustomerEntity.java
│   │   │           │   └── mapper/
│   │   │           │       └── OrderMapper.java
│   │   │           ├── messaging/
│   │   │           │   └── KafkaEventPublisher.java
│   │   │           ├── external/
│   │   │           │   └── payment/
│   │   │           │       └── AlipayPaymentService.java
│   │   │           └── config/
│   │   │               ├── PersistenceConfig.java
│   │   │               └── MessagingConfig.java
│   │   │
│   │   └── resources/
│   │       ├── application.yml
│   │       ├── application-dev.yml
│   │       └── application-prod.yml
│   │
│   └── test/
│       ├── java/
│       │   └── io/ddd4j/order/
│       │       ├── unit/
│       │       │   ├── domain/
│       │       │   │   └── OrderTest.java
│       │       │   └── application/
│       │       │       └── OrderApplicationServiceTest.java
│       │       └── integration/
│       │           └── OrderIntegrationTest.java
│       └── resources/
│           └── application-test.yml
│
└── docs/
    └── architecture.md
```

## pom.xml Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>io.ddd4j.base</groupId>
        <artifactId>ddd4j-cloud-parent</artifactId>
        <version>2023.0.x.20251205-SNAPSHOT</version>
        <relativePath/>
    </parent>

    <groupId>io.ddd4j.base</groupId>
    <artifactId>ddd4j-order</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>ddd4j-order</name>
    <description>Order Management System - Single Module Monolith</description>

    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Spring Boot Starters -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <!-- Test -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

## Package Structure

All packages follow the pattern: `{basePackage}.{layer}`

- `io.ddd4j.order.interfaces` - Interface layer
- `io.ddd4j.order.application` - Application layer
- `io.ddd4j.order.domain` - Domain layer
- `io.ddd4j.order.infrastructure` - Infrastructure layer

## Key Features

1. **Single Maven Module**: All layers in one module
2. **Clear Layer Separation**: Interfaces → Application → Domain ← Infrastructure
3. **Complete Structure**: Includes all required directories and files
4. **Test Structure**: Unit and integration test directories
5. **Configuration**: Environment-specific configuration files

## Usage

This structure is ideal for:
- Small to medium applications
- Single business domain
- Team size 5-15 people
- Quick development and deployment
- Simple maintenance
