# DDD Building Blocks 与命名约定

## 聚合大小度量表

| 指标 | 健康 | 警告 | 行动 |
|------|------|------|------|
| 每聚合实体数 | 1-5 | 6-10 | >10: 拆分 |
| 聚合根代码行数 | <500 | 500-1000 | >1000: 拆分 |
| 事务锁时间 | <100ms | 100-500ms | >500ms: 拆分 |
| 并发修改冲突 | 极少 | 偶尔 | 频繁: 拆分 |

## 文件命名约定

```
domain/
├── order/
│   ├── Order.java        # 聚合根
│   ├── OrderItem.java    # 实体
│   ├── value_objects.java # OrderId, Money, OrderStatus
│   ├── events.java        # OrderCreated, OrderPaid, OrderShipped
│   ├── repository.java    # OrderRepository（接口）
│   ├── services.java      # 领域服务
│   └── errors.java        # OrderException

application/
├── place_order/
│   ├── command.java       # PlaceOrderCommand
│   ├── handler.java       # PlaceOrderHandler
│   └── port.java          # IPlaceOrderUseCase

infrastructure/
├── postgres/
│   ├── order_repository.java  # PostgresOrderRepository
│   └── mappers/
│       └── order_mapper.java  # Domain ↔ DB 映射
```

## 六边形端口命名约定

| 类型 | 模式 | 示例 |
|------|------|------|
| Driver Port | `I{Action}UseCase` | `IPlaceOrderUseCase`, `IGetOrderUseCase` |
| Driven Port | `I{Resource}Repository` | `IOrderRepository`, `IProductRepository` |
| Driven Port | `I{Action}Service` | `IPaymentService`, `INotificationService` |
| Driven Port | `I{Resource}Gateway` | `IPaymentGateway`, `IShippingGateway` |

## 文件命名约定（TypeScript 版）

```
domain/
├── order/
│   ├── order.ts           # 聚合根
│   ├── order_item.ts      # 实体
│   ├── value_objects.ts   # OrderId, Money 等
│   ├── events.ts          # OrderCreated 等
│   ├── repository.ts      # IOrderRepository
│   ├── services.ts        # 领域服务
│   └── errors.ts          # OrderError 等

application/
├── place_order/
│   ├── command.ts         # PlaceOrderCommand
│   ├── handler.ts         # PlaceOrderHandler
│   └── port.ts            # IPlaceOrderUseCase

infrastructure/
├── postgres/
│   ├── order_repository.ts  # PostgresOrderRepository
│   └── mappers/
│       └── order_mapper.ts  # Domain ↔ DB 映射
```

## 依赖规则矩阵

|  | Domain | Application | Infrastructure |
|--|:--:|:--:|:--:|
| **Domain** | ✅ | ❌ | ❌ |
| **Application** | ✅ | ✅ | ❌ |
| **Infrastructure** | ✅ | ✅ | ✅ |

✅ = 可以依赖  ❌ = 不可以依赖

## 复杂度阶梯速查

```
Level 1: Simple layered（Controller → Service → Repository）
   ↓ 业务规则变得复杂
Level 2: Domain model（Entities with behavior）
   ↓ 需要多个入口
Level 3: Hexagonal（Ports & Adapters）
   ↓ 读写模式显著分化
Level 4: CQRS（Separate read/write models）
   ↓ 需要完整审计追踪
Level 5: Event Sourcing（Store events, derive state）

不要跳级。每一级增加真实的复杂度。只在证明当前级别不够时才升级。
```

## Entity vs Value Object 速判

```
Entity or Value Object?
├─ Has unique identity that persists → Entity
├─ Defined only by its attributes    → Value Object
├─ "Is this THE same thing?"         → Entity (identity comparison)
└─ "Does this have the same value?"  → Value Object (structural equality)
```

## Aggregate 边界速判

```
Aggregate boundaries?
├─ Must be consistent together in a transaction → Same aggregate
├─ Can be eventually consistent                 → Separate aggregates
├─ Referenced by ID only                        → Separate aggregates
└─ >10 entities in aggregate                    → Split it
```

## Domain Service or Entity method? 速判

```
Does it naturally belong to one entity?
├─ YES → Entity method
└─ NO ↓

Does it require multiple aggregates?
├─ YES → Domain Service
└─ NO ↓

Is it stateless business logic?
├─ YES → Domain Service
└─ NO → Reconsider placement
```

## 部分端口位置变体

DDD 为中心的布局：aggregate repository 接口放在 `domain/{aggregate}/repository/`
更严格 Hexagonal 布局：所有 driven ports 放在 `application/ports/driven/`
两种都可以，关键是依赖仍然指向内，infrastructure 实现而非拥有抽象。
