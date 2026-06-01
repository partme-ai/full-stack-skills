# API 分页与过滤设计

## 分页方案对比

| 方案 | 原理 | 优点 | 缺点 | 适用 |
|------|------|------|------|------|
| **Offset/Page** | `?page=1&size=20` | 实现简单，随机跳页 | 深分页性能差，数据偏移 | 管理后台、小数据集 |
| **Cursor** | `?cursor=eyJpZCI6MTAwfQ==&limit=20` | 稳定性能，实时数据准确 | 不能随机跳页 | 用户端列表、实时数据 |
| **Keyset** | `?after_id=100&limit=20` | 最快性能（索引） | 不能跳页，排序受限 | 只按 ID 排序的场景 |
| **Seek** | `?offset_id=100&size=20` | Keyset + 灵活排序 | 实现稍复杂 | 社交媒体 Feeds |

### 推荐方案

- **管理端**：Offset/Page 分页（需要跳页功能）
- **用户端**：Cursor 分页（实时数据场景）
- **大数据量**：Keyset/Seek 分页（避免 offset 导致的性能退化）

## Offset/Page 分页规范

### 请求参数

```
GET /api/v1/orders?page=1&size=20&sort=createdAt,desc
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `page` | 1 | 页码，从 1 开始 |
| `size` | 20 | 每页条数，最大 100 |
| `sort` | createdAt,desc | 排序字段和方向 |

### 响应格式

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [
      { "orderId": "ORD-2024-001", "status": "PAID", "totalAmount": "99.00" }
    ],
    "total": 100,
    "page": 1,
    "pageSize": 20,
    "totalPages": 5
  }
}
```

### 实现

```java
public class PageRequest {
    private int page = 1;        // 页码，从 1 开始
    private int size = 20;       // 每页条数
    private String sort;         // 排序：createdAt,desc

    public long getOffset() {
        return (long) (page - 1) * size;
    }

    public Sort getSort() {
        // 解析 sort 参数 → Spring Sort 对象
    }
}

public class PageResult<T> {
    private List<T> records;
    private long total;
    private int page;
    private int pageSize;
    private int totalPages;

    public static <T> PageResult<T> of(List<T> records, long total, PageRequest request) {
        PageResult<T> result = new PageResult<>();
        result.records = records;
        result.total = total;
        result.page = request.getPage();
        result.pageSize = request.getSize();
        result.totalPages = (int) Math.ceil((double) total / request.getSize());
        return result;
    }
}
```

## Cursor 分页规范

### 请求参数

```
GET /api/v1/orders?cursor=eyJjcmVhdGVkQXQiOiIyMDI0LTAxLTE1VDEwOjMwOjAwWiIsImlkIjoiT1JELTIwMjQtMDEwIn0=&limit=20
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `cursor` | 无 | 上一页最后一条记录的编码标识 |
| `limit` | 20 | 每页条数 |
| `sort` | createdAt,desc | 排序（必须与 cursor 编码一致） |

### 响应格式

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [
      { "orderId": "ORD-2024-011", "status": "PAID", "createdAt": "2024-01-16T10:30:00Z" }
    ],
    "nextCursor": "eyJjcmVhdGVkQXQiOiIyMDI0LTAxLTE2VDEwOjMwOjAwWiIsImlkIjoiT1JELTIwMjQtMDExIn0=",
    "hasMore": true
  }
}
```

### Cursor 编码实现

```java
public class CursorCodec {
    private static final ObjectMapper mapper = new ObjectMapper();

    // 将游标对象编码为 Base64
    public static String encode(Map<String, Object> cursorFields) {
        try {
            return Base64.getUrlEncoder().encodeToString(
                mapper.writeValueAsString(cursorFields).getBytes());
        } catch (JsonProcessingException e) {
            throw new RuntimeException("Cursor encode failed", e);
        }
    }

    // 解码游标
    public static Map<String, Object> decode(String cursor) {
        try {
            byte[] bytes = Base64.getUrlDecoder().decode(cursor);
            return mapper.readValue(bytes, Map.class);
        } catch (Exception e) {
            throw new IllegalArgumentException("Invalid cursor", e);
        }
    }
}
```

## 过滤设计

### 基础过滤

```
GET /api/v1/orders?status=PAID&customerId=USR-001
GET /api/v1/orders?status=PAID,SHIPPED          # 多值过滤（逗号分隔）
GET /api/v1/orders?createdAtFrom=2024-01-01&createdAtTo=2024-01-31  # 范围过滤
```

### 高级过滤（复杂查询）

```json
// POST /api/v1/orders/search
{
  "filters": [
    { "field": "status", "operator": "in", "value": ["PAID", "SHIPPED"] },
    { "field": "totalAmount", "operator": "gte", "value": 100 },
    { "field": "createdAt", "operator": "between", "value": ["2024-01-01", "2024-01-31"] }
  ],
  "sort": { "field": "createdAt", "order": "desc" },
  "page": { "page": 1, "size": 20 }
}
```

| 操作符 | 说明 | SQL 对应 |
|--------|------|---------|
| `eq` | 等于 | `=` |
| `neq` | 不等于 | `!=` |
| `in` | 包含 | `IN` |
| `nin` | 不包含 | `NOT IN` |
| `gt` / `gte` | 大于 / 大于等于 | `>` / `>=` |
| `lt` / `lte` | 小于 / 小于等于 | `<` / `<=` |
| `between` | 范围 | `BETWEEN` |
| `like` | 模糊 | `LIKE` |
| `contains` | 包含（数组/字符串） | `@>` / `LIKE %...%` |

## 字段选择

允许客户端只请求需要的字段，减少传输量：

```
GET /api/v1/orders?fields=orderId,status,totalAmount
```

```json
{
  "data": {
    "orderId": "ORD-2024-001",
    "status": "PAID",
    "totalAmount": "99.00"
  }
}
```

## 分页最佳实践

1. **统一分页格式**：所有列表接口使用相同的分页响应结构（records/total/page/pageSize）
2. **限制最大 size**：`size` 上限 100，防止大查询压垮数据库
3. **深分页优化**：超过 10000 条 offset 时建议切换到 Cursor 或 Keyset
4. **总记录数缓存**：`total` 可以使用缓存，减少 COUNT 查询
5. **排序字段加索引**：`ORDER BY createdAt` 必须有对应索引
6. **搜索端点分离**：复杂搜索用 `POST /search` 专用端点，不混入 GET 查询
7. **默认排序**：始终提供默认排序，避免分页结果不稳定
