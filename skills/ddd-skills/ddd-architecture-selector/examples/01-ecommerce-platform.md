# Case Study: E-Commerce Platform Architecture Selection

## Project Context

| Dimension | Detail |
|-----------|--------|
| **Team** | 12 developers (3 frontend, 7 backend, 2 QA) |
| **DDD Experience** | 2 members have DDD exposure, rest are beginners |
| **Business Complexity** | Moderate-High: order workflow, inventory, payment, promotion |
| **Tech Stack** | Spring Boot 3.x + MyBatis + MySQL + RocketMQ |
| **Infra Change Frequency** | Medium: potential DB migration, MQ upgrade planned |
| **Entry Points** | REST API (web + mobile), MQ events (inventory sync) |
| **Ecosystem** | Strong Chinese ecosystem preference |
| **CQRS Need** | Read/write disparity moderate (product search heavy) |

## Decision Process

### Step 1: Matrix Evaluation

```
Business Complexity: Moderate-High  → Hexagonal / Clean / COLA
Team Size: 12                       → All fit, but Clean too heavy for team DDD level
Tech Stack: Spring Boot + MyBatis   → COLA has best tooling support
Ecosystem: Chinese                   → COLA preferred
Entry Points: Multi (REST + MQ)     → Hexagonal also strong candidate
```

### Step 2: Decision Tree Result

Following the decision tree:
1. Business complexity: Moderate-High → not simple CRUD
2. Chinese ecosystem + Spring Boot + MyBatis → **COLA** primary recommendation
3. Multi-entry concern → adopt Hexagonal Port/Adapter pattern within COLA's structure (COLA's Adapter layer + Port interfaces)

### Step 3: CQRS Assessment

- Read/write disparity: Moderate (product search is heavy read)
- **Recommendation: CQRS L1** — Model Separation only
  - CommandService for writes (order creation, payment)
  - QueryService for reads (product search, order listing)
  - Shared database initially, can upgrade to L2 later

### Step 4: Domain Classification

| Domain | Type | Architecture | Priority |
|--------|------|-------------|----------|
| Order Management | Core | COLA (rich model) | P0 |
| Payment Processing | Core | COLA (rich model) | P0 |
| Inventory | Core | COLA (rich model) | P0 |
| Product Catalog | Core | COLA (rich model) | P0 |
| User Auth | Generic | Layered (shiro) | P2 |
| Notification | Generic | Off-the-shelf | P2 |
| Admin Reports | Supporting | Simple CRUD | P3 |

## Final Recommendation

```
Primary Architecture: COLA v5 (Multi-Module)
CQRS Level: L1 — Model Separation
Layering Strategy: Strict (with ArchUnit enforcement)

Module Structure:
  ├── order-adapter / order-app / order-domain / order-infrastructure
  ├── payment-adapter / payment-app / payment-domain / payment-infrastructure
  ├── inventory-adapter / inventory-app / inventory-domain / inventory-infrastructure
  ├── product-adapter / product-app / product-domain / product-infrastructure
  └── auth-adapter / auth-app (simplified — Generic domain)
```

## Rationale

1. **COLA** provides the best ecosystem fit for Spring Boot + MyBatis + Chinese team
2. **COLA's Adapter + Port pattern** naturally handles both REST and MQ entry points
3. **CQRS L1** enough for current stage — product search performance is adequate with indexing
4. **Generic/Supporting domains use simpler architectures** to avoid over-engineering
5. **Strict layering** enforced via ArchUnit in CI prevents domain corruption

## Next Steps

1. Proceed to [ddd-architecture-cola](../ddd-architecture-cola/) for implementation
2. Order BC as first implementation module (highest priority Core domain)
3. Set up ArchUnit dependency checks in CI pipeline
4. Revisit CQRS upgrade to L2 when product search becomes bottleneck
