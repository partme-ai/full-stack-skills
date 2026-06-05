# 聚合/窗口函数详解

## 聚合函数

```sql
-- ARRAY_AGG — 聚合为数组
SELECT o.id, ARRAY_AGG(p.name ORDER BY p.name) AS products
FROM orders o JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON p.id = oi.product_id GROUP BY o.id;

-- STRING_AGG — 聚合为字符串
SELECT article_id, STRING_AGG(DISTINCT tag, ', ' ORDER BY tag) AS tags
FROM article_tags GROUP BY article_id;

-- JSON_AGG / JSONB_AGG — 聚合为 JSON
SELECT o.id, JSONB_AGG(JSONB_BUILD_OBJECT('product_id', oi.product_id, 'qty', oi.quantity)) AS items
FROM orders o JOIN order_items oi ON oi.order_id = o.id GROUP BY o.id;

-- MODE — 众数
SELECT MODE() WITHIN GROUP (ORDER BY category_id) FROM products;

-- PERCENTILE_CONT / PERCENTILE_DISC — 百分位数
SELECT
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_amount) AS median,
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY total_amount) AS q1,
    PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY total_amount) AS p90
FROM orders;

-- GROUPING SETS / CUBE / ROLLUP
SELECT COALESCE(department, 'ALL') AS dept, COALESCE(role, 'ALL') AS role,
       COUNT(*) AS cnt, AVG(salary)::NUMERIC(10,2) AS avg_sal
FROM employees
GROUP BY GROUPING SETS ((department, role), (department), (role), ());

SELECT category, brand, COUNT(*) FROM products GROUP BY CUBE (category, brand);

SELECT EXTRACT(YEAR FROM created_at) AS year, EXTRACT(MONTH FROM created_at) AS month,
       COUNT(*) FROM orders GROUP BY ROLLUP (year, month) ORDER BY year, month;
```

## 窗口函数

```sql
-- ROW_NUMBER — 行号
SELECT id, name, category_id, price,
       ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY price DESC) AS rn
FROM products;

-- RANK / DENSE_RANK — 排名
SELECT salesperson, amount,
       RANK() OVER (ORDER BY amount DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank
FROM monthly_sales;

-- NTILE — 分桶
SELECT id, total_spent, NTILE(4) OVER (ORDER BY total_spent DESC) AS quartile
FROM customers;

-- LAG / LEAD — 前后行访问
SELECT dt, revenue,
       LAG(revenue, 1) OVER (ORDER BY dt) AS prev_day,
       LAG(revenue, 7) OVER (ORDER BY dt) AS prev_week,
       ROUND((revenue - LAG(revenue, 1) OVER (ORDER BY dt))
             / NULLIF(LAG(revenue, 1) OVER (ORDER BY dt), 0) * 100, 2) AS dod_pct,
       LEAD(revenue, 1) OVER (ORDER BY dt) AS next_day
FROM daily_revenue;

-- FIRST_VALUE / LAST_VALUE
SELECT category_id, name, price,
       FIRST_VALUE(price) OVER (PARTITION BY category_id ORDER BY price) AS min_price,
       LAST_VALUE(price) OVER (PARTITION BY category_id ORDER BY price
           RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS max_price
FROM products;

-- NTH_VALUE
SELECT DISTINCT category_id,
       NTH_VALUE(name, 3) OVER (PARTITION BY category_id ORDER BY price DESC
           RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS third_expensive
FROM products;

-- 窗口帧控制
SELECT dt, revenue,
       AVG(revenue) OVER (ORDER BY dt ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma_7d,
       AVG(revenue) OVER (ORDER BY dt ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS ma_30d
FROM daily_revenue;

-- 累积求和
SELECT dt, revenue, SUM(revenue) OVER (ORDER BY dt) AS cumulative_revenue
FROM daily_revenue;

-- 分组累计
SELECT category_id, dt, revenue,
       SUM(revenue) OVER (PARTITION BY category_id ORDER BY dt ROWS UNBOUNDED PRECEDING) AS cum_by_cat
FROM daily_revenue_by_category;

-- 窗口函数 + FILTER 条件聚合
SELECT dt,
       COUNT(*) AS total,
       COUNT(*) FILTER (WHERE status = 'paid') AS paid,
       COUNT(*) FILTER (WHERE status = 'cancelled') AS cancelled
FROM orders GROUP BY dt;
```

## 数组函数

```sql
-- ARRAY — 构建数组
SELECT ARRAY[1, 2, 3], ARRAY['a', 'b', 'c'];

-- ANY / ALL — 元素检查
SELECT * FROM articles WHERE '数据库' = ANY(tags);

-- UNNEST — 展开数组
SELECT UNNEST(tags) AS tag, COUNT(*) AS freq
FROM articles GROUP BY tag ORDER BY freq DESC;

-- ARRAY_APPEND / ARRAY_PREPEND / ARRAY_REMOVE / ARRAY_CAT
SELECT ARRAY_APPEND(ARRAY[1,2], 3);      -- {1,2,3}
SELECT ARRAY_PREPEND(0, ARRAY[1,2]);      -- {0,1,2}
SELECT ARRAY_REMOVE(ARRAY[1,2,3], 2);     -- {1,3}
SELECT ARRAY_CAT(ARRAY[1,2], ARRAY[3,4]); -- {1,2,3,4}

-- 数组信息
SELECT ARRAY_NDIMS(ARRAY[[1,2],[3,4]]), ARRAY_LENGTH(ARRAY[1,2,3], 1);

-- ARRAY_POSITION / ARRAY_POSITIONS
SELECT ARRAY_POSITION(ARRAY['a','b','c','b'], 'b');    -- 2
SELECT ARRAY_POSITIONS(ARRAY['a','b','c','b'], 'b');    -- {2,4}

-- STRING_TO_ARRAY / ARRAY_TO_STRING
SELECT STRING_TO_ARRAY('a,b,c', ','), ARRAY_TO_STRING(ARRAY['a','b','c'], '|');

-- 数组切片
SELECT tags[1:3] FROM articles;

-- @> / <@ — 包含, && — 重叠
SELECT * FROM articles WHERE tags @> ARRAY['SQL', '高级'];
SELECT * FROM articles WHERE tags && ARRAY['数据库', 'JSON'];

-- 数组 GIN 索引
CREATE INDEX idx_articles_tags_gin ON articles USING GIN (tags);
```
