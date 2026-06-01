# ArchUnit Configuration — 依赖方向自动化验证

> ArchUnit 是一个 Java 测试框架，可以在构建时自动验证架构规则。在 DDD 分层架构中，它用于确保各层之间的依赖方向正确。

## Maven 依赖

```xml
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.3.0</version>
    <scope>test</scope>
</dependency>
```

## 完整 ArchUnit 测试类

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
import static com.tngtech.archunit.library.Architectures.layeredArchitecture;

public class LayeredArchitectureTest {

    private static JavaClasses classes;

    @BeforeAll
    static void setup() {
        classes = new ClassFileImporter()
            .importPackages("com.example.project");
    }

    // ========== P0 规则：分层架构 ==========

    @Test
    void shouldFollowLayeredArchitecture() {
        layeredArchitecture()
            .consideringAllDependencies()
            .layer("Interface").definedBy("..interface..")
            .layer("Application").definedBy("..application..")
            .layer("Domain").definedBy("..domain..")
            .layer("Infrastructure").definedBy("..infrastructure..")

            .whereLayer("Interface").mayOnlyBeAccessedByLayers("Interface")
            .whereLayer("Application").mayOnlyBeAccessedByLayers("Interface", "Application")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers(
                "Application", "Infrastructure", "Interface", "Domain")
            .whereLayer("Infrastructure").mayOnlyBeAccessedByLayers("Infrastructure")

            .check(classes);
    }

    // ========== P0 规则：Domain 纯净度 ==========

    @Test
    void domainLayerShouldNotDependOnInfrastructure() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .check(classes);
    }

    @Test
    void domainLayerShouldNotDependOnSpring() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "org.springframework..",
                "org.springframework.stereotype..",
                "org.springframework.beans..",
                "org.springframework.context.."
            )
            .check(classes);
    }

    @Test
    void domainLayerShouldNotDependOnJpa() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "javax.persistence..",
                "jakarta.persistence..",
                "org.hibernate.."
            )
            .check(classes);
    }

    @Test
    void domainLayerShouldNotDependOnMyBatis() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "org.apache.ibatis..",
                "org.mybatis.."
            )
            .check(classes);
    }

    // ========== P1 规则：层间访问限制 ==========

    @Test
    void interfaceLayerShouldNotDirectlyAccessDomain() {
        noClasses()
            .that().resideInAPackage("..interface..")
            .should().dependOnClassesThat()
            .resideInAPackage("..domain..")
            .check(classes);
    }

    @Test
    void applicationLayerShouldNotDirectlyAccessInfrastructure() {
        noClasses()
            .that().resideInAPackage("..application..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .check(classes);
    }

    @Test
    void infrastructureShouldNotDependOnInterface() {
        noClasses()
            .that().resideInAPackage("..infrastructure..")
            .should().dependOnClassesThat()
            .resideInAPackage("..interface..")
            .check(classes);
    }

    @Test
    void infrastructureShouldNotDependOnApplication() {
        noClasses()
            .that().resideInAPackage("..infrastructure..")
            .should().dependOnClassesThat()
            .resideInAPackage("..application..")
            .check(classes);
    }

    // ========== P1 规则：循环依赖 ==========

    @Test
    void noCyclicDependencies() {
        slices().matching("com.example.project.(*)..")
            .should().beFreeOfCycles()
            .check(classes);
    }

    // ========== P2 规则：命名规范 ==========

    @Test
    void repositoryInterfacesShouldResideInDomain() {
        classes()
            .that().haveSimpleNameEndingWith("Repository")
            .and().areInterfaces()
            .should().resideInAPackage("..domain..")
            .check(classes);
    }

    @Test
    void repositoryImplementationsShouldResideInInfrastructure() {
        classes()
            .that().haveSimpleNameEndingWith("Repository")
            .and().areNotInterfaces()
            .should().resideInAPackage("..infrastructure..")
            .check(classes);
    }

    @Test
    void domainServicesShouldNotHaveFrameworkAnnotations() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().beAnnotatedWith(org.springframework.stereotype.Service.class)
            .orShould().beAnnotatedWith(org.springframework.stereotype.Component.class)
            .orShould().beAnnotatedWith(org.springframework.beans.factory.annotation.Autowired.class)
            .check(classes);
    }
}
```

## CI 集成

### GitHub Actions

```yaml
name: Architecture Check
on: [push, pull_request]
jobs:
  archunit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Run ArchUnit Tests
        run: mvn test -pl *-domain,*-application,*-infrastructure,*-interface -Dtest="*ArchitectureTest*"
```

### Maven Profile

```xml
<profile>
    <id>architecture-check</id>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <configuration>
                    <includes>
                        <include>**/*ArchitectureTest.java</include>
                    </includes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</profile>
```

## 常用规则速查

| 检查项 | ArchUnit 代码片段 |
|--------|------------------|
| 包依赖检查 | `noClasses().that().resideInAPackage("..domain..").should().dependOnClassesThat().resideInAPackage("..infrastructure..")` |
| 分层架构 | `layeredArchitecture().layer("Domain").definedBy("..domain..").whereLayer("Domain").mayOnlyBeAccessedByLayers("Application", "Infrastructure")` |
| 循环依赖 | `slices().matching("com.example.(*)..").should().beFreeOfCycles()` |
| 注解检查 | `noClasses().that().resideInAPackage("..domain..").should().beAnnotatedWith(Service.class)` |
| 命名规范 | `classes().that().haveSimpleNameEndingWith("Repository").should().resideInAPackage("..domain..")` |
| 继承检查 | `classes().that().areAssignableTo(BaseEntity.class).should().resideInAPackage("..domain..")` |
