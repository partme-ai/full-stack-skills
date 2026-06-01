# Migration Risk Assessment Checklist

## Pre-Migration Readiness

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 1 | Current architecture fully documented | ☐ | ADR, C4 diagrams up to date |
| 2 | Business complexity assessment complete | ☐ | Is migration worth the investment? |
| 3 | Team DDD knowledge assessed | ☐ | Training needs identified |
| 4 | Migration scope defined | ☐ | Full vs incremental |
| 5 | Target architecture agreed upon | ☐ | Team and stakeholders aligned |
| 6 | Rollback plan established | ☐ | Maximum 4 hours to rollback |
| 7 | Stakeholder buy-in secured | ☐ | Business + engineering alignment |
| 8 | Success metrics defined | ☐ | Measurable before/after comparison |

## Risk Scoring Matrix

| Risk Level | Impact | Probability | Score | Response |
|:----------:|:------:|:-----------:|:-----:|----------|
| Critical | Business operation disruption | High | 16-25 | Canary + automated rollback |
| High | Core feature degradation | Medium | 10-15 | Feature flag + manual rollback |
| Medium | Non-core feature impact | Low | 5-9 | Parallel run + monitoring |
| Low | Performance regression | Very Low | 1-4 | Direct switch + performance test |

### Risk = Impact × Probability (1-5 each)

## Strangler Fig Migration Strategy

```
Step 1: Route new features to target architecture
Step 2: Wrap legacy modules with anti-corruption layer
Step 3: Migrate core aggregates first (highest ROI)
Step 4: Gradually replace legacy modules
Step 5: Remove legacy when all consumers migrated
```

## Migration Phasing Template

```
Phase | Duration | Scope | Risk | Rollback
------|----------|-------|:----:|---------
Pilot | 1-2 weeks | Single aggregate (read-only) | Low | Disable feature flag
Wave 1 | 2-4 weeks | Core write operations | Medium | Traffic switch back
Wave 2 | 1-2 months | Full bounded context | High | Canary release
Wave 3 | 2-3 months | Remaining modules | Medium | Per-module rollback
```

## Architecture-Specific Risks

| Current → Target | Key Risks | Mitigation |
|-----------------|-----------|------------|
| MVC → DDD Layered | Team learning curve, service extraction complexity | Training + pair programming |
| Layered → Hexagonal | Port design mistakes, over-abstraction | Start with 1 port, iterate |
| Monolith → Microservices | Network latency, data consistency, distributed transactions | Eventual consistency + Saga |
| Clean → Event Sourcing | Event schema evolution, replay complexity | Versioned events + snapshot |
| CQRS L1 → L3 | Eventual consistency gaps, projection rebuild time | Idempotency + throttled rebuild |

## Post-Migration Validation

| # | Validation Item | Measure |
|---|----------------|---------|
| 1 | Feature parity | All old test cases pass |
| 2 | Performance | P95 latency ≤ 1.2× baseline |
| 3 | Data integrity | Row count + checksum match |
| 4 | Team productivity | Feature cycle time not increased |
| 5 | Architecture compliance | ArchUnit score ≥ 85% |
