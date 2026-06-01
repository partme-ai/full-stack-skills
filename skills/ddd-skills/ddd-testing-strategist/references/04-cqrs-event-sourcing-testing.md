# CQRS & Event Sourcing Testing

## CQRS Command Side Testing

Command side = write model. Test aggregate roots with mocked ports. Same pattern as standard Domain testing.

```java
@Test void create_order_command_creates_aggregate() {
    var cmd = new CreateOrderCommand("cust-1", List.of(
        new CreateOrderItem("p1", 2),
        new CreateOrderItem("p2", 1)
    ));

    var result = createOrderHandler.handle(cmd);

    assertNotNull(result.orderId());
    verify(orderRepository).save(any(Order.class));
}

@Test void pay_order_command_changes_status() {
    var order = createTestOrder();
    when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));
    var cmd = new PayOrderCommand(order.getId().value());

    payOrderHandler.handle(cmd);

    assertEquals(OrderStatus.PAID, order.getStatus());
    verify(orderRepository).save(order);
}

@Test void cancel_order_command_throws_for_nonexistent() {
    var cmd = new CancelOrderCommand("nonexistent");
    when(orderRepository.findById(any())).thenReturn(Optional.empty());

    assertThrows(OrderNotFoundException.class, () -> cancelOrderHandler.handle(cmd));
}
```

## CQRS Query Side Testing

Query side = read model. Test materialized views or query repositories directly — no mocks needed.

```java
@SpringBootTest
@Testcontainers
class OrderQueryServiceTest {
    @Autowired private OrderQueryService queryService;
    @Autowired private JdbcTemplate jdbc;

    @BeforeEach void setUp() {
        jdbc.execute("TRUNCATE order_view CASCADE");
        // Seed the read model
        jdbc.update("INSERT INTO order_view (id, customer_id, status, total, created_at) " +
                     "VALUES ('order-1', 'cust-1', 'PAID', 4500, NOW())");
        jdbc.update("INSERT INTO order_view (id, customer_id, status, total, created_at) " +
                     "VALUES ('order-2', 'cust-1', 'DRAFT', 2000, NOW())");
    }

    @Test void find_by_id_returns_dto() {
        var dto = queryService.findById("order-1");
        assertTrue(dto.isPresent());
        assertEquals("order-1", dto.get().getId());
        assertEquals("PAID", dto.get().getStatus());
        assertEquals(4500, dto.get().getTotal());
    }

    @Test void find_by_customer_returns_all_orders() {
        var orders = queryService.findByCustomer("cust-1");
        assertEquals(2, orders.size());
    }

    @Test void find_by_status_returns_filtered() {
        var paid = queryService.findByStatus("PAID");
        assertEquals(1, paid.size());
    }
}
```

## Event Sourcing — Event Replay Tests

Test that aggregate state can be correctly reconstructed from event streams.

```java
@Test void replay_events_reconstructs_aggregate_state() {
    var events = List.<DomainEvent>of(
        new OrderCreatedEvent("order-1", "cust-1"),
        new OrderItemAddedEvent("order-1", ProductId.from("p1"), 2, Money.usd(10)),
        new OrderPaidEvent("order-1", Money.usd(20))
    );

    var order = Order.replay(events);

    assertEquals(OrderStatus.PAID, order.getStatus());
    assertEquals("cust-1", order.getCustomerId().value());
    assertEquals(1, order.getItems().size());
    assertEquals(new Money(20, "USD"), order.getTotalAmount());
}

@Test void replay_empty_events_throws() {
    assertThrows(IllegalArgumentException.class,
        () -> Order.replay(List.of()));
}

@Test void replay_invalid_event_sequence_throws() {
    // Pay before creating
    var events = List.<DomainEvent>of(
        new OrderPaidEvent("order-1", Money.usd(20))
    );
    assertThrows(InvalidEventSequenceException.class,
        () -> Order.replay(events));
}
```

## Event Sourcing — Projection Tests

Test that projection/denormalizer builds the correct read model from events.

```java
class OrderProjectionTest {
    private InMemoryOrderViewStore viewStore;
    private OrderProjection projection;

    @BeforeEach void setUp() {
        viewStore = new InMemoryOrderViewStore();
        projection = new OrderProjection(viewStore);
    }

    @Test void on_order_created_creates_view() {
        projection.on(new OrderCreatedEvent("order-1", "cust-1"));

        var view = viewStore.findById("order-1");
        assertTrue(view.isPresent());
        assertEquals("order-1", view.get().getId());
        assertEquals("DRAFT", view.get().getStatus());
    }

    @Test void on_order_paid_updates_view_status() {
        viewStore.save(new OrderView("order-1", "DRAFT"));
        projection.on(new OrderPaidEvent("order-1", Money.usd(100)));

        var view = viewStore.findById("order-1");
        assertEquals("PAID", view.get().getStatus());
    }

    @Test void on_item_added_updates_total() {
        viewStore.save(new OrderView("order-1", "DRAFT", 0));
        projection.on(new OrderItemAddedEvent("order-1", ProductId.from("p1"), 2, Money.usd(10)));

        var view = viewStore.findById("order-1");
        assertEquals(20, view.get().getTotal()); // 2 * 10
    }

    @Test void multiple_events_produce_correct_state() {
        projection.on(new OrderCreatedEvent("order-1", "cust-1"));
        projection.on(new OrderItemAddedEvent("order-1", ProductId.from("p1"), 2, Money.usd(10)));
        projection.on(new OrderItemAddedEvent("order-1", ProductId.from("p2"), 1, Money.usd(25)));
        projection.on(new OrderPaidEvent("order-1", Money.usd(45)));

        var view = viewStore.findById("order-1");
        assertEquals("PAID", view.get().getStatus());
        assertEquals(45, view.get().getTotal());
    }
}
```

## Event Sourcing — Snapshot Tests

Test that snapshot + remaining events reconstruct correctly.

```java
@Test void snapshot_with_remaining_events_reconstructs_state() {
    var snapshot = new OrderSnapshot("order-1", "cust-1", OrderStatus.DRAFT, Money.zero("USD"));
    var remainingEvents = List.<DomainEvent>of(
        new OrderItemAddedEvent("order-1", ProductId.from("p1"), 2, Money.usd(10)),
        new OrderPaidEvent("order-1", Money.usd(20))
    );

    var order = Order.replayFromSnapshot(snapshot, remainingEvents);

    assertEquals(OrderStatus.PAID, order.getStatus());
    assertEquals(new Money(20, "USD"), order.getTotalAmount());
}
```
