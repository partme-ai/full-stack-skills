# Microservices Structure Example

## Overview

Microservices architecture is suitable for large platforms with multiple business domains and team size of 50+ people.

## Project Configuration

- **groupId**: `io.ddd4j.base`
- **artifactId**: `ecommerce-platform`
- **version**: `1.0.0-SNAPSHOT`
- **parentVersion**: `2023.0.x.20251205-SNAPSHOT` (Spring Boot 3.3.x)
- **packageBase**: `io.ddd4j.ecommerce`
- **architecture**: DDD Classic Layered Architecture

## Directory Structure

```
ecommerce-platform/                                 # 电商平台根目录
├── pom.xml                                         # 父POM
├── README.md
├── .gitignore
├── LICENSE
├── mvnw
├── mvnw.cmd
│
├── platform-common/                               # 平台通用模块
│   ├── pom.xml
│   └── src/main/java/io/ddd4j/ecommerce/common/
│       ├── kernel/
│       │   ├── AggregateRoot.java
│       │   └── ValueObject.java
│       ├── util/
│       └── exception/
│
├── services/                                      # 微服务目录
│   │
│   ├── user-service/                               # 用户服务
│   │   ├── pom.xml                                # 服务父POM
│   │   │
│   │   ├── user-service-api/                      # API模块
│   │   │   ├── pom.xml
│   │   │   └── src/main/java/io/ddd4j/ecommerce/user/api/
│   │   │       ├── package-info.java
│   │   │       └── UserService.java
│   │   │
│   │   ├── user-service-domain/                   # 领域模块
│   │   │   ├── pom.xml
│   │   │   └── src/main/java/io/ddd4j/ecommerce/user/domain/
│   │   │       ├── package-info.java
│   │   │       ├── model/
│   │   │       ├── service/
│   │   │       └── repository/
│   │   │
│   │   ├── user-service-application/             # 应用模块
│   │   │   ├── pom.xml
│   │   │   └── src/main/java/io/ddd4j/ecommerce/user/application/
│   │   │       ├── package-info.java
│   │   │       ├── service/
│   │   │       ├── command/
│   │   │       └── query/
│   │   │
│   │   ├── user-service-infrastructure/          # 基础设施模块
│   │   │   ├── pom.xml
│   │   │   └── src/main/java/io/ddd4j/ecommerce/user/infrastructure/
│   │   │       ├── package-info.java
│   │   │       ├── persistence/
│   │   │       └── external/
│   │   │
│   │   ├── user-service-interfaces/              # 接口模块
│   │   │   ├── pom.xml
│   │   │   └── src/main/java/io/ddd4j/ecommerce/user/interfaces/
│   │   │       ├── package-info.java
│   │   │       └── web/
│   │   │           └── controller/
│   │   │
│   │   └── user-service-start/                   # 启动模块
│   │       ├── pom.xml
│   │       └── src/main/java/io/ddd4j/ecommerce/user/
│   │           ├── UserApplication.java           # @SpringBootApplication
│   │           └── package-info.java
│   │
│   ├── order-service/                            # 订单服务
│   │   ├── pom.xml
│   │   ├── order-service-api/
│   │   ├── order-service-domain/
│   │   ├── order-service-application/
│   │   ├── order-service-infrastructure/
│   │   ├── order-service-interfaces/
│   │   └── order-service-start/
│   │
│   ├── product-service/                          # 商品服务
│   │   ├── pom.xml
│   │   ├── product-service-api/
│   │   ├── product-service-domain/
│   │   ├── product-service-application/
│   │   ├── product-service-infrastructure/
│   │   ├── product-service-interfaces/
│   │   └── product-service-start/
│   │
│   └── payment-service/                          # 支付服务
│       ├── pom.xml
│       ├── payment-service-api/
│       ├── payment-service-domain/
│       ├── payment-service-application/
│       ├── payment-service-infrastructure/
│       ├── payment-service-interfaces/
│       └── payment-service-start/
│
├── gateway/                                       # 网关服务
│   ├── pom.xml
│   └── gateway-start/
│       └── src/main/java/io/ddd4j/ecommerce/gateway/
│           ├── GatewayApplication.java
│           └── package-info.java
│
└── docs/
    └── architecture.md
```

## Parent pom.xml Example

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
    <artifactId>ecommerce-platform</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>ecommerce-platform</name>
    <description>E-commerce Platform - Microservices Architecture</description>

    <modules>
        <module>platform-common</module>
        <module>services</module>
        <module>gateway</module>
    </modules>

    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
</project>
```

## Service pom.xml Example (user-service)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>io.ddd4j.base</groupId>
        <artifactId>ecommerce-platform</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>

    <artifactId>user-service</artifactId>
    <packaging>pom</packaging>

    <name>user-service</name>
    <description>User Service - Microservice</description>

    <modules>
        <module>user-service-api</module>
        <module>user-service-domain</module>
        <module>user-service-application</module>
        <module>user-service-infrastructure</module>
        <module>user-service-interfaces</module>
        <module>user-service-start</module>
    </modules>
</project>
```

## Service Start Module pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>io.ddd4j.base</groupId>
        <artifactId>user-service</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>

    <artifactId>user-service-start</artifactId>
    <packaging>jar</packaging>

    <name>user-service-start</name>
    <description>User Service Start Module</description>

    <dependencies>
        <dependency>
            <groupId>io.ddd4j.base</groupId>
            <artifactId>user-service-interfaces</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>io.ddd4j.base</groupId>
            <artifactId>user-service-application</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>io.ddd4j.base</groupId>
            <artifactId>user-service-infrastructure</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>io.ddd4j.base</groupId>
            <artifactId>platform-common</artifactId>
            <version>${project.version}</version>
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

Each service follows the pattern: `{basePackage}.{serviceName}.{layerName}`

**User Service**:
- `io.ddd4j.ecommerce.user.api` - API layer
- `io.ddd4j.ecommerce.user.domain` - Domain layer
- `io.ddd4j.ecommerce.user.application` - Application layer
- `io.ddd4j.ecommerce.user.infrastructure` - Infrastructure layer
- `io.ddd4j.ecommerce.user.interfaces` - Interfaces layer

## Service Dependencies

```
user-service-start
    ↓ depends on
user-service-interfaces → user-service-application → user-service-domain ← user-service-infrastructure
    ↓                                                                              ↓
user-service-api                                                                  platform-common
```

## Key Features

1. **Independent Services**: Each service can be deployed independently
2. **Service Communication**: Through RPC (Dubbo/gRPC) and message queues (Kafka/RocketMQ)
3. **Shared Components**: `platform-common` provides common capabilities
4. **Gateway Entry**: `gateway` service handles routing, authentication, rate limiting
5. **Independent Databases**: Each service has its own database schema
6. **Modular Design**: Each service internally organized by DDD four-layer architecture

## Service Communication

```
Frontend → Gateway → Services (User, Order, Product, Payment)
                           ↓
                    Message Queue (Kafka/RocketMQ)
```

## Usage

This structure is ideal for:
- Large platforms
- Multiple business domains
- Team size 50+ people
- Independent service deployment
- Service scalability requirements

## Adding New Services

To add a new service (e.g., `inventory-service`):

1. Create service directory: `services/inventory-service/`
2. Create service parent `pom.xml`
3. Create sub-modules:
   - `inventory-service-api`
   - `inventory-service-domain`
   - `inventory-service-application`
   - `inventory-service-infrastructure`
   - `inventory-service-interfaces`
   - `inventory-service-start`
4. Add to parent `pom.xml` modules list
5. Follow package naming: `io.ddd4j.ecommerce.inventory.{layer}`
