# CQRS 测试策略示例

> Command/Query 分离后如何编写测试

```java
@SpringBootTest
class OrderCqrsTest {

    @Test
    void createOrder_Command成功_Query可查() {
        // 执行 Command
        CreateOrderCommand cmd = new CreateOrderCommand("CUST-1", List.of(
            new OrderItemCommand("PROD-1", 2)));
        OrderCreatedResult result = commandService.createOrder(cmd);

        // 验证 Query
        OrderDetailDTO detail = queryService.getOrderDetail(result.getOrderId());
        assertThat(detail.getStatus()).isEqualTo("CREATED");
        assertThat(detail.getItems()).hasSize(1);
    }

    @Test
    void 事件同步_最终一致验证() {
        commandService.payOrder(new PayOrderCommand("ORDER-1"));

        // 等待异步事件同步
        await().atMost(5, SECONDS).untilAsserted(() -> {
            OrderDocument doc = queryService.getOrder("ORDER-1");
            assertThat(doc.getStatus()).isEqualTo("PAID");
        });
    }
}
```
