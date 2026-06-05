# 03 — Infrastructure Layer: Implementation Details

> 基础设施层（Infrastructure Layer）是洋葱架构的最外层，实现 Domain 层定义的所有接口。

## 职责

- 实现 Repository 接口（JPA / MyBatis / JDBC）
- 实现 EventPublisher 接口（Kafka / RabbitMQ / Redis）
- 实现外部 API 客户端（HTTP / gRPC）
- 定义 PO（Persistent Object）和 Mapper
- 基础设施配置（数据源、连接池、MQ 连接）

## 代码模板

### Repository Implementation（仓储实现 — JPA）

```java
// infrastructure/data/repository/OrderRepositoryImpl.java
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    private final JpaOrderRepository jpaRepo;   // Spring Data JPA
    private final OrderMapper mapper;           // PO ↔ Domain

    public OrderRepositoryImpl(JpaOrderRepository jpaRepo, OrderMapper mapper) {
        this.jpaRepo = jpaRepo;
        this.mapper = mapper;
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue())
            .map(mapper::toDomain);
    }

    @Override
    public void save(Order order) {
        OrderPO po = mapper.toPO(order);
        jpaRepo.save(po);
    }

    @Override
    public void delete(OrderId id) {
        jpaRepo.deleteById(id.getValue());
    }

    @Override
    public Page<Order> findByCustomerId(CustomerId customerId, Pageable pageable) {
        return jpaRepo.findByCustomerId(customerId.getValue(), pageable)
            .map(mapper::toDomain);
    }
}

// Spring Data JPA 接口
// infrastructure/data/repository/JpaOrderRepository.java
public interface JpaOrderRepository extends JpaRepository<OrderPO, String> {
    Page<OrderPO> findByCustomerId(String customerId, Pageable pageable);
}
```

### PO（Persistent Object）

```java
// infrastructure/data/entity/OrderPO.java
@Entity
@Table(name = "orders")
public class OrderPO {
    @Id
    private String id;
    private String customerId;
    @Enumerated(EnumType.STRING)
    private OrderStatus status;
    private BigDecimal totalAmount;
    private String currency;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<OrderItemPO> items;

    // getter/setter...
}

// infrastructure/data/entity/OrderItemPO.java
@Entity
@Table(name = "order_items")
public class OrderItemPO {
    @Id
    private String id;
    private String orderId;
    private String productId;
    private BigDecimal unitPrice;
    private String currency;
    private int quantity;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "orderId", insertable = false, updatable = false)
    private OrderPO order;
    // getter/setter...
}
```

### Mapper（PO ↔ Domain）

```java
// infrastructure/data/mapper/OrderMapper.java
@Component
public class OrderMapper {
    public Order toDomain(OrderPO po) {
        if (po == null) return null;
        Order order = Order.create(
            new OrderId(po.getId()),
            new CustomerId(po.getCustomerId())
        );
        // 通过反射或内部方法恢复状态（不含领域事件）
        order.setStatus(po.getStatus());
        order.setTotalAmount(Money.of(po.getTotalAmount(), po.getCurrency()));
        po.getItems().forEach(itemPo ->
            order.addItem(
                new ProductId(itemPo.getProductId()),
                Money.of(itemPo.getUnitPrice(), itemPo.getCurrency()),
                itemPo.getQuantity()
            )
        );
        return order;
    }

    public OrderPO toPO(Order order) {
        OrderPO po = new OrderPO();
        po.setId(order.getId().getValue());
        po.setCustomerId(order.getCustomerId().getValue());
        po.setStatus(order.getStatus());
        po.setTotalAmount(order.getTotalAmount().getAmount());
        po.setCurrency(order.getTotalAmount().getCurrency().getCurrencyCode());
        po.setCreatedAt(order.getCreatedAt());
        // items mapping...
        return po;
    }
}
```

### Event Publisher 实现（Kafka）

```java
// infrastructure/messaging/KafkaEventPublisher.java
@Component
public class KafkaEventPublisher implements EventPublisher {
    private final KafkaTemplate<String, Object> kafkaTemplate;
    private final ObjectMapper objectMapper;

    public KafkaEventPublisher(KafkaTemplate<String, Object> kafkaTemplate,
                               ObjectMapper objectMapper) {
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = objectMapper;
    }

    @Override
    public void publish(DomainEvent event) {
        String topic = event.getClass().getSimpleName();
        String payload = objectMapper.writeValueAsString(event);
        kafkaTemplate.send(topic, event.getAggregateId().getValue(), payload);
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        events.forEach(this::publish);
    }
}
```

### 外部 API 客户端

```java
// infrastructure/external/PaymentGatewayImpl.java
@Component
public class PaymentGatewayImpl implements PaymentGateway {
    private final RestTemplate restTemplate;

    public PaymentGatewayImpl(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @Override
    public void charge(OrderId orderId, Money amount) {
        PaymentRequest request = new PaymentRequest(
            orderId.getValue(),
            amount.getAmount(),
            amount.getCurrency().getCurrencyCode()
        );
        ResponseEntity<PaymentResponse> response = restTemplate.postForEntity(
            "https://payment-service/api/charges",
            request,
            PaymentResponse.class
        );
        if (!response.getStatusCode().is2xxSuccessful()) {
            throw new PaymentFailedException("支付调用失败: " + response.getStatusCode());
        }
    }
}
```

## 规范检查清单

- [ ] 所有 Repository 实现 Domain 层定义的接口
- [ ] PO 类只放在 Infrastructure，不进 Domain
- [ ] Mapper 负责 PO ↔ Domain 双向转换
- [ ] 外部 API 调用包装在 Gateway 实现中
- [ ] 基础设施配置集中管理
- [ ] 支持多种实现切换（如 JPA ↔ MyBatis）
