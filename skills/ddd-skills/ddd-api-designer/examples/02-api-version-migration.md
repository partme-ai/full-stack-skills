# API 版本迁移案例：v1 → v2

> 展示从 v1 到 v2 的完整 API 版本迁移过程，包括变更分析、兼容策略、OpenAPI 差异。

## 背景

订单服务 API v1 已运行 1 年。产品团队要求新增以下功能：
1. 支持多币种（原来只有人民币）
2. 订单项需要拆分展示
3. 增加分页标准化

这些变更涉及响应体字段变更，不兼容 v1，因此需要 v2。

## 变更分析

| 变更项 | 类型 | v1 | v2 |
|--------|------|----|----|
| ID 字段名 | 重命名 | `id` (int) | `orderId` (string) |
| 金额格式 | 类型变更 | `amount` (number) | `totalAmount` (string) + `currency` |
| 订单项 | 新增 | 无独立列表 | `items` array |
| 响应封装 | 结构变更 | 裸数据 | `Result<T>` 包装 |
| 分页 | 标准化 | 无标准分页 | `page/size/total/records` |

## v1 端点

### v1 OpenAPI

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  version: 1.0.0
servers:
  - url: https://api.example.com/api/v1

paths:
  /orders:
    get:
      summary: List orders
      parameters:
        - name: status
          in: query
          schema:
            type: string
      responses:
        '200':
          description: Order list
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/OrderV1'
    post:
      summary: Create order
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequestV1'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderV1'

components:
  schemas:
    OrderV1:
      type: object
      properties:
        id:
          type: integer
          example: 1
        status:
          type: string
          example: PAID
        amount:
          type: number
          example: 99.00

    CreateOrderRequestV1:
      type: object
      properties:
        customer_id:
          type: integer
        items:
          type: array
          items:
            type: object
            properties:
              product_id:
                type: integer
              quantity:
                type: integer
```

### v1 返回示例

```json
// GET /api/v1/orders?status=PAID
[
  {
    "id": 1,
    "status": "PAID",
    "amount": 99.00
  },
  {
    "id": 2,
    "status": "PAID",
    "amount": 199.00
  }
]

// POST /api/v1/orders
{
  "id": 3,
  "status": "DRAFT",
  "amount": 299.00
}
```

## v2 端点

### v2 OpenAPI

```yaml
openapi: 3.0.3
info:
  title: Order Service API
  version: 2.0.0
servers:
  - url: https://api.example.com/api/v2

paths:
  /orders:
    get:
      summary: List orders with pagination
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [DRAFT, PAID, SHIPPED, CANCELLED]
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: size
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Paginated order list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderListResponseV2'
    post:
      summary: Create order
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequestV2'
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiResponse'

components:
  schemas:
    OrderV2:
      type: object
      properties:
        orderId:
          type: string
          example: ORD-2024-001
        status:
          type: string
          example: PAID
        totalAmount:
          type: string
          example: "99.00"
        currency:
          type: string
          example: CNY
        items:
          type: array
          items:
            $ref: '#/components/schemas/OrderItemV2'
        createdAt:
          type: string
          format: date-time

    OrderItemV2:
      type: object
      properties:
        productName:
          type: string
        quantity:
          type: integer
        unitPrice:
          type: string
        subtotal:
          type: string

    OrderListResponseV2:
      type: object
      properties:
        code:
          type: integer
          example: 0
        message:
          type: string
        data:
          type: object
          properties:
            records:
              type: array
              items:
                $ref: '#/components/schemas/OrderSummaryV2'
            total:
              type: integer
              example: 100
            page:
              type: integer
              example: 1
            pageSize:
              type: integer
              example: 20

    OrderSummaryV2:
      type: object
      properties:
        orderId:
          type: string
        status:
          type: string
        totalAmount:
          type: string
        itemCount:
          type: integer
        createdAt:
          type: string
          format: date-time

    ApiResponse:
      type: object
      properties:
        code:
          type: integer
          example: 0
        message:
          type: string
          example: success
        data:
          type: object

    CreateOrderRequestV2:
      type: object
      required: [customerId, items, currency]
      properties:
        customerId:
          type: string
        currency:
          type: string
          enum: [CNY, USD, EUR]
        items:
          type: array
          items:
            type: object
            properties:
              productId:
                type: string
              quantity:
                type: integer
```

### v2 返回示例

```json
// GET /api/v2/orders?status=PAID&page=1
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [
      {
        "orderId": "ORD-2024-001",
        "status": "PAID",
        "totalAmount": "99.00",
        "itemCount": 2,
        "currency": "CNY",
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ],
    "total": 1,
    "page": 1,
    "pageSize": 20,
    "totalPages": 1
  }
}

// POST /api/v2/orders
{
  "code": 0,
  "message": "success",
  "data": {
    "orderId": "ORD-2024-003",
    "status": "DRAFT",
    "createdAt": "2024-01-16T14:00:00Z"
  }
}
```

## 兼容策略：双运行期

### 路由方案

```
API Gateway:
  /api/v1/*  → Order Service v1 (old deployment)
  /api/v2/*  → Order Service v2 (new deployment)

Internal routing:
  v1 service  → v1 DB schema
  v2 service  → v2 DB schema (migrated)
```

### 适配层（v1 → v2 数据转换）

当 v1 用户调用 v2 端点时，通过适配器转换：

```java
@Component
public class OrderV1ToV2Adapter {

    public OrderListResponseV2 adapt(List<OrderV1> v1Orders) {
        List<OrderSummaryV2> records = v1Orders.stream()
            .map(v1 -> new OrderSummaryV2(
                "ORD-" + v1.getId(),           // id → orderId
                v1.getStatus(),
                String.format("%.2f", v1.getAmount()),  // number → string
                0,                             // itemCount (v1 didn't have it)
                null                           // createdAt (v1 didn't have timestamp)
            ))
            .collect(toList());

        return new OrderListResponseV2(
            0, "success",
            new PaginatedData<>(records, records.size(), 1, records.size(), 1)
        );
    }
}
```

## 迁移时间线

```
2024-Q1: v2 设计 + 开发
2024-Q2: v2 上线，v1 + v2 双运行
          └── 通知所有 v1 客户端开始迁移
2024-Q3: v1 废弃期
          └── v1 响应添加 Deprecated header
          └── v1 流量监控
2024-Q4: v1 下线
          └── v1 端点返回 410 Gone
          └── 删除 v1 代码和部署
```

## 客户端迁移指南

```markdown
# 迁移到 Order API v2

## 关键变更

1. `id` → `orderId`（int → string）
2. 响应改为 Result<T> 包装
3. 分页标准化为 records/page/size/total
4. 金额改为字符串格式 "99.00" + 新增 currency 字段

## 迁移步骤

### Step 1：更新请求
```diff
- POST /api/v1/orders
- { "customer_id": 1, "items": [...] }
+ POST /api/v2/orders
+ { "customerId": "USR-001", "currency": "CNY", "items": [...] }
```

### Step 2：更新响应解析
```diff
- const orderId = response.id;
+ const orderId = response.data.orderId;
```

### Step 3：更新分页处理
```diff
- const total = response.length;
+ const total = response.data.total;
+ const page = response.data.page;
```

## 回退方案
如遇兼容性问题，切换回 /api/v1/ 端点并报告问题。
v1 将在 2024-Q4 下线。
```
