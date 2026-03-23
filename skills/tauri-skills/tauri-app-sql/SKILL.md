---
name: tauri-app-sql
description: Guidance for Tauri v2 SQL plugin setup, migrations, and safe query access.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Using SQLite, MySQL, or PostgreSQL in Tauri / 在 Tauri 中使用 SQLite、MySQL 或 PostgreSQL
- SQL migrations or connection configuration / SQL 迁移或连接配置
- Secure frontend query access / 前端安全查询访问

**Trigger phrases include:**
- "sql", "sqlite", "postgres", "mysql", "migration"
- "数据库", "迁移", "连接配置", "SQL"

## How to use this skill

1. Select the database engine and connection string
2. Configure migrations in tauri.conf.json
3. Enable SQL plugin capabilities with scoped access
4. Validate queries and error handling in the app flow

## Outputs

- Database integration plan / 数据库集成方案
- Minimal-permission capability checklist / 最小权限能力清单

## Scope

- Boundary: SQL plugin configuration and usage only
- Key points: Migrations setup and capability scoping

## References

- https://v2.tauri.app/plugin/sql/
- https://v2.tauri.app/zh-cn/plugin/sql/

## Keywords

tauri sql, sqlite, postgres, mysql, migrations, database
