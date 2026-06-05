# DDD Code Review Scoring Criteria

Detailed breakdown of the 5-dimension scoring system used in DDD code reviews.

## Scoring Formula

```
Total Score = Σ(dimension_score × weight)

dimension_score = sum of (check_item_passed / check_item_total) × 100
```

## Dimension 1: Layering Compliance (weight: 30%)

### Check Items

| # | Check | Weight in Dimension | Detection Method |
|---|-------|:----:|-----------------|
| 1 | Domain layer has zero framework imports | 25% | Scan `import` statements in `domain/` |
| 2 | No reverse dependency (domain → infra) | 20% | Scan package references |
| 3 | Application layer has no SQL | 20% | Scan for Mapper/JdbcTemplate in `app/` |
| 4 | Controller has no business logic | 15% | Scan for if/else business branching |
| 5 | Repository returns Aggregate Root | 10% | Check return types of Repository methods |
| 6 | No circular dependency between modules | 10% | Dependency graph analysis |

### Scoring Example

```
Check 6/6 items passed → 30/30 points (100%)
Check 5/6 items passed → 25/30 points (83%)
Check 4/6 items passed → 20/30 points (67%)
Check < 4 items passed → 10/30 points (33%)
```

## Dimension 2: Domain Model Quality (weight: 30%)

### Check Items

| # | Check | Weight in Dimension | Detection Method |
|---|-------|:----:|-----------------|
| 1 | Rich model coverage | 30% | Entities with business methods / total entities |
| 2 | Value object usage rate | 25% | VO fields / total non-collection fields |
| 3 | Aggregate design rationality | 20% | Entity count per aggregate, ID-only cross-refs |
| 4 | Domain events for key operations | 15% | Event classes per aggregate |
| 5 | Immutability of value objects | 10% | Check for setters / non-final fields |

### Scoring Scale

| Rich Model Coverage | Score |
|--------------------|:----:|
| ≥ 80% entities have business methods | 28-30 |
| 50-79% | 20-27 |
| 20-49% | 10-19 |
| < 20% | 0-9 |

| Value Object Usage | Score Contribution |
|--------------------|:-----------------:|
| ≥ 60% of primitive-type fields replaced by VOs | Full marks |
| 30-59% | Half marks |
| < 30% | Low marks |

## Dimension 3: Naming Conventions (weight: 15%)

### Check Items

| # | Pattern | Standard | Score if Correct |
|---|---------|----------|:----------------:|
| 1 | Aggregate Root | `{BusinessName}` — e.g., `Order` | 20% |
| 2 | Repository | `{Aggregate}Repository` — e.g., `OrderRepository` | 20% |
| 3 | Domain Service | `{BusinessAction}Service` — e.g., `OrderPricingService` | 15% |
| 4 | Domain Event | Past tense — e.g., `OrderPaid` | 15% |
| 5 | Package by Aggregate | `domain/order/`, `domain/product/` | 15% |
| 6 | Method Naming | Ubiquitous language — e.g., `pay()`, not `updateStatus()` | 15% |

## Dimension 4: Code Structure (weight: 15%)

### Check Items

| # | Check | Threshold | Score if Met |
|---|-------|-----------|:------------:|
| 1 | Aggregate Root class size | < 200 lines | 20% |
| 2 | Service class size | < 100 lines | 20% |
| 3 | Method cyclomatic complexity | < 10 | 20% |
| 4 | Package organization by aggregate | Yes/No | 20% |
| 5 | Consistent exception handling | Domain exceptions used | 20% |

## Dimension 5: Test Coverage (weight: 10%)

### Check Items

| # | Check | Target | Scoring |
|---|-------|--------|---------|
| 1 | Domain layer unit test coverage | ≥ 80% methods tested | 40% |
| 2 | Aggregate Root behavior tests | All behavior methods tested | 30% |
| 3 | Domain event verification in tests | Events asserted in tests | 30% |

## Score Interpretation

| Range | Grade | Meaning | Action |
|-------|:----:|---------|--------|
| ≥ 85 | 🟢 A | Excellent DDD practice | Ready for production |
| 70-84 | 🟡 B | Basically compliant | Address minor issues |
| 50-69 | 🟠 C | Obvious anti-patterns | Plan refactoring sprint |
| < 50 | 🔴 D | Needs major refactoring | Block merge, restructure |

## Quick Calculation Template

```markdown
| Dimension | Score | Weight | Weighted |
|-----------|:-----:|:------:|:--------:|
| Layering Compliance | /100 | 30% | /30 |
| Domain Model Quality | /100 | 30% | /30 |
| Naming Conventions | /100 | 15% | /15 |
| Code Structure | /100 | 15% | /15 |
| Test Coverage | /100 | 10% | /10 |
| **Total** | | **100%** | **/100** |
```
