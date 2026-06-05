# 领域事件目录设计指南

## 领域事件识别方法

从事件风暴、用户旅程、业务规则中识别领域事件：

1. **动词过去式测试**: 事件名称必须是过去时（OrderPlaced、PaymentReceived）
2. **业务影响测试**: 事件发生后是否引起后续操作？
3. **独立意义测试**: 事件本身包含足够信息让消费者理解发生了什么

## 领域事件分类

| 类型 | 描述 | 示例 |
|------|------|------|
| **业务事件** | 核心业务流程的关键节点 | OrderSubmitted, PaymentConfirmed |
| **时间事件** | 定时触发的事件 | PaymentTimeout, SubscriptionExpired |
| **外部事件** | 外部系统触发的事件 | ThirdPartyPaymentCallback |
| **状态事件** | 聚合状态变迁 | OrderStatusChanged, PolicyActivated |

## 领域事件数据结构

```java
public abstract class DomainEvent<T extends DomainEventId> {
    private T eventId;
    private LocalDateTime occurredOn;
    private int version;          // 事件 schema 版本

    protected DomainEvent() {
        this.eventId = DomainEventId.generate();
        this.occurredOn = LocalDateTime.now();
        this.version = 1;
    }
}

public class OrderPlaced extends DomainEvent<OrderPlacedId> {
    private OrderId orderId;
    private CustomerId customerId;
    private Money totalAmount;
    private List<OrderItemLine> items;
    private LocalDateTime placedAt;
}
```

## 领域事件发布策略

| 策略 | 模式 | 适用场景 |
|------|------|---------|
| **同步发布** | 事件总线（内存） | 同一进程内、同一微服务内部 |
| **异步发布** | 消息队列（Kafka/RabbitMQ） | 跨微服务、跨限界上下文 |
| **事务性发件箱** | 事件先持久化到 DB，再由发件箱投递 | 保证事件发布与业务操作的事务一致性 |

## 领域事件命名规范

- 使用过去时态: `OrderCreated`, `PaymentReceived`, `InventoryReserved`
- 包含业务含义: 用业务术语而非技术术语
- 层级结构: `{Aggegate}{Action}` 或 `{Domain}{EventType}`

### 常见领域事件示例

```yaml
Order BC:
  - OrderCreated        # 订单创建
  - OrderItemAdded      # 添加订单项
  - OrderSubmitted      # 订单提交
  - OrderPaid           # 订单支付
  - OrderShipped        # 订单发货
  - OrderDelivered      # 订单交付
  - OrderCancelled      # 订单取消
  - OrderRefunded       # 订单退款

Payment BC:
  - PaymentInitiated    # 支付发起
  - PaymentConfirmed    # 支付确认
  - PaymentFailed       # 支付失败
  - PaymentRefunded     # 支付退款

Inventory BC:
  - StockReserved       # 库存预留
  - StockReleased       # 库存释放
  - StockOut            # 出库
  - StockIn             # 入库
```
