# 订单服务完整 API 设计案例

> 基于 DDD 订单聚合，完整展示 CQRS 分离、数据对象转换链、BFF 适配。

## 领域模型

```
Order (Aggregate Root)
├── OrderId (ValueObject)
├── OrderStatus: DRAFT → PAID → SHIPPED → DELIVERED
│                   ↘ CANCELLED
├── CustomerId (ValueObject) — 引用客户聚合
├── List<OrderItem> (Entity)
│   ├── OrderItemId
│   ├── ProductId — 引用商品聚合
│   ├── Quantity
│   └── UnitPrice
├── Money totalAmount (ValueObject)
└── List<DomainEvent>
```

## 1. CQRS 端点设计

### 命令端点（写）

```
POST   /api/v1/orders                    → 创建订单
PUT    /api/v1/orders/{orderId}/confirm   → 确认订单
PUT    /api/v1/orders/{orderId}/ship      → 标记发货
PUT    /api/v1/orders/{orderId}/deliver   → 标记送达
DELETE /api/v1/orders/{orderId}           → 取消订单
```

### 查询端点（读）

```
GET    /api/v1/orders/{orderId}           → 订单详情
GET    /api/v1/orders?status=PAID&page=1  → 订单列表
GET    /api/v1/orders/{orderId}/items     → 订单项列表
```

## 2. 数据对象转换链

```
PO (OrderPO) ↔ DO (Order) ↔ DTO (OrderDTO) ↔ VO (OrderDetailVO / OrderSummaryVO)
```

### PO — 基础设施层

```java
@Entity
@Table(name = "orders")
public class OrderPO {
    @Id
    private Long id;
    private String orderNo;
    private String status;       // 数据库存字符串
    private Long customerId;
    private BigDecimal totalAmount;
    private String currency;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private Integer version;     // 乐观锁
}
```

### DO — 领域层

```java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private OrderStatus status;
    private CustomerId customerId;
    private Money totalAmount;
    private List<OrderItem> items;

    public Order(OrderId id, CustomerId customerId, List<OrderItem> items) {
        this.id = id;
        this.customerId = customerId;
        this.items = Collections.unmodifiableList(items);
        this.status = OrderStatus.DRAFT;
        this.totalAmount = calculateTotal();
        addDomainEvent(new OrderCreatedEvent(id, customerId, totalAmount));
    }

    public void confirm() {
        if (!status.canConfirm()) {
            throw new BusinessException(40001, "订单状态不允许确认",
                "当前状态：" + status + "，可确认状态：DRAFT");
        }
        this.status = OrderStatus.CONFIRMED;
        addDomainEvent(new OrderConfirmedEvent(id));
    }

    private Money calculateTotal() {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }
}
```

### DTO — 接口层

```java
// 命令 DTO
public record CreateOrderRequest(
    @NotNull String customerId,
    @NotEmpty List<@Valid OrderItemRequest> items
) {
    public CreateOrderCommand toCommand() {
        return new CreateOrderCommand(
            CustomerId.of(this.customerId()),
            this.items().stream().map(OrderItemRequest::toItem).toList()
        );
    }
}

// 查询 DTO
public record OrderDetailDTO(
    String orderId,
    String status,
    String totalAmount,
    List<OrderItemDTO> items,
    String createdAt
) {}
```

### VO — 前端视图

```json
{
  "orderId": "ORD-2024-001",
  "status": "PAID",
  "statusText": "已支付",
  "totalAmount": "¥99.00",
  "items": [
    { "productName": "T-Shirt", "quantity": 2, "price": "¥49.50" }
  ],
  "actions": ["cancel", "apply_return"]
}
```

## 3. 转换器（Assembler）

```java
public class OrderAssembler {
    // DO → DTO (read direction)
    public static OrderDetailDTO toDetailDTO(Order order) {
        return new OrderDetailDTO(
            order.getId().getValue(),
            order.getStatus().name(),
            order.getTotalAmount().toString(),
            order.getItems().stream().map(OrderAssembler::toItemDTO).toList(),
            order.getCreatedAt().toString()
        );
    }

    public static OrderSummaryDTO toSummaryDTO(Order order) {
        return new OrderSummaryDTO(
            order.getId().getValue(),
            order.getStatus().name(),
            order.getTotalAmount().toString(),
            order.getItems().size()
        );
    }

    // Command → DO (write direction)
    public static Order toDomain(CreateOrderCommand command) {
        List<OrderItem> items = command.items().stream()
            .map(item -> new OrderItem(
                OrderItemId.generate(),
                ProductId.of(item.productId()),
                item.quantity(),
                item.unitPrice()
            )).toList();
        return new Order(OrderId.generate(), command.customerId(), items);
    }
}
```

## 4. 统一响应

```json
// 创建订单成功
POST /api/v1/orders → 201
{
  "code": 0,
  "message": "success",
  "data": {
    "orderId": "ORD-2024-001",
    "status": "DRAFT",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}

// 订单列表查询
GET /api/v1/orders?status=PAID&page=1 → 200
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [
      { "orderId": "ORD-2024-001", "status": "PAID", "totalAmount": "99.00", "itemCount": 2 }
    ],
    "total": 1,
    "page": 1,
    "pageSize": 20,
    "totalPages": 1
  }
}
```

## 5. OpenAPI 摘要

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  version: 1.0.0
servers:
  - url: https://api.example.com/api/v1
paths:
  /orders:
    post:
      tags: [Order Commands]
      summary: Create order
      requestBody:
        $ref: '#/components/schemas/CreateOrderRequest'
      responses:
        '201': { $ref: '#/components/schemas/OrderCreatedResponse' }
    get:
      tags: [Order Queries]
      summary: List orders
      parameters:
        - name: status
          in: query
          schema: { type: string }
      responses:
        '200': { $ref: '#/components/schemas/OrderListResponse' }
```
