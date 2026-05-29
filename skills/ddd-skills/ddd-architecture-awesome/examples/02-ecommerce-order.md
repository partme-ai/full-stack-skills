# 电商订单系统 — DDD 端到端示例

基于 DDD 的电商订单系统完整案例，覆盖从战略设计到代码落地的全过程。

## 业务背景

一个典型 B2C 电商平台的订单模块：
- 用户下单 → 库存扣减 → 支付 → 发货 → 签收
- 支持订单改价、取消、退款等逆向流程
- 与会员系统、商品系统、物流系统等外部上下文协作

## 战略设计（Strategic Design）

### 领域划分

| 域 | 类型 | 说明 |
|----|------|------|
| 订单域 | Core Domain | 核心利润来源，需要深度建模 |
| 支付域 | Supporting | 支撑订单完成，可对接第三方 |
| 商品域 | Supporting | 支撑下单展示，可独立演进 |
| 会员域 | Generic | 通用能力，可购买或开源 |

### 限界上下文

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Order BC    │───→│ Payment BC   │───→│  Gateway BC  │
│  (订单上下文)  │    │  (支付上下文)  │    │  (支付网关)   │
└──────┬───────┘    └──────────────┘    └──────────────┘
       │
       │ ACL (防腐层)
       ▼
┌──────────────┐    ┌──────────────┐
│ Product BC   │    │  Member BC   │
│  (商品上下文)  │    │  (会员上下文)  │
└──────────────┘    └──────────────┘
```

### 上下文映射

| 关系 | 上游 | 下游 | 模式 |
|------|------|------|------|
| Order → Payment | Payment BC | Order BC | Customer-Supplier |
| Order → Product | Product BC | Order BC | ACL (Anti-Corruption Layer) |
| Order → Member | Member BC | Order BC | ACL |
| Payment → Gateway | Gateway BC | Payment BC | OHS (Open Host Service) |

## 战术设计（Tactical Design）

### 聚合设计

#### Order 聚合（聚合根：Order）

```
Order (Aggregate Root)
├── OrderId (VO)
├── BuyerId (VO — Member BC 的 ID 引用)
├── OrderStatus (VO: DRAFT → PAID → SHIPPED → DELIVERED → CANCELLED)
├── Money totalAmount (VO)
├── Address shippingAddress (VO)
├── List<OrderItem> items (Entity)
│   ├── ProductId (VO)
│   ├── Money unitPrice (VO)
│   └── int quantity
├── ── 行为 ──
├── void place()           // 下单
├── void pay()              // 支付完成
├── void ship()             // 发货
├── void deliver()          // 签收
├── void cancel(String reason)  // 取消
└── ── 事件 ──
    ├── OrderPlacedEvent
    ├── OrderPaidEvent
    ├── OrderShippedEvent
    └── OrderCancelledEvent
```

#### 聚合设计原则体现

| 原则 | 体现 |
|------|------|
| 小聚合 | Order 聚合仅包含 2 个实体（Order + OrderItem） |
| ID 引用 | Product、Member 通过 ID 引用，不持有对象 |
| 一致性边界 | order.pay() 只改变 Order 状态，库存扣减通过事件异步 |
| 不变量 | canceled 订单不可 pay，delivered 订单不可 cancel |

### 值对象设计

```java
// 不可变值对象
public record Money(BigDecimal amount, Currency currency) {
    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Currency mismatch");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }
}

public record OrderStatus(String code) {
    public static final OrderStatus DRAFT = new OrderStatus("DRAFT");
    public static final OrderStatus PAID = new OrderStatus("PAID");
    public static final OrderStatus SHIPPED = new OrderStatus("SHIPPED");
    public static final OrderStatus DELIVERED = new OrderStatus("DELIVERED");
    public static final OrderStatus CANCELLED = new OrderStatus("CANCELLED");

    public boolean canPay() { return this == DRAFT; }
    public boolean canShip() { return this == PAID; }
    public boolean canCancel() { return this == DRAFT || this == PAID; }
}
```

### 领域事件与流程

```
Order.placed → InventoryDeductionRequested → Inventory.deduct
Order.paid → PaymentConfirmed → Order.status=PAID
Order.paid → ShipmentRequested → Shipment.create
Shipment.picked → OrderShipped → Order.status=SHIPPED
Shipment.delivered → OrderDelivered → Order.status=DELIVERED
```

## 分层架构落地

```
ecommerce-order/
├── order-adapter/            # 适配器层
│   ├── web/                  # REST Controller
│   │   ├── OrderCommandController.java
│   │   └── OrderQueryController.java
│   └── event/                # 事件消费者
│       └── PaymentEventConsumer.java
├── order-app/                # 应用层
│   ├── command/
│   │   ├── PlaceOrderCommand.java
│   │   ├── PayOrderCommand.java
│   │   └── CancelOrderCommand.java
│   ├── query/
│   │   └── OrderQueryService.java
│   └── event/
│       └── OrderEventPublisher.java
├── order-domain/             # 领域层
│   ├── model/
│   │   ├── Order.java        # 聚合根
│   │   ├── OrderItem.java    # 实体
│   │   └── vo/               # 值对象
│   ├── service/
│   │   └── OrderDomainService.java
│   └── repository/
│       └── OrderRepository.java  # 接口
└── order-infrastructure/     # 基础设施层
    ├── repository/
    │   └── OrderRepositoryImpl.java
    └── mapper/
        └── OrderMapper.java
```

## 关键代码片段

### 聚合根示例

```java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private BuyerId buyerId;
    private OrderStatus status;
    private Money totalAmount;
    private Address shippingAddress;
    private List<OrderItem> items = new ArrayList<>();
    private LocalDateTime createdAt;

    public Order(OrderId id, BuyerId buyerId, Address shippingAddress) {
        this.id = id;
        this.buyerId = buyerId;
        this.status = OrderStatus.DRAFT;
        this.shippingAddress = shippingAddress;
        this.createdAt = LocalDateTime.now();
    }

    public void addItem(ProductId productId, Money unitPrice, int quantity) {
        if (this.status != OrderStatus.DRAFT) {
            throw new OrderException("Only draft orders can add items");
        }
        this.items.add(new OrderItem(productId, unitPrice, quantity));
    }

    public void place() {
        if (this.items.isEmpty()) {
            throw new OrderException("Order must have at least one item");
        }
        this.totalAmount = items.stream()
            .map(OrderItem::subtotal)
            .reduce(Money::add)
            .orElseThrow();
        addDomainEvent(new OrderPlacedEvent(this.id, this.totalAmount));
    }

    public void pay() {
        if (!this.status.canPay()) {
            throw new OrderException("Cannot pay order in status: " + this.status);
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }

    public void cancel(String reason) {
        if (!this.status.canCancel()) {
            throw new OrderException("Cannot cancel order in status: " + this.status);
        }
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelledEvent(this.id, reason));
    }
}
```

## 从本案例学到的 DDD 关键点

1. **聚合设计**：Order 聚合只包含紧密相关的 OrderItem，Product 和 Member 通过 ID 引用
2. **值对象**：Money、OrderStatus、Address 都是不可变值对象，自带业务行为
3. **领域事件**：状态变更通过领域事件传播，实现聚合间最终一致性
4. **充血模型**：place()、pay()、cancel() 业务方法在聚合根上，不是 Service
5. **防腐层**：外部上下文数据通过 ACL 转换，不污染本上下文模型
