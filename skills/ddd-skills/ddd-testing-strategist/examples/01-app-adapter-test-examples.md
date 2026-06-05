# Application & Adapter Test Examples

## Application Service Test (TypeScript — Mock Ports)

```typescript
// tests/application/place_order/place_order_handler.test.ts
import { describe, it, expect, beforeEach } from 'vitest';
import { PlaceOrderHandler, PlaceOrderCommand } from './place_order_handler';
import { createTestProduct } from '../../fixtures/product_fixtures';

describe('PlaceOrderHandler', () => {
  let handler: PlaceOrderHandler;
  let orderRepo: MockOrderRepository;
  let productRepo: MockProductRepository;
  let eventPublisher: MockEventPublisher;

  beforeEach(() => {
    orderRepo = new MockOrderRepository();
    productRepo = new MockProductRepository();
    eventPublisher = new MockEventPublisher();
    handler = new PlaceOrderHandler(orderRepo, productRepo, eventPublisher);
  });

  it('creates order with items and saves', async () => {
    productRepo.addProduct(createTestProduct('prod-1', 10.00));
    productRepo.addProduct(createTestProduct('prod-2', 20.00));

    const orderId = await handler.handle({
      customerId: 'cust-123',
      items: [
        { productId: 'prod-1', quantity: 2 },
        { productId: 'prod-2', quantity: 1 },
      ],
    });

    expect(orderId).toBeDefined();
    const savedOrder = await orderRepo.findById(orderId);
    expect(savedOrder).not.toBeNull();
    expect(savedOrder!.items).toHaveLength(2);
    expect(savedOrder!.total.amount).toBe(40);
  });

  it('publishes domain events', async () => {
    productRepo.addProduct(createTestProduct('prod-1', 10.00));

    await handler.handle({
      customerId: 'cust-123',
      items: [{ productId: 'prod-1', quantity: 1 }],
    });

    expect(eventPublisher.publishedEvents).toHaveLength(1);
    expect(eventPublisher.publishedEvents[0]).toBeInstanceOf(OrderCreated);
  });

  it('throws when product not found', async () => {
    await expect(
      handler.handle({
        customerId: 'cust-123',
        items: [{ productId: 'nonexistent', quantity: 1 }],
      })
    ).rejects.toThrow(ProductNotFoundError);
  });

  it('rolls back on save error', async () => {
    productRepo.addProduct(createTestProduct('prod-1', 10.00));
    orderRepo.simulateErrorOnSave();

    await expect(
      handler.handle({
        customerId: 'cust-123',
        items: [{ productId: 'prod-1', quantity: 1 }],
      })
    ).rejects.toThrow();
    expect(orderRepo.savedOrders).toHaveLength(0);
  });
});
```

## Spring Boot API Test (Java)

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
@Testcontainers
class OrderControllerE2ETest {
    @Autowired private MockMvc mvc;
    @Autowired private JdbcTemplate jdbc;

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry reg) {
        reg.add("spring.datasource.url", postgres::getJdbcUrl);
        reg.add("spring.datasource.username", postgres::getUsername);
        reg.add("spring.datasource.password", postgres::getPassword);
    }

    @BeforeEach void setUp() {
        jdbc.execute("TRUNCATE orders, order_items, products CASCADE");
        jdbc.update("INSERT INTO products (id, name, price) VALUES ('p1', 'Product 1', 1000)");
        jdbc.update("INSERT INTO products (id, name, price) VALUES ('p2', 'Product 2', 2000)");
    }

    @Test
    void complete_order_workflow() throws Exception {
        // Step 1: Create order
        var createResult = mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customerId":"cust-123","items":[
                        {"productId":"p1","quantity":2},
                        {"productId":"p2","quantity":1}
                    ]}"""))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").isNotEmpty())
            .andExpect(jsonPath("$.total").value(4000))
            .andReturn();

        String orderId = JsonPath.read(createResult.getResponse().getContentAsString(), "$.id");

        // Step 2: Get order by ID
        mvc.perform(get("/orders/{id}", orderId))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.customerId").value("cust-123"))
            .andExpect(jsonPath("$.items").isArray())
            .andExpect(jsonPath("$.items.length()").value(2));

        // Step 3: Pay order
        mvc.perform(post("/orders/{id}/pay", orderId))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.status").value("PAID"));

        // Step 4: Verify status after payment
        mvc.perform(get("/orders/{id}", orderId))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.status").value("PAID"));

        // Step 5: List orders by customer
        mvc.perform(get("/orders").param("customerId", "cust-123"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.length()").value(1));
    }

    @Test void creates_order_and_returns_201() throws Exception {
        mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customerId":"cust-123","items":[{"productId":"p1","quantity":2}]}
                    """))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").isNotEmpty())
            .andExpect(jsonPath("$.customerId").value("cust-123"));
    }

    @Test void returns_400_for_invalid_product() throws Exception {
        mvc.perform(post("/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customerId":"cust-123","items":[{"productId":"nonexistent","quantity":1}]}
                    """))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").value("Product not found"));
    }

    @Test void returns_404_for_nonexistent_order() throws Exception {
        mvc.perform(get("/orders/nonexistent"))
            .andExpect(status().isNotFound());
    }
}
```

## Adapter Mock Patterns (Hexagonal Architecture)

```java
// Mock Repository for domain service testing
class MockOrderRepository implements OrderRepository {
    private final Map<OrderId, Order> store = new HashMap<>();
    private boolean shouldErrorOnSave = false;

    @Override
    public Optional<Order> findById(OrderId id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public void save(Order order) {
        if (shouldErrorOnSave) throw new RuntimeException("Simulated save error");
        store.put(order.getId(), order);
    }

    public void simulateErrorOnSave() { this.shouldErrorOnSave = true; }
    public int savedCount() { return store.size(); }
}

// Mock EventPublisher for application service testing
class MockEventPublisher implements EventPublisher {
    private final List<DomainEvent> published = new ArrayList<>();

    @Override
    public void publish(DomainEvent event) { published.add(event); }

    @Override
    public void publishAll(List<DomainEvent> events) { published.addAll(events); }

    public List<DomainEvent> publishedEvents() { return Collections.unmodifiableList(published); }
    public void clear() { published.clear(); }
}
```

## Architecture Rule Test (ArchUnit)

```java
@RunWith(ArchUnitRunner.class)
public class ArchitectureConstraintTest {
    @Test void domain_has_no_external_dependencies() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAnyPackage("org.springframework..", "javax.persistence..")
            .check(new ClassFileImporter().importPackages("com.example"));
    }

    @Test void domain_does_not_depend_on_application() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..application..")
            .check(new ClassFileImporter().importPackages("com.example"));
    }

    @Test void application_does_not_depend_on_infrastructure() {
        noClasses()
            .that().resideInAPackage("..application..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .check(new ClassFileImporter().importPackages("com.example"));
    }

    @Test void repositories_are_named_correctly() {
        classes()
            .that().resideInAPackage("..domain..repository..")
            .should().haveSimpleNameEndingWith("Repository")
            .check(new ClassFileImporter().importPackages("com.example"));
    }

    @Test void domain_events_use_past_tense() {
        classes()
            .that().resideInAPackage("..domain..event..")
            .should().haveSimpleNameEndingWith("Event")
            .andShould().haveSimpleNameMatching(".*(Created|Updated|Deleted|Paid|Cancelled|Shipped|Confirmed)")
            .check(new ClassFileImporter().importPackages("com.example"));
    }
}
```
