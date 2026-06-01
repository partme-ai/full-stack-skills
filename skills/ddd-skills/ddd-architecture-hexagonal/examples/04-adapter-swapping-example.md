# Example: 适配器可替换性示例

本示例展示六边形架构的适配器可替换性。通过更换 DI 配置，可以在不修改 Domain/Application 代码的情况下切换数据库、支付网关和消息队列实现。

## 场景：数据库切换（Postgres → MongoDB）

### Step 1: 定义端口（Domain 层 — 不需要修改）

```java
// domain/port/outbound/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
    void delete(Order order);
}
```

### Step 2: 实现 Postgres 适配器

```java
// adapter/outbound/persistence/PostgresOrderRepository.java
@Repository
public class PostgresOrderRepository implements OrderRepository {
    private final JpaOrderRepository jpaRepo;
    private final OrderMapper mapper;

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue()).map(mapper::toDomain);
    }

    @Override
    public void save(Order order) {
        jpaRepo.save(mapper.toPO(order));
    }

    @Override
    public void delete(Order order) {
        jpaRepo.deleteById(order.getId().getValue());
    }
}
```

### Step 3: 实现 MongoDB 适配器（新增 — 不需要修改现有关代码）

```java
// adapter/outbound/persistence/MongoOrderRepository.java
@Repository
public class MongoOrderRepository implements OrderRepository {
    private final MongoTemplate mongoTemplate;
    private final MongoOrderConverter converter;

    public MongoOrderRepository(MongoTemplate mongoTemplate, MongoOrderConverter converter) {
        this.mongoTemplate = mongoTemplate;
        this.converter = converter;
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        var document = mongoTemplate.findById(id.getValue(), Document.class, "orders");
        return Optional.ofNullable(document).map(converter::toDomain);
    }

    @Override
    public void save(Order order) {
        var document = converter.toDocument(order);
        mongoTemplate.save(document, "orders");
    }

    @Override
    public void delete(Order order) {
        var query = new Query(Criteria.where("_id").is(order.getId().getValue()));
        mongoTemplate.remove(query, "orders");
    }
}
```

### Step 4: 切换 DI 配置（唯一需要修改的地方）

```java
// 切换前: Postgres
@Configuration
public class DatabaseConfig {
    @Bean
    public OrderRepository orderRepository(JpaOrderRepository jpaRepo, OrderMapper mapper) {
        return new PostgresOrderRepository(jpaRepo, mapper);
    }
}

// 切换后: MongoDB
@Configuration
public class DatabaseConfig {
    @Bean
    public OrderRepository orderRepository(MongoTemplate mongoTemplate) {
        return new MongoOrderRepository(mongoTemplate, new MongoOrderConverter());
    }
}
```

### Step 5: 验证 — Domain 和 Application 代码零修改

```java
// 无需修改！以下代码完全不受影响
@ApplicationService
public class CreateOrderService implements CreateOrderUseCase {
    // 只依赖 OrderRepository 接口，不管实现是 Postgres 还是 MongoDB
    private final OrderRepository orderRepository;
    // ...
}
```

## 场景：支付网关切换（Stripe → PayPal）

### 端口定义（Domain — 不需要修改）

```java
// domain/port/outbound/PaymentGateway.java
public interface PaymentGateway {
    PaymentResult charge(Money amount, PaymentMethod method);
    RefundResult refund(PaymentId paymentId, Money amount);
}
```

### Stripe 实现

```java
// adapter/outbound/external/StripePaymentGateway.java
@Component
public class StripePaymentGateway implements PaymentGateway {
    private final StripeClient stripeClient;

    @Override
    public PaymentResult charge(Money amount, PaymentMethod method) {
        try {
            var intent = stripeClient.paymentIntents().create(/* ... */);
            return PaymentResult.success(PaymentId.from(intent.getId()));
        } catch (StripeException e) {
            throw new InfrastructureException("Stripe payment failed", e);
        }
    }
}
```

### PayPal 实现（新增）

```java
// adapter/outbound/external/PayPalPaymentGateway.java
@Component
public class PayPalPaymentGateway implements PaymentGateway {
    private final PayPalHttpClient payPalClient;

    @Override
    public PaymentResult charge(Money amount, PaymentMethod method) {
        try {
            var order = new OrderRequest();
            order.checkoutPaymentIntent("CAPTURE");
            order.purchaseUnits(List.of(new PurchaseUnitRequest(
                    new MoneyRequest(amount.getCurrencyCode(), amount.toCents()))));
            var response = payPalClient.execute(new OrdersCreateRequest().requestBody(order));
            return PaymentResult.success(PaymentId.from(response.result().id()));
        } catch (IOException e) {
            throw new InfrastructureException("PayPal payment failed", e);
        }
    }
}
```

## 场景：消息队列切换（RabbitMQ → Kafka）

### 端口定义（Domain — 不需要修改）

```java
// domain/port/outbound/EventPublisher.java
public interface EventPublisher {
    void publish(DomainEvent event);
    void publishAll(List<DomainEvent> events);
}
```

### Kafka 实现

```java
// adapter/outbound/messaging/KafkaEventPublisher.java
@Component
public class KafkaEventPublisher implements EventPublisher {
    private final KafkaTemplate<String, String> kafkaTemplate;
    private final ObjectMapper objectMapper;

    @Override
    public void publish(DomainEvent event) {
        try {
            var payload = objectMapper.writeValueAsString(event.toPayload());
            kafkaTemplate.send("domain-events", event.getEventType(), payload);
        } catch (JsonProcessingException e) {
            throw new InfrastructureException("Event serialization failed", e);
        }
    }

    @Override
    public void publishAll(List<DomainEvent> events) {
        events.forEach(this::publish);
    }
}
```

## 环境配置（Profile 切换）

```yaml
# application-dev.yml — 开发环境用内存实现
adapter:
  persistence: inmemory
  payment: fake
  messaging: inmemory

# application-staging.yml — 预发布环境用真实但独立服务
adapter:
  persistence: postgres
  payment: stripe-test
  messaging: rabbitmq

# application-prod.yml — 生产环境
adapter:
  persistence: postgres
  payment: stripe
  messaging: kafka
```

```java
// 通过 Profile 切换配置
@Configuration
@Profile("dev")
public class DevAdapterConfig {
    @Bean
    public OrderRepository orderRepository() {
        return new InMemoryOrderRepository();
    }
    @Bean
    public PaymentGateway paymentGateway() {
        return new FakePaymentGateway();
    }
}
```

## 适配器可替换性清单

| 适配器类型 | 可替换实现 | 切换方式 |
|-----------|-----------|---------|
| OrderRepository | Postgres / MySQL / MongoDB / InMemory | DI Config |
| PaymentGateway | Stripe / PayPal / WeChatPay / Fake | DI Config |
| EventPublisher | RabbitMQ / Kafka / AWS SQS / InMemory | DI Config |
| NotificationPort | SendGrid / AliyunSMS / AWS SES / LogOnly | DI Config |
| VerificationCode | Redis / DB / Mock | DI Config |

## 验证：更改适配器后零回归

```java
// 这些 Domain 层测试不受适配器变更影响
@Test
void order_state_transitions() {
    var order = Order.create(CustomerId.of("cust-001"));
    order.pay(PaymentId.of("PAY-001"));
    assertEquals(OrderStatus.PAID, order.getStatus());
}

// 这些应用层测试不受适配器变更影响（Mock 端口）
@Test
void create_order_via_usecase() {
    var orderRepo = mock(OrderRepository.class);
    var service = new CreateOrderService(orderRepo, /* ... */);
    // ...
}

// 只有适配器层的集成测试需要修改
// @Test
// void postgres_repository_should_save() { ... }
// → 新增：
// @Test
// void mongo_repository_should_save() { ... }
```
