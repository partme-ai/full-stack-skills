# Spring Boot DDD 分层架构实操示例


## 技术栈

- Spring Boot 3.2.x + Spring Data JPA 3.2.x + Lombok 1.18.x
- Jakarta Validation 3.0 + PostgreSQL 16
- Maven 3.9.x

## 聚合根示例（充血模型）

```java
@Entity
@Table(name = "orders")
@Data
@NoArgsConstructor
public class Order {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
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

    // 领域行为
    public void addItem(OrderItem item) {
        this.items.add(item);
        recalculateTotal();
    }

    private void recalculateTotal() {
        this.totalAmount = items.stream()
            .map(OrderItem::calculateTotal)
            .reduce(Money.zero(), Money::add);
    }

    public void confirm() {
        if (this.status != OrderStatus.CREATED) {
            throw new InvalidOrderStateException("只有已创建状态的订单才能确认");
        }
        this.status = OrderStatus.CONFIRMED;
    }
}
```

## 值对象示例

```java
@Embeddable
public class Money {
    private BigDecimal amount;
    private String currency;

    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("货币类型不匹配");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    public static Money zero() {
        return new Money(BigDecimal.ZERO, "CNY");
    }
}
```

## 仓储接口

```java
public interface OrderRepository {
    Optional<Order> findById(Long id);
    Order save(Order order);
    List<Order> findByCustomerId(String customerId);
}
```

## 应用服务

```java
@Service
@Transactional
public class OrderApplicationService {
    private final OrderRepository orderRepository;

    public OrderDTO createOrder(CreateOrderCommand command) {
        Order order = new Order();
        order.setCustomerId(command.getCustomerId());
        for (OrderItemCommand itemCmd : command.getItems()) {
            order.addItem(new OrderItem(itemCmd.getProductId(), itemCmd.getQuantity(), itemCmd.getUnitPrice()));
        }
        order.confirm();
        return OrderMapper.toDTO(orderRepository.save(order));
    }
}
```

## 源代码

