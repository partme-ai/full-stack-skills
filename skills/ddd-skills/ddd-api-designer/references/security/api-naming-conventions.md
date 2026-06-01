# API 端点与数据对象命名规范

## 命令 API（写操作）

```
POST   /api/v1/orders                 # 创建订单
PUT    /api/v1/orders/{id}/confirm     # 确认订单
DELETE /api/v1/orders/{id}             # 取消订单

命名规则：
- 使用名词复数（/orders 而非 /order）
- 写操作用动词后缀（confirm, cancel, approve, ship）
- 避免深层嵌套（最多 2 层：/orders/{id}/items）
```

## 查询 API（读操作）

```
GET    /api/v1/orders/{id}             # 订单详情
GET    /api/v1/orders?status=PAID      # 订单列表
GET    /api/v1/orders/{id}/items       # 订单项列表

命名规则：
- 资源驱动命名
- 查询参数：?status=PAID&page=1&size=20
- 避免动词：GET /getOrders ✗  → GET /orders ✓
```

## CQRS 读写端点对照

```
命令（写）:
  POST   /orders             → CreateOrderCommand
  PUT    /orders/{id}/confirm → ConfirmOrderCommand
  DELETE /orders/{id}        → CancelOrderCommand

查询（读）:
  GET /orders/{id}           → OrderDetailDTO（物化视图）
  GET /orders?status=PAID    → OrderSummaryDTO[]（读模型）
```

## 错误码规范

| Code | HTTP Status | Meaning | Retryable |
|:--:|:--:|------|:--:|
| 0 | 200/201 | 成功 | — |
| 40001 | 400 | OrderStatus 不允许支付 | No |
| 40002 | 400 | 参数校验失败 | No |
| 40401 | 404 | 聚合未找到 | No |
| 40901 | 409 | 并发冲突（乐观锁） | Yes |
| 50000 | 500 | 系统内部错误 | Yes |

## 事件契约字段规范

每个领域事件必须包含：
- `eventId`：UUID，全局唯一
- `eventType`：事件类型，如 `order.paid`
- `aggregateId`：来源聚合 ID
- `occurredAt`：发生时间戳
- `schemaVersion`：schema 版本号
- `correlationId`：关联 ID（跨服务追踪）
- `payload`：业务数据，序列化为 JSON

## 事件版本兼容策略

| 策略 | 做法 | 适用 |
|------|------|------|
| 只增字段 | 新增字段设默认值 | 兼容升级 |
| 升级主版本 | 新 topic + 旧 topic 保留 | API 签名变化 |
| 双写过渡 | v1 + v2 同时发布，消费者升级后下线 v1 | 平滑迁移 |

## 统一响应格式

```json
// 成功（单体）
{ "code": 0, "message": "success", "data": { "id": "...", "status": "PAID" } }

// 成功（分页）
{ "code": 0, "message": "success", "data": { "records": [...], "total": 100, "page": 1, "pageSize": 20 } }

// 错误
{ "code": 40001, "message": "订单状态不允许支付", "detail": "当前：CANCELLED，可支付：DRAFT" }

// 校验错误
{ "code": 40002, "message": "参数校验失败", "detail": [{ "field": "amount", "message": "金额不能为负数" }] }
```
