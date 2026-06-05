# Redis 内存优化深度指南

## 1. 内存模型

```
Redis 内存构成:
┌─────────────────────────────────┐
│ 数据内存 (key + value)           │ ← 主要部分
│ 元数据 (dict entry/robj)         │ ← 每个 key 约 64 字节开销
│ 缓冲区 (client/复制/AOF)         │
│ 自身 (代码/栈)                   │
└─────────────────────────────────┘
```

## 2. 编码优化 — 选择最省内存的数据结构

| 数据结构 | 小数据编码 | 省内存机制 | 阈值配置 |
|---------|-----------|-----------|---------|
| Hash | ziplist | 连续内存块，无指针开销 | `hash-max-ziplist-entries 512`<br>`hash-max-ziplist-value 64` |
| ZSet | ziplist | 同上 | `zset-max-ziplist-entries 128`<br>`zset-max-ziplist-value 64` |
| Set | intset | 整数数组，连续内存 | `set-max-intset-entries 512` |
| List | quicklist | ziplist 链表节点 | `list-max-ziplist-size -2`<br>`list-compress-depth 0` |

## 3. 内存优化 10 大技巧

### 3.1 用 Hash 替代 String 存对象

```redis
# 坏: 每个字段一个 key (大量元数据开销)
SET user:1001:name "Alice"
SET user:1001:age 30
SET user:1001:email "alice@example.com"
# 内存: 3 × (37+key_overhead) ≈ 300 字节

# 好: 一个 Hash 存所有字段
HSET user:1001 name "Alice" age 30 email "alice@example.com"
# 内存: ~160 字节 (节省 ~50%)
```

### 3.2 合理设置过期时间

```bash
# 不使用过期 = 内存只增不减
# 最佳实践: 每个 key 都设 TTL
SET cache:xxx value EX 3600

# 批量设置随机 TTL 避免雪崩
SET cache:a value EX $(( 300 + RANDOM % 60 ))
```

### 3.3 短 key 命名

```redis
# 坏: 超长 key 名
SET "user:profile:data:by:user:id:1001:preferences" value

# 好: 短 key 名
SET u:1001:pref value
# 节省: 每个 key 减少数十字节, 百万 key 节省数十 MB
```

### 3.4 使用小数据类型

```redis
# 统计在线用户数
# 坏: Set 存储所有用户ID
SADD online:users 1001  # 每个 member 约 60+ 字节

# 好: Bitmap 按位存储 (每个用户 1 bit)
SETBIT online:2024-01-15 1001 1  # 仅 1 位

# 统计 UV
# 坏: Set 存储所有访问用户 (大数据量)
# 好: HyperLogLog (单 key 仅 12KB)
PFADD visits:2024-01-15 "user1" "user2"
```

### 3.5 压缩大 Value

```python
import zlib
import json

# 存储前压缩
data = json.dumps(large_object)
compressed = zlib.compress(data.encode())
redis.set("large:key", compressed)

# 读取后解压
compressed = redis.get("large:key")
data = json.loads(zlib.decompress(compressed))
```

## 4. 内存监控与调优

```bash
# 查看内存使用
redis-cli INFO MEMORY

# 关键指标解读
used_memory_human: 4.00G       # 已用内存
used_memory_peak_human: 6.00G  # 峰值 (需关注)
used_memory_rss_human: 5.50G   # 系统分配内存 (含碎片)
mem_fragmentation_ratio: 1.37   # 碎片率 (>1.5 需处理)

# 找到大 key
redis-cli --bigkeys

# 查看 key 的精确内存占用
redis-cli MEMORY USAGE user:1001

# 查看 key 的编码
redis-cli OBJECT ENCODING user:1001
redis-cli OBJECT IDLETIME user:1001
```

## 5. 内存淘汰策略选择

| 策略 | 适用场景 | 示例配置 |
|------|---------|---------|
| allkeys-lru | 通用缓存，访问时间间隔模式 | `maxmemory-policy allkeys-lru` |
| volatile-lru | 部分 key 持久化部分做缓存 | `maxmemory-policy volatile-lru` |
| allkeys-lfu | 访问频率差异大的场景 | `maxmemory-policy allkeys-lfu` |
| allkeys-random | 缓存键命中率均匀 | `maxmemory-policy allkeys-random` |
| volatile-ttl | 优先保留过期时间短的 | `maxmemory-policy volatile-ttl` |

```bash
# 最佳生产配置: 4GB 内存 + LRU 淘汰
maxmemory 4gb
maxmemory-policy allkeys-lru
```

## 6. 内存碎片处理

```bash
# 检查碎片率
redis-cli INFO | grep mem_fragmentation_ratio

# 自动碎片整理 (Redis 4.0+)
CONFIG SET activedefrag yes
CONFIG SET active-defrag-threshold-lower 10
CONFIG SET active-defrag-threshold-upper 100
CONFIG SET active-defrag-ignore-bytes 100mb
CONFIG SET active-defrag-cycle-min 5
CONFIG SET active-defrag-cycle-max 75

# 手动 (高碎片率时)
redis-cli MEMORY PURGE
# 如仍高，需重启 Redis 节点
```
