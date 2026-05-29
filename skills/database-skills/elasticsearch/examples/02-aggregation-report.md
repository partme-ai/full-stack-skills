# 示例: 聚合报表 — 电商销售分析

## 场景

基于订单数据构建销售分析仪表盘：销售额趋势、TOP 品类、品牌分布、价格区段。

## 步骤

### 1. 创建索引

```json
PUT /orders
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "order_id": { "type": "keyword" },
      "user_id": { "type": "keyword" },
      "product_id": { "type": "keyword" },
      "product_name": { "type": "text", "fields": { "keyword": { "type": "keyword" } } },
      "category": { "type": "keyword" },
      "brand": { "type": "keyword" },
      "amount": { "type": "float" },
      "quantity": { "type": "integer" },
      "status": { "type": "keyword" },
      "region": { "type": "keyword" },
      "order_date": { "type": "date" },
      "payment_date": { "type": "date" }
    }
  }
}
```

### 2. 按品类统计销售额 (terms + sum)

```bash
# 每个品类的总销售额, 降序排列
GET /orders/_search
{
  "size": 0,
  "aggs": {
    "by_category": {
      "terms": {
        "field": "category",
        "size": 20,
        "order": { "total_sales": "desc" }
      },
      "aggs": {
        "total_sales": { "sum": { "field": "amount" } },
        "avg_order": { "avg": { "field": "amount" } },
        "order_count": { "value_count": { "field": "order_id" } }
      }
    }
  }
}
```

### 3. 每日销售趋势 (date_histogram + sum)

```bash
# 按天统计销售额
GET /orders/_search
{
  "size": 0,
  "query": {
    "range": {
      "order_date": { "gte": "now-30d", "lte": "now" }
    }
  },
  "aggs": {
    "daily_sales": {
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "day",
        "format": "yyyy-MM-dd",
        "min_doc_count": 0,
        "extended_bounds": {
          "min": "2024-01-01",
          "max": "2024-12-31"
        }
      },
      "aggs": {
        "revenue": { "sum": { "field": "amount" } },
        "orders": { "value_count": { "field": "order_id" } }
      }
    }
  }
}
```

### 4. 价格区段分布 (range + stats)

```bash
# 价格区段 + 每个区段的统计
GET /orders/_search
{
  "size": 0,
  "aggs": {
    "price_ranges": {
      "range": {
        "field": "amount",
        "ranges": [
          { "key": "低价 (<100)", "to": 100 },
          { "key": "中低价 (100-500)", "from": 100, "to": 500 },
          { "key": "中价 (500-2000)", "from": 500, "to": 2000 },
          { "key": "高价 (2000-10000)", "from": 2000, "to": 10000 },
          { "key": "超高 (>10000)", "from": 10000 }
        ]
      },
      "aggs": {
        "amount_stats": { "stats": { "field": "amount" } },
        "brand_distribution": {
          "terms": { "field": "brand", "size": 5 }
        }
      }
    }
  }
}
```

### 5. 地区分布 + TOP 品牌 (嵌套聚合)

```bash
# 各地区销售额, 每个地区 TOP 品牌
GET /orders/_search
{
  "size": 0,
  "aggs": {
    "by_region": {
      "terms": {
        "field": "region",
        "size": 10,
        "order": { "revenue": "desc" }
      },
      "aggs": {
        "revenue": { "sum": { "field": "amount" } },
        "order_count": { "value_count": { "field": "order_id" } },
        "top_brands": {
          "terms": {
            "field": "brand",
            "size": 5,
            "order": { "brand_revenue": "desc" }
          },
          "aggs": {
            "brand_revenue": { "sum": { "field": "amount" } }
          }
        }
      }
    }
  }
}
```

### 6. 综合仪表盘查询 (一次查询完成多项分析)

```bash
# 一次查询返回多种聚合结果
GET /orders/_search
{
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        { "term": { "status": "completed" } },
        { "range": { "order_date": { "gte": "now-30d/d", "lte": "now" } } }
      ]
    }
  },
  "aggs": {
    "overview": {        // 总体指标
      "stats": { "field": "amount" }
    },
    "total_revenue": {
      "sum": { "field": "amount" }
    },
    "unique_customers": {
      "cardinality": { "field": "user_id" }
    },
    "sales_trend": {     // 日销售趋势
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "day"
      },
      "aggs": {
        "daily_revenue": { "sum": { "field": "amount" } }
      }
    },
    "top_categories": {  // TOP 品类
      "terms": { "field": "category", "size": 10 },
      "aggs": {
        "cat_revenue": { "sum": { "field": "amount" } }
      }
    },
    "price_distribution": {  // 价格分布
      "percentiles": {
        "field": "amount",
        "percents": [25, 50, 75, 90, 99]
      }
    }
  }
}
# 一次请求返回: 总览统计 + 总销售额 + 去重用户数 + 日趋势 + TOP 品类 + 价格百分位
```
