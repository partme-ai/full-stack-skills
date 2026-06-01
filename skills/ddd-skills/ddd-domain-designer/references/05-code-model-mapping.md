# 领域对象 → 代码对象映射表


## 代码模型目录结构

```
{project}-domain/
├── {aggregate}/
│   ├── entity/       # 实体 + 聚合根
│   ├── valueobject/  # 值对象
│   ├── event/        # 领域事件
│   ├── service/      # 领域服务
│   └── repository/   # 仓储接口
```

## 领域对象与代码对象映射

| 领域对象 | 代码对象 | 包路径 |
|---------|---------|--------|
| 订单聚合根 | Order | domain/order/entity/Order.java |
| 订单项实体 | OrderItem | domain/order/entity/OrderItem.java |
| 金额值对象 | Money | domain/order/valueobject/Money.java |
| 订单状态 | OrderStatus | domain/order/valueobject/OrderStatus.java |
| 订单已支付事件 | OrderPaidEvent | domain/order/event/OrderPaidEvent.java |
| 订单仓储接口 | OrderRepository | domain/order/repository/OrderRepository.java |
| 订单领域服务 | OrderPricingService | domain/order/service/OrderPricingService.java |

## 代码模型设计原则

1. **包结构按聚合组织**，不是按层组织（domain/order/ 下包含该聚合的所有对象）
2. **充血模型**：实体类包含业务行为方法
3. **聚合间通过 ID 引用**：Order 只持有 CustomerId，不持有 Customer 对象
4. **仓储接口在 Domain 定义**：只定义接口签名，不含实现
5. **领域事件命名过去式**：OrderPaid, OrderCancelled, ProductCreated

## 各层对象与转换

| 层 | 对象类型 | 命名规范 |
|----|---------|---------|
| Interface | VO | XxxVO |
| Interface | Request/Response DTO | XxxRequest, XxxResponse |
| Application | Command/Query | XxxCommand, XxxQuery |
| Application | DTO | XxxDTO |
| Domain | DO (Domain Object) | 实体类名（Order, Customer） |
| Infrastructure | PO (Persistent Object) | XxxPO 或 Entity |

## 松散分层 vs 严格分层

| 策略 | 特点 | 适用 |
|------|------|------|
| 严格分层 | 每层只能调用下一层 | 强制规范，大型项目 |
| 松散分层 | 上层可调用任意下层 | 灵活，中小项目 |

