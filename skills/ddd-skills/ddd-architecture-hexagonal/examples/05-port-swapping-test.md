# Example: 主适配器端口可替换性与测试

本示例展示六边形架构中主适配器（Primary Adapter）的端口可替换性。同一个 `UseCase` 接口可以被 REST、gRPC、CLI 三种入口调用，无需修改 Domain 和 Application 层代码。

## 场景：同一 UseCase 三种入口

### 端口定义（Domain 层 — 唯一不变的核心）

```java
// domain/port/inbound/CreateOrderUseCase.java
public interface CreateOrderUseCase {
    OrderCreatedResult execute(CreateOrderCommand command);
}

// domain/port/inbound/CreateOrderCommand.java
public record CreateOrderCommand(
    CustomerId customerId,
    List<OrderLineItem> items,
    Address shippingAddress
) {}

// domain/port/inbound/OrderCreatedResult.java
public record OrderCreatedResult(
    OrderId orderId,
    OrderStatus status,
    Money totalAmount,
    Instant createdAt
) {}
```

### 应用服务实现（Application 层 — 不依赖具体入口类型）

```java
// application/service/CreateOrderServiceImpl.java
@ApplicationService
public class CreateOrderServiceImpl implements CreateOrderUseCase {
    private final OrderRepository orderRepository;
    private final EventPublisher eventPublisher;

    public CreateOrderServiceImpl(OrderRepository orderRepository, EventPublisher eventPublisher) {
        this.orderRepository = orderRepository;
        this.eventPublisher = eventPublisher;
    }

    @Override
    public OrderCreatedResult execute(CreateOrderCommand command) {
        var order = Order.create(command.customerId());
        command.items().forEach(order::addItem);
        order.assignShippingAddress(command.shippingAddress());
        orderRepository.save(order);
        eventPublisher.publish(new OrderCreatedEvent(order));
        return OrderCreatedResult.from(order);
    }
}
```

## 入口 1：REST Controller

```java
// adapter/inbound/rest/OrderController.java
@RestController
@RequestMapping("/api/orders")
public class OrderController {
    private final CreateOrderUseCase createOrderUseCase;

    public OrderController(CreateOrderUseCase createOrderUseCase) {
        this.createOrderUseCase = createOrderUseCase;
    }

    @PostMapping
    public ResponseEntity<CreateOrderResponse> create(@RequestBody @Valid CreateOrderRequest request) {
        var command = request.toCommand();
        var result = createOrderUseCase.execute(command);
        return ResponseEntity.status(201).body(CreateOrderResponse.from(result));
    }
}
```

## 入口 2：gRPC Service

```java
// adapter/inbound/grpc/OrderGrpcService.java
@GrpcService
public class OrderGrpcService extends OrderServiceGrpc.OrderServiceImplBase {
    private final CreateOrderUseCase createOrderUseCase;
    private final GrpcMapper grpcMapper;

    public OrderGrpcService(CreateOrderUseCase createOrderUseCase, GrpcMapper grpcMapper) {
        this.createOrderUseCase = createOrderUseCase;
        this.grpcMapper = grpcMapper;
    }

    @Override
    public void createOrder(CreateOrderProto request, StreamObserver<CreateOrderResponseProto> observer) {
        var command = grpcMapper.toCommand(request);
        var result = createOrderUseCase.execute(command);
        observer.onNext(grpcMapper.toProto(result));
        observer.onCompleted();
    }
}
```

## 入口 3：CLI Command

```java
// adapter/inbound/cli/CreateOrderCommand.java
@Component
public class CreateOrderCliCommand implements CommandLineRunner {
    private final CreateOrderUseCase createOrderUseCase;

    public CreateOrderCliCommand(CreateOrderUseCase createOrderUseCase) {
        this.createOrderUseCase = createOrderUseCase;
    }

    @Override
    public void run(String... args) {
        if (args.length < 1 || !"--create-order".equals(args[0])) return;
        var command = parseArgs(args);
        var result = createOrderUseCase.execute(command);
        System.out.printf("订单已创建: %s (金额: %s)%n", result.orderId(), result.totalAmount());
    }
}
```

## 测试：端口级别隔离验证

核心验证目标：**Domain 和 Application 层不需要为每种入口编写测试，因为入口切换不影响业务逻辑。**

### 1. 领域层测试（零入口依赖）

```java
// domain/src/test/java/.../OrderTest.java
class OrderTest {
    @Test
    void should_create_order_with_initial_status() {
        var order = Order.create(CustomerId.of("CUST-001"));
        assertEquals(OrderStatus.CREATED, order.getStatus());
        assertTrue(order.getItems().isEmpty());
    }

    @Test
    void should_add_item_to_order() {
        var order = Order.create(CustomerId.of("CUST-001"));
        order.addItem(new OrderLineItem(ProductId.of("PROD-001"), 2, Money.of(99.99)));
        assertEquals(1, order.getItems().size());
    }
}
```

### 2. 应用层测试（Mock 端口 — 不依赖入口类型）

```java
// application/src/test/java/.../CreateOrderServiceImplTest.java
class CreateOrderServiceImplTest {
    @Mock OrderRepository orderRepository;
    @Mock EventPublisher eventPublisher;
    private CreateOrderServiceImpl service;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        service = new CreateOrderServiceImpl(orderRepository, eventPublisher);
    }

    @Test
    void should_execute_order_creation() {
        var command = new CreateOrderCommand(
            CustomerId.of("CUST-001"),
            List.of(new OrderLineItem(ProductId.of("PROD-001"), 1, Money.of(99.99))),
            new Address("北京", "朝阳区", "100000")
        );
        var result = service.execute(command);
        assertNotNull(result.orderId());
        verify(orderRepository).save(any(Order.class));
        verify(eventPublisher).publish(any(OrderCreatedEvent.class));
    }
}
```

### 3. 主适配器测试（仅测协议转换 — 用 Mock 隔离业务逻辑）

```java
// adapter/src/test/java/.../rest/OrderControllerTest.java
@WebMvcTest(OrderController.class)
class OrderControllerTest {
    @MockBean CreateOrderUseCase createOrderUseCase;
    @Autowired MockMvc mockMvc;

    @Test
    void should_convert_http_request_to_command() throws Exception {
        var result = new OrderCreatedResult(
            OrderId.of("ORD-001"), OrderStatus.CREATED, Money.of(99.99), Instant.now());
        when(createOrderUseCase.execute(any())).thenReturn(result);

        mockMvc.perform(post("/api/orders")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                    {"customerId":"CUST-001","items":[{"productId":"PROD-001","quantity":1,"price":99.99}]}
                    """))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.orderId").value("ORD-001"));
    }
}
```

```java
// adapter/src/test/java/.../grpc/OrderGrpcServiceTest.java
@ExtendWith(MockitoExtension.class)
class OrderGrpcServiceTest {
    @Mock CreateOrderUseCase createOrderUseCase;
    @Mock GrpcMapper grpcMapper;
    private OrderGrpcService service;

    @Test
    void should_convert_grpc_request_to_command() {
        service = new OrderGrpcService(createOrderUseCase, grpcMapper);
        var protoRequest = CreateOrderProto.newBuilder()
            .setCustomerId("CUST-001").build();
        var command = new CreateOrderCommand(
            CustomerId.of("CUST-001"), List.of(), null);
        when(grpcMapper.toCommand(protoRequest)).thenReturn(command);
        when(createOrderUseCase.execute(command)).thenReturn(mockResult());

        var observer = new TestStreamObserver<CreateOrderResponseProto>();
        service.createOrder(protoRequest, observer);

        assertNotNull(observer.getResponse());
    }
}
```

### 4. 适配器可替换性测试（同一测试用例验证所有入口）

```java
// adapter/src/test/java/.../PrimaryAdapterSwapTest.java
class PrimaryAdapterSwapTest {
    @Mock CreateOrderUseCase useCase;
    private OrderController restAdapter;
    private OrderGrpcService grpcAdapter;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        restAdapter = new OrderController(useCase);
        var grpcMapper = new GrpcMapper();
        grpcAdapter = new OrderGrpcService(useCase, grpcMapper);
    }

    @ParameterizedTest
    @MethodSource("allPrimaryAdapters")
    void all_adapters_produce_same_order_result(String label, CreateOrderCommand command) {
        var expectedResult = new OrderCreatedResult(
            OrderId.of("ORD-001"), OrderStatus.CREATED, Money.of(99.99), Instant.now());
        when(useCase.execute(command)).thenReturn(expectedResult);

        // 验证所有入口都返回一致的 UseCase 执行结果
        // REST、gRPC、CLI 只是协议转换层，业务结果完全一致
        var restResponse = restAdapter.create(new CreateOrderRequest(command));
        assertEquals(201, restResponse.getStatusCodeValue());

        // 验证 UseCase 被每个入口正确调用
        verify(useCase, times(1)).execute(command);
    }
}
```

## 验证清单：端口可替换性确认

| 检查项 | REST | gRPC | CLI | 说明 |
|--------|:----:|:----:|:---:|------|
| UseCase 接口零修改 | ✅ | ✅ | ✅ | 所有入口调用同一个 `CreateOrderUseCase` |
| 业务逻辑零修改 | ✅ | ✅ | ✅ | `CreateOrderServiceImpl` 不变 |
| 新增入口无需改现有代码 | ✅ | ✅ | ✅ | 各自实现协议转换即可 |
| 领域层测试零修改 | ✅ | ✅ | ✅ | `OrderTest` 不受入口影响 |
| 应用层测试零修改 | ✅ | ✅ | ✅ | `CreateOrderServiceImplTest` 用 Mock |
| 适配器测试各自独立 | ✅ | ✅ | ✅ | 只测协议映射不测业务逻辑 |

## 核心结论

> **主适配器可替换性证明了六边形边界正确**: 所有入口只做协议转换，业务逻辑完全隔离在 Domain 和 Application 层。新增 gRPC 或 CLI 入口时，Domain 和 Application 代码零修改——这是六边形架构的对称性验证。
