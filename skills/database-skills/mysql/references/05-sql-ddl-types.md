# DDL 与数据类型详解

## 简介

DDL（Data Definition Language）用于定义和管理数据库对象（库、表、索引、约束等）。正确选择数据类型和约束对性能和数据完整性至关重要。

## 数据库操作

```sql
-- 创建数据库
CREATE DATABASE IF NOT EXISTS shop
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

-- 修改数据库
ALTER DATABASE shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 删除数据库
DROP DATABASE IF EXISTS shop;

-- 查看数据库列表
SHOW DATABASES;

-- 切换数据库
USE shop;

-- 查看当前数据库
SELECT DATABASE();
```

### 字符集选择建议

| 字符集 | 说明 | 推荐度 |
|--------|------|--------|
| `utf8mb4` | 支持 4 字节 emoji，推荐 | ★★★★★ |
| `utf8mb3` (utf8) | 不支持 emoji，已过时 | ★☆☆☆☆ |
| `utf8mb4_unicode_ci` | Unicode 通用排序 | ★★★★★ |
| `utf8mb4_general_ci` | 较宽松排序，稍快但不准确 | ★★★☆☆ |
| `utf8mb4_bin` | 二进制比较，区分大小写 | ★★★☆☆ |
| `utf8mb4_0900_ai_ci` | MySQL 8.0 默认，基于 UCA 9.0.0 | ★★★★★ |

**原则**：生产环境统一使用 `utf8mb4` + `utf8mb4_unicode_ci`，避免字符集混用导致乱码和索引失效。

## 数据类型

### 整数类型

| 类型 | 存储 | 有符号范围 | 无符号范围 | 推荐用途 |
|------|------|-----------|-----------|---------|
| `TINYINT` | 1B | -128 ~ 127 | 0 ~ 255 | 状态/性别/年龄 |
| `SMALLINT` | 2B | -32,768 ~ 32,767 | 0 ~ 65,535 | 库存/排名 |
| `MEDIUMINT` | 3B | -8,388,608 ~ 8,388,607 | 0 ~ 16,777,215 | 中型计数器 |
| `INT` | 4B | -2,147,483,648 ~ 2,147,483,647 | 0 ~ 4,294,967,295 | 常用主键 |
| `BIGINT` | 8B | -2^63 ~ 2^63-1 | 0 ~ 2^64-1 | 雪花ID/流水号 |

**主键建议**：预期行数超过 40 亿时用 `BIGINT`，否则用 `INT`。MySQL 8.0.17+ 不推荐 `UNSIGNED`，建议用 `CHECK` 约束代替。

```sql
-- ❌ 旧做法
age TINYINT UNSIGNED NOT NULL

-- ✅ MySQL 8.0.17+ 推荐
age TINYINT NOT NULL CHECK (age >= 0)
```

### 浮点数与定点数

| 类型 | 存储 | 精度 | 用途 |
|------|------|------|------|
| `FLOAT` | 4B | 约 7 位 | 科学计算（不用于金额） |
| `DOUBLE` | 8B | 约 15 位 | 科学计算 |
| `DECIMAL(M,D)` | M+2B 变长 | 精确 | **金额必选** |

```sql
-- 金额字段
price DECIMAL(10, 2) NOT NULL DEFAULT 0.00  -- 最大 99999999.99
rate  DECIMAL(5, 4)                          -- 利率 0.0001 ~ 9.9999
```

### 字符串类型

| 类型 | 最大长度 | 存储 | 用途 |
|------|---------|------|------|
| `CHAR(N)` | 255 | 定长，不足补空格 | 固定长度：手机号(11)、编码 |
| `VARCHAR(N)` | 65535 | 变长+1-2B前缀 | 用户名、邮箱、标题 |
| `TINYTEXT` | 255B | 行外 | 短备注 |
| `TEXT` | 64KB | 行外 | 文章内容、评论 |
| `MEDIUMTEXT` | 16MB | 行外 | 日志、长文本 |
| `LONGTEXT` | 4GB | 行外 | 大文档 |

**VARCHAR 长度选择**：
- `VARCHAR(255)` 和 `VARCHAR(50)` 在行内存储消耗相同（只看实际长度）
- 但临时表排序时按定义长度分配内存，不宜无意义设大
- 合理范围：50-200

**TEXT 注意事项**：
- TEXT 列不能有 DEFAULT 值
- TEXT 列不能用于内存临时表（ORDER BY 含 TEXT 会使用磁盘临时表）
- TEXT 列的索引必须指定前缀长度：`CREATE INDEX idx_content ON article (content(100));`

### 枚举类型

| 类型 | 存储 | 说明 |
|------|------|------|
| `ENUM('v1','v2',...)` | 1-2B | 单选枚举，内部按整数存储 |
| `SET('v1','v2',...)` | 1-8B | 多选位图 |

**ENUM 注意事项**：
- 修改 ENUM 定义需全表重建（ALTER TABLE MODIFY）
- 内部按索引排序（定义顺序），非字母序
- 推荐用 `TINYINT` + 代码映射，更灵活且迁移友好

```sql
-- 推荐做法
status TINYINT NOT NULL DEFAULT 0 COMMENT '0:pending 1:paid 2:shipped'

-- 不推荐
status ENUM('pending', 'paid', 'shipped') NOT NULL DEFAULT 'pending'
```

### JSON 类型 (MySQL 5.7+)

```sql
-- 建表使用 JSON
attrs JSON DEFAULT NULL COMMENT '商品扩展属性'

-- 插入 JSON 数据
INSERT INTO product VALUES (1, '手机', '{"color": "black", "specs": {"ram": "8GB"}}');

-- 查询 JSON 值
SELECT attrs->>'$.color' AS color FROM product;
```

详情参见 references/04-functions-json.md。

### 空间数据类型

| 类型 | 说明 | 业务场景 |
|------|------|---------|
| `POINT` | 点（经纬度） | 位置坐标 |
| `LINESTRING` | 线 | 路线 |
| `POLYGON` | 多边形 | 区域 |

```sql
-- 创建空间表
CREATE TABLE location (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  coord POINT NOT NULL SRID 4326  -- WGS84 坐标系
);

-- 插入空间数据
INSERT INTO location VALUES (1, '北京天安门', ST_GeomFromText('POINT(116.397 39.908)', 4326));

-- 查询距离（米）
SELECT name, ST_Distance_Sphere(coord, ST_GeomFromText('POINT(116.4 39.9)', 4326)) AS distance_m
FROM location;

-- 空间索引
ALTER TABLE location ADD SPATIAL INDEX idx_coord (coord);
```

## 约束 (Constraints)

| 约束 | 说明 | 注意 |
|------|------|------|
| `PRIMARY KEY` | 唯一标识每行，自动非空 | 建议 BIGINT AUTO_INCREMENT 或有序 UUID |
| `UNIQUE` | 唯一值，允许多个 NULL | 联合唯一: `UNIQUE KEY uk_c1_c2 (c1, c2)` |
| `FOREIGN KEY` | 引用完整性、级联操作 | InnoDB 专用，影响写入性能 |
| `CHECK` | 值范围检查 | 8.0.16+ 才实际执行 |
| `NOT NULL` | 不允许 NULL | 能用就用，提高查询效率 |
| `DEFAULT` | 默认值 | 8.0.13+ 支持表达式 |
| `AUTO_INCREMENT` | 自增序列 | 仅整数主键 |

### 完整建表示例

```sql
CREATE TABLE IF NOT EXISTS `order` (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '订单ID',
  order_no    VARCHAR(32) NOT NULL COMMENT '订单号',
  user_id     INT UNSIGNED NOT NULL COMMENT '用户ID',
  amount      DECIMAL(10, 2) NOT NULL DEFAULT 0.00 COMMENT '金额',
  status      TINYINT NOT NULL DEFAULT 0 COMMENT '状态:0待支付1已支付2已取消',
  quantity    INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '数量',
  email       VARCHAR(100) DEFAULT NULL COMMENT '通知邮箱',
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  deleted_at  DATETIME DEFAULT NULL COMMENT '软删除时间',
  
  PRIMARY KEY (id),
  UNIQUE KEY uk_order_no (order_no),
  KEY idx_user_id (user_id),
  KEY idx_status_created (status, created_at),
  KEY idx_deleted_at (deleted_at),
  CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
  CONSTRAINT chk_amount CHECK (amount >= 0),
  CONSTRAINT chk_status CHECK (status IN (0, 1, 2))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='订单表';
```

## ALTER TABLE — 表结构变更

```sql
-- 添加列
ALTER TABLE user ADD COLUMN avatar VARCHAR(500) DEFAULT NULL AFTER nickname;

-- 修改列类型
ALTER TABLE user MODIFY COLUMN email VARCHAR(200) NOT NULL;

-- 重命名列
ALTER TABLE user CHANGE COLUMN email new_email VARCHAR(200) NOT NULL;

-- 重命名表
RENAME TABLE old_name TO new_name;

-- 添加索引
ALTER TABLE user ADD INDEX idx_email (email);
ALTER TABLE user ADD UNIQUE KEY uk_email (email);

-- 删除索引
ALTER TABLE user DROP INDEX idx_email;

-- 在线 DDL (MySQL 5.6+)
ALTER TABLE user ADD COLUMN age INT, ALGORITHM=INPLACE, LOCK=NONE;
```

**生产环境大表改结构**使用 `pt-online-schema-change`(Percona Toolkit) 或 `gh-ost`，避免锁表。

## DROP / TRUNCATE / DELETE 对比

| 操作 | 速度 | 可回滚 | 重置自增值 | 触发 ON DELETE | 释放空间 |
|------|------|--------|-----------|---------------|---------|
| `DELETE` | 慢（逐行） | ✅ | ❌ | ✅ | 不释放 |
| `TRUNCATE` | 快（DROP+CREATE） | ❌ | ✅ | ❌ | 释放 |
| `DROP` | 快 | ❌ | N/A | ❌ | 全部释放 |
