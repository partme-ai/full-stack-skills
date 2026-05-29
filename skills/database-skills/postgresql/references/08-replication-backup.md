# 复制/备份/权限详解

## 流复制 (Streaming Replication)

### 主库配置

```conf
# postgresql.conf
wal_level = replica
max_wal_senders = 10
wal_keep_size = 1GB
hot_standby = on
```

```sql
-- pg_hba.conf
-- host replication replicator 192.168.1.0/24 md5

CREATE USER replicator WITH REPLICATION LOGIN PASSWORD 'strong_password';
```

### 从库搭建

```bash
# 清空从库数据目录
rm -rf /var/lib/postgresql/data/*

# 从主库拉取基础备份
pg_basebackup -h 192.168.1.100 -U replicator \
    -D /var/lib/postgresql/data -P -v --wal-method=stream

# PG 12+: 创建 standby.signal
touch /var/lib/postgresql/data/standby.signal

# 配置主库连接
echo "primary_conninfo = 'host=192.168.1.100 port=5432 user=replicator password=strong_password'" \
    >> /var/lib/postgresql/data/postgresql.auto.conf

# 启动从库
systemctl start postgresql

# 检查复制状态（主库）
SELECT * FROM pg_stat_replication;
# 从库
SELECT * FROM pg_stat_wal_receiver;
```

### 同步 vs 异步

```sql
-- 同步复制：主库等待从库确认
-- 配置: synchronous_standby_names = 'FIRST 1 (slave1, slave2)'
-- 数据零丢失，但写入延迟增加

-- 检查同步状态
SELECT application_name, state, sync_state, write_lag, flush_lag, replay_lag
FROM pg_stat_replication;
-- sync: 同步, async: 异步, potential: 候选同步
```

## 逻辑复制 (PG 10+)

```sql
-- 发布端
CREATE PUBLICATION my_pub FOR ALL TABLES;
CREATE PUBLICATION orders_pub FOR TABLE orders, order_items;
CREATE PUBLICATION paid_orders_pub FOR TABLE orders WHERE (status = 'paid');  -- PG 15+

-- 订阅端
CREATE SUBSCRIPTION my_sub
CONNECTION 'host=192.168.1.100 port=5432 dbname=mydb user=replicator password=strong_password'
PUBLICATION my_pub;

-- 管理
ALTER SUBSCRIPTION my_sub ENABLE;
ALTER SUBSCRIPTION my_sub DISABLE;
ALTER SUBSCRIPTION my_sub REFRESH PUBLICATION;
DROP SUBSCRIPTION my_sub;

-- 监控
SELECT * FROM pg_stat_subscription;
```

## 备份与恢复

### pg_dump — 逻辑备份

```bash
# SQL 格式
pg_dump -h localhost -U postgres -d mydb > mydb.sql

# 自定义格式（推荐）
pg_dump -h localhost -U postgres -d mydb -Fc -f mydb.dump

# 并行导出目录格式
pg_dump -h localhost -U postgres -d mydb -Fd -j 4 -f /backup/mydb/

# 只导出结构
pg_dump -h localhost -U postgres -d mydb -s -f mydb_schema.sql

# 指定表
pg_dump -h localhost -U postgres -d mydb -t orders -t users -f mydb_tables.sql

# 全局对象（角色、表空间）
pg_dumpall -h localhost -U postgres -g -f global_objects.sql
```

### pg_restore — 恢复

```bash
pg_restore -h localhost -U postgres -d mydb /backup/mydb.dump
pg_restore -h localhost -U postgres -d mydb -j 4 /backup/mydb.dump  # 并行
pg_restore -h localhost -U postgres -d mydb -t users /backup/mydb.dump  # 指定表

# SQL 文件恢复
psql -h localhost -U postgres -d mydb < mydb.sql
```

### WAL 归档与 PITR

```conf
# postgresql.conf
archive_mode = on
archive_command = 'cp %p /archive/%f'
wal_keep_size = 1GB
```

```bash
# 创建基础备份
pg_basebackup -h localhost -U postgres -D /backup/base -P -v --wal-method=stream

# PITR 恢复步骤:
# 1. 停止 PG
# 2. 用基础备份恢复数据目录
# 3. 创建 recovery.signal (PG 12+)
# 4. 配置 restore_command 和 recovery_target_time
# 5. 启动 PG
```

### pg_basebackup — 物理备份

```bash
# 基础用法
pg_basebackup -h localhost -U replicator -D /backup/pg_base -P -v --wal-method=stream

# 压缩 tar 格式
pg_basebackup -h localhost -U replicator -D /backup/pg_base -Ft -z -P -v

# 验证备份 (PG 13+)
pg_verifybackup /backup/pg_base
```

## 高可用工具

```bash
# Patroni (基于 etcd/consul/ZK)
# 自动故障转移 + 自动恢复
patroni /etc/patroni/patroni.yml

# repmgr
repmgr -f /etc/repmgr.conf primary register
repmgr -f /etc/repmgr.conf standby clone
repmgr -f /etc/repmgr.conf standby register
repmgr -f /etc/repmgr.conf standby switchover

# PgBouncer — 连接池
# Pgpool-II — 连接池 + 读写分离 + 负载均衡
```

## 权限管理

```sql
-- ROLE 管理
CREATE ROLE app_user WITH LOGIN PASSWORD 'password';
CREATE ROLE readonly_role;
CREATE ROLE readwrite_role;

-- 角色层级
GRANT readonly_role TO app_user;

-- Schema 权限
GRANT USAGE ON SCHEMA public TO readonly_role;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO readwrite_role;

-- 默认权限（未来新建表自动授权）
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly_role;

-- 序列、函数
GRANT USAGE, SELECT ON ALL SEQUENCES TO readwrite_role;
GRANT EXECUTE ON ALL FUNCTIONS TO readwrite_role;

-- RLS 行级安全（多租户隔离）
CREATE TABLE tenant_orders (id BIGSERIAL PRIMARY KEY, tenant_id INTEGER NOT NULL, ...);
ALTER TABLE tenant_orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON tenant_orders
    USING (tenant_id = current_setting('app.tenant_id')::INTEGER);

ALTER TABLE tenant_orders FORCE ROW LEVEL SECURITY;
SET app.tenant_id = '1001';  -- 应用层设置
```

## 扩展

```sql
-- PostGIS: CREATE EXTENSION postgis;
-- pgvector: CREATE EXTENSION vector;
-- pg_stat_statements: CREATE EXTENSION pg_stat_statements;
-- uuid-ossp: CREATE EXTENSION "uuid-ossp";
-- pgcrypto: CREATE EXTENSION pgcrypto;
-- citext: CREATE EXTENSION citext;
-- pg_trgm: CREATE EXTENSION pg_trgm;
-- unaccent: CREATE EXTENSION unaccent;
```
