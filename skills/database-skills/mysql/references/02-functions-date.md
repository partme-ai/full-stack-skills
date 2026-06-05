# 日期时间函数 (Date & Time Functions)

## 简介

MySQL 的日期时间函数用于获取当前时间、提取日期组件、格式化和计算日期差。在报表统计、时间范围查询、过期计算等场景中高频使用。

## 常用函数速查

### 获取当前日期时间

| 函数 | 说明 | 示例结果 |
|------|------|---------|
| `NOW()` | 当前日期时间 | '2024-03-15 14:30:00' |
| `CURDATE()` | 当前日期 | '2024-03-15' |
| `CURTIME()` | 当前时间 | '14:30:00' |
| `UTC_DATE()` | UTC 当前日期 | '2024-03-15' |
| `UTC_TIME()` | UTC 当前时间 | '06:30:00' |
| `UTC_TIMESTAMP()` | UTC 当前日期时间 | '2024-03-15 06:30:00' |
| `SYSDATE()` | 函数执行时的当前时间（非语句开始时间） | '2024-03-15 14:30:01' |
| `CURRENT_TIMESTAMP` | NOW() 的同义词 | '2024-03-15 14:30:00' |

### 提取日期/时间组件

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `DATE(expr)` | 提取日期部分 | `DATE(NOW())` | '2024-03-15' |
| `TIME(expr)` | 提取时间部分 | `TIME(NOW())` | '14:30:00' |
| `YEAR(date)` | 提取年 | `YEAR('2024-03-15')` | 2024 |
| `MONTH(date)` | 提取月 | `MONTH('2024-03-15')` | 3 |
| `DAY(date)` | 提取日 | `DAY('2024-03-15')` | 15 |
| `HOUR(time)` | 提取时 | `HOUR('14:30:00')` | 14 |
| `MINUTE(time)` | 提取分 | `MINUTE('14:30:00')` | 30 |
| `SECOND(time)` | 提取秒 | `SECOND('14:30:00')` | 0 |
| `EXTRACT(unit FROM date)` | 提取任意部分 | `EXTRACT(MONTH FROM '2024-03-15')` | 3 |

### 日期运算

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `DATE_ADD(date, INTERVAL expr unit)` | 日期加法 | `DATE_ADD(NOW(), INTERVAL 7 DAY)` | 7 天后 |
| `DATE_SUB(date, INTERVAL expr unit)` | 日期减法 | `DATE_SUB(NOW(), INTERVAL 1 MONTH)` | 上月同日 |
| `DATEDIFF(d1, d2)` | 日期差（天） | `DATEDIFF('2024-03-20', '2024-03-15')` | 5 |
| `TIMESTAMPDIFF(unit, d1, d2)` | 灵活时间差 | `TIMESTAMPDIFF(HOUR, '2024-01-01', NOW())` | 小时数 |
| `LAST_DAY(date)` | 月末日期 | `LAST_DAY('2024-02-01')` | '2024-02-29' |

**支持的时间单位**：`MICROSECOND`, `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, `YEAR`

### 格式化与转换

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `DATE_FORMAT(date, fmt)` | 日期格式化 | `DATE_FORMAT(NOW(), '%Y年%m月%d日')` | '2024年03月15日' |
| `TIME_FORMAT(t, fmt)` | 时间格式化 | `TIME_FORMAT('14:30:00', '%H:%i')` | '14:30' |
| `STR_TO_DATE(str, fmt)` | 字符串转日期 | `STR_TO_DATE('2024-03-15', '%Y-%m-%d')` | 2024-03-15 |
| `UNIX_TIMESTAMP([date])` | 转 Unix 时间戳 | `UNIX_TIMESTAMP('2024-03-15')` | 1710489600 |
| `FROM_UNIXTIME(ts)` | 时间戳转日期 | `FROM_UNIXTIME(1710489600)` | '2024-03-15 00:00:00' |

**DATE_FORMAT 常用格式符**：

| 格式符 | 说明 | 示例 |
|--------|------|------|
| `%Y` | 四位年份 | 2024 |
| `%y` | 两位年份 | 24 |
| `%m` | 两位月份 | 03 |
| `%c` | 月份（无前导零） | 3 |
| `%d` | 两位日期 | 15 |
| `%e` | 日期（无前导零） | 15 |
| `%H` | 24 小时制（00-23） | 14 |
| `%h` / `%I` | 12 小时制（01-12） | 02 |
| `%i` | 分钟（00-59） | 30 |
| `%s` | 秒（00-59） | 00 |
| `%W` | 星期名称 | Friday |
| `%M` | 月份名称 | March |
| `%a` | 缩写星期 | Fri |
| `%b` | 缩写月份 | Mar |

### 星期与周

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `WEEKDAY(date)` | 周索引 (0=Mon, 6=Sun) | `WEEKDAY('2024-03-18')` | 0 (周一) |
| `DAYOFWEEK(date)` | 周索引 (1=Sun, 7=Sat) | `DAYOFWEEK('2024-03-18')` | 2 (周一) |
| `DAYNAME(date)` | 星期名 | `DAYNAME('2024-03-18')` | 'Monday' |
| `MONTHNAME(date)` | 月份名 | `MONTHNAME('2024-03-18')` | 'March' |
| `WEEK(date[, mode])` | 周数 | `WEEK('2024-03-18')` | 12 |
| `WEEKOFYEAR(date)` | ISO 周数 | `WEEKOFYEAR('2024-03-18')` | 12 |
| `QUARTER(date)` | 季度 | `QUARTER('2024-03-18')` | 1 |
| `DAYOFYEAR(date)` | 一年中的第几天 | `DAYOFYEAR('2024-03-18')` | 78 |

## 业务场景

### 场景 1: 本月、本周、本日统计

```sql
-- 本月注册用户
SELECT COUNT(*) FROM user
WHERE created_at >= DATE_FORMAT(CURDATE(), '%Y-%m-01');

-- 本周注册用户（周一为一周开始）
SELECT COUNT(*) FROM user
WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY);

-- 今日统计
SELECT COUNT(*) FROM `order`
WHERE DATE(created_at) = CURDATE();
```

### 场景 2: 按年月聚合

```sql
SELECT 
  DATE_FORMAT(created_at, '%Y-%m') AS month, 
  COUNT(*) AS order_count,
  SUM(amount) AS total_revenue
FROM `order`
GROUP BY month
ORDER BY month;
```

### 场景 3: 计算用户注册天数

```sql
SELECT id, name, 
  DATEDIFF(NOW(), created_at) AS days_since_reg 
FROM user;
```

### 场景 4: 计算任务耗时

```sql
SELECT task_id, 
  TIMESTAMPDIFF(SECOND, start_time, end_time) AS duration_seconds
FROM task;
```

### 场景 5: 上月同期对比

```sql
SELECT 
  DATE_FORMAT(created_at, '%Y-%m-%d') AS day,
  COUNT(*) AS orders_today
FROM `order`
WHERE created_at >= DATE_SUB(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), INTERVAL WEEKDAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH)) DAY)
  AND created_at < CURDATE();
```

## 注意事项

- `DATETIME` vs `TIMESTAMP`：`TIMESTAMP` 会自动时区转换，范围仅到 2038 年
- `NOW()` 和 `SYSDATE()` 的区别：`NOW()` 返回语句开始的时刻，`SYSDATE()` 返回函数执行时的时刻
- MySQL 5.6.4+ 支持毫秒精度：`NOW(3)`, `CURTIME(6)`
- 日期函数中使用 `DATE()` 包裹列会导致索引失效（应改用范围查询）
