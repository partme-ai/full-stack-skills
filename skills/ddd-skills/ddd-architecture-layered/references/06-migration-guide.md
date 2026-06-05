# Migration Guide — 三层 → DDD 四层迁移指南

> 本指南帮助将已有的传统三层架构（Controller/Service/DAO）项目逐步迁移到 DDD 四层架构。

## 迁移总览

```
传统三层：               第一次迁移：               目标状态：
Controller              Interface                Interface
  ↓                        ↓                        ↓
Service                  Application              Application
  ↓ (混杂业务+持久化)        ↓                        ↓
DAO/ORM                  Domain + DAO             Domain (纯)
                           ↓ (分步)                  ↓
                         Infrastructure            Infrastructure
```

## 迁移步骤

### Phase A: 准备工作（1-2 天）

1. **评估现状** — 梳理现有代码结构，识别业务模块
2. **项目结构调整** — 创建新的模块目录结构（空）
3. **经验积累** — 团队学习 DDD 分层概念
4. **确定范围** — 选择一个非核心模块作为试点

### Phase B: 接口层分离（1-2 天）

**Before（三层）**:
```
controller/
  └── OrderController.java    // 含业务逻辑
service/
  └── OrderService.java       // 含 Controller 调用
```

**After（四层）**:
```
interface/
  └── controller/OrderController.java  // 纯协议转换
application/
  └── service/OrderApplicationService.java  // 纯编排
```

**操作**:
1. 将 Controller 中的业务逻辑移到 Application Service
2. 引入 DTO，Controller 只做 DTO ↔ Command 转换
3. 保持现有 Service 类不动（下阶段拆分）

### Phase C: 领域层提取（2-5 天）

**Before**:
```java
@Service
public class OrderService {
    @Autowired
    private OrderMapper orderMapper;  // MyBatis DAO

    @Transactional
    public void pay(Long orderId) {
        // 1. 查询
        OrderDO orderDO = orderMapper.findById(orderId);
        // 2. 业务判断（三层中混杂在 Service）
        if (!"DRAFT".equals(orderDO.getStatus())) {
            throw new BizException("不可支付");
        }
        // 3. 更新
        orderDO.setStatus("PAID");
        orderMapper.update(orderDO);
    }
}
```

**After**:
```java
// Domain 层
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;

    public void pay() {
        if (!status.canPay()) {
            throw new OrderException("当前状态不可支付");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}

public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
}

// Application 层
@Service
public class OrderApplicationService {
    private final OrderRepository orderRepository;

    @Transactional
    public void payOrder(PayOrderCommand command) {
        Order order = orderRepository.findById(new OrderId(command.getOrderId()))
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));
        order.pay();
        orderRepository.save(order);
    }
}

// Infrastructure 层
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    // 实现持久化，可以重用旧的 OrderMapper
}
```

### Phase D: 基础设施层分离（2-3 天）

**操作**:
1. 将 DAO/ORM 代码移到 Infrastructure 层
2. Domain 层定义 Repository 接口
3. Infrastructure 实现 Repository（可重用旧代码）
4. 引入 PO ↔ DO 映射

### Phase E: 引入领域事件（2-3 天）

**操作**:
1. 识别关键业务变更点
2. 定义领域事件实体（`OrderPlaced`, `OrderPaid`）
3. 在聚合根中添加事件发布
4. 在 Infrastructure 层实现事件发布

### Phase F: 验证与修复（1 天）

1. 运行现有测试，确保功能不变
2. 添加 Domain 层单元测试
3. 集成 ArchUnit 验证依赖方向
4. 用 `ddd-code-reviewer` 审查

## 迁移策略

### 策略 A：渐进式（推荐）

```
新功能 → DDD 四层
老功能 → keep 三层，逐步迁移
```

- 适合：大型项目，无法一次重构
- 优点：风险低，可逐步验证
- 周期：2-4 周完成核心模块

### 策略 B：大爆炸式

```
一次性将所有代码改为四层
```

- 适合：小型项目（< 10 个类）
- 优点：一次性完成，没有过渡期
- 风险：高，需要充分测试

### 策略 C：Strangler Fig（绞杀者模式）

```
新建 DDD 模块 → 流量逐步切到新模块 → 下线老模块
```

- 适合：有 API Gateway 的项目
- 优点：零停机迁移
- 周期：1-3 个月

## 迁移检查清单

- [ ] 选定试点模块（非核心，2-3 个聚合）
- [ ] 创建新的模块目录结构
- [ ] 将 Controller 中的业务逻辑迁到 AppService
- [ ] 将 Service 中的业务逻辑迁到 Domain Entity
- [ ] 将 DAO 代码迁到 Infrastructure Repository
- [ ] 引入 PO ↔ DO 映射层
- [ ] 引入领域事件（关键操作）
- [ ] 添加 Domain 层单元测试
- [ ] 集成 ArchUnit 检查
- [ ] 运行 ddd-code-reviewer
- [ ] 旧代码全部迁完后删除三层目录

## 常见陷阱

| 陷阱 | 说明 | 避免方法 |
|------|------|---------|
| 一次迁移太多 | 项目风险高 | 渐进式迁移 |
| 新旧混合 | 同一功能部分三层部分四层 | 明确边界 |
| 忽略测试 | 重构后功能出错 | 先写测试再迁移 |
| Domain 不纯 | 遗留 JPA 注解 | 新 Domain 类从零写 |
| 过度工程 | 简单 CRUD 也四层 | 评估业务复杂度 |
