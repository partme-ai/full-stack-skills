# COLA v5 基础设施层详解

## 基础设施层目录结构

```
{project}-infrastructure/
├── config/                        # 配置中心（v5 增强）
│   ├── database/                  # 数据库配置（DataSource、MyBatis、JPA）
│   ├── cache/                     # 缓存配置（Redis、LocalCache）
│   ├── message/                   # 消息配置（Kafka、RocketMQ、RabbitMQ）
│   ├── rpc/                       # RPC 配置（Dubbo、gRPC、Feign）
│   ├── external/                  # 外部服务配置（支付、邮件、OSS）
│   └── monitor/                   # 监控配置（Metrics、Log、Tracing）
├── persistence/                   # 持久化实现
│   ├── repositoryimpl/            # 仓储实现类
│   ├── mapper/                    # MyBatis Mapper
│   ├── dao/                       # 数据访问对象
│   └── entity/                    # 持久化实体（PO/DO）
├── gatewayimpl/                   # 网关实现
│   ├── customer/
│   ├── order/
│   └── external/                  # 外部网关实现
├── external/                      # 外部服务客户端
│   ├── payment/                   # 支付（Alipay、WechatPay）
│   ├── message/                   # 消息（SMS、Email）
│   └── storage/                   # 存储（OSS）
├── util/                          # 基础设施工具
│   ├── IdGenerator.java
│   ├── JsonUtils.java
│   └── CryptoUtils.java
└── component/                     # 基础设施组件（v5 新增）
    ├── lock/                      # 分布式锁
    ├── rateLimiter/               # 限流器
    ├── circuitbreaker/            # 熔断器
    └── retry/                     # 重试模板
```

## 核心实现规则

### 1. 实现 Domain 层接口

```java
// Domain 定义接口
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    Order save(Order order);
}

// Infrastructure 实现
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    @Resource
    private OrderMapper orderMapper;
    @Resource
    private OrderConverter orderConverter;

    @Override
    public Order save(Order order) {
        OrderPO po = orderConverter.toPO(order);
        orderMapper.insert(po);
        return orderConverter.toDomain(po);
    }

    @Override
    public Optional<Order> findById(OrderId id) {
        return Optional.ofNullable(orderMapper.selectById(id.getValue()))
            .map(orderConverter::toDomain);
    }
}
```

### 2. PO ↔ Domain 转换

```java
@Component
public class OrderConverter {
    // Domain → PO（写方向）
    public OrderPO toPO(Order order) {
        OrderPO po = new OrderPO();
        po.setId(order.getId().getValue());
        po.setStatus(order.getStatus().name());
        po.setTotalAmount(order.getTotalAmount().getAmount());
        po.setCurrency(order.getTotalAmount().getCurrency().getCurrencyCode());
        return po;
    }

    // PO → Domain（读方向）
    public Order toDomain(OrderPO po) {
        return Order.builder()
            .id(new OrderId(po.getId()))
            .status(OrderStatus.valueOf(po.getStatus()))
            .totalAmount(new Money(po.getTotalAmount(), Currency.getInstance(po.getCurrency())))
            .build();
    }
}
```

### 3. Gateway 实现（防腐层）

```java
// Domain 定义
public interface PaymentGateway {
    PaymentResult doPay(PayCommand command);
    RefundResult doRefund(RefundCommand command);
}

// Infrastructure 实现
@Component
public class PaymentGatewayImpl implements PaymentGateway {
    @Value("${payment.alipay.app-id}")
    private String appId;

    @Resource
    private AlipayClient alipayClient;

    @Override
    public PaymentResult doPay(PayCommand command) {
        AlipayRequest request = buildAlipayRequest(command);
        AlipayResponse response = alipayClient.pay(request);
        return PaymentResult.of(response);
    }
}
```

### 4. 基础设施组件（v5 新增）

```java
// 分布式锁组件
@Component
public class RedisDistributedLock implements DistributedLock {
    @Resource
    private StringRedisTemplate redisTemplate;

    @Override
    public boolean tryLock(String key, long timeout, TimeUnit unit) {
        return Boolean.TRUE.equals(
            redisTemplate.opsForValue()
                .setIfAbsent(key, "locked", timeout, unit)
        );
    }

    @Override
    public void unlock(String key) {
        redisTemplate.delete(key);
    }
}
```

## 基础设施层最佳实践

- **纯技术实现**：不包含任何业务判断或规则
- **PO 独立**：持久化 PO 与 Domain Entity 分离，使用 Converter 转换
- **配置外置**：数据库、MQ 等连接信息放在 `application.yml`，不使用硬编码
- **可替换性**：所有基础设施实现都面向 Domain 接口编程，支持替换
