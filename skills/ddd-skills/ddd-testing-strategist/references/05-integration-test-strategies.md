# Integration Test Strategies

## Repository Integration Tests

Test aggregate root persistence — save and load the complete aggregate graph. Use Testcontainers for real database.

### Complete Aggregate Persistence

```java
@SpringBootTest
@Testcontainers
class OrderRepositoryImplIntegrationTest {
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
        .withDatabaseName("testdb");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired private OrderRepository repository;
    @Autowired private JdbcTemplate jdbc;

    @BeforeEach void clean() {
        jdbc.execute("TRUNCATE TABLE orders, order_items CASCADE");
    }

    @Test void persists_and_retrieves_aggregate() {
        Order order = Order.create(CustomerId.from("cust-1"));
        order.addItem(ProductId.from("p1"), Quantity.of(2), Money.usd(10));
        order.addItem(ProductId.from("p2"), Quantity.of(1), Money.usd(25));

        repository.save(order);
        var loaded = repository.findById(order.getId()).orElseThrow();

        assertEquals(order.getId(), loaded.getId());
        assertEquals(order.getCustomerId(), loaded.getCustomerId());
        assertEquals(2, loaded.getItems().size());
        assertEquals(new Money(45, "USD"), loaded.getTotalAmount());
    }

    @Test void updates_existing_aggregate() {
        Order order = Order.create(CustomerId.from("cust-1"));
        order.addItem(ProductId.from("p1"), Quantity.of(1), Money.usd(10));
        repository.save(order);

        order.addItem(ProductId.from("p2"), Quantity.of(3), Money.usd(20));
        repository.save(order);

        var loaded = repository.findById(order.getId()).orElseThrow();
        assertEquals(2, loaded.getItems().size());
    }

    @Test void deletes_aggregate() {
        Order order = Order.create(CustomerId.from("cust-1"));
        repository.save(order);
        repository.delete(order);

        assertTrue(repository.findById(order.getId()).isEmpty());
    }

    @Test void returns_empty_for_nonexistent() {
        assertTrue(repository.findById(OrderId.from("nonexistent")).isEmpty());
    }
}
```

### N+1 Query Detection

```java
@Test
void loading_aggregate_should_not_cause_n_plus_1() {
    // Create order with many items
    Order order = Order.create(CustomerId.from("cust-1"), create50Items());
    repository.save(order);

    // Capture SQL count
    SQLStatementCountValidator.reset();
    var loaded = repository.findById(order.getId());
    assertTrue(loaded.isPresent());
    assertSelectCount(1); // 1 query with JOIN, not 1 + N
}
```

## API Integration Tests

Test HTTP endpoints with real database and mocked external services.

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
@Testcontainers
class OrderControllerIntegrationTest {
    @Autowired private MockMvc mvc;
    @Autowired private JdbcTemplate jdbc;

    @BeforeEach void setUp() {
        jdbc.execute("TRUNCATE orders, order_items, products CASCADE");
        jdbc.update("INSERT INTO products (id, name, price) VALUES ('p1', 'Product 1', 1000)");
        jdbc.update("INSERT INTO products (id, name, price) VALUES ('p2', 'Product 2', 2000)");
    }

    @Test void create_order_returns_201() throws Exception {
        mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customerId":"cust-1","items":[{"productId":"p1","quantity":2}]}
                    """))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").isNotEmpty())
            .andExpect(jsonPath("$.total").value(2000));
    }

    @Test void create_order_with_invalid_product_returns_400() throws Exception {
        mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customerId":"cust-1","items":[{"productId":"nonexistent","quantity":1}]}
                    """))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").value("Product not found"));
    }

    @Test void get_order_returns_200() throws Exception {
        String orderId = createTestOrder().getBody().getId();

        mvc.perform(get("/orders/{id}", orderId))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.id").value(orderId))
            .andExpect(jsonPath("$.items").isArray());
    }

    @Test void get_nonexistent_order_returns_404() throws Exception {
        mvc.perform(get("/orders/nonexistent"))
            .andExpect(status().isNotFound());
    }
}
```

## Messaging Integration Tests

Test event publishing and consumption with a real message broker.

```java
@SpringBootTest
@EnableKafka
@Testcontainers
class OrderEventPublisherIntegrationTest {
    @Container
    static KafkaContainer kafka = new KafkaContainer(
        DockerImageName.parse("confluentinc/cp-kafka:latest"));

    @Autowired private OrderEventPublisher publisher;
    @Autowired private KafkaTemplate<String, String> kafkaTemplate;

    @Test void publishes_domain_event_to_kafka() {
        var event = new OrderPaidEvent(OrderId.from("order-1"), Money.usd(100));

        publisher.publish(event);

        // Verify event was published to the correct topic
        // using a test consumer
    }
}
```
