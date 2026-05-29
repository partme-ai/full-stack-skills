# 索引类型与视图详解

## 6种索引类型

| 索引类型 | 适用场景 | 操作符 | 典型用途 |
|---------|---------|--------|---------|
| **B-Tree** (默认) | 等值/范围查询 | =, <, <=, >, >=, BETWEEN, IN, IS NULL, LIKE ('abc%') | 主键、外键、排序字段 |
| **Hash** | 等值查询 | = | 长随机值的等值比较 (有限用途) |
| **GiST** | 几何/全文/范围 | &&, <@, @>, <<, >>, ~= | PostGIS、范围排除约束 |
| **GIN** | 复合值索引 | @>, <@, ?, ?|, ?&, @@ | JSONB、数组、全文搜索 |
| **BRIN** | 大表顺序相关数据 | =, <, <=, >, >=, BETWEEN | 时间序列、日志表 (节省 95%+ 空间) |
| **SP-GiST** | 空间分区/聚类 | 同 GiST | 四叉树、k-d 树、前缀树 |

## 索引创建

```sql
-- B-Tree
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_orders_created_at ON orders (created_at DESC);
CREATE INDEX idx_orders_user_status ON orders (user_id, status);

-- 复合索引列顺序: 等值在前，范围在后，选择性高的在前
-- ✅ WHERE user_id = 1 AND status = 'paid'  → 索引 (user_id, status) 最优
-- ❌ WHERE status = 'paid' AND created_at > '2024-01-01' → 索引 (created_at, status) 更好

-- 部分索引（仅索引活跃用户，更小更快）
CREATE INDEX idx_users_active ON users (email) WHERE is_active = TRUE;

-- 覆盖索引 / INCLUDE (PG 11+, 避免回表)
CREATE INDEX idx_orders_covering ON orders (user_id, status) INCLUDE (total_amount, created_at);

-- Hash 索引
CREATE INDEX idx_users_email_hash ON users USING HASH (email);

-- GIN 索引
CREATE INDEX idx_articles_body_tsv ON articles USING GIN (body_tsv);
CREATE INDEX idx_config_gin ON user_configs USING GIN (config);
CREATE INDEX idx_articles_tags_gin ON articles USING GIN (tags);
CREATE INDEX idx_config_path ON user_configs USING GIN (config jsonb_path_ops);

-- GiST 索引
CREATE INDEX idx_room_bookings_period ON room_bookings USING GIST (period);

-- BRIN 索引（大表时序数据，极大节省空间）
CREATE INDEX idx_orders_brin ON orders USING BRIN (created_at) WITH (pages_per_range = 32);

-- CONCURRENTLY — 在线建索引（不阻塞写）
CREATE INDEX CONCURRENTLY idx_orders_user_id ON orders (user_id);
```

## 索引维护

```sql
-- DROP INDEX CONCURRENTLY — 在线删除
DROP INDEX CONCURRENTLY IF EXISTS idx_orders_old;

-- REINDEX — 重建索引（索引膨胀时）
REINDEX INDEX idx_orders_user_id;
REINDEX TABLE orders;
REINDEX DATABASE mydb;

-- REINDEX CONCURRENTLY — 在线重建 (PG 12+)
REINDEX INDEX CONCURRENTLY idx_orders_user_id;
```

## 视图 (View)

```sql
-- 普通视图 — 虚拟表
CREATE VIEW user_order_summary AS
SELECT u.id, u.username, COUNT(o.id) AS total_orders,
       COALESCE(SUM(o.total_amount), 0) AS total_spent,
       MAX(o.created_at) AS last_order_date
FROM users u LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.username;

-- WITH CHECK OPTION — 确保更新满足视图条件
CREATE VIEW paid_orders AS SELECT * FROM orders WHERE status = 'paid'
WITH CHECK OPTION;

-- 物化视图 — 物理存储的快照
CREATE MATERIALIZED VIEW mv_monthly_sales AS
SELECT DATE_TRUNC('month', o.created_at) AS month, p.category_id,
       COUNT(DISTINCT o.id) AS order_count, SUM(oi.quantity * oi.price) AS revenue
FROM orders o JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON p.id = oi.product_id
GROUP BY month, p.category_id WITH DATA;

-- 刷新物化视图
REFRESH MATERIALIZED VIEW mv_monthly_sales;

-- 并发刷新（需唯一索引, PG 9.4+）
CREATE UNIQUE INDEX idx_mv_monthly_sales_unique ON mv_monthly_sales (month, category_id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_monthly_sales;
```
