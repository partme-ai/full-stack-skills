---
name: dbeaver
description: "Guides DBeaver usage for database connection management, SQL development, data import/export, and ER diagram generation across MySQL, PostgreSQL, Oracle, MongoDB, and other databases. Use when the user needs to configure DBeaver connections, write queries in the SQL editor, export data, or generate ER diagrams."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Configure DBeaver database connections (MySQL, PostgreSQL, Oracle, MongoDB, etc.)
- Write and execute SQL queries in the DBeaver SQL editor
- Export data to CSV, JSON, SQL, or Excel formats
- Import data from files into database tables
- Generate ER diagrams to visualize table relationships
- Manage multiple database connections, bookmarks, and drivers

## How to use this skill

### Workflow

1. **Create a connection** - New Connection > Select database type > Configure host/port/credentials > Test Connection
2. **Write SQL** - Open SQL Editor (F3) > Write query > Execute (Ctrl+Enter)
3. **Manage data** - Right-click table > Export Data or Import Data > Choose format
4. **Generate ER diagram** - Right-click schema > View Diagram > Arrange tables

### Quick-Start Example: Connect and Query

```
1. File > New > Database Connection
2. Select "PostgreSQL" > Enter:
   Host: localhost
   Port: 5432
   Database: mydb
   Username: admin
   Password: ****
3. Click "Test Connection" to verify
4. Open SQL Editor (F3), run:
   SELECT table_name, pg_size_pretty(pg_total_relation_size(table_name::text))
   FROM information_schema.tables
   WHERE table_schema = 'public'
   ORDER BY pg_total_relation_size(table_name::text) DESC;
```

### Data Export

```
Right-click table > Export Data >
  Format: CSV / JSON / SQL INSERT / Excel
  Options: Set delimiter, encoding, header row
  Target: File or clipboard
```

## Best Practices

1. **Driver management** - DBeaver auto-downloads drivers on first connect; update drivers periodically
2. **Secure credentials** - Enable encrypted password storage in connection properties
3. **Transaction mode** - Switch to manual commit in production to prevent accidental changes
4. **Result set navigation** - Use filters, sorting, and pagination for large result sets
5. **Keyboard shortcuts** - Ctrl+Enter to execute, Ctrl+Shift+E to explain plan, F3 for SQL editor

## Keywords

dbeaver, database, SQL, PostgreSQL, MySQL, Oracle, MongoDB, 数据库管理, SQL editor, ER diagram, data export, data import, database tool