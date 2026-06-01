# Architecture Patterns Reference

This document provides detailed structure examples for four DDD architecture patterns.

## 1. DDD Classic Layered Architecture (DDD 经典分层架构)

### Layer Structure

```
interfaces (接口层)
    ↓ 依赖
application (应用层)
    ↓ 依赖
domain (领域层)
    ↑ 实现接口
infrastructure (基础设施层)
```

### Package Structure

```
{basePackage}.{module}.interfaces
{basePackage}.{module}.application
{basePackage}.{module}.domain
{basePackage}.{module}.infrastructure
```

### Key Components

- **interfaces**: Controllers, DTOs, Filters, Exception Handlers
- **application**: Application Services, Commands, Queries, Event Handlers
- **domain**: Aggregates, Entities, Value Objects, Domain Services, Repository Interfaces
- **infrastructure**: Repository Implementations, External Services, Configurations

### Reference

See: `docs/1、DDD 经典分层架构目录结构.md`

## 2. Hexagonal Architecture (六边形架构)

### Layer Structure

```
adapter (适配器层)
    ↓ 依赖
application (应用层)
    ↓ 依赖
domain (领域层)
    ↑ 实现接口
infrastructure (基础设施层)
```

### Package Structure

```
{basePackage}.{module}.adapter
{basePackage}.{module}.application
{basePackage}.{module}.domain
{basePackage}.{module}.infrastructure
```

### Key Components

- **adapter**: Web Controllers, RPC Providers, Message Consumers, Scheduled Jobs
- **application**: Use Cases, Application Services, Ports (Inbound/Outbound)
- **domain**: Entities, Value Objects, Domain Services, Domain Events
- **infrastructure**: Repository Implementations, External Service Adapters, Configurations

### Ports and Adapters

- **Inbound Ports**: Define application services (e.g., `IOrderService`)
- **Outbound Ports**: Define external dependencies (e.g., `IOrderRepository`, `IPaymentProvider`)
- **Inbound Adapters**: Web Controllers, CLI, Message Consumers
- **Outbound Adapters**: Database Repositories, External API Clients, Message Publishers

### Reference

See: `docs/2、六边形架构详细目录结构参考.md`

## 3. Clean Architecture (整洁架构)

### Layer Structure

```
interfaces (接口适配器层)
    ↓ 依赖
application (应用层/用例层)
    ↓ 依赖
domain (领域层/实体层)
    ↑ 实现接口
infrastructure (基础设施层)
```

### Package Structure

```
{basePackage}.{module}.interfaces
{basePackage}.{module}.application
{basePackage}.{module}.domain
{basePackage}.{module}.infrastructure
```

### Key Components

- **interfaces**: Controllers, Presenters, Gateways (Input/Output Ports)
- **application**: Use Cases, Application Services, Input/Output Ports
- **domain**: Entities, Value Objects, Domain Services, Repository Interfaces
- **infrastructure**: Repository Implementations, External Service Adapters, Configurations

### Ports

- **Input Ports**: Define use case interfaces
- **Output Ports**: Define external dependencies (Repository, External Services)

### Reference

See: `docs/3、整洁架构详细目录结构参考.md`

## 4. COLA V5 (菱形架构)

### Layer Structure

```
adapter (适配器层)
    ↓ 依赖
app (应用层)
    ↓ 依赖
domain (领域层)
    ↑ 实现接口
infrastructure (基础设施层)
```

### Package Structure

```
{basePackage}.{module}.adapter
{basePackage}.{module}.app
{basePackage}.{module}.domain
{basePackage}.{module}.infrastructure
```

### Key Components

- **adapter**: Web Controllers, RPC Providers, Job Schedulers, Message Listeners
- **app**: Executors (Command/Query), Application Services, Extensions
- **domain**: Entities, Value Objects, Domain Services, Abilities, Gateways, Repository Interfaces
- **infrastructure**: Repository Implementations, Gateway Implementations, External Clients

### COLA V5 Specific Features

- **Executors**: Command Executors (`CmdExe`) and Query Executors (`QryExe`)
- **Extensions**: Extension Points for business logic extension
- **Abilities**: Domain abilities for cross-entity business rules
- **Gateways**: Domain gateways for external dependencies

### Reference

See: `docs/4、COLA V5 架构详细目录结构参考.md`

## Comparison Table

| Aspect | DDD Classic | Hexagonal | Clean | COLA V5 |
|--------|-------------|-----------|-------|---------|
| **Interface Layer** | `interfaces` | `adapter` | `interfaces` | `adapter` |
| **Application Layer** | `application` | `application` | `application` | `app` |
| **Domain Layer** | `domain` | `domain` | `domain` | `domain` |
| **Infrastructure** | `infrastructure` | `infrastructure` | `infrastructure` | `infrastructure` |
| **Port Concept** | No | Yes (Inbound/Outbound) | Yes (Input/Output) | Yes (Gateways) |
| **Use Cases** | Application Services | Use Cases | Use Cases | Executors |
| **Extension** | No | No | No | Yes (Extension Points) |
| **Ability** | Domain Services | Domain Services | Domain Services | Abilities |

## Choosing an Architecture

### Choose DDD Classic when:
- Following Eric Evans' DDD book
- Need clear layer separation
- Standard DDD implementation

### Choose Hexagonal when:
- Need technology isolation
- Multiple driving adapters (Web, CLI, Message)
- High testability requirements

### Choose Clean Architecture when:
- Need concentric circle structure
- High testability requirements
- Business logic complexity

### Choose COLA V5 when:
- Need extension mechanism
- Want ability pattern
- Alibaba COLA framework users

## Common Principles

All four architectures follow these principles:

1. **Dependency Rule**: Dependencies point inward, domain layer has no external dependencies
2. **Interface Segregation**: Domain layer defines interfaces, infrastructure implements them
3. **Separation of Concerns**: Clear layer responsibilities
4. **Testability**: Domain layer can be tested independently
