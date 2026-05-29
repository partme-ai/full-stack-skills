# 分析函数（窗口函数）+ 聚合

分析函数是 Oracle 最强大的功能之一，在不改变行数的情况下进行聚合计算。

## 聚合函数

```sql
-- 基础聚合
SELECT COUNT(*) FROM employees;                     -- 总行数
SELECT COUNT(commission_pct) FROM employees;        -- 非 NULL 行数
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MAX(hire_date) FROM employees;
SELECT MIN(hire_date) FROM employees;

-- MEDIAN — 中位数
SELECT MEDIAN(salary) FROM employees;

-- STATS_MODE — 众数
SELECT STATS_MODE(department_id) FROM employees;

-- GROUP BY ROLLUP / CUBE（小计+总计）
SELECT department_id, job_id, SUM(salary)
FROM employees
WHERE department_id IN (50, 80)
GROUP BY ROLLUP(department_id, job_id);   -- 小计 + 总计

SELECT department_id, job_id, SUM(salary)
FROM employees
WHERE department_id IN (50, 80)
GROUP BY CUBE(department_id, job_id);    -- 所有维度小计

-- GROUPING — 区分 NULL 是数据值还是小计行
SELECT department_id, job_id, SUM(salary),
       CASE WHEN GROUPING(department_id)=1 THEN '总计'
            WHEN GROUPING(job_id)=1 THEN '小计'
            ELSE '明细'
       END AS rollup_level
FROM employees GROUP BY ROLLUP(department_id, job_id);
```

## 分析函数（窗口函数）

### 排序函数

```sql
-- ROW_NUMBER — 唯一序号
SELECT department_id, last_name, salary,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS seq
FROM employees;

-- RANK / DENSE_RANK — 排名（允许并列）
SELECT department_id, last_name, salary,
       RANK()       OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
FROM employees;
-- RANK: 1,2,2,4   DENSE_RANK: 1,2,2,3

-- NTILE — 分桶
SELECT customer_id, amount,
       NTILE(5) OVER (ORDER BY amount DESC) AS bucket
FROM orders;
```

### 前后行访问

```sql
-- LAG — 访问前一行（环比计算）
SELECT hire_date, salary,
       LAG(salary, 1, 0) OVER (ORDER BY hire_date) AS prev_salary,
       salary - LAG(salary, 1, 0) OVER (ORDER BY hire_date) AS diff
FROM employees;

-- LEAD — 访问后一行
SELECT hire_date, salary,
       LEAD(salary, 1) OVER (ORDER BY hire_date) AS next_salary
FROM employees;
```

### 窗口聚合

```sql
-- FIRST_VALUE / LAST_VALUE — 窗口首尾行
SELECT department_id, last_name, salary,
       FIRST_VALUE(salary) OVER (PARTITION BY department_id
           ORDER BY salary DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS max_in_dept
FROM employees;

-- 累计求和
SELECT sale_date, amount,
       SUM(amount) OVER (ORDER BY sale_date) AS running_total
FROM daily_sales;

-- 移动平均（7 日）
SELECT sale_date, amount,
       AVG(amount) OVER (ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7d
FROM daily_sales;

-- RATIO_TO_REPORT — 占比
SELECT department_id, last_name, salary,
       RATIO_TO_REPORT(salary) OVER (PARTITION BY department_id) AS pct_of_dept
FROM employees;
```
