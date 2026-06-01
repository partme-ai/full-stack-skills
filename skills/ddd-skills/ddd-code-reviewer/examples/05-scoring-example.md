# Scoring Calculation Example

This example demonstrates the full scoring calculation for a fictional project `partme-inventory-service`.

## Input Data

### Dimension 1: Layering Compliance (weight 30%)

| Check Item | Pass? | Weight | Score |
|------------|:-----:|:------:|:-----:|
| Domain zero framework dependency | ❌ | 25% | 0 |
| No reverse dependency | ✅ | 20% | 20 |
| App layer no SQL | ✅ | 20% | 20 |
| Controller no business logic | ✅ | 15% | 15 |
| Repository returns aggregate root | ⚠️ (partial) | 10% | 5 |
| No circular dependencies | ✅ | 10% | 10 |

**Raw score**: (0 + 20 + 20 + 15 + 5 + 10) = 70/100
**Weighted**: 70 × 30% = **21.0/30**

### Dimension 2: Domain Model Quality (weight 30%)

| Check Item | Pass? | Weight | Score |
|------------|:-----:|:------:|:-----:|
| Rich model coverage (6/10 entities) | ⚠️ | 30% | 18 |
| Value Object usage (4/12 fields) | ⚠️ | 25% | 8 |
| Aggregate design | ✅ | 20% | 18 |
| Domain events for key operations (2/5) | ⚠️ | 15% | 6 |
| Immutability of value objects (3/4 VOs) | ✅ | 10% | 8 |

**Raw score**: (18 + 8 + 18 + 6 + 8) = 58/100
**Weighted**: 58 × 30% = **17.4/30**

### Dimension 3: Naming Conventions (weight 15%)

| Check Item | Pass? | Weight | Score |
|------------|:-----:|:------:|:-----:|
| Aggregate Root naming | ✅ | 20% | 20 |
| Repository naming | ✅ | 20% | 20 |
| Domain Service naming | ✅ | 15% | 15 |
| Domain Event naming | ⚠️ | 15% | 10 |
| Package by aggregate | ✅ | 15% | 15 |
| Method naming | ✅ | 15% | 15 |

**Raw score**: (20 + 20 + 15 + 10 + 15 + 15) = 95/100
**Weighted**: 95 × 15% = **14.25/15**

### Dimension 4: Code Structure (weight 15%)

| Check Item | Pass? | Weight | Score |
|------------|:-----:|:------:|:-----:|
| Aggregate Root < 200 lines | ✅ | 20% | 20 |
| Service < 100 lines | ❌ | 20% | 0 |
| Cyclomatic complexity < 10 | ⚠️ | 20% | 10 |
| Package by aggregate | ✅ | 20% | 20 |
| Exception handling | ✅ | 20% | 18 |

**Raw score**: (20 + 0 + 10 + 20 + 18) = 68/100
**Weighted**: 68 × 15% = **10.2/15**

### Dimension 5: Test Coverage (weight 10%)

| Check Item | Pass? | Weight | Score |
|------------|:-----:|:------:|:-----:|
| Domain layer unit coverage (~70%) | ⚠️ | 40% | 28 |
| Aggregate root behavior tests | ✅ | 30% | 28 |
| Domain event verification | ❌ | 30% | 0 |

**Raw score**: (28 + 28 + 0) = 56/100
**Weighted**: 56 × 10% = **5.6/10**

## Final Calculation

```text
Total = 21.0 + 17.4 + 14.25 + 10.2 + 5.6 = 68.45/100
```

## Result

| Dimension | Raw Score | Weight | Weighted |
|-----------|:---------:|:------:|:--------:|
| Layering Compliance | 70/100 | 30% | 21.0/30 |
| Domain Model Quality | 58/100 | 30% | 17.4/30 |
| Naming Conventions | 95/100 | 15% | 14.25/15 |
| Code Structure | 68/100 | 15% | 10.2/15 |
| Test Coverage | 56/100 | 10% | 5.6/10 |
| **Total** | | **100%** | **68.45 → 68/100** |

**Grade**: 🟠 C (Obvious anti-patterns present — plan refactoring sprint)

## What-If Analysis

### Scenario A: Fix Domain Framework Dependency Only

Fix 1 P0 issue: `javax.persistence.Entity` removed from domain.

| Old | New | Improvement |
|:---:|:---:|:-----------:|
| Layering 70 → 21.0 | Layering 90 → 27.0 | **+6.0** |
| Total: 68/100 | Total: **74/100** | Grade 🟡 B |

### Scenario B: Fix P0 Issues Only

Fix domain framework dependency + add domain events.

| Old | New | Improvement |
|:---:|:---:|:-----------:|
| Layering 70 → 21.0 | Layering 90 → 27.0 | +6.0 |
| Domain Model 58 → 17.4 | Domain Model 76 → 22.8 | +5.4 |
| Total: 68/100 | Total: **79.4/100** | Grade 🟡 B |

### Scenario C: Fix All Issues

Address all P0 + P1 issues.

| Old | New | Improvement |
|:---:|:---:|:-----------:|
| Layering 70 → 21.0 | Layering 100 → 30.0 | +9.0 |
| Domain Model 58 → 17.4 | Domain Model 85 → 25.5 | +8.1 |
| Naming 95 → 14.25 | Naming 100 → 15.0 | +0.75 |
| Structure 68 → 10.2 | Structure 85 → 12.75 | +2.55 |
| Test 56 → 5.6 | Test 80 → 8.0 | +2.4 |
| Total: 68/100 | Total: **91.25/100** | Grade 🟢 A |

## ROI Estimation

| Scenario | Effort | Score Gain | ROI |
|----------|:------:|:----------:|:---:|
| A (1 P0 fix) | 0.5h | +6.0 | 12.0 pts/h |
| B (2 P0 fixes) | 3h | +11.4 | 3.8 pts/h |
| C (all issues) | 20h | +23.25 | 1.16 pts/h |

**Recommendation**: Start with Scenario B (max ROI). Plan Scenario C for next sprint.
