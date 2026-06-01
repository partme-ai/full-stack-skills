# Unified Response Format Specification

## Core Design

Every API response follows the same envelope format (`Result<T>`):

```json
{
  "code": 0,
  "message": "success",
  "data": { /* type-specific payload */ },
  "requestId": "req-abc123",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Response Type Definitions

### Success Response: Single Object

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "orderId": "ORD-2024-001",
    "status": "PAID",
    "totalAmount": "99.00",
    "items": [
      { "itemId": "ITEM-001", "productName": "T-Shirt", "quantity": 2, "price": "49.50" }
    ]
  },
  "requestId": "req-abc123"
}
```

### Success Response: Paginated List

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [
      { "orderId": "ORD-2024-001", "status": "PAID", "totalAmount": "99.00" },
      { "orderId": "ORD-2024-002", "status": "DRAFT", "totalAmount": "150.00" }
    ],
    "total": 100,
    "page": 1,
    "pageSize": 20,
    "totalPages": 5
  },
  "requestId": "req-abc123"
}
```

### Success Response: No Content (204)

```http
HTTP/1.1 204 No Content
Content-Length: 0
```

Used for DELETE operations — no response body.

### Error Response: Business Error

```json
{
  "code": 40001,
  "message": "订单状态不允许支付",
  "detail": "当前状态：CANCELLED，可支付状态：DRAFT",
  "requestId": "req-abc123",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Error Response: Validation Error

```json
{
  "code": 40002,
  "message": "参数校验失败",
  "detail": [
    { "field": "amount", "message": "金额不能为负数" },
    { "field": "customerId", "message": "客户ID不能为空" },
    { "field": "items", "message": "订单项不能为空" }
  ],
  "requestId": "req-abc123"
}
```

### Error Response: Not Found

```json
{
  "code": 40401,
  "message": "订单未找到",
  "detail": "orderId: ORD-2024-999",
  "requestId": "req-abc123"
}
```

### Error Response: Conflict / Concurrent Modification

```json
{
  "code": 40901,
  "message": "数据已被其他操作修改",
  "detail": "预期版本: 3, 当前版本: 5",
  "requestId": "req-abc123"
}
```

### Error Response: System Error (500)

```json
{
  "code": 50000,
  "message": "系统内部错误",
  "requestId": "req-abc123"
}
```

## Error Code System

### Code Range Allocation

| Code Range | Category | HTTP Status | Description |
|:----------:|----------|:-----------:|-------------|
| 0 | Success | 200/201 | Success |
| 40001-40099 | Business Rule Violation | 400 | Domain rule prevented operation |
| 40100-40199 | Authentication | 401 | Missing or invalid credentials |
| 40300-40399 | Authorization | 403 | Insufficient permissions |
| 40401-40499 | Not Found | 404 | Resource not found |
| 40901-40999 | Conflict | 409 | Optimistic lock / duplicate |
| 41201-41299 | Precondition Failed | 412 | Version mismatch |
| 42901-42999 | Rate Limit | 429 | Too many requests |
| 50000-50099 | System Error | 500 | Unexpected internal error |
| 50301-50399 | Service Unavailable | 503 | Downstream service unavailable |

### Code Naming Convention

```
XXYYY
│└── Specific error number (001-999)
└── Category:
    0  = Success
    40 = Client error (4xx)
    41 = Auth (401)
    43 = Forbidden (403)
    44 = Not Found (404)
    49 = Conflict (409)
    42 = Rate limit (429)
    50 = Server error (500)
    53 = Service unavailable (503)
```

## Response Wrapper Implementation

### Java

```java
public class Result<T> {
    private int code;
    private String message;
    private T data;
    private String detail;
    private String requestId;
    private String timestamp;

    // Success
    public static <T> Result<T> success(T data) {
        return new Result<>(0, "success", data, null, null, now());
    }

    // Error with detail
    public static <T> Result<T> error(int code, String message, Object detail) {
        return new Result<>(code, message, null, detail, null, now());
    }

    // System error with requestId
    public static <T> Result<T> systemError(String requestId) {
        return new Result<>(50000, "系统内部错误", null, null, requestId, now());
    }
}
```

### TypeScript

```typescript
interface ApiResponse<T> {
  code: number;
  message: string;
  data?: T;
  detail?: any;
  requestId: string;
  timestamp: string;
}

interface PaginatedData<T> {
  records: T[];
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
}

// Usage
type OrderListResponse = ApiResponse<PaginatedData<OrderSummary>>;
type OrderDetailResponse = ApiResponse<OrderDetail>;
```

## Exception Handling Strategy

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Result<?> handleBusiness(BusinessException e) {
        return Result.error(e.getCode(), e.getMessage(), e.getDetail());
    }

    @ExceptionHandler(ValidationException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Result<?> handleValidation(ValidationException e) {
        return Result.error(40002, "参数校验失败", e.getErrors());
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Result<?> handleNotFound(ResourceNotFoundException e) {
        return Result.error(40401, e.getMessage(), e.getResourceId());
    }

    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public Result<?> handleSystem(Exception e, HttpServletRequest request) {
        log.error("System error", e);
        return Result.systemError(request.getAttribute("requestId").toString());
    }
}
```

## Guidelines

1. **Always wrap responses**: All API responses use `Result<T>` envelope. Only health checks and file downloads are exempt.
2. **Consistent error codes**: Same error across endpoints returns same code. No code reuse across different error types.
3. **No stack traces**: Error responses never include stack traces. Use `requestId` for server-side log correlation.
4. **Include requestId**: Every response includes a requestId for debugging. Attach to logs for traceability.
5. **ISO 8601 timestamps**: All datetime values use ISO 8601 format with timezone.
6. **Avoid null in data**: If no data, omit the `data` field entirely, or return an empty object `{}`.
