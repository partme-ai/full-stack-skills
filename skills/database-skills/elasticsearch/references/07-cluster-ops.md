# 集群运维

## 节点类型

| 类型 | 角色 | 职责 | 推荐配置 |
|------|------|------|---------|
| **Master** | `[master]` | 集群管理、元数据、选主 | 3 个专用, 4C 8G |
| **Data** | `[data]` | 存储数据、查询/聚合 | N 个, 8C 32G+ SSD |
| **Ingest** | `[ingest]` | 数据预处理管道 | 日志量大时可用 |
| **Coordinating** | `[]` | 请求分发、结果合并 | 大查询场景, 8C 32G+ |

**生产环境推荐**：3 个专用 Master + N 个 Data + 2 个 Coordinating。

## 发现与选主

```yaml
# elasticsearch.yml
discovery.seed_hosts: ["node1:9300", "node2:9300", "node3:9300"]
cluster.initial_master_nodes: ["node1", "node2", "node3"]
```

**防脑裂**：专用 Master 节点、奇数个 (≥3)、堆内存 ≤50% 物理内存。

## 分片分配与再平衡

```bash
# 查看分片分配
GET /_cat/shards?v

# 延迟分片分配 (重启节点时)
PUT /_all/_settings
{
  "settings": {
    "index.unassigned.node_left.delayed_timeout": "5m"
  }
}

# 取消再平衡 (维护时)
PUT /_cluster/settings
{
  "transient": {
    "cluster.routing.rebalance.enable": "none"
  }
}

# 重新路由
POST /_cluster/reroute
{
  "commands": [
    {
      "move": {
        "index": "my_index",
        "shard": 0,
        "from_node": "node-1",
        "to_node": "node-2"
      }
    }
  ]
}
```

## 快照与恢复 (Snapshot/Restore)

```bash
# 1. 注册快照仓库
PUT /_snapshot/my_backup
{
  "type": "s3",
  "settings": {
    "bucket": "my-es-backups",
    "region": "us-east-1",
    "base_path": "elasticsearch/backups"
  }
}

# 2. 创建快照
PUT /_snapshot/my_backup/snapshot_20240101
{
  "indices": "logs-*,products",
  "ignore_unavailable": true,
  "include_global_state": true
}

# 3. 查看状态
GET /_snapshot/my_backup/snapshot_20240101/_status

# 4. 恢复
POST /_snapshot/my_backup/snapshot_20240101/_restore
{
  "indices": "products",
  "rename_pattern": "(.+)",
  "rename_replacement": "restored_$1"
}

# 5. SLM 自动管理
PUT /_slm/policy/daily_snapshot
{
  "name": "<daily-snap-{now/d}>",
  "repository": "my_backup",
  "schedule": "0 30 1 * * ?",
  "retention": {
    "expire_after": "30d",
    "min_count": 5,
    "max_count": 50
  }
}
```

## ILM — 索引生命周期管理

```json
PUT /_ilm/policy/logs_policy
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_size": "50GB",
            "max_age": "1d",
            "max_docs": 5000000
          }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "shrink": { "number_of_shards": 1 },
          "forcemerge": { "max_num_segments": 1 },
          "allocate": { "require": { "box_type": "warm" } }
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": {
          "searchable_snapshot": {
            "snapshot_repository": "my_backup"
          }
        }
      },
      "delete": {
        "min_age": "365d",
        "actions": { "delete": {} }
      }
    }
  }
}
```

**生命周期**：hot (热节点 SSD) → warm (温节点 HDD) → cold (可搜索快照) → delete。

## 监控命令

```bash
# 集群健康
GET /_cluster/health?pretty

# 节点信息
GET /_cat/nodes?v&h=name,node.role,heap.percent,ram.percent,cpu,load_1m,master

# 索引信息
GET /_cat/indices?v&h=index,docs.count,store.size,pri.store.size
GET /_cat/shards?v

# 热点线程 (排查 CPU 突增)
GET /_nodes/hot_threads

# 待处理任务
GET /_cat/pending_tasks

# 节点统计
GET /_nodes/stats/indices,os,process,jvm,fs,transport,http

# 任务管理
GET /_tasks?detailed&actions=*byquery
POST /_tasks/<task_id>/_cancel
```

## 性能优化

### 分片黄金法则

- 每个分片 20-50GB (最佳)
- 每 GB 堆内存 20-25 个分片 (含副本)
- 案例: 1TB → 20-25 主分片 × 1 副本 = 40-50 总分片

### 写入优化

1. 关闭 refresh (`refresh_interval: -1`)
2. 增加 translog 同步间隔 (`30s`)
3. Bulk API (5-15MB/批)
4. 副本数设为 0 (写完恢复)
5. 合理 mapping (关闭 norms 等)

### 查询优化

- filter 优先 (可缓存, 不贡献算分)
- 避免 script 查询
- search_after 替代深度 from+size
- 限制 _source 返回字段

### 慢查询日志

```bash
PUT /_settings
{
  "index.search.slowlog.threshold.query.warn": "2s",
  "index.search.slowlog.threshold.query.info": "500ms",
  "index.search.slowlog.threshold.fetch.warn": "1s",
  "index.indexing.slowlog.threshold.index.warn": "10s"
}
```

### Profile API

```bash
GET /products/_search
{
  "profile": true,
  "query": {
    "match": { "title": "手机" }
  }
}
```
