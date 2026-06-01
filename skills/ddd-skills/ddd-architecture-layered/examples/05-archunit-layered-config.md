# ArchUnit 分层架构验证配置示例

## 依赖

```xml
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.3.0</version>
    <scope>test</scope>
</dependency>
```

## 分层规则验证

```java
import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
import static com.tngtech.archunit.library.Architectures.*;

public class LayeredArchitectureTest {

    private final JavaClasses classes = new ClassFileImporter()
        .importPackages("com.example.order");

    @Test
    void verifyLayeredArchitecture() {
        ArchRule rule = layeredArchitecture()
            .consideringAllDependencies()
            .layer("Interface").definedBy("..interface..")
            .layer("Application").definedBy("..application..")
            .layer("Domain").definedBy("..domain..")
            .layer("Infrastructure").definedBy("..infrastructure..")

            .whereLayer("Interface").mayOnlyBeAccessedByLayers("Interface")
            .whereLayer("Application").mayOnlyBeAccessedByLayers("Interface", "Application")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers("Application", "Infrastructure")
            .whereLayer("Infrastructure").mayOnlyBeAccessedByLayers("Infrastructure");

        rule.check(classes);
    }

    @Test
    void domainMustNotDependOnSpring() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.springframework..")
            .because("Domain 层不能依赖 Spring 框架")
            .check(classes);
    }

    @Test
    void domainMustNotDependOnInfrastructure() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .because("Domain 层不能依赖 Infrastructure 层")
            .check(classes);
    }

    @Test
    void applicationMustNotDependOnInterface() {
        noClasses()
            .that().resideInAPackage("..application..")
            .should().dependOnClassesThat()
            .resideInAPackage("..interface..")
            .because("Application 层不能依赖 Interface 层")
            .check(classes);
    }

    @Test
    void repositoryImplShouldBeInInfrastructure() {
        classes()
            .that().haveSimpleNameEndingWith("RepositoryImpl")
            .should().resideInAPackage("..infrastructure..")
            .because("Repository 实现必须在 Infrastructure 层")
            .check(classes);
    }

    @Test
    void repositoryInterfaceShouldBeInDomain() {
        classes()
            .that().haveSimpleNameEndingWith("Repository")
            .and().areInterfaces()
            .should().resideInAPackage("..domain..")
            .because("Repository 接口必须在 Domain 层")
            .check(classes);
    }
}
```

## Maven 插件集成（CI 阶段自动执行）

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.2.5</version>
    <configuration>
        <includes>
            <include>**/*ArchitectureTest.java</include>
        </includes>
    </configuration>
</plugin>
```

## 关键说明

- ArchUnit 在测试阶段执行，不影响运行时性能
- 规则失败构建即中断，防止违规代码合入
- 建议将 `LayeredArchitectureTest` 放在 `src/test/java` 的根包下
- 包名模式 `..interface..` 表示任何层级下的对应包
