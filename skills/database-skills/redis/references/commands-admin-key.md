# Redis 命令详解 — Key / 事务 / Lua / PubSub / 连接 / 服务器

> 内容源自 doc.redisfans.com 完整翻译版 (Redis 2.8+)，每个命令包含简介、参数说明、业务场景。

---

## 1. Key（键）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| DEL | O(N) | ≥1.0.0 | 删除 key |
| EXISTS | O(1) | ≥1.0.0 | 检查存在 |
| EXPIRE | O(1) | ≥1.0.0 | 设置 TTL |
| TTL | O(1) | ≥1.0.0 | 查看 TTL |
| TYPE | O(1) | ≥1.0.0 | 返回类型 |
| KEYS | O(N) | ≥1.0.0 | 查找 key |
| SCAN | O(1)/cursor | ≥2.8.0 | 渐进遍历 |

### DEL
**DEL key [key ...]**

删除一个或多个 key。不支持通配符（请使用 SCAN + DEL）。
- 时间复杂度 O(N)：N 为删除的 key 数量，复杂类型（List/Set/ZSet/Hash）删除时间与元素数量相关

**业务场景**：
- 清理缓存 `DEL cache:user:42 cache:user:43 cache:user:44`
- 重置数据 `DEL user:1001:session`

**返回值**：被删除 key 的数量

---

### EXISTS
**EXISTS key [key ...] (Redis 3.0.3+ 支持多 key)**

检查 key 是否存在。多 key 版本返回存在的 key 数。

**业务场景**：
- 缓存命中判断 `EXISTS cache:hot:article:42` → 1 命中
- 批量校验 `EXISTS key1 key2 key3` → 快速判断多个 key 全部存在

---

### EXPIRE / PEXPIRE
**EXPIRE key seconds**
**PEXPIRE key milliseconds**

设置 key 的生存时间（秒/毫秒），到期后自动删除（易失性）。
- TTL 不会被只读/修改命令（INCR/LPUSH/HSET）改变
- RENAME 后新 key 继承 TTL
- SET/GETSET 会清除原有 TTL

**业务场景**：
```
# 导航会话（60 秒无操作清空）
MULTI
    RPUSH navig:user:42 "page_3"
    EXPIRE navig:user:42 60
EXEC
```

---

### EXPIREAT / PEXPIREAT
**EXPIREAT key timestamp**
**PEXPIREAT key milliseconds-timestamp**

设置 key 在指定 Unix 时间戳过期。精确到秒/毫秒。

**业务场景**：
- **优惠券到期**：`EXPIREAT coupon:user:42 1893456000`（2030-01-01 00:00）
- **定时删除**：配合 cron 计算到期时间戳

---

### TTL / PTTL
**TTL key** — 返回剩余生存时间（秒），-1 无过期，-2 key 不存在
**PTTL key** — 返回毫秒数

**业务场景**：
- 热键 TTL 监控（防止缓存穿透）
- 动态延长热点数据 TTL：TTL < 30 时 EXPIRE 续期

---

### PERSIST
**PERSIST key** — 移除 key 的过期时间，使其持久保留

**业务场景**：将热点 key 从"定时过期"转为"永久缓存"

---

### TYPE
**TYPE key** — 返回 key 的数据类型：string / list / set / zset / hash / stream / none

**业务场景**：键值类型校验，防止对集合类型执行字符串操作

---

### KEYS
**KEYS pattern** — 查找所有匹配 pattern 的 key
- 支持 glob 风格：`*` `?` `[a-z]`
- **O(N) 阻塞操作，生产环境严禁使用**

**正确做法**：使用 `SCAN 0 MATCH user:* COUNT 100`

---

### SCAN
**SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]**

渐进式迭代数据库中的 key。每次返回游标 + 一批 key。
- cursor = 0 开始迭代，cursor = 0 结束
- COUNT 提示每次返回数量（不保证精确）
- TYPE 过滤类型 (Redis 6.0+)

**业务场景**：
```
SCAN 0 MATCH user:* COUNT 100        # 迭代查找 user: 开头的 key
SCAN 0 TYPE hash COUNT 100           # 只找 hash 类型的 key
```

---

### RENAME / RENAMENX
**RENAME key newkey** — 改名（newkey 存在则覆盖）
**RENAMENX key newkey** — 改名（仅 newkey 不存在时）

**业务场景**：数据迁移、key 命名变更、A/B 测试流量切换

---

### MOVE
**MOVE key db** — 将当前数据库的 key 移到指定数据库

> 注意：Cluster 模式只支持 0 号数据库，MOVE 无法使用。

---

### RANDOMKEY
**RANDOMKEY** — 从当前数据库中随机返回一个 key

**业务场景**：数据采样、缓存预热随机检查

---

### DUMP / RESTORE
**DUMP key** — 序列化 key 并返回（含 TTL 信息）
**RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME t] [FREQ f]**

**业务场景**：
- **迁移单个 key**：源 DUMP → 目标 RESTORE
- **备份恢复**：对单个 key 做序列化备份

---

### OBJECT
**OBJECT subcommand [arguments [arguments]]**
- `OBJECT REFCOUNT key` — 引用计数
- `OBJECT ENCODING key` — 底层编码（raw/embstr/ziplist/dict/intset/skiplist）
- `OBJECT IDLETIME key` — 空闲时间（LRU 相关）

**业务场景**：
```
OBJECT ENCODING user:1001    → "hashtable" 或 "ziplist"
OBJECT IDLETIME hot_data     → 判断是否为闲置 key
```

---

### SORT
**SORT key [BY pattern] [LIMIT offset count] [GET pattern] [ASC|DESC] [ALPHA] [STORE destination]**

对 List、Set、ZSet 中的元素排序（支持外部 key BY/GET，**可能阻塞**）。

> Redis 6.2.0+ 弃用 SORT，推荐使用 SORT_RO（只读版）。

---

## 2. 事务（Transaction）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| MULTI | O(1) | ≥1.2.0 | 开始事务 |
| EXEC | 取决于命令 | ≥1.2.0 | 执行 |
| DISCARD | O(1) | ≥2.0.0 | 取消 |
| WATCH | O(1) | ≥2.0.0 | 乐观锁 |

### MULTI / EXEC / DISCARD
**MULTI** — 标记事务块开始（后续命令入队）
**EXEC** — 顺序执行队列中所有命令
**DISCARD** — 取消事务，清空命令队列

**事务特性**：
- 原子性：EXEC 时要么全部执行，要么因语法错误全部不执行
- 无回滚：运行时错误（如对 string 执行 LIST 操作）不影响其他命令
- 隔离性：EXEC 前其他客户端不会看到中间状态

**业务场景**：
```
# 转账（原子扣减 + 增加）
MULTI
    DECRBY account:42 1000
    INCRBY account:100 1000
EXEC
```

---

### WATCH / UNWATCH
**WATCH key [key ...]** — 乐观锁（CAS）
**UNWATCH** — 取消所有 WATCH

**业务场景**：
```
# 库存扣减（CAS 保证）
WATCH stock:item:1001
count = GET stock:item:1001
if count > 0:
    MULTI
        DECRBY stock:item:1001 1
    EXEC    # 如果 stock:item:1001 在此期间被修改 → EXEC 返回 nil
else:
    UNWATCH    # 放弃监视
```

---

## 3. Lua 脚本命令

| 命令 | 可用版本 | 说明 |
|------|---------|------|
| EVAL | ≥2.6.0 | 执行脚本 |
| EVALSHA | ≥2.6.0 | 执行缓存脚本 |
| SCRIPT LOAD | ≥2.6.0 | 加载到缓存 |
| SCRIPT EXISTS | ≥2.6.0 | 检查缓存 |
| SCRIPT FLUSH | ≥2.6.0 | 清理缓存 |
| SCRIPT KILL | ≥2.6.0 | 终止运行 |

### EVAL
**EVAL script numkeys key [key ...] arg [arg ...]**

在服务器端执行 Lua 脚本。脚本在 Redis 内原子执行。

**关键规则**：
- 所有 key 通过 KEYS 数组传入（Cluster 兼容）
- 所有参数通过 ARGV 数组传入
- 脚本应短小精悍（Lua 脚本执行时阻塞其他所有请求）

**业务场景：原子取余分配**
```lua
-- 一致性哈希槽分配
local slot = redis.call("HGET", KEYS[1], ARGV[1])
if not slot then
    slot = redis.call("HLEN", KEYS[1]) % tonumber(ARGV[2])
    redis.call("HSET", KEYS[1], ARGV[1], slot)
end
return slot
```

**业务场景：原子限流**
```lua
-- 滑动窗口限流
local key = KEYS[1]
local now = redis.call("TIME")[1]
local window = tonumber(ARGV[1])
local limit = tonumber(ARGV[2])

redis.call("ZREMRANGEBYSCORE", key, 0, now - window)
local count = redis.call("ZCARD", key)

if count < limit then
    redis.call("ZADD", key, now, now .. ":" .. math.random())
    redis.call("EXPIRE", key, window)
    return 1  -- 允许
else
    return 0  -- 限流
end
```

---

## 4. Pub/Sub（发布/订阅）命令

| 命令 | 可用版本 | 说明 |
|------|---------|------|
| SUBSCRIBE | ≥2.0.0 | 订阅频道 |
| PUBLISH | ≥2.0.0 | 发布消息 |
| PSUBSCRIBE | ≥2.0.0 | 模式订阅 |

### SUBSCRIBE / PUBLISH
**SUBSCRIBE channel [channel ...]** — 订阅一个或多个频道
**PUBLISH channel message** — 向频道发送消息

**业务场景**：
- **实时通知广播**：用户发布新内容时通知关注者
- **服务状态广播**：配置变更通知所有服务实例
- **实时聊天**：每个聊天室一个频道

### PSUBSCRIBE
**PSUBSCRIBE pattern [pattern ...]**

按模式订阅频道。模式支持 glob 风格：`news.*` 匹配 `news.sports`、`news.tech` 等。

### PUBSUB
**PUBSUB subcommand [argument [arguments]]**
- `PUBSUB CHANNELS [pattern]` — 查看当前活跃频道
- `PUBSUB NUMSUB [channel ...]` — 查看频道订阅数
- `PUBSUB NUMPAT` — 查看模式订阅数

---

## 5. 连接（Connection）命令

| 命令 | 可用版本 | 说明 |
|------|---------|------|
| AUTH | ≥1.0.0 | 密码认证 |
| SELECT | ≥1.0.0 | 切换数据库 |
| PING | ≥1.0.0 | 存活检测 |
| CLIENT | ≥2.4.0 | 客户端管理 |

### AUTH
**AUTH password** — 向 Redis 验证密码（requirepass 配置）

### SELECT
**SELECT index** — 切换到指定数据库（0-15，默认 16 个库）
> ⚠️ Cluster 模式不支持 SELECT，只可用 0 号库。推荐用不同 key 前缀代替。

### PING
**PING** — 检查连接是否存活。返回 PONG。

### QUIT
**QUIT** — 关闭连接

### CLIENT 系列
**CLIENT SETNAME name** — 设置连接名称（便于 DEBUG）
**CLIENT GETNAME** — 获取连接名称
**CLIENT LIST** — 列出所有连接（含名称/地址/状态/缓冲区大小）
**CLIENT KILL [ip:port] [ID client-id]** — 杀掉连接
**CLIENT PAUSE timeout** — 暂停所有客户端命令（用于故障转移）
**CLIENT UNPAUSE** — 恢复

---

## 6. 服务器（Server）命令

| 命令 | 可用版本 | 说明 |
|------|---------|------|
| INFO | ≥1.0.0 | 服务器信息 |
| CONFIG | ≥2.0.0 | 配置管理 |
| SLOWLOG | ≥2.2.12 | 慢查询日志 |
| MONITOR | ≥1.0.0 | 实时调试 |

### INFO
**INFO [section]**

返回服务器信息（含 9 个 section）：
- Server / Clients / Memory / Persistence / Stats / Replication / CPU / Keyspace / Cluster

**常用**：`INFO MEMORY` `INFO STATS` `INFO REPLICATION` `INFO KEYSPACE`

### CONFIG
**CONFIG GET parameter** — 获取配置值 `CONFIG GET *` 全部
**CONFIG SET parameter value** — 修改运行时配置（无需重启）
**CONFIG REWRITE** — 写入 redis.conf（使修改持久化）
**CONFIG RESETSTAT** — 重置 INFO 统计

### SLOWLOG
**SLOWLOG GET [count]** — 返回慢查询
**SLOWLOG LEN** — 慢查询总数
**SLOWLOG RESET** — 清空慢查询

### MONITOR
实时打印 Redis 收到的所有命令。**生产慎用**（降低约 50% 吞吐量）。

### FLUSHDB / FLUSHALL
**FLUSHDB** — 清空当前数据库
**FLUSHALL** — 清空所有数据库
> 用 `CONFIG SET rename-command FLUSHALL ""` 禁用

### BGSAVE / SAVE
**BGSAVE** — 后台 fork 生成 RDB（不阻塞）
**SAVE** — 前台生成 RDB（阻塞所有请求）

### BGREWRITEAOF
异步重写 AOF 文件（压缩）。

### SHUTDOWN
**SHUTDOWN [NOSAVE|SAVE]** — 关闭服务器
- SAVE：关闭前生成 RDB
- NOSAVE：跳过保存

### SLAVEOF
**SLAVEOF host port** — 设置主从
**SLAVEOF NO ONE** — 取消复制，提升为主

### ROLE
返回实例的角色：master / slave / sentinel + 复制状态

### INFO 关键字段解读

```
used_memory_human: 4.00G           # 已用内存
used_memory_peak_human: 6.00G      # 峰值内存
mem_fragmentation_ratio: 1.37      # 碎片率（>1.5 需整理）
connected_clients: 50              # 当前连接数
instantaneous_ops_per_sec: 15000   # 当前 QPS
keyspace_hits: 410000              # 缓存命中率计算
keyspace_misses: 82000
expired_keys: 0                    # 过期 key 数
evicted_keys: 0                    # 淘汰 key 数
rejected_connections: 0            # 拒绝的连接数
```
