---
name: ddd-cqrs-architecture
description: Comprehensive guidance for CQRS Architecture — independent CQRS skill covering L1/L2/L3 implementation levels, Event Sourcing, idempotency design, domain event lifecycle, and architecture-specific CQRS integration patterns for Layered/Onion/Hexagonal/Clean/COLA. Use when user asks about CQRS, 读写分离, Event Sourcing, 事件溯源, Command Bus, Query Model, or domain events.
license: Apache-2.0
---

# DDD CQRS Architecture

CQRS (Command Query Responsibility Segregation) architecture — independent skill covering L1/L2/L3 adoption, Event Sourcing, idempotency design, and integration patterns for all 5 DDD architectures.

## Workflow

```
用户输入                          本 Skill 处理流程
────────────────────────────────────────────────────────────
"需要 CQRS 方案"     →  判断是否需要 CQRS → 推荐 L1/L2/L3 级别
"怎么做读写分离"     →  Command Model + Query Model 分离设计
"需要 Event Sourcing" →  事件溯源设计 + 投影重建策略
"跨架构集成"        →  按架构类型输出集成模式 + 目录结构
"事件处理"          →  领域事件全生命周期 + 幂等设计
```

## When to Use CQRS

### 适用场景
- **读写模式显著分化**: 写操作（创建/更新）与读操作（报表/搜索）使用不同的数据结构和优化策略
- **高并发写入**: 写操作需要 ACID 保证，读操作可以接受最终一致性
- **多视图需求**: 同一数据需要多种展示形式（列表/详情/统计/搜索）
- **审计追踪要求**: 需要完整记录所有状态变更历史
- **团队具备事件驱动能力**: 理解最终一致性和事件溯源概念

### 边界 — 何时升级

```
CRUD 够用（读=写）         → 单模型，无需 CQRS
  ↓ 读写行为开始偏离
L1 模型分离                → CommandService / QueryService 分离，共享 DB
  ↓ 读负载高，需要独立优化
L2 数据库分离               → Command DB + Query DB，事件同步
  ↓ 审计/时间旅行/重放需求
L3 Event Sourcing          → EventStore + Projection
```

### 不推荐场景
| 场景 | 替代方案 |
|------|---------|
| 简单 CRUD，读=写 | 单模型，不引入 CQRS |
| 原型/一次性项目 | 跳过 CQRS，使用 Simple Layered |
| 团队不熟悉事件驱动 | 先用 `ddd-event-storming` 建立事件思维 |
| 强一致性要求极高 | 评估 CQRS 是否适合，考虑分布式事务成本 |

## CQRS Core Principles

### 核心分离原则

```
传统 CRUD：                     CQRS：
         ┌──────────┐          ┌──────────┐     ┌──────────┐
         │   CRUD   │          │ Command  │     │  Query   │
         │  Service │          │  Model   │     │  Model   │
         └────┬─────┘          └────┬─────┘     └────┬─────┘
              │                     │                  │
         ┌────┴────┐            ┌───┴───┐          ┌───┴───┐
         │   DB    │            │ Write │          │ Read  │
         └─────────┘            │  DB   │          │  DB   │
                                └───────┘          └───────┘
```

### 分离维度

| 维度 | 命令侧（Write） | 查询侧（Read） |
|------|----------------|----------------|
| 职责 | 处理状态变更，执行业务规则 | 返回数据视图，无业务逻辑 |
| 模型 | Command Model（命令对象+聚合根） | Query Model（DTO+物化视图） |
| 存储 | Write DB (3NF, ACID) | Read DB (反范式, 查询优化) |
| 一致性 | 强一致性（聚合内） | 最终一致性（跨聚合/服务） |
| 输出 | 领域事件 | DTO / View Model |

## L1/L2/L3 Adoption Strategy

### L1 — Model Separation

**成本最低**：仅代码层分离 Command/Query Service，共享数据库。

```java
// 写侧
@Service
public class OrderCommandService {
    private final OrderRepository orderRepository;

    @Transactional
    public OrderCreatedResult createOrder(CreateOrderCommand command) {
        Order order = Order.create(command);
        orderRepository.save(order);
        return OrderCreatedResult.from(order);
    }
}

// 读侧
@Service
public class OrderQueryService {
    private final OrderReadRepository orderReadRepository;

    public OrderDetailDTO getOrderDetail(String orderId) {
        return orderReadRepository.findDetailById(orderId)
            .orElseThrow(() -> new OrderNotFoundException(orderId));
    }

    public Page<OrderSummaryDTO> listOrders(OrderQuery query, Pageable pageable) {
        return orderReadRepository.findByCriteria(query, pageable);
    }
}
```

**何时选 L1**：读写数据结构相同但逻辑分离，查询优化需求简单。

### L2 — Database Separation

**中等成本**：分离 Command DB 和 Query DB，通过领域事件同步。

```java
// 领域事件
public class OrderPaidEvent extends DomainEvent {
    private final String orderId;
    private final BigDecimal totalAmount;

    public OrderPaidEvent(String orderId, BigDecimal totalAmount) {
        super(orderId);
        this.orderId = orderId;
        this.totalAmount = totalAmount;
    }
}

// 事件处理器 → 同步到 Query DB
@Component
public class OrderPaidEventHandler {
    private final OrderReadRepository readRepo;

    @EventListener
    @Async
    public void on(OrderPaidEvent event) {
        OrderDocument doc = OrderDocument.from(event);
        readRepo.save(doc);   // 写入 Elasticsearch / Query DB
    }
}
```

**何时选 L2**：读负载高，需要独立优化策略，不同存储技术需求。

### L3 — Event Sourcing

**最高成本**：以事件流作为唯一真相源，通过投影重建读模型。

```java
// 事件溯源聚合
public class Order extends EventSourcedAggregate {
    private OrderStatus status;

    public void pay() {
        apply(new OrderPaidEvent(this.id));
    }

    @EventHandler
    private void on(OrderPaidEvent event) {
        this.status = OrderStatus.PAID;
    }
}

// 投影
@Component
public class OrderProjection {
    private final JdbcTemplate jdbc;

    @EventListener
    public void on(OrderPaidEvent event) {
        jdbc.update(
            "UPDATE order_projection SET status = ? WHERE id = ?",
            "PAID", event.getOrderId()
        );
    }
}
```

**何时选 L3**：审计追踪、时间旅行查询、事件重放、完整变更历史。

## 事件处理全流程

### 事件生命周期

```
领域行为 → 构建 DomainEvent → 持久化 → EventBus 发布
                                        ↓
                               ┌────────┴────────┐
                               ↓                  ↓
                        本地处理器 (同步)      MQ 外发 (异步)
                        (同一进程)             (跨服务)
                                                ↓
                                          外部处理器
                                          (幂等 + 补偿)
```

### Domain Event 基类模板

```java
public abstract class DomainEvent {
    private final String eventId;       // UUID
    private final String aggregateId;   // 来源聚合 ID
    private final long occurredAt;      // 时间戳
    private final int version;          // 事件版本

    public DomainEvent(String aggregateId) {
        this.eventId = UUID.randomUUID().toString();
        this.aggregateId = aggregateId;
        this.occurredAt = System.currentTimeMillis();
        this.version = 1;
    }
}
```

### Outbox 表结构

```sql
CREATE TABLE domain_event_outbox (
    id              VARCHAR(36) PRIMARY KEY,
    aggregate_id    VARCHAR(36) NOT NULL,
    aggregate_type  VARCHAR(100) NOT NULL,
    event_type      VARCHAR(200) NOT NULL,
    event_data      JSON NOT NULL,
    schema_version  INT NOT NULL DEFAULT 1,
    occurred_at     DATETIME NOT NULL,
    published       TINYINT NOT NULL DEFAULT 0,
    retry_count     INT NOT NULL DEFAULT 0,
    correlation_id  VARCHAR(36),
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_outbox_published (published, created_at)
);
```

### 发布策略对比

| 策略 | 延迟 | 复杂度 | 场景 |
|------|:----:|:------:|------|
| 轮询发布（定时扫表） | 1-5s | 低 | 中小流量 |
| CDC（Debezium binlog） | < 100ms | 中 | 高流量低延迟 |
| 事务提交回调 | < 10ms | 低 | Spring 项目 |

## 幂等设计

### 四种策略

| 策略 | 开销 | 可靠性 | 最佳场景 |
|------|:----:|:------:|---------|
| **事件去重表** | 中 | ★★★ | 金融级关键事件 |
| **状态机守卫** | 低 | ★★★ | 状态驱动事件 |
| **Redis + TTL** | 低 | ★★☆ | 非关键通知 |
| **业务幂等** | 低 | ★★★ | 简单操作 |

```java
// 策略 1: 事件去重表
@Transactional
public void handle(OrderPaidEvent event) {
    // UNIQUE(event_id) 约束防重
    eventRecordDao.insert(new EventRecord(event.getEventId()));
    // 业务处理...
}

// 策略 2: 状态机守卫
public void pay() {
    if (this.status == OrderStatus.PAID) return;   // 幂等守卫
    this.status = OrderStatus.PAID;
    addDomainEvent(new OrderPaidEvent(this.id));
}

// 策略 3: Redis 去重
public boolean isDuplicate(String eventId) {
    return redisTemplate.opsForValue()
        .setIfAbsent("event:" + eventId, "1", Duration.ofHours(1));
}

// 策略 4: 业务条件幂等
int affected = jdbc.update(
    "UPDATE stock SET stock = stock - ? WHERE stock >= ?",
    quantity, quantity
);
if (affected == 0) return;  // 库存不足或已扣减
```

## 各架构 CQRS 集成模式

| 架构 | 集成点 | 目录结构 |
|------|--------|---------|
| **Layered** | Application 层 Command/Query Service 分离 | `app/service/command/` + `app/service/query/` |
| **Onion** | Core 层 Command/Query UseCase 接口 | `core/application/command/` + `core/application/query/` |
| **Hexagonal** | Port 层 Command Port + Query Port | `domain/port/command/` + `domain/port/query/` |
| **Clean** | UseCase 层 Command Interactor + Query Interactor | `usecase/interactor/command/` + `usecase/interactor/query/` |
| **COLA** | App 层 Command + Query 子模块 | `app/command/` + `app/query/` |

## 落地步骤

```
Phase 1: 评估（1d）
  → 确认是否需要 CQRS → 选择 L1/L2/L3 级别

Phase 2: 命令模型设计（1-2d）
  → 设计 Command 对象 → 实现 CommandHandler → 发布领域事件

Phase 3: 查询模型设计（1-2d）
  → 设计 Query 对象 → 实现 QueryHandler → DTO 组装

Phase 4: 事件同步（L2/L3 需要，1-3d）
  → Outbox 表 → 事件发布器 → 投影更新
  → 幂等策略实现 → 重试/死信机制

Phase 5: 集成测试（1-2d）
  → Command → 领域事件 → Query DB 同步 → 验证最终一致
```

## Gotchas

- **过早升级到 L2/L3**: 不要一上来就分离数据库或 Event Sourcing。先在 L1 验证 CQRS 确实带来价值。大多数项目 L1 就够了。
- **Query 侧直接查写库**: Query 绝不能直接读取 Command 侧的数据库表。即使 L1 共享数据库，也应该读专门的 Read Model。
- **忘了事件幂等**: 领域事件的消费者必须实现幂等。同一个事件可能被投递多次（at-least-once）。
- **事件版本不兼容**: 修改事件结构时必须向后兼容。添加字段可以，删除/重命名字段会破坏消费者。
- **最终一致性的 UI 处理**: L2/L3 下 Command 成功后 Query 数据可能还没更新。前端需要轮询或 WebSocket 推送。
- **过大的聚合**: 事件溯源聚合应保持小聚合原则，过大导致性能问题和事件风暴。

## FAQ

| 问题 | 回答 |
|------|------|
| CQRS 一定会引入最终一致性吗？ | L1 不需要（共享 DB 强一致），L2/L3 需要。 |
| Event Sourcing 和 CQRS 是绑定的吗？ | 不是。ES 可以不配合 CQRS（少见），CQRS 也可以不用 ES（L1/L2）。 |
| 什么时候需要 Outbox 模式？ | 任何需要可靠事件发布的场景。避免双写问题（写 DB + 发 MQ）。 |
| CQRS 和微服务什么关系？ | 正交关系。CQRS 可在单体内部署（L1/L2），也可以跨微服务（L2/L3）。 |
| 查询模型可以复杂到什么程度？ | 可以跨多个聚合、多个微服务组装数据，使用反范式化的物化视图。 |

## Keywords

`CQRS`, `Command Query Responsibility Segregation`, `读写分离`, `Event Sourcing`, `事件溯源`, `Command Bus`, `Query Model`, `Command Model`, `领域事件`, `Domain Event`, `最终一致性`, `Eventual Consistency`, `Outbox Pattern`, `Transactional Outbox`, `Materialized View`, `Projection`, `Event Store`, `Idempotency`, `幂等`, `L1 Model Separation`, `L2 DB Separation`, `L3 Event Sourcing`, `Clean Architecture CQRS`, `Hexagonal CQRS`, `COLA CQRS`, `Layered CQRS`, `Onion CQRS`

## References

- `references/event-governance.md` — 事件驱动工程化治理：Outbox DDL、幂等、重试/死信/补偿/对账、事件契约版本兼容、可观测性
- `references/clean-ddd-hexagonal-cqrs.md` — CQRS & Domain Events：Commands, Queries, Read Models, Event Dispatcher, Outbox Pattern
- `references/cqrs-events.md` — CQRS 领域事件详解：事件分类、事件存储、投影策略、版本管理
- `references/domain-events-deep.md` — 领域事件深入：事件驱动设计原则、聚合内事件 vs 跨服务事件
- `references/domain-vs-integration-events.md` — 领域事件 vs 集成事件：区分定义、边界划分、跨上下文通信
- `references/partme-06-domain-events.md` — 领域事件实操（极客时间）：保险承保案例、事件运行机制、事件总线架构
- `references/ddd4j-cqrs-mindmap.md` — CQRS 思维导图：核心理念、架构模式、命令侧/查询侧组件、一致性模型
- `references/cqrs-mindmap.md` — CQRS 思维导图精简版：适用场景、实施策略、挑战与解决方案

See `examples/` directory for complete runnable examples.

## Examples

See `examples/` directory:
- `examples/order-l1-model-separation.md` — L1 模型分离完整示例（Order 聚合）
- `examples/order-l2-db-separation.md` — L2 数据库分离完整示例（Event Sync）
- `examples/order-l3-event-sourcing.md` — L3 Event Sourcing 完整示例
- `examples/multi-architecture-integration.md` — 5 种架构 CQRS 集成对比示例
- `examples/inventory-cqrs.md` — 库存 CQRS 完整实现（含幂等策略）
