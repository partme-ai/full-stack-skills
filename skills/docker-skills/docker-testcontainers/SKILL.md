---
name: docker-testcontainers
description: Guidance for Testcontainers — running Docker containers in automated integration tests. Covers Java (@Testcontainers, @Container, PostgreSQL/Redis/Kafka/Elasticsearch), Python (testcontainers-python with pytest), container lifecycle management (singleton, reuse), CI/CD integration (Docker-in-Docker, Ryuk), Testcontainer best practices, and database migration testing. Use when the user asks about testcontainers, integration testing with Docker, database testing, Java testcontainers, Python testcontainers, or needs to test with real Docker services. 使用场景：testcontainers、集成测试、docker 测试、数据库测试、Java Testcontainers、Python Testcontainers.
license: Apache-2.0
---

# Docker Testcontainers — 集成测试容器

Guidance for running Docker containers in automated tests with Testcontainers.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "testcontainers", "Testcontainer", "测试容器"
- "集成测试", "docker 测试"
- "数据库测试", "PostgreSQL test", "MySQL test"
- "Java Testcontainers", "Python Testcontainers"
- "测试环境搭建"

## Java — Testcontainers

### PostgreSQL Example

```java
@Testcontainers
@SpringBootTest
class OrderRepositoryTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Test
    void shouldSaveAndFindOrder() {
        Order saved = repository.save(new Order(...));
        assertThat(repository.findById(saved.getId())).isPresent();
    }
}
```

### Redis Example

```java
@Container
static GenericContainer<?> redis = new GenericContainer<>("redis:7-alpine")
        .withExposedPorts(6379);

// Get connection string
String redisUrl = "redis://" + redis.getHost() + ":" + redis.getMappedPort(6379);
```

### Kafka Example

```java
@Container
static KafkaContainer kafka = new KafkaContainer(
        DockerImageName.parse("confluentinc/cp-kafka:7.6.0"));

String bootstrapServers = kafka.getBootstrapServers();
```

## Python — testcontainers-python

```python
import pytest
from testcontainers.postgres import PostgresContainer
from testcontainers.redis import RedisContainer

@pytest.fixture(scope="module")
def postgres():
    with PostgresContainer("postgres:16-alpine") as pg:
        yield pg.get_connection_url()

def test_database_connection(postgres):
    import psycopg2
    conn = psycopg2.connect(postgres)
    assert conn.status == psycopg2.STATUS_READY
```

## Container Lifecycle

```java
// Singleton: one container for all tests
@Container
static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16");

// Per-test: new container for each test
@Test
void test() {
    try (var redis = new GenericContainer<>("redis:7")) {
        redis.start();
        // test...
    } // auto-closed by try-with-resources
}
```

## CI/CD Configuration

```yaml
# GitHub Actions — DinD (Docker-in-Docker)
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      docker:
        image: docker:27-dind
        options: --privileged
    steps:
      - uses: actions/checkout@v4
      - run: ./gradlew test
```

## Workflow — 推荐集成流程

Step 1: **添加依赖**: `testImplementation 'org.testcontainers:testcontainers:1.20.6'`
Step 2: **定义容器**: `@Container static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine")`
Step 3: **注入配置**: `@DynamicPropertySource` 将容器连接信息注入 Spring 配置
Step 4: **编写测试**: `@Test void shouldSaveAndFind()` 正常业务测试
Step 5: **CI 加速**: 启用 `withReuse(true)` + GHA cache

## Gotchas — Common Pitfalls

- **CI slow startup**: Container images need to be pulled in CI. → **Recovery**: Pre-warm by adding `docker pull postgres:16-alpine` before test step; enable `withReuse(true)` in `.testcontainers.properties`.
- **Port conflicts in CI**: Testcontainers picks random ports — no conflicts. But hardcoded ports in tests will fail. → **Recovery**: Always use `container.getMappedPort(5432)` instead of hardcoding port numbers.
- **Resource cleanup**: Ryuk auto-removes containers. In CI, ensure DinD or socket access. → **Recovery**: If `TESTCONTAINERS_RYUK_DISABLED=true`, add `@AfterAll` cleanup; check Docker socket is mounted in CI.
- **Static vs instance containers**: Static `@Container` fields share ONE container across the class. Instance fields create per-test containers. → **Recovery**: Use static for databases (shared state OK); use instance for isolation-critical tests; check `@TestInstance(TestInstance.Lifecycle.PER_CLASS)` for JUnit 5.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | Java/Python 集成测试 | PostgreSQL/MySQL/Redis/Kafka 等容器化数据库测试 |
| ✅ 能做 | Spring Boot 测试 | @Testcontainers + @DynamicPropertySource 自动注入 |
| ✅ 能做 | CI 集成 | GitHub Actions/Jenkins 中自动启动/清理 |
| ⚠️ 需条件 | 跨 JVM 复用 | 需配置 `testcontainers.reuse.enable=true` |
| ⚠️ 需条件 | 非 Java 语言测试 | 使用各语言对应 Testcontainers 库 |
| ❌ 超范围 | 手动测试/调试 | 使用 `docker-run` |
| ❌ 超范围 | 生产数据库测试 | 连接生产实例而非容器 |
| ❌ 超范围 | 性能/压测 | 专用工具（JMeter/K6） |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Manual testing | `docker-run` |
| Production database testing | `docker-storage` + real instance |
| Mock testing | Use Mockito/unittest.mock |
| Docker basics | `docker-basics` |

## Security & Stability

- Testcontainers use random ports — no port conflicts with running services.
- Containers are automatically cleaned up by Ryuk after test completion.
- Never use Testcontainers in production code — test scope only.
- Use `withReuse(true)` for local development to speed up tests (container survives between runs).

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Testcontainers 概述 | https://docs.docker.com/testcontainers/ |
| Testcontainers for Java | https://java.testcontainers.org/ |
| Testcontainers Cloud | https://testcontainers.com/cloud/ |
| Spring Boot 集成 | https://java.testcontainers.org/modules/spring-boot/ |
| CI 配置 | https://java.testcontainers.org/supported_docker_environment/continuous_integration/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-testcontainers` — 测试容器**

**← Prev**: `docker-troubleshooting` — Problem debugging
**→ Next**: `docker-ai-ml` — AI/ML workloads
