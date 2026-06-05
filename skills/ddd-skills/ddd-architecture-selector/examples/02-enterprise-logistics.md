# Case Study: Enterprise Logistics Platform Architecture Selection

## Project Context

| Dimension | Detail |
|-----------|--------|
| **Team** | 45 developers (7 squads: routing, tracking, dispatch, billing, warehouse, analytics, integration) |
| **DDD Experience** | High — core team of 12 with multiple DDD projects |
| **Business Complexity** | Very High: real-time routing optimization, multi-carrier integration, SLA management |
| **Tech Stack** | Java 21 + Spring Boot + MongoDB + PostgreSQL + Kafka + Redis |
| **Infra Change Frequency** | High: carriers change API frequently (50+ carrier integrations) |
| **Entry Points** | REST API + WebSocket (real-time tracking) + MQ events + Batch processing + Scheduled jobs |
| **Ecosystem** | International + Chinese (multi-region deployment) |
| **CQRS Need** | Very High — tracking reads 1000:1 vs writes, analytics runs complex aggregations |

## Decision Process

### Step 1: Matrix Evaluation

```
Business Complexity: Very High        → Hexagonal / Clean / COLA all valid
Team Size: 45 (7 squads)              → Clean for strict isolation, Hexagonal per squad flexibility
Infra Change Frequency: High           → Hexagonal (carrier adapter swap out)
Entry Points: 5 types (REST+WS+MQ+Batch+Schedule) → Hexagonal wins on adapter diversity
Ecosystem: Multi-region               → No ecosystem preference, Hexagonal is language-agnostic
CQRS Need: Very High                   → L2+ architecture required
```

### Step 2: Decision Tree Result

1. Very High complexity + frequent infra changes → **Hexagonal Architecture** primary recommendation
2. 7 squads need clear boundaries → **One Hexagonal module per bounded context** per squad
3. CQRS L2 — DB Separation for tracking, CQRS L1 for other domains

### Step 3: CQRS Assessment

**Tracking Domain** (read:write ≈ 1000:1):
- **CQRS L2** — DB Separation (MongoDB for write, Elasticsearch for read)
- Synchronization via Kafka domain events → ES indexing service
- Real-time WebSocket reads from ES

**Analytics Domain** (complex aggregations):
- **CQRS L2** — DB Separation (event-sourced write, materialized views for read)
- Pre-computed aggregations updated via event stream processing

**Other Domains** (order, dispatch, billing):
- **CQRS L1** — Model Separation only (shared DB)

### Step 4: Domain Classification

| Domain | Type | Architecture | CQRS | Squad |
|--------|------|-------------|------|-------|
| Real-time Routing | Core | Hexagonal + L2 CQRS | L2 | Squad A |
| Shipment Tracking | Core | Hexagonal + L2 CQRS (ES) | L2 | Squad B |
| Order Dispatch | Core | Hexagonal + L1 CQRS | L1 | Squad C |
| Carrier Integration | Generic | Hexagonal (adapter-heavy) | L0 | Squad D |
| Billing | Core | Hexagonal + L1 CQRS | L1 | Squad E |
| Warehouse Ops | Supporting | Hexagonal (simplified) | L0 | Squad F |
| Analytics | Supporting | Hexagonal + L2 CQRS (ES) | L2 | Squad G |

## Final Recommendation

```
Primary Architecture: Hexagonal (per bounded context)
CQRS: Mixed (L2 for tracking & analytics, L1 for others, L0 for generic)

Cross-cutting:
  - Common: Shared kernel (Money, GeoPoint, TimeWindow)
  - Anti-Corruption Layer (ACL) for each carrier integration
  - Event backbone: Kafka for all domain events
  - API Gateway: GraphQL for client-facing, gRPC for inter-service
```

## Rationale

1. **Hexagonal** is the best fit for multi-adapter diversity (REST + WS + MQ + Batch + Schedule)
2. **Carrier integrations** map naturally to Outbound Adapters — swap without domain impact
3. **CQRS L2 for tracking** is justified by 1000:1 read/write ratio
4. **7 squads each own a Hexagonal module** provides autonomy without architecture divergence
5. **Anti-Corruption Layer** is critical for 50+ carrier API integrations with different data models

## Next Steps

1. Proceed to [ddd-architecture-hexagonal](../ddd-architecture-hexagonal/) for Port/Adapter implementation
2. Follow with [ddd-cqrs-architecture](../ddd-cqrs-architecture/) for CQRS L2 + ES deep-dive
3. Carrier Integration ACL as first pilot (highest adapter diversity, lowest risk domain)
4. Shipment Tracking as second pilot (demonstrates CQRS L2 value)
5. Set up Architecture Decision Records (ADR) per squad to track evolution
6. Establish cross-squad Architecture Review Board for shared kernel changes
