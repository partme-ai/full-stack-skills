# JSON 函数 (JSON Functions, MySQL 5.7+)

## 简介

MySQL 5.7+ 原生支持 JSON 数据类型和一系列 JSON 操作函数。JSON 类型比字符串存储更高效（自动校验格式、内部二进制存储），支持通过虚拟列建立索引。

## 函数速查

### 查询与提取

| 函数 | 说明 | 版本 | 示例 |
|------|------|------|------|
| `JSON_EXTRACT(doc, path)` | 提取 JSON 值 | 5.7+ | `JSON_EXTRACT(attrs, '$.color')` |
| `col->'$.path'` | JSON_EXTRACT 简写 | 5.7+ | `attrs->'$.color'` |
| `col->>'$.path'` | 去引号版 | 8.0+ | `attrs->>'$.color'` |
| `JSON_CONTAINS(doc, val, path)` | 是否包含指定值 | 5.7+ | `JSON_CONTAINS(attrs, '"red"', '$.color')` |
| `JSON_CONTAINS_PATH(doc, one_or_all, path...)` | 路径是否存在 | 5.7+ | `JSON_CONTAINS_PATH(attrs, 'one', '$.color')` |
| `JSON_KEYS(doc, path)` | 返回所有键 | 5.7+ | `JSON_KEYS(attrs)` |
| `JSON_LENGTH(doc, path)` | 数组/对象长度 | 5.7+ | `JSON_LENGTH(attrs, '$.tags')` |
| `JSON_DEPTH(doc)` | JSON 文档深度 | 5.7+ | `JSON_DEPTH(attrs)` |
| `JSON_VALID(doc)` | 验证 JSON 合法性 | 5.7+ | `JSON_VALID('{"a":1}')` |
| `JSON_SEARCH(doc, one_or_all, str)` | 搜索值路径 | 5.7+ | `JSON_SEARCH(attrs, 'one', 'red')` |
| `JSON_TABLE(doc, path COLUMNS(...))` | JSON 转行（表函数） | 8.0+ | 见下 |

### JSON 路径语法

| 路径表达式 | 说明 |
|-----------|------|
| `$` | 根节点 |
| `$.key` | 对象键 |
| `$.nested.key` | 嵌套键 |
| `$[0]` | 数组第一个元素 |
| `$[*]` | 所有数组元素 |
| `$.key[*].sub` | 数组中所有元素的子键 |

### 构造与修改

| 函数 | 说明 | 示例 |
|------|------|------|
| `JSON_OBJECT(k, v, ...)` | 构造 JSON 对象 | `JSON_OBJECT('id', 1, 'name', 'test')` |
| `JSON_ARRAY(v1, v2, ...)` | 构造 JSON 数组 | `JSON_ARRAY(1, 2, 3)` |
| `JSON_QUOTE(str)` | 字符串转 JSON 值 | `JSON_QUOTE('hello "world"')` |
| `JSON_UNQUOTE(val)` | 去除 JSON 引号 | `JSON_UNQUOTE('"hello"')` |
| `JSON_SET(doc, path, val)` | 设置/覆盖值 | `JSON_SET(attrs, '$.price', 5999)` |
| `JSON_INSERT(doc, path, val)` | 插入（不覆盖已有） | `JSON_INSERT(attrs, '$.discount', 0.8)` |
| `JSON_REPLACE(doc, path, val)` | 替换（仅在路径存在时） | `JSON_REPLACE(attrs, '$.price', 4999)` |
| `JSON_REMOVE(doc, path)` | 删除键 | `JSON_REMOVE(attrs, '$.discount')` |
| `JSON_ARRAY_APPEND(doc, path, val)` | 数组追加 | `JSON_ARRAY_APPEND(attrs, '$.tags', 'sale')` |
| `JSON_ARRAY_INSERT(doc, path, val)` | 数组插入 | `JSON_ARRAY_INSERT(attrs, '$.tags[0]', 'hot')` |
| `JSON_MERGE_PATCH(doc, patch)` | 合并（覆盖式） | `JSON_MERGE_PATCH(attrs, '{"color":"blue"}')` |
| `JSON_MERGE_PRESERVE(doc, patch)` | 合并（保留式） | `JSON_MERGE_PRESERVE(attrs, '{"color":"blue"}')` |

### 聚合函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `JSON_ARRAYAGG(col)` | 列转 JSON 数组 | `JSON_ARRAYAGG(product_name)` |
| `JSON_OBJECTAGG(k, v)` | 列转 JSON 对象 | `JSON_OBJECTAGG(id, name)` |

## 业务场景

### 场景 1: 从商品 JSON 字段提取属性

```sql
SELECT id, name, 
  attrs->>'$.color' AS color,
  attrs->'$.specs' AS specs
FROM product;
```

### 场景 2: 更新嵌套 JSON 字段

```sql
UPDATE product 
SET attrs = JSON_SET(attrs, '$.specs.storage', '256GB', '$.price', 5999) 
WHERE id = 1;
```

### 场景 3: 记录操作日志（JSON 动态字段）

```sql
INSERT INTO audit_log (action, detail) VALUES ('update_product',
  JSON_OBJECT(
    'product_id', 1, 
    'old_price', 99, 
    'new_price', 129, 
    'operator', 'admin',
    'timestamp', NOW()
  ));
```

### 场景 4: JSON_TABLE 展开为关系表 (MySQL 8.0+)

```sql
SELECT jt.*
FROM product,
JSON_TABLE(attrs, '$' COLUMNS (
  color VARCHAR(20) PATH '$.color',
  ram VARCHAR(10) PATH '$.specs.ram',
  storage VARCHAR(10) PATH '$.specs.storage'
)) AS jt
WHERE color = 'black';
```

### 场景 5: 通过虚拟列建立 JSON 索引

MySQL 不支持直接对 JSON 列建索引。通过虚拟列 + 普通索引实现：

```sql
-- 添加虚拟列
ALTER TABLE product ADD COLUMN color_virtual VARCHAR(20) 
  GENERATED ALWAYS AS (attrs->>'$.color');

-- 为虚拟列建索引
CREATE INDEX idx_product_color ON product(color_virtual);

-- 查询自动使用索引
SELECT * FROM product WHERE color_virtual = 'red';
```

## 注意事项

- JSON 列不存储重复键（保留最后一个值）
- JSON 列自动格式校验，非法格式会报错
- JSON 的二进制格式（BSON）允许快速键值查找，无需解析全文
- JSON 列不能有 DEFAULT 值（MySQL 限制）
- JSON 列不能直接索引，必须通过虚拟列间接索引
- 在 WHERE 中直接使用 `attrs->>'$.key'` 不会使用索引，需走虚拟列
- MySQL 8.0.13+ 支持 `JSON_TYPE()` 等更多 JSON 工具函数
