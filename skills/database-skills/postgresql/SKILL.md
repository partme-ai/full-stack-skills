---
name: postgresql
description: Provides comprehensive guidance for PostgreSQL database including SQL syntax, advanced features, JSON support, full-text search, and performance tuning. Use when the user asks about PostgreSQL, needs to work with PostgreSQL features, write complex queries, or optimize PostgreSQL databases.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 设计表、索引、约束、触发器与 PL/pgSQL；编写或优化 SQL
- 使用 psql、pg_dump、用户与角色权限
- 排查锁、VACUUM、复制与扩展（如 pgvector）

## How to use this skill

1. **SQL**：DDL、DML、窗口函数、CTE；EXPLAIN ANALYZE 分析；扩展如 JSONB、全文检索。
2. **CLI**：`psql` 连接与元命令；`pg_dump/pg_restore` 备份；配置 pg_hba.conf 与 listen_addresses。
3. **环境**：版本与扩展兼容；生产用流复制与 PITR；监控连接、锁与表膨胀。

## Best Practices

- 合理使用索引与 VACUUM；大表分区与归档。
- 权限用 ROLE 与 GRANT 细化；敏感数据可加密列。
- 备份与 WAL 归档验证；升级前测试与回滚方案。

## Keywords

postgresql, postgres, psql, 关系型数据库, 索引, 复制
