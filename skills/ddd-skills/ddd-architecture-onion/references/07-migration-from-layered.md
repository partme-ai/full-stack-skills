# 07 — Migration: From Layered Architecture to Onion

> 从传统三层架构渐进迁移到洋葱架构的完整路径，避免"大爆炸式重写"。

## 迁移策略原则

1. **渐进式** — 每次只迁移一个聚合，不中断现有功能
2. **并行运行** — 新旧架构同时运行，直到全部迁移完成
3. **Strangler Fig 模式** — 新功能走洋葱，老功能逐步搬
4. **测试先行** — 迁移前写测试，迁移后测试通过

## 迁移路线图

```
Phase 1                    Phase 2                     Phase 3                    Phase 4
─────────                  ─────────                   ─────────                  ─────────
原始三层                  分离 Domain 接口            抽取 Application 层         完全洋葱架构

Controller                 Controller                 Controller                 API Layer
   ↓                          ↓                          ↓                          ↓
Service (大泥球)          Service (大泥球)           Application Service         Application Layer
   ↓                          ↓                          ↓                          ↓
Repository                 [Domain Interface] ← 新增     Domain Service            Domain Layer ★
   ↓                          ↓                          ↓                          ↓
DB                         Repository Impl            Repository Impl            Infrastructure
                           DB                         DB                         DB
```

## 详细迁移步骤

### Phase 1：提取 Repository 接口（1-2 天/聚合）

**目标**：将 Repository 接口从 Infrastructure 层提取到 Domain 层

```java
// 迁移前：接口和实现都在 Infrastructure
// infrastructure/repository/OrderRepository.java
public interface OrderRepository {
    Order findById(Long id);
    void save(Order order);
}

// 迁移后：接口移到 Domain，实现留在 Infrastructure
// domain/repository/OrderRepository.java  ← 新位置
public interface OrderRepository {
    Optional<Order> findById(OrderId id);  // 返回 Optional，用值对象 ID
    void save(Order order);
}

// infrastructure/repository/OrderRepositoryImpl.java  ← 保持不变
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    // ... 实现
}
```

**检查点**：
- [ ] Domain 层出现 `repository/` 包
- [ ] 所有 Repository 接口已移到 Domain 层
- [ ] Service 层通过接口引用 Repository（非具体实现类）
- [ ] 单元测试可通过 Mock Repository 接口运行

### Phase 2：Domain 实体充血化（2-3 天/聚合）

**目标**：将 Service 中的业务逻辑移到实体中

```java
// 迁移前：贫血模型 + 上帝 Service
public class Order {         // 纯数据
    private Long id;
    private String status;
    // getter/setter
}

public class OrderService {  // 所有逻辑在这里
    public void pay(Long orderId) {
        Order order = orderRepo.findById(orderId);
        if (!"DRAFT".equals(order.getStatus())) {
            throw new RuntimeException("不可支付");
        }
        order.setStatus("PAID");
        orderRepo.save(order);
    }
}

// 迁移后：充血模型
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;  // 用值对象代替字符串

    public void pay() {
        if (!status.canPay()) {
            throw new DomainException("不可支付");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}

public class OrderApplicationService {  // 薄层编排
    @Transactional
    public void payOrder(String orderId) {
        Order order = orderRepo.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        order.pay();                    // 业务逻辑在实体
        orderRepo.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
    }
}
```

**检查点**：
- [ ] Entity 包含业务方法（不再是纯 setter）
- [ ] 值对象替换字符串/基本类型（`OrderStatus` → `String`，`Money` → `BigDecimal`）
- [ ] Service 层行数降低 50%+（业务逻辑下沉到实体）
- [ ] 关键操作发布领域事件

### Phase 3：分离 Application 层（1-2 天）

**目标**：从 Service 中分离出纯编排的 Application 层

```java
// 迁移前：Service 混杂业务+编排
@Service
public class OrderService {
    @Autowired private OrderRepository orderRepo;
    @Autowired private PaymentClient paymentClient;

    @Transactional
    public void payOrder(Long orderId) {
        // 业务校验
        Order order = orderRepo.findById(orderId);
        if (order.getStatus() != OrderStatus.DRAFT) {
            throw new BusinessException("当前状态不可支付");
        }
        // 编排
        paymentClient.charge(order.getTotalAmount());
        // 持久化
        order.setStatus(OrderStatus.PAID);
        orderRepo.save(order);
    }
}

// 迁移后：Application 层纯编排
// application/service/OrderApplicationService.java
@Service
public class OrderApplicationService {
    private final OrderRepository orderRepo;
    private final PaymentGateway paymentGateway;
    private final EventPublisher eventPublisher;

    public OrderApplicationService(
            OrderRepository orderRepo,
            PaymentGateway paymentGateway,
            EventPublisher eventPublisher) {
        this.orderRepo = orderRepo;
        this.paymentGateway = paymentGateway;
        this.eventPublisher = eventPublisher;
    }

    @Transactional
    public void payOrder(String orderId) {
        Order order = orderRepo.findById(new OrderId(orderId))
            .orElseThrow(() -> new OrderNotFoundException(orderId));
        order.pay(paymentGateway);     // 业务逻辑在 Domain
        orderRepo.save(order);
        eventPublisher.publishAll(order.getDomainEvents());
    }
}
```

**检查点**：
- [ ] Application Service 不含 if/else 业务逻辑
- [ ] 事务注解在 Application 层
- [ ] 构造器注入（非 @Autowired 字段注入）
- [ ] 返回值是 DTO 而非 Domain 实体

### Phase 4：引入值对象和领域事件（2-3 天）

**目标**：用值对象替代基本类型，为关键操作添加领域事件

```java
// 迁移前：基本类型满天飞
public class Order {
    private Long id;
    private Long customerId;
    private BigDecimal amount;
    private String status;
    private String currency;
}

// 迁移后：值对象封装
public class Order extends AggregateRoot<OrderId> {
    private CustomerId customerId;     // 值对象
    private Money totalAmount;         // 值对象（含金额+币种）
    private OrderStatus status;        // 枚举值对象
}
```

### Phase 5：引入 DI 组装模块（1 天）

**目标**：创建独立的 composition 模块集中管理 DI

```xml
<!-- 创建 composition module，依赖所有其他模块 -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-core</artifactId>
</dependency>
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-infrastructure</artifactId>
</dependency>
<dependency>
    <groupId>com.example</groupId>
    <artifactId>order-api</artifactId>
</dependency>
```

### Phase 6：代码审查与测试补齐（1 天）

**检查点**（对照 Gotchas 清单）：
- [ ] Domain 层零框架依赖
- [ ] Repository 接口在 Domain，实现在 Infrastructure
- [ ] Application 层纯编排
- [ ] 值对象不可变
- [ ] 跨聚合通过 ID 引用
- [ ] DI 集中在 composition
- [ ] Domain 层测试覆盖率 > 90%

## 迁移前后对比

| 指标 | 迁移前（三层） | 迁移后（洋葱） |
|------|:-----------:|:------------:|
| Domain 层框架依赖 | 有 | 无 |
| 业务逻辑位置 | Service（散落） | Entity（集中） |
| 值对象使用 | 少 | 多（替代基本类型） |
| 领域事件 | 无 | 关键操作都有 |
| 单元测试难度 | 困难（需启动框架） | 容易（纯 Java） |
| 换数据库代价 | 高（改所有 DAO） | 低（改一个 Repository 实现） |
| 多入口支持 | 困难 | 原生支持 |

## 注意事项

- 不急于一步到位：先做 Phase 1-2（收益最大，风险最小）
- 不影响现有功能：每次迁移都要跑全量测试
- 团队培训：迁移前确保团队理解依赖倒置原则
- 迁移评估：如果项目只剩 3 个月维护期，不建议迁移
