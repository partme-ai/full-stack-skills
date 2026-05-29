# 桶聚合 (Bucket Aggregations)

桶聚合将文档分组到不同的"桶"中，类似 SQL 的 GROUP BY。每个桶可以嵌套子聚合。

## terms — 分组聚合 (GROUP BY)

```bash
# 按标签分组统计
GET /products/_search
{
  "size": 0,
  "aggs": {
    "by_tags": {
      "terms": {
        "field": "tags",
        "size": 20,
        "order": { "_count": "desc" }
      }
    }
  }
}

# 带子聚合: 每个分组的平均价格
GET /products/_search
{
  "size": 0,
  "aggs": {
    "by_brand": {
      "terms": {
        "field": "brand",
        "size": 10,
        "order": { "avg_price": "desc" }
      },
      "aggs": {
        "avg_price": { "avg": { "field": "price" } },
        "product_count": { "value_count": { "field": "id" } }
      }
    }
  }
}
```

**注意事项**：
- `size` 控制返回桶数（默认 10），超大 size 消耗内存
- `order` 支持按文档数 (`_count`)、聚合键 (`_key`)、子聚合排序
- keyword 字段上聚合性能最佳，text 字段需开启 `fielddata`

## range / date_range — 范围分组

```bash
# 价格区间分组
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_ranges": {
      "range": {
        "field": "price",
        "ranges": [
          { "key": "0-1000", "from": 0, "to": 1000 },
          { "key": "1000-5000", "from": 1000, "to": 5000 },
          { "key": "5000+", "from": 5000 }
        ]
      }
    }
  }
}

# 日期范围
GET /orders/_search
{
  "size": 0,
  "aggs": {
    "date_ranges": {
      "date_range": {
        "field": "order_date",
        "ranges": [
          { "from": "now-30d/d", "to": "now" },
          { "from": "now-90d/d", "to": "now-30d/d" }
        ]
      }
    }
  }
}
```

## histogram / date_histogram — 直方图

```bash
# 价格直方图 (间隔 1000)
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_histogram": {
      "histogram": {
        "field": "price",
        "interval": 1000,
        "min_doc_count": 1
      }
    }
  }
}

# 时间直方图 (按小时/天/月/年聚合)
GET /orders/_search
{
  "size": 0,
  "aggs": {
    "orders_over_time": {
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "day",     // month, quarter, year
        "format": "yyyy-MM-dd",
        "min_doc_count": 0,
        "extended_bounds": {
          "min": "2024-01-01",
          "max": "2024-12-31"
        }
      }
    }
  }
}
```

## filter / filters — 过滤聚合

```bash
# 单一过滤
GET /products/_search
{
  "size": 0,
  "aggs": {
    "active_products": {
      "filter": { "term": { "status": "active" } },
      "aggs": {
        "avg_price": { "avg": { "field": "price" } }
      }
    }
  }
}

# 多过滤
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_categories": {
      "filters": {
        "other_bucket": true,
        "filters": {
          "budget":  { "range": { "price": { "lte": 5000 } } },
          "mid":     { "range": { "price": { "from": 5000, "to": 15000 } } },
          "premium": { "range": { "price": { "gte": 15000 } } }
        }
      }
    }
  }
}
```

## 管道聚合 (Pipeline Aggregations)

```bash
# derivative — 环比增量
GET /orders/_search
{
  "size": 0,
  "aggs": {
    "sales_per_day": {
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "day"
      },
      "aggs": {
        "daily_sales": { "sum": { "field": "amount" } },
        "sales_derivative": {
          "derivative": { "buckets_path": "daily_sales" }
        }
      }
    }
  }
}

# bucket_script — 计算桶间比例
GET /products/_search
{
  "size": 0,
  "aggs": {
    "total_products": { "value_count": { "field": "id" } },
    "active_products": {
      "filter": { "term": { "status": "active" } }
    },
    "active_ratio": {
      "bucket_script": {
        "buckets_path": {
          "activeCount": "active_products>_count",
          "totalCount": "total_products"
        },
        "script": "params.activeCount / params.totalCount * 100"
      }
    }
  }
}

# bucket_selector — 过滤桶 (类似 HAVING)
GET /products/_search
{
  "size": 0,
  "aggs": {
    "by_brand": {
      "terms": { "field": "brand", "size": 100 },
      "aggs": {
        "avg_price": { "avg": { "field": "price" } },
        "brands_having_avg_gt_10000": {
          "bucket_selector": {
            "buckets_path": { "avgPrice": "avg_price" },
            "script": "params.avgPrice > 10000"
          }
        }
      }
    }
  }
}
```

## 业务场景速查

| 聚合 | 场景 |
|------|------|
| terms | 商品分类统计、品牌分布、标签统计 |
| date_histogram | 销售日报/月报、API 请求时序、监控趋势 |
| range | 价格区间分布、年龄段统计 |
| filters | 多条件对比分析 |
| derivative | 环比增长/下降分析 |
| bucket_selector | 过滤出符合条件的组 (HAVING) |
