# API Security Design for DDD APIs

## Security Architecture Overview

```
┌─ Request ─────────────────────────────────────────────┐
│                                                        │
│  1. Authentication (Who are you?)                      │
│     ├── JWT Bearer Token (standard)                    │
│     ├── OAuth2 / OpenID Connect (third-party)          │
│     └── API Key (service-to-service)                   │
│                                                        │
│  2. Rate Limiting (How much can you do?)               │
│     ├── Per-user rate limit                            │
│     └── Per-endpoint rate limit (cmd vs query)          │
│                                                        │
│  3. Authorization (What can you do?)                   │
│     ├── BC-level authorization                         │
│     └── Resource ownership check                       │
│                                                        │
│  4. Input Validation (What data is allowed?)           │
│     ├── Controller: format validation                  │
│     ├── Application: business validation               │
│     └── Domain: invariant validation                   │
│                                                        │
│  → Domain Service (after all checks pass)              │
└────────────────────────────────────────────────────────┘
```

## Layer 1: Authentication

### JWT Bearer Token

```yaml
# OpenAPI Security Scheme
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

# Protected endpoint
/api/v1/orders:
  post:
    security:
      - BearerAuth: []
```

**JWT Token Structure:**
```json
{
  "sub": "user-123",
  "roles": ["admin"],
  "bounded_contexts": ["order:write", "order:read", "payment:read"],
  "iat": 1700000000,
  "exp": 1700086400
}
```

### Service-to-Service: API Key

```yaml
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
```

Internal services authenticate via API key in header. Keys are rotated quarterly.

## Layer 2: Authorization

### Per-Bounded Context Authorization

Each bounded context has independent permissions:

```
User Token Claims:
  "bounded_contexts": [
    "order:write", "order:read",
    "payment:read",
    "product:read"
  ]

Order BC User → Can create/read orders, cannot modify payments
Payment BC User → Can read payment info, cannot create orders
```

### Resource Ownership Check

```java
public class OrderAuthorizationService {
    public void verifyOrderOwnership(String userId, OrderId orderId) {
        Order order = orderRepository.findById(orderId)
            .orElseThrow(() -> new ResourceNotFoundException("Order not found"));

        if (!order.getCustomerId().getValue().equals(userId)) {
            throw new ForbiddenException("You can only access your own orders");
        }
    }
}
```

## Layer 3: Input Validation

### Three-Level Validation

| Level | Location | What | Example |
|-------|----------|------|---------|
| **Format** | Controller | Field types, ranges, required | `@NotNull`, `@Min(1)`, `@Email` |
| **Business** | Application | Domain rules, state machine | "Can't pay cancelled order" |
| **Invariant** | Domain | Aggregate invariants | "Total must equal sum of items" |

### Controller Validation

```java
@PostMapping("/orders")
public Result<OrderResponse> createOrder(
    @Valid @RequestBody CreateOrderRequest request
) {
    // Controller: format validation via @Valid
    // Pass to application service for business validation
    OrderResponse response = orderAppService.createOrder(request.toCommand());
    return Result.success(response);
}

public record CreateOrderRequest(
    @NotNull Long customerId,
    @NotEmpty List<@Valid OrderItemRequest> items,
    @NotNull @Min(1) BigDecimal totalAmount
) {}
```

## Layer 4: Rate Limiting

### Command vs Query QPS

| Endpoint Type | Default QPS | Burst | Notes |
|---------------|-------------|-------|-------|
| Command (POST/PUT/DELETE) | 50/s | 100/s | Lower, prevent abuse |
| Query (GET) | 200/s | 500/s | Higher, can cache |
| Auth (login/register) | 10/s | 20/s | Lowest, brute-force protection |
| Public endpoints | 5/s | 10/s | Anonymous access |

### Implementation in API Gateway

```yaml
# Rate limiting per user
rate_limits:
  command:
    algorithm: token_bucket
    capacity: 50
    refill_rate: 50/s
  query:
    algorithm: token_bucket
    capacity: 200
    refill_rate: 200/s
```

## OpenAPI Security Examples

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  version: 1.0.0
paths:
  /api/v1/orders:
    post:
      summary: Create order
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
      responses:
        '201':
          description: Order created
  /api/v1/orders/{id}:
    get:
      summary: Get order detail
      security:
        - BearerAuth: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Order detail
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

## Security Checklist

- [ ] All endpoints require authentication (except health check)
- [ ] Command endpoints verify resource ownership
- [ ] Input validated at controller (format), application (business), domain (invariant)
- [ ] Command APIs have lower rate limits than query APIs
- [ ] Error responses never leak stack traces or internal details
- [ ] API keys rotated at least quarterly
- [ ] CORS configured per BFF domain
- [ ] SQL injection prevention (use parameterized queries)
- [ ] JWT tokens have short expiry (15 min access, 7 day refresh)
