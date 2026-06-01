## 基于Springboot的DDD实战(不依赖框架)

领域驱动设计（DDD）是一把锋利的双刃剑。它既是斩断复杂业务“一团乱麻”的神兵利器，也可能在经验不足的团队手中，成为过度设计、拖累项目的沉重枷锁。

今天，我们一起结合经典之作《实现领域驱动设计》（红皮书），软件设计的基本原则，通过一个复杂的业务场景，探讨如何在Spring生态中，真正地、务实地落地DDD，并融入一些好的的工程实践。

### 1. 理念的基石：DDD不是银弹，而是战略罗盘

在开始之前，我们必须达成一个共识：DDD的核心价值在于战略设计，而非战术上的炫技。

- 传统分层架构的问题: **数据驱动**，**贫血模型**，业务逻辑散落在大量的Service类中。当业务变得复杂时，这些Service会迅速膨胀，最终变成难以维护的“上帝类”。
- **DDD的承诺**: 将系统的核心——业务领域——置于中心地位。通过通用语言（Ubiquitous Language）统一团队认知，通过限界上下文（Bounded Context）拆分复杂问题，让软件的结构精准地反映业务的本质。
- **工程哲学共鸣**:
    - **高内聚、低耦合**: 微服务理念本质上就是DDD限界上下文的物理实现。每个服务（上下文）都拥有自己的数据和业务逻辑，团队对其有完全的自主权。
    - **清晰性与可测试性**: 充血的领域模型将数据和行为封装在一起，使得业务规则的单元测试变得极其简单，这与对代码质量和可维护性的极致追求不谋而合。
    - **设计文档（Design Docs）**: 任何重要的设计都需要文档化并进行评审。DDD的战略设计过程，尤其是上下文地图（Context Map），正是设计文档中最重要的输入。

### 2. 我们的竞技场：一个复杂的业务场景——“Nova Coffee” 新零售平台

为了让讨论不流于空泛，我们设定一个足够复杂的业务背景。

**业务背景**: “Nova Coffee”是一家精品连锁咖啡品牌，希望打造一个线上下单、线下履约、会员一体化的新零售平台。

**核心流程**:

- 用户端: 消费者通过App浏览商品、下单、支付、选择自提或外送。
- 门店端: 咖啡师在门店工作台（POS/平板）接收订单，制作饮品，完成订单（叫号自提或交由骑手）。
- 会员系统: 用户通过消费累积积分（星星），兑换优惠券，升级会员等级。
- 营销活动: 运营人员可以配置各种营销活动，如“第二杯半价”、“满30减5优惠券”等。
- 履约配送: 如果是外送单，系统需要与第三方运力平台对接，进行叫单、状态同步。

这个场景的复杂性在于，它涉及多个相互关联但又职责分明的业务领域。

### 3. 战略设计：绘制架构蓝图，而非一头扎进代码

这是落地DDD最关键，也最容易被忽视的一步。先别急着创建Spring Boot项目！

过程:

#### 1. **识别领域与子域**:

- **核心域 (Core Domain)**: 订单交易。这是业务的核心，是我们最需要投入精力的部分。
- **支撑子域 (Supporting Subdomain)**: 门店运营、营销活动。这些领域为核心域服务，需要我们自己构建，但不是业务的根本。
- **通用子域 (Generic Subdomain)**: 会员身份（可以是标准的认证授权服务）、支付（对接支付宝/微信）。这些是通用的功能，可以直接外购或使用开源方案。

#### 2. **建立通用语言 (Ubiquitous Language)**:

- 与产品经理、业务专家一起，定义每个领域的通用语言。
- **订单领域**: `订单(Order)`、`商品(Item)`、`消费者(Consumer)`、`支付(Payment)`、`履约方式(Fulfillment)`。
- **门店领域**: `订单(Order)`（注意！此订单非彼订单）、`饮品制作单(ProductionTicket)`、`咖啡师(Barista)`、`库存(Inventory)`。
- **会员领域**: `会员(Member)`、`星星(Star)`、`优惠券(Coupon)`、`等级(Tier)`。
- **我们立刻发现，“订单”在不同领域含义不同。**在交易中，它关心的是金额、商品列表；在门店，它关心的是制作要求、取餐码。这是划分限界上下文的强烈信号。

#### 3. 定义限界上下文 (Bounded Context):

基于子域和通用语言的差异，我们定义限界上下文：

- Ordering Context (订单上下文)
- Store Operations Context (门店运营上下文)
- Membership Context (会员上下文)
- Marketing Context (营销上下文)
- Delivery Context (履约上下文)

#### 4. 绘制上下文地图 (Context Map):

这是战略设计的核心产出，它定义了上下文之间的关系。我们将使用Spring Cloud来实现这些关系。

![](https://wiki.hiwepy.com/uploads/ddd/images/m_ae150e1e415b31e11e724a248626d8e4_r.png)

**解读**:

- **会员和营销是上游，为订单提供服务**。订单通过防腐层（ACL）调用它们提供的开放主机服务（OHS）（通常是REST API）。ACL确保上游模型的变更不会污染下游的订单模型。
- **订单是核心**，它通过发布语言（PL）（通常是领域事件，如OrderCreatedEvent）将状态变更通知下游的门店和履约上下文。这种异步、事件驱动的方式实现了完美的解耦。

### 4. 战术设计：在限界上下文中精雕细琢
现在，我们可以选择一个限界上下文，比如核心的Ordering Context，来深入战术设计和项目搭建。

#### 4.1 项目结构 (多模块Maven/Gradle)

这是避免DDD被滥用的第一道防线：强制性的分层隔离。

```
nova-coffee/
 ├── pom.xml
└── ordering-context/
    ├── pom.xml
    ├── domain/                    # 领域层 (纯粹的领域模型，无任何框架依赖)
    │   ├── pom.xml
    │   └── src/main/java/
    │       └── com/novacoffee/ordering/domain/
    │           ├── model/
    │           │   ├── order/
    │           │   │   ├── Order.java            (聚合根)
    │           │   │   ├── OrderItem.java        (实体)
    │           │   │   ├── OrderStatus.java      (枚举)
    │           │   │   └── Money.java            (值对象)
    │           │   └── ...
    │           ├── event/
    │           │   └── OrderCreatedEvent.java    (领域事件)
    │           ├── repository/
    │           │   └── OrderRepository.java      (仓储接口)
    │           └── service/
    │               └── PricingService.java       (领域服务)
    ├── application/               # 应用层 (编排领域层，处理用例)
    │   ├── pom.xml
    │   └── src/main/java/
    │       └── com/novacoffee/ordering/application/
    │           ├── OrderingApplicationService.java (应用服务)
    │           └── dto/
    │               ├── CreateOrderCommand.java   (命令)
    │               └── OrderDTO.java             (数据传输对象)
    ├── infrastructure/            # 基础设施层 (实现领域接口，与外界交互)
    │   ├── pom.xml
    │   └── src/main/java/
    │       └── com/novacoffee/ordering/infrastructure/
    │           ├── persistence/
    │           │   └── JpaOrderRepository.java   (JPA实现仓储)
    │           ├── acl/
    │           │   └── MembershipACL.java        (防腐层实现)
    │           └── messaging/
    │               └── KafkaEventPublisher.java  (事件发布实现)
    └── interfaces/                # 接口层 (暴露API，处理外部请求)
        ├── pom.xml
        └── src/main/java/
            └── com/novacoffee/ordering/interfaces/
                └── web/
                    └── OrderController.java      (Spring MVC Controller)
```

依赖关系: `interfaces -> application -> domain。infrastructure -> domain`。关键：**domain**层不依赖任何其他层，它是项目的核心和灵魂。

#### 4.2 样例代码 (以Order聚合为例)

Domain层: **Order.java** (聚合根)

```java
// package com.novacoffee.ordering.domain.model.order;

// 无Spring、JPA注解，纯粹的Java对象
public class Order {
    private Long id;
    private OrderStatus status;
    private List<OrderItem> items;
    private Money totalPrice;
    private Long consumerId;

    // 构造函数负责创建时业务规则校验
    public Order(Long consumerId, List<OrderItem> items, PricingService pricingService) {
        if (consumerId == null) throw new IllegalArgumentException("Consumer ID cannot be null.");
        if (items == null || items.isEmpty()) throw new IllegalArgumentException("Order must have at least one item.");

        this.consumerId = consumerId;
        this.items = new ArrayList<>(items);
        this.status = OrderStatus.PENDING_PAYMENT;
        // 委托领域服务计算价格
        this.totalPrice = pricingService.calculateTotalPrice(this.items);
    }

    // 业务方法，封装行为和状态变更
    public void pay() {
        if (this.status != OrderStatus.PENDING_PAYMENT) {
            throw new IllegalStateException("Order is not pending payment.");
        }
        this.status = OrderStatus.PAID;
        // 此处可以发布领域事件: DomainEventPublisher.publish(new OrderPaidEvent(this.id));
    }

    // getters... (注意：仅暴露必要信息，保护内部状态)
}
```

Domain层: **OrderRepository.java** (仓储接口)

```java
// package com.novacoffee.ordering.domain.repository;

public interface OrderRepository {
    Optional<Order> findById(Long id);
    void save(Order order); // 保存操作涵盖了新增和更新
}
```

Application层: **OrderingApplicationService.java**

```java
// package com.novacoffee.ordering.application;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
// ... imports

@Service
public class OrderingApplicationService {

    private final OrderRepository orderRepository;
    private final PricingService pricingService; // 领域服务
    private final MembershipACL membershipACL; // 防腐层

    // 构造函数注入
    public OrderingApplicationService(...) { ... }

    @Transactional
    public Long createOrder(CreateOrderCommand command) {
        // 1. 通过ACL获取外部信息
        if (!membershipACL.isMemberActive(command.getConsumerId())) {
            throw new BusinessException("Member is not active.");
        }

        // 2. 将DTO转换为领域对象
        List<OrderItem> items = command.getItems().stream().map(...).collect(Collectors.toList());

        // 3. 创建聚合根，执行领域逻辑
        Order newOrder = new Order(command.getConsumerId(), items, pricingService);

        // 4. 使用仓储持久化
        orderRepository.save(newOrder);

        // 5. （可选）发布领域事件
        // eventPublisher.publish(new OrderCreatedEvent(newOrder.getId()));

        return newOrder.getId();
    }
}
```

### 5. 架构师的红线：如何避免错误的DDD实践（实践反例）

#### 1. 贫血模型 + 上帝Service (最常见的错误)

- 错误做法: `Order`类只有一堆getter/setter。`OrderingApplicationService`里有上千行代码，包含了各种if/else来处理状态流转和价格计算。
- 为何错误: 这完全违背了DDD的封装原则，业务逻辑泄露，Order沦为数据载体。最终导致代码难以测试和维护。
- 正确做法: 如上例所示，将业务逻辑和规则（如`pay()`方法）内聚到Order聚合根中。

#### 2. 领域层被框架污染

- 错误做法: 在Order.java领域模型上添加@Entity, @Table, @Column等JPA注解。
- 为何错误: 这让你的核心领域模型与持久化技术紧紧绑定。如果有一天你想从JPA切换到MyBatis，或者甚至换成NoSQL数据库，将是一场灾难。
- 正确做法: 在infrastructure层创建单独的JPA实体OrderJpaEntity，并在仓储实现中完成领域对象Order和持久化对象OrderJpaEntity之间的转换（可以使用MapStruct等工具）。

#### 3.无视限界上下文，跨服务直接查库

- 错误做法: Ordering Context的服务为了获取会员等级，直接配置Membership Context的数据库连接池，跨库JOIN查询。
- 为何错误: 这是微服务架构的头号杀手。它破坏了服务的封装性和自主性，两个团队被紧紧耦合在一起，一方的数据库变更可能导致另一方服务崩溃。
- 正确做法: 严格遵守上下文地图。Ordering只能通过Membership发布的API（OHS）或订阅其事件来获取数据。

#### 4.万物皆聚合

- 错误做法: 把所有有关联的实体都塞进一个巨大的聚合里，比如Consumer聚合里包含了`List<Order>，List<Address>，List<Coupon>…`
- 为何错误: 聚合的设计原则是尽可能小，并保证事务的一致性。巨大的聚合会导致严重的性能问题（加载整张对象图）和并发冲突。
- 正确做法: 聚合之间通过ID引用。Order聚合中只包含consumerId，而不是整个Consumer对象。如果需要Consumer的信息，通过应用服务去查询。

### DDD是一场回归软件本质的修行

将DDD与Spring生态结合是一件有趣的事。它要求我们不仅是代码的编写者，更是业务的思考者和模型的塑造者。

- 请记住，DDD的成功不在于你使用了多少时髦的模式，而在于：
- 你的代码能否让新来的业务人员看懂？ (通用语言)
- 你的系统边界是否清晰，能否支持团队独立、高效地工作？ (限界上下文)
- 你的核心业务逻辑是否被妥善地保护、封装和测试？ (聚合根与领域模型)

————————————————
版权声明：本文为CSDN博主「zero13_小葵司」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42288219/article/details/152282099