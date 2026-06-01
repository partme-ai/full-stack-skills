# Application Layer — 应用层

> 应用层是"薄层"，负责用例编排、事务管理和跨聚合协调，**不包含业务逻辑**。

## 职责

- 编排领域服务完成业务用例
- 管理事务边界（`@Transactional`）
- 转换 Command/Query 到领域对象
- 协调跨聚合的操作
- 安全认证和权限校验
- 发送/订阅领域事件

## 包含的子模块

```
application/
├── service/                    # 应用服务（纯编排）
│   ├── OrderApplicationService.java
│   └── CustomerApplicationService.java
├── command/                    # 命令对象（CQRS 写操作）
│   ├── CreateOrderCommand.java
│   └── PayOrderCommand.java
├── query/                      # 查询对象（CQRS 读操作）
│   ├── GetOrderQuery.java
│   └── SearchOrdersQuery.java
├── assembler/                  # DO ↔ DTO 转换
│   ├── OrderAssembler.java
│   └── CustomerAssembler.java
├── event/                      # 应用级事件处理
│   ├── OrderPlacedEventHandler.java
│   └── OrderPaidEventHandler.java
├── dto/                        # 数据传输对象
│   ├── OrderDTO.java
│   └── OrderItemDTO.java
├── validator/                  # 应用验证器
│   └── OrderValidator.java
└── exception/                  # 应用层异常
    ├── ApplicationException.java
    └── CommandValidationException.java
```

## 关键规则

1. **无业务逻辑** — Application 层不应该包含 if/else 业务判断
2. **只编排** — 调用领域服务完成业务，不自己实现业务
3. **事务边界** — `@Transactional` 在 Application Service 方法上
4. **依赖 Domain** — Application 可以依赖 Domain 层

## 应用服务代码示例

```java
@Service
@Transactional
public class OrderApplicationService {
    private final OrderRepository orderRepository;
    private final PricingService pricingService;
    private final DomainEventPublisher eventPublisher;

    public OrderDTO createOrder(CreateOrderCommand command) {
        // 1. 将 Command 转换为领域对象
        List<OrderItem> items = command.getItems().stream()
            .map(i -> new OrderItem(i.getProductId(), i.getPrice(), i.getQuantity()))
            .toList();

        // 2. 创建聚合根（领域逻辑在工厂或构造器中）
        Order order = Order.create(command.getCustomerId(), items, pricingService);

        // 3. 通过仓储持久化
        orderRepository.save(order);

        // 4. 发布领域事件
        eventPublisher.publish(new OrderCreatedEvent(order.getId()));

        // 5. 返回 DTO
        return OrderAssembler.toDTO(order);
    }
}
```

## 命令对象示例

```java
public class CreateOrderCommand {
    @NotBlank(message = "客户ID不能为空")
    private String customerId;

    @NotEmpty(message = "订单项不能为空")
    private List<OrderItemCommand> items;

    // getters
}

public class OrderItemCommand {
    private String productId;
    private BigDecimal price;
    private int quantity;
    // getters
}
```

## 编排原则

```
ApplicationService 的典型方法结构：
  1. 参数校验（Command/Query 来自 Interface 层）
  2. Command → DO 转换（Assembler/手动）
  3. 调用领域服务（Domain Service）
  4. 事务提交（@Transactional 自动）
  5. 发布领域事件（EventPublisher）
  6. DO → DTO 转换（Assembler）
  7. 返回结果（DTO）
```

## 好的 Application Service vs 坏的

| ✅ 好的（纯编排） | ❌ 坏的（含业务逻辑） |
|-----------------|---------------------|
| 调用 `order.pay()` | 写 `if (status == DRAFT)` 判断 |
| 调用 `pricingService.calculate()` | 写 `price * quantity` 计算 |
| 调用 `orderRepository.save()` | 直接操作 JPA EntityManager |
| 方法 < 20 行 | 方法 > 50 行 |
| 没有 if/else 业务分支 | 大量 if/else 业务规则 |
