# Domain Layer Test Examples

## Value Object: Money

```java
import static org.assertj.core.api.Assertions.*;

class MoneyTest {
    @Test void creates_money_with_valid_amount() {
        Money money = new Money(10.50, "USD");
        assertThat(money.getAmount()).isEqualTo(10.50);
        assertThat(money.getCurrency()).isEqualTo("USD");
    }

    @Test void throws_for_negative_amount() {
        assertThatThrownBy(() -> new Money(-1, "USD"))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessageContaining("Amount must not be negative");
    }

    @Test void adds_same_currency() {
        Money sum = new Money(10, "USD").add(new Money(20, "USD"));
        assertThat(sum).isEqualTo(new Money(30, "USD"));
    }

    @Test void throws_for_different_currencies_on_add() {
        assertThatThrownBy(() -> new Money(10, "USD").add(new Money(20, "CNY")))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessageContaining("Currency mismatch");
    }

    @Test void multiplies_by_factor() {
        Money result = new Money(5.50, "USD").multiply(3);
        assertThat(result).isEqualTo(new Money(16.50, "USD"));
    }

    @Test void equals_same_amount_and_currency() {
        assertThat(new Money(10, "USD")).isEqualTo(new Money(10, "USD"));
    }

    @Test void not_equals_different_amount() {
        assertThat(new Money(10, "USD")).isNotEqualTo(new Money(20, "USD"));
    }
}
```

## Aggregate Root: Order

```java
class OrderTest {

    // --- Create Order ---

    @Test void creates_order_with_draft_status() {
        Order order = Order.create(CustomerId.from("cust-123"));

        assertThat(order.getStatus()).isEqualTo(OrderStatus.DRAFT);
        assertThat(order.getCustomerId()).isEqualTo(CustomerId.from("cust-123"));
        assertThat(order.getItems()).isEmpty();
    }

    @Test void creation_emits_orderCreated_event() {
        Order order = Order.create(CustomerId.from("cust-123"));

        assertThat(order.getDomainEvents())
            .hasSize(1)
            .first()
            .isInstanceOf(OrderCreatedEvent.class);
    }

    // --- Add Item ---

    @Test void adds_item_to_order() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.addItem(ProductId.from("p1"), Quantity.of(2), new Money(10, "USD"));

        assertThat(order.getItems()).hasSize(1);
        assertThat(order.getItems().get(0).getProductId()).isEqualTo(ProductId.from("p1"));
        assertThat(order.getItems().get(0).getQuantity()).isEqualTo(Quantity.of(2));
    }

    @Test void increases_quantity_for_existing_product() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.addItem(ProductId.from("p1"), Quantity.of(2), new Money(10, "USD"));
        order.addItem(ProductId.from("p1"), Quantity.of(3), new Money(10, "USD"));

        assertThat(order.getItems()).hasSize(1);
        assertThat(order.getItems().get(0).getQuantity()).isEqualTo(Quantity.of(5));
    }

    @Test void throws_when_adding_item_to_cancelled_order() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.cancel("test");

        assertThatThrownBy(() ->
            order.addItem(ProductId.from("p1"), Quantity.of(1), new Money(10, "USD")))
            .isInstanceOf(OrderException.class)
            .hasMessageContaining("cancelled");
    }

    @Test void throws_when_adding_item_with_zero_quantity() {
        Order order = Order.create(CustomerId.from("cust-123"));

        assertThatThrownBy(() ->
            order.addItem(ProductId.from("p1"), Quantity.of(0), new Money(10, "USD")))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessageContaining("Quantity must be positive");
    }

    // --- Pay Order ---

    @Test void pays_order_successfully() {
        Order order = createOrderWithItems();
        order.pay(mock(PaymentGateway.class));

        assertThat(order.getStatus()).isEqualTo(OrderStatus.PAID);
        assertThat(order.getPaidAt()).isNotNull();
    }

    @Test void pay_emits_orderPaid_event() {
        Order order = createOrderWithItems();
        order.pay(mock(PaymentGateway.class));

        assertThat(order.getDomainEvents())
            .filteredOn(e -> e instanceof OrderPaidEvent)
            .hasSize(1);
    }

    @Test void throws_when_paying_already_paid_order() {
        Order order = createPaidOrder();

        assertThatThrownBy(() -> order.pay(mock(PaymentGateway.class)))
            .isInstanceOf(OrderException.class)
            .hasMessageContaining("already paid");
    }

    // --- Cancel Order ---

    @Test void cancels_order() {
        Order order = createOrderWithItems();
        order.cancel("Customer changed mind");

        assertThat(order.getStatus()).isEqualTo(OrderStatus.CANCELLED);
    }

    @Test void cancel_emits_orderCancelled_event() {
        Order order = createOrderWithItems();
        order.cancel("Customer changed mind");

        assertThat(order.getDomainEvents())
            .filteredOn(e -> e instanceof OrderCancelledEvent)
            .hasSize(1);
    }

    @Test void cancelled_event_contains_reason() {
        Order order = createOrderWithItems();
        order.cancel("Duplicate order");

        assertThat(order.getDomainEvents())
            .filteredOn(e -> e instanceof OrderCancelledEvent)
            .first()
            .extracting("reason")
            .isEqualTo("Duplicate order");
    }

    // --- Total Calculation ---

    @Test void calculates_total_correctly() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.addItem(ProductId.from("p1"), Quantity.of(2), new Money(10, "USD"));
        order.addItem(ProductId.from("p2"), Quantity.of(1), new Money(25, "USD"));

        assertThat(order.calculateTotal()).isEqualTo(new Money(45, "USD"));
    }

    @Test void total_is_zero_for_empty_order() {
        Order order = Order.create(CustomerId.from("cust-123"));

        assertThat(order.calculateTotal()).isEqualTo(Money.zero("USD"));
    }

    // --- Test Fixture Builders ---

    private Order createOrderWithItems() {
        Order order = Order.create(CustomerId.from("cust-123"));
        order.addItem(ProductId.from("p1"), Quantity.of(2), new Money(10, "USD"));
        return order;
    }

    private Order createPaidOrder() {
        Order order = createOrderWithItems();
        order.pay(mock(PaymentGateway.class));
        order.clearEvents();
        return order;
    }
}
```

## Domain Service: PricingService

```java
class PricingServiceTest {
    @Mock OrderRepository orderRepository;
    @Mock DiscountPolicy discountPolicy;
    @InjectMocks PricingService pricingService;

    @Test void calculates_price_without_discount() {
        Order order = createOrderWithItems(new Money(100, "USD"));
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));
        when(discountPolicy.isVipCustomer(order.getCustomerId())).thenReturn(false);

        pricingService.calculatePrice(order.getId());

        assertThat(order.getTotalAmount()).isEqualTo(new Money(100, "USD"));
    }

    @Test void applies_vip_discount() {
        Order order = createOrderWithItems(new Money(100, "USD"));
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));
        when(discountPolicy.isVipCustomer(order.getCustomerId())).thenReturn(true);
        when(discountPolicy.getVipDiscountRate()).thenReturn(0.1);

        pricingService.calculatePrice(order.getId());

        assertThat(order.getTotalAmount()).isEqualTo(new Money(90, "USD"));
    }

    @Test void applies_seasonal_discount_on_top_of_vip() {
        Order order = createOrderWithItems(new Money(100, "USD"));
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));
        when(discountPolicy.isVipCustomer(order.getCustomerId())).thenReturn(true);
        when(discountPolicy.getVipDiscountRate()).thenReturn(0.1);
        when(discountPolicy.isSeasonalActive()).thenReturn(true);
        when(discountPolicy.getSeasonalDiscountRate()).thenReturn(0.2);

        pricingService.calculatePrice(order.getId());

        assertThat(order.getTotalAmount()).isEqualTo(new Money(72, "USD"));
    }
}
```
