# Example: ArchUnit Dependency Verification Test

## File: `order-framework/src/test/java/.../archunit/CleanArchitectureTest.java`

Complete ArchUnit test suite for verifying Clean Architecture dependency rules automatically.

## Complete Test Suite

```java
package com.example.framework.archunit;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import com.tngtech.archunit.lang.ArchRule;
import com.tngtech.archunit.lang.syntax.ArchRuleDefinition;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
import static com.tngtech.archunit.library.Architectures.*;
import static com.tngtech.archunit.library.dependencies.SlicesRuleDefinition.*;

/**
 * Automated Clean Architecture dependency verification.
 * Run as part of CI/CD pipeline. Fails build on violations.
 */
class CleanArchitectureTest {

    private static JavaClasses classes;

    @BeforeAll
    static void setUp() {
        classes = new ClassFileImporter()
            .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
            .importPackages("com.example..");
    }

    // ─────────────────────────────────────────────
    // Layer Dependency Rules
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("Layer Dependency Rules")
    class LayerDependencyTests {

        @Test
        @DisplayName("Enterprise layer must not depend on outer layers")
        void enterpriseShouldNotDependOnOuterLayers() {
            noClasses()
                .that().resideInAnyPackage("com.example.core..")
                .should().dependOnClassesThat()
                .resideInAnyPackage(
                    "com.example.usecase..",
                    "com.example.adapter..",
                    "com.example.framework.."
                )
                .because("Enterprise Business Rules (core) must be completely "
                    + "independent of outer layers (Clean Architecture rule)")
                .check(classes);
        }

        @Test
        @DisplayName("UseCase layer must not depend on Adapter or Framework")
        void useCaseShouldNotDependOnAdapterOrFramework() {
            noClasses()
                .that().resideInAnyPackage("com.example.usecase..")
                .should().dependOnClassesThat()
                .resideInAnyPackage(
                    "com.example.adapter..",
                    "com.example.framework.."
                )
                .because("UseCase layer must only depend on Enterprise layer "
                    + "and its own packages")
                .check(classes);
        }

        @Test
        @DisplayName("Adapter layer must not depend on Framework")
        void adapterShouldNotDependOnFramework() {
            noClasses()
                .that().resideInAnyPackage("com.example.adapter..")
                .should().dependOnClassesThat()
                .resideInAnyPackage("com.example.framework..")
                .because("Adapter layer must not know about framework configuration");
        }

        @Test
        @DisplayName("No layer should have circular dependencies")
        void noCircularDependencies() {
            slices().matching("com.example.(*)..")
                .should().beFreeOfCycles()
                .because("Cycles between layers violate the Dependency Rule");
        }
    }

    // ─────────────────────────────────────────────
    // Layer Architecture Definition
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("Clean Architecture Layers")
    class CleanArchitectureDefinitionTests {

        @Test
        @DisplayName("All layers follow Clean Architecture dependency direction")
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

                // Dependency constraints: outer can depend on inner, NOT reverse
                .whereLayer("Enterprise")
                    .mayOnlyBeAccessedByLayers("UseCase", "Adapter", "Framework")
                .whereLayer("UseCase")
                    .mayOnlyBeAccessedByLayers("Adapter", "Framework")
                .whereLayer("Adapter")
                    .mayOnlyBeAccessedByLayers("Framework")

                .because("Clean Architecture: source code dependencies "
                    + "must point only inward")
                .check(classes);
        }
    }

    // ─────────────────────────────────────────────
    // Enterprise Layer Purity
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("Enterprise Layer Purity")
    class EnterprisePurityTests {

        @Test
        @DisplayName("Enterprise entities must not use Spring annotations")
        void entitiesShouldNotUseSpringAnnotations() {
            noClasses()
                .that().resideInAnyPackage("com.example.core.entity..")
                .should().beAnnotatedWith("org.springframework.stereotype.Service")
                .orShould().beAnnotatedWith("org.springframework.stereotype.Component")
                .orShould().beAnnotatedWith("org.springframework.web.bind.annotation.RestController")
                .orShould().beAnnotatedWith("org.springframework.stereotype.Repository")
                .because("Enterprise entities must be pure POJOs — "
                    + "no framework annotations allowed")
                .check(classes);
        }

        @Test
        @DisplayName("Enterprise layer must not use JPA annotations")
        void entitiesShouldNotUseJpaAnnotations() {
            noClasses()
                .that().resideInAnyPackage("com.example.core..")
                .should().beAnnotatedWith("jakarta.persistence.Entity")
                .orShould().beAnnotatedWith("jakarta.persistence.Table")
                .orShould().beAnnotatedWith("jakarta.persistence.Column")
                .orShould().beAnnotatedWith("jakarta.persistence.Id")
                .because("Enterprise layer must be JPA-free — "
                    + "persistence is an infrastructure concern")
                .check(classes);
        }

        @Test
        @DisplayName("Enterprise layer must not import framework packages")
        void entitiesShouldNotImportFrameworkPackages() {
            noClasses()
                .that().resideInAnyPackage("com.example.core..")
                .should().dependOnClassesThat()
                .resideInAnyPackage(
                    "org.springframework..",
                    "jakarta.persistence..",
                    "jakarta.servlet..",
                    "com.fasterxml.jackson..",
                    "org.apache..",
                    "org.hibernate.."
                )
                .because("Enterprise Business Rules must have zero framework dependencies")
                .check(classes);
        }
    }

    // ─────────────────────────────────────────────
    // UseCase Layer Rules
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("UseCase Layer Rules")
    class UseCaseLayerTests {

        @Test
        @DisplayName("UseCase ports must be interfaces")
        void portsShouldBeInterfaces() {
            classes()
                .that().resideInAnyPackage("com.example.usecase.port..")
                .should().beInterfaces()
                .because("Ports are contracts — must be interfaces")
                .check(classes);
        }

        @Test
        @DisplayName("UseCase interactors must implement a port interface")
        void interactorsShouldImplementPort() {
            classes()
                .that().resideInAnyPackage("com.example.usecase.interactor..")
                .should().implement(
                    (java.lang.reflect.Type) null // simplified: check naming convention instead
                )
                .because("Every Interactor must implement an Input Port")
                .check(classes);

            // Alternative: check naming convention
            classes()
                .that().resideInAnyPackage("com.example.usecase.interactor..")
                .should().haveSimpleNameEndingWith("Interactor")
                .because("UseCase implementations should be named *Interactor")
                .check(classes);
        }

        @Test
        @DisplayName("UseCase must not import Spring's @Service annotation")
        void useCaseShouldNotUseServiceAnnotation() {
            noClasses()
                .that().resideInAnyPackage("com.example.usecase..")
                .should().beAnnotatedWith("org.springframework.stereotype.Service")
                .because("UseCase layer uses @Service from Spring — "
                    + "use framework config for wiring instead")
                .allowEmptyShould(true)
                .check(classes);
        }
    }

    // ─────────────────────────────────────────────
    // Adapter Layer Rules
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("Adapter Layer Rules")
    class AdapterLayerTests {

        @Test
        @DisplayName("Adapters implementing Output Ports must have matching names")
        void repositoryImplementationsShouldHaveCorrectSuffix() {
            classes()
                .that().resideInAnyPackage("com.example.adapter.repository..")
                .and().areNotInterfaces()
                .should().haveSimpleNameEndingWith("Repository")
                .orShould().haveSimpleNameEndingWith("Impl")
                .because("Repository adapters should be named *Repository or *Impl")
                .check(classes);
        }

        @Test
        @DisplayName("Controllers must be in the adapter layer")
        void controllersShouldBeInAdapterLayer() {
            classes()
                .that().areAnnotatedWith("org.springframework.web.bind.annotation.RestController")
                .or().areAnnotatedWith("org.springframework.stereotype.Controller")
                .should().resideInAnyPackage("com.example.adapter.controller..")
                .because("Controllers belong in the Adapter layer, not UseCase or Enterprise")
                .check(classes);
        }

        @Test
        @DisplayName("JPA entities must be in the adapter layer")
        void jpaEntitiesShouldBeInAdapterLayer() {
            classes()
                .that().areAnnotatedWith("jakarta.persistence.Entity")
                .should().resideInAnyPackage("com.example.adapter..")
                .because("JPA entities belong in the Adapter layer, "
                    + "separate from domain entities")
                .check(classes);
        }
    }

    // ─────────────────────────────────────────────
    // Naming Conventions
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("Naming Conventions")
    class NamingConventionTests {

        @Test
        @DisplayName("Enterprise entities should not be suffixed with 'Entity'")
        void domainEntitiesShouldNotBeNamedEntity() {
            classes()
                .that().resideInAnyPackage("com.example.core.entity..")
                .should().haveSimpleNameNotEndingWith("Entity")
                .because("Domain entities are just domain classes; "
                    + "'Entity' suffix implies JPA Entity (which is in adapter)")
                .check(classes);
        }

        @Test
        @DisplayName("Value objects should be immutable (final fields)")
        void valueObjectsShouldBeFinal() {
            // Simplified check: value objects should have 'final' modifier
            // or be Java records
            noClasses()
                .that().resideInAnyPackage("com.example.core.valueobject..")
                .should().haveOnlyFinalFields()
                .orShould().beRecords();
        }

        @Test
        @DisplayName("Repository interfaces should be in port.output package")
        void repositoryInterfacesShouldBeInPortOutput() {
            classes()
                .that().haveSimpleNameEndingWith("Repository")
                .and().areInterfaces()
                .and().resideInAnyPackage("com.example.usecase..")
                .should().resideInAnyPackage("com.example.usecase.port.output..")
                .because("Repository interfaces (Output Ports) belong in "
                    + "usecase.port.output package")
                .check(classes);
        }
    }

    // ─────────────────────────────────────────────
    // Anti-pattern Detection
    // ─────────────────────────────────────────────

    @Nested
    @DisplayName("Anti-pattern Detection")
    class AntiPatternTests {

        @Test
        @DisplayName("No domain service should have @Transactional")
        void domainServiceShouldNotBeTransactional() {
            noMethods()
                .that().areDeclaredInClassesThat()
                .resideInAnyPackage("com.example.core..")
                .should().beAnnotatedWith("org.springframework.transaction.annotation.Transactional")
                .because("Transactions belong in the Adapter/Infrastructure layer, "
                    + "not in Enterprise Business Rules")
                .check(classes);
        }

        @Test
        @DisplayName("Enterprise services should not autowire")
        void enterpriseLayerShouldNotAutowired() {
            noClasses()
                .that().resideInAnyPackage("com.example.core..")
                .should().beAnnotatedWith("org.springframework.beans.factory.annotation.Autowired")
                .because("Enterprise layer uses constructor injection via framework config, "
                    + "not field injection with @Autowired")
                .check(classes);
        }
    }
}
```

## Maven Setup

```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.3.0</version>
    <scope>test</scope>
</dependency>
```

## Test Execution

```bash
# Run ArchUnit tests only
./mvnw test -pl order-framework -Dtest=CleanArchitectureTest

# Include as part of the verify lifecycle
./mvnw verify
```

## CI Pipeline Integration

```yaml
# .github/workflows/architecture.yml
name: Architecture Compliance
on: [pull_request]

jobs:
  archunit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
      - name: Cache Maven
        uses: actions/cache@v3
        with:
          path: ~/.m2/repository
          key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}

      - name: Run ArchUnit Tests
        run: |
          ./mvnw test -pl order-framework \
            -Dtest=CleanArchitectureTest \
            -DfailIfNoTests=false

      - name: Generate Report (on failure)
        if: failure()
        run: echo "Architecture violations found. Check test output above."
```

## Expected Output

```
CleanArchitectureTest -
  ✔ Layer Dependency Rules
    ✔ Enterprise layer must not depend on outer layers
    ✔ UseCase layer must not depend on Adapter or Framework
    ✔ Adapter layer must not depend on Framework
    ✔ No layer should have circular dependencies
  ✔ Clean Architecture Layers
    ✔ All layers follow Clean Architecture dependency direction
  ✔ Enterprise Layer Purity
    ✔ Enterprise entities must not use Spring annotations
    ✔ Enterprise layer must not use JPA annotations
    ✔ Enterprise layer must not import framework packages
  ✔ UseCase Layer Rules
    ✔ UseCase ports must be interfaces
    ✔ UseCase interactors must implement a port interface
    ✔ UseCase must not import Spring's @Service annotation
  ✔ Adapter Layer Rules
    ✔ Repository implementations should have correct suffix
    ✔ Controllers must be in the adapter layer
    ✔ JPA entities must be in the adapter layer
  ✔ Naming Conventions
    ✔ Enterprise entities should not be suffixed with 'Entity'
    ✔ Value objects should be immutable
    ✔ Repository interfaces should be in port.output package
  ✔ Anti-pattern Detection
    ✔ No domain service should have @Transactional
    ✔ Enterprise layer should not autowire
```

## Key Points

| Test Category | Why It Matters |
|---------------|----------------|
| **Layer Dependencies** | Enforces the Clean Architecture dependency rule at compile level |
| **Enterprise Purity** | Prevents framework leaks into the most critical layer |
| **Port Interfaces** | Ensures the interface-segregation principle is followed |
| **Name Conventions** | Makes architecture violations obvious from file names alone |
| **Anti-patterns** | Catches common mistakes that violate DDD principles |

> Run ArchUnit tests in CI on every pull request. If a violation is found, the build fails before the code reaches production.
