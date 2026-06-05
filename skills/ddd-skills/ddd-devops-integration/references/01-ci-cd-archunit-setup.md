# CI/CD ArchUnit Setup Reference

## ArchUnit Maven Configuration

```xml
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>1.3.0</version>
    <scope>test</scope>
</dependency>
```

## Gradle Configuration

```groovy
testImplementation 'com.tngtech.archunit:archunit-junit5:1.3.0'
```

## Full ArchUnit Test Suite for CI/CD

```java
@AnalyzeClasses(packages = "com.example")
public class ArchitectureComplianceTest {

    // P0 — Domain purity: zero framework dependencies
    @ArchTest
    static final ArchRule domain_no_spring =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.springframework..", "javax.persistence..",
                "org.apache.ibatis..", "com.baomidou..");

    @ArchTest
    static final ArchRule domain_no_infrastructure =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..");

    @ArchTest
    static final ArchRule domain_no_external_libs =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("com.fasterxml.jackson..", "org.apache.http..",
                "io.netty..");

    // P1 — Layer dependency direction
    @ArchTest
    static final ArchRule layered_architecture =
        layeredArchitecture()
            .consideringAllDependencies()
            .layer("Interface").definedBy("..interface..")
            .layer("Application").definedBy("..application..")
            .layer("Domain").definedBy("..domain..")
            .layer("Infrastructure").definedBy("..infrastructure..")
            .whereLayer("Interface").mayNotBeAccessedByAnyLayer()
            .whereLayer("Application").mayOnlyBeAccessedByLayers("Interface")
            .whereLayer("Domain").mayOnlyBeAccessedByLayers("Application", "Infrastructure", "Interface")
            .whereLayer("Infrastructure").mayOnlyBeAccessedByLayers("Application");

    // P1 — No circular dependencies between modules
    @ArchTest
    static final ArchRule no_cycle_between_modules =
        slices()
            .matching("com.example.(*)..")
            .should().beFreeOfCycles();

    // P2 — Naming conventions
    @ArchTest
    static final ArchRule aggregate_root_naming =
        classes()
            .that().areAnnotatedWith(AggregateRoot.class)
            .should().haveSimpleNameEndingWith("Aggregate")
            .orShould().haveSimpleNameEndingWith("Root");

    @ArchTest
    static final ArchRule repository_naming =
        classes()
            .that().resideInAPackage("..domain..repository..")
            .and().areInterfaces()
            .should().haveSimpleNameEndingWith("Repository");
}
```

## CI/CD Integration

### Step 1: Run ArchUnit tests as a dedicated pipeline stage

```yaml
# Pipeline stage configuration
architecture-validation:
  stage: test
  script:
    - mvn test -pl domain -Dtest=ArchitectureComplianceTest
  artifacts:
    reports:
      junit: domain/target/surefire-reports/TEST-*.xml
    expire_in: 30 days
```

### Step 2: Configure severity-based failure policy

| Severity | CI/CD Action | Example |
|:--------:|-------------|---------|
| P0 | Block merge | Domain layer has Spring import |
| P1 | Warning + manual approval | Layer violation |
| P2 | Report only | Naming convention violation |

### Step 3: Generate architecture report

```bash
# Generate HTML report
mvn test -pl domain -Dtest=ArchitectureComplianceTest \
  -Darchunit.output.path=target/archunit-report
```

## Performance Considerations

- Run ArchUnit tests in parallel with other test suites
- Use `@AnalyzeClasses(importOptions = {DoNotIncludeTests.class})` to skip test classes
- Cache analysis results with `importOptions = {ImportOption.Predefined.ONLY_INCLUDE_SOURCE}`

## CI/CD Check Script

```bash
#!/bin/bash
# ci-arch-check.sh — Run architecture validation in CI
set -e

echo "=== Architecture Validation ==="

# Run all ArchUnit tests
mvn test -pl domain -Dtest=ArchitectureComplianceTest \
  -Darchunit.freeze.store.default.class=com.tngtech.archunit.library.freeze.ViolationStoreFactory$InMemory

# Check for any violations
if [ $? -ne 0 ]; then
  echo "❌ Architecture violations detected!"
  echo "See target/surefire-reports for details."
  exit 1
fi

echo "✅ Architecture validation passed."
```
