# Redis 生产配置最佳实践

## 推荐生产配置 (redis.conf)

```conf
# ────────────────────────────────────
# 基础配置
# ────────────────────────────────────
daemonize no
pidfile /var/run/redis_6379.pid
port 6379
bind 0.0.0.0                        # 生产环境改为内网 IP
protected-mode yes

# ────────────────────────────────────
# 内存管理
# ────────────────────────────────────
maxmemory 4gb
maxmemory-policy allkeys-lru
maxmemory-samples 10                # LRU 采样样本数 (越大越精确)

# ────────────────────────────────────
# 持久化 — 混合模式
# ────────────────────────────────────
save 900 1
save 300 10
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb
dir /data/redis/

appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes
aof-use-rdb-preamble yes             # 混合持久化 (Redis 4.0+)

# ────────────────────────────────────
# 网络与连接
# ────────────────────────────────────
tcp-backlog 511
timeout 300
tcp-keepalive 300
maxclients 10000

# ────────────────────────────────────
# 复制
# ────────────────────────────────────
replica-serve-stale-data yes
replica-read-only yes
repl-diskless-sync no
repl-diskless-sync-delay 5
repl-disable-tcp-nodelay no
replica-priority 100

# ────────────────────────────────────
# 安全
# ────────────────────────────────────
requirepass your-strong-password-here
rename-command FLUSHALL ""
rename-command FLUSHDB ""
rename-command CONFIG ""
rename-command SHUTDOWN ""
rename-command DEBUG ""
rename-command SLAVEOF ""

# ────────────────────────────────────
# 慢查询日志
# ────────────────────────────────────
slowlog-log-slower-than 10000       # 记录 >10ms 的命令
slowlog-max-len 128

# ────────────────────────────────────
# 高级配置
# ────────────────────────────────────
hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-size -2
list-compress-depth 0
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64

hz 10
dynamic-hz yes
activedefrag yes                     # 自动碎片整理 (Redis 4.0+)
```

## Docker 部署

```bash
# 单机 Redis
docker run -d --name redis \
    -p 6379:6379 \
    -v /data/redis/data:/data \
    -v /data/redis/redis.conf:/usr/local/etc/redis/redis.conf \
    redis:7-alpine redis-server /usr/local/etc/redis/redis.conf

# Redis Cluster
docker network create redis-cluster

for port in 7000 7001 7002 7003 7004 7005; do
    mkdir -p /data/redis/${port}
    docker run -d --name redis-${port} \
        --net redis-cluster \
        -p ${port}:${port} \
        -v /data/redis/${port}:/data \
        redis:7-alpine redis-server \
            --port ${port} \
            --cluster-enabled yes \
            --cluster-config-file nodes.conf \
            --cluster-node-timeout 5000 \
            --appendonly yes
done

# 创建集群
docker exec redis-7000 redis-cli --cluster create \
    192.168.1.100:7000 192.168.1.100:7001 192.168.1.100:7002 \
    192.168.1.100:7003 192.168.1.100:7004 192.168.1.100:7005 \
    --cluster-replicas 1
```

## 性能调优检查清单

- [ ] `maxmemory` 设置为物理内存的 60-70%
- [ ] `maxmemory-policy` 设为 `allkeys-lru`（缓存场景）
- [ ] 禁用危险命令（FLUSHALL/CONFIG/EVAL...）
- [ ] 慢查询阈值 ≤ 10ms
- [ ] 连接池配置合理（maxTotal ≤ maxclients）
- [ ] Big Key 已拆分或索引
- [ ] 不分业务混用实例
- [ ] 监控指标已接入（INFO 命令定期采集）
- [ ] RDB + AOF 混合持久化已配置
- [ ] 主从 / Sentinel / Cluster 已部署
