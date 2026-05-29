# 示例：Data Guard 物理备库搭建

## 场景

生产库 PRIMARY (host1) 需要搭建一个物理备库 STANDBY (host2) 实现高可用，使用实时应用（Real-Time Apply）。

## 前提条件

- 主库已启用归档模式 (`SELECT log_mode FROM v$database;` 返回 `ARCHIVELOG`)
- 主备库 Oracle 版本一致
- 主备库网络互通（1521 端口）
- 主库已设置 `FORCE LOGGING`

## 步骤 1：主库参数配置

```sql
-- 设置 DB_UNIQUE_NAME
ALTER SYSTEM SET LOG_ARCHIVE_CONFIG='DG_CONFIG=(PRIMARY,STANDBY)' SCOPE=BOTH;
ALTER SYSTEM SET DB_UNIQUE_NAME=PRIMARY SCOPE=SPFILE;

-- 设置归档目的地
ALTER SYSTEM SET LOG_ARCHIVE_DEST_1='LOCATION=/u01/archivelog/orcl VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=PRIMARY' SCOPE=BOTH;

-- 备库归档传输（使用 ASYNC 模式，不影响主库性能）
ALTER SYSTEM SET LOG_ARCHIVE_DEST_2='SERVICE=standby_host:1521/orcl LGWR ASYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME=STANDBY' SCOPE=BOTH;
ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_2=ENABLE SCOPE=BOTH;

-- 网络配置
ALTER SYSTEM SET FAL_CLIENT='PRIMARY' SCOPE=BOTH;
ALTER SYSTEM SET FAL_SERVER='STANDBY' SCOPE=BOTH;

-- 文件路径转换
ALTER SYSTEM SET DB_FILE_NAME_CONVERT='/u01/oradata/orcl/','/u02/oradata/orcl/' SCOPE=SPFILE;
ALTER SYSTEM SET LOG_FILE_NAME_CONVERT='/u01/oradata/orcl/','/u02/oradata/orcl/' SCOPE=SPFILE;

-- 启用手动备库文件管理
ALTER SYSTEM SET STANDBY_FILE_MANAGEMENT=AUTO SCOPE=BOTH;

-- 重启数据库使 SPFILE 参数生效
SHUTDOWN IMMEDIATE;
STARTUP;
```

## 步骤 2：准备备库

```text
# 备库 $ORACLE_HOME/network/admin/tnsnames.ora 配置
PRIMARY =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = primary_host)(PORT = 1521))
    (CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = orcl))
  )

STANDBY =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = standby_host)(PORT = 1521))
    (CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = orcl))
  )

# 备库 $ORACLE_HOME/network/admin/listener.ora 配置
LISTENER =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = standby_host)(PORT = 1521))
  )
```

```sql
-- 备库参数文件（在备库创建 pfile，修改 db_unique_name）
-- 修改 /u01/app/oracle/admin/orcl/pfile/init.ora
-- *.db_unique_name='STANDBY'
```

## 步骤 3：使用 RMAN DUPLICATE 创建备库

```bash
# 在主库执行
rman target sys/password@PRIMARY auxiliary sys/password@STANDBY <<EOF
DUPLICATE TARGET DATABASE FOR STANDBY
  FROM ACTIVE DATABASE
  DORECOVER
  SPFILE
    SET db_unique_name='STANDBY' COMMENT 'Standby'
    SET LOG_ARCHIVE_DEST_1='LOCATION=/u01/archivelog/orcl VALID_FOR=(ALL_LOGFILES,ALL_ROLES) DB_UNIQUE_NAME=STANDBY'
    SET LOG_ARCHIVE_DEST_2='SERVICE=primary_host:1521/orcl LGWR ASYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME=PRIMARY'
    SET FAL_CLIENT='STANDBY'
    SET FAL_SERVER='PRIMARY'
    SET DB_FILE_NAME_CONVERT='/u02/oradata/orcl/','/u01/oradata/orcl/'
    SET LOG_FILE_NAME_CONVERT='/u02/oradata/orcl/','/u01/oradata/orcl/'
  NOFILENAMECHECK;
EOF
```

## 步骤 4：启动备库实时应用

```sql
-- 备库启动到 MOUNT 状态
STARTUP MOUNT;

-- 启用实时应用（备库自动应用归档日志）
ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE DISCONNECT;

-- 验证实时应用状态
SELECT process, status, sequence# FROM v$managed_standby;
-- 预期看到 MRP0 进程状态为 APPLYING_LOG
```

## 步骤 5：启用 Active Data Guard（可选）

```sql
-- 备库只读打开（19c 及以前）
ALTER DATABASE OPEN READ ONLY;
ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT;
-- 此时备库以只读方式打开，同时应用日志

-- 验证备库可用
SELECT database_role, open_mode FROM v$database;
-- 预期返回: PHYSICAL STANDBY / READ ONLY WITH APPLY
```

## 步骤 6：验证同步状态

```sql
-- 主库查询
SELECT database_role, open_mode FROM v$database;
SELECT dest_name, status, error FROM v$archive_dest WHERE dest_name LIKE '%DEST_2';

-- 备库查询日志应用延迟
SELECT name, value, time_computed FROM v$dataguard_stats WHERE name LIKE '%lag%';
-- apply_lag: 应用延迟（秒）
-- transport_lag: 传输延迟（秒）
```

## 步骤 7：Switchover 切换（计划内）

```bash
# 主库操作
sqlplus / as sysdba
ALTER DATABASE COMMIT TO SWITCHOVER TO STANDBY;
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;

# 备库操作
sqlplus / as sysdba
ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY;
ALTER DATABASE OPEN;
```
