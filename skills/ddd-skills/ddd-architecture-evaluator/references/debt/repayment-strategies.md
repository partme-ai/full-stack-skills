# Technical Debt Repayment Strategies

## Strategy Selection Matrix

| Debt Level | Strategy | Effort | ROI Timeline |
|:----------:|----------|:------:|:------------:|
| Severe (>60) | All-hands refactoring sprint | 2-4 weeks | Immediate |
| Moderate (41-60) | Ring-fenced 20% time per sprint | Ongoing | 3 months |
| Mild (21-40) | Quarterly debt sprint | 1 week/quarter | 6-12 months |
| Healthy (≤20) | Continuous improvement | As needed | Ongoing |

## Structural Debt Repayment (P0)

1. **Layer violations**: Add ArchUnit rules, block CI for new violations
2. **Circular deps**: Extract shared interface or event-based communication
3. **Anemic entities**: Move one service method per sprint into entity
4. **Framework leaks**: Replace @Entity with POJO in domain; use JPA in infra only

## Design Debt Repayment (P1)

1. **Oversized aggregates**: Identify sub-aggregates, extract with ID refs
2. **Missing events**: Map domain events from existing @Transactional methods
3. **String → VO**: Replace one field per sprint using Strangler Fig for DB columns
