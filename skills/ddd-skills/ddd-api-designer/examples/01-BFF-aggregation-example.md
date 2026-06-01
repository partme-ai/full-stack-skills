# BFF 聚合案例：订单详情页

> 演示 BFF 层如何将多个微服务的数据聚合到一个页面专用的 VO。

## 场景

**订单详情页**需要展示以下数据：

```
┌─ 订单详情页 ──────────────────────────────────────────┐
│                                                        │
│  订单信息: #ORD-2024-001                               │
│  状态: 已支付  |  金额: ¥99.00                         │
│                                                        │
│  ├─ 商品清单:                                          │
│  │  1. T-Shirt × 2 — ¥49.50/件                        │
│  │  2. 牛仔裤 × 1 — ¥199.00/件                        │
│  │                                                        │
│  ├─ 支付信息:                                          │
│  │  支付方式: 微信支付                                 │
│  │  支付时间: 2024-01-15 10:30                         │
│  │                                                        │
│  ├─ 物流信息:                                          │
│  │  快递单号: SF-1234567890                            │
│  │  预计送达: 2024-01-20                               │
│  │                                                        │
│  └─ 操作按钮: [取消订单] [申请退款] [查看物流]          │
└────────────────────────────────────────────────────────┘
```

## 无 BFF 的痛点

```
前端需要调用 4 个不同的 API：
  1. GET /api/v1/orders/{id}             → Order Service
  2. GET /api/v1/orders/{id}/items       → Order Service (or nested)
  3. GET /api/v1/payments/order/{id}     → Payment Service
  4. GET /api/v1/shipping/order/{id}     → Shipping Service

问题：
  - 4 次 HTTP 调用，延迟叠加
  - 前端需要处理部分失败（某个服务挂了）
  - 前端需要自己组合数据
  - 每个页面都重复这种组合逻辑
```

## BFF 聚合方案

### BFF 端点

```
GET /api/web-bff/order-detail/{orderId}
```

### BFF 内部调用链

```
BFF OrderDetailService
  │
  ├── (并行) → Order Service (gRPC)     → OrderDetailDO
  │               getOrder(orderId)
  │
  ├── (并行) → Payment Service (gRPC)   → PaymentDTO
  │               getPaymentByOrder(orderId)
  │
  ├── (并行) → Shipping Service (gRPC)  → ShippingDTO
  │               getShippingByOrder(orderId)
  │
  └── 组装 → OrderDetailVO (返回给前端)
```

### BFF 服务实现

```java
@Service
public class OrderDetailBffService {

    private final OrderServiceClient orderClient;
    private final PaymentServiceClient paymentClient;
    private final ShippingServiceClient shippingClient;

    public OrderDetailVO getOrderDetail(String orderId) {
        // 并行调用三个微服务
        CompletableFuture<OrderDetailDO> orderFuture =
            CompletableFuture.supplyAsync(() -> orderClient.getOrder(orderId));
        CompletableFuture<PaymentDTO> paymentFuture =
            CompletableFuture.supplyAsync(() -> paymentClient.getPaymentByOrder(orderId));
        CompletableFuture<ShippingDTO> shippingFuture =
            CompletableFuture.supplyAsync(() -> shippingClient.getShippingByOrder(orderId));

        // 等待所有调用完成（带超时）
        CompletableFuture.allOf(orderFuture, paymentFuture, shippingFuture)
            .get(3, TimeUnit.SECONDS);

        // 组装 VO
        OrderDetailDO order = orderFuture.get();
        PaymentDTO payment = paymentFuture.get();      // 可能为 null（未支付）
        ShippingDTO shipping = shippingFuture.get();    // 可能为 null（未发货）

        return OrderDetailVO.builder()
            .orderId(order.getOrderId())
            .status(order.getStatus())
            .statusText(getStatusText(order.getStatus()))
            .totalAmount(order.getTotalAmount())
            .items(order.getItems().stream()
                .map(this::toItemVO)
                .toList())
            .payment(payment != null ? toPaymentVO(payment) : null)
            .shipping(shipping != null ? toShippingVO(shipping) : null)
            .actions(determineActions(order.getStatus()))
            .build();
    }

    private List<String> determineActions(OrderStatus status) {
        return switch (status) {
            case DRAFT -> List.of("pay", "cancel");
            case PAID -> List.of("cancel", "apply_refund");
            case SHIPPED -> List.of("track", "confirm_receipt");
            case DELIVERED -> List.of("review", "apply_return");
            case CANCELLED -> List.of("reorder");
        };
    }
}
```

### BFF VO 定义

```json
// BFF 返回的前端 VO
GET /api/web-bff/order-detail/ORD-2024-001 → 200

{
  "code": 0,
  "message": "success",
  "data": {
    "orderId": "ORD-2024-001",
    "status": "PAID",
    "statusText": "已支付",
    "totalAmount": "¥298.00",

    "items": [
      { "productName": "T-Shirt", "imageUrl": "https://cdn.com/tshirt.jpg",
        "quantity": 2, "unitPrice": "¥49.50", "subtotal": "¥99.00" },
      { "productName": "牛仔裤", "imageUrl": "https://cdn.com/jeans.jpg",
        "quantity": 1, "unitPrice": "¥199.00", "subtotal": "¥199.00" }
    ],

    "payment": {
      "method": "微信支付",
      "amount": "¥298.00",
      "paidAt": "2024-01-15T10:30:00"
    },

    "shipping": null,

    "actions": ["cancel", "apply_refund"],
    "createdAt": "2024-01-15T10:30:00",

    "ui": {
      "pageTitle": "订单详情",
      "primaryAction": "取消订单",
      "primaryActionColor": "red"
    }
  }
}
```

## 部分失败处理

```java
public OrderDetailVO getOrderDetailSafe(String orderId) {
    OrderDetailDO order = null;
    PaymentDTO payment = null;
    ShippingDTO shipping = null;
    List<String> warnings = new ArrayList<>();

    try {
        order = orderClient.getOrder(orderId);
    } catch (Exception e) {
        // Order service is critical — fail the whole request
        throw new BffException("订单服务暂时不可用", e);
    }

    try {
        payment = paymentClient.getPaymentByOrder(orderId);
    } catch (Exception e) {
        warnings.add("支付信息暂时不可用");
    }

    try {
        shipping = shippingClient.getShippingByOrder(orderId);
    } catch (Exception e) {
        warnings.add("物流信息暂时不可用");
    }

    OrderDetailVO vo = assembleVO(order, payment, shipping);
    vo.setWarnings(warnings);
    return vo;
}
```

## BFF 响应超时策略

| 策略 | 实现 | 适用场景 |
|------|------|---------|
| Wait All | `CompletableFuture.allOf().get(timeout)` | 核心数据 |
| Wait Fast | 先返回已就绪的数据，慢的异步补充 | 非关键数据 |
| Fallback | 下游超时时返回默认值 | 可选数据 |
| Circuit Break | 下游连续失败后快速失败 | 防止雪崩 |
