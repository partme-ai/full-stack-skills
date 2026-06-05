# Redis Cluster 搭建与运维示例

## 1. 最小生产集群 (3主3从)

```bash
# 6 个节点目录
mkdir -p /data/redis/{7000,7001,7002,7003,7004,7005}

# 每个节点 redis.conf
cat > /data/redis/7000/redis.conf << 'EOF'
port 7000
cluster-enabled yes
cluster-config-file nodes-7000.conf
cluster-node-timeout 5000
appendonly yes
appendfsync everysec
protected-mode no
bind 0.0.0.0
daemonize yes
logfile /var/log/redis/7000.log
EOF

# 启动 6 个节点
redis-server /data/redis/7000/redis.conf
redis-server /data/redis/7001/redis.conf
redis-server /data/redis/7002/redis.conf
redis-server /data/redis/7003/redis.conf
redis-server /data/redis/7004/redis.conf
redis-server /data/redis/7005/redis.conf

# 创建集群 (Redis 5+)
redis-cli --cluster create \
    192.168.1.100:7000 192.168.1.100:7001 192.168.1.100:7002 \
    192.168.1.100:7003 192.168.1.100:7004 192.168.1.100:7005 \
    --cluster-replicas 1
```

## 2. 集群运维命令

```bash
# 检查集群状态
redis-cli -c -h 192.168.1.100 -p 7000 cluster info
redis-cli -c -h 192.168.1.100 -p 7000 cluster nodes

# 重新平衡 slot
redis-cli --cluster rebalance 192.168.1.100:7000 \
    --cluster-weight node1=1 node2=2 node3=1 \
    --cluster-use-empty-masters

# 修复集群
redis-cli --cluster fix 192.168.1.100:7000

# 动态扩容：添加节点
redis-cli --cluster add-node 新节点:7006 已有节点:7000 --cluster-slave
redis-cli --cluster reshard 已有节点:7000 --cluster-from all \
    --cluster-to 新节点id --cluster-slots 1000 --cluster-yes
```

## 3. 数据迁移方案

```bash
# 使用 redis-shake 跨集群迁移
redis-shake.linux -type sync -conf redis-shake.conf

# redis-shake.conf 示例
source.type = cluster
source.address = 192.168.1.100:7000
target.type = cluster
target.address = 192.168.1.200:7000
```
