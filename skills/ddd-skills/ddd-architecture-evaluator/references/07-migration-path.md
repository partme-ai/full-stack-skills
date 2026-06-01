# 从 MVC/贫血到 DDD/充血 — 迁移路径


## 6 步渐进迁移

```
传统 MVC（贫血模型）
  ↓ Step 1: 识别限界上下文与聚合
  ↓ Step 2: 提取值对象（Money → Email → PhoneNumber）
  ↓ Step 3: 把业务规则从 Service 搬到 Entity（充血）
  ↓ Step 4: 引入 Repository 接口（Domain 定义，Infra 实现）
  ↓ Step 5: 用领域事件替代直接 Service 调用（跨聚合）
  ↓ Step 6: 把 Controller 变成薄适配器
DDD 分层架构（充血模型）
```

## Step 1: 识别限界上下文与聚合

**操作**：
- 用事件风暴识别领域事件和命令
- 找出聚合根（有独立生命周期、全局唯一 ID）
- 划定聚合边界（一次事务只改一个聚合）

**产出**：限界上下文清单 + 聚合清单

## Step 2: 提取值对象

**操作**：
- 把 String status → OrderStatus 枚举/类
- 把 BigDecimal amount + String currency → Money 值对象
- 把 String email → Email 值对象（含格式校验）

**收益**：类型安全、自校验、业务语义清晰

## Step 3: 充血化

**操作**：
- 把 OrderService.pay(orderId) 中的逻辑移到 Order.pay()
- 把 OrderService.cancel(orderId, reason) 移到 Order.cancel(reason)
- 把 OrderService.calculateTotal(orderId) 移到 Order.calculateTotal()

**检验标准**：Order 实体不再只有 getter/setter

## Step 4: 引入 Repository 接口

**操作**：
- 在 Domain 层定义 `interface OrderRepository { save(); findById(); }`
- 在 Infrastructure 层实现（JPA/MyBatis）
- 应用服务注入接口，不直接依赖 ORM

**检验**：Domain 层无 `@Entity`, `@Repository`, `@Table`

## Step 5: 领域事件替代直接调用

**操作**：
- 跨聚合操作改为 `addDomainEvent(new OrderPaid(orderId))`
- 应用层统一发布领域事件
- 事件处理器完成后续操作

**收益**：聚合解耦，支持 1→N 订阅

## Step 6: Controller 薄化

**操作**：
- Controller 只做协议转换（HTTP → Command）
- 业务逻辑全部在 Domain + Application
- DTO 转换在 Application 层完成

**检验**：Controller 无 if/else 业务判断

## 源代码

