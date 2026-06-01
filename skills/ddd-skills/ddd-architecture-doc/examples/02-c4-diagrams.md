# C4 图完整示例 — 电商平台

> 本文档展示电商平台完整的 C4 四层图示例。
> 所有图表使用 Mermaid 格式，可直接嵌入架构文档。

---

## L1: System Context — 电商平台全景

```mermaid
graph TB
    Customer["👤 顾客"]
    Admin["👤 管理员"]
    Supplier["🏭 供应商"]
    Logistics["🚚 物流系统"]
    PaymentGW["💳 支付网关"]
    SMSService["📱 短信服务"]

    subgraph Platform["🧩 电商平台"]
        direction TB
        BC1["订单系统"]
        BC2["支付系统"]
        BC3["商品系统"]
        BC4["库存系统"]
        BC5["用户系统"]
    end

    Admin -->|管理商品/订单| BC3
    Customer -->|浏览下单| BC1
    Customer -->|支付| BC2
    Supplier -->|供货| BC4
    BC1 -->|发货| Logistics
    BC2 -->|调用| PaymentGW
    BC1 -->|短信通知| SMSService
```

**说明**：L1 图展示电商平台与外部角色的交互。这是给业务方和架构师看的"电梯演讲"图。

---

## L2: Container — 订单系统内部容器

```mermaid
graph TB
    subgraph OrderSystem["📦 订单系统"]
        OrderAPI["Order API\n(Spring Boot)"]
        OrderWorker["Order Worker\n(Spring Boot)"]
        OrderDB[("Order DB\n(PostgreSQL 16)")]
        OrderCache[("Order Cache\n(Redis 7.x)")]
        OrderQueue["Order Event Queue\n(RabbitMQ 3.13)"]
    end

    Web["Web App\n(React)"]
    Mobile["Mobile App\n(React Native)"]
    PaymentSystem["支付系统"]
    InventorySystem["库存系统"]

    Web -->|REST/JSON| OrderAPI
    Mobile -->|REST/JSON| OrderAPI
    OrderAPI -->|读写| OrderDB
    OrderAPI -->|缓存| OrderCache
    OrderAPI -->|发事件| OrderQueue
    OrderWorker -->|消费| OrderQueue
    OrderWorker -->|写| OrderDB
    OrderQueue -->|事件| PaymentSystem
    OrderQueue -->|事件| InventorySystem
```

**说明**：L2 图展示订单系统内部的容器划分和技术选型。开发者和 DevOps 关注的层面。

---

## L3: Component — 订单 API 的 COLA 四层

```mermaid
graph TB
    subgraph Adapter["适配层\n(adapter)"]
        direction TB
        Controller["OrderController"]
        ReqDTO["CreateOrderRequest"]
        RespDTO["OrderResponse"]
    end

    subgraph App["应用层\n(app)"]
        direction TB
        AppService["OrderAppService"]
        Cmd["CreateOrderCommand"]
        Query["OrderQueryService"]
    end

    subgraph Domain["领域层\n(domain)"]
        direction TB
        OrderAgg["Order (聚合根)"]
        OrderItem["OrderItem (实体)"]
        Money["Money (值对象)"]
        OrderStatus["OrderStatus (枚举)"]
        DomainEvent["OrderCreatedEvent"]
        Repo["OrderRepository (接口)"]
        DomainSvc["OrderDomainService"]
    end

    subgraph Infra["基础设施层\n(infrastructure)"]
        direction TB
        JpaRepo["JpaOrderRepository"]
        EventPub["RabbitMqEventPublisher"]
        CacheSvc["RedisCacheService"]
    end

    Controller --> AppService
    Controller --> Query
    AppService --> Cmd
    AppService --> Repo
    AppService --> DomainSvc
    DomainSvc --> OrderAgg
    OrderAgg --> OrderItem
    OrderAgg --> Money
    OrderAgg --> OrderStatus
    OrderAgg --> DomainEvent
    JpaRepo -.->|实现| Repo
    EventPub --> OrderQueue
```

**说明**：L3 图展示 COLA 四层架构中每个层的核心组件及其依赖关系。这是开发者日常工作的主要参考图。

---

## L4: Code — 订单聚合类图

```mermaid
classDiagram
    class Order {
        -OrderId id
        -CustomerId customerId
        -OrderStatus status
        -Money totalAmount
        -List~OrderItem~ items
        -Address shippingAddress
        -LocalDateTime createdAt
        +pay() void
        +cancel(String reason) void
        +addItem(ProductId, Money, int) void
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
        +multiply(int) Money
        +equals(Object) boolean
    }

    class OrderStatus {
        <<enumeration>>
        PENDING_PAYMENT
        PAID
        SHIPPED
        DELIVERED
        CANCELLED
        +canPay() boolean
        +canCancel() boolean
        +nextStatus() OrderStatus
    }

    class OrderId {
        -String value
        +generate() OrderId
        +fromString(String) OrderId
        +toString() String
    }

    class Address {
        -String province
        -String city
        -String district
        -String detail
        -String zipCode
        +getFullAddress() String
    }

    class OrderCreatedEvent {
        -OrderId orderId
        -CustomerId customerId
        -Money totalAmount
        -LocalDateTime occurredOn
    }

    class OrderPaidEvent {
        -OrderId orderId
        -Money amount
        -LocalDateTime paidAt
    }

    Order "1" --> "*" OrderItem
    Order --> Money
    Order --> OrderId
    Order --> OrderStatus
    Order --> Address
    Order ..> OrderCreatedEvent : 发布
    Order ..> OrderPaidEvent : 发布
```

**说明**：L4 图展示 Order 聚合的内部类结构。开发者实现具体功能时的参考。

---

## 关键映射：DDD ↔ C4

| DDD 概念 | C4 级别 | 谁看 |
|---------|---------|------|
| 全系统所有限界上下文 | L1 System Context | 业务方、架构师 |
| 每个限界上下文部署单元 | L2 Container | 架构师、DevOps |
| 每个容器的 Adapter/App/Domain/Infra | L3 Component | 开发团队 |
| 聚合内部结构（实体、值对象、事件） | L4 Code | 开发者 |
