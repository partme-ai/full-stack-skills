# Technical Debt Calculation Guide

## Debt Identification Methods

### Structural Debt (P0) — Weight: 0.5

| Metric | Detection Method | Scoring |
|--------|-----------------|---------|
| Layer violation ratio | `grep` for domain → infra imports | violations / total files × 100 |
| Circular dependency count | `jdepend` / `archunit` | each cycle = 5 pts |
| Anemic entity ratio | entities with only getter/setter / total entities | ratio × 100 |
| Framework leak ratio | domain files with Spring/JPA imports / total domain files | ratio × 100 |

```
Structural Debt Score = Σ(metric_scores) / 4
Score range: 0-100
```

### Design Debt (P1) — Weight: 0.3

| Metric | Detection Method | Scoring |
|--------|-----------------|---------|
| Oversized aggregate ratio | aggregates with > 5 entities / total aggregates | ratio × 100 |
| Missing domain event ratio | key operations without events / total operations | ratio × 100 |
| Value object missing rate | String fields replaceable by VO / total fields | ratio × 100 |
| Cross-aggregate ref count | direct object references between aggregates | each = 3 pts |

```
Design Debt Score = Σ(metric_scores) / 4
Score range: 0-100
```

### Testing Debt (P2) — Weight: 0.2

| Metric | Detection Method | Scoring |
|--------|-----------------|---------|
| Domain unit test coverage | line coverage for domain module | (100 - coverage%) |
| Aggregate root test coverage | distinct aggregate root tests / total aggregate roots | (100 - ratio × 100) |
| Integration test coverage | integration tests / infrastructure classes | (100 - ratio × 100) |

```
Testing Debt Score = Σ(metric_scores) / 3
Score range: 0-100
```

## Final Calculation

```
Total Debt = Structural × 0.5 + Design × 0.3 + Testing × 0.2

Thresholds:
  ≤ 20  → 🟢 Healthy (no action needed)
  21-40 → 🟡 Mild (schedule repayment)
  41-60 → 🟠 Moderate (create repayment plan this quarter)
  > 60  → 🔴 Severe (start refactoring immediately)
```

## Example Calculation

```yaml
Structural:
  Layer violations: 12 files / 50 total = 24%
  Circular dependencies: 2 cycles × 5 = 10
  Anemic entities: 5/8 = 62.5%
  Average: (24 + 10 + 62.5) / 4 = 24.1

Design:
  Oversized aggregates: 2/6 = 33.3%
  Missing events: 3/10 = 30%
  VO missing rate: 40%
  Cross-aggregate refs: 1 × 3 = 3
  Average: (33.3 + 30 + 40 + 3) / 4 = 26.6

Testing:
  Domain coverage: 100 - 45% = 55
  Aggregate root testing: 100 - (3/6 × 100) = 50
  Integration testing: 100 - (5/12 × 100) = 58.3
  Average: (55 + 50 + 58.3) / 3 = 54.4

Total = 24.1 × 0.5 + 26.6 × 0.3 + 54.4 × 0.2
      = 12.05 + 7.98 + 10.88
      = 30.91 → 🟡 Mild
```
