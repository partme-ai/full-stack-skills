# 搜索服务 API 设计案例

> 搜索上下文（Search BC）的 REST API 设计，展示 CQRS 查询侧的物化视图设计。

## 领域模型

```
SearchIndex (Read Model)
├── DocumentId
├── DocumentType
├── Title / Content
├── Tags[]
└── IndexedAt
```

## 端点设计

| 端点 | 类型 | 说明 |
|------|------|------|
| `GET /api/v1/search?q=&type=&page=` | Query | 全文搜索 |
| `POST /api/v1/search/index` | Command | 重建索引 |
| `GET /api/v1/search/suggest?q=` | Query | 搜索建议 |
| `GET /api/v1/search/facets?field=` | Query | 聚合统计 |

## 查询侧设计要点

- 搜索结果使用 Cursor 分页（`?cursor=xxx&size=20`）
- 支持字段选择（`?fields=id,title,summary`）
- 结果按相关性排序（评分倒序）
