# 字符串/正则函数详解

## 字符串函数

```sql
-- FORMAT — 格式化字符串
SELECT FORMAT('ORD-%s-%04d', TO_CHAR(NOW(), 'YYYYMMDD'), 123);
-- 结果: ORD-20240529-0123

-- SPLIT_PART — 分割字符串
SELECT SPLIT_PART('北京市海淀区中关村', '区', 1);
-- 结果: 北京市海淀

-- STRING_AGG — 字符串聚合（将分类名称合并为逗号分隔字符串）
SELECT STRING_AGG(DISTINCT c.name, ', ' ORDER BY c.name) AS categories
FROM products p
JOIN product_categories pc ON pc.product_id = p.id
JOIN categories c ON c.id = pc.category_id
WHERE p.id = 1001;

-- CONCAT / CONCAT_WS
SELECT CONCAT_WS(', ', province, city, district, detail) AS full_address FROM addresses;

-- LEFT / RIGHT
SELECT LEFT('Hello World', 5);   -- Hello
SELECT RIGHT('Hello World', 5);  -- World

-- REPEAT / REVERSE
SELECT REPEAT('*', 5);           -- *****
SELECT REVERSE('PostgreSQL');    -- LQSregtsoP

-- POSITION / STRPOS
SELECT POSITION('SQL' IN 'PostgreSQL');  -- 7
SELECT STRPOS('PostgreSQL', 'SQL');       -- 7

-- SUBSTRING (支持正则)
SELECT SUBSTRING('abc123def' FROM '[0-9]+');  -- 123

-- TRANSLATE
SELECT TRANSLATE('hello', 'aeiou', '12345');  -- h2ll4
```

## 正则函数

```sql
-- REGEXP_MATCH — 正则匹配（提取邮箱）
SELECT REGEXP_MATCH(
    '联系邮箱: alice@example.com, 备用: bob@test.com',
    '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'g'
);
-- 结果: {alice@example.com,bob@test.com}

-- REGEXP_REPLACE — 正则替换（脱敏手机号）
SELECT REGEXP_REPLACE('13812345678', '(\d{3})\d{4}(\d{4})', '\1****\2');
-- 结果: 138****5678
```

## PL/pgSQL 函数

```sql
-- 标量函数
CREATE OR REPLACE FUNCTION calculate_discount(
    price NUMERIC, discount_pct NUMERIC, max_discount NUMERIC DEFAULT 100
) RETURNS NUMERIC
LANGUAGE plpgsql IMMUTABLE
AS $$
BEGIN
    RETURN GREATEST(price * (1 - discount_pct / 100), price - max_discount);
END;
$$;

-- 表函数 (RETURNS TABLE)
CREATE OR REPLACE FUNCTION get_user_orders(
    p_user_id INTEGER, p_status TEXT DEFAULT NULL, p_limit INTEGER DEFAULT 100
) RETURNS TABLE (order_id BIGINT, total_amount NUMERIC(12,2), status TEXT, created_at TIMESTAMPTZ)
LANGUAGE plpgsql STABLE
AS $$
BEGIN
    RETURN QUERY
    SELECT o.id, o.total_amount, o.status, o.created_at
    FROM orders o
    WHERE o.user_id = p_user_id AND (p_status IS NULL OR o.status = p_status)
    ORDER BY o.created_at DESC LIMIT p_limit;
END;
$$;

-- 函数 (FUNCTION) vs 过程 (PROCEDURE)
-- FUNCTION: 必须返回值, SELECT 中调用
-- PROCEDURE (PG 11+): 无返回值, CALL 调用, 支持事务控制

-- 函数重载
CREATE OR REPLACE FUNCTION format_price(price NUMERIC) RETURNS TEXT
LANGUAGE SQL IMMUTABLE AS $$ SELECT '¥' || ROUND(price, 2)::TEXT; $$;

CREATE OR REPLACE FUNCTION format_price(price NUMERIC, currency TEXT) RETURNS TEXT
LANGUAGE SQL IMMUTABLE AS $$ SELECT currency || ROUND(price, 2)::TEXT; $$;

-- PL/pgSQL 控制结构
CREATE OR REPLACE FUNCTION process_order(p_order_id BIGINT) RETURNS TEXT
LANGUAGE plpgsql
AS $$
DECLARE
    v_order orders%ROWTYPE;
    v_log TEXT := '';
BEGIN
    SELECT * INTO STRICT v_order FROM orders WHERE id = p_order_id;

    IF v_order.status = 'pending' THEN
        v_log := '待处理';
    ELSIF v_order.status = 'paid' THEN
        v_log := '已支付';
    END IF;

    RETURN v_log;
EXCEPTION
    WHEN NO_DATA_FOUND THEN RETURN '订单不存在';
    WHEN OTHERS THEN RETURN '错误: ' || SQLERRM;
END;
$$;
```

## 触发器

```sql
-- 自动更新 updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column() RETURNS TRIGGER
LANGUAGE plpgsql AS $$ BEGIN NEW.updated_at = NOW(); RETURN NEW; END; $$;

CREATE TRIGGER trg_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW WHEN (OLD.* IS DISTINCT FROM NEW.*)
    EXECUTE FUNCTION update_updated_at_column();

-- 审计日志触发器
CREATE OR REPLACE FUNCTION audit_order_changes() RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO order_audit_log (order_id, new_data, action) VALUES (NEW.id, row_to_json(NEW)::JSONB, 'INSERT');
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO order_audit_log (order_id, old_data, new_data, action) VALUES (NEW.id, row_to_json(OLD)::JSONB, row_to_json(NEW)::JSONB, 'UPDATE');
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO order_audit_log (order_id, old_data, action) VALUES (OLD.id, row_to_json(OLD)::JSONB, 'DELETE');
    END IF;
    RETURN NEW;
END;
$$;

-- 事件触发器 (DDL)
CREATE OR REPLACE FUNCTION prevent_table_drop() RETURNS EVENT_TRIGGER
LANGUAGE plpgsql AS $$ BEGIN RAISE EXCEPTION '禁止删除表'; END; $$;
CREATE EVENT TRIGGER prevent_drop_trigger ON sql_drop EXECUTE FUNCTION prevent_table_drop();
```

## 数字函数

```sql
-- RANDOM — 随机抽样
SELECT * FROM users ORDER BY RANDOM() LIMIT 5;

-- GENERATE_SERIES — 生成序列
SELECT GENERATE_SERIES('2024-01-01'::DATE, '2024-01-10'::DATE, '1 day');
SELECT GENERATE_SERIES(1, 10, 2);  -- 1, 3, 5, 7, 9

-- WIDTH_BUCKET — 等宽分桶
SELECT WIDTH_BUCKET(age, 0, 100, 10) AS bucket, MIN(age), MAX(age), COUNT(*)
FROM users GROUP BY bucket ORDER BY bucket;

-- ROUND / TRUNC / CEIL / FLOOR / POWER / SQRT / ABS / DIV / MOD / GCD / LCM
SELECT ROUND(123.456, 2), TRUNC(123.456, 2), CEIL(123.001), FLOOR(123.999);
SELECT POWER(2,10), SQRT(144), ABS(-42), DIV(10,3), MOD(10,3), GCD(12,18), LCM(12,18);
```
