# 示例: 集群监控实战

## 场景

日常运维需要监控 Elasticsearch 集群的健康状态、性能指标和资源使用情况。

## 1. 集群健康检查

### 快速健康状态

```bash
# 绿色 = 全部正常, 黄色 = 副本未分配, 红色 = 主分片丢失
GET /_cluster/health?pretty
```

```json
{
  "cluster_name": "production",
  "status": "yellow",
  "timed_out": false,
  "number_of_nodes": 5,
  "number_of_data_nodes": 3,
  "active_primary_shards": 125,
  "active_shards": 240,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 10,
  "delayed_unassigned_shards": 0,
  "active_shards_percent_as_number": 96.0
}
```

**解读**：unassigned_shards=10, active_shards_percent=96% → 有副本未分配。检查节点是否宕机。

### 详细健康诊断

```bash
# 查看所有未分配分片的原因
GET /_cluster/allocation/explain?pretty

# 重点关注字段:
# - current_node: 当前所在节点
# - can_remain_on_current_node: 能否保留
# - can_rebalance_cluster: 能否再平衡
# - node_decision: 节点决策
```

## 2. 节点监控

### 节点概览

```bash
# 节点角色和资源使用
GET /_cat/nodes?v&h=name,node.role,heap.percent,ram.percent,cpu,load_1m,disk.used_percent,master

# 示例输出:
# name     node.role heap.percent ram.percent cpu load_1m disk.used_percent master
# master-1 m                  42          35   8     2.3               42 *
# data-1   d                  67          72  35    12.5               56 -
# data-2   d                  55          60  28     9.8               52 -
# coord-1  -                  48          45  15     4.1               38 -
```

**告警阈值**：
- heap.percent > 85 → GC 压力大
- cpu > 80 → 需要扩容
- disk.used_percent > 85 → 需要清理或 ILM

### 热点线程排查 (CPU 突增)

```bash
# 当集群 CPU 突然飙高时
GET /_nodes/hot_threads

# 返回每个节点的热点线程堆栈
# 重点关注:
# - bulk 线程 → 写入压力大
# - search 线程 → 查询压力大
# - merge 线程 → 段合并 (大批量写入后)
# - GC 线程 → 内存问题
```

### 节点统计

```bash
# 获取节点级别详细统计
GET /_nodes/stats/indices,os,process,jvm,fs,transport,http

# 关注指标:
# - indices.indexing: 写入速率
# - indices.search: 查询速率
# - jvm.mem.heap_used_percent: 堆内存使用
# - jvm.gc.collectors.young.collection_time_in_millis: GC 时间
# - os.cpu.percent: CPU
# - fs.total.available_in_bytes: 磁盘空间
```

## 3. 索引监控

### 索引概览

```bash
# 查看所有索引的大小和文档数
GET /_cat/indices?v&h=index,docs.count,store.size,pri.store.size

# 查看索引分片分布
GET /_cat/shards?v

# 按大小排序
GET /_cat/indices?v&s=store.size:desc
```

### 段 (Segment) 监控

```bash
# 检查段的统计
GET /my_index/_segments

# 查看各索引段数
GET /_cat/segments?v&h=index,shard,segment,size,committed,search
```

**段过多 (>100)** 表示需要 force_merge：`POST /my_index/_forcemerge?max_num_segments=1`

## 4. 性能监控脚本

### Shell 健康检查脚本

```bash
#!/bin/bash
# es_health_check.sh
ES_HOST="http://localhost:9200"

# 集群健康
echo "=== 集群健康 ==="
curl -s "$ES_HOST/_cluster/health?pretty" | python3 -c "
import json, sys
h = json.load(sys.stdin)
print(f'状态: {h[\"status\"]}')
print(f'节点: {h[\"number_of_nodes\"]} (数据节点: {h[\"number_of_data_nodes\"]})')
print(f'活跃分片: {h[\"active_shards\"]}/{h[\"active_primary_shards\"]}p')
print(f'未分配: {h[\"unassigned_shards\"]}')
print(f'活跃率: {h[\"active_shards_percent_as_number\"]:.1f}%')
"

# 节点资源
echo -e "\n=== 节点资源 ==="
curl -s "$ES_HOST/_cat/nodes?v&h=name,node.role,heap.percent,cpu,load_1m,disk.used_percent"

# 索引 TOP 10 大索引
echo -e "\n=== TOP 10 大索引 ==="
curl -s "$ES_HOST/_cat/indices?v&h=index,docs.count,store.size&s=store.size:desc&limit=10"

# JVM 堆内存 Top 节点
echo -e "\n=== JVM 内存 (Top 5) ==="
curl -s "$ES_HOST/_nodes/stats/jvm" | python3 -c "
import json, sys
nodes = json.load(sys.stdin)['nodes']
for node_id, info in sorted(nodes.items(), key=lambda x: x[1]['jvm']['mem']['heap_used_percent'], reverse=True)[:5]:
    name = info['name']
    mem = info['jvm']['mem']
    gc = info['jvm']['gc']['collectors']
    print(f'{name}: heap={mem[\"heap_used_percent\"]}%  old_gc={gc[\"old\"][\"collection_count\"]}次({gc[\"old\"][\"collection_time_in_millis\"]//1000}s)')
"
```

## 5. 告警规则建议

| 指标 | 警告阈值 | 严重阈值 | 检查间隔 |
|------|---------|---------|---------|
| cluster health status | yellow > 5min | red | 1min |
| heap usage | > 80% | > 90% | 1min |
| CPU | > 70% | > 85% | 5min |
| disk usage | > 80% | > 90% | 1min |
| unassigned shards | > 0 | > 5 | 1min |
| search latency P99 | > 1s | > 5s | 5min |
| indexing latency P99 | > 500ms | > 2s | 5min |
| GC old gen count | > 5/min | > 10/min | 1min |

## 6. Kibana 监控配置

```yaml
# 启用 Kibana 监控 UI (Stack Monitoring)
# Management → Stack Monitoring
# 可查看:
# - 集群概览 (节点/索引/分片)
# - 节点 CPU/内存/磁盘/IO
# - 索引搜索/写入速率
# - GC 统计
# - 慢查询 Top N
```

## 性能排查清单

```
1. 是否 Yellow/Red → 检查未分配分片 (allocation/explain)
2. CPU 高 → hot_threads 排查
3. 查询慢 → Profile API + 慢查询日志
4. 写入慢 → 检查 refresh_interval + Bulk 优化
5. 磁盘满 → ILM 清理 + force_merge
6. GC 频繁 → 减少分片/字段, 增加堆内存
7. Segments 多 → force_merge (只读索引)
8. 深度分页 → 改用 search_after
```
