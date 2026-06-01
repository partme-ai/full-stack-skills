# Testing Strategy for Clean Architecture

## Pyramid Overview

```
         ╱╲
        ╱ E2E ╲              Framework Layer
       ╱────────╲            Full request → response
      ╱Integration╲
     ╱──────────────╲        Adapter Layer
    ╱  Unit + Mock  ╲
   ╱──────────────────╲      UseCase Layer
  ╱    Pure Unit       ╲
 ╱────────────────────────╲  Enterprise Layer
╱                          ╲ Zero mocking needed
```

## Testing by Layer

### Enterprise Layer — Pure Unit Tests

```java
class OrderTest {

    @Test
    void shouldCreateOrderWithDraftStatus() {
        Order order = new Order(OrderId.generate(), Money.ZERO);
        assertThat(order.status()).isEqualTo(OrderStatus.DRAFT);
    }

    @Test
    void shouldTransitionToPaid() {
        Order order = new Order(OrderId.generate(), Money.ZERO);
        order.pay();
        assertThat(order.status()).isEqualTo(OrderStatus.PAID);
    }

    @Test
    void shouldNotPayCancelledOrder() {
        Order order = new Order(OrderId.generate(), Money.ZERO);
        order.cancel();
        assertThatThrownBy(order::pay)
            .isInstanceOf(OrderDomainException.class)
            .hasMessageContaining("cannot transition");
    }

    @Test
    void shouldCalculateTotalFromItems() {
        Order order = new Order(OrderId.generate(), Money.ZERO);
        order.addItem(new OrderItem("PROD-1", 2, new Money("50.00")));
        order.addItem(new OrderItem("PROD-2", 1, new Money("30.00")));
        assertThat(order.calculateTotal()).isEqualTo(new Money("130.00"));
    }

    @Test
    void shouldEmitDomainEvents() {
        Order order = new Order(OrderId.generate(), Money.ZERO);
        order.pay();
        assertThat(order.domainEvents())
            .hasSize(2) // Created + Paid
            .anyMatch(e -> e instanceof OrderCreatedEvent)
            .anyMatch(e -> e instanceof OrderPaidEvent);
    }
}
```

### UseCase Layer — Mock Output Ports

```java
class CreateOrderInteractorTest {

    private InMemoryOrderRepository orderRepo;
    private SpyEventPublisher eventPublisher;
    private SpyNotificationPort notificationPort;
    private CreateOrderInteractor interactor;

    @BeforeEach
    void setUp() {
        orderRepo = new InMemoryOrderRepository();
        eventPublisher = new SpyEventPublisher();
        notificationPort = new SpyNotificationPort();
        interactor = new CreateOrderInteractor(
            orderRepo, eventPublisher, notificationPort);
    }

    @Test
    void shouldCreateOrderSuccessfully() {
        CreateOrderInput input = new CreateOrderInput(
            "CUST-001",
            List.of(new OrderItemInput("PROD-001", 2, new MoneyInput("10.00", "USD")))
        );

        CreateOrderOutput output = interactor.execute(input);

        assertThat(output.status()).isEqualTo(OrderStatus.DRAFT);
        assertThat(output.totalAmount()).isEqualTo(new Money("20.00", "USD"));
    }

    @Test
    void shouldPersistOrder() {
        CreateOrderInput input = validInput();
        CreateOrderOutput output = interactor.execute(input);

        Order saved = orderRepo.findById(output.orderId()).orElseThrow();
        assertThat(saved.status()).isEqualTo(OrderStatus.DRAFT);
    }

    @Test
    void shouldPublishDomainEvents() {
        CreateOrderInput input = validInput();
        interactor.execute(input);

        assertThat(eventPublisher.publishedEvents())
            .hasSize(1)
            .allMatch(e -> e instanceof OrderCreatedEvent);
    }

    @Test
    void shouldSendNotification() {
        CreateOrderInput input = validInput();
        interactor.execute(input);

        assertThat(notificationPort.sentEmails()).hasSize(1);
    }

    @Test
    void shouldFailForEmptyOrder() {
        CreateOrderInput input = new CreateOrderInput("CUST-001", List.of());
        assertThatThrownBy(() -> interactor.execute(input))
            .isInstanceOf(DomainException.class);
    }

    private CreateOrderInput validInput() {
        return new CreateOrderInput(
            "CUST-001",
            List.of(new OrderItemInput("PROD-001", 1, new MoneyInput("10.00", "USD")))
        );
    }
}
```

### PayOrderInteractor Test

```java
class PayOrderInteractorTest {

    private InMemoryOrderRepository orderRepo;
    private SpyPaymentGateway paymentGateway;
    private SpyEventPublisher eventPublisher;
    private PayOrderInteractor interactor;

    @BeforeEach
    void setUp() {
        orderRepo = new InMemoryOrderRepository();
        paymentGateway = new SpyPaymentGateway();
        eventPublisher = new SpyEventPublisher();
        interactor = new PayOrderInteractor(
            orderRepo, paymentGateway, eventPublisher);
    }

    @Test
    void shouldPayOrderSuccessfully() {
        Order order = givenCreatedOrder();
        PayOrderOutput output = interactor.execute(
            new PayOrderInput(order.id(), "pm_card_visa"));

        assertThat(output.status()).isEqualTo(OrderStatus.PAID);
        assertThat(output.transactionId()).isNotBlank();
    }

    @Test
    void shouldFailWhenPaymentDeclined() {
        Order order = givenCreatedOrder();
        paymentGateway.shouldFail(true);

        assertThatThrownBy(() -> interactor.execute(
            new PayOrderInput(order.id(), "pm_card_declined")))
            .isInstanceOf(PaymentFailedException.class);
    }

    private Order givenCreatedOrder() {
        Order order = new Order(OrderId.generate(), new Money("99.00"));
        orderRepo.save(order);
        return order;
    }
}
```

### Adapter Layer — Integration Tests

```java
@SpringBootTest
@AutoConfigureMockMvc
class OrderControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private OrderRepository orderRepository;
    // Uses in-memory test implementation via @Profile("test")

    @Test
    void shouldCreateOrder() throws Exception {
        String requestJson = """
            {
                "customerId": "CUST-001",
                "items": [
                    {"productId": "PROD-001", "quantity": 1, "unitPrice": 10.00}
                ]
            }
            """;

        mockMvc.perform(post("/api/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content(requestJson))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.orderId").isNotEmpty())
            .andExpect(jsonPath("$.status").value("DRAFT"));
    }

    @Test
    void shouldGetOrder() throws Exception {
        // Arrange: create order first
        CreateOrderOutput output = givenOrderExists();

        mockMvc.perform(get("/api/v1/orders/{id}", output.orderId().value()))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.status").value("DRAFT"));
    }

    @Test
    void shouldReturn404ForUnknownOrder() throws Exception {
        mockMvc.perform(get("/api/v1/orders/UNKNOWN"))
            .andExpect(status().isNotFound());
    }

    private CreateOrderOutput givenOrderExists() {
        CreateOrderInput input = new CreateOrderInput(
            "CUST-001",
            List.of(new OrderItemInput("PROD-001", 1, new MoneyInput("10.00", "USD"))));
        return createOrderInteractor.execute(input);
    }
}
```

### Repository Integration Test

```java
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@ActiveProfiles("test")
class JpaOrderRepositoryTest {

    @Autowired
    private SpringDataOrderJpaRepository jpaRepo;

    private JpaOrderRepository repository;

    @BeforeEach
    void setUp() {
        repository = new JpaOrderRepository(jpaRepo, new OrderPersistenceConverter());
    }

    @Test
    void shouldSaveAndFindOrder() {
        Order order = new Order(OrderId.generate(), Money.ZERO);
        repository.save(order);

        Optional<Order> found = repository.findById(order.id());
        assertThat(found).isPresent();
        assertThat(found.get().status()).isEqualTo(OrderStatus.DRAFT);
    }
}
```

## Test Double Recommendations

| Test Double | Layer | Purpose |
|---|---|---|
| **InMemoryRepository** | UseCase tests | Fast, reliable repository mock |
| **SpyEventPublisher** | UseCase tests | Verify events were published |
| **StubPaymentGateway** | UseCase tests | Control payment outcomes |
| **MockMvc** | Adapter tests | Controller HTTP integration |
| **Testcontainers** | Adapter tests | Real DB repository tests |
| **WireMock** | Adapter tests | External API gateway tests |

## In-Memory Test Doubles

```java
public class InMemoryOrderRepository implements OrderRepository {
    private final Map<OrderId, Order> store = new HashMap<>();

    @Override
    public Order save(Order order) {
        store.put(order.id(), order);
        return order;
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public void delete(OrderId id) {
        store.remove(id);
    }

    public void clear() { store.clear(); }
}

public class SpyEventPublisher implements EventPublisher {
    private final List<DomainEvent> events = new ArrayList<>();

    @Override
    public void publish(DomainEvent event) {
        events.add(event);
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        this.events.addAll(events);
    }

    public List<DomainEvent> publishedEvents() { return Collections.unmodifiableList(events); }
    public void clear() { events.clear(); }
}
```

## Coverage Targets

| Layer | Coverage Target | Testing Focus |
|---|---|---|
| Enterprise | > 95% | Entity behaviors, state transitions, invariants |
| UseCase | > 90% | Orchestration logic, port interaction, error paths |
| Adapter | > 80% | HTTP mapping, persistence mapping, gateway calls |
| Framework | > 70% | DI wiring, configuration, security filters |

## Testing Anti-patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| **Spring Boot test for Entity** | Slow, framework-dependent | Pure JUnit test |
| **Mocking everything** | Brittle tests, false confidence | Use InMemory doubles for repos |
| **Testing private methods** | Tests tied to implementation | Test through public behavior |
| **No error path tests** | Code works only in happy path | Test domain exceptions, payment failures |
| **Over-mocking** | Tests mock too many dependencies | Integration test through adapter |
