# 示例: 全文搜索实战 — 电商商品搜索

## 场景

构建一个电商商品搜索功能，支持关键词搜索、多字段搜索、价格筛选、分页。

## 步骤

### 1. 创建索引与 Mapping

```json
PUT /products
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  },
  "mappings": {
    "dynamic": "strict",
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "ik_max_word",
        "fields": {
          "keyword": { "type": "keyword", "ignore_above": 256 }
        }
      },
      "description": {
        "type": "text",
        "analyzer": "ik_max_word"
      },
      "category": { "type": "keyword" },
      "brand": { "type": "keyword" },
      "price": { "type": "float" },
      "tags": { "type": "keyword" },
      "status": { "type": "keyword" },
      "created_at": { "type": "date" },
      "stock": { "type": "integer" }
    }
  }
}
```

### 2. 导入示例数据

```bash
POST /products/_bulk
{"index":{"_id":1}}
{"title":"Apple MacBook Pro 16英寸 M3 Pro","description":"Apple M3 Pro芯片, 18GB统一内存, 512GB存储","category":"笔记本","brand":"Apple","price":19999,"tags":["electronics","laptop","apple"],"status":"active","stock":50,"created_at":"2024-01-15T10:30:00Z"}
{"index":{"_id":2}}
{"title":"华为 MateBook X Pro 2024","description":"13.9英寸 3K触控屏, 32GB内存, 1TB SSD","category":"笔记本","brand":"华为","price":14999,"tags":["electronics","laptop","huawei"],"status":"active","stock":30,"created_at":"2024-01-20T14:00:00Z"}
{"index":{"_id":3}}
{"title":"iPhone 15 Pro Max 256GB","description":"A17 Pro芯片, 4800万像素主摄, 钛金属设计","category":"手机","brand":"Apple","price":9999,"tags":["electronics","phone","apple"],"status":"active","stock":100,"created_at":"2024-02-01T09:00:00Z"}
{"index":{"_id":4}}
{"title":"Samsung Galaxy S24 Ultra","description":"Snapdragon 8 Gen 3, 200MP相机, S Pen","category":"手机","brand":"Samsung","price":12999,"tags":["electronics","phone","samsung"],"status":"active","stock":80,"created_at":"2024-02-10T11:00:00Z"}
{"index":{"_id":5}}
{"title":"机械革命 极光Pro 游戏本","description":"RTX4060显卡, i7-12650H, 15.6英寸165Hz","category":"笔记本","brand":"机械革命","price":6999,"tags":["electronics","laptop","gaming"],"status":"active","stock":20,"created_at":"2024-03-01T16:00:00Z"}
{"index":{"_id":6}}
{"title":"Apple MacBook Air M2","description":"M2芯片, 13.6英寸, 8GB内存, 256GB存储","category":"笔记本","brand":"Apple","price":8999,"tags":["electronics","laptop","apple"],"status":"inactive","stock":0,"created_at":"2023-06-01T10:00:00Z"}
```

### 3. 基本关键词搜索

```bash
# 搜索"笔记本" (精确匹配标题)
GET /products/_search
{
  "query": {
    "match": {
      "title": "笔记本"
    }
  }
}
# 返回: MacBook Pro, MateBook X Pro, 极光Pro

# 多字段搜索 (标题+描述)
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "苹果笔记本 M3",
      "fields": ["title^3", "description"],
      "type": "best_fields"
    }
  }
}
# title 权重 3 倍, MacBook Pro 排最前
```

### 4. 综合搜索 (关键词 + 筛选 + 分页)

```bash
# 搜索"笔记本", 过滤价格 5000-15000, 只返回 active 商品
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "笔记本" } }
      ],
      "filter": [
        { "term": { "status": "active" } },
        { "range": { "price": { "gte": 5000, "lte": 15000 } } }
      ]
    }
  },
  "sort": [
    { "price": { "order": "asc" } }
  ],
  "_source": ["title", "brand", "price", "stock"]
}
# 返回: 极光Pro (6999), MacBook Air (8999), MateBook X Pro (14999)
```

### 5. 搜索建议 (Completion Suggester)

```json
PUT /products/_mapping
{
  "properties": {
    "title_suggest": {
      "type": "completion"
    }
  }
}

POST /products/_update/1
{
  "doc": {
    "title_suggest": ["Apple MacBook Pro", "MacBook Pro"]
  }
}

POST /products/_update/3
{
  "doc": {
    "title_suggest": ["iPhone 15 Pro Max", "iPhone 15"]
  }
}

# 搜索建议
GET /products/_search
{
  "suggest": {
    "product_suggest": {
      "prefix": "mac",
      "completion": {
        "field": "title_suggest",
        "size": 5
      }
    }
  }
}
# 返回: ["Apple MacBook Pro", "MacBook Pro"]
```

### 6. 高亮显示

```bash
GET /products/_search
{
  "query": {
    "match": { "title": "笔记本" }
  },
  "highlight": {
    "fields": {
      "title": {},
      "description": {}
    },
    "pre_tags": ["<em>"],
    "post_tags": ["</em>"]
  }
}
# title 中"笔记本"会被 <em> 标签包裹
```

## 完整搜索 API 示例

```bash
# 前端搜索框调用的完整 API
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        { "multi_match": {
          "query": "笔记本",
          "fields": ["title^3", "description", "brand"],
          "type": "best_fields"
        }}
      ],
      "filter": [
        { "term": { "status": "active" } },
        { "terms": { "category": ["笔记本", "平板"] }},
        { "range": { "price": { "gte": 3000, "lte": 20000 } }},
        { "term": { "brand": "Apple" }}
      ],
      "should": [
        { "term": { "tags": "hot" }},
        { "term": { "is_new": true }}
      ]
    }
  },
  "sort": [
    { "_score": { "order": "desc" }},
    { "created_at": { "order": "desc" }}
  ],
  "from": 0,
  "size": 20,
  "_source": ["title", "brand", "price", "stock", "category"],
  "highlight": {
    "fields": { "title": { "number_of_fragments": 0 } }
  }
}
```
