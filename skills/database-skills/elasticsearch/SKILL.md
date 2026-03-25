---
name: elasticsearch
description: "Guides Elasticsearch usage including index mapping design, query DSL (match, term, bool, aggregations), bulk indexing, cluster management, and performance tuning. Use when the user needs to implement full-text search, design index mappings, write complex search queries, or manage Elasticsearch clusters."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Design index mappings with analyzers and field types
- Write search queries (match, term, bool, multi_match, nested, aggregations)
- Index, update, or bulk-load documents via the REST API
- Manage clusters (shards, replicas, snapshots, upgrades)
- Integrate Elasticsearch with Kibana or Logstash (ELK stack)

## How to use this skill

### Workflow

1. **Design the mapping** - Define field types, analyzers, and index settings
2. **Index documents** - Use PUT/POST or bulk API
3. **Write queries** - Use Query DSL with filters for caching
4. **Monitor and tune** - Check cluster health, slow logs, and shard balance

### Quick-Start Example: Create Index and Search

```json
// Create index with mapping
PUT /products
{
  "mappings": {
    "properties": {
      "name":        { "type": "text", "analyzer": "standard" },
      "description": { "type": "text" },
      "price":       { "type": "float" },
      "category":    { "type": "keyword" },
      "created_at":  { "type": "date" }
    }
  }
}

// Index a document
POST /products/_doc
{
  "name": "Wireless Mouse",
  "description": "Ergonomic wireless mouse with USB-C receiver",
  "price": 29.99,
  "category": "electronics",
  "created_at": "2025-01-15"
}

// Search with bool query and aggregation
GET /products/_search
{
  "query": {
    "bool": {
      "must": [{ "match": { "description": "wireless" } }],
      "filter": [{ "range": { "price": { "lte": 50 } } }]
    }
  },
  "aggs": {
    "by_category": { "terms": { "field": "category" } }
  }
}
```

## Best Practices

1. **Define explicit mappings** - Avoid dynamic mapping in production; set `dynamic: strict` to catch errors
2. **Use filters for exact matches** - Filters are cached and faster than queries for keyword/range conditions
3. **Paginate with search_after** - Avoid deep `from`/`size` pagination; use `search_after` for large result sets
4. **Plan shards carefully** - Target 20-40 GB per shard; avoid too many small shards
5. **Snapshot regularly** - Use snapshot/restore for backups; test restore procedures

## Keywords

elasticsearch, search, index, mapping, query DSL, aggregation, 搜索引擎, 全文检索, 聚合, ELK, Kibana, bulk API, cluster
