# Multi-Module Monolith Structure Example

## Overview

Multi-module monolith is suitable for medium to large applications with multiple business domains and team size of 15-50 people.

## Project Configuration

- **groupId**: `io.ddd4j.base`
- **artifactId**: `ddd4j-douyin`
- **version**: `1.0.0-SNAPSHOT`
- **parentVersion**: `2023.0.x.20251205-SNAPSHOT` (Spring Boot 3.3.x)
- **packageBase**: `io.ddd4j.douyin`
- **architecture**: DDD Classic Layered Architecture

## Directory Structure

```
ddd4j-douyin/
├── pom.xml                                          # 父POM
├── README.md
├── .gitignore
├── LICENSE
├── mvnw
├── mvnw.cmd
│
├── ddd4j-douyin-bom/                                # BOM依赖管理
│   ├── pom.xml
│   └── src/main/java/io/ddd4j/douyin/bom/
│       └── package-info.java
│
├── ddd4j-douyin-dependencies/                      # 公共依赖
│   ├── pom.xml
│   └── src/main/java/io/ddd4j/douyin/dependencies/
│       └── package-info.java
│
├── ddd4j-douyin-api/                               # API业务模块
│   ├── pom.xml
│   ├── ddd4j-douyin-api-adapter/                  # 适配器层
│   │   ├── pom.xml
│   │   └── src/main/java/io/ddd4j/douyin/api/adapter/
│   │       ├── package-info.java
│   │       ├── web/
│   │       │   ├── controller/
│   │       │   │   └── ApiController.java
│   │       │   └── dto/
│   │       └── rpc/
│   │
│   ├── ddd4j-douyin-api-client/                   # 客户端模块
│   │   ├── pom.xml
│   │   └── src/main/java/io/ddd4j/douyin/api/client/
│   │       ├── package-info.java
│   │       └── ApiClient.java
│   │
│   ├── ddd4j-douyin-api-app/                      # 应用层
│   │   ├── pom.xml
│   │   └── src/main/java/io/ddd4j/douyin/api/app/
│   │       ├── package-info.java
│   │       ├── service/
│   │       │   └── ApiApplicationService.java
│   │       ├── command/
│   │       └── query/
│   │
│   ├── ddd4j-douyin-api-domain/                   # 领域层
│   │   ├── pom.xml
│   │   └── src/main/java/io/ddd4j/douyin/api/domain/
│   │       ├── package-info.java
│   │       ├── model/
│   │       │   ├── aggregate/
│   │       │   ├── valueobject/
│   │       │   └── event/
│   │       ├── service/
│   │       └── repository/
│   │
│   └── ddd4j-douyin-api-infrastructure/            # 基础设施层
│       ├── pom.xml
│       └── src/main/java/io/ddd4j/douyin/api/infrastructure/
│           ├── package-info.java
│           ├── persistence/
│           ├── messaging/
│           └── external/
│
├── ddd4j-douyin-common/                           # 通用模块
│   ├── pom.xml
│   ├── ddd4j-douyin-common-domain/               # 通用领域
│   │   ├── pom.xml
│   │   └── src/main/java/io/ddd4j/douyin/common/domain/
│   │       ├── package-info.java
│   │       └── model/
│   │
│   └── ddd4j-douyin-common-infrastructure/       # 通用基础设施
│       ├── pom.xml
│       └── src/main/java/io/ddd4j/douyin/common/infrastructure/
│           ├── package-info.java
│           └── config/
│
└── ddd4j-douyin-start/                            # 启动模块
    ├── pom.xml
    └── src/main/java/io/ddd4j/douyin/
        ├── DouyinApplication.java                  # @SpringBootApplication
        └── package-info.java
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
    <artifactId>ddd4j-douyin</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>ddd4j-douyin</name>
    <description>Douyin Platform - Multi-Module Monolith</description>

    <modules>
        <module>ddd4j-douyin-bom</module>
        <module>ddd4j-douyin-dependencies</module>
        <module>ddd4j-douyin-api</module>
        <module>ddd4j-douyin-common</module>
        <module>ddd4j-douyin-start</module>
    </modules>

    <properties>
        <java.version>17</java.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
</project>
```

## Module pom.xml Example (api-domain)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>io.ddd4j.base</groupId>
        <artifactId>ddd4j-douyin</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>

    <artifactId>ddd4j-douyin-api-domain</artifactId>
    <packaging>jar</packaging>

    <name>ddd4j-douyin-api-domain</name>
    <description>API Domain Layer</description>

    <dependencies>
        <!-- Common Domain -->
        <dependency>
            <groupId>io.ddd4j.base</groupId>
            <artifactId>ddd4j-douyin-common-domain</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>
</project>
```

## Package Structure

Each module follows the pattern: `{basePackage}.{moduleName}.{layerName}`

**API Module**:
- `io.ddd4j.douyin.api.adapter` - Adapter layer
- `io.ddd4j.douyin.api.app` - Application layer
- `io.ddd4j.douyin.api.domain` - Domain layer
- `io.ddd4j.douyin.api.infrastructure` - Infrastructure layer

**Common Module**:
- `io.ddd4j.douyin.common.domain` - Common domain
- `io.ddd4j.douyin.common.infrastructure` - Common infrastructure

## Module Dependencies

```
ddd4j-douyin-start
    ↓ depends on
ddd4j-douyin-api-adapter → ddd4j-douyin-api-app → ddd4j-douyin-api-domain ← ddd4j-douyin-api-infrastructure
    ↓                                                                              ↓
ddd4j-douyin-common-domain ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ddd4j-douyin-common-infrastructure
    ↓
ddd4j-douyin-bom
    ↓
ddd4j-douyin-dependencies
```

## Key Features

1. **Multiple Maven Modules**: Each business domain has its own module
2. **Layer Separation**: Each module contains complete DDD layers
3. **Shared Common Module**: Reusable domain and infrastructure components
4. **BOM Management**: Centralized dependency version management
5. **Dependency Control**: Clear module dependencies

## Usage

This structure is ideal for:
- Medium to large applications
- Multiple business domains
- Team size 15-50 people
- Need for module isolation
- Shared component reuse

## Adding New Business Modules

To add a new business module (e.g., `ddd4j-douyin-order`):

1. Create module directory: `ddd4j-douyin-order/`
2. Create sub-modules:
   - `ddd4j-douyin-order-adapter`
   - `ddd4j-douyin-order-app`
   - `ddd4j-douyin-order-domain`
   - `ddd4j-douyin-order-infrastructure`
3. Add to parent `pom.xml` modules list
4. Follow package naming: `io.ddd4j.douyin.order.{layer}`
