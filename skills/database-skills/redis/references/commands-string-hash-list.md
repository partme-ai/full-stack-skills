# Redis 命令详解 — String / Hash / List

> 内容源自 doc.redisfans.com 完整翻译版 (Redis 2.8+)，每个命令包含简介、参数说明、业务场景。

---

## 1. String（字符串）命令

| 命令 | 时间复杂度 | 可用版本 | 分类 |
|------|-----------|---------|------|
| SET | O(1) | ≥1.0.0 | 基础 |
| GET | O(1) | ≥1.0.0 | 基础 |
| INCR | O(1) | ≥1.0.0 | 计数器 |
| MSET | O(N) | ≥1.0.1 | 批量 |
| APPEND | O(1) | ≥2.0.0 | 字符串操作 |

### SET
**SET key value [EX seconds] [PX milliseconds] [NX|XX] [KEEPTTL]**

将字符串值 value 关联到 key。如果 key 已存在，SET 覆写旧值。对于原带 TTL 的 key，SET 执行后清除原 TTL。

**参数说明**：
- `EX seconds`：设置过期时间（秒），等价 SETEX
- `PX milliseconds`：设置过期时间（毫秒），等价 PSETEX
- `NX`：仅在 key 不存在时设置，等价 SETNX
- `XX`：仅在 key 已存在时设置
- `KEEPTTL` (Redis 6.0+)：保留 key 原有的 TTL

> ⚠️ Redis 未来版本可能废弃 SETNX / SETEX / PSETEX，推荐统一使用 SET 的可选参数。

**业务场景：分布式锁**
```
SET resource:lock random_string NX EX 30
```
- 返回 OK → 获得锁
- 返回 NIL → 锁被占用，稍后重试
- 解锁需配合 Lua 脚本原子校验 token 后 DEL

**业务场景：缓存**
```
SET user:profile:42 '{"name":"Alice"}' EX 3600
```

**返回值**：OK（成功）| NIL（NX/XX 条件未满足）

---

### GET
**GET key**

返回 key 所关联的字符串值。key 不存在返回 nil，key 不是 string 类型返回错误。

**业务场景**：
- 缓存读取（配合 SETEX 写入）
- 分布式锁 token 校验
- Session 数据获取

**返回值**：字符串值 | nil（key 不存在）

---

### INCR
**INCR key**

将 key 中存储的数字值增一。key 不存在则先初始化为 0 再执行。值不能超过 64 位有符号整数。

**业务场景**：
- **计数器**：页面访问量、文章 PV/UV
- **序列生成器**：订单号自增 (`INCR order:seq`)
- **限流计数器**：每秒/每分钟请求计数
- **消息未读数**：`INCR user:42:unread`

**错误处理**：如果 key 存的值不是数字，返回 WRONGTYPE 错误。

**返回值**：执行 INCR 后的新值

---

### INCRBY
**INCRBY key increment**

将 key 中的数字加上指定增量（可正可负）。等价于 INCR 的通用版本。

**业务场景**：
- 积分增减 `INCRBY user:42:points 100`
- 库存批量扣减 `INCRBY stock:item:1001 -1`

---

### INCRBYFLOAT
**INCRBYFLOAT key increment**

为 key 中的值加上浮点数增量。支持精度到小数点后 17 位。

**业务场景**：价格计算、余额操作、汇率换算

---

### DECR / DECRBY
**DECR key** / **DECRBY key decrement**

将 key 中的数字值减一/减 decrement。等价于 INCRBY 的减量版本。

**业务场景**：
- 库存剩余量实时递减
- 优惠券剩余数量
- 限流可用配额

---

### MSET
**MSET key value [key value ...]**

同时设置一个或多个 key-value。MSET 是原子操作（要么全设要么全不设），MGET 不是（但读取本身是原子单次操作）。

**业务场景**：批量初始化缓存、批量保存配置

```
MSET user:1:name "Alice" user:1:age 30 user:1:city "Beijing"
```

**返回值**：OK

---

### MSETNX
**MSETNX key value [key value ...]**

仅当所有给定 key 都不存在时，才同时设置一个或多个 key-value。原子性保证"全部或全不"。

**业务场景**：批量初始化确保不覆盖已有数据

---

### MGET
**MGET key [key ...]**

返回所有给定 key 的值（按请求顺序返回）。某个 key 不存在则返回 nil。

**业务场景**：批量查缓存（比 N 次 GET 节省 RTT）

---

### APPEND
**APPEND key value**

将 value 追加到 key 原值的末尾。key 不存在则等同于 SET。

**业务场景**：日志追加、文本拼接、Feed 构建

**返回值**：追加后的字符串长度

---

### GETRANGE
**GETRANGE key start end**

返回 key 中字符串的子串（0-based，包含 start 和 end）。支持负数偏移（-1 是最后一个字符）。

**业务场景**：截取部分内容展示、分页读取长字符串

---

### SETRANGE
**SETRANGE key offset value**

从 offset 开始，用 value 覆写 key 的字符串。原字符串长度不足则自动补充零字节（\x00）。

**业务场景**：更新固定长度字段、位图叠加写入

---

### STRLEN
**STRLEN key**

返回字符串值的长度。key 不存在返回 0。

---

### GETSET
**GETSET key value**

原子操作：设置新值，返回旧值。如果 key 不存在则返回 nil（此时相当于 SET）。

**业务场景**：计数器重置（获取旧值后置零）、轮转更新

---

### SETEX
**SETEX key seconds value**

等价 `SET key value EX seconds`。建议直接用 SET 替代。

---

### SETNX
**SETNX key value**

等价 `SET key value NX`。建议直接用 SET 替代。

---

### PSETEX
**PSETEX key milliseconds value**

等价 `SET key value PX milliseconds`。建议直接用 SET 替代。

---

### BITCOUNT
**BITCOUNT key [start end [BYTE|BIT]]**

计算字符串中 1 的比特位数量（popcount）。可通过 start/end 指定字节范围。

**业务场景**：
- **在线用户统计**：每天一个 BITMAP，用户 ID 作为 offset
- **签到统计**：`BITCOUNT sign:2024-01-15`
- **日活 UV 统计**：多天 BITMAP 的 BITOP OR 再 BITCOUNT

---

### BITOP
**BITOP operation destkey key [key ...]**

对一个或多个 key 执行位运算：AND / OR / NOT / XOR，结果保存到 destkey。

**业务场景**：
- **连续签到统计**：`BITOP AND result sign:01 sign:02 sign:03` （当月全部签到的用户）
- **任意签到查找**：`BITOP OR result sign:01 sign:02`（月内至少签到一次的用户）
- **广告去重**：多日曝光用户 BITOP OR

---

### SETBIT / GETBIT
**SETBIT key offset value** / **GETBIT key offset**

设置/获取指定偏移量上的比特位（0 或 1）。

**业务场景**：
- 用户签到：`SETBIT sign:2024-01 42 1`
- 布隆过滤器实现
- 独立用户标记

---

## 2. Hash（哈希表）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| HSET | O(1) | ≥2.0.0 | 设置字段 |
| HGET | O(1) | ≥2.0.0 | 获取字段 |
| HGETALL | O(N) | ≥2.0.0 | 获取所有 |
| HMSET | O(N) | ≥2.0.0 | 批量设置 |
| HINCRBY | O(1) | ≥2.0.0 | 字段计数 |

### HSET
**HSET key field value [field value ...] (Redis 4.0+ 支持多 field)**

设置哈希表 key 中的字段。字段已存在则覆盖旧值。多字段版本返回新创建字段数量。

**业务场景：对象存储**
```
HSET user:1001 name "Alice" age 30 email "alice@example.com"
```
替代了 `set user:1001:name` / `set user:1001:age` / `set user:1001:email` 三个 key，节省约 50% 内存。

---

### HGET
**HGET key field**

获取哈希表中指定字段的值。

---

### HGETALL
**HGETALL key**

返回哈希表中所有字段和值（交替排列）。**大 Hash 场景慎用**（阻塞 Redis）。

**业务场景**：小对象（字段数 < 100）适合全量读取；大对象改用 HSCAN 分批迭代。

---

### HMSET / HMGET
**HMSET key field value [field value ...]**
**HMGET key field [field ...]**

批量设置/获取字段。HMSET 已被 HSET 的多 field 版本取代。

**业务场景**：`HMGET user:1001 name email` 只取需要的字段，避免 HGETALL 浪费带宽。

---

### HEXISTS / HDEL
**HEXISTS key field** — 判断字段是否存在
**HDEL key field [field ...]** — 删除一个或多个字段

---

### HLEN
**HLEN key** — 返回哈希表中字段数量

**业务场景**：Hash 大小时监控（HLEN 是 O(1) 的快照）。

---

### HKEYS / HVALS
**HKEYS key** — 获取所有字段名
**HVALS key** — 获取所有字段值

---

### HINCRBY / HINCRBYFLOAT
**HINCRBY key field increment** — 整数增加
**HINCRBYFLOAT key field increment** — 浮点数增加

**业务场景**：Hash 中的计数器（如用户积分 `HINCRBY user:1001 score 10`）

---

### HSETNX
**HSETNX key field value** — 字段不存在时才设置（等价 Hash 版的 SETNX）

**业务场景**：
- 第一次访问时设置初始值
- 防止覆盖已有数据

### HSCAN
**HSCAN key cursor [MATCH pattern] [COUNT count]**

渐进式迭代哈希表中的字段。**替代 HGETALL 大 Hash 场景**。

---

## 3. List（列表）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| LPUSH | O(1) | ≥1.0.0 | 左推 |
| RPUSH | O(1) | ≥1.0.0 | 右推 |
| LPOP | O(1) | ≥1.0.0 | 左弹 |
| LRANGE | O(S+N) | ≥1.0.0 | 范围查 |
| LTRIM | O(N) | ≥1.0.0 | 修剪 |
| BLPOP | O(1) | ≥2.0.0 | 阻塞左弹 |

### RPUSH / LPUSH
**RPUSH key value [value ...]** — 右端推入
**LPUSH key value [value ...]** — 左端推入

**业务场景**：
- **队列** (FIFO)：`RPUSH queue job1` + `LPOP queue` 或 `BLPOP queue`
- **栈** (LIFO)：`LPUSH stack item` + `LPOP stack`
- **时间线**：`LPUSH timeline:user42 post_id` + `LTRIM timeline:user42 0 99`

---

### LRANGE
**LRANGE key start stop**

返回列表中指定区间内的元素（0-based）。负偏移索引：-1 是最后一个。

**业务场景**：分页读取列表、获取最新 N 条消息

```
LRANGE messages 0 9    -- 最新 10 条
LRANGE messages 0 -1   -- 全部（慎用，大列表会阻塞）
```

---

### LTRIM
**LTRIM key start stop**

修剪列表，仅保留指定区间内的元素。

**业务场景：固定长度列表**
```
LPUSH recent:items article:1001
LTRIM recent:items 0 99    -- 最多保留 100 条
```

---

### LPOP / RPOP
**LPOP key [count] (Redis 6.2+)** — 移除并返回左边第一个元素
**RPOP key [count] (Redis 6.2+)** — 移除并返回右边第一个元素

---

### BLPOP / BRPOP
**BLPOP key [key ...] timeout**
**BRPOP key [key ...] timeout**

阻塞式弹出：列表为空时等待，直到超时或有元素加入。timeout=0 表示无限等待。

**业务场景：可靠消息队列**
```
# Worker 端
BLOP queue 0                       # 无限等待新任务
# 有元素加入队列时立即返回，无需轮询
```

**阻塞特性**：
- 多个客户端同时 BLPOP 同一 key → 第一个等待的客户端优先
- 监视多个 key：按 key 顺序依次检查
- 超时返回 nil（两个 nil 值）

---

### RPOPLPUSH / BRPOPLPUSH
**RPOPLPUSH source destination** — 转存（原子操作）
**BRPOPLPUSH source destination timeout** — 阻塞版转存

**业务场景：可靠消息处理（备份队列）**
```
# 生产：RPUSH queue:incoming job
# 消费：BRPOPLPUSH queue:incoming queue:processing 0
# 成功处理后：LREM queue:processing 1 job
# 处理失败：RPUSH queue:retry job
```
原子转移保证消息不丢——崩溃重启后还能从 processing 队列恢复。

---

### LINDEX / LSET / LINSERT
**LINDEX key index** — 根据索引获取
**LSET key index value** — 设置索引位置的元素
**LINSERT key BEFORE|AFTER pivot value** — 在指定元素前后插入

**业务场景**：LRANGE 读取后定位到特定位置修改、列表中间插入优先级任务

---

### LLEN
**LLEN key** — 返回列表长度（O(1)）

**业务场景**：消息队列积压长度监控、列表大小的快速判断

---

### LREM
**LREM key count value**

移除列表中与 value 匹配的元素。
- count > 0：从左到右移除最多 count 个
- count < 0：从右到左移除最多 |count| 个
- count = 0：移除全部匹配

**业务场景**：取消点赞、清理已处理消息

---

### LPUSHX / RPUSHX
**LPUSHX key value** — 仅当列表存在时左推
**RPUSHX key value** — 仅当列表存在时右推

**业务场景**：仅在队列初始化后才接收新消息，避免自动创建空列表。
