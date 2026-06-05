# C4 模型示例 — 电商平台完整四层图

> 本文档提供电商平台的 C4 模型全四层 Mermaid 图例，可直接嵌入架构文档。

---

## L1: System Context Diagram

```mermaid
graph TB
    Customer["👤 顾客"]
    Admin["👤 管理员"]
    Logistics["🚚 物流系统"]
    PaymentGateway["💳 支付网关"]
    SMS["📱 短信服务"]

    subgraph Platform["电商平台"]
        OrderBC["订单上下文"]
        PaymentBC["支付上下文"]
        ProductBC["商品上下文"]
        InventoryBC["库存上下文"]
    end

    Customer -->|"下订单"| OrderBC
    Customer -->|"支付"| PaymentBC
    Admin -->|"管理商品"| ProductBC
    OrderBC -->|"发货通知"| Logistics
    PaymentBC -->|"调用"| PaymentGateway
    OrderBC -->|"验证库存"| InventoryBC
    OrderBC -->|"短信通知"| SMS
```

## L2: Container Diagram — 订单上下文

```mermaid
graph TB
    subgraph OrderContext["订单上下文"]
        OrderAPI["订单 API\n(Spring Boot)"]
        OrderDB[("订单数据库\n(PostgreSQL)")]
        OrderCache["订单缓存\n(Redis)"]
        OrderQueue["订单事件队列\n(RabbitMQ)"]
        Worker["订单处理 Worker\n(Spring Boot)"]
    end

    WebApp["Web App\n(React)"]
    MobileApp["移动 App\n(React Native)"]

    WebApp -->|REST API| OrderAPI
    MobileApp -->|REST API| OrderAPI
    OrderAPI -->|读写| OrderDB
    OrderAPI -->|缓存查询| OrderCache
    OrderAPI -->|发布事件| OrderQueue
    Worker -->|消费事件| OrderQueue
    Worker --> OrderDB
    OrderQueue -->|同步| PaymentContext["支付上下文"]
    OrderQueue -->|通知| Logistics
```

## L3: Component Diagram — 订单上下文的 COLA 四层

```mermaid
graph TB
    subgraph Adapter["适配层"]
        OrderController["OrderController"]
        OrderDTO["OrderDTO"]
    end

    subgraph App["应用层"]
        OrderAppService["OrderAppService"]
        CreateOrderCmd["CreateOrderCommand"]
        CancelOrderCmd["CancelOrderCommand"]
        OrderQueryService["OrderQueryService"]
    end

    subgraph Domain["领域层"]
        Order["Order (聚合根)"]
        OrderItem["OrderItem (实体)"]
        Money["Money (值对象)"]
        OrderRepository["OrderRepository (接口)"]
        OrderDomainService["OrderDomainService"]
        OrderPaidEvent["OrderPaidEvent"]
    end

    subgraph Infra["基础设施层"]
        JpaOrderRepo["JpaOrderRepository"]
        EventPublisher["RabbitMqEventPublisher"]
    end

    OrderController --> OrderAppService
    OrderController --> OrderQueryService
    OrderAppService --> CreateOrderCmd
    OrderAppService --> OrderRepository
    OrderAppService --> OrderDomainService
    Order --> OrderItem
    Order --> Money
    Order --> OrderPaidEvent
    JpaOrderRepo -.->|implements| OrderRepository
    EventPublisher --> OrderQueue
```

## L4: Code Diagram — 订单聚合内部结构

```mermaid
classDiagram
    class Order {
        -OrderId id
        -OrderStatus status
        -Money totalAmount
        -List~OrderItem~ items
        -CustomerId customerId
        -Address shippingAddress
        +pay() void
        +cancel(String reason) void
        +addItem(OrderItem) void
        +removeItem(ProductId) void
        +calculateTotal() Money
        +canBePaid() boolean
    }

    class OrderItem {
        -ProductId productId
        -String productName
        -Money unitPrice
        -int quantity
        +getSubtotal() Money
        +updateQuantity(int) void
    }

    class Money {
        -BigDecimal amount
        -Currency currency
        +add(Money) Money
        +subtract(Money) Money
        +multiply(BigDecimal) Money
        +isGreaterThan(Money) boolean
    }

    class OrderStatus {
        <<enumeration>>
        PENDING_PAYMENT
        PAID
        SHIPPED
        DELIVERED
        CANCELLED
        RETURNING
        +canPay() boolean
        +canCancel() boolean
        +canShip() boolean
    }

    class OrderId {
        -String value
        +generate() OrderId
        +fromString(String) OrderId
    }

    class OrderPaidEvent {
        -OrderId orderId
        -Money amount
        -LocalDateTime paidAt
        +occurredOn() LocalDateTime
    }

    Order "1" --> "*" OrderItem
    Order --> Money
    Order --> OrderId
    Order --> OrderStatus
    Order --> Address
    Order ..> OrderPaidEvent : publishes
```
