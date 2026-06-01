# COLA 示例：CQRS 读写分离完整实现

> 基于 COLA v5 的 CQRS 强化目录结构，展示命令/查询的严格分离。

## 写模型（Command Side）

### 命令对象

```java
// app/model/command/OrderCreateCmd.java
@Data
@Command
public class OrderCreateCmd {
    @NotBlank private String customerId;
    @NotEmpty private List<OrderItemDTO> items;
    private String remark;
    private String bizId;   // 业务身份（用于扩展点路由）

    public void validate() {
        Assert.notEmpty(items, "订单项不能为空");
        Assert.isTrue(items.size() <= 50, "单笔订单最多 50 项");
    }
}
```

### 命令执行器

```java
// app/executor/command/order/OrderCreateCmdExe.java
@Component
@CommandExecutor
public class OrderCreateCmdExe implements CommandExecutor<OrderCreateCmd, OrderDTO> {
    @Resource private OrderRepository orderRepository;
    @Resource private ProductGateway productGateway;
    @Resource private IdGenerator idGenerator;
    @Resource private ExtensionExecutor extensionExecutor;

    @Override
    @Transactional(rollbackFor = Exception.class)
    public OrderDTO execute(OrderCreateCmd cmd) {
        cmd.validate();

        // 1. 校验库存
        for (OrderItemDTO item : cmd.getItems()) {
            InventoryInfo inv = productGateway.checkInventory(
                new ProductId(item.getProductId()), item.getQuantity());
            if (!inv.isAvailable()) {
                throw new BizException("库存不足: " + item.getProductId());
            }
        }

        // 2. 创建订单（领域逻辑）
        Order order = Order.create(
            new OrderId(idGenerator.nextId()),
            new CustomerId(cmd.getCustomerId()),
            cmd.getItems().stream().map(this::toItem).collect(Collectors.toList())
        );

        // 3. 应用扩展点（价格计算等）
        Money finalPrice = extensionExecutor.execute(
            OrderPriceCalculateExtPt.class, cmd.getBizId(),
            ext -> ext.calculate(order, order.getTotalAmount())
        );

        // 4. 保存订单
        orderRepository.save(order);

        // 5. 发布领域事件（异步处理后续逻辑）
        order.getDomainEvents().forEach(eventBus::publish);

        return OrderAssembler.toDTO(order);
    }

    private OrderItem toItem(OrderItemDTO dto) {
        return new OrderItem(
            new ProductId(dto.getProductId()),
            dto.getQuantity(),
            new Money(dto.getUnitPrice(), Currency.getInstance("CNY"))
        );
    }
}
```

## 读模型（Query Side）

### 查询对象

```java
// app/model/query/OrderListQry.java
@Data
public class OrderListQry {
    private String customerId;
    private String status;
    private LocalDateTime startTime;
    private LocalDateTime endTime;
    private int page = 1;
    private int pageSize = 20;

    public Pageable toPageable() {
        return PageRequest.of(page - 1, pageSize, Sort.by("createdAt").descending());
    }

    public void validate() {
        Assert.isTrue(page >= 1, "页码从 1 开始");
        Assert.isTrue(pageSize <= 100, "每页最多 100 条");
    }
}
```

### 查询执行器

```java
// app/executor/query/order/OrderListQryExe.java
@Component
public class OrderListQryExe implements QueryExecutor<OrderListQry, PageResult<OrderDTO>> {
    @Resource
    private OrderRepository orderRepository;

    @Override
    public PageResult<OrderDTO> execute(OrderListQry qry) {
        qry.validate();

        // 查询通过 Repository 接口（非事务）
        Page<Order> orders = orderRepository.search(qry.toCriteria(), qry.toPageable());

        return PageResult.of(
            orders.getContent().stream()
                .map(OrderAssembler::toDTO)
                .collect(Collectors.toList()),
            orders.getTotalElements(),
            qry.getPage(),
            qry.getPageSize()
        );
    }
}
```

## 适配层 API

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    @Resource private OrderCreateCmdExe orderCreateCmdExe;  // Command Executor
    @Resource private OrderListQryExe orderListQryExe;      // Query Executor

    // 命令 API（写操作）
    @PostMapping
    public Response<OrderDTO> create(@Valid @RequestBody OrderCreateRequest request) {
        return Response.success(orderCreateCmdExe.execute(request.toCommand()));
    }

    // 查询 API（读操作）
    @GetMapping
    public Response<PageResult<OrderDTO>> list(OrderListQry qry) {
        return Response.success(orderListQryExe.execute(qry));
    }

    @GetMapping("/{id}")
    public Response<OrderDTO> get(@PathVariable String id) {
        OrderGetQry qry = new OrderGetQry();
        qry.setOrderId(id);
        return Response.success(orderGetQryExe.execute(qry));
    }
}
```

## 命令 vs 查询 API 设计对比

| 维度 | 命令 API（写） | 查询 API（读） |
|------|---------------|---------------|
| HTTP 方法 | POST, PUT, DELETE | GET |
| 请求体 | Command 对象（业务语义） | Query 参数（过滤条件） |
| 返回值 | 有限字段（操作结果 + ID） | 完整数据（DTO） |
| 幂等 | 必须支持 | 天然幂等 |
| 事务 | 需要 | 不需要 |
| 扩展点 | 经常使用 | 基本不用 |
| 限流 | 严格限流 | 宽松限流 |
| 缓存 | 不适用（写入后失效） | 适用 |

## 事件驱动同步（L2 数据库分离）

```java
// 当需要使用领域事件同步读写模型时
@Component
public class OrderPaidEventExe implements EventExecutor<OrderPaidEvent> {
    @Resource private OrderReadModelRepository readModelRepository;

    @Override
    public void execute(OrderPaidEvent event) {
        // 更新读模型（从库/ES）
        OrderReadModel readModel = readModelRepository.findById(event.getOrderId());
        readModel.setStatus("PAID");
        readModel.setPaidAt(LocalDateTime.now());
        readModelRepository.save(readModel);
    }
}
```
