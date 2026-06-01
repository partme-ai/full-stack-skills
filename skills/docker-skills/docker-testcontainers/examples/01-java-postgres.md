# Java Testcontainers with PostgreSQL + Redis

```java
@Testcontainers
@SpringBootTest
class OrderServiceTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine")
            .withDatabaseName("testdb");

    @Container
    static GenericContainer<?> redis = new GenericContainer<>("redis:7-alpine")
            .withExposedPorts(6379);

    @DynamicPropertySource
    static void properties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
        registry.add("spring.redis.host", redis::getHost);
        registry.add("spring.redis.port", () -> redis.getMappedPort(6379));
    }

    @Autowired
    private OrderService orderService;

    @Test
    void shouldCreateAndRetrieveOrder() {
        Order order = orderService.create(new CreateOrderRequest("item-1", 2));
        assertThat(orderService.findById(order.getId())).isPresent();
    }
}
```

### build.gradle
```groovy
testImplementation "org.testcontainers:testcontainers:1.20.0"
testImplementation "org.testcontainers:postgresql:1.20.0"
testImplementation "org.testcontainers:junit-jupiter:1.20.0"
```
