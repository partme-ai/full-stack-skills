---
name: tauri-app-sql
description: "Access SQLite, MySQL, or PostgreSQL databases from the frontend using the Tauri v2 SQL plugin with migrations. Use when setting up a database connection, running SQL migrations, or executing queries with scoped access from the frontend."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Using SQLite, MySQL, or PostgreSQL in a Tauri app
- SQL migrations or database schema setup
- Running queries from the frontend

**Trigger phrases include:**
- "sql", "sqlite", "database", "postgres", "mysql", "migration", "db plugin"

## How to use this skill

1. **Install the SQL plugin** (with SQLite feature):
   ```bash
   cargo add tauri-plugin-sql --features sqlite
   ```
2. **Register the plugin** with migrations in your Tauri builder:
   ```rust
   use tauri_plugin_sql::{Migration, MigrationKind};
   let migrations = vec![Migration {
       version: 1, description: "create_users", sql: "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
       kind: MigrationKind::Up,
   }];
   tauri::Builder::default()
       .plugin(tauri_plugin_sql::Builder::new().add_migrations("sqlite:app.db", migrations).build())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["sql:allow-load", "sql:allow-execute", "sql:allow-select"] }
   ```
4. **Query from the frontend**:
   ```typescript
   import Database from '@tauri-apps/plugin-sql';
   const db = await Database.load('sqlite:app.db');
   await db.execute('INSERT INTO users (name) VALUES (?)', ['Alice']);
   const users = await db.select<{ id: number; name: string }[]>('SELECT * FROM users');
   ```
5. **Use parameterized queries** to prevent SQL injection
6. **Keep migrations versioned** and run them automatically on app startup

## Outputs

- SQL plugin setup with SQLite/Postgres/MySQL
- Migration system with versioned schemas
- Frontend query patterns with parameterized inputs

## References

- https://v2.tauri.app/plugin/sql/

## Keywords

tauri sql, sqlite, database, postgres, mysql, migrations, queries
