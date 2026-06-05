# Architecture Fitness Assessment Template

## 5-Dimension Scoring

### Dimension 1: Business Alignment

| Score | Description | Evidence Required |
|:-----:|------------|-----------------|
| 5 | Architecture perfectly matches business complexity | Business complexity matrix matches architecture layers |
| 4 | Minor over/under-engineering in non-critical areas | ≤ 2 instances of mismatch |
| 3 | Noticeable mismatch in a core domain | 1 core bounded context has wrong architecture level |
| 2 | Significant over/under-engineering across multiple domains | ≥ 2 bounded contexts affected |
| 1 | Architecture fundamentally wrong for the business (e.g., Clean for CRUD) | Complete architecture-business mismatch |

**Template Prompt**:
```
Business Alignment Assessment:
- Project type (CRUD / Complex domain / Real-time / Data-heavy):
- Business complexity score (1-5):
- Current architecture complexity score (1-5):
- Gap: {complexity_score - architecture_score}
- Notes:
```

### Dimension 2: Team Fit

| Score | Description | Evidence Required |
|:-----:|------------|-----------------|
| 5 | Team fully understands and follows conventions | < 5% code violates conventions |
| 4 | Most team members understand; occasional violations | 5-15% violations |
| 3 | Partial understanding; significant violations | 15-30% violations; rework needed |
| 2 | Architecture is foreign to most team members | 30-50% violations; onboarding required |
| 1 | Team ignores architecture entirely | > 50% violations; architecture not followed |

**Template Prompt**:
```
Team Fit Assessment:
- Team size:
- Average DDD experience (years):
- Ramp-up time for new members (weeks):
- Code convention violation rate (%):
- Notes:
```

### Dimension 3: Technology Fit

| Score | Description | Evidence Required |
|:-----:|------------|-----------------|
| 5 | Architecture and tech stack perfectly aligned | No friction points |
| 4 | Minor friction in non-critical layers | 1-2 adaptation points needed |
| 3 | Some friction (e.g., JPA with Clean Architecture) | 3-5 workarounds in place |
| 2 | Significant mismatch requiring middleware / wrappers | Middleware layer needed |
| 1 | Architecture requires different tech stack | Major tech migration needed |

**Template Prompt**:
```
Technology Fit Assessment:
- Primary framework/ORM:
- Architecture pattern:
- Known friction points:
- Workarounds in use:
- Notes:
```

### Dimension 4: Evolution Capability

| Score | Description | Evidence Required |
|:-----:|------------|-----------------|
| 5 | Easy to add new BCs, swap infrastructure | Module isolation proven |
| 4 | Possible with standard effort | Minor refactoring needed |
| 3 | Possible but requires planning | 1-2 sprint prep needed |
| 2 | Difficult; significant rework required | Multi-sprint effort |
| 1 | Monolith with tightly coupled modules | No module isolation |

**Template Prompt**:
```
Evolution Capability Assessment:
- BC count:
- Module coupling score (1-5):
- Average refactoring effort (points):
- New feature delivery cycle (weeks):
- Notes:
```

### Dimension 5: Delivery Efficiency

| Score | Description | Evidence Required |
|:-----:|------------|-----------------|
| 5 | Architecture accelerates delivery | Feature cycle meets targets |
| 4 | Neutral impact on delivery | No significant drag |
| 3 | Architecture slightly slows delivery | 10-20% overhead |
| 2 | Architecture significantly slows delivery | 20-40% overhead |
| 1 | Architecture blocks delivery | Cannot ship without workarounds |

**Template Prompt**:
```
Delivery Efficiency Assessment:
- Average feature cycle time (days):
- Architecture overhead (%):
- Deployment frequency:
- Bottleneck layer:
- Notes:
```

## Overall Score

```
Total Fitness = (BA × 0.25 + TF × 0.25 + TT × 0.20 + EC × 0.15 + DE × 0.15)

Weighting rationale:
- Business Alignment & Team Fit: 25% each (people + purpose)
- Technology Fit: 20% (tools)
- Evolution Capability & Delivery Efficiency: 15% each (outcomes)
```
