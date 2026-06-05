# 示例: 主从复制搭建

## 场景

为电商平台搭建一主一从架构，实现读写分离和基本高可用。主库处理 DML（写），从库处理 SELECT（读）。

## 环境

- Master: 192.168.1.100:3306
- Slave: 192.168.1.101:3306
- MySQL 8.0.x

## 步骤

### Step 1: Master 配置

编辑 `/etc/my.cnf`：

```ini
[mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin
binlog_format = ROW
binlog_expire_logs_seconds = 604800
sync_binlog = 1
innodb_flush_log_at_trx_commit = 1
```

重启 MySQL：`systemctl restart mysqld`

### Step 2: Master 创建复制用户

```sql
CREATE USER 'replicator'@'192.168.1.101' IDENTIFIED BY 'StrongPassword123!';
GRANT REPLICATION SLAVE ON *.* TO 'replicator'@'192.168.1.101';
FLUSH PRIVILEGES;
```

### Step 3: 记录 Master 二进制日志位置

```sql
FLUSH TABLES WITH READ LOCK;  -- 锁住所有表
SHOW MASTER STATUS;
-- 输出:
-- File: mysql-bin.000042
-- Position: 841236
```

> **注意**：新开一个终端会话执行 `SHOW MASTER STATUS`，不要在锁会话中执行，否则锁会一直持有。

### Step 4: 初始数据同步

```bash
# 在 Master 上导出数据
mysqldump -u root -p --all-databases --single-transaction --master-data=2 > /tmp/mysql_full.sql

# 复制到 Slave
scp /tmp/mysql_full.sql root@192.168.1.101:/tmp/

# 解锁 Master
UNLOCK TABLES;
```

### Step 5: Slave 配置

编辑 `/etc/my.cnf`：

```ini
[mysqld]
server-id = 2
relay_log = /var/log/mysql/mysql-relay-bin
read_only = 1
log_slave_updates = 0          # 可选：记录从库更新到 binlog
skip_slave_start = 1           # 防止自动启动复制
```

重启 MySQL：`systemctl restart mysqld`

### Step 6: Slave 恢复初始数据

```bash
mysql -u root -p < /tmp/mysql_full.sql
```

### Step 7: 配置复制

```sql
CHANGE MASTER TO
  MASTER_HOST = '192.168.1.100',
  MASTER_PORT = 3306,
  MASTER_USER = 'replicator',
  MASTER_PASSWORD = 'StrongPassword123!',
  MASTER_LOG_FILE = 'mysql-bin.000042',
  MASTER_LOG_POS = 841236;

START SLAVE;
```

### Step 8: 验证复制

```sql
SHOW SLAVE STATUS\G
-- Slave_IO_Running: Yes
-- Slave_SQL_Running: Yes
-- Seconds_Behind_Master: 0
```

### Step 9: 测试

```sql
-- Master 上插入测试数据
INSERT INTO test.replication_test VALUES (1, 'hello');

-- Slave 上验证
SELECT * FROM test.replication_test;  -- 应该看到数据
```

## 验证脚本

```bash
#!/bin/bash
# check_replication.sh

IO_STATUS=$(mysql -e "SHOW SLAVE STATUS\G" | grep "Slave_IO_Running" | awk '{print $2}')
SQL_STATUS=$(mysql -e "SHOW SLAVE STATUS\G" | grep "Slave_SQL_Running" | awk '{print $2}')
LAG=$(mysql -e "SHOW SLAVE STATUS\G" | grep "Seconds_Behind_Master" | awk '{print $2}')

if [ "$IO_STATUS" = "Yes" ] && [ "$SQL_STATUS" = "Yes" ]; then
    echo "Replication OK. Lag: ${LAG}s"
    exit 0
else
    echo "Replication ERROR!"
    exit 1
fi
```

## 常见问题排查

| 问题 | 检查 | 解决方案 |
|------|------|---------|
| Slave_IO_Running: Connecting | 网络连通性 | `ping 192.168.1.100`，检查防火墙 3306 |
| Slave_IO_Running: No | 复制用户权限 | 检查 MASTER_USER/MASTER_PASSWORD |
| 主键冲突 | 初始数据不一致 | `SET GLOBAL sql_slave_skip_counter = 1;` |
| 复制延迟高 | Slave 性能 | 升级硬件、开启并行复制 |
