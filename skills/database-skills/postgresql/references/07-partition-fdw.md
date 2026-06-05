# 分区表与 FDW 详解

## 分区表 (PG 10+)

### RANGE 分区

```sql
CREATE TABLE orders_partitioned (
    id BIGSERIAL, user_id INTEGER NOT NULL, total_amount NUMERIC(12,2),
    status TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
) PARTITION BY RANGE (created_at);

CREATE TABLE orders_2024_01 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
CREATE TABLE orders_2024_02 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- 默认分区
CREATE TABLE orders_default PARTITION OF orders_partitioned DEFAULT;
```

### LIST 分区

```sql
CREATE TABLE customers_partitioned (
    id BIGSERIAL, name TEXT NOT NULL, region TEXT NOT NULL
) PARTITION BY LIST (region);

CREATE TABLE customers_asia PARTITION OF customers_partitioned
    FOR VALUES IN ('CN', 'JP', 'KR', 'SG');
CREATE TABLE customers_americas PARTITION OF customers_partitioned
    FOR VALUES IN ('US', 'CA', 'BR', 'MX');
```

### HASH 分区

```sql
CREATE TABLE logs_partitioned (
    id BIGSERIAL, level TEXT, message TEXT, logged_at TIMESTAMPTZ DEFAULT NOW()
) PARTITION BY HASH (id);

CREATE TABLE logs_p0 PARTITION OF logs_partitioned FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE logs_p1 PARTITION OF logs_partitioned FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE logs_p2 PARTITION OF logs_partitioned FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE logs_p3 PARTITION OF logs_partitioned FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

### 子分区 (PG 11+)

```sql
CREATE TABLE sales (id BIGSERIAL, sale_date DATE NOT NULL, region TEXT NOT NULL, amount NUMERIC(12,2))
PARTITION BY RANGE (sale_date);

CREATE TABLE sales_2024_q1 PARTITION OF sales
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01')
    PARTITION BY LIST (region);
```

### 分区维护

```sql
-- 添加新分区
CREATE TABLE orders_2024_04 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2024-04-01') TO ('2024-05-01');

-- 分离分区（变成独立表）
ALTER TABLE orders_partitioned DETACH PARTITION orders_2024_01;

-- 附加分区
ALTER TABLE orders_partitioned ATTACH PARTITION orders_2024_01
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

-- 分区裁剪自动生效
EXPLAIN SELECT * FROM orders_partitioned
WHERE created_at >= '2024-02-15' AND created_at < '2024-03-01';
-- 只在 orders_2024_02 分区上扫描

-- 分区表索引自动应用到所有分区
CREATE INDEX ON orders_partitioned (user_id);
CREATE INDEX ON orders_partitioned (created_at DESC);
```

### 分区最佳实践

- 每个分区 1-10GB 为宜
- 时间分区常用：日、周、月、季
- 定期分离旧分区用于归档
- 分区数不宜超过 1000
- 分区键直接影响分区裁剪能力

## FDW (Foreign Data Wrapper)

### postgres_fdw — 跨 PG 数据库

```sql
CREATE EXTENSION postgres_fdw;

CREATE SERVER remote_prod FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host '192.168.1.100', port '5432', dbname 'prod_db');

CREATE USER MAPPING FOR current_user SERVER remote_prod
OPTIONS (user 'readonly_user', password 'secret');

CREATE FOREIGN TABLE remote_orders (
    id BIGINT, user_id INTEGER, total_amount NUMERIC(12,2), status TEXT, created_at TIMESTAMPTZ
) SERVER remote_prod OPTIONS (schema_name 'public', table_name 'orders');

-- 查询远程表
SELECT * FROM remote_orders WHERE created_at > NOW() - INTERVAL '1 hour';

-- 批量导入外部表结构
IMPORT FOREIGN SCHEMA public FROM SERVER remote_prod INTO local_schema
LIMIT TO (users, orders, products);
```

### file_fdw — 读取 CSV

```sql
CREATE EXTENSION file_fdw;
CREATE SERVER file_server FOREIGN DATA WRAPPER file_fdw;

CREATE FOREIGN TABLE csv_orders (
    id BIGINT, user_id INTEGER, amount NUMERIC(10,2), order_date DATE
) SERVER file_server OPTIONS (filename '/data/orders.csv', format 'csv', header 'true');

SELECT SUM(amount) FROM csv_orders WHERE order_date >= '2024-01-01';
```

### FDW 性能考量

- 适合小数据量或低频跨库查询
- 大数据量传输建议用逻辑复制或 ETL
- WHERE 条件尽量 push down 到远程
