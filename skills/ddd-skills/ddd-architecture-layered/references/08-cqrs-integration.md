# CQRS Integration — CQRS 轻量集成（L1：模型分离）

> 在 DDD 分层架构中，CQRS（Command Query Responsibility Segregation）可以在应用层实现轻量级的读写模型分离，无需引入独立数据库。

## CQRS 三级策略

| 级别 | 说明 | 复杂度 | 适用场景 |
|:----:|------|:------:|---------|
| **L1** | 模型分离：同一数据库，Command Service + Query Service 分离 | ★☆☆ | 分层架构的推荐起点 |
| **L2** | 数据库分离：主库(写) + 从库/ES(读) | ★★☆ | 读写压力差异大的系统 |
| **L3** | Event Sourcing：事件流 + 物化视图 | ★★★ | 审计追踪、时间旅行 |

## L1 模型分离（分层架构推荐）

```
同一个数据库，但区分写模型和读模型：

写路径:                        读路径:
Interface                      Interface
  ↓                              ↓
Application/Command            Application/Query
  ↓                              ↓
Domain (聚合根 + Repository)    Read Model (专为查询优化)
  ↓                              ↓
Infrastructure (DB)            Infrastructure (同一 DB)

关键：写操作通过 Domain 层；读操作直接查询，不走 Domain 层。
```

## 目录结构

```
application/
├── command/                    # 写模型
│   ├── CreateOrderCommand.java
│   ├── PayOrderCommand.java
│   └── CancelOrderCommand.java
├── service/
│   └── OrderCommandService.java   # 写服务（走 Domain）
├── query/                      # 读模型
│   ├── GetOrderQuery.java
│   └── SearchOrdersQuery.java
└── service/
    └── OrderQueryService.java   # 读服务（直接查询）
```

## 写服务示例

```java
@Service
@Transactional
public class OrderCommandService {
    private final OrderRepository orderRepository;

    public void payOrder(PayOrderCommand command) {
        Order order = orderRepository.findById(new OrderId(command.getOrderId()))
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));
        order.pay();
        orderRepository.save(order);
        // 写路径确保领域逻辑完整性
    }
}
```

## 读服务示例

```java
@Service
@Transactional(readOnly = true)
public class OrderQueryService {
    // 直接注入 DAO/ReadModelRepository，不走 Domain 层
    private final OrderReadRepository readRepository;

    public OrderListDTO searchOrders(SearchOrdersQuery query) {
        // 直接查询，不使用聚合根
        return readRepository.search(query.getStatus(), query.getPage(), query.getSize());
    }
}

// 读取专用的 Repository（在 Infrastructure 层）
@Repository
public class OrderReadRepository {
    private final JdbcTemplate jdbcTemplate;

    public OrderListDTO search(String status, int page, int size) {
        String sql = """
            SELECT id, order_number, customer_id, status, total_amount, created_at
            FROM orders
            WHERE (:status IS NULL OR status = :status)
            ORDER BY created_at DESC
            LIMIT :size OFFSET :offset
            """;
        // 返回扁平的 DTO，不需要重构为领域对象
        return jdbcTemplate.query(sql, new OrderListRowMapper());
    }
}
```

## 领域事件桥接（L1→L2 过渡）

如果需要升级到 L2（数据库分离），通过领域事件实现写库 → 读库的数据同步：

```
Aggregate (写) → DomainEvent → EventBus → EventHandler → Query DB (读)
```

```java
// 1. 聚合根发布事件
public class Order extends AggregateRoot<OrderId> {
    public void pay() {
        // ... 业务逻辑 ...
        addDomainEvent(new OrderPaidEvent(this.id, this.customerId, this.totalAmount));
    }
}

// 2. 事件处理器更新读模型
@Component
public class OrderPaidEventHandler {
    private final OrderReadRepository readRepository;

    @EventListener
    public void on(OrderPaidEvent event) {
        // 更新读模型的物化视图
        readRepository.updateOrderStatus(event.getOrderId(), "PAID");
    }
}
```

## 查询优化建议

```
查询 DTO 设计：
  └── 为每个查询场景定义专门的 DTO（不要复用 Domain 对象）
  └── 使用扁平的 DTO，避免嵌套对象
  └── 不同列表可以有不同的 DTO（列表页 vs 详情页）

查询性能优化：
  └── 直接使用 JdbcTemplate/MyBatis，不走 ORM 的完整生命周期
  └── 使用数据库原生查询（JOIN/聚合函数）
  └── 对高频查询加缓存（Redis/本地缓存）

分页查询：
  └── 使用 offset/limit 或 cursor-based 分页
  └── 不加载全部数据到内存
```

## 何时启用 CQRS

```
需要 CQRS L1 的场景：
  └── 读操作和写操作的数据结构差异很大
  └── 查询需要进行大量 JOIN 或聚合
  └── 需要为不同端（Web/iOS/Android）定制查询

不需要 CQRS 的场景：
  └── 以简单 CRUD 为主的系统
  └── 读写使用相同的数据结构
  └── 团队刚接触 DDD（建议先掌握纯四层）
```

## 参考

- [ddd-cqrs-architecture](../../ddd-cqrs-architecture/) — CQRS 完整指南
- Martin Fowler CQRS — CQRS 概念定义
- Microsoft DDD Microservices — CQRS 实现模式
