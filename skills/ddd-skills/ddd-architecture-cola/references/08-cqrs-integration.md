# COLA v5 CQRS 集成模式

## CQRS 在 COLA 中的目录体现

```
{project}-app/
├── executor/
│   ├── command/         # 写操作执行器（CQRS 的 Command Side）
│   │   ├── customer/
│   │   │   ├── CustomerCreateCmdExe.java
│   │   │   ├── CustomerUpdateCmdExe.java
│   │   │   └── CustomerDeleteCmdExe.java
│   │   └── order/
│   │       ├── OrderCreateCmdExe.java
│   │       ├── OrderPayCmdExe.java
│   │       └── OrderCancelCmdExe.java
│   └── query/           # 读操作执行器（CQRS 的 Query Side）
│       ├── customer/
│       │   ├── CustomerGetQryExe.java
│       │   └── CustomerSearchQryExe.java
│       └── order/
│           ├── OrderGetQryExe.java
│           └── OrderListQryExe.java
├── model/
│   ├── command/         # 命令对象（写请求 DTO）
│   │   ├── CustomerCreateCmd.java
│   │   ├── OrderPayCmd.java
│   │   └── OrderCancelCmd.java
│   └── query/           # 查询对象（读请求 DTO）
│       ├── CustomerGetQry.java
│       ├── CustomerSearchQry.java
│       └── OrderListQry.java
└── service/             # 可选：传统编排方式（非 CQRS 场景）
```

## CQRS 三级落地策略

### L1 — 模型分离（推荐起步）

同一数据源，仅代码层面分离命令和查询：

```java
// 命令执行器（写）
@CommandExecutor
public class OrderCreateCmdExe {
    @Resource
    private OrderRepository orderRepository;

    @Override
    public OrderDTO execute(OrderCreateCmd cmd) {
        Order order = Order.create(cmd);
        orderRepository.save(order);
        return OrderAssembler.toDTO(order);
    }
}

// 查询执行器（读）
@QueryExecutor
public class OrderGetQryExe {
    @Resource
    private OrderRepository orderRepository;

    @Override
    public OrderDTO execute(OrderGetQry qry) {
        return orderRepository.findById(new OrderId(qry.getId()))
            .map(OrderAssembler::toDTO)
            .orElseThrow(() -> new OrderNotFoundException(qry.getId()));
    }
}
```

### L2 — 数据库分离（中级）

命令写主库，查询读从库/ES：

```java
// 命令执行器 → 写主库
@CommandExecutor
public class OrderCreateCmdExe {
    @Resource
    @Qualifier("primaryOrderRepository")  // 主库
    private OrderRepository orderRepository;

    @Override
    @Transactional
    public OrderDTO execute(OrderCreateCmd cmd) {
        Order order = Order.create(cmd);
        order.addDomainEvent(new OrderCreatedEvent(order));
        orderRepository.save(order);
        return OrderAssembler.toDTO(order);
    }
}

// 查询执行器 → 读从库
@QueryExecutor
public class OrderListQryExe {
    @Resource
    @Qualifier("readonlyOrderRepository")  // 从库
    private OrderRepository orderRepository;

    @Override
    public PageResult<OrderDTO> execute(OrderListQry qry) {
        return orderRepository.findByPage(qry.toPageRequest());
    }
}
```

### L3 — Event Sourcing（高级）

事件溯源 + 物化视图：

```java
// 命令执行器 → 只写事件流
@CommandExecutor
public class OrderCreateCmdExe {
    @Resource
    private EventStore eventStore;

    @Override
    public OrderDTO execute(OrderCreateCmd cmd) {
        OrderCreated event = new OrderCreated(
            new OrderId(UUID.randomUUID().toString()),
            cmd.getCustomerId(),
            cmd.getItems()
        );
        eventStore.append(event);  // 只追加，不保存状态
        return OrderDTO.from(event);
    }
}

// 查询执行器 → 读物化视图
@QueryExecutor
public class OrderGetQryExe {
    @Resource
    private OrderProjectionRepository projectionRepo;

    @Override
    public OrderDTO execute(OrderGetQry qry) {
        return projectionRepo.findById(qry.getId())
            .orElseThrow(() -> new OrderNotFoundException(qry.getId()));
    }
}
```

## 幂等设计

### 1. 事件表去重

```sql
CREATE TABLE idempotent_event (
    event_id    VARCHAR(64) PRIMARY KEY,   -- 唯一事件 ID
    event_type  VARCHAR(64) NOT NULL,
    status      VARCHAR(16) NOT NULL,      -- PROCESSED / PENDING
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### 2. 状态机防护

```java
public enum OrderStatus {
    DRAFT {          // 草稿
        @Override
        public boolean canPay() { return true; }
        @Override
        public boolean canCancel() { return true; }
    },
    PAID {           // 已支付（终态）
        @Override
        public boolean canPay() { return false; }
        @Override
        public boolean canCancel() { return true; }
    },
    CANCELLED {      // 已取消（终态）
        @Override
        public boolean canPay() { return false; }
        @Override
        public boolean canCancel() { return false; }
    };

    public abstract boolean canPay();
    public abstract boolean canCancel();
}
```

### 3. Redis 轻量去重

```java
@Component
public class IdempotentHelper {
    @Resource
    private StringRedisTemplate redisTemplate;

    public boolean tryProcess(String eventId) {
        return Boolean.TRUE.equals(
            redisTemplate.opsForValue()
                .setIfAbsent("idempotent:" + eventId, "1", Duration.ofHours(24))
        );
    }
}
```

## CQRS 各层职责总结

| 组件 | 目录 | 职责 |
|------|------|------|
| Command Object | `app/model/command/` | 写操作请求 DTO，包含 `validate()` |
| Query Object | `app/model/query/` | 读操作请求 DTO |
| Command Executor | `app/executor/command/` | 写操作编排（事务） |
| Query Executor | `app/executor/query/` | 读操作编排（无事务） |
| Event Executor | `app/executor/event/` | 领域事件处理 |
| Event Handler | `app/eventhandler/` | 事件监听处理器 |
| App Service | `app/service/` | 非 CQRS 的传统编排方式 |
