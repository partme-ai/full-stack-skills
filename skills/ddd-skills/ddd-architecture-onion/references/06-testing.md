# 06 — Testing Strategy for Onion Architecture

> 洋葱架构的层隔离特性使得测试天然分层：内层可纯单元测试，外层逐步集成。

## 测试金字塔

```
         ╱╲
        ╱ E2E ╲             ← 少量：完整用户旅程
       ╱────────╲
      ╱ Integration ╲        ← 中量：Infrastructure + API
     ╱────────────────╲
    ╱   Unit Tests      ╲    ← 大量：Domain + Application
   ╱────────────────────────╲
```

## 各层测试策略

| 层 | 测试类型 | 依赖 | 工具 |
|---|---------|------|------|
| Domain | 单元测试 | 无（纯 Java） | JUnit 5, AssertJ |
| Application | 单元测试 | Mock 所有 Port | JUnit 5, Mockito |
| Infrastructure | 集成测试 | 真实 DB / MQ | Testcontainers, WireMock |
| API | 集成测试 | Mock Application 层 | MockMvc, WebTestClient |
| E2E | 端到端 | 真实环境 | Testcontainers, RestAssured |

## 代码模板

### Domain 层单元测试（纯业务逻辑，零 Mock）

```java
// test/java/.../domain/model/OrderTest.java
class OrderTest {

    @Test
    void shouldCreateOrderSuccessfully() {
        OrderId id = OrderId.generate();
        Order order = Order.create(id, new CustomerId("CUST-001"));

        assertThat(order.getId()).isEqualTo(id);
        assertThat(order.getStatus()).isEqualTo(OrderStatus.DRAFT);
        assertThat(order.getItems()).isEmpty();
        assertThat(order.getTotalAmount()).isEqualTo(Money.ZERO);
    }

    @Test
    void shouldAddItemToDraftOrder() {
        Order order = Order.create(OrderId.generate(), new CustomerId("CUST-001"));

        order.addItem(new ProductId("PROD-001"), Money.of(BigDecimal.TEN, "CNY"), 2);

        assertThat(order.getItems()).hasSize(1);
        assertThat(order.getItems().get(0).getQuantity()).isEqualTo(2);
        assertThat(order.getTotalAmount()).isEqualTo(Money.of(new BigDecimal("20"), "CNY"));
    }

    @Test
    void shouldThrowExceptionWhenAddingItemToNonDraftOrder() {
        Order order = Order.create(OrderId.generate(), new CustomerId("CUST-001"));
        order.addItem(new ProductId("PROD-001"), Money.of(BigDecimal.TEN, "CNY"), 1);
        order.submit();

        assertThatThrownBy(() ->
            order.addItem(new ProductId("PROD-002"), Money.of(BigDecimal.TEN, "CNY"), 1)
        ).isInstanceOf(DomainException.class)
         .hasMessageContaining("只能向草稿订单添加商品");
    }

    @Test
    void shouldSubmitOrder() {
        Order order = createOrderWithItems();
        order.submit();
        assertThat(order.getStatus()).isEqualTo(OrderStatus.SUBMITTED);
    }

    @Test
    void shouldThrowExceptionWhenSubmittingEmptyOrder() {
        Order order = Order.create(OrderId.generate(), new CustomerId("CUST-001"));
        assertThatThrownBy(order::submit)
            .isInstanceOf(DomainException.class)
            .hasMessageContaining("不能提交空订单");
    }

    private Order createOrderWithItems() {
        Order order = Order.create(OrderId.generate(), new CustomerId("CUST-001"));
        order.addItem(new ProductId("PROD-001"), Money.of(BigDecimal.TEN, "CNY"), 2);
        return order;
    }
}
```

### Application 层单元测试（Mock 所有端口）

```java
// test/java/.../application/service/OrderApplicationServiceImplTest.java
class OrderApplicationServiceImplTest {
    @Mock private OrderRepository orderRepository;
    @Mock private PaymentGateway paymentGateway;
    @Mock private EventPublisher eventPublisher;
    private OrderApplicationServiceImpl orderAppService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        orderAppService = new OrderApplicationServiceImpl(
            orderRepository, paymentGateway, eventPublisher, new OrderAssembler()
        );
    }

    @Test
    void shouldCreateOrderSuccessfully() {
        CreateOrderCommand command = new CreateOrderCommand();
        command.setCustomerId("CUST-001");
        CreateOrderCommand.Item item = new CreateOrderCommand.Item();
        item.setProductId("PROD-001");
        item.setUnitPrice(new BigDecimal("10"));
        item.setQuantity(2);
        command.setItems(List.of(item));

        OrderDTO result = orderAppService.createOrder(command);

        assertThat(result).isNotNull();
        assertThat(result.getCustomerId()).isEqualTo("CUST-001");
        assertThat(result.getStatus()).isEqualTo("SUBMITTED");
        // 验证调用了 Repository
        verify(orderRepository).save(any(Order.class));
        verify(eventPublisher, atLeastOnce()).publish(any(DomainEvent.class));
    }

    @Test
    void shouldThrowExceptionWhenPayNotFoundOrder() {
        when(orderRepository.findById(any(OrderId.class))).thenReturn(Optional.empty());

        assertThatThrownBy(() ->
            orderAppService.payOrder(new PayOrderCommand("NONEXIST"))
        ).isInstanceOf(OrderNotFoundException.class);

        verify(orderRepository, never()).save(any());
    }
}
```

### Infrastructure 层集成测试（Testcontainers）

```java
// test/java/.../infrastructure/data/repository/OrderRepositoryImplTest.java
@Testcontainers
class OrderRepositoryImplTest {
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
        .withDatabaseName("testdb")
        .withUsername("test")
        .withPassword("test");

    @Autowired private OrderRepositoryImpl orderRepository;
    @Autowired private JpaOrderRepository jpaRepo;
    @Autowired private OrderMapper mapper;

    @Test
    void shouldSaveAndFindOrder() {
        Order order = createTestOrder();
        orderRepository.save(order);

        Optional<Order> found = orderRepository.findById(order.getId());

        assertThat(found).isPresent();
        assertThat(found.get().getStatus()).isEqualTo(OrderStatus.DRAFT);
        assertThat(found.get().getItems()).hasSize(2);
    }

    @Test
    void shouldDeleteOrder() {
        Order order = createTestOrder();
        orderRepository.save(order);
        orderRepository.delete(order.getId());

        Optional<Order> found = orderRepository.findById(order.getId());
        assertThat(found).isEmpty();
    }

    private Order createTestOrder() {
        Order order = Order.create(OrderId.generate(), new CustomerId("CUST-001"));
        order.addItem(new ProductId("PROD-001"), Money.of(BigDecimal.TEN, "CNY"), 1);
        order.addItem(new ProductId("PROD-002"), Money.of(new BigDecimal("20"), "CNY"), 2);
        return order;
    }
}
```

### API 层集成测试（MockMvc）

```java
// test/java/.../api/controller/OrderControllerTest.java
@WebMvcTest(OrderController.class)
class OrderControllerTest {
    @Autowired private MockMvc mockMvc;
    @MockBean private OrderApplicationService orderAppService;

    @Test
    void shouldCreateOrder() throws Exception {
        CreateOrderCommand command = new CreateOrderCommand();
        OrderDTO orderDTO = new OrderDTO();
        orderDTO.setOrderId("ORD-001");
        orderDTO.setStatus("SUBMITTED");
        when(orderAppService.createOrder(any())).thenReturn(orderDTO);

        String requestBody = """
            {
                "customerId": "CUST-001",
                "items": [{"productId": "PROD-001", "unitPrice": 10.0, "quantity": 2}]
            }
            """;

        mockMvc.perform(post("/api/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content(requestBody))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.data.orderId").value("ORD-001"));
    }

    @Test
    void shouldReturn400WhenInvalidRequest() throws Exception {
        String requestBody = """
            {
                "customerId": "",
                "items": []
            }
            """;

        mockMvc.perform(post("/api/v1/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content(requestBody))
            .andExpect(status().isBadRequest());
    }
}
```

### 测试覆盖率目标

| 层 | 目标覆盖率 | 测试重点 |
|---|:--------:|---------|
| Domain 实体 | 100% | 所有业务方法、边界条件、异常路径 |
| Domain 值对象 | 100% | 不可变性、equals/hashCode、工厂方法 |
| Domain 领域服务 | 100% | 跨实体逻辑组合 |
| Application 服务 | 90%+ | 编排逻辑、异常处理、事件发布 |
| Infrastructure Repository | 80%+ | CRUD、映射正确性 |
| API Controller | 80%+ | 请求/响应格式、状态码、异常映射 |

## 规范检查清单

- [ ] Domain 层测试无任何框架启动
- [ ] Application 层测试使用 Mock 替代真实基础设施
- [ ] Infrastructure 层测试使用 Testcontainers
- [ ] API 层测试使用 @WebMvcTest（不启动完整容器）
- [ ] 测试覆盖异常路径和边界条件
- [ ] 测试命名遵循 `should_状态_when_条件` 格式
