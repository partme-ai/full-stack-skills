# Example 5: ArchUnit 校验完整配置 + CI/CD 流水线集成

本示例展示如何在 COLA v5 项目中配置 ArchUnit 架构合规测试，并将其集成到 GitHub Actions / GitLab CI 流水线中。

## 目录结构

```
project-root/
├── start/
├── adapter/
├── app/
├── domain/
├── infrastructure/
├── common/
└── start/src/test/java/com/yourcompany/
    └── ArchitectureComplianceTest.java   ← 架构校验测试类
```

## ArchUnit 校验测试

```java
package com.yourcompany;

import com.tngtech.archunit.junit.AnalyzeClasses;
import com.tngtech.archunit.junit.ArchTest;
import com.tngtech.archunit.lang.ArchRule;
import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;

@AnalyzeClasses(packages = "com.yourcompany")
public class ArchitectureComplianceTest {

    // ── P0: Domain 层零依赖 ──

    @ArchTest
    static final ArchRule domain_not_depend_infrastructure =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .because("Domain 层不能依赖 Infrastructure");

    @ArchTest
    static final ArchRule domain_not_depend_app =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..app..")
            .because("Domain 层不能依赖 App");

    @ArchTest
    static final ArchRule domain_not_depend_adapter =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..adapter..")
            .because("Domain 层不能依赖 Adapter");

    // ── P0: Domain 无框架依赖 ──

    @ArchTest
    static final ArchRule domain_no_spring =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.springframework..", "org.springframework.stereotype..")
            .because("Domain 层禁止 Spring 依赖");

    @ArchTest
    static final ArchRule domain_no_jpa =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("javax.persistence..", "jakarta.persistence..")
            .because("Domain 层禁止 JPA 依赖");

    @ArchTest
    static final ArchRule domain_no_mybatis =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.apache.ibatis..")
            .because("Domain 层禁止 MyBatis 依赖");

    // ── P0: Adapter 层不应访问 Infrastructure ──

    @ArchTest
    static final ArchRule adapter_not_depend_infrastructure =
        noClasses()
            .that().resideInAPackage("..adapter..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .because("Adapter 必须通过 App 层访问基础设施");

    // ── P1: 包命名合规 ──

    @ArchTest
    static final ArchRule domain_no_controller =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().resideInAPackage("..controller..")
            .because("Controller 属于 Adapter 层");

    @ArchTest
    static final ArchRule adapter_no_repository =
        noClasses()
            .that().resideInAPackage("..adapter..")
            .should().resideInAPackage("..repository..")
            .because("Repository 属于 Domain 或 Infrastructure 层");
}
```

## Maven 依赖

```xml
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.2.0</version>
    <scope>test</scope>
</dependency>
```

## CI/CD 集成

### GitHub Actions

```yaml
name: COLA Architecture Check
on: [push, pull_request]
jobs:
  architecture-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Run Architecture Tests
        run: mvn test -Dtest=ArchitectureComplianceTest
      - name: Check Score
        run: python scripts/check_cola.py .
```

### GitLab CI

```yaml
cola-architecture-check:
  stage: test
  image: eclipse-temurin:17
  script:
    - mvn test -Dtest=ArchitectureComplianceTest
    - python3 scripts/check_cola.py .
  only:
    - merge_requests
    - main
```

## 运行方式

```bash
# 本地运行
mvn test -Dtest=ArchitectureComplianceTest

# Python 轻量校验（无需编译）
python scripts/check_cola.py src/

# 查看评分
# 输出示例：
# 模块: adapter, app, domain, infrastructure, start
# 违规: 2 (P0:0, P1:2)
# 评分: 90 → A（优秀）
```
