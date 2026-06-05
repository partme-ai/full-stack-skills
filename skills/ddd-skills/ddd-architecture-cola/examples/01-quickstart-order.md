# COLA 示例：Order 订单聚合完整实现

> 本节展示一个完整的订单聚合，涵盖 Domain/App/Adapter/Infrastructure 四层。

## 领域层 (domain)

```java
// === 聚合根 ===
public class Order extends AggregateRoot<OrderId> {
    private OrderId id;
    private CustomerId customerId;
    private OrderStatus status;
    private Money totalAmount;
    private List<OrderItem> items;
    private LocalDateTime createdAt;

    public static Order create(OrderId id, CustomerId customerId, List<OrderItem> items) {
        Order order = new Order();
        order.id = id;
        order.customerId = customerId;
        order.status = OrderStatus.DRAFT;
        order.items = new ArrayList<>(items);
        order.totalAmount = calculateTotal(items);
        order.createdAt = LocalDateTime.now();
        order.addDomainEvent(new OrderCreatedEvent(id, customerId, order.totalAmount));
        return order;
    }

    public void pay() {
        if (!status.canPay()) throw new OrderDomainException("不可支付");
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id, this.totalAmount));
    }

    public void cancel() {
        if (!status.canCancel()) throw new OrderDomainException("不可取消");
        this.status = OrderStatus.CANCELLED;
        addDomainEvent(new OrderCancelledEvent(this.id));
    }

    private static Money calculateTotal(List<OrderItem> items) {
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }

    // getter 省略
}

// === 值对象 ===
public class OrderId {
    private final String value;
    public OrderId(String value) {
        this.value = Objects.requireNonNull(value);
    }
    public String getValue() { return value; }
    @Override public boolean equals(Object o) { /* 按值比较 */ }
    @Override public int hashCode() { return value.hashCode(); }
}

// === 实体 ===
public class OrderItem {
    private ProductId productId;
    private int quantity;
    private Money unitPrice;

    public Money getSubtotal() {
        return unitPrice.multiply(quantity);
    }
}

// === 仓储接口 ===
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    Order save(Order order);
    Page<Order> findByCustomerId(CustomerId customerId, Pageable pageable);
}
```

## 应用层 (app)

```java
// === 命令对象 ===
public class OrderCreateCmd {
    @NotBlank private String customerId;
    @NotEmpty private List<OrderItemDTO> items;
    // getter/setter
}

// === 命令执行器 ===
@Component
@CommandExecutor
public class OrderCreateCmdExe implements CommandExecutor<OrderCreateCmd, OrderDTO> {
    @Resource private OrderRepository orderRepository;
    @Resource private ProductGateway productGateway;

    @Override
    @Transactional
    public OrderDTO execute(OrderCreateCmd cmd) {
        // 校验库存
        for (OrderItemDTO item : cmd.getItems()) {
            InventoryInfo inv = productGateway.checkInventory(
                new ProductId(item.getProductId()), item.getQuantity());
            if (!inv.isAvailable()) throw new BizException("库存不足: " + item.getProductId());
        }

        // 创建订单
        Order order = Order.create(
            new OrderId(UUID.randomUUID().toString()),
            new CustomerId(cmd.getCustomerId()),
            cmd.getItems().stream().map(this::toItem).collect(Collectors.toList())
        );

        orderRepository.save(order);
        return OrderAssembler.toDTO(order);
    }
}

// === 查询执行器 ===
@Component
public class OrderGetQryExe implements QueryExecutor<OrderGetQry, OrderDTO> {
    @Resource private OrderRepository orderRepository;

    @Override
    public OrderDTO execute(OrderGetQry qry) {
        return orderRepository.findById(new OrderId(qry.getOrderId()))
            .map(OrderAssembler::toDTO)
            .orElseThrow(() -> new OrderNotFoundException(qry.getOrderId()));
    }
}
```

## 适配层 (adapter)

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    @Resource private OrderCreateCmdExe orderCreateCmdExe;
    @Resource private OrderGetQryExe orderGetQryExe;

    @PostMapping
    public Response<OrderDTO> create(@Valid @RequestBody OrderCreateRequest request) {
        return Response.success(orderCreateCmdExe.execute(request.toCommand()));
    }

    @GetMapping("/{id}")
    public Response<OrderDTO> get(@PathVariable String id) {
        OrderGetQry qry = new OrderGetQry();
        qry.setOrderId(id);
        return Response.success(orderGetQryExe.execute(qry));
    }

    @PostMapping("/{id}/pay")
    public Response<Void> pay(@PathVariable String id) {
        OrderPayCmd cmd = new OrderPayCmd();
        cmd.setOrderId(id);
        orderPayCmdExe.execute(cmd);
        return Response.success();
    }
}
```

## 基础设施层 (infrastructure)

```java
// === 持久化 PO ===
@Table(name = "t_order")
public class OrderPO {
    @Id private String id;
    private String customerId;
    private String status;
    private BigDecimal totalAmount;
    private String currency;
    private LocalDateTime createdAt;
}

// === MyBatis Mapper ===
@Mapper
public interface OrderMapper {
    @Insert("INSERT INTO t_order(id, customer_id, status, total_amount, currency, created_at) " +
            "VALUES(#{id}, #{customerId}, #{status}, #{totalAmount}, #{currency}, #{createdAt})")
    void insert(OrderPO po);

    @Select("SELECT * FROM t_order WHERE id = #{id}")
    OrderPO selectById(String id);
}

// === 仓储实现 ===
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    @Resource private OrderMapper orderMapper;
    @Resource private OrderConverter orderConverter;

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

// === PO ↔ Domain 转换 ===
@Component
public class OrderConverter {
    public OrderPO toPO(Order order) {
        OrderPO po = new OrderPO();
        po.setId(order.getId().getValue());
        po.setStatus(order.getStatus().name());
        po.setTotalAmount(order.getTotalAmount().getAmount());
        po.setCurrency(order.getTotalAmount().getCurrency().getCurrencyCode());
        return po;
    }

    public Order toDomain(OrderPO po) {
        // 注意：领域对象的完整重建需要 items 等关联数据
        return Order.builder()
            .id(new OrderId(po.getId()))
            .status(OrderStatus.valueOf(po.getStatus()))
            .totalAmount(new Money(po.getTotalAmount(), Currency.getInstance(po.getCurrency())))
            .build();
    }
}
```

## 数据库 DDL

```sql
CREATE TABLE t_order (
    id          VARCHAR(64) PRIMARY KEY,
    customer_id VARCHAR(64) NOT NULL,
    status      VARCHAR(16) NOT NULL DEFAULT 'DRAFT',
    total_amount DECIMAL(12,2) NOT NULL,
    currency    VARCHAR(3) NOT NULL DEFAULT 'CNY',
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer (customer_id),
    INDEX idx_status (status)
);

CREATE TABLE t_order_item (
    id          BIGINT AUTO_INCREMENT PRIMARY KEY,
    order_id    VARCHAR(64) NOT NULL,
    product_id  VARCHAR(64) NOT NULL,
    quantity    INT NOT NULL,
    unit_price  DECIMAL(12,2) NOT NULL,
    INDEX idx_order (order_id)
);
```
