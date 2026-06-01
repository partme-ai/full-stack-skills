# API 幂等设计

## 为什么需要幂等

在分布式系统中，网络超时、客户端重试、MQ 重复消费都会导致同一请求被多次执行。幂等设计确保重复请求不产生副作用。

### 哪些操作需要幂等

| 方法 | 天然幂等？ | 说明 |
|------|:----------:|------|
| GET | ✅ | 不修改状态 |
| PUT | ✅ | 全量替换，多次执行结果相同 |
| DELETE | ✅ | 删除已删除的资源返回相同结果 |
| POST | ❌ | 每次执行创建新资源，必须幂等处理 |

## 四种幂等实现方案

### 1. 幂等键（Idempotency-Key）— 最推荐

客户端在请求头中传入唯一键，服务端缓存结果去重。

```yaml
POST /api/v1/orders
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
```

**流程**：

```
请求到达 → 查缓存 (key → result)
  ├── 命中 → 直接返回缓存结果（200 OK）
  └── 未命中 → 执行业务逻辑 → 存储 (key, result) → 返回结果
```

**注意事项**：
- 缓存 TTL 必须超过最大重试窗口（推荐 24h）
- 使用 Redis + TTL 实现
- 幂等键空间应足够大（UUID v4）
- 幂等键的响应结果不可变更：第一次成功 → 永远返回成功；第一次失败 → 后续重试继续执行（业务有状态时需要结合状态机）

```java
public class IdempotencyFilter implements Filter {
    private final RedisTemplate<String, String> redis;

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) {
        HttpServletRequest req = (HttpServletRequest) request;
        String idempotencyKey = req.getHeader("Idempotency-Key");

        if (idempotencyKey != null && "POST".equalsIgnoreCase(req.getMethod())) {
            String cached = redis.opsForValue().get("idempotent:" + idempotencyKey);
            if (cached != null) {
                // 返回缓存结果
                response.getWriter().write(cached);
                return;
            }
        }
        chain.doFilter(request, response);
    }
}
```

### 2. 业务唯一索引 — 简单可靠

利用数据库唯一约束防止重复：

```sql
-- 订单号唯一约束
ALTER TABLE orders ADD UNIQUE INDEX uk_order_no (order_no);
```

```java
try {
    orderRepository.save(order);
} catch (DuplicateKeyException e) {
    // 重复订单号 → 返回已创建的订单信息
    return orderRepository.findByOrderNo(order.getOrderNo());
}
```

### 3. 状态机 — 防重入

业务状态有明确流转路径，已处理状态不可重复触发：

```java
public class Order {
    private OrderStatus status;

    public void confirm() {
        if (this.status != OrderStatus.DRAFT) {
            // DRAFT → CONFIRMED 只允许一次
            throw new BusinessException(40001, "当前状态不允许确认",
                "当前：" + this.status + "，需要：DRAFT");
        }
        this.status = OrderStatus.CONFIRMED;
    }

    public void pay() {
        if (this.status != OrderStatus.CONFIRMED) {
            throw new BusinessException(40001, "当前状态不允许支付");
        }
        this.status = OrderStatus.PAID;
    }
}
```

### 4. 业务幂等（乐观锁）— 无额外存储

利用数据库条件更新：

```sql
-- 扣减库存：stock >= 1 确保不会超卖
UPDATE product SET stock = stock - 1 WHERE id = ? AND stock >= 1;

-- 乐观锁版本号
UPDATE orders SET status = 'PAID', version = version + 1
WHERE id = ? AND version = ?;
```

## 幂等策略选型矩阵

| 场景 | 推荐方案 |
|------|---------|
| 创建订单（POST） | 幂等键 + 订单号唯一索引 |
| 支付回调 | 业务唯一索引（支付单号） |
| 状态变更（PUT） | 状态机 + 乐观锁 |
| 库存扣减 | 条件更新（stock >= n） |
| MQ 消息消费 | 消息 ID 幂等键 + 去重表 |

## 幂等键最佳实践

1. **幂等键由客户端生成**：UUID v4，确保唯一性
2. **幂等键作用域**：按 (key, endpoint) 区分，不同端点可用相同 key
3. **结果缓存不可变**：第一次成功→永远返回成功结果
4. **TTL 设计**：至少 24h，最长 7 天（取决于业务重试窗口）
5. **幂等键大小**：建议 64 字节以内，作为 Redis key 需控制长度

## 幂等键在 OpenAPI 中的定义

```yaml
paths:
  /orders:
    post:
      parameters:
        - name: Idempotency-Key
          in: header
          required: false
          schema:
            type: string
            format: uuid
          description: 客户端幂等键，防止重复创建
      responses:
        '201':
          description: 首次创建
        '200':
          description: 幂等返回（重复请求使用相同幂等键）
          headers:
            Idempotent-Replayed:
              schema:
                type: boolean
              description: 标识该响应是重放结果
```
