# L1 模型分离完整示例 — Order 聚合

> 所属级别: L1（模型分离） | 共享同一数据库 | 代码层读写分离

## 业务场景

用户下单 → 创建订单 → 查询订单列表 / 订单详情

## 目录结构

```
com/example/order/
├── command/
│   ├── CreateOrderCommand.java
│   ├── OrderCommandService.java
│   └── OrderCreatedResult.java
├── query/
│   ├── OrderQuery.java
│   ├── OrderQueryService.java
│   ├── OrderDetailDTO.java
│   └── OrderSummaryDTO.java
├── domain/
│   ├── Order.java                  # 聚合根
│   ├── OrderStatus.java            # 值对象
│   ├── OrderId.java                # 值对象
│   └── OrderRepository.java        # 仓储接口
├── infrastructure/
│   └── OrderRepositoryImpl.java    # 仓储实现（共享）
└── controller/
    ├── OrderCommandController.java
    └── OrderQueryController.java
```

## 写侧代码

### Command 对象

```java
public class CreateOrderCommand {
    private final String customerId;
    private final List<OrderItemCommand> items;

    // constructor, getters — immutable
}

public class OrderItemCommand {
    private final String productId;
    private final int quantity;
}
```

### Command Service

```java
@Service
public class OrderCommandService {
    private final OrderRepository orderRepository;

    @Transactional
    public OrderCreatedResult createOrder(CreateOrderCommand command) {
        Order order = Order.create(command);
        orderRepository.save(order);
        return OrderCreatedResult.from(order);
    }
}
```

### 聚合根

```java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private OrderStatus status;
    private List<OrderItem> items;
    private CustomerId customerId;

    public static Order create(CreateOrderCommand command) {
        Order order = new Order();
        order.id = new OrderId(UUID.randomUUID().toString());
        order.status = OrderStatus.CREATED;
        order.items = command.getItems().stream()
            .map(OrderItem::fromCommand)
            .toList();
        order.customerId = new CustomerId(command.getCustomerId());
        order.addDomainEvent(new OrderCreatedEvent(order.id));
        return order;
    }
}
```

## 读侧代码

### Query 对象

```java
public class OrderQuery {
    private final String customerId;
    private final OrderStatus status;
    private final LocalDate startDate;
    private final LocalDate endDate;
}
```

### Query Service

```java
@Service
public class OrderQueryService {
    private final OrderRepository orderRepository;

    public OrderDetailDTO getOrderDetail(OrderId id) {
        Order order = orderRepository.findById(id)
            .orElseThrow(() -> new OrderNotFoundException(id));
        return OrderDetailDTO.from(order);
    }

    public Page<OrderSummaryDTO> listOrders(OrderQuery query, Pageable pageable) {
        return orderRepository.findByCriteria(query, pageable);
    }
}
```

### DTO

```java
public class OrderDetailDTO {
    private String orderId;
    private String status;
    private String customerName;
    private List<OrderItemDTO> items;
    private BigDecimal totalAmount;
    private LocalDateTime createdAt;

    public static OrderDetailDTO from(Order order) {
        OrderDetailDTO dto = new OrderDetailDTO();
        dto.orderId = order.getId().getValue();
        dto.status = order.getStatus().name();
        dto.items = order.getItems().stream()
            .map(OrderItemDTO::from)
            .toList();
        dto.createdAt = order.getCreatedAt();
        return dto;
    }
}
```

## 控制器

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderCommandController {
    private final OrderCommandService commandService;

    @PostMapping
    public ResponseEntity<OrderCreatedResult> createOrder(
            @RequestBody CreateOrderCommand command) {
        OrderCreatedResult result = commandService.createOrder(command);
        return ResponseEntity.status(201).body(result);
    }
}

@RestController
@RequestMapping("/api/v1/orders")
public class OrderQueryController {
    private final OrderQueryService queryService;

    @GetMapping("/{id}")
    public ResponseEntity<OrderDetailDTO> getOrder(@PathVariable String id) {
        OrderDetailDTO dto = queryService.getOrderDetail(new OrderId(id));
        return ResponseEntity.ok(dto);
    }

    @GetMapping
    public ResponseEntity<Page<OrderSummaryDTO>> listOrders(OrderQuery query, Pageable pageable) {
        return ResponseEntity.ok(queryService.listOrders(query, pageable));
    }
}
```

## 适用场景

- 读写逻辑已有明显差异，但数据库结构一致
- 最小化架构改动，快速验证 CQRS 价值
- 团队首次引入 CQRS，逐步过渡
