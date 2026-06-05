# 映射与字段类型详解

Mapping 定义文档中每个字段的数据类型和分析方式，相当于关系型数据库的 Schema。

## 字段类型速查

| 字段类型 | 说明 | 适用场景 |
|---------|------|---------|
| `text` | 被分词的全文字段 | 全文搜索、文章内容 |
| `keyword` | 精确值、不被分词 | 标签、状态、分类、ID |
| `integer` | 32 位整数 | 年龄、计数 |
| `long` | 64 位整数 | 时间戳、大数值 |
| `float` | 单精度浮点 | 价格、分数 |
| `double` | 双精度浮点 | 科学计算 |
| `boolean` | 布尔值 | 开关、状态 |
| `date` | 日期 (可多 format) | 时间字段 |
| `ip` | IPv4/IPv6 | IP 分析、CIDR 匹配 |
| `geo_point` | 经纬度点 | 地理位置、距离排序 |
| `geo_shape` | 复杂地理形状 | 区域查询、地理围栏 |
| `nested` | 嵌套对象 (独立索引) | 保持数组内对象关联 |
| `object` | JSON 对象 (默认) | 普通嵌套数据 |
| `completion` | 自动补全 | 搜索建议 |
| `dense_vector` | 稠密向量 | KNN 语义搜索 |
| `flattened` | 扁平化嵌套对象 | 未知结构的元数据 |
| `percolator` | 反向搜索 | 告警规则匹配 |
| `range` | 范围类型 (integer_range) | IP 段、时间范围 |

## 动态映射 (Dynamic Mapping)

| 设置 | 行为 |
|------|------|
| `"dynamic": true` | 自动检测并添加新字段 (默认) |
| `"dynamic": "runtime"` | 运行时映射 (7.11+) |
| `"dynamic": false` | 忽略新字段 (不索引，可查询 _source) |
| `"dynamic": "strict"` | 遇到新字段抛出异常 |

## 映射参数详解

```json
PUT /articles
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "ik_max_word",
        "search_analyzer": "ik_smart",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          },
          "pinyin": {
            "type": "text",
            "analyzer": "pinyin"
          }
        }
      },
      "price": {
        "type": "float",
        "coerce": false
      },
      "meta_data": {
        "type": "flattened"
      }
    }
  }
}
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `analyzer` | 索引分词器 | standard |
| `search_analyzer` | 搜索分词器 | 同 analyzer |
| `fields` | 多字段 | 无 |
| `copy_to` | 复制到组合字段 | 无 |
| `coerce` | 自动类型转换 | true |
| `doc_values` | 列式存储（排序/聚合） | text 外 true |
| `index` | 是否索引 | true |
| `norms` | 归一化因子（算分用） | true |
| `ignore_above` | 超长不索引 (keyword) | 无 |
| `eager_global_ordinals` | 预加载全局序数 | false |

## 别名 (Alias) 与索引模板

```json
// 原子切换别名 (零停机重建)
POST /_aliases
{
  "actions": [
    { "remove": { "index": "products_v1", "alias": "products" } },
    { "add": { "index": "products_v2", "alias": "products" } }
  ]
}

// 索引模板
PUT /_index_template/logs_template
{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "number_of_shards": 3,
      "number_of_replicas": 1
    },
    "mappings": {
      "properties": {
        "@timestamp": { "type": "date" },
        "message": { "type": "text" },
        "level": { "type": "keyword" }
      }
    }
  }
}
```

## 索引设置

```json
PUT /my_index
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1,
    "refresh_interval": "30s",
    "max_result_window": 100000,
    "codec": "best_compression"
  },
  "mappings": { ... }
}
```

**重要**：`number_of_shards` 建后不可修改。`refresh_interval` 大批量写入时可设为 `-1`（关闭）。
