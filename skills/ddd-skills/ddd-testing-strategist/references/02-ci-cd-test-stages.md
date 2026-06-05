# CI/CD Test Stage Configuration

## 三阶段测试编排

```
Commit Stage (< 5 min):
  目标：快速反馈，6-8秒完成
  ✓ Value Object 单元测试
  ✓ Aggregate Root 测试
  ✓ Domain Service 测试（Mock Repository）
  ✓ 禁止：涉及 DB / 网络 / MQ 的测试

PR Stage (< 15 min):
  目标：全面验证变更质量
  ✓ Repository 集成测试（Testcontainers）
  ✓ Application Service 集成测试（Mock Ports）
  ✓ API 契约测试
  ✓ Architecture 测试（ArchUnit）
  ✓ N+1 查询检测

Release Stage (< 30 min):
  目标：生产环境最终验证
  ✓ E2E 测试（关键用户旅程 3-5 个）
  ✓ 性能测试（N+1 查询检测 + 响应时间）
  ✓ 安全扫描（已知漏洞检查）
```

## GitHub Actions 配置示例

```yaml
name: DDD Testing Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  commit-stage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
      - name: Domain Unit Tests
        run: ./mvnw test -pl domain -Dtest="*Test" -DfailIfNoTests=false

  pr-stage:
    needs: commit-stage
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: testdb
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - name: Integration + Architecture Tests
        run: |
          ./mvnw verify -pl infrastructure,adapter \
            -Dtest="*IntegrationTest,*ArchTest" \
            -Dspring.datasource.url=jdbc:postgresql://localhost:5432/testdb

  release-stage:
    needs: pr-stage
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: E2E Tests
        run: ./mvnw verify -pl e2e -Dtest="*E2ETest"
      - name: Performance Tests
        run: ./mvnw gatling:test
```

## N+1 Query Detection in CI

```xml
<!-- Maven Surefire + hibernate-statistics -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <systemPropertyVariables>
            <hibernate.generate_statistics>true</hibernate.generate_statistics>
        </systemPropertyVariables>
    </configuration>
</plugin>
```

```java
@Test
void aggregate_loading_should_not_cause_n_plus_1() {
    SQLStatementCountValidator.reset();
    Order order = repository.findById(orderId).orElseThrow();
    // Access items — should NOT trigger N+1
    int itemCount = order.getItems().size();
    assertSelectCount(1); // Single query with JOIN
}
```

## Architecture Test Stage

```java
@RunWith(ArchUnitRunner.class)
public class ArchitectureTest {
    @Test
    void domain_layer_should_not_depend_on_infrastructure() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .check(new ClassFileImporter()
                .importPackages("com.example"));
    }

    @Test
    void domain_layer_should_have_no_framework_deps() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.springframework..", "javax.persistence..")
            .check(new ClassFileImporter()
                .importPackages("com.example"));
    }
}
```
