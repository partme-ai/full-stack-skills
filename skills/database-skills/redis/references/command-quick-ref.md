# Redis 命令速查

## 操作分类速查

```
内存操作: SET / GET / DEL / EXISTS / TYPE / TTL / EXPIRE / PERSIST
计数器:   INCR / DECR / INCRBY / INCRBYFLOAT
散列:     HSET / HGET / HGETALL / HDEL / HEXISTS / HINCRBY
列表:     LPUSH / RPUSH / LPOP / RPOP / LRANGE / LLEN / LTRIM / BLPOP
集合:     SADD / SREM / SMEMBERS / SISMEMBER / SCARD / SINTER / SUNION
有序集合: ZADD / ZREM / ZRANGE / ZRANK / ZSCORE / ZINCRBY / ZINTERSTORE
位图:     SETBIT / GETBIT / BITCOUNT / BITOP
地理:     GEOADD / GEOPOS / GEODIST / GEORADIUS
流:       XADD / XREAD / XREADGROUP / XACK / XRANGE / XLEN / XTRIM
超日志:   PFADD / PFCOUNT / PFMERGE
事务:     MULTI / EXEC / WATCH / DISCARD
脚本:     EVAL / EVALSHA / SCRIPT LOAD / SCRIPT KILL
连接:     PING / AUTH / SELECT / CLIENT LIST / CLIENT KILL
服务器:   INFO / CONFIG GET/SET / SLOWLOG / MONITOR / DBSIZE / FLUSHALL
发布订阅: PUBLISH / SUBSCRIBE / PSUBSCRIBE / PUBSUB
```

## 字符串命令速查

```
SET key value [EX|PX] [NX|XX]     # 设置值，支持过期和条件
GET key                            # 返回字符串值或 nil
MGET key1 key2                     # 批量获取
MSET k1 v1 k2 v2                   # 批量设置
INCR key                           # 整数 +1 (原子)
INCRBY key n                       # 整数 +n
DECR key                           # 整数 -1
DECRBY key n                       # 整数 -n
APPEND key value                   # 追加到末尾
GETRANGE key start end             # 获取子串
SETRANGE key offset value          # 从 offset 覆写
STRLEN key                         # 获取长度
GETSET key new_value               # 返回旧值设新值
SETEX key sec value                # 设置+过期
SETNX key value                    # 不存在才设置
```

## 哈希命令速查

```
HSET key field value               # 设置字段
HSETNX key field value             # 不存在才设置
HGET key field                     # 获取字段
HGETALL key                        # 获取所有 (慎用)
HMGET key f1 f2                    # 批量获取
HMSET key f1 v1 f2 v2             # 批量设置
HDEL key field                     # 删除字段
HEXISTS key field                  # 判断存在
HLEN key                           # 字段数量
HKEYS key                          # 所有字段名
HVALS key                          # 所有字段值
HINCRBY key field n                # 字段值 +n
HINCRBYFLOAT key field n           # 浮点增加
```

## 列表命令速查

```
LPUSH key v1 v2                    # 左推
RPUSH key v1 v2                    # 右推
LPOP key                           # 左弹
RPOP key                           # 右弹
LRANGE key start stop              # 范围获取
LINDEX key index                   # 索引获取
LLEN key                           # 长度
LREM key count value               # 移除元素
LTRIM key start stop               # 修剪
LSET key index value               # 设置索引值
BLPOP key timeout                  # 阻塞左弹
BRPOP key timeout                  # 阻塞右弹
RPOPLPUSH src dst                  # 转存
BRPOPLPUSH src dst timeout         # 阻塞转存
```

## 集合命令速查

```
SADD key m1 m2                     # 添加
SREM key m1                        # 移除
SMEMBERS key                       # 所有成员
SISMEMBER key m                    # 是否在集合中
SCARD key                          # 数量
SPOP key                           # 随机弹出
SRANDMEMBER key count              # 随机取样
SINTER k1 k2                       # 交集
SUNION k1 k2                       # 并集
SDIFF k1 k2                        # 差集
SINTERSTORE dest k1 k2             # 交集存
SUNIONSTORE dest k1 k2             # 并集存
SDIFFSTORE dest k1 k2              # 差集存
SSCAN key cursor                   # 渐进迭代
```

## 有序集合命令速查

```
ZADD key score member              # 添加
ZREM key member                    # 移除
ZRANGE key start stop [WITHSCORES] # 按排名取 (小到大)
ZREVRANGE key start stop [WS]      # 按排名取 (大到小)
ZRANGEBYSCORE key min max          # 按分数取
ZRANK key member                   # 排名 (小到大)
ZREVRANK key member                # 排名 (大到小)
ZSCORE key member                  # 分数
ZCARD key                          # 数量
ZINCRBY key n member               # 分数 +n
ZCOUNT key min max                 # 分数区间内数量
ZREM key member                    # 移除
ZREMRANGEBYRANK key start stop     # 移除排名区间
ZREMRANGEBYSCORE key min max       # 移除分数区间
ZINTERSTORE dest n keys [WEIGHTS]  # 交集
ZUNIONSTORE dest n keys [WEIGHTS]  # 并集
ZSCAN key cursor                   # 渐进迭代
```

## 发布订阅命令速查

```
SUBSCRIBE channel                  # 订阅
UNSUBSCRIBE channel                # 退订
PUBLISH channel message            # 发布
PSUBSCRIBE pattern                 # 模式订阅
PUNSUBSCRIBE pattern               # 模式退订
PUBSUB channels                    # 查看活跃频道
PUBSUB numsub channel              # 查看频道订阅数
```

## 脚本命令速查

```
EVAL script numkeys key [key] arg [arg]           # 执行 Lua
EVALSHA sha1 numkeys key [key] arg [arg]          # 通过 SHA1 执行缓存脚本
SCRIPT LOAD script                                 # 加载脚本到缓存
SCRIPT EXISTS sha1                                 # 检查脚本是否在缓存
SCRIPT FLUSH                                       # 清除脚本缓存
SCRIPT KILL                                        # 终止正在运行的脚本
```

## 连接命令速查

```
PING                               # 检查是否 alive
ECHO message                       # 回显
AUTH password                      # 认证
SELECT index                       # 选择数据库
QUIT                               # 关闭连接
```

## 服务器命令速查

```
INFO [section]                     # 服务器信息
CONFIG GET parameter               # 获取配置
CONFIG SET parameter value         # 修改配置 (运行时)
CONFIG REWRITE                     # 写入配置文件
DBSIZE                             # 当前数据库 key 数量
FLUSHDB                            # 清空当前库
FLUSHALL                           # 清空所有库
CLIENT LIST                        # 客户端列表
CLIENT KILL ip:port                # 杀死客户端连接
SLOWLOG GET n                      # 获取慢查询日志
MONITOR                            # 实时监控 (生产慎用)
SAVE                               # 同步保存 RDB
BGSAVE                             # 后台保存 RDB
BGREWRITEAOF                       # 重写 AOF
LASTSAVE                           # 最后保存时间
SHUTDOWN                           # 关闭服务器
SLAVEOF host port                  # 设置主从
ROLE                               # 查看角色
TIME                               # 服务器时间
DEBUG OBJECT key                   # key 调试信息
MEMORY USAGE key                   # 精确内存
MEMORY PURGE                       # 整理碎片
COMMAND                            # 命令统计
```
