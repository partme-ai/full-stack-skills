---
name: mysql
description: Provides comprehensive guidance for MySQL including SQL syntax, functions, indexing, optimization, replication, backup, and high availability. Use when the user asks about MySQL, needs to write MySQL queries, design database schemas, optimize performance, or manage MySQL databases.
license: Complete terms in LICENSE.txt
---

# MySQL — 关系型数据库管理系统

MySQL 是最流行的开源关系型数据库管理系统（RDBMS），以 InnoDB 存储引擎为核心，支持 ACID 事务、外键约束和多种复制架构。

## Workflow — 使用流程

```
遇到 MySQL 需求时，按以下顺序决策:

1. 明确场景
├── 建库建表 / 设计 schema?    → DDL 与数据类型参考 (references/05)
├── 复杂查询 / 报表分析?        → DML + 聚合/窗口函数 (references/03)
├── 性能慢 / 优化 SQL?          → 索引与执行计划 (references/06)
├── 备份 / 恢复?                → 备份与恢复 (references/08)
├── 主从 / 高可用?              → 复制与高可用 (references/07)
├── 存储过程 / 分区 / 事务?     → 高级特性 (references/09)
├── 字符串/日期/JSON 函数?       → 函数参考 (references/01-04)
└── 实战配置 / 搭建?             → 示例 (examples/)

2. 引擎选择: InnoDB (99% 场景) → MyISAM (只读归档) → MEMORY (临时表)
3. 索引设计: 主键先 → 查询/排序/JOIN 列建索引 → 检查最左前缀
4. 生产措施: 开启慢查询 → 配置主从复制 → 制定备份策略
```

## When to Use / When NOT to

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| 需要 ACID 事务保障的业务系统（订单、支付、账户） | 高频 KV 存取（<1ms 延迟，用 Redis） |
| 数据结构固定、关系明确的 OLTP 场景 | 文档型非结构化数据（用 MongoDB） |
| 需要复杂 JOIN/子查询的报表分析 | 海量日志/时序数据（用 ClickHouse） |
| 中小规模到中大规模 OLTP（百万~亿级） | 超大规模分布式事务（用 TiDB） |
| 主从复制读写分离架构 | 图关系数据（用 Neo4j） |
| 需要丰富内置函数和存储过程 | 全文搜索引擎为主（用 Elasticsearch） |

## Boundary — 能力边界

| ✅ 完全适用 | ⚠️ 有条件适用 | ❌ 不适用（替代方案） |
|-----------|--------------|------------------|
| OLTP 业务系统 | 单表过亿行（需分库分表） | 纯内存缓存 → Redis |
| ACID 事务一致性 | 跨分片分布式事务（XA/Seata） | 文档存储 → MongoDB |
| 复杂 SQL（JOIN/子查询/聚合） | 实时流计算（MySQL + Flink） | 全文搜索 → Elasticsearch |
| 主从复制读写分离 | 强一致多主写入（Galera/PXC） | 时序大数据 → ClickHouse |
| mysqldump/XtraBackup 备份 | JSON 深度查询（不如 MongoDB） | 分布式强一致 → TiDB |
| 分区表（RANGE/LIST/HASH） | 高并发写入 > 1万 TPS | 图数据库 → Neo4j |

## SQL 语法速查

| 类别 | 核心语法 | 详情参考 |
|------|---------|---------|
| DDL | `CREATE/ALTER/DROP TABLE`，数据类型、约束 | references/05-sql-ddl-types.md |
| DML | `INSERT/UPDATE/DELETE`，`ON DUPLICATE KEY UPDATE` | 同上 |
| DQL | `SELECT/JOIN/GROUP BY/HAVING/UNION`，CTE，子查询 | references/03, 09 |
| 事务 | `START TRANSACTION/COMMIT/ROLLBACK/SAVEPOINT` | references/09-advanced-features.md |
| 分页 | `LIMIT/OFFSET`（小表），`WHERE id > :last` 游标（大表） | references/06-index-optimization.md |

## 函数速查

| 类别 | 最常用函数 | 详情参考 |
|------|-----------|---------|
| 字符串 | `CONCAT, SUBSTRING, REPLACE, LPAD, GROUP_CONCAT, LENGTH` | references/01-functions-string.md |
| 日期时间 | `NOW, DATE_FORMAT, DATEDIFF, DATE_ADD, TIMESTAMPDIFF` | references/02-functions-date.md |
| 聚合 | `COUNT, SUM, AVG, MAX, MIN, GROUP_CONCAT` | references/03-functions-aggregate-window.md |
| 窗口 (8.0+) | `ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, NTILE` | references/03-functions-aggregate-window.md |
| JSON (5.7+) | `JSON_EXTRACT, JSON_SET, JSON_CONTAINS, JSON_TABLE` | references/04-functions-json.md |
| 条件 | `IF, IFNULL, COALESCE, CASE WHEN` | references/05-sql-ddl-types.md |

## 高级特性索引

| 特性 | 简介 | 参考 |
|------|------|------|
| 视图 (View) | 存储的查询定义，简化复杂查询和权限控制 | references/09-advanced-features.md |
| CTE (8.0+) | 命名临时结果集，支持递归树形查询 | 同上 |
| 存储过程 | 封装多条 SQL 带事务控制的业务逻辑 | 同上 |
| 触发器 | 自动响应 INSERT/UPDATE/DELETE 的事件处理 | 同上 |
| 事务与锁 | ACID、MVCC、四种隔离级别、行锁/表锁/死锁 | 同上 |
| 分区表 | RANGE/LIST/HASH/KEY 分区，数据归档加速 | 同上 |
| 全文索引 (5.6+) | FULLTEXT + MATCH AGAINST 代替 LIKE 搜索 | references/06-index-optimization.md |
| 函数索引 (8.0.13+) | 对表达式/函数结果建索引 | 同上 |
| 降序索引 (8.0+) | 混合排序方向的索引优化 | 同上 |
| 主从复制 | Binlog + Relay Log 实现数据同步 | references/07-replication-ha.md |
| 半同步复制 | 至少一个 Slave 确认，平衡性能与一致性 | 同上 |
| InnoDB Cluster | Group Replication + MySQL Router 原生 HA | 同上 |
| XtraBackup | 物理热备份，支持增量 | references/08-backup-restore.md |
| PITR | 利用 Binlog 实现时间点恢复 | 同上 |

## 引擎对比

| 特性 | InnoDB | MyISAM | MEMORY |
|------|--------|--------|--------|
| 事务 | ✅ ACID | ❌ | ❌ |
| 外键 | ✅ | ❌ | ❌ |
| 行级锁 | ✅ 行锁 | ❌ 表锁 | ❌ 表锁 |
| MVCC | ✅ | ❌ | ❌ |
| 崩溃恢复 | ✅ redo log | ❌ 需 REPAIR TABLE | ❌ 重启即丢 |
| 全文索引 | ✅ 5.6+ | ✅ | ❌ |
| 缓存 | Buffer Pool（数据和索引） | Key Cache（仅索引） | 全内存 |
| 适用场景 | 99% 场景默认首选 | 只读归档（极少用） | 临时表 |
| 表大小限制 | 64TB | 256TB | max_heap_table_size |

## Gotchas — 常见陷阱

| # | 反模式 | 问题 | 正确做法 |
|---|--------|------|---------|
| 1 | 金额用 FLOAT/DOUBLE | 浮点精度误差 | 用 `DECIMAL(10,2)` |
| 2 | WHERE 列用函数/隐式转换 | 索引失效，全表扫描 | 避免函数操作列，类型匹配 |
| 3 | 大批量分页用 OFFSET | OFFSET 越深越慢 | 游标分页 `WHERE id > :last` |
| 4 | 全表无主键 | 无法行级锁，复制延迟 | 每个表必须有 BIGINT 主键 |
| 5 | SELECT * 生产使用 | 浪费带宽，无法覆盖索引 | 显式列出需要列 |
| 6 | 大字段无前缀索引 | 索引过大，B+ 树效率低 | 前缀索引 `col(N)` |
| 7 | 长事务不提交 | undo log 膨胀，MVCC 开销 | 控制事务大小，及时 COMMIT |
| 8 | 索引过多 | 写入性能降低 | 单表索引 ≤ 5-8 个 |
| 9 | COUNT(*) InnoDB 大表 | 需要扫描全表（MyISAM 才缓存） | 用近似值或计数表 |
| 10 | LIKE '%keyword%' 搜索 | 无法用索引 | FULLTEXT + MATCH AGAINST |
| 11 | NOT IN (子查询) | 不做半连接优化 | 用 NOT EXISTS |
| 12 | 字符集混用 | 乱码、索引隐性转换 | 统一 utf8mb4 |
| 13 | TEXT/BLOB 过多 | 行溢出，性能差 | 拆分到子表或 OSS |
| 14 | REPLACE 常见误解 | 实际是 DELETE+INSERT | 明确需求后用 ON DUPLICATE KEY UPDATE |
| 15 | 不做备份验证 | 备份损坏但无人知 | 每月定期恢复演练 |

## FAQ

| # | 问题 | 答案 |
|---|------|------|
| 1 | 如何选择 DATETIME 还是 TIMESTAMP？ | TIMESTAMP 自动时区转换（范围 1970-2038），DATETIME 无时区影响（范围 1000-9999） |
| 2 | VARCHAR 最大长度设多少合适？ | 根据业务设合理值（50-200），不要无意义设 255（临时表排序按定义长度分配内存） |
| 3 | 如何快速插入百万级数据？ | `LOAD DATA INFILE` (最快)，或批量 INSERT（每批 500-1000 行），关闭 AUTOCOMMIT |
| 4 | 什么时候需要分库分表？ | 单表 > 5000 万行或单实例 > 2TB 且预期继续增长 |
| 5 | MySQL 8.0 vs 5.7 选哪个？ | 新项目选 8.0（窗口函数、CTE、降序索引、原子 DDL、Hash Join） |
| 6 | 如何监控 MySQL 性能？ | 慢查询日志 + pt-query-digest + Prometheus + Grafana + performance_schema |
| 7 | 主从延迟怎么处理？ | 检查 Slave 硬件、拆分大事务、开启并行复制、关键读走主库 |
| 8 | 误操作删除了数据怎么办？ | 立即停止写入 → 用 Binlog PITR 恢复到误操作前的时间点 |
| 9 | InnoDB 为什么比 MyISAM 好？ | 事务、行锁、崩溃恢复、MVCC、外键。MyISAM 已过时 |
| 10 | 如何查看当前数据库的活跃连接？ | `SHOW PROCESSLIST;` 或 `SELECT * FROM sys.session;` |
| 11 | 如何安全地在大表上添加索引？ | MySQL 8.0 用 `ALGORITHM=INPLACE, LOCK=NONE`；或用 pt-online-schema-change |
| 12 | 唯一索引和普通索引怎么选？ | 需要唯一约束用 UNIQUE；只需加速查询用普通索引 |
| 13 | 有哪些推荐的管理工具？ | CLI: mysql CLI；GUI: Sequel Ace / DataGrip / Navicat；命令行: Percona Toolkit |
| 14 | utf8mb4 和 utf8 有什么区别？ | utf8 是 utf8mb3（最多 3 字节），不支持 emoji；utf8mb4 支持完整的 Unicode（含 emoji）|
| 15 | 如何排查死锁？ | `SHOW ENGINE INNODB STATUS;` 查看 LATEST DETECTED DEADLOCK 部分 |

## Keywords

MySQL, Database, RDBMS, SQL, DDL, DML, DQL, DCL, InnoDB, MyISAM, MEMORY, ACID, transaction, index, B-Tree, EXPLAIN, query optimization, replication, master-slave, binlog, backup, restore, XtraBackup, mysqldump, PITR, partition, view, stored procedure, trigger, CTE, window function, JSON, utf8mb4, performance_schema, slow query, connection pool, sharding, high availability, HA

## References

### 官方文档
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/)

### 工具
- [Percona XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup)
- [Percona Toolkit](https://www.percona.com/software/database-tools/percona-toolkit)
- [Orchestrator](https://github.com/openark/orchestrator) — MySQL 高可用管理
- [gh-ost](https://github.com/github/gh-ost) — 在线表结构变更

### 本 skill 深度参考
- references/01-functions-string.md — 字符串函数大全
- references/02-functions-date.md — 日期时间函数大全
- references/03-functions-aggregate-window.md — 聚合与窗口函数
- references/04-functions-json.md — JSON 函数
- references/05-sql-ddl-types.md — DDL 与数据类型详解
- references/06-index-optimization.md — 索引与执行计划
- references/07-replication-ha.md — 主从复制与高可用
- references/08-backup-restore.md — 备份与恢复
- references/09-advanced-features.md — 高级特性（视图/CTE/存储过程/触发器/事务/分区）

### 实战示例
- examples/01-connection-pool.md — 连接池配置
- examples/02-slow-query-optimization.md — 慢查询优化
- examples/03-master-slave-setup.md — 主从复制搭建
- examples/04-backup-strategy.md — 备份策略方案
