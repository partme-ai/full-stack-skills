# 库存 CQRS 完整实现 — 含幂等策略

> 业务：库存扣减 + 库存查询 | 侧重幂等性和并发控制

## 业务场景

商品下单 → 扣减库存 → 发布 StockDeductedEvent → 同步到库存视图

## 幂等设计实现

### 方案 1: 事件去重表

```sql
CREATE TABLE idempotent_event (
    event_id        VARCHAR(36) PRIMARY KEY,
    event_type      VARCHAR(100) NOT NULL,
    status          VARCHAR(20) NOT NULL DEFAULT 'PROCESSING',
    handler_name    VARCHAR(200) NOT NULL,
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    processed_at    DATETIME
);
```

```java
@Component
public class IdempotentEventHandler {
    private final JdbcTemplate jdbc;

    public boolean tryProcess(String eventId, String eventType, String handlerName) {
        try {
            jdbc.update("""
                INSERT INTO idempotent_event
                    (event_id, event_type, status, handler_name)
                VALUES (?, ?, 'PROCESSING', ?)
                """,
                eventId, eventType, handlerName);
            return true;  // 首次处理
        } catch (DuplicateKeyException e) {
            // 重复事件，检查状态
            String status = jdbc.queryForObject(
                "SELECT status FROM idempotent_event WHERE event_id = ?",
                String.class, eventId);
            return "FAILED".equals(status);  // 失败重试
        }
    }

    public void markSuccess(String eventId) {
        jdbc.update(
            "UPDATE idempotent_event SET status = 'SUCCESS', processed_at = NOW()",
            eventId);
    }

    public void markFailed(String eventId) {
        jdbc.update(
            "UPDATE idempotent_event SET status = 'FAILED' WHERE event_id = ?",
            eventId);
    }
}
```

### 方案 2: 业务条件幂等（库存扣减）

```java
@Component
public class InventoryCommandHandler {
    private final JdbcTemplate jdbc;

    @Transactional
    public DeductResult deductStock(DeductStockCommand command) {
        // 幂等扣减: stock >= quantity 时才扣减
        int affected = jdbc.update("""
            UPDATE inventory
            SET stock = stock - ?,
                version = version + 1
            WHERE product_id = ?
              AND stock >= ?
              AND version = ?
            """,
            command.getQuantity(),
            command.getProductId(),
            command.getQuantity(),
            command.getExpectedVersion());

        if (affected == 0) {
            Inventory current = jdbc.queryForObject(
                "SELECT stock, version FROM inventory WHERE product_id = ?",
                (rs, row) -> new Inventory(
                    rs.getInt("stock"),
                    rs.getInt("version")),
                command.getProductId());
            if (current == null) {
                throw new ProductNotFoundException(command.getProductId());
            }
            if (current.stock() < command.getQuantity()) {
                return DeductResult.insufficient(current.stock());
            }
            // 并发冲突
            return DeductResult.conflict(current.version());
        }
        return DeductResult.success();
    }
}
```

### 方案 3: 状态机守卫（订单级幂等）

```java
public class InventoryReservation extends AggregateRoot<ReservationId> {
    private ReservationStatus status;
    private String productId;
    private int quantity;

    public void confirm() {
        if (status == ReservationStatus.CONFIRMED) {
            return;  // 幂等：已确认则不重复处理
        }
        if (status != ReservationStatus.PENDING) {
            throw new InventoryException("当前状态不可确认: " + status);
        }
        this.status = ReservationStatus.CONFIRMED;
        addDomainEvent(new ReservationConfirmedEvent(this.id));
    }

    public void cancel() {
        if (status == ReservationStatus.CANCELLED) {
            return;  // 幂等：已取消
        }
        this.status = ReservationStatus.CANCELLED;
        addDomainEvent(new ReservationCancelledEvent(this.id));
    }
}
```

## 完整调用链

```java
// 1. Command 入口
@RestController
@RequestMapping("/api/v1/inventory")
public class InventoryController {
    private final InventoryCommandHandler commandHandler;
    private final InventoryQueryHandler queryHandler;

    @PostMapping("/deduct")
    public DeductResult deductStock(@RequestBody DeductStockCommand command) {
        return commandHandler.deductStock(command);
    }

    @GetMapping("/{productId}")
    public InventoryView getInventory(@PathVariable String productId) {
        return queryHandler.getInventory(productId);
    }
}

// 2. 事件发布
@Component
public class StockDeductedEventHandler {
    private final IdempotentEventHandler idempotentHandler;
    private final InventoryReadRepository readRepo;

    @Async
    @Transactional
    public void on(StockDeductedEvent event) {
        String eventId = event.getEventId();
        if (!idempotentHandler.tryProcess(eventId, "StockDeductedEvent", "StockDeductedEventHandler")) {
            return;
        }
        try {
            // 更新库存视图
            readRepo.updateStock(event.getProductId(), event.getRemainingStock());
            idempotentHandler.markSuccess(eventId);
        } catch (Exception e) {
            idempotentHandler.markFailed(eventId);
            throw e;  // 触发重试
        }
    }
}

// 3. 查询侧
@Service
public class InventoryQueryHandler {
    private final InventoryReadRepository readRepo;
    private final RedisTemplate<String, InventoryView> redis;

    public InventoryView getInventory(String productId) {
        // 缓存提升读性能
        return redis.opsForValue()
            .get("inventory:" + productId, InventoryView.class)
            .orElseGet(() -> {
                InventoryView view = readRepo.findByProductId(productId);
                redis.opsForValue().set("inventory:" + productId, view, Duration.ofSeconds(30));
                return view;
            });
    }
}
```

## 幂等策略对比

| 策略 | 代码量 | 性能 | 可靠性 | 适用场景 |
|------|:-----:|:----:|:-----:|---------|
| 去重表 (DB) | 中 | 中 | ★★★ | 跨服务事件，需要持久化去重 |
| 业务条件 (SQL) | 低 | 高 | ★★★ | 库存扣减、余额扣减等数值操作 |
| 状态机守卫 | 低 | 高 | ★★★ | 状态驱动实体（订单、审批） |
| Redis + TTL | 低 | 高 | ★★☆ | 非关键通知、缓存刷新 |

## 完整测试

```java
@SpringBootTest
class InventoryCqrsTest {

    @Test
    void deductStock_幂等_同一命令重复执行() {
        DeductStockCommand command = new DeductStockCommand("PROD-001", 2, 1);
        commandHandler.deductStock(command);  // 第一次：成功扣减
        DeductResult result = commandHandler.deductStock(command);  // 第二次：版本冲突
        assertThat(result.isConflict()).isTrue();
    }

    @Test
    void eventHandler_幂等_同一事件重复投递() {
        StockDeductedEvent event = new StockDeductedEvent("PROD-001", 98);
        eventHandler.on(event);   // 第一次：正常处理
        eventHandler.on(event);   // 第二次：幂等跳过
        InventoryView view = queryHandler.getInventory("PROD-001");
        assertThat(view.getStock()).isEqualTo(98);
    }
}
```
