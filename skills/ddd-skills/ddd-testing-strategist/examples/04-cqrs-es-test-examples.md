# CQRS & Event Sourcing Test Examples

## CQRS Command Handler Test

```java
class CreateOrderHandlerTest {
    @Mock private OrderRepository orderRepository;
    @Mock private EventPublisher eventPublisher;
    @InjectMocks private CreateOrderHandler handler;

    @Test void handle_creates_and_saves_order() {
        var cmd = new CreateOrderCommand("cust-123", List.of(
            new OrderItemDto("p1", 2),
            new OrderItemDto("p2", 1)
        ));

        var result = handler.handle(cmd);

        assertNotNull(result.orderId());
        verify(orderRepository).save(any(Order.class));
        verify(eventPublisher).publish(any(OrderCreatedEvent.class));
    }

    @Test void handle_throws_when_duplicate() {
        var cmd = new CreateOrderCommand("cust-123", List.of(
            new OrderItemDto("p1", 1)
        ));
        doThrow(new DuplicateOrderException("Duplicate request"))
            .when(orderRepository).save(any());

        assertThrows(DuplicateOrderException.class, () -> handler.handle(cmd));
        verify(eventPublisher, never()).publish(any());
    }
}

class PayOrderHandlerTest {
    @Mock private OrderRepository orderRepository;
    @Mock private PaymentGateway paymentGateway;
    @Mock private EventPublisher eventPublisher;
    @InjectMocks private PayOrderHandler handler;

    @Test void handle_pays_and_saves() {
        var order = createTestOrder();
        when(orderRepository.findById(any())).thenReturn(Optional.of(order));

        handler.handle(new PayOrderCommand("order-1"));

        assertEquals(OrderStatus.PAID, order.getStatus());
        verify(orderRepository).save(order);
        verify(paymentGateway).charge(any());
        verify(eventPublisher).publish(any(OrderPaidEvent.class));
    }

    @Test void handle_throws_for_already_paid() {
        var order = createPaidOrder();
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));

        assertThrows(OrderException.class,
            () -> handler.handle(new PayOrderCommand(order.getId().value())));

        verify(orderRepository, never()).save(any());
        verify(paymentGateway, never()).charge(any());
    }

    @Test void handle_throws_when_order_not_found() {
        when(orderRepository.findById(any())).thenReturn(Optional.empty());

        assertThrows(OrderNotFoundException.class,
            () -> handler.handle(new PayOrderCommand("nonexistent")));
    }
}
```

## CQRS Query Handler Test

```java
@SpringBootTest
@Testcontainers
class OrderQueryHandlerTest {
    @Autowired private OrderQueryHandler queryHandler;
    @Autowired private JdbcTemplate jdbc;

    @BeforeEach void setUp() {
        jdbc.execute("TRUNCATE order_read_model CASCADE");
        jdbc.update("""
            INSERT INTO order_read_model (id, customer_id, status, total, item_count, created_at)
            VALUES ('o1', 'c1', 'PAID', 4500, 2, NOW())
        """);
        jdbc.update("""
            INSERT INTO order_read_model (id, customer_id, status, total, item_count, created_at)
            VALUES ('o2', 'c1', 'DRAFT', 2000, 1, NOW())
        """);
    }

    @Test void get_order_by_id() {
        var order = queryHandler.getOrderById("o1");
        assertTrue(order.isPresent());
        assertEquals("o1", order.get().getId());
        assertEquals("PAID", order.get().getStatus());
        assertEquals(4500, order.get().getTotal());
        assertEquals(2, order.get().getItemCount());
    }

    @Test void get_order_returns_empty_for_nonexistent() {
        assertTrue(queryHandler.getOrderById("nonexistent").isEmpty());
    }

    @Test void list_orders_by_customer() {
        var orders = queryHandler.listByCustomer("c1");
        assertEquals(2, orders.size());
    }

    @Test void list_orders_by_status() {
        var paid = queryHandler.listByStatus("PAID");
        assertEquals(1, paid.size());
        assertEquals("o1", paid.get(0).getId());
    }

    @Test void list_orders_by_customer_and_status() {
        var orders = queryHandler.listByCustomerAndStatus("c1", "DRAFT");
        assertEquals(1, orders.size());
        assertEquals("o2", orders.get(0).getId());
    }
}
```

## Event Sourcing — Aggregate Replay Test

```java
class EventSourcedOrderTest {
    @Test void replay_events_builds_correct_state() {
        var events = List.of(
            new OrderCreatedEvent("order-1", "cust-123"),
            new OrderItemAddedEvent("order-1", "p1", 2, 1000),
            new OrderItemAddedEvent("order-1", "p2", 1, 2500),
            new OrderPaidEvent("order-1", 4500)
        );

        var order = EventSourcedOrder.replay(events);

        assertEquals(OrderStatus.PAID, order.getStatus());
        assertEquals("cust-123", order.getCustomerId());
        assertEquals(2, order.getItems().size());
        assertEquals(4500, order.getTotal());
    }

    @Test void replay_handles_empty_order_creation() {
        var events = List.of(
            new OrderCreatedEvent("order-1", "cust-123")
        );

        var order = EventSourcedOrder.replay(events);

        assertEquals(OrderStatus.DRAFT, order.getStatus());
        assertTrue(order.getItems().isEmpty());
        assertEquals(0, order.getTotal());
    }

    @Test void replay_handles_cancellation() {
        var events = List.of(
            new OrderCreatedEvent("order-1", "cust-123"),
            new OrderCancelledEvent("order-1", "Customer request")
        );

        var order = EventSourcedOrder.replay(events);

        assertEquals(OrderStatus.CANCELLED, order.getStatus());
    }

    @Test void replay_with_snapshot_and_new_events() {
        var snapshot = new OrderSnapshot("order-1", "cust-123", OrderStatus.PAID, 4500);
        var newEvents = List.of(
            new OrderRefundedEvent("order-1", 4500)
        );

        var order = EventSourcedOrder.replayFromSnapshot(snapshot, newEvents);

        assertEquals(OrderStatus.REFUNDED, order.getStatus());
        assertEquals(0, order.getTotal());
    }

    @Test void replay_throws_on_invalid_event_sequence() {
        var events = List.of(
            new OrderPaidEvent("order-1", 1000) // Pay before creation
        );

        assertThrows(InvalidEventSequenceException.class,
            () -> EventSourcedOrder.replay(events));
    }
}
```

## Event Sourcing — Projection Test

```java
class OrderProjectionTest {
    private InMemoryOrderViewStore viewStore;
    private OrderProjection projection;

    @BeforeEach void setUp() {
        viewStore = new InMemoryOrderViewStore();
        projection = new OrderProjection(viewStore);
    }

    @Test void on_order_created_creates_view() {
        projection.on(new OrderCreatedEvent("o1", "c1"));

        var view = viewStore.findById("o1");
        assertTrue(view.isPresent());
        assertEquals("o1", view.get().getId());
        assertEquals("DRAFT", view.get().getStatus());
        assertEquals("c1", view.get().getCustomerId());
        assertEquals(0, view.get().getTotal());
    }

    @Test void on_order_paid_updates_view_status_and_total() {
        viewStore.save(new OrderView("o1", "DRAFT", 0));
        projection.on(new OrderPaidEvent("o1", 4500));

        var view = viewStore.findById("o1");
        assertEquals("PAID", view.get().getStatus());
        assertEquals(4500, view.get().getTotal());
    }

    @Test void on_item_added_updates_view_total() {
        viewStore.save(new OrderView("o1", "DRAFT", 0));
        projection.on(new OrderItemAddedEvent("o1", "p1", 2, 1000));

        var view = viewStore.findById("o1");
        assertEquals(2000, view.get().getTotal()); // 2 * 1000
    }

    @Test void multiple_events_produce_consistent_state() {
        projection.on(new OrderCreatedEvent("o1", "c1"));
        projection.on(new OrderItemAddedEvent("o1", "p1", 2, 1000));
        projection.on(new OrderItemAddedEvent("o1", "p2", 1, 2500));
        projection.on(new OrderPaidEvent("o1", 4500));

        var view = viewStore.findById("o1");
        assertEquals("PAID", view.get().getStatus());
        assertEquals(4500, view.get().getTotal());
        assertEquals("c1", view.get().getCustomerId());
    }

    @Test void projection_is_idempotent() {
        projection.on(new OrderCreatedEvent("o1", "c1"));
        projection.on(new OrderCreatedEvent("o1", "c1")); // duplicate

        var view = viewStore.findById("o1");
        assertTrue(view.isPresent());
        // Should not create duplicate or throw
    }
}
```

## CQRS Read Model Seed Test

```java
@Component
class OrderReadModelSeeder {
    private final JdbcTemplate jdbc;

    public OrderReadModelSeeder(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public void seedTestData() {
        jdbc.execute("TRUNCATE order_read_model CASCADE");
        jdbc.update("""
            INSERT INTO order_read_model (id, customer_id, status, total, item_count)
            VALUES ('seed-order-1', 'seed-cust-1', 'PAID', 3000, 1)
        """);
        jdbc.update("""
            INSERT INTO order_read_model (id, customer_id, status, total, item_count)
            VALUES ('seed-order-2', 'seed-cust-1', 'DRAFT', 1500, 1)
        """);
    }

    public void cleanTestData() {
        jdbc.execute("TRUNCATE order_read_model CASCADE");
    }
}
```
