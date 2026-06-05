# API 文档化模式

> DDD 架构下的 API 文档规范，面向 CQRS 模式的命令/查询分离。

---

## 1. 命令 API 文档模板

```markdown
## POST /api/v1/{resource}/{action}

**命令**: {CommandName}
**ID 支持**: {幂等键}

### 请求体
```json
{
    "idempotentKey": "{唯一请求 ID}",
    "data": { ... }
}
```

### 响应
```json
{
    "code": 0,
    "message": "success",
    "data": {
        "id": "{资源 ID}",
        "status": "{结果状态}"
    }
}
```

### 业务规则
1. {规则 1}
2. {规则 2}

### 领域事件
- 成功触发：{EventName}
```

## 2. 查询 API 文档模板

```markdown
## GET /api/v1/{resource}s

**查询**: {QueryName}
**CQRS 模型**: {QueryModel}

### 参数
| 参数 | 类型 | 必填 | 说明 |
|------|:----:|:----:|------|
| {param1} | {type} | 是 | {说明} |

### 响应
```json
{
    "code": 0,
    "data": {
        "records": [],
        "total": 100,
        "page": 1,
        "pageSize": 20
    }
}
```

### 说明
- 查询不走领域模型，直接从读模型返回
- 不触发领域事件
- 不改变系统状态
```

## 3. OpenAPI 规范参考

```yaml
openapi: 3.0.3
info:
  title: 电商平台 API
  version: 1.0.0
paths:
  /api/v1/orders:
    post:
      summary: 创建订单（命令）
      operationId: createOrder
      x-cqrs-type: command
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
      responses:
        '200':
          description: 订单创建成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderCreatedResponse'

components:
  schemas:
    CreateOrderRequest:
      type: object
      required:
        - customerId
        - items
      properties:
        customerId:
          type: string
          description: 客户 ID
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItem'
    OrderCreatedResponse:
      type: object
      properties:
        orderId:
          type: string
        status:
          type: string
```

## 4. API 文档章节结构

```
API 文档标准章节：

1. {资源} Overview
   - 所属限界上下文
   - CQRS 类型（命令/查询）
   
2. Endpoints
   - 命令类（POST/PUT/DELETE）
   - 查询类（GET）
   
3. 请求/响应格式
   - 统一响应格式
   - 错误码说明
   
4. 业务规则
   - 命令的业务规则（哪些状态可操作）
   - 查询的过滤/排序/分页规则
   
5. 限流策略
   - 命令 API：较低 QPS
   - 查询 API：较高 QPS
   
6. 安全要求
   - 认证方式
   - 权限要求
```

## 5. DDD 与非 DDD API 文档差异

| 维度 | 传统 API 文档 | DDD API 文档 |
|------|-------------|-------------|
| 关注点 | HTTP 端点 + 参数 | 业务能力 + 领域语义 |
| 命令描述 | "POST /orders 创建订单" | "下单命令：创建新订单，触发订单已创建事件" |
| 参数说明 | "status: 订单状态" | "订单状态：业务状态机，包含 DRAFT→PAID→SHIPPED 等" |
| 事件关联 | 无 | "成功触发 OrderCreatedEvent，由库存消费" |
