# Migration — 逐步迁移指南

## 概述

从现有架构（如传统三层架构）迁移到六边形架构，推荐采用侵略性藤蔓模式（Strangler Fig Pattern），逐步替换而非一次性重写。

## 迁移路径

```
传统三层架构 → DDD 四层架构 → 六边形架构（端口适配器）
     ↓               ↓               ↓
   Phase 1        Phase 2         Phase 3
```

## Phase 1: 识别边界（1-2 周）

### 目标
识别当前的模块边界和依赖关系，确定迁移范围。

### 步骤

```
1. 绘制当前架构图
   ┌─────────────────┐
   │   Controller     │  ← 识别业务逻辑是否泄漏到 Controller
   ├─────────────────┤
   │   Service       │  ← 识别上帝 Service
   ├─────────────────┤
   │   Repository    │  ← 识别 SQL 是否分散在各层
   └─────────────────┘

2. 识别候选聚合
   - 找 Entity 和值对象候选
   - 标记贫血模型
   - 确定聚合边界

3. 确定迁移范围
   - 全量迁移 vs 渐进迁移
   - 核心聚合优先 vs 非核心模块先试水
```

### 产出物
- 当前架构评估报告
- 聚合边界识别清单
- 迁移范围决策

## Phase 2: 抽取 Domain 层（3-4 周）

### 目标
创建独立的 Domain 模块，将业务逻辑从 Service 迁入实体。

### 步骤

```java
// 1. 创建 domain 模块
// {project}-domain/
// ├── model/         —— 实体、值对象（从现有 Entity 迁移）
// ├── service/       —— 领域服务
// ├── event/         —— 领域事件
// └── port/          —— 端口定义（先只定义出站端口）

// 2. 创建值对象
// Before: String 表示
public class Order {
    private String status;        // ❌ 字符串
    private BigDecimal amount;    // ❌ 裸 BigDecimal
}

// After: 值对象封装
public class Order {
    private OrderStatus status;  // ✅ 值对象
    private Money amount;        // ✅ 值对象
}

// 3. 充血模型改造
// Before: 贫血模型
public class Order {
    private String status;
    public void setStatus(String status) { this.status = status; }
}
// Service 中: if ("DRAFT".equals(order.getStatus())) { order.setStatus("PAID"); }

// After: 充血模型
public class Order {
    private OrderStatus status;
    public void pay() {
        if (!status.canPay()) throw new OrderException("不可支付");
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}
```

### 里程碑检查清单
- [ ] Domain 模块独立编译，零框架依赖
- [ ] 核心实体已改为充血模型
- [ ] 值对象已替代主要字符串/基本类型字段
- [ ] 出站端口接口已在 Domain 层定义
- [ ] Domain 层单元测试全部通过

## Phase 3: 抽取 Application 层 + 适配器（2-3 周）

### 目标
创建 Application 层和 Adapter 层，实现完整的端口/适配器分离。

### 步骤

```java
// 1. 定义入站端口
// domain/port/inbound/CreateOrderUseCase.java
public interface CreateOrderUseCase {
    OrderCreatedResult execute(CreateOrderCommand command);
}

// 2. 创建应用服务（实现入站端口）
// application/service/CreateOrderService.java
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepository orderRepository;  // 出站端口注入
    // ... 编排逻辑
}

// 3. 抽取适配器
// 旧 Controller → 拆分为 Adapter + DTO
// adapter/inbound/web/OrderController.java
@RestController
public class OrderController {
    private final CreateOrderUseCase createOrderUseCase;  // 注入端口而非 Service
    // ... 仅协议转换
}

// 4. 分离持久化实现
// adapter/outbound/persistence/PostgresOrderRepository.java
@Repository
public class PostgresOrderRepository implements OrderRepository {
    // 实现 Domain 层定义的端口
}

// 5. 替换老代码调用
// Before:
// orderService.createOrder(request);
//
// After:
// createOrderUseCase.execute(request.toCommand());
```

### 回退策略

```java
// 过渡期间双向运行（新旧并存）
@Service
public class OrderServiceFacade {
    private final CreateOrderUseCase newImpl;
    private final LegacyOrderService legacyImpl;

    public void createOrder(CreateOrderRequest request) {
        // 新实现
        var result = newImpl.execute(request.toCommand());
        // 老实现（用于对比验证）
        legacyImpl.createOrder(request);
    }
}
```

## 迁移优先级

| 优先级 | 模块 | 说明 | 预估工期 |
|--------|------|------|---------|
| P0 | 核心聚合（Order/Payment） | 业务最复杂，收益最高 | 2-3 周 |
| P1 | 支撑模块（User/Product） | 相对独立，适合先行 | 1-2 周 |
| P2 | 报表/查询模块 | 读多写少，风险低 | 1 周 |
| P3 | 非核心集成 | 外部系统对接 | 按需 |

## 迁移风险与应对

| 风险 | 影响 | 概率 | 应对策略 |
|------|------|------|---------|
| 业务中断 | 高 | 低 | 渐进迁移 + 回退机制 |
| 团队学习曲线 | 中 | 高 | 培训 + 代码审查 + 内部文档 |
| 与现有 CI/CD 不兼容 | 中 | 中 | 分模块构建，逐步集成 |
| 性能回归 | 中 | 中 | 端口抽象增加间接调用开销，关注关键路径 |
| 代码膨胀 | 低 | 中 | 端口粒度控制，不做过早抽象 |

## 迁移完成检查清单

- [ ] 所有业务逻辑在 Domain 层，零框架依赖
- [ ] 所有出站端口由 Adapter 层实现，Application 层只依赖端口接口
- [ ] 入站 Adapter 仅做协议转换，不包含业务逻辑
- [ ] Domain 层单元测试可在不启动 Spring 的情况下全部通过
- [ ] 所有 Repository 实现与 Domain 接口匹配
- [ ] DI 配置集中在独立模块
- [ ] 旧的 Service 层代码已移除或标记为 @Deprecated
- [ ] ArchUnit 测试已集成 CI，自动检查依赖方向
