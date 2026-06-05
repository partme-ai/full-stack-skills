# 字符串函数 (String Functions)

## 简介

MySQL 提供丰富的字符串处理函数，用于字符串拼接、截取、替换、格式化等操作。这些函数在数据清洗、脱敏、报表生成中广泛使用。

## 常用函数速查

### 拼接与格式化

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `CONCAT(s1, s2, ...)` | 字符串拼接 | `CONCAT(first_name, ' ', last_name)` | 'John Doe' |
| `CONCAT_WS(sep, s1, s2)` | 带分隔符拼接 | `CONCAT_WS('-', '2024', '01', '15')` | '2024-01-15' |
| `GROUP_CONCAT(col)` | 分组拼接 | `GROUP_CONCAT(name ORDER BY id SEPARATOR ',')` | 'a,b,c' |
| `FORMAT(x, d)` | 千分位格式化 | `FORMAT(12345.67, 2)` | '12,345.67' |
| `LPAD(s, n, pad)` | 左填充 | `LPAD('7', 3, '0')` | '007' |
| `RPAD(s, n, pad)` | 右填充 | `RPAD('7', 3, '0')` | '700' |

### 截取与定位

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `SUBSTRING(s, pos, len)` | 子串 | `SUBSTRING('Hello World', 1, 5)` | 'Hello' |
| `LEFT(s, n)` | 左截取 | `LEFT('abcde', 3)` | 'abc' |
| `RIGHT(s, n)` | 右截取 | `RIGHT('abcde', 2)` | 'de' |
| `LOCATE(sub, s, pos)` | 子串位置 | `LOCATE('is', 'this is test')` | 3 |
| `INSTR(s, sub)` | 子串位置 | `INSTR('this is test', 'is')` | 3 |
| `SUBSTRING_INDEX(s, delim, n)` | 按分隔符截取 | `SUBSTRING_INDEX('a,b,c', ',', 2)` | 'a,b' |

### 替换与转换

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `REPLACE(s, from, to)` | 替换 | `REPLACE('abc123', '123', '456')` | 'abc456' |
| `INSERT(s, pos, len, new)` | 插入替换 | `INSERT('phone', 2, 4, '****')` | 'p****e' |
| `UPPER(s)` / `LOWER(s)` | 大小写转换 | `UPPER('abc')` | 'ABC' |
| `TRIM(s)` | 去首尾空格 | `TRIM(' abc ')` | 'abc' |
| `LTRIM(s)` / `RTRIM(s)` | 去左/右空格 | `LTRIM(' abc')` | 'abc' |
| `REVERSE(s)` | 逆序 | `REVERSE('abc')` | 'cba' |
| `REPEAT(s, n)` | 重复 | `REPEAT('x', 5)` | 'xxxxx' |

### 长度与校验

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `LENGTH(s)` | 字节长度 | `LENGTH('你好')` | 6 (utf8mb4) |
| `CHAR_LENGTH(s)` | 字符长度 | `CHAR_LENGTH('你好')` | 2 |
| `BIT_LENGTH(s)` | 位长度 | `BIT_LENGTH('A')` | 8 |
| `ORD(s)` | 首字符 ASCII | `ORD('A')` | 65 |
| `ASCII(s)` | 首字符 ASCII | `ASCII('A')` | 65 |

## 业务场景

### 场景 1: 手机号脱敏

```sql
SELECT 
  REPLACE(phone, SUBSTRING(phone, 4, 4), '****') AS masked_phone 
FROM user;
-- 138****0000

-- 更推荐的做法（INSERT 函数）
SELECT INSERT(phone, 4, 4, '****') AS masked_phone FROM user;
```

### 场景 2: 商品编号补零

```sql
SELECT CONCAT('PRD', LPAD(id, 5, '0')) AS product_no FROM product;
-- PRD00001, PRD00002, ...
```

### 场景 3: 统计每个用户的所有订单号

```sql
SELECT user_id, 
  GROUP_CONCAT(order_no ORDER BY created_at SEPARATOR ', ') AS order_list
FROM `order`
GROUP BY user_id;
```

### 场景 4: 检查邮箱格式

```sql
SELECT * FROM user WHERE LOCATE('@', email) = 0;
```

### 场景 5: JSON 字符串提取（旧版本兼容）

```sql
-- 在 MySQL 5.7 之前，JSON 字段用字符串存储时的提取方式
SELECT 
  SUBSTRING_INDEX(SUBSTRING_INDEX(attrs, '"color":"', -1), '"', 2) AS color
FROM product;
```

## 注意事项

- `LENGTH()` 返回**字节数**而非字符数，对于多字节字符集（utf8mb4）一个中文字符占 3-4 字节
- `CHAR_LENGTH()` 返回**字符数**，处理中文时使用此函数
- `GROUP_CONCAT` 的结果长度受 `group_concat_max_len` 限制（默认 1024）
- MySQL 字符串索引默认从 **1** 开始（非 0）
