# Spring Boot + PostgreSQL 集成测试全流程

## build.gradle

```groovy
dependencies {
    testImplementation 'org.testcontainers:testcontainers:1.20.6'
    testImplementation 'org.testcontainers:postgresql:1.20.6'
    testImplementation 'org.testcontainers:junit-jupiter:1.20.6'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```

## 基础测试

```java
@SpringBootTest
@Testcontainers
class UserRepositoryTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired
    private UserRepository userRepository;

    @Test
    void shouldSaveAndFindUser() {
        User user = new User("test@example.com", "Alice");
        userRepository.save(user);
        Optional<User> found = userRepository.findByEmail("test@example.com");
        assertThat(found).isPresent();
    }
}
```

## 多容器集成（PostgreSQL + Redis + Kafka）

```java
@SpringBootTest
@Testcontainers
class OrderServiceIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine");

    @Container
    static GenericContainer<?> redis = new GenericContainer<>("redis:7-alpine")
            .withExposedPorts(6379);

    @Container
    static KafkaContainer kafka = new KafkaContainer(
            DockerImageName.parse("confluentinc/cp-kafka:7.6.1"));

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
        registry.add("spring.data.redis.host", redis::getHost);
        registry.add("spring.data.redis.port", () -> redis.getMappedPort(6379));
        registry.add("spring.kafka.bootstrap-servers", kafka::getBootstrapServers);
    }

    @Test
    void shouldCreateOrderAndSendEvent() {
        // 测试完整订单流程
    }
}
```

## 单例容器（所有测试类共享，加速）

```java
// 父类
@Testcontainers
public abstract class AbstractIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine");

    static {
        postgres.start();
    }
}

// 子类直接继承
class UserTest extends AbstractIntegrationTest { ... }
class OrderTest extends AbstractIntegrationTest { ... }
```

## CI 配置

```yaml
# .github/workflows/test.yml
- name: Run integration tests
  run: ./gradlew test
  # Testcontainers 自动启动/清理，无需额外配置
```
```

