# CQRS API Design Pattern

## Core Principle

CQRS (Command Query Responsibility Segregation) separates write operations from read operations at the API level. This is distinct from CQRS at the architecture level — API-level CQRS focuses on endpoint design, request/response structure, and DTO separation.

## Endpoint Patterns

### Command Endpoints (Write)

Commands represent **intent** — they change system state.

```
POST   /api/v1/orders                    → CreateOrderCommand
PUT    /api/v1/orders/{id}/confirm        → ConfirmOrderCommand
PUT    /api/v1/orders/{id}/ship           → ShipOrderCommand
DELETE /api/v1/orders/{id}                → CancelOrderCommand
```

**Characteristics:**
- Non-idempotent operations use POST
- Idempotent operations use PUT with idempotency key
- Response contains the created/modified resource summary
- Always validate business rules before applying changes

### Query Endpoints (Read)

Queries represent **questions** — they return system state without side effects.

```
GET    /api/v1/orders/{id}                → OrderDetailDTO
GET    /api/v1/orders?status=PAID&page=1  → OrderSummaryDTO[]
GET    /api/v1/orders/{id}/items          → OrderItemDTO[]
```

**Characteristics:**
- Always idempotent and safe (no side effects)
- Can be cached aggressively
- Response structure may differ significantly from command response
- Can use materialized views or read models

## DTO Separation Rules

| Aspect | Command DTO | Query DTO |
|--------|-------------|-----------|
| Naming | `CreateOrderRequest` | `OrderDetailDTO` |
| Direction | Input (request body) | Output (response body) |
| Fields | What's needed to execute the command | What's needed to display |
| Validation | Business rules + format | None (read-only) |
| Mutability | May be mutable | Immutable |

## Idempotency for Command APIs

```yaml
POST /api/v1/orders
Headers:
  Idempotency-Key: uuid-v4-unique-key

# If first request → 201 Created
# If retry with same key → 200 OK (same resource, no duplicate)
# If different key for same data → 409 Conflict (idempotency check)
```

Implementation:
1. Client generates UUID as idempotency key
2. Server stores `(key, result)` in cache with TTL
3. On duplicate key → return cached result
4. Cache TTL must exceed max retry window (recommended: 24h)

## Materialized View Pattern

For query performance, maintain dedicated read models:

```
┌─────────────┐     Domain Events     ┌─────────────┐
│ Command DB  │ ─────────────────────→ │  Read Model  │
│ (normalized)│                        │ (denormalized)│
└─────────────┘                        └─────────────┘
      │                                      │
      ▼                                      ▼
  Order Aggregate                     OrderDetailMV (flat JSON)
  ├── Order (root)                    ├── id, status, total
  ├── Items[]                        ├── customerName, email
  ├── Payment                        ├── items[ {name, qty, price} ]
  └── Customer (ID ref)              ├── paymentMethod, paidAt
                                      └── shippingAddress, status
```

The Read Model is updated asynchronously via domain events, allowing query-optimized structures independent of the domain model.
