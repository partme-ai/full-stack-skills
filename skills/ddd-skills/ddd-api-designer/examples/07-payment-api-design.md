# 支付服务完整 API 设计案例

> 支付限界上下文（Payment BC）的 REST API 设计，展示幂等、状态机、异步回调等典型场景。

## 领域模型

```
Payment (Aggregate Root)
├── PaymentId (ValueObject)
├── OrderId (ValueObject) — 引用订单聚合
├── PaymentStatus: UNPAID → PROCESSING → SUCCESS → REFUNDING → REFUNDED
│                                          ↘ FAILED
├── Money amount (ValueObject)
├── PaymentMethod (ValueObject): WECHAT_PAY / ALIPAY / CARD
├── PaymentChannel (Entity)：通道请求记录
│   ├── channelType
│   ├── channelOrderNo
│   └── channelStatus
└── List<PaymentEvent> (DomainEvent)
```

## 1. CQRS 端点设计

### 命令端点（写）

```
POST   /api/v1/payments                     → 发起支付
POST   /api/v1/payments/{paymentId}/refund  → 发起退款
PUT    /api/v1/payments/{paymentId}/cancel   → 取消支付

# 回调端点（第三方支付异步通知）
POST   /api/v1/payments/callback/wechat      → 微信支付回调
POST   /api/v1/payments/callback/alipay      → 支付宝回调
```

### 查询端点（读）

```
GET    /api/v1/payments/{paymentId}          → 支付详情
GET    /api/v1/payments/order/{orderId}      → 订单支付记录列表
```

## 2. 幂等设计

支付 API 的幂等设计是核心：**防止重复扣款**。

### 幂等键应用

```yaml
# 发起支付 — 幂等键防止重复支付请求
POST /api/v1/payments
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
```

```java
@Service
public class PaymentService {
    private final PaymentRepository paymentRepository;
    private final IdempotencyService idempotencyService;

    public PaymentResult initiatePayment(CreatePaymentCommand command, String idempotencyKey) {
        // 1. 幂等检查
        PaymentResult cached = idempotencyService.getCachedResult(idempotencyKey);
        if (cached != null) return cached;

        // 2. 业务幂等：同一订单不能重复发起支付
        paymentRepository.findByOrderId(command.orderId())
            .filter(p -> p.getStatus() != PaymentStatus.UNPAID)
            .ifPresent(p -> { throw new BusinessException(40001, "该订单已发起支付"); });

        // 3. 执行支付
        Payment payment = Payment.create(command);
        PaymentResult result = paymentRepository.save(payment);

        // 4. 缓存幂等结果
        idempotencyService.cacheResult(idempotencyKey, result);
        return result;
    }
}
```

### 退款幂等

```java
public class Payment {
    public RefundRecord refund(Money amount, String reason) {
        // 状态机幂等：已退款状态不可重复退款
        if (this.status == PaymentStatus.REFUNDED) {
            throw new BusinessException(40001, "该支付已全额退款");
        }
        // 部分退款：计算可退余额
        Money refundable = this.amount.subtract(this.totalRefunded());
        if (amount.greaterThan(refundable)) {
            throw new BusinessException(40001, "可退余额不足",
                "可退: " + refundable + "，申请: " + amount);
        }
        this.totalRefundedAmount = this.totalRefundedAmount.add(amount);
        if (this.totalRefundedAmount.equals(this.amount)) {
            this.status = PaymentStatus.REFUNDED;
        } else {
            this.status = PaymentStatus.REFUNDING;
        }
        addDomainEvent(new PaymentRefundedEvent(this.id, amount));
        return new RefundRecord(RefundId.generate(), amount, reason, LocalDateTime.now());
    }
}
```

## 3. 异步回调处理

第三方支付异步通知（Webhook）的处理规范。

### 回调端点设计

```java
@RestController
public class PaymentCallbackController {
    private final PaymentCallbackHandler callbackHandler;

    // 微信支付回调 — 统一入口
    @PostMapping("/api/v1/payments/callback/wechat")
    public ResponseEntity<String> handleWechatCallback(@RequestBody String xmlBody,
                                                        @RequestHeader Map<String, String> headers) {
        // 1. 验签
        if (!WechatSignature.verify(xmlBody, headers)) {
            return ResponseEntity.status(401).body("signature verification failed");
        }

        // 2. 幂等处理（防止重复回调）
        WechatNotify notify = WechatNotify.parse(xmlBody);
        return callbackHandler.handleCallback("WECHAT", notify.getOutTradeNo(), () -> {
            Payment payment = paymentRepository.findByOrderNo(notify.getOutTradeNo())
                .orElseThrow(() -> new ResourceNotFoundException("Payment not found"));

            if (notify.isSuccess()) {
                payment.markSuccess(notify.getTransactionId(), notify.getPaidAt());
            } else {
                payment.markFailed(notify.getErrorCode());
            }
            paymentRepository.save(payment);
        });
    }

    // 返回 "SUCCESS" 通知微信停止回调
    // 返回其他 → 微信会重试（最多 3 天）
}
```

### 回调幂等 Handler

```java
@Service
public class PaymentCallbackHandler {

    public ResponseEntity<String> handleCallback(String channel, String outTradeNo,
                                                  Runnable businessLogic) {
        String lockKey = "callback:" + channel + ":" + outTradeNo;

        // 分布式锁防并发
        if (!redisLock.tryLock(lockKey, 30, TimeUnit.SECONDS)) {
            return ResponseEntity.ok("SUCCESS");  // 另一个线程在处理
        }

        try {
            // 幂等：已处理过的回调不再执行
            if (redis.hasKey("callback:processed:" + outTradeNo)) {
                return ResponseEntity.ok("SUCCESS");
            }
            businessLogic.run();
            redis.set("callback:processed:" + outTradeNo, "1", 7, TimeUnit.DAYS);
            return ResponseEntity.ok("SUCCESS");

        } catch (Exception e) {
            log.error("Callback processing failed", e);
            return ResponseEntity.status(500).body("retry");
        } finally {
            redisLock.unlock(lockKey);
        }
    }
}
```

## 4. 数据对象转换链

```
PaymentPO ↔ Payment (DO) ↔ PaymentDTO ↔ PaymentVO
```

### DO — 充血模型

```java
public class Payment extends AggregateRoot<PaymentId> {
    private PaymentId id;
    private OrderId orderId;
    private PaymentStatus status;
    private Money amount;
    private PaymentMethod method;
    private String channelOrderNo;    // 第三方支付单号
    private Money totalRefundedAmount;

    // 创建支付
    public static Payment create(OrderId orderId, Money amount, PaymentMethod method) {
        Payment payment = new Payment(PaymentId.generate(), orderId, amount, method);
        payment.status = PaymentStatus.UNPAID;
        payment.addDomainEvent(new PaymentInitiatedEvent(payment.id, orderId, amount));
        return payment;
    }

    // 支付成功回调
    public void markSuccess(String channelOrderNo, LocalDateTime paidAt) {
        if (this.status != PaymentStatus.PROCESSING) {
            // 幂等：已成功的回调直接忽略
            if (this.status == PaymentStatus.SUCCESS) return;
            throw new BusinessException(40001, "当前状态不允许标记成功",
                "当前：" + this.status);
        }
        this.status = PaymentStatus.SUCCESS;
        this.channelOrderNo = channelOrderNo;
        addDomainEvent(new PaymentSuccessEvent(this.id, this.orderId, this.amount, paidAt));
    }

    // 退款
    public void refund(Money amount, String reason) {
        if (this.status != PaymentStatus.SUCCESS) {
            throw new BusinessException(40001, "只有已支付的订单才能退款");
        }
        Money refundable = this.amount.subtract(this.totalRefundedAmount);
        if (amount.greaterThan(refundable)) {
            throw new BusinessException(40001, "可退余额不足");
        }
        this.totalRefundedAmount = this.totalRefundedAmount.add(amount);
        this.status = amount.equals(this.amount) ? PaymentStatus.REFUNDED : PaymentStatus.REFUNDING;
        addDomainEvent(new PaymentRefundedEvent(this.id, this.orderId, amount));
    }
}
```

## 5. 统一响应

```json
// 发起支付成功
POST /api/v1/payments → 201
{
  "code": 0,
  "message": "success",
  "data": {
    "paymentId": "PAY-2024-001",
    "orderId": "ORD-2024-001",
    "amount": "99.00",
    "method": "WECHAT_PAY",
    "status": "PROCESSING",
    "payUrl": "weixin://pay/...",
    "expiresIn": 300
  }
}

// 微信回调处理成功
POST /api/v1/payments/callback/wechat → 200
HTTP body: "SUCCESS"

// 退款成功
POST /api/v1/payments/PAY-2024-001/refund → 200
{
  "code": 0,
  "message": "success",
  "data": {
    "refundId": "REF-2024-001",
    "amount": "99.00",
    "status": "REFUNDED",
    "refundedAt": "2024-01-16T11:00:00Z"
  }
}
```

## 6. 安全设计

| 端点 | 认证 | 限流 | 幂等 | 特殊 |
|------|------|------|------|------|
| POST /payments | JWT + BC 授权 | 30/min/user | ✅ Idempotency-Key | 资源所有权检查 |
| POST /payments/{id}/refund | JWT + OPERATOR 角色 | 10/min/user | ✅ 状态机 + 业务幂等 | 退款金额校验 |
| POST /callback/* | 签名验证（无 JWT） | 100/min/IP | ✅ 去重表 + 回调幂等 | 白名单 IP |
| GET /payments/{id} | JWT | 200/min/user | 天然幂等 | — |
