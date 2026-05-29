# 示例: 零停机重建索引 (Zero-Downtime Reindex)

## 场景

需要修改已有索引的 mapping（如添加字段、修改分词器），但生产环境不能停机。

## 核心思路

Alias（别名） + Reindex（数据迁移） + 原子切换。

## 步骤

### 1. 假设已有索引和别名

```bash
# 初始状态: 已有 products_v1 索引, 通过 products 别名访问
GET /products/_search
{
  "query": { "match_all": {} }
}
# 别名可以透明访问
```

### 2. 创建新索引 (v2) 使用新的 mapping

```json
PUT /products_v2
{
  "settings": {
    "number_of_shards": 5,
    "number_of_replicas": 1,
    "refresh_interval": "-1"
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "ik_max_word",
        "fields": {
          "keyword": { "type": "keyword", "ignore_above": 256 },
          "pinyin": { "type": "text", "analyzer": "pinyin" }
        }
      },
      "description": {
        "type": "text",
        "analyzer": "ik_max_word"
      },
      "price": { "type": "double" },
      "new_field": { "type": "keyword" },
      "search_all": {
        "type": "text",
        "analyzer": "ik_max_word"
      }
    }
  }
}
```

### 3. 执行 Reindex 数据迁移

```bash
# 使用 slices=auto 并行加速
POST /_reindex?slices=auto&wait_for_completion=false
{
  "source": {
    "index": "products_v1"
  },
  "dest": {
    "index": "products_v2"
  },
  "script": {
    "source": """
      // 如果新索引有 copy_to 字段, 在脚本中处理
      if (ctx._source.title != null && ctx._source.description != null) {
        ctx._source.search_all = ctx._source.title + ' ' + ctx._source.description;
      }
      // 添加新字段默认值
      ctx._source.new_field = 'migrated';
    """
  }
}
# 返回 task id, 可用 _tasks API 查看进度
GET /_tasks/<task_id>
```

### 4. 原子切换别名 (零停机)

```bash
# 关键步骤: 一次操作移除旧别名 + 添加新别名
# 这期间已有查询不会中断
POST /_aliases
{
  "actions": [
    { "remove": { "index": "products_v1", "alias": "products" } },
    { "add": { "index": "products_v2", "alias": "products" } }
  ]
}
# 原子操作, 切换完成后所有通过 products 别名的查询自动指向 v2
```

### 5. 验证并删除旧索引

```bash
# 验证新索引数据完整
GET /products/_search
{
  "query": { "match_all": {} },
  "size": 0
}

# 确认无误后删除旧索引
DELETE /products_v1
```

## Reindex 进阶技巧

### 跨集群 Reindex

```bash
POST /_reindex
{
  "source": {
    "remote": {
      "host": "http://old-cluster:9200",
      "username": "elastic",
      "password": "pass"
    },
    "index": "products"
  },
  "dest": {
    "index": "products_v2"
  }
}
```

### 只迁移部分数据

```bash
POST /_reindex
{
  "source": {
    "index": "products_v1",
    "query": {
      "term": { "status": "active" }
    }
  },
  "dest": {
    "index": "products_active"
  }
}
```

### 冲突处理

```bash
# 跳过已存在的文档 (op_type=create)
POST /_reindex
{
  "source": { "index": "products_v1" },
  "dest": {
    "index": "products_v2",
    "op_type": "create"
  }
}

# 或者使用 version_type=external 保留旧版本
```

### Reindex 大小和速度

```bash
# 限制批次大小 (默认 1000)
POST /_reindex
{
  "source": {
    "index": "products_v1",
    "size": 5000
  },
  "dest": {
    "index": "products_v2"
  }
}

# 限制速率 (每秒文档数)
PUT /_cluster/settings
{
  "transient": {
    "indices.recovery.max_bytes_per_sec": "200mb"
  }
}
```

## 注意事项

1. **大索引 Reindex**：建议 `slices=auto` 并行执行，可根据数据节点数自动调整并行度
2. **源索引不影响**：Reindex 期间源索引可继续读写服务
3. **Refresh 优化**：新索引设 `refresh_interval: -1`，迁移完再恢复
4. **副本优化**：新索引设 `number_of_replicas: 0`，迁移完再调回
5. **验证数据完整性**：迁移后对比文档数 (`_cat/count`)
6. **善后清理**：确认新索引正常后删除旧索引释放空间
