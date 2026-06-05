# 字符串 / 数字 / NULL 处理函数

## 字符串函数

```sql
-- CONCAT / || — 字符串连接
SELECT 'Hello' || ' ' || 'World' FROM DUAL;          -- Hello World (推荐 ||)

-- SUBSTR — 截取子串
SELECT SUBSTR('Oracle Database', 1, 6) FROM DUAL;    -- Oracle
SELECT SUBSTR('Oracle Database', 8) FROM DUAL;       -- Database

-- INSTR — 查找子串位置
SELECT INSTR('oracleoracle', 'oracle') FROM DUAL;               -- 1
SELECT INSTR('oracleoracle', 'oracle', 1, 2) FROM DUAL;         -- 7（第 2 次出现）

-- LPAD / RPAD — 左/右填充
SELECT LPAD('123', 10, '*') FROM DUAL;                           -- *******123
SELECT RPAD('Oracle', 10, '-.-') FROM DUAL;                      -- Oracle-.-.-

-- TRIM / LTRIM / RTRIM — 去除空格/字符
SELECT TRIM('  Hello  ') FROM DUAL;                              -- Hello
SELECT LTRIM('xxxHello', 'x') FROM DUAL;                         -- Hello
SELECT RTRIM('Hello...', '.') FROM DUAL;                         -- Hello

-- REPLACE — 替换子串
SELECT REPLACE('Oracle Database 19c', '19c', '23c') FROM DUAL;  -- Oracle Database 23c

-- TRANSLATE — 字符级替换
SELECT TRANSLATE('12345', '123', 'abc') FROM DUAL;               -- abc45

-- 正则表达式系列
-- REGEXP_LIKE  — 正则匹配
SELECT * FROM employees WHERE REGEXP_LIKE(email, '^[A-Z]');
-- REGEXP_SUBSTR — 正则提取子串
SELECT REGEXP_SUBSTR('contact@oracle.com', '@[^.]+\\.com') FROM DUAL;
-- REGEXP_REPLACE — 正则替换（手机号脱敏）
SELECT REGEXP_REPLACE('13812345678', '(\d{3})\d{4}(\d{4})', '\1****\2') FROM DUAL;
-- REGEXP_INSTR  — 正则查找位置
SELECT REGEXP_INSTR('Hello World', '[aeiou]') FROM DUAL;         -- 2
```

## 数字函数

```sql
-- ROUND — 四舍五入
SELECT ROUND(123.4567) FROM DUAL;      -- 123
SELECT ROUND(123.4567, 2) FROM DUAL;   -- 123.46
SELECT ROUND(123.4567, -2) FROM DUAL;  -- 100

-- TRUNC — 截断（不四舍五入）
SELECT TRUNC(123.4567) FROM DUAL;      -- 123
SELECT TRUNC(123.4567, 2) FROM DUAL;   -- 123.45

-- MOD — 取模
SELECT MOD(10, 3) FROM DUAL;           -- 1

-- ABS / CEIL / FLOOR
SELECT ABS(-10) FROM DUAL;             -- 10
SELECT CEIL(3.14) FROM DUAL;           -- 4
SELECT FLOOR(3.14) FROM DUAL;          -- 3

-- POWER / SQRT
SELECT POWER(2, 10) FROM DUAL;         -- 1024
SELECT SQRT(144) FROM DUAL;            -- 12

-- GREATEST / LEAST
SELECT GREATEST(10, 20, 5, 30) FROM DUAL;  -- 30
SELECT LEAST(10, 20, 5, 30) FROM DUAL;     -- 5
```

## NULL 处理函数

```sql
-- NVL — 空值替换（2 个参数）
SELECT last_name, NVL(commission_pct, 0) AS commission FROM employees;

-- NVL2 — 空值条件（3 个参数）
SELECT last_name, NVL2(commission_pct, '有佣金', '无佣金') AS status FROM employees;

-- COALESCE — 返回第一个非空值（可变参数）
SELECT COALESCE(phone_number, email, '无联系方式') AS contact FROM employees;

-- NULLIF — 两值相等返回 NULL
SELECT NULLIF('A', 'B') FROM DUAL;  -- 'A'
SELECT NULLIF('A', 'A') FROM DUAL;  -- NULL

-- LNNVL — 反转条件结果（对 NULL 敏感）
SELECT * FROM employees WHERE LNNVL(commission_pct > 0.2);
-- 等价于: WHERE commission_pct IS NULL OR commission_pct <= 0.2
```
