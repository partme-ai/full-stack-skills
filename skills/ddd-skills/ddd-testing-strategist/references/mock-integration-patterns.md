# 各层测试模式 — Mock 实现与集成测试

## Mock Repository 实现

```java
public class MockOrderRepository implements OrderRepository {
    private final Map<OrderId, Order> store = new HashMap<>();
    private boolean shouldError = false;

    @Override
    public Optional<Order> findById(OrderId id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public void save(Order order) {
        if (shouldError) throw new RuntimeException("Simulated save error");
        store.put(order.getId(), order);
    }

    @Override
    public void delete(Order order) {
        store.remove(order.getId());
    }

    public void simulateErrorOnSave() { this.shouldError = true; }
}
```

## Mock Event Publisher

```java
public class MockEventPublisher implements EventPublisher {
    public final List<DomainEvent> publishedEvents = new ArrayList<>();

    @Override
    public void publish(DomainEvent event) { publishedEvents.add(event); }

    @Override
    public void publishAll(List<DomainEvent> events) { publishedEvents.addAll(events); }
}
```

## 应用层测试（Mock 端口）

```java
class PlaceOrderHandlerTest {
    private PlaceOrderHandler handler;
    private MockOrderRepository orderRepo;
    private MockProductRepository productRepo;
    private MockEventPublisher eventPublisher;

    @BeforeEach void setUp() {
        orderRepo = new MockOrderRepository();
        productRepo = new MockProductRepository();
        eventPublisher = new MockEventPublisher();
        handler = new PlaceOrderHandler(orderRepo, productRepo, eventPublisher);
    }

    @Test void creates_order_with_items_and_saves() {
        productRepo.add(createTestProduct("prod-1", 10.00));
        productRepo.add(createTestProduct("prod-2", 20.00));
        var cmd = new PlaceOrderCommand("cust-123", List.of(
            new ItemCmd("prod-1", 2), new ItemCmd("prod-2", 1)));

        var orderId = handler.handle(cmd);

        assertNotNull(orderId);
        var saved = orderRepo.findById(OrderId.from(orderId.value())).orElseThrow();
        assertEquals(2, saved.getItems().size());
        assertEquals(new Money(40, "USD"), saved.getTotal());
    }

    @Test void publishes_domain_events() {
        productRepo.add(createTestProduct("prod-1", 10.00));
        var cmd = new PlaceOrderCommand("cust-123", List.of(new ItemCmd("prod-1", 1)));

        handler.handle(cmd);

        assertEquals(1, eventPublisher.publishedEvents.size());
        assertTrue(eventPublisher.publishedEvents.get(0) instanceof OrderCreated);
    }

    @Test void throws_when_product_not_found() {
        var cmd = new PlaceOrderCommand("cust-123", List.of(new ItemCmd("nonexistent", 1)));
        assertThrows(ProductNotFoundError.class, () -> handler.handle(cmd));
    }

    @Test void rolls_back_on_error() {
        productRepo.add(createTestProduct("prod-1", 10.00));
        orderRepo.simulateErrorOnSave();
        var cmd = new PlaceOrderCommand("cust-123", List.of(new ItemCmd("prod-1", 1)));
        assertThrows(RuntimeException.class, () -> handler.handle(cmd));
        assertEquals(0, orderRepo.savedCount());
    }
}
```

## 仓储集成测试（真实 DB）

```java
@SpringBootTest
@Testcontainers
class PostgresOrderRepositoryTest {
    @Autowired private OrderRepository repository;
    @Autowired private JdbcTemplate jdbc;

    @BeforeEach void setUp() {
        jdbc.execute("TRUNCATE orders, order_items CASCADE");
    }

    @Test void persists_and_retrieves_complete_aggregate() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.addItem(ProductId.from("prod-1"), Quantity.of(2), Money.usd(10));
        repository.save(order);

        var retrieved = repository.findById(order.getId()).orElseThrow();

        assertEquals(order.getId(), retrieved.getId());
        assertEquals(1, retrieved.getItems().size());
        assertEquals(2, retrieved.getItems().get(0).getQuantity().value());
    }

    @Test void updates_existing_order() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.addItem(ProductId.from("prod-1"), Quantity.of(1), Money.usd(10));
        repository.save(order);
        order.addItem(ProductId.from("prod-2"), Quantity.of(3), Money.usd(20));
        repository.save(order);

        var retrieved = repository.findById(order.getId()).orElseThrow();
        assertEquals(2, retrieved.getItems().size());
    }

    @Test void returns_empty_for_nonexistent() {
        assertTrue(repository.findById(OrderId.from("nonexistent")).isEmpty());
    }
}
```

## API 集成测试

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
class OrdersApiTest {
    @Autowired private MockMvc mvc;
    @Autowired private JdbcTemplate jdbc;

    @BeforeEach void setUp() {
        jdbc.execute("TRUNCATE orders, order_items, products");
        jdbc.update("INSERT INTO products VALUES ('prod-1', 'Product 1', 1000)");
    }

    @Test void creates_order_and_returns_201() throws Exception {
        mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customer_id":"cust-123","items":[{"product_id":"prod-1","quantity":2}]}"""))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").isNotEmpty());
    }

    @Test void returns_400_for_invalid_product() throws Exception {
        mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customer_id":"cust-123","items":[{"product_id":"nonexistent","quantity":1}]}"""))
            .andExpect(status().isBadRequest());
    }

    @Test void returns_404_for_nonexistent_order() throws Exception {
        mvc.perform(get("/orders/nonexistent"))
            .andExpect(status().isNotFound());
    }
}
```

## 事件分发器模式

```java
public class EventDispatcher {
    private final Map<String, List<EventHandler<?>>> handlers = new HashMap<>();

    public <T extends DomainEvent> void register(String eventType, EventHandler<T> handler) {
        handlers.computeIfAbsent(eventType, k -> new ArrayList<>()).add(handler);
    }

    public void dispatch(DomainEvent event) {
        handlers.getOrDefault(event.getEventType(), List.of())
            .forEach(h -> h.handle(event));
    }

    public void dispatchAll(List<DomainEvent> events) {
        events.forEach(this::dispatch);
    }
}

// 注册示例
dispatcher.register("order.created", new OrderCreatedHandler());
dispatcher.register("order.confirmed", new OrderConfirmedHandler());
dispatcher.register("order.shipped", new SendShippingNotificationHandler());
```
