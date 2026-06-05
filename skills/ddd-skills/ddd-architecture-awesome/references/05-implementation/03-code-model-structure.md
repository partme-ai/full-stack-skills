# Code Model — 微服务代码模型结构

## DDD 微服务代码目录结构

```
{project}-microservice/
├── interfaces/                  # 用户接口层
│   ├── controller/             # REST Controller
│   ├── dto/                    # Data Transfer Object
│   ├── assembler/              # DTO ↔ DO 转换器
│   └── facade/                 # Facade 接口（粗粒度入口）
├── application/                # 应用层
│   ├── service/                # ApplicationService（编排）
│   └── event/                  # 事件发布和订阅
│       ├── publish/
│       └── subscribe/
├── domain/                     # 领域层
│   ├── {aggregate-name}/       # 按聚合分包
│   │   ├── entity/             # 聚合根、实体、值对象
│   │   ├── service/            # 领域服务
│   │   ├── repository/         # 仓储接口
│   │   └── event/              # 领域事件实体
│   └── shared/                 # 共享值对象、领域异常
└── infrastructure/             # 基础层
    ├── persistence/            # 仓储实现 + Mapper
    ├── messaging/              # 消息队列
    ├── config/                 # 配置
    └── util/                   # 工具类
```

## 各层职责速查

| 层 | 可以做什么 | 不能做什么 |
|----|-----------|-----------|
| **interfaces** | 请求解析、参数校验、DTO组装 | 不能有业务逻辑 |
| **application** | 服务编排、事务控制、权限校验、事件发布 | 不能有核心业务规则 |
| **domain** | 实体方法、领域服务、不变量检查 | 不能依赖框架、不能调基础层 |
| **infrastructure** | 数据库操作、消息发送、外部API调用 | 不能有业务判断 |

## 领域对象 → 代码对象映射表

| 领域对象 | 代码对象 | 所在层/包 | 示例 |
|----------|----------|----------|------|
| 聚合根 | AggregateRoot 类 | domain.{agg}/entity | Order, Customer |
| 实体 | Entity 类 | domain.{agg}/entity | OrderItem, Address |
| 值对象 | VO 类 (record) | domain.{agg}/entity | Money, OrderStatus |
| 聚合 | 聚合目录 | domain.{agg}/ | order/, customer/ |
| 领域服务 | DomainService 类 | domain.{agg}/service | OrderDomainService |
| 领域事件 | Event 实体类 | domain.{agg}/event | OrderPaidEvent |
| 仓储接口 | Repository 接口 | domain.{agg}/repository | OrderRepository |
| 仓储实现 | RepositoryImpl 类 | infrastructure/persistence | OrderRepositoryImpl |
| 应用服务 | ApplicationService 类 | application/service | OrderAppService |
| 命令 | Command 类 | application/service | PlaceOrderCommand |
| DTO | DTO 类 | interfaces/dto | OrderDTO |
| Facade | Facade 类 | interfaces/facade | OrderFacade |

## 聚合分包原则

```
为什么按聚合分包？
├── 业务高内聚：一个聚合的所有代码在一起，职责清晰
├── 架构演进：要拆分微服务时，直接复制聚合目录即可
└── 团队协作：不同聚合可分配给不同开发者，减少冲突
```

## 代码隔离规则

| 规则 | 说明 |
|------|------|
| 聚合之间不直接调用领域服务 | 通过应用层编排 |
| 聚合之间不直接关联数据库表 | 通过应用服务或事件 |
| 一个聚合对应一个仓储 | 仓储接口在聚合内，实现在基础设施层 |
| 不允许循环依赖 | A聚合 ↔ B聚合 不允许 |

## 充血模型实体示例

```java
// domain/order/entity/Order.java
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private BuyerId buyerId;
    private OrderStatus status;
    private Money totalAmount;
    private List<OrderItem> items = new ArrayList<>();

    // 实体方法 — 充血
    public void addItem(ProductId productId, Money unitPrice, int quantity) {
        if (status != OrderStatus.DRAFT) {
            throw new OrderException("Only DRAFT orders can add items");
        }
        items.add(new OrderItem(productId, unitPrice, quantity));
    }

    public void place() {
        if (items.isEmpty()) throw new OrderException("Must have at least one item");
        totalAmount = items.stream().map(OrderItem::subtotal).reduce(Money::add).orElseThrow();
        addDomainEvent(new OrderPlacedEvent(this.id, this.totalAmount));
    }
}
```

## 非典型领域模型处理

某些业务找不出聚合根（如客户归并、报表计算），处理方式：

```
1. 仍用聚合封装这些松耦合的实体
2. 照常设计实体的属性和方法
3. 照常封装领域服务和应用服务
4. 照常设计仓储
5. 唯一差异：没有聚合根来管理聚合内对象的生命周期
   └── 这部分用传统方法（如 Service 直接协调实体）
```
