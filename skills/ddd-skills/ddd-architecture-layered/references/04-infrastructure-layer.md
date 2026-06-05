# Infrastructure Layer — 基础设施层

> 基础设施层实现 Domain 层定义的接口，封装所有技术细节。它是 DDD 分层架构中"依赖倒置"的兑现层。

## 职责

- 实现 Repository 接口（JPA/MyBatis/内存）
- PO ↔ DO 对象映射
- 领域事件发布（Kafka/RabbitMQ/Spring Event）
- 外部服务集成（支付/通知/物流）
- 缓存（Redis/Guava）
- 数据库配置和迁移
- 安全基础设施（JWT/加密）

## 包含的子模块

```
infrastructure/
├── repository/                  # 仓储实现
│   ├── jpa/                    # JPA 实现
│   │   ├── JpaOrderRepository.java
│   │   └── JpaCustomerRepository.java
│   ├── mybatis/                # MyBatis 实现
│   │   └── MyBatisOrderRepository.java
│   └── memory/                 # 内存实现（测试用）
│       └── InMemoryOrderRepository.java
├── persistence/                # 持久化实体
│   ├── entity/                 # JPA Entity（PO）
│   │   ├── OrderPO.java
│   │   └── OrderItemPO.java
│   └── mapper/                 # PO ↔ DO 映射
│       └── OrderMapper.java
├── messaging/                  # 消息队列
│   ├── publisher/              # 事件发布实现
│   │   ├── KafkaEventPublisher.java
│   │   └── SpringEventPublisher.java
│   └── consumer/               # 事件消费
│       └── OrderEventConsumer.java
├── external/                   # 外部服务
│   ├── payment/                # 支付集成
│   │   └── AlipayPaymentService.java
│   └── notification/           # 通知集成
│       └── SmsNotificationService.java
├── cache/                      # 缓存
│   └── redis/
│       └── RedisOrderCache.java
├── config/                     # 配置
│   ├── PersistenceConfig.java
│   ├── MessagingConfig.java
│   └── CacheConfig.java
└── security/                   # 安全基础设施
    └── JwtTokenProvider.java
```

## 关键规则

1. **实现接口** — Infrastructure 实现 Domain 层定义的接口
2. **反向依赖** — Infrastructure 依赖 Domain（非 Domain 依赖 Infra）
3. **可替换** — 更换数据库/消息队列只需替换 Infra 层的实现
4. **不含业务逻辑** — Infrastructure 只做技术实现

## 仓储实现示例

```java
// Domain 层定义的接口
// interface OrderRepository { void save(Order order); Optional<Order> findById(OrderId id); }

// Infrastructure 层的 JPA 实现
@Repository
public class JpaOrderRepository implements OrderRepository {
    private final JpaOrderRepo jpaRepo;
    private final OrderMapper mapper;

    @Override
    public void save(Order order) {
        OrderPO po = mapper.toPO(order);
        jpaRepo.save(po);
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue())
            .map(mapper::toDomain);
    }
}

// Spring Data JPA 接口（在 Infrastructure 层）
interface JpaOrderRepo extends JpaRepository<OrderPO, Long> {
    Optional<OrderPO> findByOrderNumber(String orderNumber);
}
```

## PO ↔ DO 映射

```java
// PO（持久化对象）— 与数据库表结构一一对应
@Entity
@Table(name = "orders")
public class OrderPO {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String orderNumber;
    private String customerId;
    @Enumerated(EnumType.STRING)
    private String status;
    private BigDecimal totalAmount;
    private String currency;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "order")
    private List<OrderItemPO> items;
    // getters/setters
}

// Mapper（映射器）— 在 Infrastructure 层
@Component
public class OrderMapper {
    public OrderPO toPO(Order domain) {
        OrderPO po = new OrderPO();
        po.setOrderNumber(domain.getId().getValue());
        po.setCustomerId(domain.getCustomerId().getValue());
        po.setStatus(domain.getStatus().name());
        po.setTotalAmount(domain.getTotalAmount().getAmount());
        po.setCurrency(domain.getTotalAmount().getCurrency());
        po.setItems(domain.getItems().stream().map(this::toItemPO).toList());
        return po;
    }

    public Order toDomain(OrderPO po) {
        return new Order(
            new OrderId(po.getOrderNumber()),
            new CustomerId(po.getCustomerId()),
            // ... 从 PO 重建领域对象
        );
    }
}
```

## 事件发布实现

```java
// Domain 层定义的事件发布接口
// interface DomainEventPublisher { void publish(DomainEvent event); }

// Infrastructure 层实现 - Spring 事件
@Component
public class SpringEventPublisher implements DomainEventPublisher {
    private final ApplicationEventPublisher springPublisher;

    @Override
    public void publish(DomainEvent event) {
        springPublisher.publishEvent(event);
    }
}

// Infrastructure 层实现 - Kafka
@Component
public class KafkaEventPublisher implements DomainEventPublisher {
    private final KafkaTemplate<String, Object> kafkaTemplate;

    @Override
    public void publish(DomainEvent event) {
        kafkaTemplate.send("domain-events", event.getEventId(), event);
    }
}
```

## 依赖倒置设计原则

```
传统方式（错误）：                    DDD 方式（正确）：
Domain                              Domain
  └── 依赖 JPA @Entity               └── 定义 OrderRepository 接口
  └── import javax.persistence       └── 纯 POJO
        ↓                                    ↓
Infrastructure                      Infrastructure
  └── 实现 SQL/ORM                    └── 实现 OrderRepository
                                    └── JPA 注解在 PO 上，不在 Domain
```

## 检查清单

- [ ] Infrastructure 不直接依赖 Interface/Application 层
- [ ] PO 对象的注解（JPA/MyBatis）不影响 Domain 层
- [ ] 更换 DB 只需替换 Infrastructure 实现
- [ ] Domain 接口的实现在 Infrastructure，不在 Application
- [ ] 外部 API 调用在 Infrastructure 层，不在 Domain 或 Application
- [ ] 缓存逻辑在 Infrastructure，不泄露到其他层
