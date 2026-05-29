---
name: redis
description: Provides comprehensive guidance for Redis including data structures (string/hash/list/set/zset/geo/hyperloglog/bitmap/stream), common commands with examples, caching patterns, persistence (RDB/AOF), replication & sentinel, cluster, Lua scripting, transactions, pub/sub, pipelining, security hardening, and production best practices. Use when the user asks about Redis, needs to implement caching, choose Redis data structures, configure persistence or cluster, or troubleshoot Redis performance.
license: Complete terms in LICENSE.txt
---

# Redis — 内存数据结构存储系统

Redis（Remote Dictionary Server）是一个开源的内存数据结构存储系统，用作数据库、缓存和消息代理。

## Workflow — 使用流程

```
遇到 Redis 相关需求时，按以下顺序决策:

Step 1: 明确场景
├── 缓存加速?     → 转到 Step 2
├── 数据结构存储? → 转到 Step 2
├── 消息队列?     → 转到 1.7 Stream 章节
├── 分布式锁?     → 转到 2.4 分布式锁
├── 高可用/集群?  → 转到 4. 高可用架构
└── 性能问题?     → 转到 6. 性能优化

Step 2: 选择数据结构
├── 简单键值 / 计数器 / Session → String
├── 对象存储 (多字段)           → Hash
├── 队列 / 时间线 / 日志        → List
├── 标签 / 社交关系 / 去重      → Set
├── 排行榜 / 延时队列 / 范围查询 → ZSet
├── 签到 / 在线状态 / 布隆过滤   → Bitmap
├── UV 统计 / 去重计数          → HyperLogLog
└── 附近的人 / 地理围栏         → Geo

Step 3: 确定持久化策略
├── 允许丢少量数据?      → RDB (默认配置)
├── 高数据安全要求?      → AOF appendfsync everysec
├── 最佳性价比?          → 混合持久化 (推荐)
└── 纯缓存 (不持久化)?   → 关闭持久化

Step 4: 部署架构
├── 单机 (<16GB, 可容忍宕机)   → 单机 + AOF
├── 主从 (读流量大)             → 主从复制
├── 高可用 (自动故障转移)       → Sentinel (3节点)
├── 水平扩展 (>单机内存)        → Cluster (6节点起)
└── 读写分离 + 高可用          → Sentinel + 读写分离
```

## When to Use (and When NOT to)

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| 需要极低延迟（<1ms）的键值存取 | 需要复杂 SQL 关联查询和事务性报表 |
| 热点数据缓存以减轻数据库压力 | 数据持久性要求超过内存可承受范围 |
| 高并发计数器（INCR/DECR） | 需要完整的 ACID 事务保证（用关系型数据库） |
| 排行榜/时间线/消息队列等数据结构场景 | 数据量远大于内存容量且不需要高速访问 |
| 分布式锁/限流/会话管理 | 已经使用成熟的分布式缓存中间件且不迁移 |
| 实时分析、地理位置搜索、UV 统计 | 需要数据之间强引用约束和外键 |

**核心原则：Redis 是内存数据库，不是关系型数据库替代品。**

## Boundary — 能力边界

| ✅ 完全适用 | ⚠️ 有条件适用 | ❌ 不适用 |
|------------|--------------|---------|
| 缓存加速、API 响应提速 | 强一致性要求场景（需配合 DB + 锁） | 代替关系型数据库作为唯一存储 |
| 计数器、排行榜、时间线 | Redis 作为消息队列（Stream 替代 Pub/Sub） | 复杂 SQL 查询和 JOIN |
| 分布式锁、限流、Session 存储 | 生产数据量 > 内存的场景（需 Cluster） | 存储大文件或二进制数据 |
| 实时排行榜、地理空间查询 | 作为主数据库存储核心业务事务 | 需要外键约束和引用完整性 |
| 去重统计（HyperLogLog/Bitmap） | 跨业务共享 Redis 实例（需 ACL 隔离） | 替代搜索引擎做全文搜索（用 RediSearch） |

**超出范围时**：请使用 PostgreSQL（关系型数据）、MongoDB（文档型）、Elasticsearch（全文搜索）、RabbitMQ/Kafka（消息队列）。

## When to trigger this skill

**ALWAYS use this skill when the user mentions:**
- "Redis", "缓存", "cache", "Session 存储", "分布式锁"
- "String", "Hash", "List", "Set", "ZSet", "Sorted Set", "Geo", "HyperLogLog", "Stream"
- "SET / GET / INCR /... (any Redis command)"
- "RDB", "AOF", "持久化", "Persistence"
- "主从", "Sentinel", "Cluster", "哨兵", "集群", "切片"
- "redis.conf", "redis-cli", "redis-benchmark"
- "Lua 脚本", "事务 / MULTI / EXEC", "Pipeline", "Pub/Sub"
- "缓存穿透", "缓存雪崩", "缓存击穿", "Big Key", "Hot Key"
- "Redis 性能优化", "慢查询", "内存淘汰"

---

## 1. Redis 核心数据结构与命令

### 1.1 数据结构选型速查表

| 数据结构 | 底层实现 | 最佳场景 | 复杂度 | 最大容量 |
|---------|---------|---------|-------|---------|
| **String** | SDS (Simple Dynamic String) | 缓存、计数器、Session、分布式锁 | O(1) | 512MB |
| **Hash** | ziplist / dict | 对象存储（用户、文章）、字段更新 | O(n) n为字段数 | 4294967295 字段 |
| **List** | quicklist | 消息队列、时间线、日志 | O(1) 头尾 | 4294967295 元素 |
| **Set** | intset / dict | 标签、社交关系、去重 | O(1) 增删查 | 4294967295 成员 |
| **ZSet** | ziplist / skiplist+dict | 排行榜、延时队列、范围查询 | O(log n) 跳表 | 4294967295 成员 |
| **Bitmap** | String 位操作 | 签到/活跃用户统计、布隆过滤 | O(1) 位操作 | 512MB (2^32位) |
| **HyperLogLog** | 概率数据结构 | UV 统计、去重计数 | O(1) | 12KB/键 (0.81%误差) |
| **Geo** | ZSet 封装 | 附近的人、地理围栏 | O(log n) | 同 ZSet |
| **Stream** | radix tree | 消息队列、事件溯源、消费组 | O(log n) | 4294967295 消息 |

### 1.2 String 命令与示例

```redis
# 基础操作
SET key "value"                    -- 设置值
SET key "value" EX 60              -- 设置值 + 60s 过期
SET key "value" NX                 -- 仅 key 不存在时设置 (分布式锁)
GET key                            -- 获取值
GETSET key "new"                   -- 设置新值返回旧值 (原子操作)
STRLEN key                         -- 获取字符串长度
APPEND key "suffix"                -- 追加

# 数字操作 (Redis 内部数字存储为字符串)
INCR counter                       -- 原子 +1 (自增)
INCRBY counter 10                  -- 原子 +10
DECR counter                       -- 原子 -1
DECRBY counter 5                   -- 原子 -5
INCRBYFLOAT price 1.5              -- 浮点数增加

# 批量操作
MSET k1 v1 k2 v2                   -- 批量设置 (非原子)
MGET k1 k2                         -- 批量获取
MSETNX k1 v1 k2 v2                 -- 仅当所有 key 都不存在时设置 (原子)

# 子串操作
GETRANGE key 0 -1                  -- 获取全部子串
SETRANGE key 6 "Redis"             -- 从偏移 6 覆写

# 带过期操作
SETEX key 3600 "value"             -- 设置值 + 秒级过期
PSETEX key 3000 "value"            -- 设置值 + 毫秒级过期
```

**String 编码选择**：值 ≤ 44 字节用 `embstr`（一次内存分配），> 44 字节用 `raw`（两次分配）。

### 1.3 Hash 命令与示例

```redis
HSET user:1001 name "Alice" age 30     -- 设置多字段
HGET user:1001 name                     -- 获取单字段
HMGET user:1001 name age                -- 获取多字段
HGETALL user:1001                       -- 获取所有字段 (慎用，大 key 场景阻塞)
HKEYS user:1001                         -- 获取所有字段名
HVALS user:1001                         -- 获取所有字段值
HDEL user:1001 age                      -- 删除字段
HEXISTS user:1001 name                  -- 检查字段是否存在
HLEN user:1001                          -- 字段数量
HINCRBY user:1001 score 10              -- 字段数值增加
HSETNX user:1001 email "a@b.com"        -- 仅字段不存在时设置
```

**Hash 编码选择**：字段数 < 512 且每个值长度 < 64 字节使用 `ziplist`（节省内存），否则升级为 `dict`（哈希表）。可配置 `hash-max-ziplist-entries` 和 `hash-max-ziplist-value`。

### 1.4 List 命令与示例

```redis
# 右进左出 (队列模式 - FIFO)
RPUSH queue "job1" "job2"              -- 右边推入一个或多个
LPOP queue                             -- 左边弹出

# 左进右出 (栈模式 - LIFO)
LPUSH stack "a" "b"                    -- 左边推入
RPOP stack                             -- 右边弹出

# 范围操作
LRANGE list 0 -1                       -- 获取全部元素
LINDEX list 0                          -- 获取指定索引元素
LLEN list                              -- 列表长度
LTRIM list 0 99                        -- 修剪保留前 100 个
LREM list 2 "value"                    -- 移除 2 个匹配的值
LSET list 0 "new"                      -- 设置指定索引的值
LINSERT list BEFORE "b" "a"            -- 在元素前插入

# 阻塞操作 (超时秒数，0 表示无限等待)
BLPOP queue 5                          -- 阻塞式左弹出，超时 5s
BRPOP queue 5                          -- 阻塞式右弹出
```

**List 编码选择**：元素数量或单个元素长度超阈值后从 `quicklist` 模式（ziplist 节点链表）转为 linkedlist。

**典型场景**：
- `LPUSH + LTRIM` = 固定长度最新消息列表
- `RPUSH + BLPOP` = 可靠消息队列
- `BRPOPLPUSH` = 安全队列（备份到 backup list）

### 1.5 Set 命令与示例

```redis
SADD tags "redis" "database"          -- 添加成员
SREM tags "database"                   -- 移除成员
SMEMBERS tags                          -- 获取所有成员 (慎用于大 set)
SISMEMBER tags "redis"                 -- 判断成员 O(1)
SCARD tags                             -- 成员数量

# 集合运算 (支持集合间操作)
SINTER set1 set2                       -- 交集
SUNION set1 set2                       -- 并集
SDIFF set1 set2                        -- 差集
SINTERSTORE dest s1 s2                 -- 交集存到新 key
SUNIONSTORE dest s1 s2                 -- 并集存到新 key
SDIFFSTORE dest s1 s2                  -- 差集存到新 key

# 随机操作
SRANDMEMBER key 3                      -- 随机返回 3 个成员 (不删除)
SPOP key 2                             -- 随机弹出 2 个成员 (删除)

SSCAN key 0 COUNT 100                  -- 渐进迭代 (避免阻塞)
```

### 1.6 ZSet (Sorted Set) 命令与示例

```redis
ZADD leaderboard 100 "player1" 200 "player2"  -- 添加成员及分数
ZREM leaderboard "player1"                    -- 移除成员
ZSCORE leaderboard "player1"                  -- 获取分数
ZCARD leaderboard                             -- 成员数量
ZINCRBY leaderboard 50 "player1"              -- 增加分数

# 按排名查
ZRANGE leaderboard 0 -1 WITHSCORES            -- 按分数从小到大 (加分差)
ZREVRANGE leaderboard 0 -1 WITHSCORES         -- 按分数从大到小 (排行榜)
ZRANK leaderboard "player1"                   -- 获取排名 (从小到大)
ZREVRANK leaderboard "player1"                -- 获取排名 (从大到小)

# 按分数范围查
ZRANGEBYSCORE salary 2000 5000                -- 按分数范围查询
ZREVRANGEBYSCORE salary 5000 2000             -- 按分数范围逆序
ZCOUNT salary 2000 5000                       -- 统计分数区间数
ZREMRANGEBYSCORE salary 0 1000                -- 移除分数区间成员

# 按字典序范围查
ZRANGEBYLEX words [a [z                      -- 字典序范围查询
ZLEXCOUNT words [a [z                        -- 统计字典序区间数
ZREMRANGEBYLEX words [a [z                   -- 移除字典序区间成员

# 集合运算
ZINTERSTORE dest 2 z1 z2                     -- 交集
ZUNIONSTORE dest 2 z1 z2                     -- 并集

ZSCAN leaderboard 0 COUNT 100                -- 渐进迭代
```

**ZSet 编码选择**：成员数 < 128 且所有值长度 < 64 字节时用 `ziplist`，否则用 `skiplist + dict`。

### 1.7 高级数据结构

```redis
# Bitmap — 位图
SETBIT sign:2024-01 100 1                    -- 用户 100 在 1月签到
GETBIT sign:2024-01 100                      -- 查询签到状态
BITCOUNT sign:2024-01                        -- 统计签到人数
BITOP AND dest sign:01 sign:02               -- 位运算 (AND/OR/NOT/XOR)

# HyperLogLog — 基数统计 (0.81% 误差)
PFADD visits:2024-01 "user1" "user2"         -- 添加元素
PFCOUNT visits:2024-01                       -- 近似去重计数
PFMERGE total visits:01 visits:02            -- 合并

# Geo — 地理位置
GEOADD cities 116.397 39.908 "北京"           -- 添加地标
GEODIST cities "北京" "上海" km               -- 计算两地距离
GEORADIUS cities 116.4 39.9 100 km           -- 查找 100km 内的位置
GEORADIUSBYMEMBER cities "北京" 500 km        -- 以成员为中心查找
GEOHASH cities "北京"                         -- 返回 geohash 字符串
GEOPOS cities "北京"                          -- 返回经纬度

# Stream — 消息流 (Redis 5.0+)
XADD mystream * sensor-id 1234 temp 19.8     -- 追加消息 (自动时间戳ID)
XLEN mystream                                 -- 消息长度
XRANGE mystream - +                           -- 范围查询
XREAD COUNT 10 STREAMS mystream 0            -- 读取消息
XGROUP CREATE mystream mygroup $              -- 创建消费组
XREADGROUP GROUP mygroup consumer1 COUNT 1 STREAMS mystream >  -- 消费
XACK mystream mygroup 1648123456789-0        -- 确认消息
```

---

## 2. 缓存模式与架构

### 2.1 缓存读取模式

```
Read-Through: 应用 → Redis → 数据库
               命中 ✓ 返回    未命中 ✗ 回源
```

```redis
# Cache-Aside (旁路缓存) — 最常用模式
GET cache_key        → 命中返回
                      → 未命中: 查 DB → SET cache_key value EX 3600 → 返回

# 伪代码
function get_user(user_id):
    user = redis.get("user:" + user_id)
    if user is None:
        user = db.query("SELECT * FROM users WHERE id=?", user_id)
        redis.setex("user:" + user_id, 3600, user)
    return user
```

### 2.2 缓存更新模式

| 模式 | 操作方法 | 并发安全 | 说明 |
|------|---------|---------|------|
| **Cache-Aside** | 更新 DB → 删除缓存 | ⚠️ 删除失败有脏数据 | 最通用，使用最广泛 |
| **Write-Through** | 更新 DB → 同步更新缓存 | ✅ 一致性高 | 写延迟增加，适合写少读多 |
| **Write-Behind** | 先写缓存 → 异步写 DB | ⚠️ 宕机可能丢数据 | 性能最佳，适合允许略丢数据的场景 |
| **Refresh-Ahead** | 缓存过期前自动刷新 | ✅ 无过期风暴 | 适合热点 key |

### 2.3 缓存三大问题

```
缓存穿透 (Cache Penetration)
├── 问题：查询一个不存在的数据，每次穿透到 DB
├── 后果：大量请求直接打到数据库，可能击垮 DB
├── 解决：
│   ├── ① 布隆过滤器 (Bloom Filter): 用 Bitmap 预判 key 是否存在
│   ├── ② 缓存空值: SET key "" EX 60 (短过期时间)
│   └── ③ 参数校验: 非法参数直接拒绝
└── 提示：推荐组合使用 ① + ②

缓存击穿 (Cache Breakdown / Hot Key)
├── 问题：热点 key 过期瞬间，高并发直接打到 DB
├── 后果：瞬间高并发，DB 扛不住
├── 解决：
│   ├── ① 互斥锁 (Mutex Lock): SETNX 争锁，只有一个线程回源
│   ├── ② 永不过期 + 异步刷新: 物理上不设 TTL，后台线程定时更新
│   └── ③ 热点 key 预留: 预估热点，预加载
└── 提示：互斥锁实现最简单，异步刷新性能最优

缓存雪崩 (Cache Avalanche)
├── 问题：大量缓存同时过期/Redis 宕机，流量直击 DB
├── 后果：DB 被击垮，服务雪崩
├── 解决：
│   ├── ① TTL 随机化: SET key EX (300 + random(0,60))
│   ├── ② 互斥锁: 同击穿方案
│   ├── ③ 双缓存: 主缓存 + 备份缓存
│   ├── ④ Redis 高可用: 主从 + Sentinel/Cluster
│   └── ⑤ 本地缓存 + Redis: 二级缓存 (guava/caffeine)
└── 提示：TTL 随机化是最低成本最高收益的预防措施
```

### 2.4 分布式锁

```redis
# 最简单的分布式锁 (单 Redis 实例)
SET lock:resource "uuid-value" NX EX 30       -- 加锁
-- 执行业务逻辑...
DEL lock:resource                                -- 释放锁

# 问题：误删其他线程的锁 → 需要 Lua 脚本保证原子性

# 正确的解锁 (Lua 脚本)
-- EVAL "if redis.call('get',KEYS[1])==ARGV[1] then return redis.call('del',KEYS[1]) else return 0 end" 1 lock:resource uuid-value

# Redlock 算法 (多实例场景)
# 1. 获取当前时间 T1
# 2. 向 N/2+1 个实例尝试加锁 (SET NX PX)
# 3. 用去时间 > 锁有效时间 → 加锁失败，向所有实例发送解锁
# 4. 使用 Redisson / Redlock-py 等客户端实现

# 最佳实践：使用 Redisson 等成熟客户端，不要自行实现
```

### 2.5 常见缓存 Key 设计规范

```
# 命名规范
cache:user:{id}           -- 用户缓存
cache:article:{id}        -- 文章缓存
lock:order:{order_id}     -- 分布式锁
rate:limit:ip:{ip}        -- 限流
session:{session_id}      -- Session

# 过期时间策略
- 通用原则: TTL = 业务可接受的脏数据时间 + random(0, TTL*1/5)
- 静态数据 (配置表): 1-24 小时
- 动态数据 (用户信息): 5-30 分钟
- 热点数据 (首页推荐): 1-5 分钟 + 异步刷新

# Big Key 应对
Big Key 指单个 key 存大量数据 (Hash 上百万字段 / List 千万级元素)
├── 问题：阻塞其他命令、内存不均、慢查询
├── 发现：redis-cli --bigkeys 扫描
├── 拆分：Hash → HASH_KEY:{mod(hash_field, 100)}
└── 替代：List → 改用 Stream + 消费组
```

---

## 3. 持久化

### 3.1 RDB (Redis Database) — 快照持久化

```
原理：定时将内存数据生成快照写入磁盘 (dump.rdb)
```

| 配置 | 说明 | 触发条件 |
|------|------|---------|
| `save 900 1` | 900s 内 ≥1 次写 | 自动 |
| `save 300 10` | 300s 内 ≥10 次写 | 自动 |
| `save 60 10000` | 60s 内 ≥10000 次写 | 自动 |
| `BGSAVE` | 后台 fork 子进程生成快照 | 手动 |
| `SAVE` | 主进程生成 (阻塞所有请求) | 手动 |

```
RDB 优势：文件紧凑，恢复快，适合备份和灾难恢复
RDB 劣势：可能丢失最后一次快照后的数据 (最长丢失一个 save 间隔)
```

### 3.2 AOF (Append Only File) — 日志持久化

```
原理：记录每次写操作命令，Redis 重启时回放
```

| `appendfsync` 选项 | 持久化策略 | 数据安全 | 性能影响 |
|-------------------|-----------|---------|---------|
| `always` | 每条命令 fsync | 最多丢 1 条 | 极低 (频繁磁盘写入) |
| `everysec` | 每秒 fsync | 最多丢 1s 数据 | 低 (推荐) |
| `no` | 操作系统决定 | 不可预测 | 高 |

**AOF 重写**：`BGREWRITEAOF` — 压缩 AOF 文件（将多个命令合并为最小集合）。
配置 `auto-aof-rewrite-percentage 100` 和 `auto-aof-rewrite-min-size 64mb` 自动触发。

```
AOF 优势：数据安全性高 (最多丢 1 秒数据)，文件易读
AOF 劣势：文件体积比 RDB 大，恢复比 RDB 慢
```

### 3.3 最佳选择：RDB + AOF 混合

Redis 4.0+ 支持混合持久化 (`aof-use-rdb-preamble yes`)：
- AOF 重写时先生成 RDB 快照写入 AOF 文件头部
- 后续增量写命令以 AOF 格式追加
- 重启恢复：先加载 RDB（快），再回放 AOF 增量（补全）

```
推荐生产配置：
┌─────────────────────────────────────────────┐
│ appendonly yes                              │
│ appendfsync everysec                        │
│ aof-use-rdb-preamble yes                    │
│ save 900 1                                  │
│ save 300 10                                 │
│ save 60 10000                               │
└─────────────────────────────────────────────┘
```

### 3.4 持久化对比总结

| 维度 | RDB | AOF | 混合 (RDB+AOF) |
|------|-----|-----|----------------|
| 数据完整性 | 可能丢失多 | 最多丢 1s | 最多丢 1s |
| 恢复速度 | 快 | 慢 | 快 |
| 文件大小 | 小 | 大 (可重写) | 中 |
| 实时性影响 | fork 开销 (内存翻倍) | 磁盘 I/O (可控) | 组合开销 |

---

## 4. 高可用架构

### 4.1 主从复制 (Replication)

```
┌─────────┐     复制流      ┌──────────┐
│ Master  │ ──────────────→ │ Replica  │
│ (写+读)  │                 │ (只读)   │
└─────────┘                 └──────────┘
```

**复制流程**：
```
1. Replica 发送 SLAVEOF master_ip master_port
2. Master BGSAVE 生成 RDB → 发送到 Replica
3. Replica 加载 RDB + 缓存增量命令
4. 后续持续增量复制 (基于环形缓冲区 repl_backlog)
5. 网络断开重连 → 部分重同步 (PSYNC2)
```

**核心配置**：
```conf
# master
replica-read-only no                     # Master 默认不设置只读

# replica
replicaof 192.168.1.100 6379             # 指定主节点
replica-read-only yes                    # 从节点只读
replica-priority 100                     # Sentinel 选主优先级 (越小越高)
```

**复制注意事项**：
- 主节点 fork 子进程执行 BGSAVE 时不阻塞读写（但 COW 机制会使内存翻倍）
- 从节点默认只读，可用于读流量分流
- 主节点崩溃后需手动切换从节点或使用 Sentinel

### 4.2 Sentinel (哨兵) — 自动故障转移

```
          ┌─────────────┐
          │  Sentinel-1  │
          └──────┬──────┘
                 │ 监控 + 协调
    ┌────────────┼────────────┐
    │            │            │
┌───▼───┐  ┌────▼────┐  ┌───▼───┐
│Master  │  │Replica-1│  │Replica-2│
└───────┘  └─────────┘  └─────────┘
```

**Sentinel 核心功能**：
```
1. 监控：PING 主从节点，判断是否下线
2. 通知：管理员或程序通过 API 获取状态变化
3. 故障转移：Master 挂了 → 选举新 Master
4. 配置提供：客户端请求获取当前 Master 地址
```

**部署要求**：最少 3 个 Sentinel 实例（奇数，保证 quorum）。

**sentinel.conf 配置**：
```conf
sentinel monitor mymaster 127.0.0.1 6379 2    # 监控主节点，2 个哨兵同意即判定下线
sentinel down-after-milliseconds mymaster 5000 # 5s 无响应判主观下线
sentinel failover-timeout mymaster 60000       # 故障转移超时
sentinel parallel-syncs mymaster 1             # 新主后同时多少个从同步
```

### 4.3 Cluster (集群) — 数据分片 + 高可用

```
        ┌──────────┐
        │  客户端   │
        └────┬─────┘
             │ 请求任意节点，MOVED 重定向
    ┌────────┼──────────────┐
    │        │              │
┌───▼───┐ ┌──▼───┐    ┌───▼───┐
│Node 1  │ │Node 2 │... │Node N  │
│ 0-5460 │ │5461-10922 │  │10923-16383│
│+Slave  │ │+Slave │  │+Slave  │
└────────┘ └───────┘    └───────┘
```

**核心概念**：
- 16384 个 hash slot：`CRC16(key) % 16384`
- 每个节点负责一段 slot 区间
- 节点间 gossip 协议通信（PONG/PING）
- 自动主从切换：主节点挂了，从节点晋升

**集群搭建要点**：
```bash
# 配置文件：(每个节点必须有集群模式)
cluster-enabled yes
cluster-config-file nodes-6379.conf
cluster-node-timeout 5000

# 创建集群 (Redis 5+)
redis-cli --cluster create 192.168.1.100:6379 192.168.1.101:6379 \
  192.168.1.102:6379 192.168.1.103:6379 192.168.1.104:6379 192.168.1.105:6379 \
  --cluster-replicas 1

# 常用操作
redis-cli --cluster check 192.168.1.100:6379    # 检查集群状态
redis-cli --cluster info 192.168.1.100:6379     # 集群信息
redis-cli --cluster rebalance 192.168.1.100:6379 # 重新平衡 slot
redis-cli --cluster add-node 新节点ip:port 已有节点ip:port --cluster-slave
```

**集群限制**：
- 只支持 0 号数据库（SELECT 0）
- 批量操作（MGET/MSET）的 key 必须在同一 slot（使用 hash tag `{user:1001}`）
- 事务/Lua 脚本的 key 必须在同一节点（同一 slot）
- 不支持多 key 操作在跨 slot 场景

### 4.4 架构选型决策树

```
数据量 < 单个节点内存 (≤16GB) ?
├── YES → 是否需要自动故障转移?
│         ├── NO  → 单机 + RDB/AOF
│         └── YES → 读写分离需要?
│                   ├── NO  → 主从 + Sentinel (3实例)
│                   └── YES → 主从 + Sentinel (读写分离)
│
└── NO → 数据量预期增长?
         ├── NO  → 升级单机内存 (垂直扩展)
         └── YES → Cluster 集群 (水平扩展)
                   ├── 三主三从 (最小生产配置)
                   ├── 六主六从 (中等规模)
                   └── 九主九从 (大规模)
```

---

## 5. Lua 脚本与事务

### 5.1 事务 (Transaction)

```redis
MULTI                              -- 开始事务
SET key1 "value1"                  -- 命令入队 (QUEUED)
SET key2 "value2"                  -- 命令入队
EXEC                               -- 按顺序执行所有命令

# WATCH — 乐观锁 (CAS 模式)
WATCH stock:100                    -- 监视 key
count = GET stock:100              -- 读取当前值
MULTI
SET stock:100 (count - 1)          -- 如果期间 stock:100 被修改 → EXEC 返回 nil
EXEC
UNWATCH                            -- 取消监视
```

**事务 vs Pipeline 对比**：

| 特性 | MULTI/EXEC (事务) | Pipeline (管道) |
|------|------------------|----------------|
| 原子性 | ✅ 全部/全部不执行 | ❌ 不保证 |
| 阻塞等待结果 | ✅ 是 | ✅ 是 |
| 中间可读结果 | ❌ 仅入队不可读 | ✅ 可读 |
| 错误处理 | 语法错全部失败/运行时错其他继续 | 每命令独立 |
| 适用场景 | 需要 "all or nothing" | 批量操作提升性能 |

### 5.2 Lua 脚本

Redis 2.6+ 内置 Lua 5.1 解释器，脚本在服务器端原子执行。

```lua
-- 原子扣减库存脚本
-- EVAL script 1 key arg
-- KEYS[1] = stock:100
-- ARGV[1] = 1 (扣减数量)

local stock = redis.call("GET", KEYS[1])
if not stock or tonumber(stock) < tonumber(ARGV[1]) then
    return -1  -- 库存不足
end
redis.call("DECRBY", KEYS[1], ARGV[1])
return redis.call("GET", KEYS[1])

-- 调用方式: EVAL "上述脚本" 1 stock:100 1
-- 缓存: SCRIPT LOAD "script" → SHA → EVALSHA SHA 1 stock:100 1
```

**Lua 脚本最佳实践**：
- 脚本应短小精悍（控制在 100 行内），长脚本会阻塞其他请求
- 使用 `SCRIPT LOAD` + `EVALSHA` 减少网络传输
- 脚本中所有 key 必须使用 KEYS 数组传入，不能用硬编码
- 脚本不要访问不同节点的 key（Cluster 场景）
- 使用 `redis.log(redis.LOG_WARNING, msg)` 调试

### 5.3 CAS (乐观锁) 模式

```lua
-- 更安全的库存扣减：数值检查 + 原子操作
local key = KEYS[1]
local expected = tonumber(ARGV[1])
local new_value = tonumber(ARGV[2])

local current = redis.call("GET", key)
if tonumber(current) ~= expected then
    return -1  -- 已被其他客户端修改
end
return redis.call("SET", key, new_value)
```

---

## 6. 性能优化与运维

### 6.1 内存淘汰策略 (maxmemory-policy)

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| `noeviction` | 不淘汰，写操作返回错误 | 数据库模式 (禁止丢数据) |
| `allkeys-lru` | 全 key 最近最少使用 | 通用缓存 (推荐) |
| `allkeys-lfu` | 全 key 最不经常使用 (Redis 4.0+) | 访问频率差异大的缓存 |
| `volatile-lru` | 有过期时间的 key LRU | 部分持久化、部分缓存 |
| `volatile-ttl` | 淘汰 TTL 最短的 key | 特定场景 |
| `volatile-random` | 随机淘汰有过期时间的 key | 不太推荐 |

```bash
redis-cli CONFIG SET maxmemory 4gb           # 设置最大内存
redis-cli CONFIG SET maxmemory-policy allkeys-lru  # LRU 淘汰
```

### 6.2 Big Key 与 Hot Key

**Big Key 检测**：
```bash
# 扫描大 key (阻塞，建议低峰期执行)
redis-cli --bigkeys

# 用 MEMORY USAGE 精确查看内存占用
redis-cli MEMORY USAGE mykey

# 用 DEBUG 命令 (Redis 4.0+)
redis-cli MEMORY DOCTOR
```

**Big Key 拆分策略**：
```
场景 1: Hash 包含上百万字段
→ 拆分: HASH_KEY:{hash(field) % 100} = {field: value}

场景 2: List 包含千万级元素
→ 替换为 Stream (支持消费组)

场景 3: ZSet 大排行榜
→ 分桶: ranking:2024-01, ranking:2024-02...

场景 4: String 存储大 JSON (>10MB)
→ 压缩存储: Snappy/LZ4 压缩后存，读取解压
```

**Hot Key 应对**：
```
问题：单个 key QPS 极高 (如 10万+/秒)
解决：
├── 本地缓存 (Local Cache): 二级缓存 (如 Caffeine)
├── 读写分离: 从节点分担读流量
├── 热点拆分: hotkey:{random(0,10)} = value (分片读取)
└── 代理层: Redis Proxy (如 Twemproxy/RedisShake)
```

### 6.3 慢查询日志

```bash
CONFIG SET slowlog-log-slower-than 10000     # 记录 >10ms 的命令
CONFIG SET slowlog-max-len 128               # 最多保留 128 条记录

SLOWLOG GET 10                               # 获取前 10 条慢查询
SLOWLOG LEN                                  # 慢查询总数
SLOWLOG RESET                                # 清空慢查询
```

### 6.4 性能基准与优化

```bash
# 基准测试
redis-benchmark -h 127.0.0.1 -p 6379 -c 50 -n 100000 -q
redis-benchmark -t set,get,incr,lpush -q    # 指定命令测试
redis-benchmark -P 10 -q                     # Pipeline 模式

# 预期性能 (单实例):
# GET/SET: 10万+ QPS (无持久化)
# Pipeline 100条: 100万+ QPS
# Lua 脚本: 5-15万 次/秒
```

**关键优化参数**：
```conf
tcp-backlog 511                           # TCP 连接队列
timeout 300                               # 客户端空闲超时
tcp-keepalive 300                         # TCP keepalive
lfu-log-factor 10                         # LFU 计数器对数因子 (Redis 4.0+)
lfu-decay-time 1                          # LFU 衰减时间
hz 10                                     # 后台任务频率 (可增加到 100)
```

### 6.5 安全加固

```bash
# 基础安全
requirepass your_strong_password           # 设置密码
RENAME_COMMAND FLUSHALL ""                 # 禁用危险命令
RENAME_COMMAND FLUSHDB ""
RENAME_COMMAND CONFIG ""
RENAME_COMMAND SHUTDOWN ""

# 网络安全
bind 127.0.0.1 192.168.1.100              # 绑定内网 IP
protected-mode yes                         # 保护模式
port 6379                                  # 修改默认端口

# 连接限制
maxclients 10000                           # 最大连接数
client-output-buffer-limit normal 0 0 0    # 客户端输出缓冲区限制
client-output-buffer-limit replica 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60

# ACL (Redis 6.0+)
ACL SETUSER alice on >password ~cached:* +get +set -admin
ACL SETUSER bob on >password ~* +@all -@dangerous
```

---

## 7. Redis 生态与客户端连接

### 7.1 客户端配置

```java
// Java (Jedis 连接池)
JedisPoolConfig config = new JedisPoolConfig();
config.setMaxTotal(100);           // 最大连接数
config.setMaxIdle(50);             // 最大空闲
config.setMinIdle(10);             // 最小空闲
config.setTestOnBorrow(true);      // 获取时校验
config.setTestOnReturn(true);      // 返回时校验
config.setMaxWaitMillis(3000);     // 获取连接超时

// Java (Lettuce — 推荐，支持异步/响应式)
RedisClient client = RedisClient.create("redis://password@host:6379/0");
StatefulRedisConnection<String, String> conn = client.connect();
RedisCommands<String, String> sync = conn.sync();
RedisAsyncCommands<String, String> async = conn.async();
```

### 7.2 常用 Redis 监控命令

```bash
# 实时监控
redis-cli -a password MONITOR          # 实时打印所有命令 (生产慎用)
redis-cli -a password INFO             # 全面状态信息
redis-cli -a password INFO STATS       # 统计信息
redis-cli -a password INFO MEMORY      # 内存信息
redis-cli -a password INFO CLIENTS     # 客户端信息

# 连接数监控
redis-cli CLIENT LIST | wc -l          # 当前连接数
redis-cli INFO connected_clients       # 连接数

# 内存监控
redis-cli INFO used_memory_human       # 已用内存
redis-cli INFO used_memory_peak_human  # 峰值内存
redis-cli INFO mem_fragmentation_ratio # 内存碎片率 (>1.5 需重启)
```

### 7.3 Redis Stack 扩展

Redis Stack (Redis 6.2+) 集成了以下模块：
- **RediSearch**：全文搜索、索引、向量搜索
- **RedisJSON**：原生 JSON 数据类型支持
- **RedisTimeSeries**：时间序列数据类型
- **RedisBloom**：布隆过滤器、Cuckoo Filter

---

## Gotchas — 常见陷阱与反模式 (Common Gotchas & Anti-Patterns)

| # | 问题 | 风险 | 解决方案 |
|---|------|------|---------|

| # | 反模式 | 问题 | 正确做法 |
|---|--------|------|---------|
| 1 | 用 KEYS 在生产环境搜索 | O(n) 扫描全库，阻塞 Redis 数秒 | 用 SCAN 游标迭代 |
| 2 | 大集合上用 SMEMBERS/HGETALL | 百万级元素 JSON 序列化，内存爆炸 | 用 SSCAN/HSCAN 分批或拆分 key |
| 3 | 不使用连接池 | 每个请求创建连接，耗尽系统资源 | 使用 JedisPool/Lettuce 连接池 |
| 4 | 所有 key 不设过期时间 | 内存无限增长，触达 maxmemory | 根据场景设置合适的 TTL |
| 5 | 单机当数据库永久存储 | 无高可用，宕机丢失数据 | 主从+Sentinel 或 Cluster |
| 6 | 使用 SELECT 切分数据库 | 不便于管理监控，Cluster 不支持 | 用不同 key 前缀或不同 Redis 实例 |
| 7 | 生成超长 key 名 | 浪费内存 (key 本身也是存储) | key 名控制在合理长度 (32-64 字符) |
| 8 | 用 Redis 存大文件/二进制 | 撑爆单 key 512MB 限制，性能差 | 存文件路径 + 对象存储 |
| 9 | Pipeline 无限攒批 | 客户端缓冲区 OOM | Pipeline 批量大小控制在 100-500 |
| 10 | 不区分业务用同一个实例 | 互相影响，难以隔离 | 按业务拆分实例 + 限制内存/连接 |

---

## 9. FAQ

**Q1: Redis 为什么不建议用作主数据库？**
Redis 内存昂贵，虽支持持久化但最多丢 1 秒数据，且不支持 SQL 查询和复杂约束。典型架构是 Redis 作为加速层在前，关系型数据库做持久化存储在后。

**Q2: Redis 内存满后会发生什么？**
取决于 maxmemory-policy。推荐 `allkeys-lru`，淘汰最近最少使用的 key。如果设为 `noeviction`，写操作返回 OOM 错误。

**Q3: RDB 和 AOF 同时开启时，启动加载顺序？**
先加载 AOF（数据更完整），AOF 不存在再加载 RDB。混合持久化时 AOF 文件头部是 RDB 快照，先加载 RDB（快），再回放 AOF 增量。

**Q4: 如何选择 Stream 还是 Pub/Sub？**

| 对比 | Pub/Sub | Stream |
|------|---------|--------|
| 消息持久化 | ❌ 不持久，离线丢失 | ✅ 持久化到内存/磁盘 |
| 消费确认 | ❌ 无 ACK | ✅ XACK 确认 |
| 消费组 | ❌ 不支持 | ✅ XGROUP 消费组 |
| 消息回溯 | ❌ 不可回溯 | ✅ XRANGE 可回放 |
| 适用场景 | 实时广播通知 | 可靠消息队列/事件溯源 |

**Q5: Cluster 模式下还能用事务/Lua 吗？**
可以使用，但所有操作的 key 必须在同一节点。使用 hash tag `{tag}` 确保相关 key 路由到同一 slot。跨 slot 的事务无法执行。

**Q6: Big Key 为什么危险？**
一个 Big Key 导致：Redis 变慢（命令 O(n) 阻塞）、集群数据分布不均、持久化时间变长、主从同步延迟大。使用 `--bigkeys` 定期扫描。

**Q7: Redis 线程模型是什么样的？**
Redis 是单线程处理命令（6.0+ 网络 I/O 处理多线程）。单线程避免了锁竞争，但一个慢查询会阻塞所有后续请求。所以 Lua 脚本必须短小，KEYS 不能在 O(n) 命令上操作大集合。

**Q8: 什么情况下用 Redis 6.0+ 的 ACL？**
多租户场景、团队共用 Redis 实例时，用 ACL 控制权限可防止误操作。例如：业务线 A 只能操作 `a:*`，不能使用 FLUSHALL。

**Q9: 如何在不重启的情况下修改配置？**
`CONFIG SET` 动态修改运行期配置，`CONFIG REWRITE` 写入 redis.conf 使其重启后生效。

**Q10: Redis 内存碎片率高怎么处理？**
`mem_fragmentation_ratio > 1.5` 说明碎片严重。Redis 4.0+ 可用 `MEMORY PURGE` 命令触发碎片整理，或设置 `activedefrag yes` 自动整理。

---

## Keywords

redis, redis-cli, 缓存, string, hash, list, set, zset, sorted set, bitmap, hyperloglog, stream, geo, lua, 事务, pipeline, 持久化, RDB, AOF, 混合持久化, 主从复制, sentinel, 哨兵, cluster, 集群, 缓存穿透, 缓存击穿, 缓存雪崩, 分布式锁, 内存淘汰, LRU, LFU, big key, hot key, 慢查询, 性能优化, 安全加固, ACL, Redisson, Jedis, Lettuce, bigkey, hotkey, slot, hash tag, RediSearch, RedisJSON, Redis Stack, 数据淘汰

---

## References

- [Redis 官方文档](https://redis.io/docs/latest/)
- [Redis 命令参考 — redis.net.cn](https://www.redis.net.cn/order/)
- [Redis 教程 — redis.net.cn](https://www.redis.net.cn/tutorial/3501.html)
- [Redis 持久化 RDB/AOF — 官方](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [Redis 集群教程 — 官方](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)
- [Redis 安全 — 官方](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Redis 性能优化 — 官方](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/)
- [Redis 分布式锁 (Redlock) — 官方](https://redis.io/docs/latest/commands/set/)
