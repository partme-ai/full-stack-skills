# Architecture Testing Comparison

## 各架构的测试重心差异

| 架构 | Domain 测试重心 | Application 测试 | Adapter 测试 | 关键差异 |
|------|---------------|----------------|-------------|---------|
| **DDD Layered** | 聚合根 + 值对象 + 领域服务 | AppService（薄层，Mock Repository） | Controller + DTO 转换 | 优势：Domain 测试占比最高（60%+） |
| **Hexagonal** | 聚合根 + 端口接口 | UseCase 实现（注入端口接口） | 主适配器 + 次适配器分别测试 | 优势：端口 Mock 最容易；劣势：适配器测试多 |
| **Clean Architecture** | Entity + Enterprise 规则 | UseCase Interactor（Mock 输出端口） | Controller + Gateway + Presenter | 优势：企业规则可独立测试；劣势：层数多测试路径长 |
| **COLA** | Domain 模块 | App Service（编排 + 事务） | Adapter（Web + MQ Consumer） | 优势：模块隔离好；劣势：需额外测 CQRS 分流 |
| **CQRS** | Command 聚合根（同标准测试） | Command Handler + Query Handler 分离 | Command API + Query API 分别测 | 优势：读写解耦测试简单；劣势：Query 测物化视图 |
| **Event Sourcing** | Event Replay 重建测试 | Event Handler + Projection | Event Store 集成 | 优势：事件流可追溯；劣势：Event Replay 必测 |

## Hexagonal 架构的 Port Mock 模式

```java
// Domain 定义端口
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
}

// 应用层测试 — 注入 Mock 端口
class PayOrderServiceTest {
    @Mock OrderRepository orderRepository;
    @Mock PaymentGateway paymentGateway;
    @InjectMocks PayOrderService service;

    @Test void pay_order_success() {
        var order = createTestOrder();
        when(orderRepository.findById(order.getId())).thenReturn(Optional.of(order));

        service.pay(order.getId().value());

        verify(orderRepository).save(order);
        verify(paymentGateway).charge(any());
    }
}

// 适配器集成测试 — 真实基础设施
@SpringBootTest
@Testcontainers
class JpaOrderRepositoryTest {
    @Autowired OrderRepository orderRepository;

    @Test void persists_and_retrieves() {
        // 真实 DB 操作
    }
}
```

## Clean Architecture 的分层测试

```java
// Enterprise 层 — 零依赖，纯 POJO 测试
@Test void entity_order_should_not_allow_negative_total() {
    assertThrows(DomainException.class, () ->
        OrderEntity.create("order-1", new Money(-10, "USD")));
}

// UseCase 层 — Mock 输出端口
@Test void createOrderInteractor_should_save_to_repository() {
    var repo = mock(OrderOutputPort.class);
    var interactor = new CreateOrderInteractor(repo);

    interactor.execute(new CreateOrderInput("cust-1", items));

    verify(repo).save(any(OrderEntity.class));
}

// Adapter 层 — 集成测试
@SpringBootTest
class OrderControllerTest {
    @Test void post_order_returns_201() {
        // 真实 HTTP + 真实 DB
    }
}
```

## COLA 架构模块化测试

```java
// domain 模块 — 零框架依赖
@Test void order_pay_changes_status() {
    Order order = Order.create(customerId, items);
    order.pay(mockGateway);
    assertEquals(OrderStatus.PAID, order.getStatus());
}

// app 模块 — Mock domain 仓储
@Test void orderAppService_create() {
    when(orderRepository.save(any())).thenReturn(order);
    var result = orderAppService.createOrder(cmd);
    assertNotNull(result);
}

// adapter 模块 — 集成测试
@WebMvcTest(OrderController.class)
class OrderControllerTest {
    @Test void create_returns_201() { /* ... */ }
}
```

## 根据项目阶段选择测试策略

| 项目阶段 | 推荐测试重点 | 比例 |
|---------|------------|:---:|
| **新建 DDD 项目** | Value Object + Aggregate Root（TDDD） | 70% Domain + 20% + 10% |
| **已有项目引入 DDD** | 现有代码分层测试 + 新 Domain 测试 | 40% 适配器 + 40% Domain + 20% |
| **遗留系统迁移** | 防腐层测试 + 新聚合测试 | 40% 集成 + 30% Domain + 30% |
| **微服务拆分后** | 契约测试 + 跨服务 E2E | 30% 契约 + 30% 单服务 + 40% E2E |
