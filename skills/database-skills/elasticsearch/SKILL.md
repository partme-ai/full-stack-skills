---
name: elasticsearch
description: Provides comprehensive guidance for Elasticsearch including indexing, searching, aggregations, mappings, and cluster management. Use when the user asks about Elasticsearch, needs to implement search functionality, work with Elasticsearch queries, or manage Elasticsearch clusters.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 设计索引 mapping、分词与查询（term、match、bool、agg）
- 使用 REST API 或客户端进行索引、搜索与聚合
- 处理集群、分片、副本与运维（快照、升级）

## How to use this skill

1. **API**：PUT index、POST _doc、GET _search；query DSL 与 aggregations；reindex、_bulk。
2. **环境**：单节点或集群；版本与 Kibana/Logstash 配套；认证与 TLS。
3. **运维**：分片与副本数规划；快照与恢复；监控集群健康与慢查询。

## Best Practices

- mapping 设计好分词与类型；避免动态映射导致冲突。
- 查询用 filter 缓存与合适 size；大结果用 scroll 或 search_after。
- 生产用副本与快照；安全与权限配置完善。

## Keywords

elasticsearch, search, index, 搜索引擎, 全文检索, 聚合
