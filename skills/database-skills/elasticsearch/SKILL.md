---
name: elasticsearch
description: Provides comprehensive guidance for Elasticsearch including indexing, mappings, query DSL, aggregations, analyzers, cluster management, and ELK Stack integration. Use when the user asks about Elasticsearch, needs to implement search functionality, work with Elasticsearch queries, or manage Elasticsearch clusters.
license: Complete terms in LICENSE.txt
---

# Elasticsearch — 分布式搜索与分析引擎

Elasticsearch 是基于 Apache Lucene 的分布式搜索和分析引擎，提供近实时的全文搜索、结构化搜索、聚合分析、地理空间查询和向量搜索能力。

## Workflow — 从数据到搜索的 5 步决策流程

```
遇到 ES 相关需求时按以下顺序决策:

Step 1: 明确场景
├── 全文搜索?                    → Step 2
├── 结构化数据分析 (日志/指标)?   → Step 2
├── 向量/KNN 搜索?               → references/ 向量搜索
├── 地理空间查询?                 → references/ 地理查询
├── 集群运维/性能问题?             → references/ 07-cluster-ops
└── 数据管道/日志采集?             → references/ 08-elk-integration

Step 2: 设计索引 (Mapping + Analyzer)
├── 确定字段类型 (text/keyword/date/geo/nested…)
├── 选择分词器 (standard/ik/pinyin/自定义)
├── 规划主分片数 (每个分片 20-50GB), 建后不可改
└── 设置别名用于零停机重建

Step 3: 写入数据
├── Index API (单条), Bulk API (批量, 5-15MB/批)
├── _update (部分更新), _update_by_query (条件更新)
└── Logstash/Filebeat (日志采集管道)

Step 4: 构建查询
├── 全文搜索: match / multi_match / query_string
├── 精确过滤: term / terms / range / exists / bool filter
├── 复合查询: bool (must/should/filter/must_not)
├── 聚合分析: terms + avg → references/ 聚合专题
└── 排序/分页: sort / search_after (深度分页) / scroll (导出)

Step 5: 持续优化
├── 性能问题?  → Profile API + 慢查询日志
├── 数据增长?  → ILM + Rollover 自动化 (references/ 07-cluster-ops)
├── Mapping 变更? → Reindex + Alias 零停机 (examples/03)
└── 查询优化?  → filter 优先 query, 避免 script, 限制 _source
```

## When to Use / When NOT to

| ✅ 使用 ES | ❌ 不要用 ES |
|-----------|-------------|
| **全文搜索** — 商品/文章/文档关键词搜索 | **复杂事务** — 需要 ACID/多表 JOIN, 选 PostgreSQL |
| **日志/指标分析** — ELK Stack 日志场景 | **键值缓存** — 简单 KV 查询, 选 Redis |
| **搜索型应用** — 电商/知识库/文档管理 | **强 Schema 约束** — 需要外键/触发器, 选 RDBMS |
| **聚合/仪表盘** — 实时统计 + Kibana 可视化 | **海量文档存储无需搜索** — 选 MongoDB |
| **地理空间查询** — 附近的人/POI/地理围栏 | **纯 OLAP 分析** — PB 级离线分析, 选 ClickHouse |
| **向量搜索** — 语义相似度/RAG 检索 | **消息队列** — 选 Kafka/Pulsar |

**核心原则**：Elasticsearch 是搜索服务器，不是关系型数据库的替代品。

## Boundary — 能力边界

| ✅ 完全适用 | ⚠️ 有条件适用 | ❌ 不适用 |
|-----------|--------------|---------|
| 全文搜索、模糊搜索、相关性排序 | 强一致性（ES 是近实时，默认 1s refresh） | 代替关系型数据库做核心业务存储 |
| 日志/指标聚合分析 (Kibana) | 秒级以下数据可见性（需调 refresh_interval） | 复杂 JOIN 查询（ES 有有限 nested 支持）|
| 地理空间、自动补全、搜索建议 | 极高写入量（需调优线程池和批量写入） | ACID 事务保证 |
| 文档搜索、知识库、RAG 检索 | 50+ 节点大集群（需专用协调节点） | 存储二进制大文件（存 OSS 路径） |
| 时序数据 + ILM 滚动 | PB 级深度分页（需 search_after / PIT） | 强关联约束数据模型 |
| 向量搜索 (dense_vector + KNN) | 自定义分词器（需先测试分析效果） | 替代 Kafka 做消息队列 |

## 核心概念速查

| 概念 | ES 术语 | 关系型 DB 类比 | 关键说明 | 深度参考 |
|------|---------|---------------|---------|---------|
| **Index** | 索引 | Table | 存储文档的逻辑命名空间，名称必须小写 | references/05 |
| **Document** | 文档 | Row | JSON 格式基本数据单元，不可变（update = delete+index） | — |
| **Shard** | 分片 | Partition | 水平切分单元，主分片数建后不可改，推荐 20-50GB/分片 | references/07 |
| **Replica** | 副本 | Replica | 冗余副本提供高可用和读扩展，可动态调整 | references/07 |
| **Mapping** | 映射 | Schema | 定义字段类型和分词配置，已有字段类型不可修改 | references/05 |
| **Analyzer** | 分词器 | — | text 字段必须配置，决定搜索质量 | references/06 |

## 查询 DSL 速查

| 查询类别 | 核心查询 | 用途 | 深度参考 |
|---------|---------|------|---------|
| **全文查询** | match / match_phrase / multi_match / query_string | 文本分词搜索、短语匹配、多字段搜索 | references/01 |
| **精确查询** | term / terms / range / exists / ids | keyword 字段精确匹配、范围过滤、存在检查 | references/02 |
| **复合查询** | bool (must/filter/should/must_not) | 90% 搜索需求可用 bool 实现 | references/02 |
| **嵌套/父子** | nested / has_child / has_parent | 对象内跨字段关联、父子关系查询 | references/02 |
| **地理查询** | geo_distance / geo_bounding_box / geo_shape | 附近查询、矩形区域、复杂地理形状 | 见 geospatial 技能 |
| **向量查询** | knn 参数 / k-NN 插件 | 语义相似度、RAG 检索 | references/05 |
| **特殊查询** | fuzzy / wildcard / regexp / script / percolate | 模糊纠错、通配符、脚本、反向搜索 | references/02 |

## 聚合速查

| 聚合类型 | 核心聚合 | 类似 SQL | 深度参考 |
|---------|---------|---------|---------|
| **指标聚合** | avg / sum / min / max / stats / cardinality / percentiles | AVG / SUM / COUNT(DISTINCT) / PERCENTILE | references/03 |
| **桶聚合** | terms / date_histogram / histogram / range / filters | GROUP BY / 日期分组 / 区间分组 / 过滤分组 | references/04 |
| **管道聚合** | derivative / moving_fn / bucket_script / bucket_selector | 环比 / 移动平均 / 子聚合计算 / HAVING | references/04 |

## 集群运维概述

| 运维领域 | 关键要点 | 深度参考 |
|---------|---------|---------|
| **节点类型** | Master(3个专用) + Data(SSD) + Coordinating(大查询) | references/07 |
| **分片管理** | 分配/再平衡/reroute/延迟分配 | references/07 |
| **快照备份** | S3/FS/GCS 仓库, SLM 自动管理, 增量快照 | references/07 |
| **ILM 生命周期** | hot → warm → cold → frozen → delete 自动化 | references/07 |
| **监控命令** | _cluster/health, _cat/nodes, _cat/shards, hot_threads | references/07 |
| **安全** | RBAC 角色, 字段/文档级安全, TLS, API Key | references/07 |

## Gotchas — 常见陷阱与反模式

| # | 陷阱 | 问题 | 解决方案 |
|---|------|------|---------|
| 1 | `term` 查询 `text` 字段 | text 被分词，找不到精确值 | 用 `match` 或 `.keyword` 子字段 |
| 2 | `from+size` 深度分页 | 越深越慢直至 OOM (限制 10000) | 深翻页用 `search_after`，导出用 `scroll`/PIT |
| 3 | 建索引后改主分片数 | 建后不可修改 | 提前规划，或重建索引 (reindex) |
| 4 | 所有字段用 `text` | 聚合/排序报错 | text + keyword 多字段 |
| 5 | 依赖动态映射 | 时间戳被识别为 long 等 | 生产环境显式 mapping |
| 6 | 嵌套对象用普通查询 | 跨字段关联条件误匹配 | 必须用 `nested` 查询 |
| 7 | 分片过多或过少 | 过多→管理开销大，过少→无法扩展 | 每个分片 20-50GB |
| 8 | 大批量写入不做优化 | 频繁 refresh 产生大量小段 | 关闭 refresh (-1), Bulk API, 副本=0 |
| 9 | 忽略 filter 缓存 | 重复计算，性能差 | 不需要算分的条件放 filter |
| 10 | wildcard/regexp 前缀搜索 | 不利用倒排索引，性能极差 | 用 `prefix` 或 edge_ngram |
| 11 | 脚本查询滥用 | 不可缓存，性能差，调试困难 | 用 ingest pipeline 预处理 |
| 12 | 集群角色不做分离 | Master 因 Data GC 失联 | 专用 3 个 Master 节点 |
| 13 | 日志索引无 ILM | 索引无限增长 | ILM 自动化滚动/压缩/删除 |
| 14 | 忽略 `ignore_above` | keyword 超长导致索引失败 | 设置 `ignore_above: 256` |
| 15 | 在 text 字段开 `fielddata` | 内存消耗大 | 用 `.keyword` 多字段替代 |

## FAQ

**Q1: ES 是关系型数据库的替代品吗？**
不是。ES 是搜索服务器，不支持 ACID 事务、外键、复杂 JOIN。正确架构：业务数据存 RDBMS，ES 做搜索和聚合。

**Q2: 数据写入后多久能查到？**
近实时。写入先到 buffer，默认 1s refresh 后才可搜索。可调 `refresh_interval` 或加 `?refresh` 参数。

**Q3: text 和 keyword 字段区别？**
text：分词后索引，支持 match 搜索，不支持排序/聚合。keyword：完整值索引，支持 term 搜索、排序、聚合。

**Q4: 主分片数为什么不能修改？**
路由规则 `hash(_id) % shards`，修改后已有数据无法定位。变更需 reindex。

**Q5: 如何选择分片数？**
每个分片 20-50GB。500GB 原始数据 → 10-25 个主分片。每个节点 ≤25 分片/GB 堆内存。

**Q6: ES 为什么搜索快？**
倒排索引：将每个词项映射到文档列表，查找直接定位。加分片并行 + filter 缓存。

**Q7: 聚合 (Aggregation) 是什么？**
Bucket = GROUP BY 分组，Metric = AVG/SUM/COUNT，Pipeline = 聚合结果的再分析。详见 references/03, references/04。

**Q8: Green/Yellow/Red 状态？**
Green=全正常，Yellow=主分片正常但副本未分配，Red=主分片丢失。

**Q9: 如何零停机重建索引？**
Alias + Reindex：创建新索引 → Reindex 数据 → 原子切换 Alias → 删除旧索引。见 examples/03。

**Q10: ES 和 Solr 怎么选？**
ES 集群管理内置、近实时搜索 1s、聚合强大、ELK 生态完整。Solr 依赖 ZK，配置复杂。

**Q11: Mapping 可以修改吗？**
可新增字段，不可修改已有字段类型（如 text→keyword），需重建索引。

**Q12: search_after 和 from+size 区别？**
from+size 深度分页 OOM（限制 10000）。search_after 基于排序值翻页，性能与深度无关。

**Q13: 数据备份怎么做？**
Snapshot API 备份到 S3/GCS/FS。推荐 SLM 自动管理。增量快照只存变化。

**Q14: 查询慢如何排查？**
Profile API → 慢查询日志 → filter vs query → segments 数量 → GC 日志。

**Q15: ILM 能解决什么问题？**
自动滚动（大小/时间阈值）、自动迁移（热→温→冷）、自动压缩、自动删除。

## Keywords

elasticsearch, ES, 搜索引擎, 全文搜索, 倒排索引, Lucene, index, mapping, document, shard, replica, analyzer, ik, pinyin, 查询 DSL, match, term, bool, filter, range, multi_match, query_string, nested, geo, aggregation, 聚合, terms, date_histogram, avg, sum, cardinality, percentiles, pipeline, reindex, bulk, scroll, search_after, ILM, rollover, force_merge, alias, snapshot, cluster, ELK, Logstash, Kibana, Filebeat, KNN, dense_vector, 向量搜索, painless, ingest pipeline, RBAC, profile API, 慢查询, zero downtime

## References

- references/01-query-dsl-fulltext.md — 全文查询（match/multi_match/query_string）
- references/02-query-dsl-term.md — 精确查询与复合查询（term/range/bool）
- references/03-aggregations-metric.md — 指标聚合（avg/sum/stats/cardinality/percentiles）
- references/04-aggregations-bucket.md — 桶聚合（terms/date_histogram/range）
- references/05-mapping-types.md — 映射与字段类型详解
- references/06-analyzers.md — 分词器（标准/IK/pinyin/自定义）
- references/07-cluster-ops.md — 集群运维（分片/监控/快照/ILM）
- references/08-elk-integration.md — Logstash/Filebeat/Kibana 配置
- examples/01-fulltext-search.md — 全文搜索实战
- examples/02-aggregation-report.md — 聚合报表实战
- examples/03-reindex-zero-downtime.md — 零停机重建索引
- examples/04-cluster-monitoring.md — 集群监控实战
