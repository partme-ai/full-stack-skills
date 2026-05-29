# 示例：RMAN 备份策略 — 每周全量 + 每日增量

## 场景

为生产库制定一套完整的备份策略：每周日凌晨 Level 0 全量备份，周一至周六 Level 1 增量备份，同时备份归档日志。

## RMAN 配置

```bash
# 登录 RMAN
rman target /

# 配置备份策略（保留最近 7 天可恢复）
RMAN> CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 7 DAYS;

# 启用控制文件自动备份
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON;

# 启用备份优化（跳过未变更文件）
RMAN> CONFIGURE BACKUP OPTIMIZATION ON;

# 设置备份格式
RMAN> CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT '/backup/orcl/%U';

# 设置设备类型和并行度
RMAN> CONFIGURE DEVICE TYPE DISK PARALLELISM 2;
```

## 周日：Level 0 全量备份

```bash
rman target / <<EOF
RUN {
    ALLOCATE CHANNEL c1 DEVICE TYPE DISK;
    ALLOCATE CHANNEL c2 DEVICE TYPE DISK;
    BACKUP INCREMENTAL LEVEL 0 DATABASE
        TAG 'LEVEL0_WEEKLY'
        FORMAT '/backup/orcl/full_%d_%T_%s_%p.bkp';
    BACKUP ARCHIVELOG ALL DELETE INPUT
        FORMAT '/backup/orcl/arch_%d_%T_%s.bkp';
    BACKUP CURRENT CONTROLFILE
        FORMAT '/backup/orcl/ctrl_%d_%T_%s.bkp';
    RELEASE CHANNEL c1;
    RELEASE CHANNEL c2;
}
EOF
```

## 周一至周六：Level 1 增量备份

```bash
rman target / <<EOF
BACKUP INCREMENTAL LEVEL 1 DATABASE
    TAG 'LEVEL1_DAILY'
    FORMAT '/backup/orcl/incr_%d_%T_%s_%p.bkp';
BACKUP ARCHIVELOG ALL DELETE INPUT
    FORMAT '/backup/orcl/arch_%d_%T_%s.bkp';
EOF
```

## 验证备份

```bash
# 验证所有备份是否可恢复
rman target /
RMAN> RESTORE DATABASE VALIDATE;

# 列出备份集
RMAN> LIST BACKUP SUMMARY;
RMAN> LIST BACKUP OF DATABASE;

# 检查特定备份是否可用
RMAN> VALIDATE BACKUPSET <bs_key>;
```

## 模拟恢复

```bash
# 完全恢复（全量+增量自动应用）
rman target /
RMAN> STARTUP MOUNT;
RMAN> RESTORE DATABASE;
RMAN> RECOVER DATABASE;
RMAN> ALTER DATABASE OPEN;

# 时间点恢复（恢复到某个时间点）
rman target /
RMAN> STARTUP MOUNT;
RMAN> RESTORE DATABASE UNTIL TIME "TO_DATE('2024-08-15 14:30:00','YYYY-MM-DD HH24:MI:SS')";
RMAN> RECOVER DATABASE UNTIL TIME "TO_DATE('2024-08-15 14:30:00','YYYY-MM-DD HH24:MI:SS')";
RMAN> ALTER DATABASE OPEN RESETLOGS;
```

## Cron 调度

```bash
# 编辑 crontab
# crontab -e

# 每周日凌晨 1:00 执行全量备份
0 1 * * 0 /u01/scripts/full_backup.sh >> /u01/logs/rman_full.log 2>&1

# 每天凌晨 2:00 执行增量备份（周日除外）
0 2 * * 1-6 /u01/scripts/incr_backup.sh >> /u01/logs/rman_incr.log 2>&1

# 每天凌晨 3:00 验证备份
0 3 * * * /u01/scripts/validate_backup.sh >> /u01/logs/rman_val.log 2>&1
```
