---
name: oracle
description: Provides comprehensive guidance for Oracle database including SQL, PL/SQL, functions, performance tuning (AWR/ASH), backup (RMAN), Data Guard, and RAC. Use when the user asks about Oracle, needs to write Oracle SQL, work with PL/SQL, or manage Oracle databases.
license: Complete terms in LICENSE.txt
---

# Oracle Database — 企业级关系型数据库

Oracle Database 是全球领先的企业级关系型数据库管理系统，以其高可用性、高性能、强安全性及丰富的功能集（RAC、Data Guard、Flashback、高级分区、物化视图等）著称。

## Workflow — 使用决策树

```
遇到 Oracle 相关需求时，按以下顺序决策:

Step 1: 明确场景
├── 编写 SQL 查询/DDL/DML?       → references/09-sql-syntax.md
├── 使用内置函数?                  → 字符串/日期/聚合 → references/01-functions-string.md / 02-functions-date.md
├── 窗口/分析函数?                 → references/03-analytic-functions.md
├── 编写 PL/SQL?                  → references/04-plsql-guide.md
├── 性能调优/执行计划?             → references/05-performance-tuning.md
├── 备份恢复?                     → references/06-backup-recovery.md
├── Data Guard / RAC?             → references/07-dataguard-rac.md
├── 安全/权限/审计?                → references/08-security.md
└── 分区/物化视图/Flashback/AQ?   → references/10-features.md

Step 2: 选择工具
├── 交互式查询 → SQL*Plus / SQL Developer / DBeaver
├── 批量脚本   → SQL*Plus 静默模式
├── PL/SQL 调试 → SQL Developer / TOAD / PL/SQL Developer
└── 自动化运维 → OEM / 脚本

Step 3: 确定环境
├── 版本 → 19c (LTS), 21c/23c (最新)
├── 架构 → 单实例 / RAC / Data Guard / RAC+DG
├── CDB/PDB? → 12c+ 多租户
└── 字符集 → AL32UTF8, ZHS16GBK
```

## When to Use / When NOT to

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| 企业级事务处理（ACID 严格保证） | 简单键值缓存（用 Redis） |
| 复杂 SQL、多表 JOIN、报表分析 | 文档存储（用 MongoDB） |
| PL/SQL 存储过程/包/触发器 | 全文搜索为主（用 Elasticsearch） |
| 海量数据分区（TB/PB 级） | 实时内存计算（用 Redis/Spark） |
| 高可用（RAC/Data Guard） | 轻量嵌入式（用 SQLite） |
| 数据仓库/OLAP 分析 | 时序数据（用 InfluxDB/TimescaleDB） |
| 数据安全与审计（TDE/FGA/VPD） | 简单 CRUD 快速开发（用 PostgreSQL） |
| 大规模 OLTP 交易系统 | 仅需文档型层次化数据（用 PostgreSQL JSONB） |

## Boundary — 能力边界

| ✅ 完全适用 | ⚠️ 有条件适用 | ❌ 不适用 |
|------------|--------------|---------|
| OLTP/OLAP 混合负载 | 海量非结构化数据（用对象存储） | 代替 Redis 做内存缓存 |
| 复杂事务与数据一致性 | 跨数据库异构集成（GoldenGate/DB Link） | 实时流处理（Kafka/Storm） |
| PL/SQL 业务逻辑封装 | 多写场景（RAC 共享存储写） | 简单 CRUD 原型快速迭代 |
| 数据分区与物化视图 | 地理分布式多活（用 GoldenGate） | 多模型数据统一管理 |
| RAC 集群高可用 | 超低延迟（<100μs）查询 | 替代搜索引擎做全文搜索 |
| 细粒度安全审计 | 作为文档数据库存大量 JSON | 替代对象存储 |

超出范围时请考虑：PostgreSQL（开源关系型）、MongoDB（文档）、Redis（缓存）、Elasticsearch（全文搜索）、MySQL（轻量 Web）。

---

## SQL 语法速查

Oracle 的 SQL 差异主要体现在以下方面。完整内容见 `references/09-sql-syntax.md`。

| 特性 | 说明 | 参考文件 |
|------|------|---------|
| 数据类型 | VARCHAR2, NUMBER, CLOB, BLOB, TIMESTAMP, INTERVAL | `references/09-sql-syntax.md` |
| 序列 | `CREATE SEQUENCE` 替代 AUTO_INCREMENT | `references/09-sql-syntax.md` |
| MERGE | UPSERT（存在则更新，不存在则插入） | `references/09-sql-syntax.md` |
| INSERT ALL | 多表条件插入 | `references/09-sql-syntax.md` |
| CONNECT BY | 层次查询（组织树） | `references/09-sql-syntax.md` |
| PIVOT/UNPIVOT | 行转列/列转行 | `references/09-sql-syntax.md` |
| LISTAGG | 列转字符串聚合 | `references/09-sql-syntax.md` |
| MODEL 子句 | 电子表格式跨行计算 | `references/09-sql-syntax.md` |
| MATCH_RECOGNIZE | 模式匹配（12c+） | `references/09-sql-syntax.md` |
| FLASHBACK QUERY | 闪回查询历史数据 | `references/09-sql-syntax.md` |
| WITH (CTE) / 递归 CTE | 公用表表达式 | `references/09-sql-syntax.md` |
| 伪列 | ROWNUM, ROWID, LEVEL, ORA_ROWSCN | `references/09-sql-syntax.md` |
| 集合操作 | UNION, INTERSECT, MINUS（Oracle 差集） | `references/09-sql-syntax.md` |

## 函数速查

| 类别 | 关键函数 | 参考文件 |
|------|---------|---------|
| 字符串 | SUBSTR, INSTR, REPLACE, REGEXP_LIKE/SUBSTR/REPLACE, TRANSLATE, LISTAGG | `references/01-functions-string.md` |
| 数字 | ROUND, TRUNC, MOD, CEIL, FLOOR, POWER, GREATEST/LEAST | `references/01-functions-string.md` |
| 日期 | SYSDATE, EXTRACT, TO_DATE/TO_CHAR, ADD_MONTHS, MONTHS_BETWEEN, LAST_DAY, NEXT_DAY, TRUNC 日期版 | `references/02-functions-date.md` |
| 转换 | TO_CHAR/TO_NUMBER/TO_DATE, CAST, CONVERT, SCN_TO_TIMESTAMP | `references/02-functions-date.md` |
| NULL 处理 | NVL, NVL2, COALESCE, NULLIF, LNNVL | `references/01-functions-string.md` |
| 聚合 | COUNT, SUM, AVG, MEDIAN, STATS_MODE, ROLLUP/CUBE, GROUPING | `references/03-analytic-functions.md` |
| 分析/窗口 | ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG/LEAD, FIRST_VALUE/LAST_VALUE, RATIO_TO_REPORT | `references/03-analytic-functions.md` |

---

## 高级特性索引

| 特性 | 说明 | 参考文件 |
|------|------|---------|
| PL/SQL 块结构 | DECLARE/BEGIN/EXCEPTION/END | `references/04-plsql-guide.md` |
| 游标 (Cursor) | 显式/隐式/REF CURSOR/SYS_REFCURSOR | `references/04-plsql-guide.md` |
| 存储过程/函数 | CREATE OR REPLACE PROCEDURE/FUNCTION | `references/04-plsql-guide.md` |
| 包 (Package) | 规范+体，封装/重载/全局变量 | `references/04-plsql-guide.md` |
| 触发器 (Trigger) | DML/INSTEAD OF/DDL/系统事件 | `references/04-plsql-guide.md` |
| 集合类型 | 关联数组/嵌套表/VARRAY | `references/04-plsql-guide.md` |
| 动态 SQL | EXECUTE IMMEDIATE / DBMS_SQL / FORALL / BULK COLLECT | `references/04-plsql-guide.md` |
| 异常处理 | 预定义/自定义/RAISE_APPLICATION_ERROR | `references/04-plsql-guide.md` |
| EXPLAIN PLAN / DBMS_XPLAN | 执行计划查看与分析 | `references/05-performance-tuning.md` |
| AWR/ASH/ADDM | 性能历史/活跃会话/自动诊断 | `references/05-performance-tuning.md` |
| SQL Tuning Advisor | 自动 SQL 优化建议 | `references/05-performance-tuning.md` |
| DBMS_STATS | 统计信息收集与管理 | `references/05-performance-tuning.md` |
| SPM (SQL Plan Management) | 执行计划基线管理 | `references/05-performance-tuning.md` |
| RMAN | 全库/增量备份与恢复 | `references/06-backup-recovery.md` |
| EXPDP/IMPDP | 逻辑备份导入导出 | `references/06-backup-recovery.md` |
| 归档日志模式 | ARCHIVELOG / NOARCHIVELOG | `references/06-backup-recovery.md` |
| Data Guard | 物理备库/逻辑备库/Switchover/Failover | `references/07-dataguard-rac.md` |
| RAC | 集群/序列配置/全局等待 | `references/07-dataguard-rac.md` |
| 用户/角色/权限 | 系统权限/对象权限/Profile | `references/08-security.md` |
| FGA (细粒度审计) | 基于条件的 SQL 审计 | `references/08-security.md` |
| VPD (虚拟私有数据库) | 行级安全策略 | `references/08-security.md` |
| 数据脱敏 (Data Redaction) | 动态数据掩码 | `references/08-security.md` |
| TDE (透明数据加密) | 列级/表空间级加密 | `references/08-security.md` |
| 表空间与数据文件 | CREATE/ALTER TABLESPACE | `references/10-features.md` |
| 分区表 | RANGE/LIST/HASH/复合/间隔分区 | `references/10-features.md` |
| 索引 | B-Tree/位图/函数/域索引 | `references/10-features.md` |
| 物化视图 | 查询重写/快速刷新/ON COMMIT | `references/10-features.md` |
| Flashback | 闪回查询/表/删除/数据库 | `references/10-features.md` |
| AQ (高级队列) | 消息队列 | `references/10-features.md` |

---

## Gotchas — 常见陷阱

| # | 问题 | 风险 | 解决方案 |
|---|------|------|---------|
| 1 | ROWNUM ORDER BY 顺序错误 | 不是 Top-N | 子查询排序或 `FETCH FIRST`（12c+） |
| 2 | 隐式类型转换导致索引失效 | 全表扫描 | `WHERE hire_date = TO_DATE('2024-01-15','YYYY-MM-DD')` |
| 3 | NOT IN 子查询含 NULL 返回空 | 数据丢失 | 用 `NOT EXISTS` 替代 |
| 4 | SELECT INTO 无数据抛出 NO_DATA_FOUND | 过程终止 | 提前检查或用 EXCEPTION 捕获 |
| 5 | 绑定变量窥视 | 执行计划偏差 | 用 ACS / SQL Profile |
| 6 | 统计信息过旧 | 优化器选错计划 | 定期 `DBMS_STATS` 收集 |
| 7 | OLTP 用位图索引 | 行锁阻塞 | OLTP 用 B-Tree 索引 |
| 8 | UPDATE 大量行不用 FORALL | 性能极差 | 用 `FORALL` 批量 DML |
| 9 | 忽略分区裁剪 | 全分区扫描 | WHERE 条件含分区键 |
| 10 | 触发器递归/变异表 (ORA-04091) | 触发器失败 | 复合触发器/自治事务/语句级 |
| 11 | SELECT * 在视图/过程中 | 结构变更后行为异常 | 显式列出列名 |
| 12 | 大量 DISTINCT 掩盖 JOIN 不当 | 性能开销大 | 检查 JOIN 条件 |
| 13 | 物化视图 ON COMMIT 刷新影响 DML 性能 | 写操作拖慢 | 建日志 + ON DEMAND 定时刷新 |
| 14 | WHERE 中对列应用函数 | 索引失效 | 改写为范围查询 |
| 15 | DBMS_OUTPUT 打印大量数据 | 缓冲区溢出 | 仅调试用，生产用日志表 |

---

## FAQ

**Q1: VARCHAR2 和 NVARCHAR2 区别？**
VARCHAR2 使用数据库字符集（AL32UTF8/ZHS16GBK），NVARCHAR2 使用国家字符集（AL16UTF16）。推荐一般场景用 VARCHAR2，多语言用 NVARCHAR2。

**Q2: ROWNUM 和 ROW_NUMBER() 区别？**
ROWNUM 是伪列（先分配后排序），ROW_NUMBER() 是分析函数（排序后分配序号）。

**Q3: Oracle vs PostgreSQL 主要差异？**
| 特性 | Oracle | PostgreSQL |
|------|--------|-----------|
| 自增 | SEQUENCE / IDENTITY (12c+) | SERIAL / GENERATED AS IDENTITY |
| 字符串 | VARCHAR2 | VARCHAR / TEXT |
| 空串 | '' = NULL | '' ≠ NULL |
| 递归 | CONNECT BY / WITH RECURSIVE | WITH RECURSIVE |
| 分页 | ROWNUM / FETCH FIRST | LIMIT/OFFSET |
| UPSERT | MERGE | INSERT...ON CONFLICT |
| 表空间 | 有 | 无 |

**Q4: UNDO 和 REDO 区别？**
REDO 记录变更（重做/恢复），UNDO 记录变更前数据（回滚/一致性读/闪回）。

**Q5: 何时用物化视图？**
查询大聚合可接受延迟、基表变更不频繁、需要跨数据库缓存、需要查询重写。

**Q6: 分区表常见误区？**
分区不保证查询加速（需分区键）、不能解决所有大表问题、分区不是越多越好、OLTP 也适合分区。

**Q7: 什么是读一致性？**
Oracle 通过 UNDO 实现 SELECT 不加锁也不被写阻塞，查询使用查询开始时的 SCN 读取一致性版本。

**Q8: 死锁如何处理？**
Oracle 3 秒内自动检测，回滚牺牲品语句并抛 ORA-00060。最佳实践：统一访问顺序、事务简短。

**Q9: CDB 和 PDB 是什么？**
12c+ 多租户：CDB = 容器数据库，PDB = 可插拔数据库。一个 CDB 最多 4096 个 PDB。

**Q10: KILL SESSION 后连接未断开？**
标记为 KILLED，下次执行 SQL 时断开。`KILL SESSION 'sid,serial#' IMMEDIATE` 可立即断开。

**Q11: REDO 日志切换太频繁？**
增加 REDO 日志大小（建议 15-30 分钟切换一次）、增加日志组数（至少 3-4 组）。

**Q12: ORA-01555 "Snapshot Too Old"？**
UNDO 数据被覆盖。增大 UNDO 表空间、减少 UNDO_RETENTION、优化长查询。

**Q13: Oracle 中如何实现分页？**
`SELECT * FROM (SELECT t.*, ROWNUM AS rn FROM (SELECT ... ORDER BY col) t) WHERE rn BETWEEN 11 AND 20` 或 12c+ `OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY`。

**Q14: 什么是 FORCE LOGGING？**
强制所有 DML 写 REDO（即使是 NOLOGGING 操作），Data Guard 环境要求开启。

**Q15: 如何查看当前数据库版本？**
`SELECT * FROM v$version;` 或 `SELECT banner FROM v$version WHERE banner LIKE 'Oracle%';`

---

## Keywords

oracle, Oracle Database, PL/SQL, SQL*Plus, RAC, Data Guard, ADG, RMAN, expdp, impdp, flashback, AWR, ASH, ADDM, DBMS_XPLAN, VARCHAR2, NUMBER, CLOB, SEQUENCE, SYNONYM, CONNECT BY, PIVOT, LISTAGG, MERGE, INSERT ALL, MODEL, MATCH_RECOGNIZE, 分析函数, 窗口函数, ROW_NUMBER, RANK, LAG, LEAD, 存储过程, 包, 触发器, 游标, REF CURSOR, 动态SQL, FORALL, BULK COLLECT, 分区表, 物化视图, 位图索引, 表空间, TDE, FGA, VPD, DBMS_STATS, SPM, CDB, PDB, 多租户, UNDO, REDO, 读一致性, ORA-01555

## References

- `references/01-functions-string.md` — 字符串/数字/NULL 处理函数
- `references/02-functions-date.md` — 日期/转换函数
- `references/03-analytic-functions.md` — 分析函数（窗口函数）+ 聚合
- `references/04-plsql-guide.md` — PL/SQL 详解
- `references/05-performance-tuning.md` — 性能调优
- `references/06-backup-recovery.md` — 备份恢复
- `references/07-dataguard-rac.md` — Data Guard / RAC
- `references/08-security.md` — 安全与权限
- `references/09-sql-syntax.md` — SQL 语法详解
- `references/10-features.md` — 特有特性（分区/物化视图/Flashback/AQ）
- `examples/01-plsql-procedure.md` — PL/SQL 存储过程示例
- `examples/02-awr-analysis.md` — AWR 性能分析示例
- `examples/03-rman-backup.md` — RMAN 备份示例
- `examples/04-dataguard-setup.md` — Data Guard 搭建示例
- [Oracle 19c 官方文档](https://docs.oracle.com/en/database/oracle/oracle-database/19/)
- [Oracle Live SQL (在线练习)](https://livesql.oracle.com/)
