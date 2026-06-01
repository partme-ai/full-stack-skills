# COLA v5 项目脚手架

## Maven Archetype 快速创建

```bash
mvn archetype:generate \
  -DarchetypeGroupId=com.alibaba.cola \
  -DarchetypeArtifactId=cola-archetype-web \
  -DarchetypeVersion=5.0.0 \
  -DgroupId=com.yourcompany \
  -DartifactId=your-project \
  -Dversion=1.0.0-SNAPSHOT
```

## 手动搭建（推荐生产使用）

### 多模块 Maven 配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.yourcompany</groupId>
    <artifactId>your-project</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>start</module>
        <module>adapter</module>
        <module>app</module>
        <module>domain</module>
        <module>infrastructure</module>
        <module>common</module>
    </modules>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
    </parent>

    <properties>
        <java.version>17</java.version>
        <cola.version>5.0.0</cola.version>
        <mybatis.version>3.0.3</mybatis.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>com.alibaba.cola</groupId>
                <artifactId>cola-component-dto</artifactId>
                <version>${cola.version}</version>
            </dependency>
            <dependency>
                <groupId>com.alibaba.cola</groupId>
                <artifactId>cola-component-domain-starter</artifactId>
                <version>${cola.version}</version>
            </dependency>
            <dependency>
                <groupId>com.alibaba.cola</groupId>
                <artifactId>cola-component-catchlog-starter</artifactId>
                <version>${cola.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
```

### 各模块依赖

| 模块 | 依赖 | 说明 |
|------|------|------|
| start | adapter, common | 启动模块，依赖所有非 domain 模块 |
| adapter | app, domain | 适配层，可调用应用层和领域层 |
| app | domain, infrastructure | 应用层，编排领域层 + 基础设施 |
| domain | (none) | 领域层，纯 POJO，零框架依赖 |
| infrastructure | domain | 基础设施实现领域层接口 |
| common | (none) | 通用工具和常量 |

### Gradle 版本

```groovy
// settings.gradle
rootProject.name = 'your-project'
include 'start', 'adapter', 'app', 'domain', 'infrastructure', 'common'

// build.gradle (根)
subprojects {
    apply plugin: 'java'
    apply plugin: 'org.springframework.boot'
    apply plugin: 'io.spring.dependency-management'

    group = 'com.yourcompany'
    version = '1.0.0-SNAPSHOT'
    sourceCompatibility = '17'
}
```

## 启动模块 (start)

```java
@SpringBootApplication(scanBasePackages = "com.yourcompany")
@EnableCola
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

> `@EnableCola` 是 COLA v5 新增注解，启动 COLA 扩展点机制和领域事件总线。
