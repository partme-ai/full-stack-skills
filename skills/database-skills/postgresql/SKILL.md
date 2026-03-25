---
name: postgresql
description: "Guides PostgreSQL development including table design, indexing, constraints, PL/pgSQL, JSONB, full-text search, window functions, CTEs, EXPLAIN ANALYZE tuning, backup/restore, replication, and extensions like pgvector. Use when the user needs to write or optimize PostgreSQL queries, design schemas, or manage PostgreSQL databases."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Design tables, indexes, constraints, triggers, or PL/pgSQL functions
- Write or optimize SQL queries (joins, CTEs, window functions, aggregations)
- Use PostgreSQL-specific features (JSONB, full-text search, array types, pgvector)
- Manage users, roles, and permissions with psql
- Configure backup (pg_dump), replication, or performance tuning (EXPLAIN ANALYZE)

## How to use this skill

### Workflow

1. **Identify the task** - Schema design, query writing, optimization, or administration
2. **Write the SQL** - Use the patterns and examples below
3. **Analyze performance** - Run EXPLAIN ANALYZE on slow queries
4. **Apply best practices** - Index strategy, VACUUM, partitioning as needed

### Quick-Start Example: Table with Index and Query

```sql
-- Create a table with constraints
CREATE TABLE orders (
    id          BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL REFERENCES customers(id),
    status      TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','shipped','delivered')),
    total       NUMERIC(10,2) NOT NULL,
    metadata    JSONB DEFAULT '{}',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Create an index for common queries
CREATE INDEX idx_orders_customer_status ON orders (customer_id, status);

-- Query with CTE and window function
WITH monthly_totals AS (
    SELECT customer_id,
           date_trunc('month', created_at) AS month,
           SUM(total) AS month_total
    FROM orders
    WHERE status = 'delivered'
    GROUP BY customer_id, date_trunc('month', created_at)
)
SELECT customer_id, month, month_total,
       LAG(month_total) OVER (PARTITION BY customer_id ORDER BY month) AS prev_month
FROM monthly_totals;
```

### Performance Analysis

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE customer_id = 42 AND status = 'pending';
```

## Best Practices

1. **Index strategically** - Create indexes for WHERE/JOIN columns; use partial indexes for filtered queries
2. **Run VACUUM regularly** - Prevent table bloat; configure autovacuum thresholds for high-write tables
3. **Partition large tables** - Use range partitioning on timestamp columns for tables over 100M rows
4. **Use ROLE/GRANT** - Grant least privilege; never use superuser for application connections
5. **Backup and verify** - Use `pg_dump` or WAL archiving; test restore procedures regularly

## Keywords

postgresql, postgres, psql, SQL, JSONB, full-text search, CTE, window function, 关系型数据库, 索引, 复制, EXPLAIN ANALYZE, pg_dump, partitioning
