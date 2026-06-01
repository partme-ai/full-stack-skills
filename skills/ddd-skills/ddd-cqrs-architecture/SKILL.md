---
name: ddd-cqrs-architecture
description: Comprehensive guidance for CQRS Architecture — independent CQRS skill covering L1/L2/L3 implementation levels, Event Sourcing, idempotency design, domain event lifecycle, and architecture-specific CQRS integration patterns for Layered/Onion/Hexagonal/Clean/COLA. Use when user asks about CQRS, 读写分离, Event Sourcing, 事件溯源, Command Bus, Query Model, or domain events.
license: Apache-2.0
---
# DDD CQRS Architecture

CQRS (Command Query Responsibility Segregation) — L1/L2/L3 adoption, Event Sourcing, idempotency, integration with 5 DDD architectures.

## When to Use This Skill

**Trigger keywords**: CQRS, 读写分离, Event Sourcing, 事件溯源, Command Bus, Query Model, 领域事件, domain event, 幂等, idempotency, eventual consistency, projection, materialized view

## Workflow

```
Step 1: 判断是否需要 CQRS → 确认读写模式是否显著分化
Step 2: 选择 CQRS 级别 → L1/L2/L3
Step 3: 设计命令模型 → Command → Handler → 领域事件
Step 4: 设计查询模型 → Query → Handler → DTO
Step 5: 实现事件同步（L2/L3）→ Outbox → 发布器 → 投影
Step 6: 按架构集成 → 根据 Layered/Onion/Hexagonal/Clean/COLA
```

## When to Use CQRS

### 适用场景
- **读写模式显著分化**: 写操作与读操作用不同数据结构和优化策略
- **高并发写入**: 写需 ACID 保证，读可接受最终一致性
- **多视图需求**: 同一数据多种展示形式（列表/详情/统计/搜索）
- **审计追踪要求**: 完整记录所有状态变更历史
- **团队具备事件驱动能力**: 理解最终一致性和事件溯源概念

### 升级路径
```
CRUD 够用（读=写）         → 单模型，无需 CQRS
  ↓
L1 模型分离                → CommandService / QueryService 分离，共享 DB
  ↓
L2 数据库分离               → Command DB + Query DB，事件同步
  ↓
L3 Event Sourcing          → EventStore + Projection
```

### 不适用场景
| 场景 | 替代方案 |
|------|---------|
| 简单 CRUD，读=写 | 单模型，不引入 CQRS |
| 原型/一次性项目 | 跳过 CQRS |
| 团队不熟悉事件驱动 | 先用 `ddd-event-storming` 建立事件思维 |
| 强一致性要求极高 | 评估分布式事务成本 |

## CQRS Core Principles

| 维度 | 命令侧（Write） | 查询侧（Read） |
|------|----------------|----------------|
| 职责 | 处理状态变更，执行业务规则 | 返回数据视图，无业务逻辑 |
| 模型 | Command Model（命令对象+聚合根） | Query Model（DTO+物化视图） |
| 存储 | Write DB (3NF, ACID) | Read DB (反范式, 查询优化) |
| 一致性 | 强一致性（聚合内） | 最终一致性（跨聚合/服务） |
| 输出 | 领域事件 | DTO / View Model |

## L1/L2/L3 Adoption Strategy

### L1 — Model Separation
成本最低：仅代码层分离 Command/Query Service，共享数据库。适用于读写数据结构相同但逻辑分离的场景。
参考示例: `examples/order-l1-model-separation.md`

### L2 — Database Separation
中等成本：分离 Command DB 和 Query DB，通过领域事件同步。适用于读负载高、独立优化策略需求的场景。
参考示例: `examples/order-l2-db-separation.md`

### L3 — Event Sourcing
最高成本：以事件流作为唯一真相源，通过投影重建读模型。适用于审计追踪、时间旅行查询、事件重放的场景。
参考示例: `examples/order-l3-event-sourcing.md`

## Event Lifecycle

```
领域行为 → 构建 DomainEvent → 持久化 → EventBus 发布
                                        → 本地处理器 (同步)
                                        → MQ 外发 (异步, 跨服务)
```

### 发布策略
- **轮询发布（定时扫表）**: 延迟 1-5s, 低复杂度, 中小流量
- **CDC（Debezium binlog）**: 延迟 <100ms, 中复杂度, 高流量低延迟
- **事务提交回调**: 延迟 <10ms, 低复杂度, Spring 项目

详细参考: `references/cqrs-events.md`

## 幂等设计

| 策略 | 开销 | 可靠性 | 场景 |
|------|:----:|:------:|------|
| **事件去重表** | 中 | ★★★ | 金融级关键事件 |
| **状态机守卫** | 低 | ★★★ | 状态驱动事件 |
| **Redis + TTL** | 低 | ★★☆ | 非关键通知 |
| **业务幂等** | 低 | ★★★ | 简单操作 |

详细参考（含代码示例）: `references/event-governance.md`

## 各架构 CQRS 集成模式

| 架构 | 集成点 | 目录结构 |
|------|--------|---------|
| **Layered** | Application 层 Command/Query Service 分离 | `app/service/command/` + `app/service/query/` |
| **Onion** | Core 层 Command/Query UseCase 接口 | `core/application/command/` + `core/application/query/` |
| **Hexagonal** | Port 层 Command Port + Query Port | `domain/port/command/` + `domain/port/query/` |
| **Clean** | UseCase 层 Command Interactor + Query Interactor | `usecase/interactor/command/` + `usecase/interactor/query/` |
| **COLA** | App 层 Command + Query 子模块 | `app/command/` + `app/query/` |

详细参考: `examples/multi-architecture-integration.md`

## Gotchas

- **过早升级到 L2/L3**: 先在 L1 验证 CQRS 价值，大多数项目 L1 就够了
- **Query 侧直接查写库**: Query 绝不能直接读取 Command 侧数据库表
- **忘了事件幂等**: 消费者必须实现幂等（at-least-once 投递）
- **事件版本不兼容**: 修改事件结构必须向后兼容
- **最终一致性的 UI 处理**: L2/L3 下前端需轮询或 WebSocket
- **过大的聚合**: 事件溯源聚合应保持小聚合原则

## FAQ

| 问题 | 回答 |
|------|------|
| CQRS 一定会引入最终一致性？ | L1 不需要，L2/L3 需要 |
| Event Sourcing 和 CQRS 绑定？ | 否，可独立使用 |
| 何时需要 Outbox 模式？ | 需要可靠事件发布时，避免双写问题 |
| CQRS 和微服务关系？ | 正交，可在单体内部署或跨微服务 |
| 查询模型复杂到何种程度？ | 可跨聚合/服务组装，反范式化物化视图 |

## Rules

| 规则 | 说明 |
|------|------|
| Command 侧需验证权限 | 执行命令前必须鉴权 |
| 事件体不能含敏感数据 | 密码、PII 等不应出现在事件中 |
| 查询侧不能修改状态 | Query Handler/Service 不能有写操作 |
| 同一事务写业务数据 + Outbox | 避免双写问题 |
| 聚合内强一致，聚合间最终一致 | 一个事务最多改一个聚合的状态 |

## Skill Boundary

### ✅ 擅长处理
1. 读写模式显著分化的系统（报表 vs 交易）
2. 需要事件驱动架构的项目
3. CQRS 三级渐进落地（L1 模型分离 / L2 DB分离 / L3 Event Sourcing）
4. 与 5 种 DDD 架构的集成模式
5. 领域事件全生命周期治理（发布/订阅/幂等/补偿）

### ⚠️ 需要条件
1. 已选好基础架构（Layered/Onion/Hexagonal/Clean/COLA）
2. 团队理解最终一致性和事件驱动概念
3. 业务场景确实需要读写分离（非简单 CRUD）

### ❌ 不该用（超出范围）
1. 简单 CRUD（读=写） → 不适用 CQRS
2. 原型/一次性项目 → 不应该使用 CQRS
3. 团队不熟悉事件驱动 → 先用 `ddd-event-storming` 建立事件思维
4. 已使用 CQRS 框架（Axon） → 框架内置了 CQRS 模式

## Security & Stability

- Code templates are educational — replace URLs/credentials with env vars.
- Command handlers must validate authorization. Never trust caller is authorized.
- Event payloads must not contain sensitive data — events are stored and replayed.
- 最小权限原则：Command API 和 Query API 应使用不同的访问权限控制

## Keywords

`CQRS`, `读写分离`, `Event Sourcing`, `事件溯源`, `Command Bus`, `Query Model`, `Command Model`, `领域事件`, `Domain Event`, `最终一致性`, `Eventual Consistency`, `Outbox Pattern`, `Transactional Outbox`, `Materialized View`, `Projection`, `Event Store`, `Idempotency`, `幂等`, `L1/L2/L3`, `Clean Architecture CQRS`, `Hexagonal CQRS`, `COLA CQRS`

## References

### Architecture CQRS Patterns
- `references/architecture/clean-ddd-hexagonal-cqrs.md` — CQRS & Domain Events：Commands, Queries, Read Models, Event Dispatcher, Outbox
- `references/cqrs-events.md` — CQRS 领域事件：事件分类、事件存储、投影策略、版本管理
- `references/cqrs-mindmap.md` — CQRS 思维导图：适用场景、实施策略
- `references/ddd4j-cqrs-mindmap.md` — CQRS 思维导图：核心理念、架构模式、组件

### Domain Events & Event Governance
- `references/event-governance.md` — 事件治理：Outbox DDL、幂等、重试/死信/补偿/对账
- `references/domain-events/domain-events-deep.md` — 领域事件深入：事件驱动设计原则
- `references/domain-vs-integration-events.md` — 领域事件 vs 集成事件：边界划分
- `references/partme-06-domain-events.md` — 领域事件实操：保险承保案例

## Examples

- `examples/order-l1-model-separation.md` — L1 模型分离完整示例
- `examples/order-l2-db-separation.md` — L2 数据库分离 + 事件同步
- `examples/order-l3-event-sourcing.md` — L3 Event Sourcing 完整示例
- `examples/multi-architecture-integration.md` — 5 种架构 CQRS 集成对比
- `examples/inventory-cqrs.md` — 库存 CQRS + 幂等策略实现
