# 流复制搭建示例

## 场景：搭建一主一从的高可用架构

### 主库配置

```conf
# postgresql.conf 配置
listen_addresses = 'localhost,192.168.1.100'
wal_level = replica
max_wal_senders = 10
wal_keep_size = 1GB
hot_standby = on
```

```bash
# 重启主库
systemctl restart postgresql
```

### 创建复制用户

```sql
-- 在主库执行
CREATE USER replicator WITH REPLICATION LOGIN PASSWORD 'Str0ng!Pass';
```

```bash
# 在 pg_hba.conf 添加
echo 'host replication replicator 192.168.1.0/24 md5' >> /var/lib/pgsql/data/pg_hba.conf

# 重新加载配置
psql -c "SELECT pg_reload_conf();"
```

### 从库搭建

```bash
# 安装相同版本 PostgreSQL

# 停从库
systemctl stop postgresql

# 清空从库数据目录
rm -rf /var/lib/pgsql/data/*

# 从主库拉取基础备份
pg_basebackup -h 192.168.1.100 -U replicator \
    -D /var/lib/pgsql/data -P -v --wal-method=stream

# PG 12+: 创建 standby 信号文件
touch /var/lib/pgsql/data/standby.signal

# 配置主库连接信息
cat > /var/lib/pgsql/data/postgresql.auto.conf << EOF
primary_conninfo = 'host=192.168.1.100 port=5432 user=replicator password=Str0ng!Pass'
EOF

# 启动从库
systemctl start postgresql
```

### 验证复制

```sql
-- 在主库检查复制状态
SELECT pid, application_name, state, sync_state,
       write_lag, flush_lag, replay_lag
FROM pg_stat_replication;

-- 在从库检查接收状态
SELECT pid, status, receive_start_lsn, received_lsn,
       latest_end_lsn, latest_end_time
FROM pg_stat_wal_receiver;

-- 测试: 在主库创建表并插入数据
CREATE TABLE test_replication (id SERIAL PRIMARY KEY, data TEXT, ts TIMESTAMPTZ DEFAULT NOW());
INSERT INTO test_replication (data) VALUES ('hello from primary');

-- 在从库验证（从库为只读模式）
SELECT * FROM test_replication;
```

### 故障转移

```bash
# 手动提升从库为主库
# 在从库执行
pg_ctl promote -D /var/lib/pgsql/data
# 或
systemctl stop postgresql
# 删除 standby.signal 后启动
rm /var/lib/pgsql/data/standby.signal
systemctl start postgresql

# 此时原从库变为可读写
```

### 常见问题排查

```bash
# 查看复制日志
tail -f /var/lib/pgsql/data/log/postgresql-*.log

# 检查网络连通性
psql -h 192.168.1.100 -U replicator -d postgres -c "SELECT 1"

# 检查 WAL 发送进程
ps aux | grep wal_sender

# 检查磁盘空间（WAL 堆积会导致磁盘满）
df -h /var/lib/pgsql/data/
```
