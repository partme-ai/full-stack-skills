# 备份与恢复 — RMAN / EXPDP / IMPDP / 归档

## RMAN 备份

```sql
-- 连接 RMAN
-- rman target /

-- 全库备份（含归档日志）
RMAN> BACKUP DATABASE PLUS ARCHIVELOG DELETE INPUT;

-- 增量备份 Level 0（基础）
RMAN> BACKUP INCREMENTAL LEVEL 0 DATABASE PLUS ARCHIVELOG;

-- 增量备份 Level 1（差异）
RMAN> BACKUP INCREMENTAL LEVEL 1 DATABASE;

-- 表空间备份
RMAN> BACKUP TABLESPACE tbs_app_data;

-- 数据文件备份
RMAN> BACKUP DATAFILE '/u01/oradata/orcl/app_data01.dbf';

-- 控制文件/归档日志备份
RMAN> BACKUP CURRENT CONTROLFILE;
RMAN> BACKUP ARCHIVELOG ALL DELETE INPUT;
```

## RMAN 恢复

```sql
-- 全库恢复
RMAN> STARTUP MOUNT;
RMAN> RESTORE DATABASE;
RMAN> RECOVER DATABASE;
RMAN> ALTER DATABASE OPEN;

-- 时间点恢复（不完全恢复）
RMAN> STARTUP MOUNT;
RMAN> RESTORE DATABASE UNTIL TIME "TO_DATE('2024-08-15 14:00:00','YYYY-MM-DD HH24:MI:SS')";
RMAN> RECOVER DATABASE UNTIL TIME "...";
RMAN> ALTER DATABASE OPEN RESETLOGS;

-- 表空间恢复
RMAN> SQL "ALTER TABLESPACE tbs_app_data OFFLINE IMMEDIATE";
RMAN> RESTORE TABLESPACE tbs_app_data;
RMAN> RECOVER TABLESPACE tbs_app_data;
RMAN> SQL "ALTER TABLESPACE tbs_app_data ONLINE";

-- 验证备份
RMAN> RESTORE DATABASE VALIDATE;

-- 备份策略配置
RMAN> CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 7 DAYS;
RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON;
RMAN> CONFIGURE BACKUP OPTIMIZATION ON;
```

## 逻辑备份（EXPDP / IMPDP）

```sql
-- 导出全库
-- expdp system/password DIRECTORY=dp_dir DUMPFILE=full_export.dmp FULL=Y

-- 导出指定模式
-- expdp system/password DIRECTORY=dp_dir DUMPFILE=hr_export.dmp SCHEMAS=HR

-- 导出指定表
-- expdp hr/password DIRECTORY=dp_dir DUMPFILE=emp_export.dmp TABLES=employees,departments

-- 条件导出
-- expdp hr/password DIRECTORY=dp_dir DUMPFILE=emp_dept50.dmp TABLES=employees QUERY='employees:"WHERE department_id = 50"'

-- 并行导出
-- expdp hr/password DIRECTORY=dp_dir DUMPFILE=hr_%U.dmp SCHEMAS=HR PARALLEL=4

-- 全库导入
-- impdp system/password DIRECTORY=dp_dir DUMPFILE=full_export.dmp FULL=Y

-- 导入并重映射表空间/模式
-- impdp system/password DIRECTORY=dp_dir DUMPFILE=hr_export.dmp REMAP_SCHEMAS=HR:HR_NEW REMAP_TABLESPACE=USERS:TBS_APP_DATA

-- 跳过已存在对象
-- impdp hr/password DIRECTORY=dp_dir DUMPFILE=hr_export.dmp TABLE_EXISTS_ACTION=SKIP
-- TABLE_EXISTS_ACTION: SKIP / APPEND / TRUNCATE / REPLACE
```

## 归档日志模式

```sql
-- 查看当前日志模式
SELECT log_mode FROM v$database;

-- 启用归档日志模式
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE ARCHIVELOG;
ALTER DATABASE OPEN;

-- 禁用归档日志模式
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE NOARCHIVELOG;
ALTER DATABASE OPEN;

-- 归档日志管理
ALTER SYSTEM SET log_archive_dest_1='LOCATION=/u01/archivelog/orcl' SCOPE=BOTH;
ALTER SYSTEM SET log_archive_format='orcl_%t_%s_%r.arc' SCOPE=SPFILE;
ALTER SYSTEM SWITCH LOGFILE;

-- 查看归档日志
SELECT * FROM v$archived_log ORDER BY sequence#;
SELECT * FROM v$recovery_file_dest;
ALTER SYSTEM SET db_recovery_file_dest_size = 200G;
```
