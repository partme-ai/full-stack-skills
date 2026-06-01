# 5 种架构 CQRS 集成对比示例

> 演示同一业务（订单支付）在 5 种 DDD 架构下的 CQRS 集成模式

## 业务

```
用户支付订单 → Command: PayOrderCommand → 领域事件: OrderPaidEvent → Query: 订单状态更新
```

## 1. Layered + CQRS

**目录**: `app/service/command/PayOrderCommandService.java` + `app/service/query/OrderQueryService.java`

```java
// Command Service (Application 层)
@Service
public class PayOrderCommandService {
    private final OrderRepository orderRepository;
    private final EventPublisher eventPublisher;

    @Transactional
    public void payOrder(PayOrderCommand command) {
        Order order = orderRepository.findById(command.getOrderId())
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));
        order.pay();
        orderRepository.save(order);
        eventPublisher.publish(new OrderPaidEvent(order.getId()));
    }
}

// Query Service (Application 层)
@Service
public class OrderQueryService {
    private final OrderReadRepository readRepository;

    public OrderDetailDTO getOrder(String orderId) {
        return readRepository.findDetailById(orderId);
    }
}
```

## 2. Onion + CQRS

**目录**: `core/application/command/PayOrderUseCase.java` + `core/application/query/GetOrderUseCase.java`

```java
// 定义 UseCase 接口 (Core 层)
public interface PayOrderUseCase {
    void execute(PayOrderCommand command);
}

public interface GetOrderUseCase {
    OrderDetailDTO execute(GetOrderQuery query);
}

// 实现 UseCase (Core 层)
public class PayOrderUseCaseImpl implements PayOrderUseCase {
    private final OrderRepository orderRepository;  // Core 定义的接口
    private final EventBus eventBus;

    @Override
    public void execute(PayOrderCommand command) {
        Order order = orderRepository.findById(command.getOrderId());
        order.pay();
        orderRepository.save(order);
        eventBus.publish(new OrderPaidEvent(order.getId()));
    }
}

public class GetOrderUseCaseImpl implements GetOrderUseCase {
    private final OrderReadRepository readRepo;

    @Override
    public OrderDetailDTO execute(GetOrderQuery query) {
        return readRepo.findDetailById(query.getOrderId());
    }
}
```

## 3. Hexagonal + CQRS

**目录**: `domain/port/command/PayOrderPort.java` + `domain/port/query/OrderQueryPort.java`

```java
// Ports (Domain 层 — 接口定义)
public interface PayOrderPort {  // 入站端口
    void pay(PayOrderCommand command);
}

public interface OrderQueryPort {  // 入站端口
    OrderDetailDTO getOrder(String orderId);
}

// UseCase 实现 (Application 层)
@ApplicationService
public class PayOrderService implements PayOrderPort {
    private final OrderRepository orderRepo;    // 出站端口
    private final EventPublisher eventPub;      // 出站端口

    @Override
    public void pay(PayOrderCommand command) {
        Order order = orderRepo.findById(new OrderId(command.getOrderId()));
        order.pay();
        orderRepo.save(order);
        eventPub.publish(new OrderPaidEvent(order.getId()));
    }
}

// Primary Adapter (REST)
@RestController
public class OrderController {
    private final PayOrderPort payOrder;        // 注入入站端口
    private final OrderQueryPort queryOrder;

    @PostMapping("/orders/{id}/pay")
    public void payOrder(@PathVariable String id) {
        payOrder.pay(new PayOrderCommand(id));
    }

    @GetMapping("/orders/{id}")
    public OrderDetailDTO getOrder(@PathVariable String id) {
        return queryOrder.getOrder(id);
    }
}
```

## 4. Clean + CQRS

**目录**: `usecase/interactor/command/PayOrderInteractor.java` + `usecase/interactor/query/GetOrderInteractor.java`

```java
// Input/Output Ports (UseCase 层)
public interface PayOrderInputPort {
    void execute(PayOrderInput input);
}

public interface OrderQueryOutputPort {
    OrderDetailDTO execute(OrderQueryInput input);
}

// Interactor (UseCase 层)
public class PayOrderInteractor implements PayOrderInputPort {
    private final OrderRepository orderRepo;    // 输出端口
    private final EventPublisher eventPublisher;

    @Override
    public void execute(PayOrderInput input) {
        Order order = orderRepo.findById(input.getOrderId());
        order.pay();
        orderRepo.save(order);
        eventPublisher.publish(new OrderPaidEvent(order.getId()));
    }
}

public class GetOrderInteractor implements OrderQueryOutputPort {
    private final OrderReadRepository readRepo;

    @Override
    public OrderDetailDTO execute(OrderQueryInput input) {
        return readRepo.findDetailById(input.getOrderId());
    }
}
```

## 5. COLA + CQRS

**目录**: `app/command/OrderCommandExecutor.java` + `app/query/OrderQueryExecutor.java`

```java
// Command 执行器 (App 层)
@Component
public class OrderCommandExecutor {
    private final OrderRepository orderRepo;
    private final DomainEventBus eventBus;

    public void execute(PayOrderCmd cmd) {
        Order order = orderRepo.find(cmd.getOrderId());
        order.pay();
        orderRepo.save(order);
        eventBus.fire(new OrderPaidEvent(order.getId()));
    }
}

// Query 执行器 (App 层)
@Component
public class OrderQueryExecutor {
    private final OrderReadRepo readRepo;

    public OrderDetailDTO execute(GetOrderQry qry) {
        return readRepo.findDetail(qry.getOrderId());
    }
}
```

## 集成模式对比总结

| 架构 | Command 位置 | Query 位置 | 事件发布者 | 核心抽象 |
|------|-------------|-----------|-----------|---------|
| Layered | `app/service/command/` | `app/service/query/` | 应用服务 | Service 分离 |
| Onion | `core/application/command/` | `core/application/query/` | UseCase 接口 | UseCase 接口 |
| Hexagonal | `domain/port/command/` | `domain/port/query/` | 入站端口 | Port |
| Clean | `usecase/interactor/command/` | `usecase/interactor/query/` | Interactor | Input/Output Port |
| COLA | `app/command/` | `app/query/` | CommandExecutor | Executor |
