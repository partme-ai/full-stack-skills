# Testcontainers 通用模式与最佳实践

## 容器生命周期

| 注解/方式 | 生命周期 | 场景 |
|-----------|------|------|
| `@Container` (static) | 所有测试类共享 | 数据库、消息队列 |
| `@Container` (instance) | 每个测试方法重建 | 需要隔离的测试 |
| `new XxxContainer()` + try-finally | 手动控制 | 复杂生命周期 |

## 单例模式（性能最佳）

```java
// 所有测试共享一个数据库容器，大幅减少启动时间
public abstract class SharedPostgresContainer {
    static PostgreSQLContainer<?> postgres;

    static {
        postgres = new PostgreSQLContainer<>("postgres:16-alpine")
                .withReuse(true);   // 跨 JVM 复用！
        postgres.start();
        Runtime.getRuntime().addShutdownHook(new Thread(postgres::stop));
    }
}
```

启用跨 JVM 复用：`~/.testcontainers.properties`

```properties
testcontainers.reuse.enable=true
```

## 等待策略

```java
// HTTP 等待
new GenericContainer<>("myapp").waitingFor(
    Wait.forHttp("/health").forPort(8080).forStatusCode(200)
);

// 日志等待
new GenericContainer<>("myapp").waitingFor(
    Wait.forLogMessage(".*Started.*", 1)
);

// 健康检查等待
new GenericContainer<>("myapp").waitingFor(
    Wait.forHealthcheck()
);

// TCP 等待
new GenericContainer<>("redis").waitingFor(
    Wait.forListeningPort()
);
```

## 常用容器速查

| 容器 | 使用方式 |
|------|------|
| PostgreSQL | `new PostgreSQLContainer<>("postgres:16-alpine")` |
| MySQL | `new MySQLContainer<>("mysql:8.4")` |
| Redis | `new GenericContainer<>("redis:7-alpine").withExposedPorts(6379)` |
| Kafka | `new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:7.6.1"))` |
| MongoDB | `new MongoDBContainer<>("mongo:7")` |
| Elasticsearch | `new ElasticsearchContainer<>("elasticsearch:8.15.0")` |
| LocalStack (AWS) | `new LocalStackContainer<>(DockerImageName.parse("localstack/localstack:3.7"))` |
| WireMock | `new WireMockContainer("wiremock/wiremock:3.9.1")` |

## CI 加速

```yaml
# 使用 Ryuk 自动清理（Testcontainers 默认）
# 无需额外配置

# 启用跨 JVM 复用减少启动时间
- name: Configure Testcontainers
  run: |
    echo "testcontainers.reuse.enable=true" >> ~/.testcontainers.properties
```

## 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `Could not find a valid Docker environment` | Docker 未运行 | 启动 Docker Desktop / colima |
| 端口冲突 | 随机端口已占用 | Testcontainers 自动处理随机端口 |
| CI 中启动慢 | 首次拉取镜像 | 预拉取镜像 / 使用 `withReuse(true)` |
| Mac 上性能差 | Docker Desktop 文件共享慢 | 使用 OrbStack 或 colima |
```

