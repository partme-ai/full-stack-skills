# Application Services — 应用服务层

## 概述

应用服务（Application Service）位于应用层，实现 Domain 层定义的入站端口（UseCase 接口）。应用服务负责用例编排（orchestration），将领域模型操作和端口调用串联起来，但本身不包含业务逻辑。

## 核心职责

1. **用例编排** — 调用领域对象的方法和出站端口
2. **事务管理** — 控制事务边界
3. **权限检查** — 调用授权服务验证操作权限
4. **事件发布** — 在操作完成后发布领域事件
5. **输入验证** — 补充业务级校验（非格式校验）

## 应用服务实现

```java
// application/service/CreateOrderService.java
@ApplicationService  // 自定义注解，非 Spring @Service
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;
    private final OrderPricingService pricingService;
    private final EventPublisher eventPublisher;

    public CreateOrderService(
            OrderRepository orderRepository,
            ProductRepository productRepository,
            OrderPricingService pricingService,
            EventPublisher eventPublisher) {
        this.orderRepository = orderRepository;
        this.productRepository = productRepository;
        this.pricingService = pricingService;
        this.eventPublisher = eventPublisher;
    }

    @Override
    @Transactional
    public OrderCreatedResult execute(CreateOrderCommand command) {
        // 1. 创建聚合
        Order order = Order.create(command.getCustomerId());

        // 2. 添加商品（调用领域方法）
        for (ItemCmd item : command.getItems()) {
            Product product = productRepository.findById(item.getProductId())
                    .orElseThrow(() -> new ProductNotFoundException(item.getProductId()));
            order.addItem(product.getId(), item.getQuantity(), product.getPrice());
        }

        // 3. 计算价格（调用领域服务）
        order.applyPricing(pricingService.calculateFinalPrice(order, command.getCustomerGrade()));

        // 4. 持久化
        orderRepository.save(order);

        // 5. 发布事件
        eventPublisher.publishAll(order.getDomainEvents());

        // 6. 返回结果
        return OrderCreatedResult.from(order);
    }
}
```

## 查询用例

```java
// application/service/GetOrderService.java
@ApplicationService
public class GetOrderService implements GetOrderUseCase {
    private final OrderRepository orderRepository;
    private final OrderDTOAssembler assembler;

    @Override
    public OrderDTO execute(GetOrderQuery query) {
        return orderRepository.findById(new OrderId(query.getOrderId()))
                .map(assembler::toDTO)
                .orElse(null);
    }
}
```

## 命令对象

```java
// application/command/CreateOrderCommand.java
public class CreateOrderCommand {
    private final CustomerId customerId;
    private final CustomerGrade customerGrade;
    private final List<ItemCmd> items;

    public CreateOrderCommand(CustomerId customerId, CustomerGrade customerGrade, List<ItemCmd> items) {
        this.customerId = customerId;
        this.customerGrade = customerGrade;
        this.items = items;
    }

    public CustomerId getCustomerId() { return customerId; }
    public CustomerGrade getCustomerGrade() { return customerGrade; }
    public List<ItemCmd> getItems() { return items; }

    public static class ItemCmd {
        private final ProductId productId;
        private final Quantity quantity;

        public ItemCmd(ProductId productId, Quantity quantity) {
            this.productId = productId;
            this.quantity = quantity;
        }

        public ProductId getProductId() { return productId; }
        public Quantity getQuantity() { return quantity; }
    }
}
```

## 应用层开发规范

### ✅ 应用层可以做的事
- 调用领域对象的方法
- 调用出站端口（Repository、Gateway）
- 管理事务（@Transactional）
- 抛出业务异常
- 调用领域服务
- 组装和返回 DTO

### ❌ 应用层不应该做的事
- 不包含业务 if/else 判断（业务逻辑在 Domain）
- 不直接操作数据库（通过 Repository 端口）
- 不处理 HTTP 请求/响应（那是 Adapter 的职责）
- 不包含技术实现细节（SQL、MQ、Redis）
- 不使用框架特定注解进行业务逻辑

## 应用层与 Domain 层的职责边界

| 场景 | 放在 Application | 放在 Domain |
|------|-----------------|-------------|
| 创建订单 | 调用 Order.create() + 调用 Repository.save() | `Order.create()` 工厂方法 + 订单状态校验 |
| 支付订单 | 开启事务 + 调用 order.pay() + 发布事件 | `order.pay()` 方法中的状态机转换 |
| 取消订单 | 检查权限 + 调用 order.cancel() | `order.cancel()` 中的取消规则 |
| 查询订单 | 调用 Repository.findById() + 组装 DTO | Order 实体本身不关心查询格式 |
| 发送通知 | 调用 NotificationPort.send() | 不关心通知的具体实现 |

## 应用服务命名规范

| 类型 | 命名模式 | 示例 |
|------|---------|------|
| 命令服务 | `{Action}Service` | `CreateOrderService`、`PayOrderService` |
| 查询服务 | `{Resource}QueryService` | `OrderQueryService`、`ProductQueryService` |
| 批量操作 | `{Action}BatchService` | `OrderBatchService` |
