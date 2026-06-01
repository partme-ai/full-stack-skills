# Example: 多入口系统示例

本示例展示六边形架构的核心优势之一：同一业务逻辑通过多种入口（REST + CLI + MQ + gRPC）访问，Domain 层代码零修改。

## 场景：订单查询系统

系统提供订单查询功能，支持：
- REST API（前端调用）
- CLI 命令（运维人员）
- Kafka Consumer（内部服务）
- gRPC（微服务间调用）

## 领域模型（零修改 — 所有入口共享）

```java
// domain/model/order/Order.java
public class Order extends AggregateRoot<OrderId> {
    // ... 与示例 01 完全相同的 Order 聚合
    // 不依赖任何 HTTP/CLI/MQ/gRPC 框架
}
```

## 入站端口（零修改 — 所有入口共享）

```java
// domain/port/inbound/GetOrderUseCase.java
public interface GetOrderUseCase {
    OrderDTO execute(GetOrderQuery query);
}

// domain/port/inbound/CreateOrderUseCase.java
public interface CreateOrderUseCase {
    OrderCreatedResult execute(CreateOrderCommand command);
}
```

## 应用服务（零修改 — 所有入口共享）

```java
// application/service/GetOrderService.java
@ApplicationService
public class GetOrderService implements GetOrderUseCase {
    private final OrderRepository orderRepository;
    private final OrderDTOAssembler assembler;

    public GetOrderService(OrderRepository orderRepository, OrderDTOAssembler assembler) {
        this.orderRepository = orderRepository;
        this.assembler = assembler;
    }

    @Override
    public OrderDTO execute(GetOrderQuery query) {
        return orderRepository.findById(new OrderId(query.getOrderId()))
                .map(assembler::toDTO)
                .orElse(null);
    }
}
```

## 入口 1: REST Controller

```java
// adapter/inbound/web/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final GetOrderUseCase getOrder;
    private final CreateOrderUseCase createOrder;

    @GetMapping("/{id}")
    public ResponseEntity<OrderDTO> get(@PathVariable String id) {
        var order = getOrder.execute(new GetOrderQuery(id));
        return order != null ? ResponseEntity.ok(order) : ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<CreateOrderResponse> create(@RequestBody @Valid CreateOrderRequest req) {
        var result = createOrder.execute(req.toCommand());
        return ResponseEntity.status(201).body(CreateOrderResponse.from(result));
    }
}
```

## 入口 2: CLI Command

```java
// adapter/inbound/cli/OrderCliCommand.java
@Component
public class OrderCliCommand implements CommandLineRunner {
    private final CreateOrderUseCase createOrder;
    private final GetOrderUseCase getOrder;

    public OrderCliCommand(CreateOrderUseCase createOrder, GetOrderUseCase getOrder) {
        this.createOrder = createOrder;
        this.getOrder = getOrder;
    }

    @Override
    public void run(String... args) {
        if (args.length == 0) return;

        switch (args[0]) {
            case "create-order" -> handleCreate(args);
            case "get-order" -> handleGet(args);
        }
    }

    private void handleCreate(String[] args) {
        // Usage: java -jar app.jar create-order cust-001 prod-001 2
        var cmd = new CreateOrderCommand(
                CustomerId.of(args[1]),
                List.of(new ItemCmd(ProductId.of(args[2]), Quantity.of(Integer.parseInt(args[3])))));
        var result = createOrder.execute(cmd);
        System.out.println("Order created: " + result.getOrderId());
    }

    private void handleGet(String[] args) {
        // Usage: java -jar app.jar get-order ORD-001
        var order = getOrder.execute(new GetOrderQuery(args[1]));
        if (order != null) {
            System.out.printf("Order %s: status=%s, amount=%s%n",
                    order.getOrderId(), order.getStatus(), order.getTotalAmount());
        } else {
            System.out.println("Order not found");
        }
    }
}
```

## 入口 3: Kafka Consumer

```java
// adapter/inbound/messaging/OrderCommandConsumer.java
@Component
public class OrderCommandConsumer {
    private final CreateOrderUseCase createOrder;
    private final ObjectMapper objectMapper;

    public OrderCommandConsumer(CreateOrderUseCase createOrder, ObjectMapper objectMapper) {
        this.createOrder = createOrder;
        this.objectMapper = objectMapper;
    }

    @KafkaListener(topics = "order-commands", groupId = "order-service")
    public void onMessage(ConsumerRecord<String, String> record) {
        try {
            var message = objectMapper.readValue(record.value(), OrderCommandMessage.class);
            var cmd = message.toCommand();
            createOrder.execute(cmd);
        } catch (Exception e) {
            throw new MessagingException("订单创建消息处理失败", e);
        }
    }
}
```

## 入口 4: gRPC Service

```java
// adapter/inbound/grpc/OrderGrpcService.java
import io.grpc.stub.StreamObserver;

public class OrderGrpcService extends OrderServiceGrpc.OrderServiceImplBase {
    private final GetOrderUseCase getOrder;
    private final CreateOrderUseCase createOrder;

    public OrderGrpcService(GetOrderUseCase getOrder, CreateOrderUseCase createOrder) {
        this.getOrder = getOrder;
        this.createOrder = createOrder;
    }

    @Override
    public void getOrder(GetOrderProtoRequest request,
                         StreamObserver<GetOrderProtoResponse> responseObserver) {
        var order = getOrder.execute(new GetOrderQuery(request.getOrderId()));
        if (order == null) {
            responseObserver.onError(Status.NOT_FOUND.asRuntimeException());
            return;
        }
        var response = GetOrderProtoResponse.newBuilder()
                .setOrderId(order.getOrderId())
                .setStatus(order.getStatus())
                .setTotalAmount(order.getTotalAmount())
                .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    @Override
    public void createOrder(CreateOrderProtoRequest request,
                            StreamObserver<CreateOrderProtoResponse> responseObserver) {
        var cmd = CreateOrderCommand.fromProto(request);
        var result = createOrder.execute(cmd);
        var response = CreateOrderProtoResponse.newBuilder()
                .setOrderId(result.getOrderId())
                .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
```

## DI 配置 — 装配所有入口

```java
// configuration/config/BeanConfig.java
@Configuration
public class BeanConfig {
    // ---- 端口实现 ----
    @Bean
    public OrderRepository orderRepository(/* ... */) { return new PostgresOrderRepository(/* ... */); }

    @Bean
    public PaymentGateway paymentGateway(/* ... */) { return new StripePaymentGateway(/* ... */); }

    @Bean
    public EventPublisher eventPublisher(/* ... */) { return new RabbitMQEventPublisher(/* ... */); }

    // ---- 应用服务 ----
    @Bean
    public GetOrderUseCase getOrderUseCase(OrderRepository repo) {
        return new GetOrderService(repo, new OrderDTOAssembler());
    }

    @Bean
    public CreateOrderUseCase createOrderUseCase(OrderRepository repo, ProductRepository productRepo,
                                                  EventPublisher eventPub) {
        return new CreateOrderService(repo, productRepo, eventPub);
    }

    // ---- 所有入口共享同一 UseCase 实例 ----
    // REST Controller:   注入 createOrderUseCase
    // CLI Command:       注入 createOrderUseCase
    // Kafka Consumer:    注入 createOrderUseCase
    // gRPC Service:      注入 createOrderUseCase
}
```

## 多入口测试

```java
// 应用服务测试（一次编写，覆盖所有入口）
@Test
void get_order_should_return_dto() {
    var orderRepo = mock(OrderRepository.class);
    var assembler = new OrderDTOAssembler();
    var service = new GetOrderService(orderRepo, assembler);
    var orderId = OrderId.generate();

    when(orderRepo.findById(orderId)).thenReturn(Optional.of(createTestOrder(orderId)));

    var result = service.execute(new GetOrderQuery(orderId.getValue()));

    assertNotNull(result);
    assertEquals(orderId.getValue(), result.getOrderId());
}
```

## 架构图

```
                    ┌─────────────────────────────────────────────────┐
                    │             入站适配器 (共享同一 UseCase)          │
                    │                                                   │
  HTTP  ──────────▶ │  OrderController     (Spring MVC)                │
  CLI   ──────────▶ │  OrderCliCommand     (CommandLineRunner)          │
  Kafka ──────────▶ │  OrderCommandConsumer (KafkaListener)             │──▶ CreateOrderUseCase (共享)
  gRPC  ──────────▶ │  OrderGrpcService    (gRPC)                      │
                    └─────────────────────────────────────────────────┘
                                                                       │
                                                    ┌──────────────────▼──────────────────┐
                                                    │        应用服务（仅一套）              │
                                                    │    CreateOrderService               │
                                                    │    GetOrderService (共享)            │
                                                    └──────────────────┬──────────────────┘
                                                                       │
                         ┌─────────────────────────────────────────────┼──────────────────────────────┐
                         │                                             │                              │
                    ┌────▼─────────┐                     ┌────────────▼──────────┐     ┌─────────────▼────┐
                    │  Postgres    │                     │  StripePayment        │     │  RabbitMQ          │
                    │  OrderRepo   │                     │  Gateway              │     │  EventPublisher    │
                    └──────────────┘                     └───────────────────────┘     └───────────────────┘
```

## 核心验证

> **验证方法**: 停止数据库、关闭 Kafka、不启动 HTTP 服务，通过 CLI 入口测试领域逻辑：
> ```
> java -jar app.jar create-order cust-001 prod-001 2
> Order created: ORD-A1B2C3D4
> ```
> 如果不用数据库和 HTTP 就能跑通核心流程，六边形边界就对了。
