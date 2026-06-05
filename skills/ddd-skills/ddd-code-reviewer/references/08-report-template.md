# DDD Code Review Report Template

Standardized report structure for DDD code review output. Use this template when generating review reports.

## Minimal Required Sections

Every DDD code review report MUST include:

1. **Overall Score** — Total + Grade
2. **Per-Dimension Scoring** — 5 dimensions with itemized results
3. **Anti-Pattern List** — Each with location and fix suggestion
4. **Improvement Suggestions** — Ordered by P0/P1/P2 priority

---

## Standard Template

```markdown
# DDD Code Review Report

**Project**: {project name}
**Review Date**: {YYYY-MM-DD}
**Reviewer**: {reviewer name}
**Scope**: {modules/aggregates reviewed}

## Overall Score: {total}/100 ({grade} {icon})

### Dimension Breakdown

| Dimension | Score | Weight | Weighted | Status |
|-----------|:-----:|:------:|:--------:|:------:|
| Layering Compliance | {score}/100 | 30% | {w}/30 | {icon} |
| Domain Model Quality | {score}/100 | 30% | {w}/30 | {icon} |
| Naming Conventions | {score}/100 | 15% | {w}/15 | {icon} |
| Code Structure | {score}/100 | 15% | {w}/15 | {icon} |
| Test Coverage | {score}/100 | 10% | {w}/10 | {icon} |
| **Total** | | **100%** | **{total}/100** | **{grade}** |

---

### 1. Layering Compliance ({score}/30)

| Check Item | Result | Note |
|------------|:------:|------|
| Domain zero framework dependency | ✅/❌/⚠️ | {detail} |
| No reverse dependency | ✅/❌/⚠️ | {detail} |
| App layer no SQL | ✅/❌/⚠️ | {detail} |
| Controller no business logic | ✅/❌/⚠️ | {detail} |
| Repository returns aggregate root | ✅/❌/⚠️ | {detail} |
| No circular dependencies | ✅/❌/⚠️ | {detail} |

### 2. Domain Model Quality ({score}/30)

| Check Item | Result | Note |
|------------|:------:|------|
| Rich model coverage | ✅/❌/⚠️ | {count} / {total} entities have business methods |
| Value Object usage | ✅/❌/⚠️ | {count} VOs used, {count} fields still primitive |
| Aggregate design | ✅/❌/⚠️ | {aggregate sizes}, {cross-ref issues} |
| Domain events | ✅/❌/⚠️ | {event count} for {operation count} key operations |
| VO immutability | ✅/❌/⚠️ | {count} VOs have setters |

### 3. Naming Conventions ({score}/15)

| Check Item | Result | Note |
|------------|:------:|------|
| Aggregate Root naming | ✅/❌/⚠️ | {example violations} |
| Repository naming | ✅/❌/⚠️ | {example violations} |
| Domain Service naming | ✅/❌/⚠️ | {example violations} |
| Domain Event naming (past tense) | ✅/❌/⚠️ | {example violations} |
| Package by aggregate | ✅/❌/⚠️ | {violation count} |

### 4. Code Structure ({score}/15)

| Check Item | Result | Note |
|------------|:------:|------|
| Aggregate Root < 200 lines | ✅/❌/⚠️ | {count} exceeding |
| Service < 100 lines | ✅/❌/⚠️ | {count} exceeding |
| Cyclomatic complexity < 10 | ✅/❌/⚠️ | {count} methods exceeding |
| Package organization | ✅/❌/⚠️ | {detail} |
| Exception handling | ✅/❌/⚠️ | {detail} |

### 5. Test Coverage ({score}/10)

| Check Item | Result | Note |
|------------|:------:|------|
| Domain unit test coverage | ✅/❌/⚠️ | ~{percentage}% |
| Aggregate root behavior tests | ✅/❌/⚠️ | {count}/{expected} tested |
| Domain event assertion | ✅/❌/⚠️ | {count} events verified |

---

### Anti-Pattern List

| Severity | Anti-Pattern | File:Line | Fix Suggestion |
|:---------:|-------------|-----------|---------------|
| P0 | {name} | {file}:{line} | {fix description} |
| P1 | {name} | {file}:{line} | {fix description} |
| P2 | {name} | {file}:{line} | {fix description} |

### Improvement Suggestions

**Immediate (P0)**:
1. {fix} — {effort estimate}
2. {fix} — {effort estimate}

**Short-term (P1)**:
1. {fix} — {effort estimate}
2. {fix} — {effort estimate}

**Long-term (P2)**:
1. {fix} — {effort estimate}
2. {fix} — {effort estimate}

---

### Change Log

| Date | Rev | Change |
|------|:---:|--------|
| {YYYY-MM-DD} | 1.0 | Initial review |
```

## Quick Summary Format (for Slack/Email)

```
🏗️ DDD Code Review — {project} ({grade})
Score: {total}/100

🔴 P0 Issues ({count}):
  - {issue} → {fix}
  - {issue} → {fix}

🟡 P1 Issues ({count}):
  - {issue} → {fix}

📊 Top Dimension: {best} ({score})
📊 Bottom Dimension: {worst} ({score})

Full report: {link}
```

## Per-Aggregate Review Card

For large reviews, break down by aggregate:

```markdown
### Aggregate: Order

**Status**: ✅ Pass (with minor issues)

| Check | Result |
|-------|:------:|
| Rich model | ✅ pay(), confirm(), cancel(), addItem() — all in entity |
| Value Objects | ⚠️ status still String, should be OrderStatus VO |
| Events | ✅ OrderPlaced, OrderConfirmed, OrderCancelled |
| Size | ✅ 180 lines (entities + VOs), 45 lines (repository interface) |
| Tests | ⚠️ ~60% coverage — missing confirm() edge cases |
```

## Aggregating Multiple Reviews

When reviewing multiple modules:

```markdown
| Module | Score | Grade | P0 | P1 | P2 | Action |
|--------|:-----:|:-----:|:--:|:--:|:--:|--------|
| Order | 85/100 | 🟢 A | 0 | 2 | 1 | Ready |
| Payment | 62/100 | 🟠 C | 2 | 3 | 1 | Refactor needed |
| Inventory | 45/100 | 🔴 D | 4 | 2 | 0 | Block merge |

**Overall Project Health**: 🟠 C — 64/100
```
