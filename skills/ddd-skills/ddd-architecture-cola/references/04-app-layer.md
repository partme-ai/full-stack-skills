# COLA v5 应用层详解

## 应用层目录结构

```
{project}-app/
├── executor/                     # 执行器（v5 CQRS 强化）
│   ├── command/                  # 命令执行器（写操作）
│   ├── query/                    # 查询执行器（读操作）
│   ├── event/                    # 事件执行器（v5 新增）
│   ├── extension/                # 扩展执行器
│   └── interceptor/              # 执行器拦截器（日志、监控、校验）
├── model/                        # 应用模型（v5 明确分离）
│   ├── command/                  # 命令对象（写请求 DTO）
│   ├── query/                    # 查询对象（读请求 DTO）
│   ├── event/                    # 应用事件
│   └── dto/                      # 应用层 DTO
├── service/                      # 应用服务（传统编排方式）
├── eventhandler/                 # 事件处理器（v5 重组）
└── extension/                    # 扩展点
    ├── point/                    # 扩展点定义
    ├── biz/                      # 业务扩展点
    └── impl/                     # 扩展实现
```

## 核心规则

### 1. App 层不放业务逻辑（P0）

```java
// ✅ 正确：App 层只编排
@CommandExecutor
public class OrderCreateCmdExe {
    @Resource
    private OrderRepository orderRepository;
    @Resource
    private ProductGateway productGateway;

    @Override
    public OrderDTO execute(OrderCreateCmd cmd) {
        // 校验库存（调用领域网关）
        InventoryInfo inventory = productGateway.checkInventory(cmd.getProductId(), cmd.getQuantity());
        if (!inventory.isAvailable()) {
            throw new BizException("库存不足");
        }

        // 创建订单（领域逻辑在 Order 实体中）
        Order order = Order.create(cmd.toOrderCreation());

        // 保存订单
        orderRepository.save(order);

        // 返回 DTO
        return OrderAssembler.toDTO(order);
    }
}
```

### 2. App 层不直接操作数据库（P0）

```java
// ❌ 错误：App 层直接操作 Mapper
@CommandExecutor
public class OrderCreateCmdExe {
    @Resource
    private OrderMapper orderMapper;  // ← 禁止！应通过 Repository 接口

    @Override
    public OrderDTO execute(OrderCreateCmd cmd) {
        // ...
        orderMapper.insert(order);    // ← P0 违规
    }
}
```

### 3. CQRS 执行器模式（推荐）

**命令执行器**（写操作）：

```java
@Component
public class CustomerCreateCmdExe implements CommandExecutor<CustomerCreateCmd, CustomerDTO> {
    @Resource
    private CustomerRepository customerRepository;

    @Override
    @Transactional
    public CustomerDTO execute(CustomerCreateCmd cmd) {
        Customer customer = new Customer(cmd.getCustomerName(), cmd.getEmail());
        customerRepository.save(customer);
        return CustomerAssembler.toDTO(customer);
    }
}
```

**查询执行器**（读操作）：

```java
@Component
public class CustomerGetQryExe implements QueryExecutor<CustomerGetQry, CustomerDTO> {
    @Resource
    private CustomerRepository customerRepository;

    @Override
    public CustomerDTO execute(CustomerGetQry qry) {
        return customerRepository.findById(new CustomerId(qry.getId()))
            .map(CustomerAssembler::toDTO)
            .orElseThrow(() -> new BizException("客户不存在"));
    }
}
```

### 4. 应用服务（传统编排）

适用于不需要 CQRS 分离的简单场景：

```java
@Service
public class OrderAppService {
    @Resource
    private OrderRepository orderRepository;

    @Transactional
    public void payOrder(PayOrderCommand command) {
        Order order = orderRepository.findById(new OrderId(command.getOrderId()))
            .orElseThrow(() -> new OrderNotFoundException(command.getOrderId()));
        order.pay();                // 领域逻辑在实体中
        orderRepository.save(order);
    }
}
```

## 应用层最佳实践

- **事务边界**：事务在 App 层，不在 Domain 层
- **命令/查询分离**：写操作走 Command Executor，读操作走 Query Executor
- **参数校验**：格式校验在 Adapter 层，业务校验在 App/Domain 层
- **DTO 转换**：使用 Assembler/Converter，不作为 Domain 对象暴露
