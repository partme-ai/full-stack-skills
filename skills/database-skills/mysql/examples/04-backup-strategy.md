# 示例: 生产环境备份策略

## 场景

日活 10 万用户的电商平台，MySQL 总数据量约 200GB，需要 24×7 运行，无法接受超过 30 分钟的数据丢失。

## 备份策略

```
全量备份:    每天 02:00 (XtraBackup 物理备份)
增量备份:    每 6 小时 (XtraBackup 增量)
二进制日志:  实时归档 (自动备份到 S3)
保留周期:    7 天全量 + 30 天增量 + 90 天 Binlog
异地备份:    同步到阿里云 OSS (跨区域复制)
恢复演练:    每月一次
```

## 备份脚本

### 全量备份脚本

```bash
#!/bin/bash
# /usr/local/bin/backup_full.sh

BACKUP_DIR="/data/backup/mysql"
DATE=$(date +%Y%m%d_%H%M%S)
FULL_DIR="${BACKUP_DIR}/full/${DATE}"
MYSQL_USER="backup_user"
MYSQL_PASS="$(cat /etc/mysql/backup_pass)"

# 创建备份目录
mkdir -p ${FULL_DIR}

# 执行 XtraBackup 全量备份
xtrabackup --backup \
  --user=${MYSQL_USER} \
  --password=${MYSQL_PASS} \
  --target-dir=${FULL_DIR} \
  --compress \
  --compress-threads=4 \
  --parallel=4 2>>/var/log/xtrabackup.log

if [ $? -eq 0 ]; then
  echo "[$(date)] Full backup completed: ${FULL_DIR}" >> /var/log/backup.log
  
  # 同步到 OSS
  ossutil sync ${FULL_DIR} oss://myapp-backup/mysql/full/${DATE}/ \
    --delete --force 2>>/var/log/oss_backup.log
    
  # 清理 7 天前的全量备份
  find ${BACKUP_DIR}/full/ -type d -mtime +7 -exec rm -rf {} \;
  echo "[$(date)] Full backup synced to OSS" >> /var/log/backup.log
else
  echo "[$(date)] Full backup FAILED!" >> /var/log/backup.log
  curl -X POST -H "Content-Type: application/json" \
    -d '{"msg":"MySQL 全量备份失败"}' \
    https://alert.example.com/notify
fi
```

### 增量备份脚本

```bash
#!/bin/bash
# /usr/local/bin/backup_inc.sh

BACKUP_DIR="/data/backup/mysql"
DATE=$(date +%Y%m%d_%H%M%S)
INC_DIR="${BACKUP_DIR}/inc/${DATE}"
MYSQL_USER="backup_user"
MYSQL_PASS="$(cat /etc/mysql/backup_pass)"
LATEST_FULL=$(ls -td ${BACKUP_DIR}/full/*/ | head -1)

# 找最近的备份作为增量基准备份
if [ -z "$(ls -A ${BACKUP_DIR}/inc/ 2>/dev/null)" ]; then
  BASEDIR="${LATEST_FULL}"
else
  BASEDIR=$(ls -td ${BACKUP_DIR}/inc/*/ | head -1)
fi

mkdir -p ${INC_DIR}

xtrabackup --backup \
  --user=${MYSQL_USER} \
  --password=${MYSQL_PASS} \
  --target-dir=${INC_DIR} \
  --incremental-basedir=${BASEDIR} \
  --compress \
  --compress-threads=4 \
  --parallel=4 2>>/var/log/xtrabackup.log

if [ $? -eq 0 ]; then
  echo "[$(date)] Incremental backup completed" >> /var/log/backup.log
  ossutil sync ${INC_DIR} oss://myapp-backup/mysql/inc/${DATE}/ \
    --delete --force 2>>/var/log/oss_backup.log
  find ${BACKUP_DIR}/inc/ -type d -mtime +30 -exec rm -rf {} \;
else
  echo "[$(date)] Incremental backup FAILED!" >> /var/log/backup.log
  curl -X POST -H "Content-Type: application/json" \
    -d '{"msg":"MySQL 增量备份失败"}' \
    https://alert.example.com/notify
fi
```

### Binlog 实时归档

```bash
#!/bin/bash
# /usr/local/bin/archive_binlog.sh

BINLOG_DIR="/var/log/mysql"
ARCHIVE_DIR="/data/backup/binlog"
FILES=($(ls -1t ${BINLOG_DIR}/mysql-bin.* 2>/dev/null))

# 排除当前正在使用的 binlog
CURRENT=$(mysql -e "SHOW MASTER STATUS\G" | grep File | awk '{print $2}')
for FILE in "${FILES[@]}"; do
  BASENAME=$(basename $FILE)
  if [ "$BASENAME" != "$CURRENT" ] && [ ! -f "${ARCHIVE_DIR}/${BASENAME}.gz" ]; then
    gzip -c $FILE > ${ARCHIVE_DIR}/${BASENAME}.gz
    ossutil cp ${ARCHIVE_DIR}/${BASENAME}.gz oss://myapp-backup/binlog/
    echo "[$(date)] Archived: ${BASENAME}" >> /var/log/binlog_archive.log
    
    # 删除本地归档后的 binlog 释放空间
    mysql -e "PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 7 DAY);"
  fi
done
```

## 恢复流程

### 完整恢复步骤

```bash
#!/bin/bash
# /usr/local/bin/restore_mysql.sh

RESTORE_DATE=$1  # 格式: 2024-03-15 10:30:00

# 1. 从 OSS 下载最近的全量备份
ossutil cp -r oss://myapp-backup/mysql/full/latest/ /tmp/restore/full/
echo "Step 1: Full backup downloaded"

# 2. 准备全量备份
xtrabackup --prepare --target-dir=/tmp/restore/full/ --apply-log-only
echo "Step 2: Full backup prepared"

# 3. 按需合并增量备份
for inc in $(ossutil ls oss://myapp-backup/mysql/inc/ | sort); do
  ossutil cp -r $inc /tmp/restore/inc/
  xtrabackup --prepare --target-dir=/tmp/restore/full/ \
    --incremental-dir=/tmp/restore/inc/ --apply-log-only
  echo "Step 3: Incremental ${inc} merged"
done

# 4. 最终准备（非 apply-log-only，回滚未提交事务）
xtrabackup --prepare --target-dir=/tmp/restore/full/
echo "Step 4: Final prepare done"

# 5. 停止 MySQL，替换数据目录
systemctl stop mysqld
mv /var/lib/mysql /var/lib/mysql_bak
xtrabackup --copy-back --target-dir=/tmp/restore/full/
chown -R mysql:mysql /var/lib/mysql
echo "Step 5: Data restored"

# 6. 启动 MySQL
systemctl start mysqld
echo "Step 6: MySQL started"

# 7. 回放 Binlog 到指定时间点（PITR）
mysqlbinlog --stop-datetime="${RESTORE_DATE}" \
  /data/backup/binlog/mysql-bin.* | mysql -u root -p
echo "Step 7: PITR applied to ${RESTORE_DATE}"
```

## 定时作业配置

```bash
# crontab -e

# 每天 02:00 全量备份
0 2 * * * /usr/local/bin/backup_full.sh

# 每 6 小时增量备份
0 */6 * * * /usr/local/bin/backup_inc.sh

# 每小时检查并归档 binlog
0 * * * * /usr/local/bin/archive_binlog.sh

# 每天 06:00 检查备份完整性
0 6 * * * /usr/local/bin/check_backup.sh
```

## 恢复演练计划

```
每月第一周周日凌晨 2:00 执行：

1. 在测试环境恢复最近的全量备份
2. 应用增量备份
3. 执行 PITR 到指定时间点
4. 验证数据完整性：
   - 检查关键表行数
   - 验证最近订单数据
   - 运行业务自检脚本
5. 记录恢复耗时，持续优化

目标 RTO: < 2 小时
目标 RPO: < 30 分钟
```
