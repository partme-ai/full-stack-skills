# Primary Adapters — 主适配器（驱动侧）

## 概述

主适配器（Primary/Driving Adapter）位于六边形左侧，负责将外部输入（HTTP 请求、CLI 命令、MQ 消息等）转换为对入站端口（UseCase）的调用。主适配器仅做协议转换，不包含业务逻辑。

## 核心职责

1. **协议转换** — 将外部协议（HTTP/CLI/MQ/gRPC）转换为 Java 方法调用
2. **参数校验** — 格式校验（非业务校验）
3. **响应格式化** — 将 UseCase 返回结果转换为外部格式
4. **异常映射** — 将领域异常转换为 HTTP 状态码等

## REST Controller

```java
// adapter/inbound/web/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final CreateOrderUseCase createOrder;
    private final GetOrderUseCase getOrder;
    private final PayOrderUseCase payOrder;

    public OrderController(
            CreateOrderUseCase createOrder,
            GetOrderUseCase getOrder,
            PayOrderUseCase payOrder) {
        this.createOrder = createOrder;
        this.getOrder = getOrder;
        this.payOrder = payOrder;
    }

    @PostMapping
    public ResponseEntity<CreateOrderResponse> create(@RequestBody @Valid CreateOrderRequest request) {
        var cmd = request.toCommand();
        var result = createOrder.execute(cmd);
        return ResponseEntity.status(201).body(CreateOrderResponse.from(result));
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderDTO> get(@PathVariable String id) {
        var query = new GetOrderQuery(id);
        var order = getOrder.execute(query);
        if (order == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(order);
    }

    @PostMapping("/{id}/pay")
    public ResponseEntity<PaymentResponse> pay(@PathVariable String id, @RequestBody @Valid PayOrderRequest request) {
        var cmd = new PayOrderCommand(id, request.getPaymentMethod());
        var result = payOrder.execute(cmd);
        return ResponseEntity.ok(PaymentResponse.from(result));
    }
}
```

## CLI Command

```java
// adapter/inbound/cli/OrderCommand.java
@Component
@CommandLineRunner
public class OrderCommand implements CommandLineRunner {
    private final CreateOrderUseCase createOrder;

    @Override
    public void run(String... args) {
        if (args.length < 3 || !"create-order".equals(args[0])) return;
        var cmd = new CreateOrderCommand(args[1], parseItems(args[2]));
        var result = createOrder.execute(cmd);
        System.out.printf("Order created: %s%n", result.getOrderId());
    }
}
```

## gRPC Service

```java
// adapter/inbound/grpc/OrderGrpcService.java
public class OrderGrpcService extends OrderServiceGrpc.OrderServiceImplBase {
    private final CreateOrderUseCase createOrder;

    @Override
    public void createOrder(CreateOrderRequest request, StreamObserver<CreateOrderResponse> responseObserver) {
        var cmd = CreateOrderCommand.fromProto(request);
        var result = createOrder.execute(cmd);
        var response = CreateOrderResponse.newBuilder()
                .setOrderId(result.getOrderId())
                .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
```

## Message Consumer

```java
// adapter/inbound/messaging/OrderMessageConsumer.java
@Component
public class OrderMessageConsumer {
    private final CreateOrderUseCase createOrder;

    @KafkaListener(topics = "order-commands")
    public void handleOrderCommand(OrderCommandMessage message) {
        var cmd = message.toCommand();
        createOrder.execute(cmd);
    }
}
```

## 主适配器开发规范

### ✅ 主适配器可以做的事
- 参数格式校验（@Valid、JSR-303）
- 请求/响应的序列化/反序列化
- 调用 UseCase 并返回结果
- 技术异常的统一处理（@ExceptionHandler）
- 认证鉴权的拦截（Filter/Interceptor）

### ❌ 主适配器不能做的事
- 包含业务 if/else 判断
- 直接操作数据库或 Repository
- 包含领域逻辑（价格计算、状态校验等）
- 依赖基础设施框架的特定注解进行业务操作

## 多入口适配器对比

| 入口类型 | 技术 | 适配器类 | 端口调用 |
|---------|------|---------|---------|
| REST API | Spring Web | `OrderController` | `CreateOrderUseCase` |
| CLI | CommandLineRunner | `OrderCommand` | `CreateOrderUseCase` |
| gRPC | gRPC | `OrderGrpcService` | `CreateOrderUseCase` |
| MQ Consumer | Kafka/RabbitMQ | `OrderMessageConsumer` | `CreateOrderUseCase` |
| Scheduled Task | @Scheduled | `OrderScheduledTask` | `CreateOrderUseCase` |
| GraphQL | graphql-java | `OrderGraphQLResolver` | `CreateOrderUseCase` |

> 同一入站端口可以被多个主适配器调用——这正是六边形架构的「多入口」核心价值。
