# COLA v5 适配层详解

## 适配层目录结构

```
{project}-adapter/
├── web/                           # Web 适配器
│   ├── controller/                # REST 控制器
│   ├── api/                       # API 适配器（v5 强调）
│   ├── dto/                       # 请求/响应 DTO
│   │   ├── request/
│   │   ├── response/
│   │   └── converter/             # DTO 转换器
│   ├── validator/                 # 请求校验器
│   └── advice/                    # 全局异常处理
├── rpc/                           # RPC 适配器
│   ├── provider/                  # RPC 服务提供者
│   ├── consumer/                  # RPC 服务消费者
│   ├── facade/                    # RPC 门面（v5 新概念）
│   └── dto/                       # RPC DTO
├── job/                           # 定时任务
│   ├── scheduler/                 # 调度器
│   └── task/                      # 具体任务
├── message/                       # 消息适配器
│   ├── consumer/                  # 消息消费者
│   ├── producer/                  # 消息生产者
│   └── listener/                  # 事件监听器
├── graphql/                       # GraphQL 适配器（v5 增强）
│   ├── resolver/
│   └── dto/
└── mobile/                        # 移动端适配器
```

## 核心规则

### 1. Adapter 层无业务逻辑（P0）

```java
// ✅ 正确：Controller 只做协议转换
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    @Resource
    private OrderCreateCmdExe orderCreateCmdExe;

    @PostMapping
    public Response<OrderDTO> create(@Valid @RequestBody OrderCreateRequest request) {
        OrderCreateCmd cmd = request.toCommand();    // 协议 → 命令
        OrderDTO dto = orderCreateCmdExe.execute(cmd); // 委托给 executor
        return Response.success(dto);
    }
}
```

### 2. 全局异常处理

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(BizException.class)
    public Response<Void> handleBizException(BizException e) {
        return Response.fail(e.getCode(), e.getMessage());
    }

    @ExceptionHandler(ValidationException.class)
    public Response<Void> handleValidation(ValidationException e) {
        return Response.fail(400, e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public Response<Void> handleUnknown(Exception e) {
        log.error("Unexpected error", e);
        return Response.fail(500, "系统繁忙，请稍后重试");
    }
}
```

### 3. DTO 转换

```java
// Adapter 层 DTO，与 Domain 对象分离
public class OrderCreateRequest {
    @NotBlank
    private String productId;
    @Min(1)
    private Integer quantity;
    @NotNull
    private BigDecimal unitPrice;

    // 转换到 Command 对象（App 层）
    public OrderCreateCmd toCommand() {
        OrderCreateCmd cmd = new OrderCreateCmd();
        cmd.setProductId(this.productId);
        cmd.setQuantity(this.quantity);
        cmd.setUnitPrice(this.unitPrice);
        return cmd;
    }
}
```

### 4. RPC 适配器示例

```java
// RPC 提供者
@DubboService
public class CustomerRpcProviderImpl implements CustomerRpcProvider {
    @Resource
    private CustomerCreateCmdExe customerCreateCmdExe;

    @Override
    public CustomerRpcResponse createCustomer(CustomerRpcRequest request) {
        CustomerCreateCmd cmd = request.toCommand();
        CustomerDTO dto = customerCreateCmdExe.execute(cmd);
        return CustomerRpcResponse.from(dto);
    }
}
```

## 适配层最佳实践

- **Controller 职责**：只做 HTTP 协议转换，不放任何业务判断
- **DTO 独立**：Adapter 层 DTO 与应用层 DTO 分离，不混用
- **参数校验**：使用 `@Valid` + JSR-303 做格式校验
- **统一响应**：统一使用 `Response<T>` 包装返回
- **版本管理**：URL 路径版本 `/api/v1/` → `/api/v2/`
