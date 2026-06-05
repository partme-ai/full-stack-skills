# 索引与执行计划 (Index & Query Optimization)

## 简介

索引是 MySQL 性能优化的核心手段。正确的索引能大幅减少扫描行数，错误的索引设计则会导致全表扫描和性能灾难。

## 索引类型

| 索引类型 | 底层结构 | 版本要求 | 适用场景 |
|---------|---------|---------|---------|
| **B-Tree** | B+ 树 | 全版本 | 等值/范围/排序查询（默认） |
| **Hash** | 哈希表 | MEMORY 引擎 | 等值查询（不支持范围） |
| **Fulltext** | 倒排索引 | 5.6+ | 全文搜索 (MATCH AGAINST) |
| **Spatial** | R-Tree | 5.7+ | 空间数据查询 |
| **Descending** | B+ 树降序 | 8.0+ | 混合排序方向优化 |
| **Invisible** | 同 B-Tree | 8.0+ | 测试删除影响而不实际删除 |
| **Functional Key Parts** | 表达式索引 | 8.0.13+ | 函数/表达式索引 |

### B-Tree 索引创建

```sql
-- 普通索引
CREATE INDEX idx_name ON user (name);

-- 唯一索引
CREATE UNIQUE INDEX uk_email ON user (email);

-- 复合索引（最左前缀原则）
CREATE INDEX idx_city_age ON user (city, age);

-- 前缀索引（字符串前 N 字符）
CREATE INDEX idx_email_prefix ON user (email(10));

-- 全文索引
CREATE FULLTEXT INDEX ftx_content ON article (title, content);

-- 降序索引 (MySQL 8.0+)
CREATE INDEX idx_created_desc ON `order` (created_at DESC);

-- 不可见索引（测试用）
CREATE INDEX idx_test ON user (name) INVISIBLE;
ALTER TABLE user ALTER INDEX idx_test VISIBLE;

-- 函数索引 (MySQL 8.0.13+)
CREATE INDEX idx_phone_last4 ON user ((RIGHT(phone, 4)));
```

## 复合索引最左前缀原则

复合索引 `idx_a_b_c (a, b, c)`：

| 查询条件 | 索引使用情况 |
|---------|-------------|
| `WHERE a = 1` | ✅ 使用 a |
| `WHERE a = 1 AND b = 2` | ✅ 使用 a, b |
| `WHERE a = 1 AND b = 2 AND c = 3` | ✅ 使用 a, b, c |
| `WHERE a = 1 ORDER BY b` | ✅ 使用 a（排序） |
| `WHERE a = 1 AND c = 3` | ✅ 使用 a（c 只能过滤） |
| `WHERE a IN (1, 2) AND b = 3` | ✅ 使用 a, b |
| `WHERE b = 2` | ❌ 跳过了 a |
| `WHERE c = 3` | ❌ 跳过了 a, b |

### 索引设计原则

1. **区分度高的列放前面**：选择性 = `COUNT(DISTINCT col) / COUNT(*)`
2. **等值条件列放前面**：`=` 比范围查询列放前面
3. **覆盖索引**：查询列全在索引中（Extra 显示 `Using index`），避免回表
4. **索引下推 (ICP)**：MySQL 5.6+，引擎层用 WHERE 条件过滤索引记录后再回表

## EXPLAIN 执行计划分析

### 使用 EXPLAIN

```sql
EXPLAIN SELECT u.name, o.order_no
FROM user u
JOIN `order` o ON u.id = o.user_id
WHERE u.id = 100;
```

### EXPLAIN 输出列

| 列名 | 含义 | 关键值 |
|------|------|--------|
| `id` | SELECT 标识符，id 越大越先执行 | |
| `select_type` | 查询类型 | SIMPLE, PRIMARY, SUBQUERY, DERIVED, UNION |
| `table` | 表名 | |
| `partitions` | 扫描的分区 | |
| `type` | 访问类型（性能排序） | system > const > eq_ref > ref > range > index > **ALL** |
| `possible_keys` | 可能使用的索引 | |
| `key` | 实际使用的索引 | |
| `key_len` | 使用的索引字节长度 | 越大越好（匹配更多列） |
| `ref` | 索引匹配的列或常量 | |
| `rows` | 预估扫描行数 | 越小越好 |
| `filtered` | 过滤后百分比 | |
| `Extra` | 额外信息 | **🔑 重要** |

### type 访问类型（从优到劣）

| type | 说明 | 示例 |
|------|------|------|
| **system** | 表只有一行 | 最好 |
| **const** | 主键/唯一索引等值查询 | `WHERE id = 1` |
| **eq_ref** | JOIN 主键/唯一索引关联 | `ON u.id = o.user_id` |
| **ref** | 普通索引等值查询 | `WHERE name = '张三'` |
| **range** | 索引范围扫描 | `WHERE id > 100`, `LIKE '张%'` |
| **index** | 全索引扫描 | 不推荐 |
| **ALL** | 全表扫描 | **❌ 最差** |

### Extra 关键信息

| Extra 值 | 含义 |
|----------|------|
| **Using index** | 覆盖索引（无需回表）✅ 最佳 |
| **Using where** | 用 WHERE 过滤 |
| **Using index condition** | 索引下推 ICP ✅ |
| **Using temporary** | 使用临时表（需优化）❌ |
| **Using filesort** | 文件排序（需优化）❌ |
| **Using join buffer** | JOIN 未用索引 ❌ |
| **Using MRR** | 多范围读取优化 ✅ |

### EXPLAIN ANALYZE (MySQL 8.0.18+)

```sql
-- 实际执行并显示各步骤耗时和行数
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) AS order_count
FROM user u
LEFT JOIN `order` o ON u.id = o.user_id
GROUP BY u.id
ORDER BY order_count DESC
LIMIT 10;
```

## SQL 优化原则

```
★ 核心原则：减少扫描行数，减少回表，减少排序

1. WHERE 条件列建索引（符合最左前缀）
2. 避免 SELECT *，仅取需要的列（利用覆盖索引）
3. 用 EXISTS 代替 IN（大数据量下）
4. 用 UNION ALL 代替 UNION（不需要去重时）
5. 用 LIMIT 限制结果集大小
6. 大表分页用游标（WHERE id > last_id）而非 OFFSET
7. JOIN 的关联列必须有索引
8. GROUP BY / ORDER BY 的列尽量利用索引
9. 避免在 WHERE 条件列上使用函数或计算
10. 拆分大查询为多次小查询（减少锁范围）
```

## 常见优化案例

### 隐式类型转换（索引失效）

```sql
-- ❌ phone 是 VARCHAR，传 INT 导致全表扫描
SELECT * FROM user WHERE phone = 13800138000;

-- ✅ 字符类型就传字符串
SELECT * FROM user WHERE phone = '13800138000';
```

### WHERE 条件函数操作（索引失效）

```sql
-- ❌ DATE() 函数使索引失效
SELECT * FROM `order` WHERE DATE(created_at) = '2024-01-01';

-- ✅ 范围查询可用索引
SELECT * FROM `order` WHERE created_at >= '2024-01-01' AND created_at < '2024-01-02';
```

### 大分页优化

```sql
-- ❌ OFFSET 越大越慢（先扫描再丢弃）
SELECT * FROM `order` ORDER BY id LIMIT 100000, 20;

-- ✅ 游标分页
SELECT * FROM `order` WHERE id > 100000 ORDER BY id LIMIT 20;

-- ✅ 子查询 + JOIN 方式
SELECT * FROM `order`
JOIN (SELECT id FROM `order` ORDER BY id LIMIT 100000, 20) AS tmp
ON `order`.id = tmp.id;
```

### OR 改为 UNION

```sql
-- ❌ OR 可能用不到复合索引
SELECT * FROM user WHERE name = '张三' OR email = 'zhangsan@example.com';

-- ✅ UNION 分别用各自索引
SELECT * FROM user WHERE name = '张三'
UNION
SELECT * FROM user WHERE email = 'zhangsan@example.com';
```

## 慢查询配置

```ini
# my.cnf
slow_query_log = ON                          # 开启慢查询
slow_query_log_file = /var/log/mysql/slow.log # 慢查询日志文件
long_query_time = 1                          # 超过 1 秒的查询记录
log_queries_not_using_indexes = ON           # 记录未使用索引的查询
min_examined_row_limit = 100                 # 扫描行数超过此值才记录
```

### 分析慢查询

```bash
# mysqldumpslow 排序取前10
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# Percona Toolkit 分析
pt-query-digest /var/log/mysql/slow.log
```

## 索引设计规范

1. 每个表必须有主键（推荐 BIGINT AUTO_INCREMENT 或有序 UUID）
2. 主键不宜过长（B+ 树二级索引过大）
3. 每个表索引数不超过 5-8 个（过多影响写入性能）
4. 大表（> 1000 万行）索引必须业务验证后创建
5. 字符串区分度低或长度大时用前缀索引
6. ORDER BY / GROUP BY / JOIN 的列考虑建索引
7. 不建索引的列：频繁更新、区分度极低（如性别）
8. 用 INVISIBLE 索引测试后再删除
9. 避免冗余索引（如 idx_a_b 和 idx_a 重复）
