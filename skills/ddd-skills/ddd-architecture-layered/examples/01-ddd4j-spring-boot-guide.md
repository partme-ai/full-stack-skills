## Java 基于DDD分层架构的实操指南

原文：https://cloud.tencent.com/developer/article/2554516

> 随着微服务架构的普及，领域驱动设计(DDD)在复杂业务系统中的应用越来越广泛。本文将结合最新技术栈（Spring Boot 3.x、Spring Data JPA 3.x、Lombok等），通过一个电商订单系统的实例，详细讲解DDD分层架构的具体实现。

### 一、技术栈选择

- 核心框架：Spring Boot 3.2.x（支持Jakarta EE 9+）
- ORM框架：Spring Data JPA 3.2.x
- 简化代码：Lombok 1.18.x
- 验证框架：Jakarta Validation 3.0
- 数据库：PostgreSQL 16（支持JSON类型，适合存储值对象）
- 构建工具：Maven 3.9.x

### 二、项目结构设计

采用模块化设计，按DDD分层思想组织代码结构：

```
order-service/
├── src/main/java/com/example/order/
│   ├── application/           // 应用层
│   │   ├── command/       // 命令对象
│   │   ├── dto/                 // 数据传输对象
│   │   ├── service/           // 应用服务
│   │  └── mapper/            // DTO与领域对象映射
│   ├── domain/                // 领域层
│   │   ├── model/             // 领域模型
│   │   │   ├── entity/        // 实体
│   │   │   ├── vo/            // 值对象
│   │   │   └── aggregate/     // 聚合根
│   │    ├── repository/        // 仓储接口
│   │   └── service/           // 领域服务
│   ├── infrastructure/        // 基础设施层
│   │   ├── persistence/       // 持久化实现
│   │   ├── messaging/         // 消息组件
│   │   └── config/            // 配置类
│   └── interfaces/            // 用户接口层
│       ├── rest/              // REST接口
│       └── facade/            // 外部服务接口
└── src/main/resources/
    ├── application.yml        // 应用配置
    └── db/migration/          // 数据库迁移脚本
```

### 三、各层具体实现

#### 1. 领域层实现（核心业务）

领域层是系统的核心，包含了所有业务规则和领域模型。以订单为例：

##### 值对象实现：

```java
// 货币值对象
@Value
public class Money {
    @NonNull
    BigDecimal amount;
    @NonNull
    Currency currency;

    // 确保货币值不能为负
    public Money(BigDecimal amount, Currency currency) {
        if (amount.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("金额不能为负数");
        }
        this.amount = amount;
        this.currency = currency;
    }

    // 金额加法操作
    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("货币类型不匹配");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }
}
```

##### 实体与聚合根实现：

```java
// 订单项实体
@Entity
@Table(name = "order_item")
@Data
@NoArgsConstructor
public class OrderItem {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String productId;
    private String productName;
    private int quantity;

    @Embedded
    private Money unitPrice;

    // 计算订单项总价
    public Money calculateTotal() {
        return new Money(
                unitPrice.getAmount().multiply(BigDecimal.valueOf(quantity)),
                unitPrice.getCurrency()
        );
    }
}

// 订单聚合根
@Entity
@Table(name = "orders")
@Data
@NoArgsConstructor
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String orderNumber;
    private String customerId;

    @Enumerated(EnumType.STRING)
    private OrderStatus status;

    @Embedded
    private Money totalAmount;

    @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinColumn(name = "order_id")
    private List<OrderItem> items = new ArrayList<>();

    // 领域行为：添加订单项
    public void addItem(OrderItem item) {
        this.items.add(item);
        recalculateTotal();
    }

    // 领域行为：重新计算订单总价
    private void recalculateTotal() {
        this.totalAmount = items.stream()
                .map(OrderItem::calculateTotal)
                .reduce(new Money(BigDecimal.ZERO, Currency.getInstance("CNY")), Money::add);
    }

    // 领域行为：确认订单
    public void confirm() {
        if (this.status != OrderStatus.CREATED) {
            throw new IllegalStateException("只有创建状态的订单可以确认");
        }
        this.status = OrderStatus.CONFIRMED;
    }
}
```

##### 领域服务与仓储接口：

```java
// 订单仓储接口
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(Long id);
    Optional<Order> findByOrderNumber(String orderNumber);
}

// 订单领域服务（处理跨聚合的业务逻辑）
@Service
@RequiredArgsConstructor
public class OrderDomainService {
    private final InventoryService inventoryService;

    // 检查订单商品库存
    public boolean checkInventory(Order order) {
        return order.getItems().stream()
                .allMatch(item -> inventoryService.hasStock(item.getProductId(), item.getQuantity()));
    }
}
```

#### 2. 应用层实现

应用层负责协调领域对象完成业务用例，处理事务和权限：

```java
// 命令对象（封装创建订单的请求参数）
@Data
public class CreateOrderCommand {
    @NotBlank(message = "客户ID不能为空")
    private String customerId;

    @NotEmpty(message = "订单项不能为空")
    private List<OrderItemCommand> items;
}

// 应用服务
@Service
@RequiredArgsConstructor
@Transactional
public class OrderApplicationService {
    private final OrderRepository orderRepository;
    private final OrderDomainService orderDomainService;
    private final OrderMapper orderMapper;

    // 创建订单用例
    public OrderDTO createOrder(CreateOrderCommand command) {
        // 1. 转换命令为领域对象
        Order order = orderMapper.toDomain(command);

        // 2. 生成订单号
        order.setOrderNumber(generateOrderNumber());
        order.setStatus(OrderStatus.CREATED);

        // 3. 业务规则校验
        if (!orderDomainService.checkInventory(order)) {
            throw new InsufficientInventoryException("商品库存不足");
        }

        // 4. 保存订单
        Order savedOrder = orderRepository.save(order);

        // 5. 发布领域事件（后续通过消息队列实现）
        // orderEventPublisher.publish(new OrderCreatedEvent(savedOrder));

        // 6. 转换为DTO返回
        return orderMapper.toDTO(savedOrder);
    }

    // 确认订单用例
    public void confirmOrder(String orderNumber) {
        Order order = orderRepository.findByOrderNumber(orderNumber)
                .orElseThrow(() -> new OrderNotFoundException("订单不存在: " + orderNumber));

        order.confirm();
        orderRepository.save(order);
    }

    // 生成唯一订单号
    private String generateOrderNumber() {
        return "ORD" + LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"))
                + RandomStringUtils.randomNumeric(4);
    }
}
```

#### 3. 基础设施层实现

基础设施层提供技术支持，实现领域层定义的接口：

```java
// 订单仓储JPA实现
@Repository
public interface JpaOrderRepository extends OrderRepository, JpaRepository<Order, Long> {
    @Override
    Optional<Order> findByOrderNumber(String orderNumber);
}

// 库存服务（外部服务调用实现）
@Service
public class InventoryServiceImpl implements InventoryService {
    private final RestTemplate restTemplate;

    @Override
    public boolean hasStock(String productId, int quantity) {
        // 调用库存服务API检查库存
        String url = "http://inventory-service/api/inventory/check?productId=" + productId + "&quantity=" + quantity;
        try {
            return restTemplate.getForObject(url, Boolean.class);
        } catch (Exception e) {
            log.error("检查库存失败", e);
            return false;
        }
    }
}
```

#### 4. 用户接口层实现

用户接口层处理HTTP请求和响应：

```java
@RestController
@RequestMapping("/api/orders")
@RequiredArgsConstructor
public class OrderController {
    private final OrderApplicationService orderApplicationService;

    @PostMapping
    public ResponseEntity<OrderDTO> createOrder(@Valid @RequestBody CreateOrderCommand command) {
        OrderDTO orderDTO = orderApplicationService.createOrder(command);
        return ResponseEntity
                .created(URI.create("/api/orders/" + orderDTO.getOrderNumber()))
                .body(orderDTO);
    }

    @PutMapping("/{orderNumber}/confirm")
    public ResponseEntity<Void> confirmOrder(@PathVariable String orderNumber) {
        orderApplicationService.confirmOrder(orderNumber);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{orderNumber}")
    public ResponseEntity<OrderDTO> getOrder(@PathVariable String orderNumber) {
        return orderApplicationService.getOrderByNumber(orderNumber)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
```

### 四、关键技术点说明

- **值对象的持久化**：使用@Embedded和@Embeddable注解将值对象嵌入实体中，避免数据库表膨胀。
- **聚合根的设计**：订单作为聚合根，负责维护订单项的一致性，所有对订单项的操作都通过订单聚合根完成。
- **领域事件处理**：在应用服务中发布领域事件，通过Spring的事件机制或消息队列（如Kafka）实现领域事件的异步处理，解耦系统组件。
- **事务管理**：在应用服务层使用@Transactional注解管理事务边界，确保业务操作的原子性。
- **对象映射**：使用MapStruct框架实现DTO与领域对象之间的映射，避免手动编写大量getter/setter代码。

### 五、总结

基于DDD的分层架构通过清晰的职责划分，将业务逻辑与技术实现分离，使系统更具可维护性和扩展性。在实际项目中，应根据业务复杂度灵活调整DDD的实现方式，不必生搬硬套所有概念。

随着微服务架构的发展，DDD与微服务的结合越来越紧密，通过领域边界划分微服务可以有效降低服务间的耦合，这也是DDD在现代软件开发中越来越受欢迎的重要原因。