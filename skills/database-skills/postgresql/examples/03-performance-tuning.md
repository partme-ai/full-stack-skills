# 性能调优示例

## 场景 1：定位慢查询

使用 EXPLAIN ANALYZE 诊断查询性能问题。

```sql
-- 创建测试表
CREATE TABLE orders (
    id BIGSERIAL, user_id INTEGER NOT NULL, status TEXT,
    total_amount NUMERIC(12,2), created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 插入测试数据（假设已有数百万行）

-- 诊断慢查询
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders WHERE status = 'pending' AND created_at > '2024-01-01';
-- 如果看到 Seq Scan → 需要加索引

-- 创建复合索引
CREATE INDEX idx_orders_status_created ON orders (status, created_at DESC);

-- 再次验证
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders WHERE status = 'pending' AND created_at > '2024-01-01';
-- 现在应该看到 Index Scan
```

## 场景 2：JOIN 性能优化

```sql
-- 慢查询：大表 JOIN + GROUP BY
EXPLAIN (ANALYZE, BUFFERS)
SELECT u.name, COUNT(o.id) AS order_count
FROM users u LEFT JOIN orders o ON o.user_id = u.id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name;

-- 检查输出中的 Sort Method
-- 如果看到 "external merge Disk: 1536kB" → work_mem 不足

-- 临时增加 work_mem（当前会话）
SET work_mem = '256MB';

-- 或者创建覆盖索引
CREATE INDEX idx_orders_user_id_covering ON orders (user_id) INCLUDE (id);
```

## 场景 3：VACUUM 与膨胀监控

```sql
-- 查看表膨胀情况
SELECT relname, n_live_tup, n_dead_tup,
       ROUND(n_dead_tup::NUMERIC / NULLIF(n_live_tup, 0) * 100, 2) AS dead_pct,
       last_autovacuum, last_autoanalyze
FROM pg_stat_user_tables
WHERE n_dead_tup > 0
ORDER BY n_dead_tup DESC LIMIT 20;

-- 为高频更新表调优 autovacuum
ALTER TABLE orders SET (
    autovacuum_vacuum_scale_factor = 0.05,
    autovacuum_vacuum_threshold = 1000
);

-- 检查事务 ID 回卷风险
SELECT datname, age(datfrozenxid) AS age,
       ROUND(100 * age(datfrozenxid)::NUMERIC / 2000000000, 2) AS pct_wraparound
FROM pg_database ORDER BY age DESC;
```

## 场景 4：pg_stat_statements 分析

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- TOP 10 最耗时查询
SELECT queryid, LEFT(query, 80) AS query_preview, calls,
       ROUND(total_exec_time::NUMERIC, 2) AS total_ms,
       ROUND(mean_exec_time::NUMERIC, 2) AS avg_ms,
       ROUND(shared_blks_hit::NUMERIC / NULLIF(shared_blks_hit + shared_blks_read, 0) * 100, 2) AS hit_ratio
FROM pg_stat_statements
ORDER BY total_exec_time DESC LIMIT 10;

-- TOP 10 I/O 密集查询
SELECT queryid, LEFT(query, 80) AS query_preview,
       shared_blks_read, temp_blks_read
FROM pg_stat_statements
WHERE shared_blks_read > 1000
ORDER BY shared_blks_read DESC LIMIT 10;

-- TOP 10 临时文件使用（work_mem 不足）
SELECT queryid, LEFT(query, 80) AS query_preview,
       temp_blk_read_time, temp_blk_write_time
FROM pg_stat_statements
WHERE temp_blk_read_time > 0
ORDER BY temp_blk_read_time DESC LIMIT 10;
```

## 场景 5：配置调优参考

```conf
# 64GB 内存服务器参考配置
shared_buffers = 12GB            # 物理内存 20-25%
work_mem = 64MB                  # 每个排序操作
maintenance_work_mem = 1GB       # VACUUM/CREATE INDEX
effective_cache_size = 12GB      # 规划器缓存估计
wal_buffers = 16MB
max_connections = 200            # 超过则用 PgBouncer
checkpoint_timeout = 15min
max_wal_size = 16GB
default_statistics_target = 100  # 大表可调至 500-1000
```
