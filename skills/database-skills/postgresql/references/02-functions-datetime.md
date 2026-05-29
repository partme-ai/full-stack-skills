# 日期/时间函数详解

```sql
-- AGE — 计算时间差
SELECT AGE('2024-05-29', '2023-01-15');
-- 结果: 1 year 4 mons 14 days

-- 计算年龄
SELECT id, EXTRACT(YEAR FROM AGE(birth_date)) AS age FROM users;

-- DATE_TRUNC — 时间截断（支持: microsecond, millisecond, second, minute, hour, day, week, month, quarter, year, decade, century, millennium）
SELECT DATE_TRUNC('month', created_at) AS month, COUNT(*) AS order_count
FROM orders GROUP BY month;

-- EXTRACT — 提取日期部分
SELECT
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    EXTRACT(DOW FROM created_at) AS day_of_week,  -- 0=Sunday
    EXTRACT(HOUR FROM created_at) AS hour,
    EXTRACT(QUARTER FROM created_at) AS quarter
FROM orders;

-- TO_CHAR — 日期格式化
SELECT
    TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI:SS') AS formatted_time,
    TO_CHAR(created_at, 'YYYY年MM月DD日') AS chinese_date,
    TO_CHAR(created_at, 'Day, DD Month YYYY') AS english_date,
    TO_CHAR(created_at, 'IW') AS iso_week_number
FROM orders;

-- JUSTIFY_DAYS / JUSTIFY_HOURS / JUSTIFY_INTERVAL
SELECT JUSTIFY_DAYS(30::INTERVAL);   -- 30 days → 1 mon
SELECT JUSTIFY_HOURS(100::INTERVAL); -- 100:00:00 → 4 days 04:00:00

-- MAKE_DATE / MAKE_TIMESTAMPTZ / MAKE_INTERVAL (PG 10+)
SELECT MAKE_DATE(2024, 6, 1);
SELECT MAKE_TIMESTAMPTZ(2024, 6, 1, 10, 30, 0, 'Asia/Shanghai');
SELECT MAKE_INTERVAL(days => 10, hours => 5);

-- DATE 运算
SELECT NOW(), NOW() + INTERVAL '1 day', NOW() - INTERVAL '3 hours';
SELECT CURRENT_DATE, CURRENT_TIME;

-- 时区转换
SELECT
    NOW() AT TIME ZONE 'Asia/Shanghai',
    NOW() AT TIME ZONE 'UTC',
    '2024-06-01 10:00:00+08'::TIMESTAMPTZ AT TIME ZONE 'America/New_York';

-- 日期范围查询最佳实践
-- ❌ 避免: WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31'
-- ✅ 推荐: WHERE created_at >= '2024-01-01' AND created_at < '2024-02-01'
```
