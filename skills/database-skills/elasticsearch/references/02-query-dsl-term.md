# 精确查询与复合查询

精确查询不会对搜索词进行分词，直接匹配倒排索引中的精确值。

## term / terms — 精确值匹配

```bash
# 精确匹配 keyword 字段 (不要对 text 字段用 term!)
GET /products/_search
{
  "query": {
    "term": {
      "tags": "electronics"
    }
  }
}

# 多值匹配
GET /products/_search
{
  "query": {
    "terms": {
      "tags": ["electronics", "laptop"]
    }
  }
}

# ids 查询
GET /products/_search
{
  "query": {
    "ids": {
      "values": ["1", "2", "3"]
    }
  }
}
```

**⚠️ 常见陷阱**：`term` 查询对 `text` 字段几乎永远不匹配，因为 text 字段被分词后存储的是词项而非完整内容。

## range — 范围查询

```bash
# 数值范围
GET /products/_search
{
  "query": {
    "range": {
      "price": { "gte": 10000, "lte": 20000 }
    }
  }
}

# 日期范围 (支持日期数学)
GET /products/_search
{
  "query": {
    "range": {
      "created_at": { "gte": "now-7d/d", "lte": "now" }
    }
  }
}

# 日期数学: now-1h, now+1d, now/d, now-1M/M, 2024-01-01||+1y
```

## exists — 存在性检查

```bash
# 查找有 description 字段的文档
GET /products/_search
{
  "query": {
    "exists": { "field": "description" }
  }
}

# 查找没有 description 的文档 (using must_not)
GET /products/_search
{
  "query": {
    "bool": {
      "must_not": [
        { "exists": { "field": "description" } }
      ]
    }
  }
}
```

## bool 查询 — 最常用的组合查询

```bash
# bool 结构: must (AND+算分), filter (AND+缓存), should (OR), must_not (NOT)
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "轻薄笔记本" } }
      ],
      "filter": [
        { "term": { "status": "active" } },
        { "range": { "price": { "gte": 3000, "lte": 8000 } } }
      ],
      "should": [
        { "match": { "description": "轻薄" } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

**filter vs query 选择**：
- filter：精确匹配、范围过滤 → 可缓存，不贡献算分
- query：全文搜索 → 贡献算分，不可缓存

## nested — 嵌套对象查询

```json
// mapping 定义
PUT /orders
{
  "mappings": {
    "properties": {
      "items": {
        "type": "nested",
        "properties": {
          "product_id": { "type": "keyword" },
          "quantity": { "type": "integer" },
          "price": { "type": "float" }
        }
      }
    }
  }
}
```

```bash
# nested 查询 (保证跨字段关联正确)
GET /orders/_search
{
  "query": {
    "nested": {
      "path": "items",
      "query": {
        "bool": {
          "must": [
            { "term": { "items.product_id": "p100" } },
            { "range": { "items.quantity": { "gte": 2 } } }
          ]
        }
      }
    }
  }
}
```

## 其他特殊查询

```bash
# fuzzy — 模糊纠错
GET /products/_search
{
  "query": {
    "fuzzy": {
      "title": {
        "value": "macbok",
        "fuzziness": "AUTO",
        "prefix_length": 2,
        "transpositions": true
      }
    }
  }
}
# "macbok" → 匹配 "macbook"

# wildcard — 通配符 (性能差, 谨慎使用)
GET /products/_search
{
  "query": {
    "wildcard": {
      "title.keyword": "Mac*"
    }
  }
}

# regexp — 正则查询 (性能开销大)
GET /products/_search
{
  "query": {
    "regexp": {
      "title.keyword": "Macbook\\s(Pro|Air)"
    }
  }
}

# boosting — 权重控制 (降权不排除)
GET /products/_search
{
  "query": {
    "boosting": {
      "positive": { "match": { "title": "手机" } },
      "negative": { "term": { "status": "discontinued" } },
      "negative_boost": 0.2
    }
  }
}
```
