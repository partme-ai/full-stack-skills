# Example 04 — CQRS + 洋葱架构融合示例

> 在洋葱架构中融入 CQRS 模式，实现 Application 层的读写分离。

## CQRS 集成点在洋葱中的位置

```
                Command Path                    Query Path
                ────────────                    ──────────
API Layer:  POST /orders                    GET /orders/{id}
                │                                  │
                ▼                                  ▼
Application:  OrderCommandService           OrderQueryService
  Layer:      (写操作：创建/支付/取消)         (读操作：查询详情/列表)
                │                                  │
                ▼                                  ▼
Domain       Domain 实体 + Repository 接口    (可能绕过 Domain，直接读)
  Layer:     (业务规则 + 不变式)               (查询不修改状态)
                │
                ▼
Infra:       OrderRepositoryImpl            OrderQueryRepositoryImpl
             (JPA 写库)                      (JPA 读库 / 物化视图)
```

## Domain 层（只处理 Command 写操作）

```java
// core/domain/model/order/Order.java
// 与 Example 01 相同 — Domain 层只处理写操作（Command）
// 查询不进入 Domain 层

// core/domain/repository/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
}
```

## Application 层：Command 写模型

```java
// core/application/command/OrderCommandService.java
public interface OrderCommandService {
    OrderDTO createOrder(CreateOrderCommand command);
    void payOrder(String orderId);
    void cancelOrder(String orderId);
}

// core/application/command/OrderCommandServiceImpl.java
public class OrderCommandServiceImpl implements OrderCommandService {
    private final OrderRepository orderRepository;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;
    private final OrderDTOAssembler assembler;

    @Override
    @Transactional
    public OrderDTO createOrder(CreateOrderCommand command) {
        Order order = Order.create(OrderId.generate(), new CustomerId(command.getCustomerId()));
        command.getItems().forEach(item ->
            order.addItem(new ProductId(item.getProductId()),
                Money.of(item.getUnitPrice(), "CNY"), item.getQuantity()));
        order.submit();
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
        return assembler.toDTO(order);
    }

    @Override
    @Transactional
    public void payOrder(String orderId) {
        Order order = orderRepository.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        order.pay(paymentGateway);
        orderRepository.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
    }
}
```

## Application 层：Query 读模型

```java
// core/application/query/OrderQueryService.java
public interface OrderQueryService {
    OrderDetailDTO getOrderDetail(String orderId);
    OrderListDTO listOrders(String customerId, int page, int size);
    OrderStatisticsDTO getOrderStatistics(LocalDate start, LocalDate end);
}

// core/application/query/OrderQueryServiceImpl.java
public class OrderQueryServiceImpl implements OrderQueryService {
    // 注意：这里注入的是查询专用的 Repository（可指向读库）
    private final OrderQueryRepository queryRepository;

    public OrderQueryServiceImpl(OrderQueryRepository queryRepository) {
        this.queryRepository = queryRepository;
    }

    @Override
    @Transactional(readOnly = true)
    public OrderDetailDTO getOrderDetail(String orderId) {
        return queryRepository.findDetailById(orderId)
            .orElseThrow(() -> new OrderNotFoundException(orderId));
    }

    @Override
    @Transactional(readOnly = true)
    public OrderListDTO listOrders(String customerId, int page, int size) {
        return queryRepository.findListByCustomer(customerId, page, size);
    }

    @Override
    @Transactional(readOnly = true)
    public OrderStatisticsDTO getOrderStatistics(LocalDate start, LocalDate end) {
        return queryRepository.getStatistics(start, end);
    }
}
```

## 查询 DTO（读模型专用，扁平化结构）

```java
// core/application/query/dto/OrderDetailDTO.java
@Data
public class OrderDetailDTO {
    private String orderId;
    private String customerId;
    private String customerName;       // 来自读模型（不经过 Domain 实体）
    private String status;
    private List<OrderItemDTO> items;
    private BigDecimal totalAmount;
    private String currency;
    private LocalDateTime createdAt;
    private LocalDateTime paidAt;

    @Data
    public static class OrderItemDTO {
        private String productId;
        private String productName;    // 读模型额外字段
        private BigDecimal unitPrice;
        private int quantity;
        private BigDecimal subtotal;
    }
}

// core/application/query/dto/OrderStatisticsDTO.java
@Data
public class OrderStatisticsDTO {
    private long totalOrders;
    private BigDecimal totalRevenue;
    private Map<String, Long> statusDistribution;
    private Map<String, BigDecimal> dailyRevenue;
}
```

## Infrastructure 层：查询 Repository

```java
// infrastructure/data/query/OrderQueryRepositoryImpl.java
@Repository
public class OrderQueryRepositoryImpl implements OrderQueryRepository {
    private final JdbcTemplate jdbcTemplate;
    private final ObjectMapper objectMapper;

    public OrderQueryRepositoryImpl(JdbcTemplate jdbcTemplate, ObjectMapper objectMapper) {
        this.jdbcTemplate = jdbcTemplate;
        this.objectMapper = objectMapper;
    }

    @Override
    public Optional<OrderDetailDTO> findDetailById(String orderId) {
        // 直接 SQL 查询，不经过 Domain 实体
        String sql = """
            SELECT o.*, c.name as customer_name,
                   json_agg(json_build_object(
                       'productId', oi.product_id,
                       'productName', p.name,
                       'unitPrice', oi.unit_price,
                       'quantity', oi.quantity,
                       'subtotal', oi.unit_price * oi.quantity
                   )) as items
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            LEFT JOIN order_items oi ON o.id = oi.order_id
            LEFT JOIN products p ON oi.product_id = p.id
            WHERE o.id = ?
            GROUP BY o.id, c.name
            """;
        return jdbcTemplate.query(sql, new Object[]{orderId}, rs -> {
            if (rs.next()) {
                return Optional.of(mapToDetailDTO(rs));
            }
            return Optional.empty();
        });
    }

    private OrderDetailDTO mapToDetailDTO(ResultSet rs) throws SQLException {
        OrderDetailDTO dto = new OrderDetailDTO();
        dto.setOrderId(rs.getString("id"));
        dto.setCustomerId(rs.getString("customer_id"));
        dto.setCustomerName(rs.getString("customer_name"));
        dto.setStatus(rs.getString("status"));
        dto.setTotalAmount(rs.getBigDecimal("total_amount"));
        dto.setCreatedAt(rs.getTimestamp("created_at").toLocalDateTime());
        // items 从 JSON 解析
        try {
            String itemsJson = rs.getString("items");
            if (itemsJson != null) {
                var items = objectMapper.readValue(itemsJson,
                    new TypeReference<List<OrderDetailDTO.OrderItemDTO>>() {});
                dto.setItems(items);
            }
        } catch (Exception e) {
            throw new RuntimeException("解析订单项失败", e);
        }
        return dto;
    }
}
```

## API 层：读写分离的 Controller

```java
// api/controller/OrderCommandController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderCommandController {
    private final OrderCommandService commandService;

    @PostMapping
    public ResponseEntity<ApiResponse<OrderResponse>> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {
        OrderDTO dto = commandService.createOrder(request.toCommand());
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(ApiResponse.success(OrderResponseAssembler.toResponse(dto)));
    }

    @PostMapping("/{orderId}/pay")
    public ResponseEntity<ApiResponse<Void>> payOrder(@PathVariable String orderId) {
        commandService.payOrder(orderId);
        return ResponseEntity.ok(ApiResponse.success(null));
    }
}

// api/controller/OrderQueryController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderQueryController {
    private final OrderQueryService queryService;

    @GetMapping("/{orderId}")
    public ResponseEntity<ApiResponse<OrderDetailResponse>> getOrderDetail(
            @PathVariable String orderId) {
        OrderDetailDTO dto = queryService.getOrderDetail(orderId);
        return ResponseEntity.ok(
            ApiResponse.success(OrderDetailResponseAssembler.toResponse(dto)));
    }

    @GetMapping
    public ResponseEntity<ApiResponse<OrderListResponse>> listOrders(
            @RequestParam String customerId,
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "20") int size) {
        OrderListDTO dto = queryService.listOrders(customerId, page, size);
        return ResponseEntity.ok(
            ApiResponse.success(OrderListResponseAssembler.toResponse(dto)));
    }

    @GetMapping("/statistics")
    public ResponseEntity<ApiResponse<OrderStatisticsResponse>> getStatistics(
            @RequestParam @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate start,
            @RequestParam @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate end) {
        OrderStatisticsDTO dto = queryService.getOrderStatistics(start, end);
        return ResponseEntity.ok(
            ApiResponse.success(OrderStatisticsResponseAssembler.toResponse(dto)));
    }
}
```

## 关键设计点

1. **读写分离**：`OrderCommandService`（写）和 `OrderQueryService`（读）是完全独立的服务
2. **读模型绕过 Domain**：查询直接使用 SQL/JPQL 映射到扁平 DTO，不实例化 Domain 实体
3. **查询 Repository 独立**：`OrderQueryRepository` 与 `OrderRepository` 是不同接口，可指向不同数据源
4. **统计查询优化**：`getOrderStatistics()` 直接聚合查询，不经过对象映射
5. **CQRS 级别**：本示例为 L1（模型分离，同一数据源），可扩展为 L2（物理分离数据库）
