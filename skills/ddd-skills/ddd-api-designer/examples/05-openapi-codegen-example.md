# OpenAPI 代码生成案例

> 展示 Spec-first 策略：从 OpenAPI 规范生成服务端骨架和客户端 SDK。

## 策略选择

| 策略 | 适用 | 工作流 |
|------|------|--------|
| **Code-first** | 内部服务、快速迭代 | 注解 → 运行时导出 Spec → 生成客户端 |
| **Spec-first** | 公共 API、团队协作 | 先写 YAML → 生成服务端骨架 → 补齐业务逻辑 |
| **Hybrid** | 企业级、多消费者 | 注解 + 规范审查 → 导出 → 生成 SDK |

**推荐**：内部 DDD 服务用 Code-first（SpringDoc），公共 API 用 Spec-first（openapi-generator）。

## 场景：支付服务 API 规范（Spec-first）

### 1. 编写 OpenAPI 规范

```yaml
# payment-api-v1.yaml
openapi: 3.0.3
info:
  title: Payment Service API
  version: 1.0.0
  description: 支付服务 API — 支付发起、回调、退款
servers:
  - url: https://api.example.com/api/v1

paths:
  /payments:
    post:
      operationId: initiatePayment
      tags: [Payment Commands]
      parameters:
        - name: Idempotency-Key
          in: header
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InitiatePaymentRequest'
      responses:
        '201':
          description: 支付发起成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentCreatedResponse'
        '400':
          $ref: '#/components/responses/BusinessError'
      x-springdoc-default: "40001"

  /payments/{paymentId}:
    get:
      operationId: getPayment
      tags: [Payment Queries]
      parameters:
        - name: paymentId
          in: path
          required: true
          schema:
            type: string
            pattern: '^PAY-\d{4}-\d{3,6}$'
      responses:
        '200':
          description: 支付详情
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentDetailResponse'

components:
  schemas:
    InitiatePaymentRequest:
      type: object
      required: [orderId, amount, currency, method]
      properties:
        orderId:
          type: string
          example: ORD-2024-001
        amount:
          type: string
          example: "99.00"
        currency:
          type: string
          enum: [CNY, USD]
        method:
          type: string
          enum: [WECHAT_PAY, ALIPAY, CARD]

    PaymentCreatedData:
      type: object
      properties:
        paymentId:
          type: string
        status:
          type: string
          enum: [PROCESSING]
        payUrl:
          type: string
        expiresIn:
          type: integer

    PaymentCreatedResponse:
      type: object
      properties:
        code:
          type: integer
          example: 0
        message:
          type: string
        data:
          $ref: '#/components/schemas/PaymentCreatedData'

    PaymentDetailData:
      type: object
      properties:
        paymentId:
          type: string
        orderId:
          type: string
        status:
          type: string
        amount:
          type: string
        method:
          type: string
        channelOrderNo:
          type: string
        createdAt:
          type: string
          format: date-time

    PaymentDetailResponse:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        data:
          $ref: '#/components/schemas/PaymentDetailData'

    ApiError:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        detail:
          type: string
        requestId:
          type: string

  responses:
    BusinessError:
      description: Business error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
```

### 2. 生成服务端骨架

```bash
# 使用 openapi-generator 生成 Java Spring 服务端
openapi-generator generate \
  -i payment-api-v1.yaml \
  -g spring \
  -o payment-service \
  --api-package com.example.payment.adapter.inbound.web \
  --model-package com.example.payment.adapter.inbound.dto \
  --additional-properties=interfaceOnly=true

# 生成目录结构
payment-service/
├── src/main/java/com/example/payment/adapter/inbound/
│   ├── web/
│   │   ├── PaymentApi.java                     # 生成的接口
│   │   └── PaymentApiController.java           # 生成的骨架
│   └── dto/
│       ├── InitiatePaymentRequest.java         # 生成的请求 DTO
│       ├── PaymentCreatedResponse.java         # 生成的响应 DTO
│       └── ApiError.java                       # 生成的错误 DTO
```

### 3. 实现业务逻辑

```java
@RestController
public class PaymentController implements PaymentApi {

    private final PaymentApplicationService paymentService;

    @Override
    public ResponseEntity<PaymentCreatedResponse> initiatePayment(
            String idempotencyKey,
            InitiatePaymentRequest request) {

        // 1. 请求 DTO → 命令对象
        InitiatePaymentCommand command = new InitiatePaymentCommand(
            OrderId.of(request.getOrderId()),
            Money.of(request.getAmount(), Currency.valueOf(request.getCurrency())),
            PaymentMethod.valueOf(request.getMethod())
        );

        // 2. 调用应用服务
        PaymentResult result = paymentService.initiate(command, idempotencyKey);

        // 3. 领域结果 → 响应 DTO
        PaymentCreatedData data = new PaymentCreatedData();
        data.setPaymentId(result.getPaymentId());
        data.setStatus("PROCESSING");
        data.setPayUrl(result.getPayUrl());
        data.setExpiresIn(300);

        PaymentCreatedResponse response = new PaymentCreatedResponse();
        response.setCode(0);
        response.setMessage("success");
        response.setData(data);

        return ResponseEntity.status(201).body(response);
    }
}
```

### 4. 生成客户端 SDK

```bash
# 生成 TypeScript 客户端
openapi-generator generate \
  -i payment-api-v1.yaml \
  -g typescript-axios \
  -o payment-client-ts

# 生成 Java 客户端
openapi-generator generate \
  -i payment-api-v1.yaml \
  -g java \
  -o payment-client-java
```

### 5. 客户端使用

```typescript
// TypeScript 客户端
import { PaymentApi } from './payment-client-ts';

const api = new PaymentApi();

// 发起支付
const response = await api.initiatePayment(
  { orderId: "ORD-2024-001", amount: "99.00", currency: "CNY", method: "WECHAT_PAY" },
  { headers: { "Idempotency-Key": uuidv4() } }
);

console.log(response.data.data.payUrl);  // weixin://pay/...
```

## Code-first 方案（SpringDoc 注解）

```java
@RestController
@RequestMapping("/api/v1/payments")
@Tag(name = "Payment Commands", description = "支付命令端点")
public class PaymentController {

    @Operation(summary = "发起支付", operationId = "initiatePayment")
    @ApiResponses({
        @ApiResponse(responseCode = "201", description = "支付发起成功"),
        @ApiResponse(responseCode = "400", description = "业务错误",
            content = @Content(schema = @Schema(implementation = ApiError.class)))
    })
    @PostMapping
    public ResponseEntity<PaymentCreatedResponse> initiatePayment(
            @RequestHeader("Idempotency-Key") @Parameter(description = "幂等键")
            String idempotencyKey,
            @RequestBody @Valid InitiatePaymentRequest request) {
        // ...
    }
}
```

导出 Spec：

```yaml
# application.yml
springdoc:
  api-docs:
    path: /api-docs
  swagger-ui:
    path: /swagger-ui.html
  packages-to-scan: com.example.payment.adapter.inbound.web
```

```bash
# 运行期导出 OpenAPI 规范
curl http://localhost:8080/api-docs > payment-api-spec.yaml
```

## OpenAPI 代码生成最佳实践

1. **每个 BC 一个 Spec 文件**：Order BC 和 Payment BC 的 Spec 独立管理
2. **用 operationId 对应方法名**：便于代码生成的方法映射
3. **接口优先**（interfaceOnly=true）：生成接口，不生成实现，避免覆盖业务代码
4. **DTO 和 VO 不走代码生成**：DDD 项目中的 DTO/VO 应手工设计，annotations 不适合复杂 DTO 结构
5. **Spec 纳入版本控制**：每次 API 变更必须更新 Spec 文件
6. **Spec diff 作为 Code Review 一部分**：审查 Spec 变更后再合入
7. **客户端 SDK 按需生成**：不要将生成的 SDK 提交到仓库，通过 CI 按需构建
