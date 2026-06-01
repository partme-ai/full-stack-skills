# Example 03 — 多入口系统示例（REST + MQ + CLI）

> 洋葱架构最适合多入口系统——同一领域核心被多种适配器共享，Domain 层完全不受入口类型影响。

## 业务描述

一个订单处理系统，支持三种入口：
- **REST API** — 前端用户操作
- **MQ Consumer** — 第三方系统通过消息创建订单
- **CLI 批处理** — 每日自动取消超时未支付订单

## 架构示意图

```
                  ┌───────────────┐
  REST ──────────▶│  API Layer    │
                  │  Controller   │
                  └───────┬───────┘
                          │
                  ┌───────▼───────┐          ┌─────────────────────┐
  MQ ────────────▶│  Application  │          │  Infrastructure      │
                  │  Layer        │◀────────▶│  ┌────────────────┐  │
                  │  Service      │          │  │  Repository     │  │
                  └───────┬───────┘          │  │  EventPublisher │  │
                          │                  │  │  External API   │  │
                  ┌───────▼───────┐          │  └────────────────┘  │
  CLI ────────────▶│  Domain  ★    │          └─────────────────────┘
                  │  Core         │
                  │  (纯业务逻辑)   │
                  └───────────────┘
```

## Domain 层（完全不受入口影响）

```java
// core/domain/model/order/Order.java
public class Order extends AggregateRoot<OrderId> {
    // 与前例相同，Domain 层对入口方式零感知
    // ... 业务方法不变
}

// core/domain/service/OrderTimeoutService.java
public class OrderTimeoutService {
    private final OrderRepository orderRepository;

    public OrderTimeoutService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    /**
     * 取消所有超时未支付订单（供 CLI 和 定时任务调用）
     */
    public int cancelTimeoutOrders(Duration timeout) {
        LocalDateTime deadline = LocalDateTime.now().minus(timeout);
        List<Order> timeoutOrders = orderRepository.findSubmittedBefore(deadline);
        for (Order order : timeoutOrders) {
            order.cancel();
            orderRepository.save(order);
        }
        return timeoutOrders.size();
    }
}
```

## Application 层

```java
// core/application/service/OrderCommandService.java
public interface OrderCommandService {
    OrderDTO createOrderFromREST(CreateOrderCommand command);
    OrderDTO createOrderFromMQ(MQCreateOrderCommand command);
    int cancelTimeoutOrders();
}

// 注意：无论来自 REST 还是 MQ，最终都调用相同的 Domain 方法
// 区别仅在于 Command 对象和校验逻辑不同
public class OrderCommandServiceImpl implements OrderCommandService {
    private final OrderRepository orderRepository;
    private final OrderTimeoutService timeoutService;
    private final EventPublisher eventPublisher;
    private final OrderDTOAssembler assembler;

    @Override
    @Transactional
    public OrderDTO createOrderFromREST(CreateOrderCommand command) {
        // REST 入口：标准校验
        validateCustomer(command.getCustomerId());
        return doCreateOrder(command.getCustomerId(), command.getItems());
    }

    @Override
    @Transactional
    public OrderDTO createOrderFromMQ(MQCreateOrderCommand command) {
        // MQ 入口：MQ 特有校验（幂等性、重试检测）
        if (isDuplicateMQMessage(command.getMessageId())) {
            return getExistingOrder(command.getOrderId());
        }
        return doCreateOrder(command.getCustomerId(), command.getItems());
    }

    @Override
    @Transactional
    public int cancelTimeoutOrders() {
        return timeoutService.cancelTimeoutOrders(Duration.ofHours(2));
    }

    // 共享的核心创建逻辑
    private OrderDTO doCreateOrder(String customerId, List<Item> items) {
        Order order = Order.create(OrderId.generate(), new CustomerId(customerId));
        items.forEach(item -> order.addItem(
            new ProductId(item.getProductId()),
            Money.of(item.getUnitPrice(), "CNY"),
            item.getQuantity()
        ));
        order.submit();
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
        return assembler.toDTO(order);
    }
}
```

## 入口 1：REST API 适配器

```java
// api/controller/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final OrderCommandService orderCommandService;

    @PostMapping
    public ResponseEntity<ApiResponse<OrderResponse>> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {
        CreateOrderCommand command = /* 转换 */;
        OrderDTO dto = orderCommandService.createOrderFromREST(command);
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(ApiResponse.success(/* 转换 */));
    }
}
```

## 入口 2：MQ 消费者适配器

```java
// api/consumer/OrderMessageConsumer.java
@Component
public class OrderMessageConsumer {
    private final OrderCommandService orderCommandService;

    @KafkaListener(topics = "order-commands")
    public void onOrderMessage(ConsumerRecord<String, MQCreateOrderCommand> record) {
        try {
            MQCreateOrderCommand command = record.value();
            OrderDTO dto = orderCommandService.createOrderFromMQ(command);
            log.info("MQ 订单创建成功: {}", dto.getOrderId());
        } catch (Exception e) {
            log.error("MQ 订单处理失败", e);
            // 发到 DLQ，后续补偿
        }
    }
}
```

## 入口 3：CLI / 定时任务适配器

```java
// api/job/OrderTimeoutJob.java
@Component
public class OrderTimeoutJob {
    private final OrderCommandService orderCommandService;

    @Scheduled(cron = "0 0 2 * * ?") // 每天凌晨 2 点
    public void cancelTimeoutOrders() {
        int cancelled = orderCommandService.cancelTimeoutOrders();
        log.info("定时取消超时订单: {} 个", cancelled);
    }
}

// api/cli/CancelTimeoutCommand.java
@Component
public class CancelTimeoutCommand implements CommandLineRunner {
    private final OrderCommandService orderCommandService;

    @Override
    public void run(String... args) {
        if (args.length > 0 && "cancel-timeout".equals(args[0])) {
            int count = orderCommandService.cancelTimeoutOrders();
            System.out.println("已取消 " + count + " 个超时订单");
        }
    }
}
```

## 关键设计点

1. **Domain 层零感知**：`Order` 和 `OrderTimeoutService` 完全不知道自己是 REST/MQ/CLI 调用的
2. **Application 层一视同仁**：`OrderCommandService` 为所有入口服务，入口特有逻辑（幂等、校验）在各适配器
3. **新增入口零成本**：加 gRPC？只需新增一个 `GrpcOrderService`，Domain/Application 层完全不动
4. **每个适配器只关心协议转换**：不做业务判断
