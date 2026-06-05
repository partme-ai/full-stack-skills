# 递归 CTE 示例

## 场景 1：组织架构树

查询从根节点到所有子节点的完整部门树。

```sql
-- 建表
CREATE TABLE departments (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    parent_id   INTEGER REFERENCES departments(id)
);

-- 插入层级数据
INSERT INTO departments (id, name, parent_id) VALUES
    (1, '总公司', NULL),
    (2, '技术部', 1),
    (3, '市场部', 1),
    (4, '后端组', 2),
    (5, '前端组', 2),
    (6, '数据组', 2),
    (7, '广告组', 3),
    (8, 'PR 组', 3);

-- 递归 CTE: 展开整个树
WITH RECURSIVE org_tree AS (
    -- 基础: 根节点
    SELECT id, name, parent_id, 1 AS level, ARRAY[id] AS path
    FROM departments
    WHERE parent_id IS NULL

    UNION ALL

    -- 递归: 子节点
    SELECT d.id, d.name, d.parent_id, t.level + 1, t.path || d.id
    FROM departments d
    JOIN org_tree t ON d.parent_id = t.id
)
SELECT id, name, level, repeat('  ', level - 1) || name AS tree_display
FROM org_tree ORDER BY path;
```

## 场景 2：商品分类全路径

将树形分类扁平化并显示完整路径。

```sql
-- 建表
CREATE TABLE categories (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    parent_id   INTEGER REFERENCES categories(id)
);

INSERT INTO categories (id, name, parent_id) VALUES
    (1, '电子产品', NULL),
    (2, '手机', 1),
    (3, '电脑', 1),
    (4, '智能手机', 2),
    (5, '功能机', 2),
    (6, '笔记本', 3),
    (7, '台式机', 3);

-- 从指定节点开始，查询所有子分类及其全路径
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id, name AS full_path
    FROM categories WHERE id = 1  -- 从 "电子产品" 开始

    UNION ALL

    SELECT c.id, c.name, c.parent_id,
           ct.full_path || ' > ' || c.name
    FROM categories c
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY full_path;
```

## 场景 3：斐波那契数列

```sql
WITH RECURSIVE fib(a, b) AS (
    SELECT 0::BIGINT, 1::BIGINT
    UNION ALL
    SELECT b, a + b FROM fib WHERE b < 1000
)
SELECT a FROM fib;
```

## 场景 4：销售统计占比

使用非递归 CTE 计算每个分类的销售额占比。

```sql
WITH category_sales AS (
    SELECT c.name AS category, SUM(oi.quantity * oi.price) AS total
    FROM order_items oi
    JOIN products p ON p.id = oi.product_id
    JOIN categories c ON c.id = p.category_id
    GROUP BY c.name
),
grand_total AS (
    SELECT SUM(total) AS total FROM category_sales
)
SELECT cs.category, cs.total,
       ROUND(cs.total / gt.total * 100, 2) AS pct
FROM category_sales cs, grand_total gt
ORDER BY cs.total DESC;
```
