# 备份与恢复 (Backup & Restore)

## 简介

MySQL 备份分为逻辑备份（mysqldump）和物理备份（XtraBackup）。逻辑备份导出 SQL 语句，适合小规模和迁移场景；物理备份直接复制数据文件，适合大数据库的快速恢复。

## mysqldump — 逻辑备份

### 基本用法

```bash
# 备份单个数据库（推荐使用 --single-transaction 避免锁表）
mysqldump -u root -p --single-transaction --routines --triggers --events shop > shop_backup.sql

# 备份所有数据库
mysqldump -u root -p --all-databases --single-transaction > all_db_backup.sql

# 只备份表结构
mysqldump -u root -p --no-data shop > shop_schema.sql

# 只备份数据
mysqldump -u root -p --no-create-info shop > shop_data.sql

# 压缩备份
mysqldump -u root -p shop | gzip > shop_backup.sql.gz

# 备份特定表
mysqldump -u root -p shop user order product > critical_tables.sql

# 备份到远程服务器
mysqldump -u root -p shop | ssh user@backup-server "cat > /backups/shop.sql"
```

### 关键参数说明

| 参数 | 说明 | 推荐 |
|------|------|------|
| `--single-transaction` | InnoDB 事务一致性备份，不锁表 | **必选**（InnoDB） |
| `--lock-tables` | MyISAM 表锁 | 仅 MyISAM 时需要 |
| `--routines` | 备份存储过程和函数 | ✅ 推荐 |
| `--triggers` | 备份触发器 | ✅ 推荐 |
| `--events` | 备份事件调度器 | ✅ 推荐 |
| `--quick` | 逐行导出（防止大表内存溢出） | ✅ 大表推荐 |
| `--opt` | 快速导出（默认开启） | 默认 |

### 恢复

```bash
# 基本恢复
mysql -u root -p shop < shop_backup.sql

# 恢复压缩备份
gunzip < shop_backup.sql.gz | mysql -u root -p shop

# 恢复多个数据库
mysql -u root -p < all_db_backup.sql
```

## XtraBackup — 物理备份

Percona XtraBackup 是 MySQL 物理备份的事实标准，支持热备份 InnoDB 表而不影响读写。

### 安装

```bash
# macOS
brew install percona-xtrabackup

# Ubuntu
apt install percona-xtrabackup-80

# CentOS
yum install percona-xtrabackup-80
```

### 全量备份与恢复

```bash
# 全量备份
xtrabackup --backup --target-dir=/data/backup/full/ --user=root --password=xxx

# 准备恢复（应用 redo log，使数据一致）
xtrabackup --prepare --target-dir=/data/backup/full/

# 恢复到 MySQL 数据目录
xtrabackup --copy-back --target-dir=/data/backup/full/
# 或手动复制
rsync -avrP /data/backup/full/ /var/lib/mysql/
chown -R mysql:mysql /var/lib/mysql/
```

### 增量备份与恢复

```bash
# 全量备份（基础）
xtrabackup --backup --target-dir=/data/backup/full/

# 增量备份（基于全量）
xtrabackup --backup --target-dir=/data/backup/inc1/ \
  --incremental-basedir=/data/backup/full/

# 第二个增量备份（基于前一个增量）
xtrabackup --backup --target-dir=/data/backup/inc2/ \
  --incremental-basedir=/data/backup/inc1/

# 增量恢复流程
# 1. 准备全量（应用 log 但不回滚未提交事务）
xtrabackup --prepare --apply-log-only --target-dir=/data/backup/full/

# 2. 合并增量 1
xtrabackup --prepare --apply-log-only --target-dir=/data/backup/full/ \
  --incremental-dir=/data/backup/inc1/

# 3. 合并增量 2（最后一次不用 --apply-log-only）
xtrabackup --prepare --target-dir=/data/backup/full/ \
  --incremental-dir=/data/backup/inc2/

# 4. copy-back 恢复
xtrabackup --copy-back --target-dir=/data/backup/full/
```

## 二进制日志与 PITR（时间点恢复）

PITR（Point-In-Time Recovery）允许恢复到某个精确的时间点，是应对误操作（DROP TABLE、DELETE 全表）的核心手段。

### 启用二进制日志

```ini
# my.cnf
log_bin = /var/log/mysql/mysql-bin
binlog_format = ROW         # ROW 格式最安全
binlog_expire_logs_seconds = 604800  # 保留 7 天
```

### 查看二进制日志

```sql
-- 查看 Binlog 是否开启
SHOW VARIABLES LIKE 'log_bin';

-- 列出所有 Binlog 文件
SHOW BINARY LOGS;

-- 查看 Binlog 事件
SHOW BINLOG EVENTS IN 'mysql-bin.000001' LIMIT 10;

-- 查看当前 Binlog 位置
SHOW MASTER STATUS;
```

### PITR 恢复流程

```bash
# Step 1: 恢复最近的完整备份
mysql -u root -p shop < shop_backup.sql

# Step 2: 回放二进制日志到指定时间点
mysqlbinlog --stop-datetime="2024-01-15 10:00:00" \
  /var/log/mysql/mysql-bin.* | mysql -u root -p

# 指定位置恢复
mysqlbinlog --stop-position=12345 \
  /var/log/mysql/mysql-bin.000001 | mysql -u root -p

# 指定开始和结束范围
mysqlbinlog \
  --start-datetime="2024-01-15 09:00:00" \
  --stop-datetime="2024-01-15 10:00:00" \
  /var/log/mysql/mysql-bin.000001 \
  /var/log/mysql/mysql-bin.000002 \
  | mysql -u root -p shop
```

## 备份策略推荐

### 生产环境备份策略

```
┌──────────────────────────────────────────────┐
│ 生产环境备份策略：                              │
│                                               │
│ 每日凌晨 2:00: 全量备份 (XtraBackup 物理备份)    │
│ 每 6 小时:      增量备份 (XtraBackup 增量)       │
│ 实时:           二进制日志持续归档 (BINLOG)       │
│ 保留周期:       最近 7 天全量 + 30 天增量         │
│ 异地备份:       备份文件同步到对象存储 (OSS/S3)    │
│ 定期演练:       每月一次恢复测试                   │
└──────────────────────────────────────────────┘
```

### 备份检查清单

- [ ] 全量备份是否成功（检查 `xtrabackup` 退出码）
- [ ] 备份文件大小是否合理（过大/过小要排查）
- [ ] 异地备份是否同步完成
- [ ] 二进制日志是否连续不中断
- [ ] 每月恢复演练验证备份可用性
- [ ] 备份保留策略是否符合合规要求

## 注意事项

- **不要只依赖一种备份方式**：逻辑备份 + 物理备份 + Binlog 三者配合
- **测试恢复**：定期在测试环境演练恢复流程，确保备份可用
- **监控备份状态**：通过脚本监控备份成功率，发送告警
- **备份加密**：敏感数据的备份文件应加密存储
- **备份压缩**：物理备份建议用 `--compress` 参数，可节省 3-5 倍存储空间
- **mysqldump 对超大表（> 50GB）不适用**：导出和导入都极慢，建议用 XtraBackup
