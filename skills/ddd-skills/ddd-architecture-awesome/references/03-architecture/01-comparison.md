# DDD Architecture Comparison

Side-by-side comparison of all DDD architecture styles.

## Quick Reference Matrix

| Dimension | Layered | Hexagonal | Onion | Clean | COLA |
|-----------|---------|-----------|-------|-------|------|
| **Origin** | Traditional N-tier | Alistair Cockburn 2005 | Jeffrey Palermo 2008 | Robert C. Martin 2012 | Alibaba 2018 |
| **Complexity** | ★☆☆☆☆ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★☆ |
| **Convention Level** | Low | Medium | Medium | High | Very High |
| **Learning Curve** | Low | Medium | Medium | High | Medium-High |
| **Flexibility** | Low | High | High | High | Medium |
| **Code Generation Support** | Good | Poor | Poor | Poor | Excellent |
| **Chinese Community** | Universal | Growing | Limited | Growing | Strong |
| **Best For** | Small projects, fast start | API-heavy apps | Domain-rich apps | Large enterprise | Chinese enterprise |

## Layered Architecture (分层架构)

```
┌─────────────────────────────┐
│     Presentation Layer      │  ← HTTP, GUI, CLI
├─────────────────────────────┤
│     Application Layer       │  ← Use cases, orchestration
├─────────────────────────────┤
│     Domain Layer            │  ← Business logic, entities
├─────────────────────────────┤
│     Infrastructure Layer    │  ← DB, messaging, external APIs
└─────────────────────────────┘
```

**Pros:**
- Simplest to understand and implement
- Good for small to medium projects
- Clear separation of concerns

**Cons:**
- Tight coupling between layers in practice
- Infrastructure concerns tend to leak upward
- Difficult to swap infrastructure implementations
- "Layered architecture done wrong is just spaghetti in boxes"

**When to choose:**
- Team is new to DDD
- Project scope is well-understood and limited
- Quick time to market is critical

## Hexagonal Architecture (六边形架构 / Ports & Adapters)

```
         ┌──────────────────────────────┐
         │         ┌────────┐          │
  HTTP ──┼──port──▶│ Domain │──port──┼── DB
         │         └────────┘          │
  MQ  ───┼──port──▶         ◀──port──┼── REST API
         │                            │
  CLI ───┼──port──▶  (pure, no deps)  ◀──port──┼── SMTP
         └──────────────────────────────┘

  Ports = Interfaces defined by domain
  Adapters = Implementations of ports (on both sides)
```

**Key concepts:**
- **Primary/Driving Adapters**: Initiate actions (HTTP controllers, CLI, tests)
- **Secondary/Driven Adapters**: Handle domain requests (DB, message queue, external API)
- **Ports**: Interfaces that domain defines for communication
- **Dependency inversion**: Domain defines the contract, infrastructure implements it

**Pros:**
- Excellent testability (replace adapters with mocks)
- Framework-agnostic domain
- Easy to swap infrastructure technologies
- Clear separation of concerns

**Cons:**
- More ceremony than layered architecture
- Interface explosion if over-applied
- Mapping overhead between layers

**When to choose:**
- Multiple input/output channels
- Need to swap infrastructure frequently
- Strong testing requirements
- API-heavy applications

## Onion Architecture (洋葱架构)

```
         ┌─────────────────────────────┐
         │      Infrastructure          │
         │  ┌───────────────────────┐  │
         │  │   Application Services │  │
         │  │  ┌─────────────────┐  │  │
         │  │  │  Domain Services │  │  │
         │  │  │  ┌───────────┐  │  │  │
         │  │  │  │  Domain   │  │  │  │
         │  │  │  │  Model    │  │  │  │
         │  │  │  └───────────┘  │  │  │
         │  │  └─────────────────┘  │  │
         │  └───────────────────────┘  │
         └─────────────────────────────┘

  Dependencies: outer → inner (NEVER inner → outer)
```

**Key concepts:**
- Concentric layers, domain at the center
- Inner layers define interfaces, outer layers implement them
- Strong dependency rule
- Domain objects have no external dependencies

**Pros:**
- Strongest protection of domain logic
- High testability
- Framework independence
- Very clear architecture

**Cons:**
- Significant abstraction overhead
- Mapping between layers
- Can feel like over-engineering for simple apps

**When to choose:**
- Domain complexity is high
- Long-lived systems
- Need framework independence
- Team has strong DDD experience

## Clean Architecture (整洁架构)

```
┌─────────────────────────────────────┐
│       Frameworks & Drivers          │
│  ┌───────────────────────────────┐  │
│  │     Interface Adapters        │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │  Application Business   │  │  │
│  │  │  Rules (Use Cases)      │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │ Enterprise        │  │  │  │
│  │  │  │ Business Rules    │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

**Pros:**
- Independent of frameworks
- Testable without UI, database, or external systems
- Independent of UI (easy to swap UIs)
- Independent of database (easy to swap databases)

**Cons:**
- Very complex to set up
- Many abstractions
- Significant ceremony
- Can be overkill for many projects

**When to choose:**
- Very large systems
- Multiple deployment targets
- Maximum flexibility needed
- Enterprise-level governance

## COLA Architecture (COLA 架构)

```
┌──────────────────────────────────────────┐
│        Adapter Layer (适配层)              │
│  ┌────────────┐  ┌────────────────────┐  │
│  │ HTTP/RPC   │  │ Message Consumer   │  │
│  └────────────┘  └────────────────────┘  │
├──────────────────────────────────────────┤
│        Application Layer (应用层)          │
│  ┌────────────┐  ┌────────────────────┐  │
│  │ Service    │  │ Assembler/DTO       │  │
│  └────────────┘  └────────────────────┘  │
├──────────────────────────────────────────┤
│        Domain Layer (领域层)               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ Entity   │ │ Service  │ │ Gateway  │ │
│  └──────────┘ └──────────┘ └──────────┘ │
├──────────────────────────────────────────┤
│        Infrastructure Layer (基础设施层)    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ DB       │ │ Cache    │ │ MQ       │ │
│  └──────────┘ └──────────┘ └──────────┘ │
└──────────────────────────────────────────┘
```

**Pros:**
- Strong conventions (predictable code organization)
- Excellent code generation support
- Chinese community and documentation
- Balances theory with practical engineering
- Built-in extension points (Interceptor, ExtPt)

**Cons:**
- Learning curve for non-Chinese teams
- Can feel rigid (strong conventions)
- Heavy dependency on Spring ecosystem
- May be over-structured for small projects

**When to choose:**
- Chinese enterprise projects
- Need strong conventions and code generation
- Team values consistency over flexibility
- Spring Boot ecosystem

## Dependency Rule Across All Architectures

Regardless of architecture style, the universal rule is:

```
DEPENDENCIES POINT INWARD ONLY

Outer layers → Inner layers: ALLOWED
Inner layers → Outer layers: FORBIDDEN

Domain MUST NOT depend on:
✗ Framework annotations in domain objects
✗ Database-specific types
✗ HTTP request/response objects
✗ Message broker clients
✗ Any infrastructure concern
```

## How to Choose

See `ddd-architecture-selector` skill for detailed decision guidance. Quick reference:

```
Is business logic complex?
  NO  → Simple Layered or skip DDD entirely
  YES → Does the project need to swap infrastructure?
         NO  → COLA (if Chinese ecosystem) or Layered
         YES → Does the project need maximum flexibility?
                NO  → Hexagonal
                YES → Clean or Onion Architecture
```