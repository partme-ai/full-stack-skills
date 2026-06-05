# 指标聚合 (Metric Aggregations)

指标聚合对文档集中的某个字段进行数值计算，类似于 SQL 聚合函数。

## 基本结构

```json
{
  "size": 0,
  "aggs": {
    "my_agg_name": {       // 自定义聚合名称
      "avg": {              // 聚合类型
        "field": "price"
      }
    }
  }
}
```

## 常用指标聚合

### avg — 平均值

```bash
GET /products/_search
{
  "size": 0,
  "aggs": {
    "avg_price": {
      "avg": { "field": "price" }
    }
  }
}
```

### sum / min / max

```bash
GET /products/_search
{
  "size": 0,
  "aggs": {
    "total_revenue": { "sum": { "field": "price" } },
    "min_price": { "min": { "field": "price" } },
    "max_price": { "max": { "field": "price" } }
  }
}
```

### stats — 批量统计

```bash
# 一次性返回 count/min/max/avg/sum
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_stats": {
      "stats": { "field": "price" }
    }
  }
}
```

### extended_stats — 扩展统计

```bash
# 额外返回方差、标准差、总和平方等
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_extended": {
      "extended_stats": { "field": "price" }
    }
  }
}
```

### cardinality — 去重计数 (COUNT DISTINCT)

```bash
GET /products/_search
{
  "size": 0,
  "aggs": {
    "unique_brands": {
      "cardinality": {
        "field": "brand",
        "precision_threshold": 100   // 精度阈值 (默认 3000)
      }
    }
  }
}
```

**说明**：cardinality 基于 HyperLogLog++ 算法，近似去重。`precision_threshold` 越高越精确，但消耗更多内存。

### value_count — 非空值计数

```bash
GET /products/_search
{
  "size": 0,
  "aggs": {
    "by_brand": {
      "terms": { "field": "brand" },
      "aggs": {
        "price_count": { "value_count": { "field": "price" } }
      }
    }
  }
}
```

通常作为子聚合，用于计算每个桶的样本数。

### percentiles — 百分位

```bash
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_percentiles": {
      "percentiles": {
        "field": "price",
        "percents": [1, 5, 25, 50, 75, 95, 99]
      }
    }
  }
}
```

### percentile_ranks — 百分位排名

```bash
# 值落在指定阈值内的百分比
GET /products/_search
{
  "size": 0,
  "aggs": {
    "price_ranks": {
      "percentile_ranks": {
        "field": "price",
        "values": [5000, 10000]
      }
    }
  }
}
```

## 业务场景速查

| 聚合 | 典型场景 |
|------|---------|
| avg | 商品均价、平均评分、平均响应时间 |
| sum | 总销售额、总库存量、总访问量 |
| stats | 批量统计摘要（报表概览） |
| cardinality | 独立访客 UV、去重品牌数、唯一 IP 数 |
| percentiles | 价格分布分析、APM P99 延迟、收入分布 |
