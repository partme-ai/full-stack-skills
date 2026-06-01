# Gotchas — Common Pitfalls

| # | Trap | Risk | Why It Happens | How to Avoid |
|---|------|:----:|---------------|--------------|
| 1 | **Trend-chasing**: COLA/Hecagonal just because "everyone uses it" | High | Community hype overrides objective evaluation | Always run the decision matrix first; don't pick architecture by popularity |
| 2 | **CQRS forgotten**: Architecture selected without CQRS assessment | High | CQRS treated as an afterthought, not a design dimension | Include CQRS assessment as mandatory step in every selection |
| 3 | **Domain classification skipped**: Same architecture applied to all domains | High | Team doesn't distinguish Core/Generic/Supporting | Always classify domains before picking architectures |
| 4 | **Team capability mismatch**: Picking architecture the team can't implement | High | Evaluator assumes "ideal team" exists | Be honest about team DDD maturity; pick what they can actually deliver |
| 5 | **Single selection forever**: Assuming architecture is fixed once chosen | Medium | Architecture seen as a one-time decision | Plan evolution: Layered → Hexagonal → CQRS as complexity grows |
| 6 | **Dependency rule violations**: Domain importing framework libraries | High | Team not trained on dependency direction | Enforce via ArchUnit in CI; make dependency checks non-optional |
| 7 | **Over-engineering for small teams**: Hexagonal with 2-person team | Medium | "Best practice" applied without context | Match architecture to team size; small team = simpler architecture |
| 8 | **Ignoring tech ecosystem**: COLA recommended for non-Java stack | High | Focus only on architecture, not language/tooling | COLA is Java-specific; Onion works better for .NET, Hexagonal for Go |
| 9 | **One architecture for all microservices**: Monolithic thinking in distributed system | Medium | Each service gets same architecture template | Per-service selection based on domain type: Core→Complex, Generic→Simple |
| 10 | **CQRS L2+ with Layered architecture** | High | Layered lacks port isolation for clean read/write separation | Only adopt L2+ with Hexagonal or Clean architectures |
| 11 | **Architecture without ArchUnit**: No automated dependency enforcement | Medium | Manual review misses violations as codebase grows | Add ArchUnit checks from day one, not after violations pile up |
| 12 | **Ignoring infrastructure change frequency**: Picking Layered for high-change infra | Medium | Infra changes considered "rare" when they're not | If you plan to swap DB/MQ within 12 months, pick Hexagonal or Onion |
| 13 | **Starting with microservices**: Splitting before proving the domain model | High | Team thinks microservices solve everything | Start monolith (Layered/COLA), split only when deployment/scaling demands it |
| 14 | **Missing Anti-Corruption Layer**: External systems leak into domain | Medium | No ACL between bounded contexts | Always add ACL for external systems; use Hexagonal's Adapter pattern |
| 15 | **Copying big-tech architecture**: Adopting Netflix/Stripe patterns for startup | High | "What works for Netflix works for us" fallacy | Match architecture to current scale, not aspirational scale |
