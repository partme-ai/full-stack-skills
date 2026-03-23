---
name: dbeaver
description: Provides comprehensive guidance for DBeaver including database connection, SQL development, data management, and ER diagrams. Use when the user asks about DBeaver, needs to connect to databases, manage database connections, or use DBeaver for SQL development.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 配置 DBeaver 数据库连接（MySQL、PostgreSQL、Oracle、MongoDB 等）
- 使用 DBeaver 进行 SQL 开发、查询、数据编辑
- 管理数据库连接、驱动、书签
- 导出/导入数据、生成 ER 图、生成 DDL

## How to use this skill

1. **连接管理**：新建连接 → 选择数据库类型 → 配置连接参数 → 测试连接。
2. **SQL 开发**：使用 SQL 编辑器、查询控制台、结果排序过滤。
3. **数据管理**：导出数据（CSV、JSON、SQL、Excel）、导入数据、批量编辑。
4. **ER 图**：从数据库生成实体关系图，可视化表结构。

## Best Practices

- 驱动管理：首次连接需下载数据库驱动，DBeaver 会自动提示。
- 敏感信息：连接属性中可加密存储密码，启用"记住密码"选项。
- 事务管理：默认自动提交，生产环境建议手动管理事务。
- 结果集：使用过滤器、排序、分页查看大量数据。

## Keywords

dbeaver, database, sql, postgresql, mysql, oracle, mongodb, 数据库管理, sql 开发, er 图