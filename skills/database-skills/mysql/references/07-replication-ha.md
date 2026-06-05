# 主从复制与高可用 (Replication & High Availability)

## 简介

MySQL 主从复制是生产环境中最常用的高可用和读写分离方案。主库（Master）记录二进制日志（Binlog），从库（Slave）通过网络读取并回放日志，实现数据同步。

## 复制原理

```
┌─────────────┐          ┌─────────────┐
│   Master    │          │   Slave     │
├─────────────┤          ├─────────────┤
│   Binlog    │─────→    │ Relay Log   │
│  (二进制日志) │  IO线程  │  (中继日志)  │
└─────────────┘          └──────┬──────┘
                               │ SQL线程
                               ▼
                           ┌─────────────┐
                           │  Slave Data  │
                           └─────────────┘
```

**复制流程**：
1. Master 提交事务时写入 Binlog
2. Slave 的 IO 线程读取 Master 的 Binlog，写入 Relay Log
3. Slave 的 SQL 线程回放 Relay Log，应用到自身数据

## 主从同步配置

### Master 配置

```ini
# my.cnf
server-id = 1
log_bin = /var/log/mysql/mysql-bin
binlog_format = ROW             # ROW 格式最安全（推荐）
binlog_expire_logs_seconds = 604800  # 保留 7 天
sync_binlog = 1                 # 每次事务提交同步（最安全）
```

```sql
-- 创建复制用户
CREATE USER 'replicator'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replicator'@'%';
FLUSH PRIVILEGES;

-- 查看 Master 状态
SHOW MASTER STATUS;
-- File: mysql-bin.000001, Position: 1234
```

### Slave 配置

```ini
# my.cnf
server-id = 2
relay_log = /var/log/mysql/mysql-relay-bin
read_only = 1                   # 只读（防止误写）
```

```sql
-- 设置主节点
CHANGE MASTER TO
  MASTER_HOST = '192.168.1.100',
  MASTER_PORT = 3306,
  MASTER_USER = 'replicator',
  MASTER_PASSWORD = 'password',
  MASTER_LOG_FILE = 'mysql-bin.000001',
  MASTER_LOG_POS = 1234;

-- 启动复制
START SLAVE;

-- 查看复制状态（关键字段）
SHOW SLAVE STATUS\G
-- Slave_IO_Running: Yes      -- IO 线程正常
-- Slave_SQL_Running: Yes     -- SQL 线程正常
-- Seconds_Behind_Master: 0   -- 延迟秒数（0 最佳）

-- 停止复制
STOP SLAVE;

-- 重置复制
RESET SLAVE ALL;
```

### 复制状态监控关键字段

| 字段 | 说明 | 正常值 |
|------|------|--------|
| `Slave_IO_Running` | IO 线程状态 | Yes |
| `Slave_SQL_Running` | SQL 线程状态 | Yes |
| `Seconds_Behind_Master` | 延迟秒数 | 0（或很小） |
| `Last_IO_Error` | IO 线程错误 | 空 |
| `Last_SQL_Error` | SQL 线程错误 | 空 |
| `Relay_Log_Space` | Relay Log 大小 | 稳定值 |
| `Exec_Master_Log_Pos` | 已执行位置 | 持续增长 |

## 复制模式对比

| 模式 | 说明 | 一致性 | 性能 | 推荐度 |
|------|------|--------|------|--------|
| **异步 (ASYNC)** | Master 不等待 Slave 确认 | 最终一致性 | 最高 | 默认 |
| **半同步 (SEMISYNC)** | 至少一个 Slave 写入 Relay Log | 较高 | 略微降低 | ★★★★★ |
| **全同步 (Group Replication)** | 多数节点确认 | 强一致性 | 最低 | 特定场景 |

### 半同步复制配置

```sql
-- Master 和 Slave 都安装插件
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';

-- Master 启用
SET GLOBAL rpl_semi_sync_master_enabled = 1;
SET GLOBAL rpl_semi_sync_master_timeout = 1000;  -- 1s 超时降级为异步

-- Slave 启用
SET GLOBAL rpl_semi_sync_slave_enabled = 1;
```

## 复制延迟处理

### 常见延迟原因

1. Slave 硬件弱于 Master
2. 大事务（一次 DELETE/UPDATE 百万行）
3. Slave 上存在慢查询锁竞争
4. 单线程 SQL 回放（MySQL 5.6+ 可开启并行复制）

### 并行复制配置 (MySQL 5.7+)

```ini
# my.cnf
slave_parallel_workers = 4
slave_parallel_type = LOGICAL_CLOCK
```

### 应用层处理延迟

```sql
-- 关键读走主库（如支付成功后的订单查询）
-- 普通读走从库（容忍秒级延迟）

-- 判断延迟：如果从库读不到数据，降级读主库
```

## 高可用方案

| 方案 | 原理 | 优点 | 缺点 | 推荐场景 |
|------|------|------|------|---------|
| **主从 + 手动切换** | 手动执行 CHANGE MASTER | 简单 | 切换时间 10min+ | 非关键业务 |
| **MHA** | 自动检测 Master 故障切换 | 成熟稳定 | 需独立管理节点 | 经典方案 |
| **Orchestrator** | 自动故障检测/拓扑管理 | 自动修复 | 复杂度中等 | **推荐方案** |
| **InnoDB Cluster** | Group Replication + MySQL Router | 原生方案 | 需 8.0+ | MySQL 官方方案 |
| **ProxySQL + 读写分离** | 中间层路由 | 灵活路由 | 引入代理层 | 配合复制使用 |

### Orchestrator 工作流程

```
1. 检测 Master 故障（心跳超时）
2. 选择最优 Slave（延迟最小、数据最新）
3. 自动提升为新 Master
4. 重新配置其他 Slave 指向新 Master
5. 通知应用层新 Master 地址（通过 API / Consul）
```

## 读写分离架构

### 应用层实现

```text
// 伪代码
if (sql.startsWith("SELECT")) {
    connection = slavePool.getConnection();
} else {
    connection = masterPool.getConnection();
}
```

### ProxySQL 实现

```sql
-- ProxySQL 配置读写分离组
INSERT INTO mysql_replication_hostgroups 
(writer_hostgroup, reader_hostgroup, comment) 
VALUES (10, 20, '读写分离');

-- SELECT 自动路由到从节点（reader_hostgroup=20）
-- DML 自动路由到主节点（writer_hostgroup=10）
```

## 分库分表 (Sharding)

### 何时需要分库分表

单表 > 5000 万行或单实例 > 2TB 且预期继续增长。

### 方案选择

| 方案 | 类型 | 说明 |
|------|------|------|
| ShardingSphere | 中间件 + 客户端 | Java 生态首选 |
| MyCAT | 数据库中间件 | 传统方案 |
| Vitess | 分布式方案 | YouTube 开源 |
| TiDB | 原生分布式 | 彻底解决但需切换数据库 |

### 分库分表注意事项

1. **分片键选择**：`user_id % shard_count` 或 `order_id % shard_count`
2. **跨分片查询**：全局表、广播表、ER 分片
3. **分布式 ID**：雪花算法、Leaf、Segment
4. **分布式事务**：XA / TCC / Saga / Seata
