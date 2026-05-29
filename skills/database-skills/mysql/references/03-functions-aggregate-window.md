# 聚合函数与窗口函数 (Aggregate & Window Functions)

## 聚合函数 (Aggregate Functions)

### 简介

聚合函数对一组行进行计算并返回单个值，常与 `GROUP BY` 子句配合使用，用于统计汇总和报表生成。

### 常用聚合函数

| 函数 | 说明 | 使用示例 | 注意 |
|------|------|---------|------|
| `COUNT(*)` | 行数计数（含 NULL） | `COUNT(*)` | 性能最好 |
| `COUNT(expr)` | 非 NULL 值计数 | `COUNT(column_name)` | 排除 NULL |
| `COUNT(DISTINCT expr)` | 去重计数 | `COUNT(DISTINCT user_id)` | UV 统计 |
| `SUM(expr)` | 求和 | `SUM(amount)` | 忽略 NULL |
| `AVG(expr)` | 平均值 | `AVG(score)` | SUM/COUNT 实现 |
| `MAX(expr)` | 最大值 | `MAX(price)` | 字符串按字典序 |
| `MIN(expr)` | 最小值 | `MIN(price)` | 字符串按字典序 |
| `GROUP_CONCAT(expr)` | 组内拼接 | `GROUP_CONCAT(name SEPARATOR ',')` | 长度限制 1024 |

### 业务场景

#### 订单日报统计

```sql
SELECT
  COUNT(*) AS total_orders,
  COUNT(DISTINCT user_id) AS unique_users,
  SUM(amount) AS total_revenue,
  AVG(amount) AS avg_order_amount,
  MAX(amount) AS max_order,
  MIN(amount) AS min_order
FROM `order`
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 1 DAY);
```

#### GROUP_CONCAT 行转列

```sql
SELECT 
  u.name,
  GROUP_CONCAT(o.order_no ORDER BY o.created_at SEPARATOR ', ') AS orders
FROM user u
LEFT JOIN `order` o ON u.id = o.user_id
GROUP BY u.id;
```

#### CASE WHEN 条件聚合 (Pivot)

```sql
SELECT
  SUM(CASE WHEN amount < 100 THEN 1 ELSE 0 END) AS low_orders,
  SUM(CASE WHEN amount BETWEEN 100 AND 1000 THEN 1 ELSE 0 END) AS mid_orders,
  SUM(CASE WHEN amount > 1000 THEN 1 ELSE 0 END) AS high_orders
FROM `order`;
```

## 窗口函数 (Window Functions, MySQL 8.0+)

### 简介

窗口函数在不折叠行的情况下对结果集进行聚合和排名计算。与 `GROUP BY` 不同，窗口函数保留所有原始行，为每行添加计算结果。

**语法**：

```sql
function_name() OVER (
  [PARTITION BY col1, col2, ...]  -- 分组（可选）
  [ORDER BY col ASC|DESC]          -- 排序（可选）
  [frame_clause]                   -- 窗口帧（可选）
)
```

### 排名函数

| 函数 | 说明 | 行为特点 | 业务场景 |
|------|------|---------|---------|
| `ROW_NUMBER()` | 行号 | 每行唯一连续编号，无并列 | TOP-N 查询、分页去重 |
| `RANK()` | 排名 | 并列跳号（如 1,1,3） | 竞赛排名 |
| `DENSE_RANK()` | 密集排名 | 并列不跳号（如 1,1,2） | 销售排名分组 |
| `NTILE(n)` | 分桶 | 均分为 n 组 | 四分位分析、数据分桶 |

#### 示例：每部门薪资 TOP 3

```sql
SELECT dept_id, name, salary
FROM (
  SELECT dept_id, name, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
  FROM employee
) t
WHERE rn <= 3;
```

#### 示例：考试成绩排名

```sql
SELECT name, score,
  RANK() OVER (ORDER BY score DESC) AS rnk,
  DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rnk
FROM exam_score;
```

### 偏移函数

| 函数 | 说明 | 业务场景 |
|------|------|---------|
| `LAG(col, offset, default)` | 向前取第 N 行 | 环比、同比 |
| `LEAD(col, offset, default)` | 向后取第 N 行 | 下期预测 |
| `FIRST_VALUE(col)` | 窗口内第一个值 | 基准对比 |
| `LAST_VALUE(col)` | 窗口内最后一个值 | 期末值 |
| `NTH_VALUE(col, n)` | 窗口内第 N 个值 | 指定位置值 |

#### 示例：日环比增长

```sql
SELECT created_at, amount,
  LAG(amount, 1, 0) OVER (ORDER BY created_at) AS prev_amount,
  amount - LAG(amount, 1, 0) OVER (ORDER BY created_at) AS diff,
  ROUND((amount - LAG(amount, 1, 0) OVER (ORDER BY created_at)) / 
        LAG(amount, 1, 0) OVER (ORDER BY created_at) * 100, 2) AS growth_pct
FROM daily_sales;
```

### 聚合窗口函数（累计计算）

聚合函数（SUM、AVG、COUNT 等）加上 `OVER()` 子句后可作为窗口函数使用。

#### 示例：月度累计销售额

```sql
SELECT date, amount,
  SUM(amount) OVER (ORDER BY date) AS cumulative_sum,
  AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7d
FROM daily_sales;
```

#### 示例：部门内薪资对比

```sql
SELECT dept_id, name, salary,
  AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg_salary,
  salary - AVG(salary) OVER (PARTITION BY dept_id) AS diff_from_avg,
  ROUND(salary / AVG(salary) OVER (PARTITION BY dept_id) * 100, 2) AS pct_of_avg
FROM employee;
```

### 窗口帧 (Frame Clause)

帧定义了窗口函数的计算范围：

| 帧语法 | 说明 |
|--------|------|
| `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` | 从开始到当前行（默认） |
| `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` | 前 6 行到当前行（移动平均） |
| `ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING` | 当前行到结束 |
| `ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING` | 前后各 3 行 |
| `RANGE BETWEEN ...` | 按值范围而非行数 |
| `ROWS UNBOUNDED PRECEDING` | 从开始到当前行（简写） |

## 注意事项

- `COUNT(*)` 和 `COUNT(col)` 不同：前者包含 NULL 行，后者排除
- `GROUP_CONCAT` 结果受 `group_concat_max_len` 限制（默认 1024），可 `SET SESSION group_concat_max_len = 10000;`
- 窗口函数只能在 `SELECT` 和 `ORDER BY` 中使用，不能在 `WHERE`、`GROUP BY`、`HAVING` 中使用
- `LAST_VALUE` 的默认帧是 `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`，需要在 ORDER BY 后显式指定帧才能得到正确结果
