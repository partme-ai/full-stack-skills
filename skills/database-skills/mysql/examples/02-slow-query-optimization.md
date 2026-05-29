# 示例: 慢查询优化实战

## 场景

电商系统中查询"最近一个月下单超过 5 次的 VIP 用户及其总消费金额"的报表越来越慢。

## 原始查询

```sql
SELECT 
  u.id, u.name, u.email,
  COUNT(o.id) AS order_count,
  SUM(o.amount) AS total_amount
FROM user u
LEFT JOIN `order` o ON u.id = o.user_id
WHERE u.level = 'vip' 
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
GROUP BY u.id, u.name, u.email
HAVING order_count > 5
ORDER BY total_amount DESC
LIMIT 100;
```

执行时间：**12.3s**（`EXPLAIN` 显示全表扫 user 和 order）

## 分析过程

### Step 1: EXPLAIN 分析

```sql
EXPLAIN FORMAT=JSON
SELECT 
  u.id, u.name, u.email,
  COUNT(o.id) AS order_count,
  SUM(o.amount) AS total_amount
FROM user u
LEFT JOIN `order` o ON u.id = o.user_id
WHERE u.level = 'vip' 
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
GROUP BY u.id, u.name, u.email
HAVING order_count > 5
ORDER BY total_amount DESC
LIMIT 100;
```

**发现的问题**：
1. `u.level` 没有索引 → type: ALL，全表扫描 50 万用户
2. `o.created_at` 没有索引 → type: ALL，全表扫描 500 万订单
3. `GROUP BY` 和 `ORDER BY` 没有索引覆盖 → Using temporary; Using filesort

### Step 2: 添加索引

```sql
-- 1. user 表的 level 查询索引
ALTER TABLE user ADD INDEX idx_level (level);

-- 2. order 表的复合索引（user_id 用于 JOIN，created_at 用于时间过滤）
ALTER TABLE `order` ADD INDEX idx_user_created (user_id, created_at);

-- 3. 覆盖索引（减少回表）
ALTER TABLE `order` ADD INDEX idx_user_created_amount (user_id, created_at, amount);
```

### Step 3: 优化后 EXPLAIN

- `user` 表：type: ref（`idx_level`），rows: 5000（从 50 万降到 5000）
- `order` 表：type: ref（`idx_user_created`），rows: 每用户约 10 行
- Extra: 不再有 Using temporary; Using filesort

## 优化后结果

```sql
-- 优化后查询
SELECT 
  u.id, u.name, u.email,
  COUNT(o.id) AS order_count,
  SUM(o.amount) AS total_amount
FROM user u
INNER JOIN `order` o ON u.id = o.user_id
WHERE u.level = 'vip' 
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
GROUP BY u.id
HAVING order_count > 5
ORDER BY total_amount DESC
LIMIT 100;
```

执行时间：**12.3s → 0.08s**（提升约 150 倍）

## 优化要点总结

| 优化项 | 优化前 | 优化后 | 效果 |
|--------|--------|--------|------|
| `level` 索引 | ALL（50万行） | ref（5000行） | 减少 99% 扫描 |
| `(user_id, created_at)` 复合索引 | ALL（500万行） | ref（平均10行/用户） | 减少 99.99% |
| `LEFT JOIN` 改为 `INNER JOIN` | 含无订单用户 | 仅含订单用户 | 减少数据处理量 |
| `GROUP BY u.id`（简化列） | 3 列分组 | 1 列分组（id 唯一） | 减少临时表开销 |
| 数据范围 | 全表扫描 | 索引范围扫描 | 大幅提高 |
