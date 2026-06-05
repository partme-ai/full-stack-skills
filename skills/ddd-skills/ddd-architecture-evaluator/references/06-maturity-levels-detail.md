# DDD Maturity Levels — Detailed Checklist

## Level 1: Ad Hoc (初始级)

| # | Check Item | Pass Criteria |
|---|-----------|--------------|
| 1.1 | Architecture pattern | Traditional 3-layer (Controller-Service-Repository) |
| 1.2 | Entity richness | Entity classes have only getters/setters, zero business methods |
| 1.3 | Value objects | No value objects used; all fields are primitives/Strings |
| 1.4 | Aggregates | No aggregate concept; data model is table-driven |
| 1.5 | Domain events | No domain events |
| 1.6 | Repository | Repository is a thin wrapper around ORM/DB |
| 1.7 | Dependencies | Service layer contains all business logic |

**Score**: 1 point if ≥ 5 items match.

## Level 2: Aware (认知级)

| # | Check Item | Pass Criteria |
|---|-----------|--------------|
| 2.1 | Partial rich model | ≥ 30% entities have at least one business method |
| 2.2 | Value objects | At least 3 value objects used (e.g., Money, Email, Phone) |
| 2.3 | Entity naming | Entity names use business language (not table names) |
| 2.4 | Service logic | Business logic is moving from Service to Entity |
| 2.5 | Domain awareness | Team can explain DDD concepts but not yet fully applied |

**Score**: 2 points if ≥ 3 items match.

## Level 3: Applied (实践级)

| # | Check Item | Pass Criteria |
|---|-----------|--------------|
| 3.1 | Aggregate boundaries | Clear aggregate boundaries; cross-aggregate ID references |
| 3.2 | Repository interfaces | Repository interfaces in Domain, implementations in Infrastructure |
| 3.3 | Domain events | Core business flows publish domain events |
| 3.4 | Layer dependency | Correct dependency direction (Domain has zero framework deps) |
| 3.5 | Entities are rich | ≥ 80% entities have business methods, not just getters/setters |
| 3.6 | Unit of Work | Transaction scope at Application layer, not Domain |
| 3.7 | Bounded context | At least one bounded context defined |

**Score**: 3 points if ≥ 5 items match.

## Level 4: Scaled (规模化级)

| # | Check Item | Pass Criteria |
|---|-----------|--------------|
| 4.1 | Multiple BCs | ≥ 2 bounded contexts with explicit context mapping |
| 4.2 | CQRS | CQRS adopted where read/write patterns diverge |
| 4.3 | Auto-validation | Architecture rules validated in CI/CD (ArchUnit) |
| 4.4 | Event-driven | Cross-context communication via events (not direct API calls) |
| 4.5 | Anti-corruption | ACL (Anti-Corruption Layer) for legacy integration |
| 4.6 | Domain service | Domain services used for operations spanning multiple aggregates |
| 4.7 | Testing strategy | Domain layer unit tests, integration tests for infrastructure |

**Score**: 4 points if ≥ 5 items match.

## Level 5: Optimized (优化级)

| # | Check Item | Pass Criteria |
|---|-----------|--------------|
| 5.1 | Continuous evolution | Architecture fitness reviewed quarterly |
| 5.2 | Event Sourcing | Event Sourcing applied where audit trail is critical |
| 5.3 | Ubiquitous language | Domain model 100% aligned with business language |
| 5.4 | ADR | Complete Architecture Decision Record traceability |
| 5.5 | Debt dashboard | Technical debt is tracked and actively paid down |
| 5.6 | Automated metrics | Architecture metrics collected and trended over time |
| 5.7 | Team autonomy | Each bounded context team owns its architecture decisions |

**Score**: 5 points if ≥ 5 items match.

## Maturity Score Calculation

```
Overall Maturity = max(Level where ≥ threshold check items pass)

Example:
  L1 items pass: 7/7 ✓
  L2 items pass: 4/7 ✓
  L3 items pass: 6/7 ✓
  L4 items pass: 3/7 ✗ (need 5)
  → Maturity Level: 3 (Applied)
```
