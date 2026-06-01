# CQRS 实现路径：L1 → L2 → L3 渐进式演进

> CQRS 不是一次性全部引入，而是根据业务复杂度逐步升级。每个 Level 都有明确的判断条件和可逆回退方案。

## CQRS 三级实现速查

| Level | 读写模型 | 数据库 | 同步方式 | 复杂度 | 适用场景 |
|:-----:|---------|:-----:|---------|:-----:|---------|
| **L1** | 代码层分离（Command/Query DTO） | 同一 DB | 同步 | 低 | 读写模型差异小 |
| **L2** | 物理分离（Read Model 独立表） | 同一 DB | 异步（事件） | 中 | 查询需要 JOIN 优化 |
| **L3** | 完全分离（独立读库） | 不同 DB | 异步（事件+CDC） | 高 | 读写性能要求差距大 / Event Sourcing |

---

## L1：代码层分离（Command/Query DTO 分离）

### 判断何时升级到 L1

```
当前状态：所有操作使用同一 Service + 同一 DTO
            → 读返回不必要的字段、写校验混在读模型
触发条件（满足 2 项即可升级）：
  - 读接口字段数 > 写接口字段数 × 2
  - 同一实体有 3+ 种不同的查询视图
  - 写操作响应中包含大量冗余关联数据
```

### 第 1 步：拆分 Command 和 Query Service

```java
// 改造前（混在一起）
@Service
public class OrderService {
    public OrderDTO createOrder(CreateOrderRequest req) { ... }
    public OrderDTO getOrder(String id) { ... }
    public List<OrderDTO> listOrders(OrderQuery query) { ... }
}

// 改造后（L1：代码分离）
@Service
public class OrderCommandService {
    public OrderId createOrder(CreateOrderCommand cmd) {
        Order order = Order.create(cmd.getCustomerId(), cmd.getItems());
        orderRepository.save(order);
        return order.getId();
    }
}

@Service
public class OrderQueryService {
    public OrderDetailDTO getOrder(String id) {
        return orderReadModel.findById(id);
    }
    public PageResult<OrderSummaryDTO> listOrders(OrderQuery query) {
        return orderReadModel.findByCriteria(query);
    }
}
```

### 第 2 步：定义独立的 Query DTO

```java
// 不同查询场景使用不同 DTO
public class OrderDetailDTO {        // 详情页：完整信息
    private String orderId;
    private String status;
    private String totalAmount;
    private List<OrderItemDTO> items;
    private String customerName;
    private String shippingAddress;
}

public class OrderSummaryDTO {        // 列表页：核心字段
    private String orderId;
    private String status;
    private String totalAmount;
    private LocalDateTime createdAt;
}
```

### 第 3 步：验证 L1 完成

```bash
# 检查：Command Service 是否只返回 ID（不返回 DTO）
grep -r "return.*DTO" **/command/  # 应无结果

# 检查：Query DTO 是否不作为写操作的响应
grep -r "QueryService" **/controller/ | grep "POST\|PUT\|DELETE"  # 应无结果
```

### L1 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| Command Handler 返回完整 DTO | 写操作耦合读模型 | 返回 ID + 状态码 |
| QueryService 中包含写操作 | 读写未真正分离 | 拆分到 CommandService |
| 所有查询共用一个 DTO | DTO 膨胀 | 按查询场景定义独立 DTO |

---

## L2：读模型物理分离（同一 DB，独立表/视图）

### 判断何时升级到 L2

```
L1 已实施，且满足以下条件之一：
  - 查询需要 3+ 表 JOIN，响应超过 200ms
  - 不同查询视图 > 5 种，L1 DTO 维护困难
  - 需要数据聚合（SUM/COUNT/GROUP BY）但写模型结构不支持
```

### 第 1 步：设计 Read Model 表

```sql
-- 写模型（规范化）
CREATE TABLE orders (
    id VARCHAR(36) PRIMARY KEY,
    customer_id VARCHAR(36) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    version INT DEFAULT 0
);

-- 读模型（反规范化，专为查询优化）
CREATE TABLE order_read_model (
    order_id VARCHAR(36) PRIMARY KEY,
    customer_id VARCHAR(36),
    customer_name VARCHAR(100),    -- JOIN 结果平铺
    status VARCHAR(20),
    total_amount DECIMAL(12,2),    -- 预计算
    item_count INT,                -- 预计算
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    INDEX idx_customer (customer_id),
    INDEX idx_status_created (status, created_at)
);
```

### 第 2 步：实现 Event Handler 同步 Read Model

```java
@Component
public class OrderReadModelProjector {
    private final OrderReadModelMapper readModelMapper;

    @EventListener
    @Transactional
    public void on(OrderCreatedEvent event) {
        OrderReadModel model = OrderReadModel.builder()
            .orderId(event.getOrderId())
            .customerId(event.getCustomerId())
            .status("DRAFT")
            .createdAt(event.getOccurredAt())
            .build();
        readModelMapper.insert(model);
    }

    @EventListener
    @Transactional
    public void on(OrderPaidEvent event) {
        readModelMapper.updateStatus(event.getOrderId(), "PAID");
    }
}
```

### 第 3 步：Query Service 直接查 Read Model

```java
@Mapper
public interface OrderReadModelMapper {
    OrderDetailDTO findById(@Param("orderId") String orderId);

    List<OrderSummaryDTO> findByCustomer(
        @Param("customerId") String customerId,
        @Param("status") String status,
        @Param("offset") int offset,
        @Param("limit") int limit
    );
}
```

### 第 4 步：验证 L2 完成

```bash
# 检查：写操作不直接查询 Read Model
grep -r "ReadModel" **/command/  # 应无结果

# 检查：Event Handler 覆盖率
# 每个关键业务操作都应有对应的 Event Handler 更新 Read Model
```

### L2 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| 跳过 Outbox 直接发事件 | 事件丢失导致读写不一致 | 事务内写 Outbox |
| Event Handler 耗时过长 | 写事务阻塞 | Handler 异步化，不能放在写事务中 |
| Read Model 只增不改 | 旧数据未被清理 | 加 updated_at 字段和清理策略 |

---

## L3：独立读库（不同 DB 或 ES/Cache）

### 判断何时升级到 L3

```
L2 已实施，且满足以下条件之一：
  - 读 QPS > 写 QPS × 10，且读写竞争同一 DB 连接池
  - 需要全文搜索、实时聚合（ES 场景）
  - 读模型数据量 > 1000 万行，MySQL 查询变慢
  - 需要 Event Sourcing（审计、回放、时间旅行）
```

### 第 1 步：配置独立数据源

```java
@Configuration
public class ReadDataSourceConfig {
    @Bean
    @ConfigurationProperties("spring.datasource.read")
    public DataSource readDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean
    public SqlSessionFactory readSqlSessionFactory() throws Exception {
        SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
        bean.setDataSource(readDataSource());
        return bean.getObject();
    }
}
```

### 第 2 步：同步策略选择

| 同步方式 | 延迟 | 一致性 | 复杂度 | 适用 |
|---------|:---:|:-----:|:-----:|------|
| **CDC (Debezium)** | < 100ms | 最终一致 | 中 | MySQL → ES / PG |
| **Outbox + 消息队列** | 1-5s | 最终一致 | 中 | 跨服务同步 |
| **双写（事务内）** | 0ms | 强一致 | 高 | 要求实时一致 |

```java
// CDC 方式（Debezium 监听 MySQL binlog → Kafka → Consumer 写入 ES）
@Component
public class OrderSyncedToElasticsearch {
    @KafkaListener(topics = "cdc.orders.order_read_model")
    public void syncToES(String orderJson) {
        OrderDoc doc = objectMapper.readValue(orderJson, OrderDoc.class);
        elasticsearchTemplate.index(doc);
    }
}
```

### 第 3 步：验证 L3 完成

```bash
# 检查：写操作依赖只包含写库
grep -r "readDataSource\|readDb" **/command/  # 应无结果

# 检查：读库同步延迟监控
# 监控指标：read_model.updated_at - orders.updated_at 的 p99 < 5s

# 检查：对账机制已配置
# 定时任务检测：order_read_model 中缺失的记录
```

### L3 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| 跳过延迟监控 | 读库滞后数小时无人知 | 对账任务 + data_lag 指标告警 |
| CDC 误删数据 | 读库历史数据丢失 | CDC 用 INSERT+DELETE 日志，不用 TRUNCATE |
| 写库故障影响读 | 全站不可用 | 读服务有读库兜底（缓存/静态数据） |

---

## 逆向回退方案

如果 CQRS 引入后复杂度超出预期，可按以下路径回退：

```
L3 → L2：停用独立读库，Query Service 回退到主库的 Read Model 表
L2 → L1：删除 Read Model 表，Query Service 直接查主库
L1 → 无：合并 Command/Query Service，恢复单一 OrderService

回退检查清单：
- [ ] Read Model 数据是否需要备份
- [ ] 消费者是否依赖独立读库的连接
- [ ] 回退后性能是否可接受（压力测试验证）
```
