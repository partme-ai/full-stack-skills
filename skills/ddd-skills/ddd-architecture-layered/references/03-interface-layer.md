# Interface Layer — 用户接口层

> 用户接口层是系统的边界，负责与外部世界交互。它转换协议、校验输入、处理异常，但**不包含业务逻辑**。

## 职责

- 接收外部请求（HTTP/gRPC/MQ/CLI）
- 协议转换（JSON ↔ Java Object）
- 请求参数校验（格式验证，非业务验证）
- 调用 Application Service
- 统一响应格式和异常处理
- 认证和授权（AuthN/AuthZ）

## 包含的子模块

```
interface/
├── controller/                  # REST API 控制器
│   ├── OrderController.java
│   └── CustomerController.java
├── dto/                         # 接口层 DTO
│   ├── request/                 # 请求 DTO
│   │   ├── CreateOrderRequest.java
│   │   └── PayOrderRequest.java
│   └── response/                # 响应 DTO
│       ├── OrderResponse.java
│       └── ApiResponse.java
├── converter/                   # DTO ↔ Command/Query 转换
│   └── OrderConverter.java
├── advice/                      # 全局异常处理
│   ├── GlobalExceptionHandler.java
│   ├── ErrorResponse.java
│   └── ErrorCode.java
└── filter/                      # 过滤器
    ├── AuthFilter.java
    ├── LoggingFilter.java
    └── CorsFilter.java
```

## 关键规则

1. **不含业务逻辑** — Controller 中不能有 if/else 业务判断
2. **纯协议转换** — Request → Command → AppService → Response
3. **参校验放在 DTO 层** — 用 `@Valid` + JSR-303 注解
4. **异常统一处理** — `@ControllerAdvice` 捕获异常

## 控制器示例

```java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final OrderApplicationService orderAppService;

    @PostMapping
    public Result<OrderResponse> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {
        // 1. DTO → Command 转换（接口层职责）
        CreateOrderCommand command = OrderConverter.toCommand(request);
        // 2. 调用应用服务
        OrderDTO result = orderAppService.createOrder(command);
        // 3. DO → Response 转换
        return Result.success(OrderConverter.toResponse(result));
    }

    @PostMapping("/{id}/pay")
    public Result<Void> payOrder(@PathVariable String id) {
        PayOrderCommand command = new PayOrderCommand(id);
        orderAppService.payOrder(command);
        return Result.success();
    }

    @GetMapping("/{id}")
    public Result<OrderResponse> getOrder(@PathVariable String id) {
        GetOrderQuery query = new GetOrderQuery(id);
        OrderDTO result = orderAppService.getOrder(query);
        return Result.success(OrderConverter.toResponse(result));
    }
}
```

## DTO 设计原则

```
Request DTO:
  └── 对应前端输入，用 @NotBlank/@NotNull/@Min 等注解校验格式
  └── 不含业务规则校验（如"订单总金额不能超过 50000"）

Response DTO:
  └── 面向展示，聚合必要的数据
  └── 不同场景可返回不同字段（详情 vs 列表 vs 摘要）

转换原则：
  └── 不转换业务逻辑，只做字段映射
  └── 一个接口一个 Request/Response，不要复用
```

## 请求 DTO 示例

```java
@Data
public class CreateOrderRequest {
    @NotBlank(message = "客户ID不能为空")
    private String customerId;

    @NotEmpty(message = "订单项不能为空")
    @Valid
    private List<OrderItemRequest> items;
}

@Data
public class OrderItemRequest {
    @NotBlank(message = "商品ID不能为空")
    private String productId;

    @NotNull(message = "单价不能为空")
    @DecimalMin(value = "0.01", message = "单价必须大于0")
    private BigDecimal price;

    @Min(value = 1, message = "数量至少为1")
    private int quantity;
}
```

## 统一响应格式

```json
// 成功响应
{
  "code": 0,
  "message": "success",
  "data": { "orderId": "ORD-2024-001", "status": "PAID" }
}

// 分页响应
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [...],
    "total": 100,
    "page": 1,
    "pageSize": 20
  }
}

// 错误响应
{
  "code": 40001,
  "message": "订单状态不允许支付",
  "detail": "当前状态：CANCELLED，可支付状态：DRAFT"
}
```

## 全局异常处理

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(DomainException.class)
    public Result<Void> handleDomain(DomainException e) {
        return Result.error(40001, e.getMessage());
    }

    @ExceptionHandler(ApplicationException.class)
    public Result<Void> handleApplication(ApplicationException e) {
        return Result.error(50001, e.getMessage());
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public Result<Void> handleValidation(MethodArgumentNotValidException e) {
        String msg = e.getBindingResult().getFieldErrors().stream()
            .map(FieldError::getDefaultMessage)
            .collect(Collectors.joining("; "));
        return Result.error(40000, msg);
    }
}
```

## 检查清单

- [ ] Controller 中没有 if/else 业务判断
- [ ] 参数校验使用 `@Valid` + JSR-303
- [ ] 异常统一由 `@ControllerAdvice` 处理
- [ ] 使用统一的响应格式（Result/ApiResponse）
- [ ] DTO 不包含业务注解
- [ ] DTO ↔ Command 转换在接口层完成
- [ ] 接口方法名体现业务操作（非 REST 资源口味）
