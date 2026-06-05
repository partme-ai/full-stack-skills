# DDD 测试模式 — Builder + Mock 实战


## Test Helpers (Builder 模式)

```java
public class OrderTestBuilder {
    private CustomerId customerId = CustomerId.from("test");
    private List<OrderItem> items = new ArrayList<>();

    public static OrderTestBuilder anOrder() { return new OrderTestBuilder(); }
    public OrderTestBuilder withItem(ProductId p, int qty, Money price) {
        items.add(new OrderItem(p, Quantity.of(qty), price)); return this;
    }

    public Order build() {
        Order o = Order.create(customerId);
        items.forEach(i -> o.addItem(i.getProductId(), i.getQuantity(), i.getUnitPrice()));
        return o;
    }

    public static Order buildDraft() { return anOrder().build(); }
    public static Order buildWithItems() {
        return anOrder().withItem(ProductId.from("p1"), 2, Money.cny(10))
                        .withItem(ProductId.from("p2"), 1, Money.cny(25)).build();
    }
    public static Order buildPaid(/* mock Gateway */) {
        Order o = buildWithItems(); o.pay(mockGateway); return o;
    }
}
```

## 聚合根测试

```java
@Test void order_pay_should_change_status() {
    Order order = OrderTestBuilder.buildWithItems();
    order.pay(mockGateway);
    assertEquals(OrderStatus.PAID, order.getStatus());
    assertTrue(order.getDomainEvents().stream().anyMatch(e -> e instanceof OrderPaidEvent));
}
@Test void order_pay_should_fail_when_cancelled() {
    Order order = OrderTestBuilder.buildWithItems();
    order.cancel("reason");
    assertThrows(OrderException.class, () -> order.pay(mockGateway));
}
```

## 仓储集成测试

```java
@SpringBootTest @Testcontainers
class OrderRepositoryImplTest {
    @Autowired OrderRepository repo;
    @Test void should_save_and_load_complete() {
        Order o = OrderTestBuilder.buildWithItems();
        repo.save(o);
        var loaded = repo.findById(o.getId());
        assertTrue(loaded.isPresent());
        assertEquals(o.getTotalAmount(), loaded.get().getTotalAmount());
    }
}
```

## Mock 策略矩阵

| 测试目标 | Repository | Gateway | EventBus |
|---------|:--:|:--:|:--:|
| 聚合根 | N/A | N/A | Capture |
| 领域服务 | Mock | Mock | Capture |
| 应用服务 | Mock | Mock | Mock |
| 仓储集成 | Real DB | N/A | N/A |
