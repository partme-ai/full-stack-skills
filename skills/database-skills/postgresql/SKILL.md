---
name: postgresql
description: Provides comprehensive guidance for PostgreSQL including SQL syntax, advanced features (JSONB/CTE/Full-text), functions, indexing, performance tuning, replication, and backup. Use when the user asks about PostgreSQL, needs to work with PostgreSQL features, write complex queries, or optimize PostgreSQL databases.
license: Complete terms in LICENSE.txt
---

# PostgreSQL — 高级关系型数据库系统

## Workflow — 使用流程

```text
遇到 PostgreSQL 需求时，按以下顺序决策:

1. 明确需求类型
   ├── DDL (建表/改表)        → 见 SQL 语法速查
   ├── DML (查询/插入/更新)    → 见 SQL 语法速查
   ├── 函数/数据处理            → 见 函数速查
   ├── 查询性能优化             → 见 references/06-index-types.md + examples/03-performance-tuning.md
   └── 高可用/备份/复制         → 见 references/08-replication-backup.md + examples/04-streaming-replication.md

2. 确定模型: 关系型 → 标准表+B-Tree | JSON文档 → JSONB+GIN | 全文搜索 → tsvector+GIN | 地理 → PostGIS+GiST

3. 索引策略: 等值→B-Tree | 范围→B-Tree | 全文→GIN | JSON→GIN | 向量→IVFFlat/HNSW | 大表时序→BRIN

4. 数据量评估: <100GB→单实例 | 100GB-1TB→分区 | 1TB-10TB→分区+只读副本 | >10TB→Citus/逻辑复制

5. 运维策略: autovacuum + pg_stat_statements + WAL归档 + PgBouncer
```

## When to Use (and When NOT to)

| ✅ Use When | ❌ Skip When |
|------------|-------------|
| 需要完整 ACID 事务和复杂 SQL | 纯键值缓存 (用 Redis/Memcached) |
| JSON 文档 + SQL 查询混合 | 纯文档无关联查询 (用 MongoDB) |
| 地理空间数据分析 (PostGIS) | 大规模全文搜索 (用 Elasticsearch) |
| 强数据完整性约束 | 海量无模式日志 (用 Elasticsearch/S3) |
| OLTP + 复杂 OLAP 混合负载 | 超大规模 OLAP (用 ClickHouse/Snowflake) |
| 需要流复制/逻辑复制/PITR | 自动水平分片 (用 CockroachDB/YugabyteDB) |

**核心原则：PostgreSQL 是全能型关系型数据库，但不是所有场景的最佳选择。**

## Boundary — 能力边界

| ✅ 完全适用 | ⚠️ 有条件适用 | ❌ 不适用 → 替代 |
|------------|--------------|----------------|
| 标准 OLTP 业务系统 | 超大规模 OLAP >20TB → ClickHouse/cstore_fdw | 纯内存缓存 <1ms → Redis |
| JSONB + 关系查询混合 | 高并发简单 KV >50万 QPS → Redis | 海量时序写入 >100万点/秒 → InfluxDB |
| 全文搜索 (数亿文档) | 实时搜索 >10亿文档 → Elasticsearch | 复杂图遍历 → Neo4j |
| 流复制 HA (故障恢复 <30s) | 跨地域多活 → CockroachDB | 自动分片无感扩缩容 |

## SQL 语法速查

深度 SQL 内容见 `references/` 各文件，此处为索引。

- **DDL**: `CREATE TABLE` (含分区、继承), `ALTER TABLE`, 数据类型 (JSONB/TSVECTOR/CITEXT/数组等), 约束 (CHECK/EXCLUDE/UNIQUE/FOREIGN KEY)
- **DML**: `INSERT ... ON CONFLICT` (UPSERT), `UPDATE ... FROM`, `DELETE ... USING`, `TRUNCATE`, `RETURNING` 子句
- **CTE**: 公用表表达式 (`WITH`), 递归 CTE (`WITH RECURSIVE`) — 见 `examples/02-cte-recursive.md`
- **连接**: `INNER/LEFT/RIGHT/FULL/CROSS JOIN`, `LATERAL` 子查询
- **事务**: `READ COMMITTED` (默认), `REPEATABLE READ`, `SERIALIZABLE`, `SAVEPOINT`, `FOR UPDATE/SHARE/NOWAIT/SKIP LOCKED`, 咨询锁

## 函数速查

深度内容见 `references/`:

| 类别 | 关键函数 | 参考文件 |
|------|---------|---------|
| 字符串/正则 | `FORMAT`, `SPLIT_PART`, `REGEXP_MATCH/REPLACE`, `STRING_AGG`, `CONCAT_WS`, `TRANSLATE`, `SUBSTRING` | `references/01-functions-string.md` |
| 日期/时间 | `AGE`, `DATE_TRUNC`, `EXTRACT`, `TO_CHAR`, `MAKE_DATE`, `JUSTIFY_*`, 时区转换 | `references/02-functions-datetime.md` |
| 聚合/窗口 | `ARRAY_AGG`, `JSONB_AGG`, `STRING_AGG`, `PERCENTILE_CONT/DISC`, `MODE`, `GROUPING SETS/CUBE/ROLLUP`, `ROW_NUMBER`, `RANK`, `LAG/LEAD`, `NTILE`, 窗口帧 | `references/03-functions-aggregate-window.md` |
| JSONB | `->`/`->>`/`#>`, `@>`/`?`/`?|`/`?&`, `JSONB_SET`, `JSONB_BUILD_OBJECT`, `JSONB_EACH`, `JSONB_TYPEOF`, GIN 索引 | `references/04-functions-jsonb.md` |

## 高级特性索引

| 特性 | 说明 | 参考 |
|------|------|------|
| 6种索引 | B-Tree, Hash, GiST, GIN, BRIN, SP-GiST, Bloom + 部分索引/覆盖索引/CONCURRENTLY | `references/06-index-types.md` |
| 视图与物化视图 | 普通视图 (虚拟表) vs 物化视图 (物理快照), WITH CHECK OPTION, CONCURRENTLY 刷新 | `references/06-index-types.md` |
| PL/pgSQL | 函数 (FUNCTION) vs 过程 (PROCEDURE), 控制结构, 异常处理, 函数重载 | `references/01-functions-string.md` |
| 触发器 | BEFORE/AFTER/INSTEAD OF, 行级/语句级, 事件触发器, 约束触发器 | `references/01-functions-string.md` |
| 全文搜索 | tsvector/tsquery, @@ 操作符, ts_rank, ts_headline, 短语搜索, 中文搜索 (zhparser) | `references/05-fulltext-search.md` |
| 分区表 | RANGE/LIST/HASH 分区, 子分区, 分区裁剪, ATTACH/DETACH | `references/07-partition-fdw.md` |
| FDW 外部表 | postgres_fdw, file_fdw, IMPORT FOREIGN SCHEMA | `references/07-partition-fdw.md` |
| 扩展 | PostGIS, pgvector, pg_stat_statements, uuid-ossp, pgcrypto, citext, pg_trgm, unaccent | `references/08-replication-backup.md` |
| 权限管理 | ROLE, SCHEMA, GRANT, 默认权限, RLS 行级安全 | `references/08-replication-backup.md` |
| 流复制与逻辑复制 | 同步/异步, PUBLICATION/SUBSCRIPTION, Patroni/repmgr | `references/08-replication-backup.md` |
| 备份与恢复 | pg_dump/pg_restore, pg_basebackup, WAL 归档 + PITR | `references/08-replication-backup.md` |
| 性能优化 | EXPLAIN ANALYZE, VACUUM/autovacuum, pg_stat_statements, 配置调优 | `examples/03-performance-tuning.md` |

## Gotchas — 常见陷阱与反模式

| # | 陷阱 | 风险 | 解决方案 |
|---|------|------|---------|
| 1 | JSONB 未建 GIN 索引 | 全表扫描, 性能差 | `CREATE INDEX ... USING GIN (config)` |
| 2 | 大量直连数据库 | 每个连接耗 5-10MB, 撑爆内存 | 使用 PgBouncer 连接池 |
| 3 | 索引膨胀未维护 | 索引体积远超表大小 | 定期 `REINDEX` 或 pg_repack |
| 4 | N+1 查询 + `SELECT *` | 传输冗余数据, 多次查询 | 只选需要列, 用 JOIN/LATERAL |
| 5 | 生产高峰期 `VACUUM FULL` | 锁表, 业务中断 | 用 pg_repack (不锁表) |
| 6 | autovacuum 触发不及时 | 死元组堆积 → 表膨胀 → 性能崩溃 | 监控 n_dead_tup, 调参 |
| 7 | `SERIAL` 而非 `BIGSERIAL` | 超 21 亿行后 ID 溢出 | 新表用 `BIGSERIAL` 或 UUID |
| 8 | 多租户未设 RLS | 数据泄露 | 启用 RLS + 外键约束 |
| 9 | 忽略事务 ID 回卷 | 数据库强制只读 | 监控 `age(relfrozenxid)` |
| 10 | UUID 做主键 (v4 随机) | B-Tree 页分裂, 写入慢 2-3x | 用 UUID v7 或 BIGSERIAL |
| 11 | 大表 `COUNT(*)` | 千万行以上全表扫描极慢 | 用 `pg_class.reltuples` 近似值 |
| 12 | 外键无索引 | 删除/更新父表时子表全表扫描 | 外键列上建索引 |
| 13 | SERIALIZABLE 无重试逻辑 | 事务冲突失败 | 应用层实现重试 |

## FAQ

**Q1: PostgreSQL vs MySQL 主要区别？**
PostgreSQL: 完全 ACID, JSONB 可索引, 6 种索引类型, 递归 CTE, 流复制+逻辑复制, 丰富 EXTENSION。MySQL: Web 应用为主, 简单查询, InnoDB 事务, 间隙锁并发控制。

**Q2: JSONB vs JSON？**
始终选 JSONB。二进制格式, 支持 GIN 索引, 查询更快。JSON 仅在你需要保留空格和键顺序时使用。

**Q3: UUID 为什么不适合做主键？**
UUID v4 随机值导致 B-Tree 页频繁分裂, 比 BIGSERIAL 慢 2-3 倍。方案: UUID v7 (时间排序), BIGSERIAL, 或 ULID/Snowflake。

**Q4: 如何在线迁移 PostgreSQL？**
逻辑复制 (PG 10+, 推荐) > pglogical 扩展 > pg_dump+pg_restore (需停机)。逻辑复制支持跨大版本、选择性复制。

**Q5: work_mem 怎么设？**
每个排序操作分配, 最大内存 = work_mem × (连接数 × 并发排序数)。64GB 机器建议 64-128MB。监控 temp_files 指标, 有磁盘排序则调大。

**Q6: pg_repack vs VACUUM FULL？**
VACUUM FULL 锁表 (ACCESS EXCLUSIVE)。pg_repack 不锁写, 适合在线环境, 优先选择。

**Q7: 死锁怎么处理？**
PG 自动检测并回滚一个事务。预防: 保持锁顺序一致、缩短事务、用 NOWAIT/SKIP LOCKED, 监控 pg_stat_database.deadlocks。

**Q8: 如何选择分区键？**
条件: 查询频繁出现 (分区裁剪)、数据均匀分布、稳定不变。常见: 时间 (RANGE)、地区 (LIST)、ID 哈希 (HASH)。分区数建议 10-200。

**Q9: 连接数设多少？**
每个连接 5-10MB, 一般 200-500 够用。超过 500 必须用 PgBouncer。(max_connections × work_mem × 0.5) + shared_buffers + 系统开销 < 内存 80%。

**Q10: 何时用 SERIALIZABLE？**
金融转账、库存扣减、强一致性报表。注意: 失败率随冲突上升, 应用层需重试逻辑。

**Q11: 查询没走索引的原因？**
统计信息过旧→ANALYZE | 类型不匹配→隐式转换 | 选择性低→规划器认为全表更优 | 函数包裹索引列→避免 WHERE DATE(col) = 写法。

**Q12: 怎么判断要不要分区？**
表 > 100GB | 存在明显按时间/地区查询模式 | 旧数据定期归档 | VACUUM 跟不上更新。不满足则分区复杂度 > 收益。

**Q13: 如何大版本升级？**
pg_upgrade 最推荐: `pg_upgrade -b old_bin -B new_bin -d old_data -D new_data`, --link 模式最快。升级后执行 ANALYZE。

**Q14: 逻辑复制 vs 流复制？**
流复制: 物理块级, 全库, 大版本必须一致, 用于 HA。逻辑复制: SQL 变更, 选表/行, 跨大版本, 用于数据同步/迁移。

**Q15: VACUUM 后表大小没变小？**
VACUUM (不带 FULL) 只标记空间可重用, 不还给 OS。真正缩小需 VACUUM FULL 或 pg_repack。

## Keywords

postgresql, postgres, psql, SQL, DDL, DML, ACID, MVCC, 事务, 索引, B-Tree, GIN, GiST, BRIN, JSONB, hstore, 数组, 全文搜索, tsvector, tsquery, 窗口函数, CTE, 递归CTE, LATERAL, PL/pgSQL, 存储过程, 触发器, 物化视图, 分区表, PostGIS, pgvector, pg_stat_statements, pgcrypto, citext, pg_trgm, FDW, postgres_fdw, EXPLAIN, VACUUM, autovacuum, pg_dump, pg_restore, pg_basebackup, WAL归档, PITR, 流复制, 逻辑复制, PUBLICATION, SUBSCRIPTION, Patroni, repmgr, PgBouncer, RLS, 行级安全, 性能优化, 备份恢复, 高可用, 死锁, 连接池

## References

- [PostgreSQL 官方文档](https://www.postgresql.org/docs/current/)
- [PostgreSQL 中文文档](http://www.postgres.cn/docs/16/)
- [PostgreSQL 性能调优 — pgtune](https://pgtune.leopard.in.ua)
- [Patroni 文档](https://patroni.readthedocs.io/)
- [PgBouncer 官方文档](https://www.pgbouncer.org/)
- [pgvector 文档](https://github.com/pgvector/pgvector)
- [PostGIS 文档](https://postgis.net/documentation/)

### 内部参考

- `references/01-functions-string.md` — 字符串/正则函数详解
- `references/02-functions-datetime.md` — 日期/时间函数详解
- `references/03-functions-aggregate-window.md` — 聚合/窗口函数详解
- `references/04-functions-jsonb.md` — JSONB 函数与操作详解
- `references/05-fulltext-search.md` — 全文搜索详解
- `references/06-index-types.md` — 索引类型与视图详解
- `references/07-partition-fdw.md` — 分区表与 FDW 详解
- `references/08-replication-backup.md` — 复制/备份/权限详解
- `examples/01-jsonb-query.md` — JSONB 查询示例
- `examples/02-cte-recursive.md` — 递归 CTE 示例
- `examples/03-performance-tuning.md` — 性能调优示例
- `examples/04-streaming-replication.md` — 流复制搭建示例
