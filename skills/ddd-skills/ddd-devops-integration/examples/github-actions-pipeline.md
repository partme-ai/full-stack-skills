# GitHub Actions — DDD 质量门禁 Pipeline


## 完整 Pipeline 配置

```yaml
name: DDD Quality Gate

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin', cache: maven }
      - name: Build & Unit Tests
        run: mvn clean test -pl domain,application

  architecture-check:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin', cache: maven }
      - name: Domain Purity Check
        run: mvn test -pl domain -Dtest=DomainPurityTest
      - name: Layering Compliance
        run: mvn test -pl domain -Dtest=LayeringComplianceTest
      - name: Module Dependency Check
        run: mvn test -pl domain -Dtest=ModuleDependencyTest

  integration-test:
    needs: architecture-check
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env: { POSTGRES_DB: testdb, POSTGRES_PASSWORD: test }
        options: >- 
          --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5
        ports: [5432:5432]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin', cache: maven }
      - name: Integration Tests
        run: mvn test -pl infrastructure -Dtest='*RepositoryImplTest'
        env:
          SPRING_DATASOURCE_URL: jdbc:postgresql://localhost:5432/testdb
```

## ArchUnit 测试类

```java
@AnalyzeClasses(packages = "com.example")
public class ArchitectureComplianceTest {

    @ArchTest
    static final ArchRule domain_no_spring = noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat().resideInAPackage("org.springframework..");

    @ArchTest
    static final ArchRule domain_no_infra = noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat().resideInAPackage("..infrastructure..");

    @ArchTest
    static final ArchRule no_cycles = slices()
        .matching("com.example.(*)..").should().beFreeOfCycles();
}
```

## 失败策略

| 严重级别 | CI/CD 行为 |
|:--:|------|
| P0 | 阻止合并（block merge） |
| P1 | 告警 + 需审批 |
| P2 | 仅报告 |
