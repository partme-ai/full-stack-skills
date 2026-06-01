# BFF (Backend for Frontend) Design Pattern

## What is BFF?

BFF is a dedicated backend layer for each frontend application. Instead of having one API serving all clients, each platform (Web, iOS, Android, MiniApp) has its own backend that tailors data and behavior specifically for that platform.

## When to Use BFF

| Scenario | Use BFF? |
|----------|----------|
| Single web app only | No — API Gateway is sufficient |
| Web + Mobile App | Yes — different data needs |
| Web + MiniApp + WeChat | Yes — platform-specific formats |
| Multiple frontend teams | Yes — independent evolution |
| Public API for third-party | Public API → API Gateway, not BFF |

## BFF Responsibilities in Detail

### 1. Data Aggregation

```
Without BFF:
  Frontend → /api/orders/{id}        → Order detail (needs 3 calls)
           → /api/payments/{orderId} → Payment info
           → /api/shipping/{orderId} → Shipping status
  Result: 3 HTTP calls, client-side aggregation

With BFF:
  Frontend → /api/web-bff/order-detail/{id}  → Single response
  BFF internally calls:
    → Order Service   → OrderDO
    → Payment Service → PaymentDTO
    → Shipping Service → ShippingDTO
  BFF combines them into OrderDetailVO
  Result: 1 HTTP call, server-side aggregation
```

### 2. Format Adaptation

```json
// Web BFF response (rich, full data)
{
  "orderId": "ORD-2024-001",
  "status": "PAID",
  "totalAmount": "99.00",
  "items": [
    { "name": "T-Shirt", "imageUrl": "https://cdn.example.com/tshirt.jpg",
      "description": "Premium cotton T-Shirt", "quantity": 2, "price": "49.50" }
  ],
  "customer": { "name": "张三", "email": "zhang@example.com" },
  "paymentMethod": "微信支付",
  "estimatedDelivery": "2024-01-20",
  "actions": ["cancel", "return"]
}

// Mobile BFF response (minimal, paginated)
{
  "orderId": "ORD-2024-001",
  "status": "PAID",
  "totalAmount": "99.00",
  "itemCount": 2,
  "estimatedDelivery": "2024-01-20",
  "action": "cancel"
}
```

### 3. Protocol Translation

```
Internal (gRPC/Protobuf):
  Order service proto:    Order { id uint64, status OrderStatus, ... }
  Payment service proto:  Payment { id uint64, amount Money, ... }

External (REST/JSON) via BFF:
  GET /api/web-bff/order-detail/{id}
  → JSON: { "orderId": "ORD-2024-001", "status": "PAID", ... }
```

## BFF Directory Structure (Hexagonal)

```
bff-web/
├── adapter/                    # BFF 适配器层
│   ├── inbound/                # 对外暴露的 REST 端点
│   │   ├── controller/
│   │   └── dto/                # 对外 VO（面向前端页面）
│   └── outbound/               # 调用下游服务的客户端
│       ├── order-service/      # gRPC/REST client → Order Service
│       ├── payment-service/    # gRPC/REST client → Payment Service
│       └── product-service/    # gRPC/REST client → Product Service
├── application/                # 聚合编排层
│   ├── service/                # 组合多个下游服务
│   └── assembler/              # 组装 VO
└── config/                     # 配置
```

## BFF Best Practices

1. **One BFF per frontend team**: Each team owns their BFF independently
2. **BFF is thin, not thick**: Aggregation only, no business logic
3. **No direct DB access**: BFF calls downstream services, never the database
4. **Handle partial failures**: If one downstream service fails, return partial data with error indicators
5. **Cache aggressively**: BFF responses are view-specific and cacheable by URL
6. **Separate deployments**: BFF and downstream services deploy independently

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| BFF contains business logic | Duplication across BFFs | Move to domain service |
| One BFF for all platforms | Single point of change | Create per-platform BFF |
| BFF calls BFF | Request chain, latency | Restructure orchestration |
| BFF accesses DB directly | Bypasses domain rules | Always go through services |
