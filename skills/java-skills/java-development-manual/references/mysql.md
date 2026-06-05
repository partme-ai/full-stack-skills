# MySQL数据库规约

## 目录
- [一、建表规约](#一建表规约)
- [二、索引规约](#二索引规约)
- [三、SQL语句](#三sql语句)
- [四、ORM映射](#四orm映射)

---

## 一、建表规约

### 【强制】规约

1. **布尔字段命名**：`is_xxx`，类型`unsigned tinyint`（1表示是，0表示否）

2. **表名/字段名规范**：
   - 必须使用小写字母或数字
   - 禁止数字开头
   - 正例：`aliyun_admin` / `rdc_config` / `level3_name`

3. **表名不使用复数名词**

4. **禁用保留字**：`desc` / `range` / `match` / `delayed`等

5. **索引命名规范**：
   - 主键索引：`pk_字段名`
   - 唯一索引：`uk_字段名`
   - 普通索引：`idx_字段名`

6. **小数类型用decimal**，禁止使用float和double

7. **字符串长度几乎相等时用char定长**

8. **varchar长度不超过5000**，超过则用text独立建表

9. **表必备三字段**：
   ```sql
   CREATE TABLE example (
       `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
       `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
       `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
       PRIMARY KEY (`id`)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='示例表';
   ```

### 【推荐】规约

1. **表命名**：`业务名称_表的作用`
2. **库名与应用名称一致**
3. **分库分表时机**：单表超过500万行或2GB

### 存储长度参考

| 对象 | 范围 | 类型 | 字节 |
|------|------|------|------|
| 年龄 | 150岁内 | tinyint unsigned | 1 |
| 数百岁 | smallint unsigned | 2 |
| 数千万年 | int unsigned | 4 |
| 约50亿年 | bigint unsigned | 8 |

---

## 二、索引规约

### 【强制】规约

1. **唯一特性字段必须建唯一索引**

2. **超过3个表禁止join**

3. **varchar字段索引必须指定长度**：
   ```sql
   CREATE INDEX idx_name ON user(name(20));
   ```

4. **页面搜索严禁左模糊或全模糊**

### 【推荐】规约

1. **利用索引有序性**：
   ```sql
   -- 索引：idx_a_b_c
   SELECT * FROM table WHERE a=? AND b=? ORDER BY c;
   ```

2. **利用覆盖索引**避免回表

3. **延迟关联优化超多分页**：
   ```sql
   SELECT t1.*
   FROM user t1,
        (SELECT id FROM user WHERE condition LIMIT 100000, 20) t2
   WHERE t1.id = t2.id;
   ```

4. **SQL性能目标**：至少range级别，要求ref，最好是consts

5. **组合索引区分度最高的在最左边**

---

## 三、SQL语句

### 【强制】规约

1. **统计行数用count(*)**：
   ```sql
   -- 正例
   SELECT count(*) FROM user;
   ```

2. **sum()注意NPE**：
   ```sql
   SELECT IFNULL(SUM(amount), 0) FROM orders;
   ```

3. **判NULL用ISNULL()**

4. **分页count为0直接返回**

5. **禁止使用外键与级联**

6. **禁止使用存储过程**

7. **数据订正先select确认**

8. **多表查询字段加别名限定**：
   ```sql
   SELECT t1.name FROM user AS t1, order AS t2 WHERE t1.id = t2.user_id;
   ```

### 【推荐】规约

1. **表别名用as**，按t1、t2、t3命名
2. **in操作控制在1000个之内**
3. **字符集用utf8mb4**

---

## 四、ORM映射

### 【强制】规约

1. **禁止SELECT \***：
   ```xml
   <select id="listUsers">
       SELECT id, username, email FROM user
   </select>
   ```

2. **参数使用#{}**：
   ```xml
   <!-- 正例：防SQL注入 -->
   <select id="getById">SELECT * FROM user WHERE id = #{id}</select>
   ```

3. **必须定义resultMap**

4. **更新时必须更新update_time**

### 【推荐】规约

**不写大而全的更新接口**：
```xml
<update id="updateUserSelective">
    UPDATE user
    <set>
        <if test="name != null">name = #{name},</if>
        <if test="email != null">email = #{email},</if>
    </set>
    WHERE id = #{id}
</update>
```
