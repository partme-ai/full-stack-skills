# DDD Applicability Decision Matrix

Extended decision matrix with real-world scenarios to help determine if DDD is right for your project.

## Decision Flowchart

```
START
  │
  ├─ Is business logic complex (rules, state machines, constraints)?
  │   NO  → Is system long-lived (> 2 years)?
  │           NO  → ✗ DDD NOT RECOMMENDED (Use simple CRUD + Service)
  │           YES → ~ Cautious: adopt tactical patterns selectively
  │   YES → Is there a domain expert or stable product owner?
  │           NO  → ~ Cautious: DDD without domain expert = complex code
  │           YES → Is the team familiar with DDD or willing to learn?
  │                   NO  → ~ Cautious: start with Layered, evolve later
  │                   YES → Do you need to swap infrastructure (DB, MQ)?
  │                           NO  → ✓ DDD RECOMMENDED (COLA or Layered)
  │                           YES → ✓ DDD STRONGLY RECOMMENDED (Hexagonal/Clean)
```

## Real-World Scenario Analysis

### Scenario 1: E-Commerce Platform

**Characteristics:**
- Complex pricing rules, promotions, discounts
- Order lifecycle with multiple states
- Multiple bounded contexts (Orders, Inventory, Payment, Shipping)
- Long-lived system expecting continuous evolution

**Assessment: ✓ STRONGLY RECOMMENDED**
- Business logic complexity: HIGH
- System lifecycle: LONG
- Domain experts: Available (business analysts, product managers)
- Infrastructure swaps: Likely (payment providers, logistics partners)

**Recommendation:** Start with Hexagonal Architecture, evolve to CQRS for read-heavy operations.

### Scenario 2: Internal Employee Directory

**Characteristics:**
- CRUD operations on employee records
- Simple search and filtering
- No complex business rules
- Short-term project

**Assessment: ✗ NOT RECOMMENDED**
- Business logic complexity: LOW (pure CRUD)
- System lifecycle: SHORT
- Domain experts: Not needed

**Recommendation:** Simple Spring Boot MVC + JPA is sufficient. DDD would be over-engineering.

### Scenario 3: Insurance Claims Processing

**Characteristics:**
- Complex claim validation rules (legal, financial)
- Multi-step approval workflow
- Integration with external systems (hospitals, police, banks)
- Regulatory compliance requirements

**Assessment: ✓ STRONGLY RECOMMENDED**
- Business logic complexity: VERY HIGH
- System lifecycle: LONG (regulatory, complex)
- Domain experts: Available (claims adjusters, legal team)
- Infrastructure swaps: Possible (regulatory changes)

**Recommendation:** Clean Architecture or COLA with Event-Driven patterns for workflow.

### Scenario 4: Blog / CMS Platform

**Characteristics:**
- Content CRUD with categories and tags
- Comment moderation
- Static page management
- SEO optimization

**Assessment: ~ CAUTIOUS**
- Business logic complexity: LOW-MEDIUM
- System lifecycle: MEDIUM
- Domain model: Simple (Post, Category, Comment)
- Infrastructure swaps: Unlikely

**Recommendation:** If content moderation rules are complex, adopt DDD tactical patterns within a simpler architecture. Otherwise, standard MVC is sufficient.

### Scenario 5: Banking Core System

**Characteristics:**
- Transaction processing with ACID requirements
- Account lifecycle management
- Regulatory compliance (KYC, AML)
- High security and audit requirements
- Long-lived (decades)

**Assessment: ✓ STRONGLY RECOMMENDED**
- Business logic complexity: VERY HIGH
- System lifecycle: VERY LONG
- Domain experts: Available (banking domain experts)
- Regulatory: CRITICAL

**Recommendation:** Clean Architecture + Event Sourcing for complete audit trail.

### Scenario 6: IoT Data Collection Dashboard

**Characteristics:**
- Collect sensor data
- Display dashboards and charts
- Alert on thresholds
- Simple configuration management

**Assessment: ~ CAUTIOUS**
- Business logic complexity: LOW (mostly data ingestion)
- System lifecycle: MEDIUM
- Complex parts: Alert rules (could benefit from DDD)
- Most functionality: Simple CRUD + aggregation

**Recommendation:** Apply DDD tactical patterns only to the alert/rule engine. Keep the rest simple.

## Scoring Checklist

Rate each dimension 1-5:

| Dimension | Score 1 | Score 3 | Score 5 |
|-----------|---------|---------|---------|
| **Business Rules** | Pure CRUD | Some validation | Complex rules, state machines |
| **Business Processes** | Linear flow | Some branching | Multi-step workflows |
| **Domain Knowledge** | Simple data model | Moderate complexity | Deep domain knowledge needed |
| **System Lifecycle** | < 1 year | 2-5 years | 5+ years |
| **Team DDD Experience** | None | Some exposure | Experienced |
| **Domain Expert Availability** | None | Part-time | Full-time dedicated |
| **Infrastructure Flexibility Need** | Fixed | Some changes | Frequent swaps |
| **Regulatory/Audit Requirements** | None | Basic logging | Full audit trail |

**Scoring:**
- **< 16**: DDD likely over-engineering. Use simple architecture.
- **16-24**: Selective DDD adoption. Apply tactical patterns to complex areas.
- **> 24**: DDD strongly recommended. Full strategic + tactical adoption.

## When DDD Adds Value

DDD provides the MOST value when:

1. **Business logic is the differentiator**: Your competitive advantage is in your domain rules
2. **System has multiple stakeholders**: Different teams need different views of the same business
3. **System will evolve for years**: Long-lived systems benefit from well-defined boundaries
4. **Team can collaborate with domain experts**: DDD requires business-technical collaboration
5. **Testing is a priority**: DDD patterns make testing significantly easier

## When DDD Does NOT Add Value

DDD provides LITTLE value when:

1. **System is pure CRUD**: Data in, data out with no business logic
2. **System is short-lived**: Prototype, proof of concept, disposable system
3. **No domain expert available**: DDD without domain collaboration is cargo cult
4. **Team resistance**: Forcing DDD on an unwilling team leads to poor implementation
5. **Simple data transformation**: ETL, data pipelines, reporting systems