# Secondary Adapters — 次适配器（被驱动侧）

## 概述

次适配器（Secondary/Driven Adapter）位于六边形右侧，负责实现出站端口（Outbound Port）定义的接口，将领域层的抽象调用转换为具体的技术实现（数据库操作、MQ 发送、HTTP 调用等）。

## 核心职责

1. **端口实现** — 实现 Domain 层定义的出站端口接口
2. **技术适配** — 将领域调用转换为具体技术（JPA/MyBatis/Redis/Kafka）
3. **异常转换** — 将技术异常（SQLException、TimeoutException）转换为领域异常
4. **数据映射** — PO（Persistence Object）↔ Domain Object 的双向转换

## JPA Repository

```java
// adapter/outbound/persistence/PostgresOrderRepository.java
@Repository
public class PostgresOrderRepository implements OrderRepository {
    private final JpaOrderRepository jpaRepo;
    private final OrderMapper mapper;

    public PostgresOrderRepository(JpaOrderRepository jpaRepo, OrderMapper mapper) {
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
        var po = mapper.toPO(order);
        jpaRepo.save(po);
    }

    @Override
    public void delete(Order order) {
        jpaRepo.deleteById(order.getId().getValue());
    }
}
```

## MyBatis Mapper 实现

```java
// adapter/outbound/persistence/MyBatisOrderRepository.java
@Repository
public class MyBatisOrderRepository implements OrderRepository {
    private final OrderMapper mapper;

    @Override
    public Optional<Order> findById(OrderId id) {
        var po = mapper.selectById(id.getValue());
        return Optional.ofNullable(po).map(OrderConverter::toDomain);
    }

    @Override
    public void save(Order order) {
        var po = OrderConverter.toPO(order);
        // 使用 MyBatis 的 insertOrUpdate
        if (mapper.existsById(po.getId())) {
            mapper.update(po);
        } else {
            mapper.insert(po);
        }
    }
}
```

## Payment Gateway 适配器

```java
// adapter/outbound/external/StripePaymentGateway.java
@Component
public class StripePaymentGateway implements PaymentGateway {
    private final StripeClient stripeClient;

    @Override
    public PaymentResult charge(Money amount, PaymentMethod method) {
        try {
            var intent = stripeClient.paymentIntents().create(PaymentIntentCreateParams.builder()
                    .setAmount(amount.toCents())
                    .setCurrency(amount.getCurrency())
                    .setPaymentMethod(method.getStripeId())
                    .setConfirm(true)
                    .build());
            return PaymentResult.success(PaymentId.from(intent.getId()));
        } catch (StripeCardException e) {
            return PaymentResult.failed(new PaymentDeclinedException(e.getMessage()));
        } catch (StripeException e) {
            throw new InfrastructureException("Payment service unavailable", e);
        }
    }

    @Override
    public RefundResult refund(PaymentId paymentId, Money amount) {
        try {
            var refund = stripeClient.refunds().create(RefundCreateParams.builder()
                    .setPaymentIntent(paymentId.getValue())
                    .setAmount(amount.toCents())
                    .build());
            return RefundResult.success(RefundId.from(refund.getId()));
        } catch (StripeException e) {
            throw new InfrastructureException("Refund failed", e);
        }
    }
}
```

## Event Publisher 适配器

```java
// adapter/outbound/messaging/RabbitMQEventPublisher.java
@Component
public class RabbitMQEventPublisher implements EventPublisher {
    private final RabbitTemplate rabbitTemplate;
    private final ObjectMapper objectMapper;

    @Override
    public void publish(DomainEvent event) {
        var message = serialize(event);
        rabbitTemplate.convertAndSend("domain-events", event.getEventType(), message);
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        events.forEach(this::publish);
    }

    private String serialize(DomainEvent event) {
        try {
            return objectMapper.writeValueAsString(event.toPayload());
        } catch (JsonProcessingException e) {
            throw new InfrastructureException("Event serialization failed", e);
        }
    }
}
```

## In-Memory 测试适配器

```java
// adapter/outbound/inmemory/InMemoryOrderRepository.java
public class InMemoryOrderRepository implements OrderRepository {
    private final Map<String, Order> store = new ConcurrentHashMap<>();

    @Override
    public Optional<Order> findById(OrderId id) {
        return Optional.ofNullable(store.get(id.getValue()));
    }

    @Override
    public void save(Order order) {
        store.put(order.getId().getValue(), order);
    }

    @Override
    public void delete(Order order) {
        store.remove(order.getId().getValue());
    }

    public void clear() {
        store.clear();
    }
}
```

## 异常转换规则

| 技术异常 | 转换后领域异常 | 说明 |
|---------|--------------|------|
| `SQLException` | `RepositoryException` | 数据库操作失败 |
| `DataIntegrityViolationException` | `ConcurrencyConflictException` | 并发冲突 |
| `StripeException` | `InfrastructureException` | 支付服务不可用 |
| `TimeoutException` | `ExternalServiceTimeoutException` | 外部服务超时 |
| `HttpClientErrorException` | `ExternalServiceException` | 外部服务调用失败 |

## 次适配器检查清单

- [ ] 是否实现了 Domain 层定义的端口接口？
- [ ] 技术异常是否在适配器内部转换为领域异常？
- [ ] 未使用 Domain 层不认识的框架注解（`@Table`、`@Column`）？
- [ ] PO/DTO ↔ Domain 转换逻辑是否集中在 Mapper/Converter 中？
- [ ] 是否设置了外部调用的超时和重试机制？
- [ ] 事务边界是否在 Application 层而非 Adapter 层？
