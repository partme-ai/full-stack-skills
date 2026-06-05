# Dependency Rules & ArchUnit Verification

## The Golden Rule

> **Source code dependencies must point only inward.**
> Outer layers can depend on inner layers.
> Inner layers never know about outer layers.

Formally: `Enterprise → UseCase → Adapter → Framework`

## Layer Dependency Matrix

```
                    Can depend on:
Layer               Ent    UC     Adap   Fram
────────────────────────────────────────────
Enterprise (★)      ✓      ✗      ✗      ✗
UseCase             ✓      ✓      ✗      ✗
Adapter             ✓      ✓      ✓      ✗
Framework           ✓      ✓      ✓      ✓

Legend:
  ✓ = allowed
  ✗ = prohibited
```

## Concrete Rules for Java Projects

```yaml
Enterprise Layer:
  Cannot import:  org.springframework.*, javax.persistence.*,
                  com.example.usecase.*, com.example.adapter.*
  Can import:     java.util.*, java.math.*, java.time.*
  Package name:   com.example.core

UseCase Layer:
  Cannot import:  org.springframework.stereotype.*, javax.persistence.*,
                  com.example.adapter.*, com.example.framework.*
  Can import:     com.example.core.* (Enterprise)
  Package name:   com.example.usecase

Adapter Layer:
  Cannot import:  com.example.framework.*
  Can import:     com.example.core.*, com.example.usecase.*
  Package names:  com.example.adapter.controller,
                  com.example.adapter.repository,
                  com.example.adapter.gateway

Framework Layer:
  Can import:     ALL layers
  Package names:  com.example.framework.config
```

## ArchUnit Test — Automated Dependency Verification

```java
package com.example.framework.archunit;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
import static com.tngtech.archunit.library.Architectures.*;

/**
 * ★ Automated Clean Architecture dependency verification.
 * Fails the build if any layer violates the dependency rule.
 */
class CleanArchitectureTest {

    private final JavaClasses classes = new ClassFileImporter()
        .importPackages("com.example..");

    // ── Layer Dependency Rules ──

    @Test
    void enterpriseLayerShouldNotDependOnOuterLayers() {
        noClasses()
            .that().resideInAnyPackage("com.example.core..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "com.example.usecase..",
                "com.example.adapter..",
                "com.example.framework..",
                "org.springframework..",
                "jakarta.persistence.."
            )
            .check(classes);
    }

    @Test
    void useCaseLayerShouldNotDependOnAdapterOrFramework() {
        noClasses()
            .that().resideInAnyPackage("com.example.usecase..")
            .should().dependOnClassesThat()
            .resideInAnyPackage(
                "com.example.adapter..",
                "com.example.framework..",
                "org.springframework.stereotype..",
                "jakarta.persistence.."
            )
            .check(classes);
    }

    @Test
    void useCaseLayerShouldOnlyDependOnCore() {
        classes()
            .that().resideInAnyPackage("com.example.usecase..")
            .should().onlyDependOnClassesThat()
            .resideInAnyPackage(
                "com.example.usecase..",
                "com.example.core..",
                "java..",
                "java.time.."
            )
            .check(classes);
    }

    @Test
    void adapterLayerShouldNotDependOnFramework() {
        noClasses()
            .that().resideInAnyPackage("com.example.adapter..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("com.example.framework..")
            .check(classes);
    }

    // ── Layer Architecture Verification ──

    @Test
    void shouldFollowCleanArchitecture() {
        layeredArchitecture()
            .consideringAllDependencies()

            // Define layers
            .layer("Enterprise")
                .definedBy("com.example.core..")
            .layer("UseCase")
                .definedBy("com.example.usecase..")
            .layer("Adapter")
                .definedBy("com.example.adapter..")
            .layer("Framework")
                .definedBy("com.example.framework..")

            // Define dependency constraints
            .whereLayer("Enterprise")
                .mayOnlyBeAccessedByLayers("UseCase", "Adapter", "Framework")
            .whereLayer("UseCase")
                .mayOnlyBeAccessedByLayers("Adapter", "Framework")
            .whereLayer("Adapter")
                .mayOnlyBeAccessedByLayers("Framework")

            .check(classes);
    }

    // ── Specific Anti-pattern Checks ──

    @Test
    void domainShouldNotUseSpringAnnotations() {
        // Domain entities must be plain POJOs
        noClasses()
            .that().resideInAnyPackage("com.example.core..")
            .should().beAnnotatedWith("org.springframework.stereotype.Service")
            .orShould().beAnnotatedWith("org.springframework.stereotype.Component")
            .orShould().beAnnotatedWith("org.springframework.web.bind.annotation.RestController")
            .orShould().beAnnotatedWith("jakarta.persistence.Entity")
            .check(classes);
    }

    @Test
    void useCaseInteractorsShouldHaveProperSuffix() {
        classes()
            .that().resideInAnyPackage("com.example.usecase.interactor..")
            .should().haveSimpleNameEndingWith("Interactor")
            .orShould().haveSimpleNameEndingWith("Service")
            .check(classes);
    }

    @Test
    void useCasePortsShouldBeInterfaces() {
        classes()
            .that().resideInAnyPackage("com.example.usecase.port..")
            .should().beInterfaces()
            .check(classes);
    }

    // ── Naming Conventions ──

    @Test
    void entityClassesShouldNotHoldJpaAnnotations() {
        noClasses()
            .that().resideInAnyPackage("com.example.core.entity..")
            .should().beAnnotatedWith("jakarta.persistence.Entity")
            .check(classes);
    }

    @Test
    void repositoryImplementationsShouldBeInAdapterPackage() {
        classes()
            .that().haveSimpleNameEndingWith("RepositoryImpl")
            .or().haveSimpleNameEndingWith("JpaRepository")
            .or().haveSimpleNameEndingWith("MyBatisRepository")
            .should().resideInAnyPackage("com.example.adapter.repository..")
            .check(classes);
    }
}
```

## Adding ArchUnit to Your Build

```xml
<!-- Maven dependency -->
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.3.0</version>
    <scope>test</scope>
</dependency>
```

```groovy
// Gradle
testImplementation 'com.tngtech.archunit:archunit-junit5:1.3.0'
```

## Module Dependency Rules (Multi-Module Maven/Gradle)

```xml
<!-- order-core/pom.xml — no dependencies on other modules -->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
</dependency>

<!-- order-usecase/pom.xml — depends on core only -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-core</artifactId>
</dependency>

<!-- order-adapter/pom.xml — depends on usecase and core -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-usecase</artifactId>
</dependency>
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- order-framework/pom.xml — depends on all -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-adapter</artifactId>
</dependency>
```

## CI Integration

```yaml
# .github/workflows/architecture-check.yml
name: Architecture Check
on: [push, pull_request]
jobs:
  archunit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
      - name: Run ArchUnit Tests
        run: ./mvnw test -pl order-framework -Dtest=CleanArchitectureTest
```

## Violation Examples

| Violation | Example | Fix |
|-----------|---------|-----|
| Entity uses `@Entity` | `com.example.core.entity.Order` has `@Entity` | Move annotation to Adapter's `OrderEntity` |
| UseCase imports `@Autowired` | `CreateOrderInteractor` uses `@Autowired` | Remove; inject via constructor in Framework config |
| Adapter imports Framework | `JpaOrderRepository` imports `com.example.framework.config.*` | Remove dependency |
| Core imports UseCase | `Order.java` imports `CreateOrderInput` | Enterprise must not know about UseCases |
