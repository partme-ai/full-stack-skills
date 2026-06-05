# Testing — 测试策略

## 概述

六边形架构的最大优势之一是测试性。通过端口隔离，可以：
- **Domain 层测试**：零基础设施，纯单元测试
- **Application 层测试**：Mock 出站端口，测试用例编排
- **Adapter 层测试**：集成真实适配器或 Test Double

## 测试金字塔

```
           ╱╲
          ╱ E2E ╲           — 完整业务流程（少量）
         ╱────────╲
        ╱ Integration ╲      — 适配器集成（中等）
       ╱────────────────╲
      ╱   Unit (Mock Ports) ╲ — 应用服务 + 端口 Mock（大量）
     ╱────────────────────────╲
    ╱   Unit (Pure Domain)     ╲ — 领域模型，零 Mock，最快（海量）
   ╱──────────────────────────────╲
```

## 领域层测试（零 Mock）

```java
// test/java/domain/model/order/OrderTest.java
class OrderTest {

    @Test
    void should_create_order_with_draft_status() {
        var order = Order.create(CustomerId.of("cust-001"));

        assertEquals(OrderStatus.DRAFT, order.getStatus());
        assertEquals(1, order.getDomainEvents().size());
        assertTrue(order.getDomainEvents().get(0) instanceof OrderCreatedEvent);
    }

    @Test
    void should_add_item_to_draft_order() {
        var order = Order.create(CustomerId.of("cust-001"));
        order.addItem(ProductId.of("prod-001"), Quantity.of(2), Money.of(100, "CNY"));

        assertEquals(1, order.getItems().size());
        assertEquals(Money.of(200, "CNY"), order.getTotalAmount());
    }

    @Test
    void should_throw_when_adding_item_to_paid_order() {
        var order = Order.create(CustomerId.of("cust-001"));
        order.addItem(ProductId.of("prod-001"), Quantity.of(1), Money.of(100, "CNY"));
        order.pay();

        assertThrows(OrderException.class, () ->
                order.addItem(ProductId.of("prod-002"), Quantity.of(1), Money.of(50, "CNY")));
    }

    @Test
    void should_transition_to_paid() {
        var order = Order.create(CustomerId.of("cust-001"));
        order.addItem(ProductId.of("prod-001"), Quantity.of(1), Money.of(100, "CNY"));
        order.pay();

        assertEquals(OrderStatus.PAID, order.getStatus());
        var events = order.getDomainEvents();
        assertTrue(events.stream().anyMatch(e -> e instanceof OrderPaidEvent));
    }

    @Test
    void should_fail_to_pay_non_draft_order() {
        var order = Order.create(CustomerId.of("cust-001"));
        order.pay();  // DRAFT → PAID

        assertThrows(OrderException.class, order::pay);  // PAID → PAID 失败
    }

    @Test
    void should_cancel_order() {
        var order = Order.create(CustomerId.of("cust-001"));
        order.cancel("客户主动取消");

        assertEquals(OrderStatus.CANCELLED, order.getStatus());
    }
}
```

## 应用层测试（Mock 端口）

```java
// test/java/application/service/CreateOrderServiceTest.java
class CreateOrderServiceTest {
    private OrderRepository orderRepository;
    private ProductRepository productRepository;
    private EventPublisher eventPublisher;
    private CreateOrderService service;

    @BeforeEach
    void setUp() {
        orderRepository = mock(OrderRepository.class);
        productRepository = mock(ProductRepository.class);
        eventPublisher = mock(EventPublisher.class);
        var pricingService = new OrderPricingService(new VolumeDiscountPolicy());
        service = new CreateOrderService(orderRepository, productRepository, pricingService, eventPublisher);
    }

    @Test
    void should_create_order_successfully() {
        // Given
        var productId = ProductId.of("prod-001");
        var customerId = CustomerId.of("cust-001");
        var command = new CreateOrderCommand(customerId, CustomerGrade.NORMAL,
                List.of(new ItemCmd(productId, Quantity.of(2))));

        when(productRepository.findById(productId))
                .thenReturn(Optional.of(new Product(productId, "测试商品", Money.of(100, "CNY"))));

        // When
        var result = service.execute(command);

        // Then
        assertNotNull(result.getOrderId());
        verify(orderRepository).save(any(Order.class));
        verify(eventPublisher).publishAll(anyList());
    }

    @Test
    void should_throw_when_product_not_found() {
        var command = new CreateOrderCommand(CustomerId.of("cust-001"), CustomerGrade.NORMAL,
                List.of(new ItemCmd(ProductId.of("non-existent"), Quantity.of(1))));

        when(productRepository.findById(any())).thenReturn(Optional.empty());

        assertThrows(ProductNotFoundException.class, () -> service.execute(command));
        verify(orderRepository, never()).save(any());
    }
}
```

## 适配器集成测试

### Repository 测试

```java
// test/java/adapter/outbound/persistence/PostgresOrderRepositoryTest.java
@SpringBootTest
@Testcontainers
class PostgresOrderRepositoryTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
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
    private OrderRepository orderRepository;

    @Test
    void should_save_and_load_aggregate() {
        // Given
        var order = Order.create(CustomerId.of("cust-001"));
        order.addItem(ProductId.of("prod-001"), Quantity.of(2), Money.of(100, "CNY"));

        // When
        orderRepository.save(order);

        // Then
        var loaded = orderRepository.findById(order.getId());
        assertTrue(loaded.isPresent());
        assertEquals(order.getTotalAmount(), loaded.get().getTotalAmount());
        assertEquals(order.getItems().size(), loaded.get().getItems().size());
    }
}
```

### In-Memory 适配器测试

```java
// test/java/adapter/outbound/inmemory/InMemoryOrderRepositoryTest.java
class InMemoryOrderRepositoryTest {
    private InMemoryOrderRepository repository;

    @BeforeEach
    void setUp() {
        repository = new InMemoryOrderRepository();
    }

    @Test
    void should_save_and_find_by_id() {
        var order = Order.create(CustomerId.of("cust-001"));
        repository.save(order);

        var found = repository.findById(order.getId());
        assertTrue(found.isPresent());
        assertEquals(order.getId(), found.get().getId());
    }

    @Test
    void should_delete_order() {
        var order = Order.create(CustomerId.of("cust-001"));
        repository.save(order);
        repository.delete(order);

        assertTrue(repository.findById(order.getId()).isEmpty());
    }

    @AfterEach
    void tearDown() {
        repository.clear();
    }
}
```

## 端口隔离验证

```java
// test/java/architecture/HexagonalArchitectureTest.java
class HexagonalArchitectureTest {

    @Test
    void domain_should_not_depend_on_frameworks() {
        JavaClasses classes = new ClassFileImporter()
                .importPackages("com.example.domain..");

        // Domain 层不能依赖 Spring/JPA
        noClasses()
                .that().resideInAPackage("com.example.domain..")
                .should().dependOnClassesThat()
                .resideInAnyPackage("org.springframework..", "javax.persistence..", "org.hibernate..")
                .check(classes);
    }

    @Test
    void application_should_only_depend_on_domain() {
        JavaClasses classes = new ClassFileImporter()
                .importPackages("com.example.application..");

        noClasses()
                .that().resideInAPackage("com.example.application..")
                .should().dependOnClassesThat()
                .resideInAnyPackage("com.example.adapter..")
                .check(classes);
    }
}
```

## 测试策略决策表

| 测试类型 | 测试对象 | 是否 Mock | 速度 | 覆盖率目标 |
|---------|---------|----------|------|----------|
| Domain Unit | Entity、VO、DomainService | 否 | ★★★★★ | 100% |
| Application Unit | ApplicationService | Mock Outbound Ports | ★★★★ | 90%+ |
| Adapter Integration | RepositoryImpl、GatewayImpl | 真实 DB/HTTP | ★★★ | 80%+ |
| E2E | 完整流程 | 否 | ★★ | 核心流程 |
| Architecture | 依赖方向 | 否（静态分析） | ★★★★★ | CI 自动执行 |
