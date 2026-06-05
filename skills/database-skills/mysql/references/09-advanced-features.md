# 高级特性 (Advanced Features)

## 简介

MySQL 提供视图、CTE、存储过程/函数、触发器、事务与锁、分区表等高级特性，用于满足复杂业务需求和性能优化。

## 视图 (View)

视图是存储的查询定义，不存储数据，使用时会展开为底层查询执行。

### 创建与使用

```sql
-- 创建视图
CREATE VIEW user_order_summary AS
SELECT u.id, u.name, COUNT(o.id) AS order_count, SUM(o.amount) AS total_amount
FROM user u
LEFT JOIN `order` o ON u.id = o.user_id
GROUP BY u.id;

-- 使用视图（像普通表一样查询）
SELECT * FROM user_order_summary WHERE order_count > 5;

-- 可更新视图（需满足条件）
UPDATE active_user SET email = 'new@example.com' WHERE id = 1;

-- 查看视图定义
SHOW CREATE VIEW user_order_summary;

-- 删除视图
DROP VIEW IF EXISTS user_order_summary;
```

### 视图限制

| 限制 | 说明 |
|------|------|
| 不可更新条件 | 含 DISTINCT、聚合、GROUP BY、HAVING、UNION 的视图不可更新 |
| 性能 | 与直接查询无异（视图不存储数据） |
| 算法 | `ALGORITHM = MERGE | TEMPTABLE | UNDEFINED` |

**业务场景**：封装复杂查询逻辑、简化报表查询、提供权限控制层。

## CTE (Common Table Expression, MySQL 8.0+)

CTE 提供临时结果集的命名引用，可读性更高，支持递归。

### 基础 CTE

```sql
WITH dept_avg AS (
  SELECT dept_id, AVG(salary) AS avg_salary
  FROM employee
  GROUP BY dept_id
)
SELECT e.name, e.salary, da.avg_salary
FROM employee e
JOIN dept_avg da ON e.dept_id = da.dept_id
WHERE e.salary > da.avg_salary;
```

### 递归 CTE — 树形结构查询

```sql
WITH RECURSIVE sub_depts AS (
  -- 基础节点（根部门）
  SELECT id, name, parent_id, 1 AS level
  FROM department
  WHERE parent_id IS NULL

  UNION ALL

  -- 递归子节点
  SELECT d.id, d.name, d.parent_id, sd.level + 1
  FROM department d
  JOIN sub_depts sd ON d.parent_id = sd.id
)
SELECT * FROM sub_depts ORDER BY level, id;
```

**业务场景**：
- 递归 CTE 查询组织树、分类树、评论树
- CTE 替代派生表，提高可读性并支持多次引用

## 存储过程与存储函数

### 存储过程

封装多条 SQL，支持事务控制、IN/OUT 参数、错误处理。

```sql
DELIMITER //
CREATE PROCEDURE transfer_funds(
  IN from_account INT,
  IN to_account INT,
  IN amount DECIMAL(10, 2),
  OUT result_code INT,
  OUT result_msg VARCHAR(200)
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    SET result_code = -1;
    SET result_msg = '转账失败，事务回滚';
  END;

  START TRANSACTION;
    UPDATE account SET balance = balance - amount 
    WHERE id = from_account AND balance >= amount;
    
    IF ROW_COUNT() = 0 THEN
      SET result_code = -2;
      SET result_msg = '余额不足';
      ROLLBACK;
    ELSE
      UPDATE account SET balance = balance + amount WHERE id = to_account;
      SET result_code = 0;
      SET result_msg = '转账成功';
      COMMIT;
    END IF;
END //
DELIMITER ;

-- 调用
CALL transfer_funds(1, 2, 100.00, @code, @msg);
SELECT @code, @msg;
```

### 存储函数

返回单值的函数，可在 SQL 中直接使用。

```sql
DELIMITER //
CREATE FUNCTION get_order_count(user_id INT) RETURNS INT
READS SQL DATA
BEGIN
  DECLARE cnt INT;
  SELECT COUNT(*) INTO cnt FROM `order` WHERE user_id = user_id;
  RETURN cnt;
END //
DELIMITER ;

-- 使用
SELECT name, get_order_count(id) AS order_count FROM user;
```

### 存储过程 vs 函数

| 特性 | 存储过程 | 存储函数 |
|------|---------|---------|
| 返回值 | 多个 OUT 参数 | 单个返回值 |
| 调用方式 | `CALL proc()` | `SELECT func()` 或 SQL 中直接使用 |
| 事务控制 | ✅ 支持 | ❌ 不支持 |
| SQL 中使用 | ❌ | ✅ |

**业务场景**：存储过程适合转账、库存核减等事务性操作。但现代应用主要在应用层（如 Spring/Go）实现业务逻辑。

## 触发器 (Trigger)

### 基本语法

```sql
-- CREATE TRIGGER trigger_name
-- {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
-- ON table_name FOR EACH ROW
-- trigger_body
```

### 常见用例

```sql
-- 1. 自动更新时间
CREATE TRIGGER before_user_update
BEFORE UPDATE ON user
FOR EACH ROW
SET NEW.updated_at = NOW();

-- 2. 审计日志
CREATE TRIGGER after_order_update
AFTER UPDATE ON `order`
FOR EACH ROW
INSERT INTO audit_log (table_name, action, old_data, new_data)
VALUES ('order', 'UPDATE',
  JSON_OBJECT('status', OLD.status, 'amount', OLD.amount),
  JSON_OBJECT('status', NEW.status, 'amount', NEW.amount));

-- 3. 防止重复签到
CREATE TRIGGER before_signin_insert
BEFORE INSERT ON signin
FOR EACH ROW
BEGIN
  DECLARE cnt INT;
  SELECT COUNT(*) INTO cnt FROM signin
  WHERE user_id = NEW.user_id AND DATE(created_at) = CURDATE();
  IF cnt > 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '今日已签到';
  END IF;
END;
```

### 触发器注意事项

| 问题 | 说明 |
|------|------|
| 隐性执行 | 排查问题困难（"魔法"行为） |
| 性能影响 | 过多触发器影响 DML 性能 |
| 错误回滚 | 触发器中的错误会回滚外层事务 |
| 嵌套复杂度 | 不建议在触发器中调用存储过程 |

**优先在应用层实现业务逻辑**，触发器仅用于审计、自动更新时间等必要场景。

## 事务与锁

### ACID 特性

| 特性 | 含义 | MySQL 实现 |
|------|------|-----------|
| 原子性 (A) | 事务全部成功或全部回滚 | undo log |
| 一致性 (C) | 事务前后数据一致 | 约束 + 事务 |
| 隔离性 (I) | 事务间互相隔离 | MVCC + 锁 |
| 持久性 (D) | 提交后数据持久保存 | redo log |

### 事务隔离级别

| 隔离级别 | 脏读 | 不可重复读 | 幻读 | 默认？ |
|---------|------|-----------|------|-------|
| READ UNCOMMITTED | ✅ 可能 | ✅ 可能 | ✅ 可能 | ❌ |
| READ COMMITTED | ❌ | ✅ 可能 | ✅ 可能 | ❌（多数公司用） |
| REPEATABLE READ | ❌ | ❌ | ✅ 可能 | ✅ MySQL 默认 |
| SERIALIZABLE | ❌ | ❌ | ❌ | ❌（性能差） |

### 事务使用

```sql
START TRANSACTION;
  UPDATE account SET balance = balance - 100 WHERE id = 1;
  UPDATE account SET balance = balance + 100 WHERE id = 2;
  -- 成功
  COMMIT;
  -- 或失败
  ROLLBACK;

-- 保存点
START TRANSACTION;
  INSERT INTO log VALUES ('step1');
  SAVEPOINT sp1;
  INSERT INTO log VALUES ('step2');  -- 出错
  ROLLBACK TO SAVEPOINT sp1;        -- 回退到 sp1
  INSERT INTO log VALUES ('step3');
COMMIT;
```

### 锁类型

| 锁类型 | 说明 | SQL |
|--------|------|-----|
| 共享锁 (S) | 允许其他事务读，禁止写 | `SELECT ... LOCK IN SHARE MODE` |
| 排他锁 (X) | 禁止其他事务读写 | `SELECT ... FOR UPDATE` |
| 表锁 (READ) | 其他会话可读不可写 | `LOCK TABLES user READ;` |
| 表锁 (WRITE) | 其他会话不可读写 | `LOCK TABLES user WRITE;` |
| 乐观锁 | 应用层版本号控制 | `UPDATE SET version+1 WHERE version=:old` |

### 死锁避免

1. **固定访问顺序**：所有事务按相同顺序访问表
2. **缩短事务时间**：不要在一个事务内执行大量无关操作
3. **降低隔离级别**：SERIALIZABLE → REPEATABLE READ → READ COMMITTED
4. **查看死锁**：`SHOW ENGINE INNODB STATUS;`

## 分区表 (Partitioning)

### 分区类型

| 分区类型 | 说明 | 典型场景 |
|---------|------|---------|
| RANGE | 按范围分区（最常用） | 时间范围：订单按年/月分区 |
| LIST | 按值列表分区 | 区域：按 region_id 分区 |
| HASH | 按哈希函数分区 | 均匀分布：按 id MOD N |
| KEY | 类似 HASH，MySQL 内部哈希 | 类似 HASH |

### RANGE 分区

```sql
CREATE TABLE orders_partitioned (
  id BIGINT NOT NULL,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2),
  created_at DATETIME NOT NULL
) PARTITION BY RANGE (YEAR(created_at)) (
  PARTITION p2022 VALUES LESS THAN (2023),
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION p2024 VALUES LESS THAN (2025),
  PARTITION p_future VALUES LESS THAN MAXVALUE
);

-- 添加分区
ALTER TABLE orders_partitioned ADD PARTITION (PARTITION p2025 VALUES LESS THAN (2026));

-- 删除分区（极快）
ALTER TABLE orders_partitioned DROP PARTITION p2022;
```

### LIST / HASH / KEY 分区

```sql
-- LIST 分区（按区域）
CREATE TABLE user_region (
  id INT NOT NULL, name VARCHAR(50), region_id INT NOT NULL
) PARTITION BY LIST (region_id) (
  PARTITION p_north VALUES IN (1, 2, 3),
  PARTITION p_south VALUES IN (4, 5, 6)
);

-- HASH 分区（按哈希）
CREATE TABLE logs (
  id INT NOT NULL, log_data TEXT, created_at DATETIME
) PARTITION BY HASH (id) PARTITIONS 8;

-- KEY 分区
CREATE TABLE sessions (
  id INT NOT NULL, session_data TEXT
) PARTITION BY KEY (id) PARTITIONS 4;
```

### 分区修剪 (Partition Pruning)

查询自动只扫描相关分区：

```sql
EXPLAIN SELECT * FROM orders_partitioned WHERE created_at >= '2024-01-01';
-- 只扫描 p2024, p_future

ALTER TABLE orders_partitioned TRUNCATE PARTITION p2022;  -- 快速清理历史数据
```

### 分区注意事项

| 注意点 | 说明 |
|--------|------|
| 分区列必须包含在主键中 | MySQL 硬限制 |
| 分区数建议 | ≤ 1024，单个分区 ≥ 10GB 时效果明显 |
| 不是越多越好 | 过多分区增加元数据开销 |
| 最大适用 | 数据归档场景（按时间删除旧分区极快） |
