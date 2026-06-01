# E-Commerce Domain Design Example

A complete worked example of DDD domain design for an e-commerce system.

## 1. Product Vision (Elevator Pitch)

> FOR online shoppers WHO want to buy products conveniently,
> OUR e-commerce platform IS an online marketplace
> THAT provides seamless ordering, payment, and delivery tracking.
> UNLIKE traditional retail, OUR product offers 24/7 availability and doorstep delivery.

## 2. Bounded Contexts

| Context | Type | Responsibility | Key Aggregates |
|---------|------|----------------|---------------|
| **Order** | Core | Order lifecycle management | Order |
| **Payment** | Core | Payment processing | Payment, Refund |
| **Product** | Supporting | Product catalog management | Product, Category |
| **Inventory** | Supporting | Stock management | Inventory, Warehouse |
| **Shipping** | Supporting | Logistics coordination | Shipment |
| **Customer** | Generic | Customer profile & auth | Customer |

## 3. Context Mapping

```
Order Context ←→ Payment Context   (Partnership)
Order Context ←→ Shipping Context  (Customer-Supplier: Order is upstream)
Order Context → Inventory Context  (Customer-Supplier: Order is upstream)
Order Context → Product Context    (Conformist: Order uses Product IDs)
Payment Context → External Gateway (Anti-Corruption Layer)
```

## 4. Aggregate: Order

### Aggregate Root
- **Order**
  - Identity: `OrderId` (value object, UUID)
  - State: `OrderStatus` (DRAFT → PAID → SHIPPING → DELIVERED → CANCELLED)

### Entities
- **OrderItem**: product reference, quantity, unit price, subtotal

### Value Objects
- `OrderId`: UUID-based identifier
- `Money`: amount + currency (immutable)
- `Address`: street, city, postal code, country
- `OrderStatus`: enum with state machine transitions
- `PhoneNumber`: validated phone format

### Invariants
1. `totalAmount` = sum of all `OrderItem.subtotal`
2. Status transitions: DRAFT→PAID→SHIPPING→DELIVERED (happy path)
3. Payment amount must match `totalAmount`
4. Order must have at least 1 OrderItem
5. Shipping address required before PAID→SHIPPING transition

### Domain Events
| Event | Trigger | Consumers |
|-------|---------|-----------|
| `OrderPlaced` | Order created | Inventory (reserve stock), Notification (email) |
| `OrderPaid` | Payment confirmed | Shipping (create shipment), Notification (SMS) |
| `OrderShipped` | Shipment dispatched | Notification (tracking info) |
| `OrderDelivered` | Delivery confirmed | Payment (release funds), Customer (review prompt) |
| `OrderCancelled` | Cancellation | Inventory (release stock), Payment (refund) |

### State Machine

```
DRAFT ──pay()──▶ PAID ──ship()──▶ SHIPPING ──deliver()──▶ DELIVERED
  │                │                  │
  └──cancel()──▶ CANCELLED ◀──cancel()─┘
```

## 5. Code Object Mapping

| Domain Object | Persistence (PO) | Transfer (DTO) | View (VO) |
|---------------|-----------------|----------------|-----------|
| Order | OrderPO | OrderDTO, OrderSummaryDTO | OrderDetailVO, OrderListVO |
| OrderItem | OrderItemPO | OrderItemDTO | OrderItemVO |
| Money | amount + currency columns | string "$99.00" | string "¥99.00" |
| Address | address JSONB column | AddressDTO | AddressVO |
| OrderId | VARCHAR(36) PK | String | String |

## 6. Persistence Strategy

| Object | Strategy | Implementation |
|--------|----------|---------------|
| Money | Inline columns | `DECIMAL(10,2) amount`, `VARCHAR(3) currency` |
| Address | JSON column | PostgreSQL `jsonb`, JPA @ColumnTransformer |
| OrderItem | Own table with FK | `order_items` table, cascade save/load |
| PhoneNumber | Single VARCHAR column | Validated on construction |

## 7. Microservice Splitting

```
Phase 1 (Monolith):
  All contexts in single deployment

Phase 2 (Split Core):
  Order + Payment → order-service
  Product + Inventory → product-service
  Shipping → shipping-service (new)

Phase 3 (Full Microservices):
  Each bounded context → independent service
  Shared: Customer context (Auth service)
```
