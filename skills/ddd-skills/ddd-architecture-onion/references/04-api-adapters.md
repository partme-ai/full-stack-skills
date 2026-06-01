# 04 — API Layer: Adapters & Controllers

> API 层（Adapter Layer）是系统对外暴露的边界，负责协议转换、数据校验、异常处理。

## 职责

- REST Controller：接收 HTTP 请求，调用 Application 服务
- DTO：请求/响应数据结构定义
- Assembler：DTO ↔ Domain 数据转换
- Middleware：拦截器、过滤器、全局异常处理
- Swagger：API 文档

## 代码模板

### REST Controller

```java
// api/controller/OrderController.java
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {
    private final OrderApplicationService orderAppService;

    public OrderController(OrderApplicationService orderAppService) {
        this.orderAppService = orderAppService;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<OrderResponse>> createOrder(
            @Valid @RequestBody CreateOrderRequest request) {
        CreateOrderCommand command = CreateOrderRequestAssembler.toCommand(request);
        OrderDTO orderDTO = orderAppService.createOrder(command);
        OrderResponse response = OrderResponseAssembler.toResponse(orderDTO);
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(ApiResponse.success(response));
    }

    @PostMapping("/{orderId}/pay")
    public ResponseEntity<ApiResponse<Void>> payOrder(
            @PathVariable String orderId) {
        orderAppService.payOrder(new PayOrderCommand(orderId));
        return ResponseEntity.ok(ApiResponse.success(null));
    }

    @GetMapping("/{orderId}")
    public ResponseEntity<ApiResponse<OrderResponse>> getOrder(
            @PathVariable String orderId) {
        OrderDTO orderDTO = orderAppService.getOrder(orderId);
        OrderResponse response = OrderResponseAssembler.toResponse(orderDTO);
        return ResponseEntity.ok(ApiResponse.success(response));
    }

    @PostMapping("/{orderId}/cancel")
    public ResponseEntity<ApiResponse<Void>> cancelOrder(
            @PathVariable String orderId) {
        orderAppService.cancelOrder(new CancelOrderCommand(orderId));
        return ResponseEntity.ok(ApiResponse.success(null));
    }
}
```

### Request / Response DTO

```java
// api/dto/request/CreateOrderRequest.java
@Data
public class CreateOrderRequest {
    @NotBlank(message = "客户ID不能为空")
    private String customerId;

    @NotEmpty(message = "订单项不能为空")
    @Valid
    private List<Item> items;

    @Data
    public static class Item {
        @NotBlank
        private String productId;

        @NotNull
        @Positive
        private BigDecimal unitPrice;

        @Min(1)
        private int quantity;
    }
}

// api/dto/response/OrderResponse.java
@Data
public class OrderResponse {
    private String orderId;
    private String customerId;
    private String status;
    private List<OrderItemResponse> items;
    private BigDecimal totalAmount;
    private LocalDateTime createdAt;

    @Data
    public static class OrderItemResponse {
        private String productId;
        private BigDecimal unitPrice;
        private int quantity;
        private BigDecimal subtotal;
    }
}
```

### Assembler（DTO ↔ Command）

```java
// api/assembler/CreateOrderRequestAssembler.java
public class CreateOrderRequestAssembler {
    public static CreateOrderCommand toCommand(CreateOrderRequest request) {
        CreateOrderCommand command = new CreateOrderCommand();
        command.setCustomerId(request.getCustomerId());
        command.setItems(request.getItems().stream()
            .map(item -> {
                CreateOrderCommand.Item cmdItem = new CreateOrderCommand.Item();
                cmdItem.setProductId(item.getProductId());
                cmdItem.setUnitPrice(item.getUnitPrice());
                cmdItem.setQuantity(item.getQuantity());
                return cmdItem;
            })
            .collect(Collectors.toList())
        );
        return command;
    }
}

// api/assembler/OrderResponseAssembler.java
public class OrderResponseAssembler {
    public static OrderResponse toResponse(OrderDTO dto) {
        OrderResponse response = new OrderResponse();
        response.setOrderId(dto.getOrderId());
        response.setCustomerId(dto.getCustomerId());
        response.setStatus(dto.getStatus());
        response.setTotalAmount(dto.getTotalAmount());
        response.setCreatedAt(dto.getCreatedAt());
        response.setItems(dto.getItems().stream()
            .map(itemDto -> {
                OrderResponse.OrderItemResponse itemResp = new OrderResponse.OrderItemResponse();
                itemResp.setProductId(itemDto.getProductId());
                itemResp.setUnitPrice(itemDto.getUnitPrice());
                itemResp.setQuantity(itemDto.getQuantity());
                itemResp.setSubtotal(itemDto.getSubtotal());
                return itemResp;
            })
            .collect(Collectors.toList())
        );
        return response;
    }
}
```

### 统一响应格式

```java
// api/dto/response/ApiResponse.java
@Data
@AllArgsConstructor
public class ApiResponse<T> {
    private int code;
    private String message;
    private T data;

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(200, "success", data);
    }

    public static <T> ApiResponse<T> error(int code, String message) {
        return new ApiResponse<>(code, message, null);
    }
}
```

### 全局异常处理

```java
// api/middleware/GlobalExceptionHandler.java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(DomainException.class)
    public ResponseEntity<ApiResponse<Void>> handleDomainException(DomainException ex) {
        return ResponseEntity.badRequest()
            .body(ApiResponse.error(400, ex.getMessage()));
    }

    @ExceptionHandler(OrderNotFoundException.class)
    public ResponseEntity<ApiResponse<Void>> handleNotFound(OrderNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(ApiResponse.error(404, ex.getMessage()));
    }

    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<ApiResponse<Void>> handleValidation(
            ConstraintViolationException ex) {
        String msg = ex.getConstraintViolations().stream()
            .map(v -> v.getPropertyPath() + ": " + v.getMessage())
            .collect(Collectors.joining(", "));
        return ResponseEntity.badRequest()
            .body(ApiResponse.error(400, msg));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Void>> handleGeneral(Exception ex) {
        log.error("Unexpected error", ex);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(ApiResponse.error(500, "内部服务异常"));
    }
}
```

## 规范检查清单

- [ ] Controller 不含业务逻辑（无 if/else 业务判断）
- [ ] 输入校验在 DTO 上使用 `@Valid` + JSR-303
- [ ] 响应格式统一（ApiResponse 包装）
- [ ] Assembler 完成 DTO ↔ Domain 转换
- [ ] 全局异常处理覆盖所有场景
- [ ] Swagger/OpenAPI 文档生成
