# Redis 命令详解 — Set / ZSet / Bitmap / Geo / HyperLogLog / Stream

> 内容源自 doc.redisfans.com 完整翻译版 (Redis 2.8+)，每个命令包含简介、参数说明、业务场景。

---

## 1. Set（集合）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| SADD | O(1)/member | ≥1.0.0 | 添加成员 |
| SREM | O(1)/member | ≥1.0.0 | 移除成员 |
| SISMEMBER | O(1) | ≥1.0.0 | 判断存在 |
| SMEMBERS | O(N) | ≥1.0.0 | 获取全部 |
| SCARD | O(1) | ≥1.0.0 | 成员数量 |

### SADD
**SADD key member [member ...]**

将一个或多个成员添加到集合。已存在的成员被忽略。

**业务场景**：
- **标签系统**：`SADD article:42:tags redis database cache`
- **社交关系**：`SADD user:42:followers user:100`
- **白名单/黑名单**：`SADD blacklist:ip 192.168.1.1`
- **去重记录**：谁访问过某页面

**返回值**：新增成员的数量（不含已存在的）

---

### SREM
**SREM key member [member ...]**

移除集合中的一个或多个成员。不存在的成员被忽略。

**业务场景**：取消关注 (`SREM user:42:following user:100`)、标签删除

---

### SISMEMBER
**SISMEMBER key member**

判断 member 是否是集合的成员（O(1) 级快速），这是 Set 最核心优势之一。

**业务场景**：
- 检查用户是否已点赞：`SISMEMBER post:42:likes user:1001`
- IP 是否在黑名单
- 用户是否已有某个角色/权限

**返回值**：1（存在）| 0（不存在）

---

### SMEMBERS
**SMEMBERS key**

返回集合中所有成员。O(N) 操作，**大集合场景慎用**（可能阻塞）。用 SSCAN 替代。

---

### SCARD
**SCARD key**

返回集合的基数（成员数量）。O(1)，不扫描。

**业务场景**：粉丝数 `SCARD user:1001:followers`、标签数量

---

### 集合运算

#### SINTER / SINTERSTORE
**SINTER key [key ...]**
**SINTERSTORE destination key [key ...]**

返回/存储所有给定集合的交集。

**业务场景**：
- **共同好友**：`SINTER user:42:friends user:100:friends`
- **权限交集**：同时拥有权限 A 和 B 的用户
- **标签匹配**：同时包含 redis 和 database 标签的文章

#### SUNION / SUNIONSTORE
**SUNION key [key ...]**
**SUNIONSTORE destination key [key ...]**

返回/存储所有给定集合的并集。自动去重。

**业务场景**：
- **合并好友列表**：获取共同好友的总集
- **群体权限合并**
- **内容推荐去重**

#### SDIFF / SDIFFSTORE
**SDIFF key [key ...]**
**SDIFFSTORE destination key [key ...]**

返回/存储第一个集合与后续集合的差集。（即：在 A 中但不在 B 中的元素）

**业务场景**：
- **推荐新关注**：`SDIFF user:42:may_know user:42:following`
- **新粉丝检测**：昨天的新增粉丝
- **增量处理**：这批数据中哪些是新的

---

### SPOP / SRANDMEMBER

**SPOP key [count]** — 随机移除并返回 count 个成员
**SRANDMEMBER key [count]** — 随机返回但不移除 count 个成员
- count > 0：返回 count 个不重复成员
- count < 0：返回 |count| 个可重复成员（允许重复）

**业务场景**：
- **抽奖系统**：`SRANDMEMBER lucky:draw:users 1`
- **随机推荐**：`SRANDMEMBER articles 5`
- **资源抽取**：随机分配任务（SPOP 消耗）

---

### SMOVE
**SMOVE source destination member**

将 member 从 source 移动到 destination。原子操作。

**业务场景**：任务流转（待处理 → 处理中）、队列状态迁移

---

### SSCAN
**SSCAN key cursor [MATCH pattern] [COUNT count]**

渐进式迭代集合元素。替代 SMEMBERS 的大集合场景。

---

## 2. Sorted Set（有序集合）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| ZADD | O(log N)/item | ≥1.2.0 | 添加/更新 |
| ZRANGE | O(log N+M) | ≥1.2.0 | 按排名查 |
| ZRANK | O(log N) | ≥2.0.0 | 获取排名 |
| ZSCORE | O(1) | ≥1.2.0 | 获取分数 |
| ZINCRBY | O(log N) | ≥1.2.0 | 增加分数 |

### ZADD
**ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [score member ...]**

将一个或多个 member 及其 score 加入有序集合。如果 member 已存在则更新 score。

**参数说明**：
- `NX`：仅新成员，不更新已存在
- `XX`：仅更新已存在，不添加新成员
- `GT|LT`：仅当新分数大于/小于当前分数时更新
- `CH`：返回值包含更新而不是新增的数量
- `INCR`：增加分数（等价 ZINCRBY）

**业务场景**：
- **实时排行榜**：`ZADD leaderboard 9527 "player_42"`
- **延时队列**：`ZADD delay:queue <unix_timestamp> "job_id"`（用 ZRANGEBYSCORE 轮询到期任务）
- **带权重的标签匹配**

**返回值**：新增成员数量（不含更新）

---

### ZRANGE / ZREVRANGE
**ZRANGE key start stop [WITHSCORES]**
**ZREVRANGE key start stop [WITHSCORES]**

按分数从小到大（ZRANGE）/ 从大到小（ZREVRANGE）返回排名区间内的成员。WITHSCORES 选项同时返回分数。

**业务场景**：
- ZREVRANGE 0 9 WITHSCORES → **排行榜 Top 10**
- ZRANGE 0 -1 → 全部成员（按分排序）

> 注意：ZRANGE 在 Redis 6.2.0+ 中扩展支持 BYSCORE / BYLEX / REV 参数，提供了更强的排序能力。

---

### ZRANGEBYSCORE / ZREVRANGEBYSCORE
**ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]**
**ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]**

按分数范围返回成员。支持区间符号：
- `(5` 不包含 5
- `5` 包含 5
- `-inf` / `+inf` 负无穷 / 正无穷

**业务场景**：
- **延时队列消费**：`ZRANGEBYSCORE delay:queue 0 <current_timestamp LIMIT 0 10`
- **薪资范围查询**：`ZRANGEBYSCORE salary 10000 20000`
- **分数段统计**：`ZCOUNT leaderboard 1000 2000`

---

### ZRANK / ZREVRANK
**ZRANK key member**
**ZREVRANK key member**

返回 member 在有序集合中的排名（0-based）。

**业务场景**：
- 查看自己的排名：`ZREVRANK leaderboard "player_42"`
- 排名变化监控：计算排名差

---

### ZSCORE
**ZSCORE key member**

返回 member 的分数值。O(1) 操作。

---

### ZINCRBY
**ZINCRBY key increment member**

将 member 的分数增加 increment（可正可负）。

**业务场景**：
- 实时更新分数：`ZINCRBY leaderboard 50 "player_42"`（+50 分）
- 扣分：`ZINCRBY leaderboard -10 "player_42"`

---

### ZCARD
**ZCARD key** — 返回有序集合的成员数量（O(1)）

**业务场景**：排行榜总人数、队列长度

---

### ZCOUNT
**ZCOUNT key min max** — 返回分数在 min 和 max 之间的成员数量

**业务场景**：特定分段人数统计（不及格/及格/优秀各多少人）

---

### ZREM / ZREMRANGEBYRANK / ZREMRANGEBYSCORE
**ZREM key member [member ...]** — 移除指定成员
**ZREMRANGEBYRANK key start stop** — 移除排名区间
**ZREMRANGEBYSCORE key min max** — 移除分数区间

**业务场景**：
- 清除过期成员 `ZREMRANGEBYSCORE leaderboard -inf 0`（分数 ≤ 0 的移除）
- 排行榜缩容 `ZREMRANGEBYRANK leaderboard 100 -1`（保留前 100）

---

### ZINTERSTORE / ZUNIONSTORE
**ZINTERSTORE destination numkeys key [key ...] [WEIGHTS w] [AGGREGATE SUM|MIN|MAX]**
**ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS w] [AGGREGATE SUM|MIN|MAX]**

计算多个有序集的交集/并集，结果保存到 destination。
- WEIGHTS：每个 key 的权重乘数
- AGGREGATE：SUM（分数相加）/ MIN（取最小分数）/ MAX（取最大分数）

**业务场景**：
- **多周期合并**：`ZUNIONSTORE monthly 4 week1 week2 week3 week4`（月排行榜 = 4 周合并）
- **加权推荐**：`ZINTERSTORE recommend 2 clicks:user purchases:user WEIGHTS 0.3 0.7`（点击 ×0.3 + 购买 ×0.7 的加权推荐）

---

### ZSCAN
**ZSCAN key cursor [MATCH pattern] [COUNT count]**

渐进式迭代有序集合。

### ZRANGEBYLEX / ZLEXCOUNT / ZREMRANGEBYLEX
**ZRANGEBYLEX key min max [LIMIT offset count]**
**ZLEXCOUNT key min max**
**ZREMRANGEBYLEX key min max**

基于字典序范围操作（需要所有成员分数相同）。区间用 `[`（闭区间）和 `(`（开区间）。

**业务场景**：字符串分组统计、按字母序浏览

---

## 3. Bitmap（位图）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| SETBIT | O(1) | ≥2.2.0 | 设置位 |
| GETBIT | O(1) | ≥2.2.0 | 获取位 |
| BITCOUNT | O(N) | ≥2.2.0 | 统计 1 数量 |
| BITOP | O(N) | ≥2.2.0 | 位运算 |
| BITPOS | O(N) | ≥2.8.7 | 查找位 |

### SETBIT / GETBIT
**SETBIT key offset value** (value: 0 或 1)
**GETBIT key offset**

```
# 用户 42 在 2024-01-15 签到
SETBIT sign:2024-01-15 42 1
# 查询签到状态
GETBIT sign:2024-01-15 42
```

**业务场景**：
- **每日签到**：亿级用户只需 (用户数/8) 字节
- **独立用户标记**：`SETBIT online:2024-01-15 user_id 1`

### BITCOUNT
**BITCOUNT key [start end [BYTE|BIT]]**

**业务场景**：
- 日活统计：`BITCOUNT online:2024-01-15`
- 签到人数：`BITCOUNT sign:2024-01`

### BITOP
**BITOP operation destkey key [key ...]**

**业务场景**：
- 月活：`BITOP OR monthly dest week1 week2 week3 week4`
- 连续活跃：`BITOP AND dest day1 day2 day3`

### BITPOS
**BITPOS key bit [start [end [BYTE|BIT]]]**

返回第一位为 0 或 1 的位置。用于找到第一个空闲位或第一个标记位。

---

## 4. HyperLogLog 命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| PFADD | O(1) | ≥2.8.9 | 添加元素 |
| PFCOUNT | O(1) | ≥2.8.9 | 基数估算 |
| PFMERGE | O(N) | ≥2.8.9 | 合并 |

### PFADD
**PFADD key element [element ...]**

添加元素到 HyperLogLog 数据结构。元素可重复添加（自动去重）。

### PFCOUNT
**PFCOUNT key [key ...]**

返回 HyperLogLog 的基数估算值。单 key O(1)，多 key O(N)（需合并临时结构）。

**误差**：标准误差 0.81%

**业务场景**：
- **UV 统计**：`PFADD uv:2024-01-15 "user_42"` → `PFCOUNT uv:2024-01-15`
- **多日合并 UV**：`PFCOUNT uv:day1 uv:day2 uv:day3`
- **搜索词去重**：`PFADD search:terms "redis cluster"`

### PFMERGE
**PFMERGE destkey sourcekey [sourcekey ...]**

合并多个 HyperLogLog 到 destkey。

**业务场景**：月 UV = 合并 30 天的 UV `PFMERGE uv:2024-01 uv:0101 uv:0102 ... uv:0130`

---

## 5. Geo（地理位置）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| GEOADD | O(log N)/item | ≥3.2.0 | 添加位置 |
| GEOPOS | O(log N)/item | ≥3.2.0 | 获取坐标 |
| GEODIST | O(log N) | ≥3.2.0 | 距离计算 |
| GEORADIUS | O(N+log M) | ≥3.2.0 | 半径查询 |
| GEOHASH | O(log N)/item | ≥3.2.0 | 编码转换 |

### GEOADD
**GEOADD key longitude latitude member [longitude latitude member ...]**

将指定的地理空间位置（经度、纬度、名称）添加到 key 中。

```
GEOADD cities 116.397 39.908 "北京" 121.474 31.230 "上海"
GEOADD cities 113.264 23.129 "广州" 114.057 22.543 "深圳"
```

---

### GEODIST
**GEODIST key member1 member2 [m|km|mi|ft]**

返回两个给定位置之间的距离。默认米（m）。

```
GEODIST cities "北京" "上海" km    → 1067.5
GEODIST cities "北京" "广州" km    → 1889.6
```

---

### GEORADIUS
**GEORADIUS key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count]**

以给定的经纬度为中心，查找半径内的位置元素。
- `WITHDIST`：同时返回距离
- `WITHCOORD`：同时返回坐标
- `COUNT`：限制返回数量

**业务场景**：
- **附近的人/店铺**：`GEORADIUS locations 116.4 39.9 5 km WITHDIST COUNT 20`
- **地理围栏**：查询指定范围内的 POI

---

### GEORADIUSBYMEMBER
**GEORADIUSBYMEMBER key member radius m|km|ft|mi [...]**

以已存储的成员为中心，查找附近的元素。

**业务场景**：基于用户当前位置查找附近服务

---

### GEOHASH
**GEOHASH key member [member ...]**

返回 Geohash 编码字符串（11 字符）。

---

## 6. Stream（消息流）命令

| 命令 | 时间复杂度 | 可用版本 | 说明 |
|------|-----------|---------|------|
| XADD | O(1)/entry | ≥5.0.0 | 追加消息 |
| XREAD | O(N) | ≥5.0.0 | 读取消息 |
| XRANGE | O(N) | ≥5.0.0 | 范围查询 |
| XGROUP | O(1) | ≥5.0.0 | 管理消费组 |
| XREADGROUP | O(N) | ≥5.0.0 | 消费组读取 |
| XACK | O(1) | ≥5.0.0 | 确认消费 |

### XADD
**XADD key [NOMKSTREAM] [MAXLEN|MINID [~] threshold] *|id field value [field value ...]**

向 Stream 追加一条新消息。`*` 表示自动生成唯一时间戳 ID，格式 `unix_ms-sequence`。
- `NOMKSTREAM`：key 不存在时不自动创建
- `MAXLEN [~]`：限制长度（`~` 启用近似修剪提升性能）
- `MINID [~]`：按 ID 阈值修剪

**业务场景**：
```
# 订单事件流
XADD orders * order_id 1001 user_id 42 amount 99.99 status created
XADD orders * order_id 1001 status paid
XADD orders * order_id 1001 status shipped
```

---

### XRANGE / XREVRANGE
**XRANGE key start end [COUNT count]**
**XREVRANGE key end start [COUNT count]**

按 ID 范围返回消息。用 `-` 和 `+` 表示最小/最大 ID。

**业务场景**：
- 查看最新消息：`XREVRANGE stream + - COUNT 10`
- 按时间段查询：`XRANGE orders 1700000000000-0 1700001000000-0`
- 全量回放：`XRANGE stream - +`

---

### XREAD
**XREAD [COUNT count] [BLOCK milliseconds] STREAMS key [key ...] id [id ...]**

读取一个或多个 Stream 中 ID 大于指定值的新消息。
- `BLOCK 0`：阻塞等待（不超时）
- `COUNT 10`：最多返回 10 条

**业务场景**：
```
# 非阻塞读取
XREAD COUNT 10 STREAMS mystream 0

# 阻塞等待新消息
XREAD COUNT 1 BLOCK 5000 STREAMS mystream $
```

---

### XGROUP
**XGROUP [CREATE|SETID|DESTROY|DELCONSUMER] key group [id|$] [MKSTREAM]**

管理消费组。
- `XGROUP CREATE mystream mygroup $`：创建组，从最新消息开始
- `XGROUP CREATE mystream mygroup 0`：创建组，从第一条消息开始
- `MKSTREAM`：key 不存在时自动创建

---

### XREADGROUP
**XREADGROUP GROUP group consumer [COUNT count] [BLOCK ms] STREAMS key [key ...] id [id ...]**

消费组读取。`>` 表示读取未被其他消费者读取的新消息。

**业务场景**：
```
# 多消费者处理订单流
# 消费者 1
XREADGROUP GROUP orders-group consumer-1 COUNT 1 BLOCK 2000 STREAMS orders >

# 消费者 2 (自动负载均衡)
XREADGROUP GROUP orders-group consumer-2 COUNT 1 BLOCK 2000 STREAMS orders >
```

---

### XACK
**XACK key group id [id ...]**

确认消息已被处理。**消息确认后才从 Pending 列表移除**。

---

### XPENDING / XINFO
**XPENDING key group [start end count [consumer]]**
**XINFO GROUPS key**

管理 Pending 消息（已投递但未 ACK）。
- `XPENDING orders payment-group`：查看待确认
- `XPENDING orders payment-group - + 10 consumer-1`：查看消费者 1 的待确认

---

## 7. 编码与空间效率对比

| 数据结构 | 小数据编码 | 内存效率 | 数据量阈值 |
|---------|-----------|---------|-----------|
| Hash | ziplist → hashtable | 高（小数据）→ 中 | entries:512, value:64B |
| ZSet | ziplist → skiplist | 高（小数据）→ 中 | entries:128, value:64B |
| Set | intset → hashtable | 高（全整数）→ 中 | entries:512 |
| List | quicklist (ziplist节点) | 高 | list-max-ziplist-size:-2 |
