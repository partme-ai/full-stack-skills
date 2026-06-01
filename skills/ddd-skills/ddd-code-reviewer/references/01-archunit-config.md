# ArchUnit Configuration for DDD Compliance

ArchUnit provides automated architecture testing for Java projects. Below are ready-to-use configurations for enforcing DDD layered architecture rules.

## Maven Dependency

```xml
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.3.0</version>
    <scope>test</scope>
</dependency>
```

## Gradle Dependency

```groovy
testImplementation 'com.tngtech.archunit:archunit-junit5:1.3.0'
```

## Complete Compliance Test Suite

```java
package com.example.architecture;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.junit.AnalyzeClasses;
import com.tngtech.archunit.junit.ArchTest;
import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;

@AnalyzeClasses(packages = "com.example")
public class DDDArchitectureComplianceTest {

    // ==========================================
    // P0 Rules — Must Pass (Block Merge)
    // ==========================================

    @ArchTest
    static final ArchRule domain_must_not_depend_on_infrastructure =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .because("Domain layer must not depend on infrastructure (DIP)");

    @ArchTest
    static final ArchRule domain_must_not_depend_on_spring =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "org.springframework..",
                "javax.persistence..",
                "jakarta.persistence..",
                "org.apache.ibatis.."
            )
            .because("Domain layer must have zero framework dependencies");

    @ArchTest
    static final ArchRule domain_must_not_use_jpa_annotations =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().beAnnotatedWith(javax.persistence.Entity.class)
            .orShould().beAnnotatedWith(jakarta.persistence.Entity.class)
            .orShould().beAnnotatedWith(javax.persistence.Table.class)
            .because("Domain entities must be pure POJOs, not JPA entities");

    @ArchTest
    static final ArchRule domain_must_not_depend_on_app =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..application..")
            .because("Domain layer must not depend on Application layer");

    // ==========================================
    // P1 Rules — Should Pass
    // ==========================================

    @ArchTest
    static final ArchRule repository_interfaces_in_domain =
        classes()
            .that().haveSimpleNameEndingWith("Repository")
            .and().resideInAPackage("..infrastructure..")
            .should().implement(
                com.tngtech.archunit.core.domain.JavaClass.Predicates
                    .resideInAPackage("..domain..")
            )
            .because("Repository interfaces should be defined in Domain layer");

    @ArchTest
    static final ArchRule application_must_not_use_sql =
        noClasses()
            .that().resideInAPackage("..application..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "java.sql..",
                "javax.sql..",
                "org.mybatis..",
                "org.springframework.jdbc.."
            )
            .because("Application layer must not directly access SQL/DB");

    @ArchTest
    static final ArchRule application_must_not_depend_on_adapter =
        noClasses()
            .that().resideInAPackage("..application..")
            .should().dependOnClassesThat()
            .resideInAPackage("..adapter..")
            .because("Application layer must not depend on Adapter layer");

    @ArchTest
    static final ArchRule controller_must_not_depend_on_repository =
        noClasses()
            .that().resideInAPackage("..adapter..controller..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..repository..")
            .because("Controllers should not directly access repositories");

    // ==========================================
    // Naming Conventions — P2
    // ==========================================

    @ArchTest
    static final ArchRule repositories_should_be_named_correctly =
        classes()
            .that().resideInAPackage("..domain..")
            .and().haveSimpleNameEndingWith("Repository")
            .should().haveSimpleNameStartingWith("I")
            .orShould().haveSimpleNameContaining("Repository")
            .because("Repository interfaces should follow naming conventions");

    @ArchTest
    static final ArchRule domain_events_should_be_past_tense =
        classes()
            .that().resideInAPackage("..domain..event..")
            .should().haveSimpleNameEndingWith("ed")
            .orShould().haveSimpleNameEndingWith("Event")
            .because("Domain events should be named in past tense (e.g., OrderPaid)");

    // ==========================================
    // Cyclic Dependency Prevention — P0
    // ==========================================

    @ArchTest
    static final ArchRule no_cycles_between_modules =
        slices().matching("..(domain|application|infrastructure|adapter)..")
            .should().beFreeOfCycles()
            .because("Modules must not have circular dependencies");

    // ==========================================
    // Class Size Checks — P2
    // ==========================================

    @ArchTest
    static final ArchRule aggregate_roots_should_not_be_too_large =
        classes()
            .that().resideInAPackage("..domain..entity..")
            .should().containNumberOfLinesLessThan(300)
            .because("Aggregate roots should be focused (< 300 lines)");
}
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Architecture Compliance
on: [pull_request]
jobs:
  arch-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
      - name: Run Architecture Tests
        run: mvn test -pl :arch-test -Dtest=DDDArchitectureComplianceTest
```

### Maven Profile

```xml
<profiles>
    <profile>
        <id>architecture-check</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <configuration>
                        <includes>
                            <include>**/*ArchitectureComplianceTest.java</include>
                        </includes>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

## Custom ArchUnit Extension: Domain Purity Checker

```java
import com.tngtech.archunit.junit.ArchUnitExtension;
import com.tngtech.archunit.lang.ArchCondition;
import com.tngtech.archunit.lang.ConditionEvents;
import com.tngtech.archunit.lang.SimpleConditionEvent;

public class DomainPurityChecker {

    public static final ArchCondition<JavaClass> BE_PURE_DOMAIN_OBJECT =
        new ArchCondition<>("be a pure domain object (no framework annotations)") {
            @Override
            public void check(JavaClass item, ConditionEvents events) {
                boolean hasJpaAnnotation = item.isAnnotatedWith(javax.persistence.Entity.class)
                    || item.isAnnotatedWith(jakarta.persistence.Entity.class)
                    || item.isAnnotatedWith(javax.persistence.Table.class);
                boolean hasSpringAnnotation = item.isAnnotatedWith(org.springframework.stereotype.Service.class)
                    || item.isAnnotatedWith(org.springframework.stereotype.Component.class);

                if (hasJpaAnnotation || hasSpringAnnotation) {
                    events.add(SimpleConditionEvent.violated(item,
                        item.getName() + " has framework annotation in domain layer"));
                }
            }
        };
}
```

## Running Tests Individually

```bash
# Run all architecture tests
mvn test -Dtest=DDDArchitectureComplianceTest

# Run only P0 rules
mvn test -Dtest=DDDArchitectureComplianceTest#domain_must_not_depend_on_infrastructure

# Run with verbose output
mvn test -Dtest=DDDArchitectureComplianceTest -Darchunit.freeze.storeDir=target/freeze
```

## Freezing Violations (Temporary Exemptions)

```java
@ArchTest
@ArchIgnore  // Temporarily ignore until refactoring complete
static final ArchRule domain_must_not_depend_on_spring =
    noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAPackage("org.springframework..");
```

Use `@ArchIgnore` for known violations with a plan to fix. Track in your technical debt backlog.
