# Unit Testing Strategies — Domain Layer

## Value Object Tests

Value objects are immutable, self-validating types. Tests focus on construction validation, behavior (arithmetic/operations), and equality.

### Construction Validation

```java
@Test void money_throws_for_negative_amount() {
    assertThrows(IllegalArgumentException.class, () -> new Money(-1, "USD"));
}
@Test void money_throws_for_null_currency() {
    assertThrows(NullPointerException.class, () -> new Money(10, null));
}
@Test void money_creates_successfully_with_valid_input() {
    assertDoesNotThrow(() -> new Money(10.50, "USD"));
}
```

### Behavior Tests

```java
@Test void money_add_returns_sum_same_currency() {
    assertEquals(new Money(30, "USD"), new Money(10, "USD").add(new Money(20, "USD")));
}
@Test void money_add_throws_for_different_currencies() {
    assertThrows(IllegalArgumentException.class,
        () -> new Money(10, "USD").add(new Money(20, "CNY")));
}
@Test void money_multiply_scales_correctly() {
    assertEquals(new Money(25, "USD"), new Money(5, "USD").multiply(5));
}
@Test void money_multiply_throws_for_negative_factor() {
    assertThrows(IllegalArgumentException.class,
        () -> new Money(10, "USD").multiply(-1));
}
```

### Equality Tests

```java
@Test void money_equals_same_amount_and_currency() {
    assertEquals(new Money(10, "USD"), new Money(10, "USD"));
}
@Test void money_not_equals_different_amount() {
    assertNotEquals(new Money(10, "USD"), new Money(20, "USD"));
}
@Test void money_not_equals_different_currency() {
    assertNotEquals(new Money(10, "USD"), new Money(10, "CNY"));
}
```

## Aggregate Root Tests

Test business rules, state transitions, invariants, and domain event emission. Each state transition = one test class.

### Order State Transition Tests

```java
class OrderPayTest {
    @Test void pay_changes_status_to_paid_when_draft() {
        Order order = Order.create(customerId, items);
        order.pay(mockGateway);
        assertEquals(OrderStatus.PAID, order.getStatus());
    }
    @Test void pay_emits_orderPaidEvent() {
        Order order = Order.create(customerId, items);
        order.pay(mockGateway);
        assertTrue(order.getDomainEvents().stream()
            .anyMatch(e -> e instanceof OrderPaidEvent));
    }
    @Test void pay_throws_when_already_paid() {
        Order order = createPaidOrder();
        assertThrows(OrderException.class, () -> order.pay(mockGateway));
    }
    @Test void pay_throws_when_cancelled() {
        Order order = Order.create(customerId, items);
        order.cancel("test");
        assertThrows(OrderException.class, () -> order.pay(mockGateway));
    }
    @Test void pay_records_payment_details() {
        Order order = Order.create(customerId, items);
        order.pay(mockGateway);
        assertNotNull(order.getPaidAt());
        assertEquals(PaymentMethod.WECHAT, order.getPaymentMethod());
    }
}

class OrderCancelTest {
    @Test void cancel_changes_status_when_draft() {
        Order order = Order.create(customerId, items);
        order.cancel("Customer request");
        assertEquals(OrderStatus.CANCELLED, order.getStatus());
    }
    @Test void cancel_emits_orderCancelledEvent() {
        Order order = Order.create(customerId, items);
        order.cancel("Customer request");
        assertTrue(order.getDomainEvents().stream()
            .anyMatch(e -> e instanceof OrderCancelledEvent));
    }
    @Test void cancel_throws_when_already_shipped() {
        Order order = createShippedOrder();
        assertThrows(OrderException.class, () -> order.cancel("test"));
    }
}
```

### Invariant Tests

```java
class OrderInvariantTest {
    @Test void total_must_equal_sum_of_item_subtotals() {
        Order order = Order.create(customerId, List.of(
            new OrderItem(ProductId.from("p1"), Quantity.of(2), new Money(10, "USD")),
            new OrderItem(ProductId.from("p2"), Quantity.of(1), new Money(25, "USD"))
        ));
        assertEquals(new Money(45, "USD"), order.calculateTotal());
    }
    @Test void cannot_add_item_after_shipped() {
        Order order = createShippedOrder();
        assertThrows(OrderException.class,
            () -> order.addItem(ProductId.from("p3"), Quantity.of(1), new Money(10, "USD")));
    }
    @Test void order_without_items_cannot_be_confirmed() {
        Order order = Order.create(customerId);
        assertThrows(OrderException.class, order::confirm);
    }
}
```

## Domain Service Tests

Test cross-entity business logic with mocked repositories. Do NOT mock other domain services.

```java
class PricingServiceTest {
    private PricingService pricingService;
    private OrderRepository orderRepository;

    @Test void applies_vip_discount_for_vip_customer() {
        Order order = Order.create(vipCustomerId, items);
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));

        pricingService.calculatePrice(order.getId());

        assertEquals(new Money(90, "USD"), order.getTotalAmount()); // 10% off
    }

    @Test void applies_no_discount_for_regular_customer() {
        Order order = Order.create(regularCustomerId, items);
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));

        pricingService.calculatePrice(order.getId());

        assertEquals(new Money(100, "USD"), order.getTotalAmount()); // full price
    }

    @Test void applies_seasonal_discount_when_active() {
        Order order = Order.create(customerId, items);
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));
        when(discountPolicy.isSeasonalActive()).thenReturn(true);

        pricingService.calculatePrice(order.getId());

        assertTrue(order.getDomainEvents().stream()
            .anyMatch(e -> e instanceof SeasonalDiscountAppliedEvent));
    }
}
```

## Test Naming Convention

```
describe '[Aggregate/Component]'
  describe '[Method/Behavior]'
    it '[expected outcome] when [condition]'
```

Examples:
- `OrderPayTest.pay_throws_when_already_paid`
- `Money.add_returns_sum_same_currency`
- `PricingService.applies_vip_discount_for_vip_customer`
