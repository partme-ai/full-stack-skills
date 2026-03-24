# Mapper 类注释模板

## 类注释模板

```java
/**
 * [实体名称]数据访问接口
 * 
 * <p>对应数据库中的 [表名] 表，提供[实体名称]相关的数据访问操作。
 * 本接口使用 MyBatis-Plus 框架，继承 BaseMapper 提供基础的 CRUD 操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>基础的增删改查操作</li>
 *   <li>[自定义查询方法1]</li>
 *   <li>[自定义查询方法2]</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
@Mapper
public interface [Entity]Mapper extends BaseMapper<[Entity]> {
}
```

## 方法注释模板

### 基础 CRUD 方法（继承自 BaseMapper）

这些方法通常不需要额外注释，因为 BaseMapper 已经提供了标准实现。

### 自定义查询方法

```java
/**
 * 根据[条件]查询[实体名称]列表
 * 
 * <p>根据[条件描述]从数据库查询符合条件的[实体名称]列表。
 * 
 * @param [参数名] [参数说明]
 * @return [实体名称]列表，如果不存在则返回空列表
 */
List<[Entity]> selectBy[Condition]([ParamType] [paramName]);
```

### 自定义更新方法

```java
/**
 * 根据[条件]更新[实体名称]
 * 
 * <p>根据[条件描述]更新[实体名称]的指定字段。
 * 
 * @param [参数名] [参数说明]
 * @return 更新的记录数
 */
int updateBy[Condition]([ParamType] [paramName]);
```

### 自定义删除方法

```java
/**
 * 根据[条件]删除[实体名称]
 * 
 * <p>根据[条件描述]删除符合条件的[实体名称]记录。
 * 
 * @param [参数名] [参数说明]
 * @return 删除的记录数
 */
int deleteBy[Condition]([ParamType] [paramName]);
```

### 使用 @Select 注解的方法

```java
/**
 * 根据[条件]查询[实体名称]
 * 
 * <p>使用自定义 SQL 查询符合条件的[实体名称]。
 * 
 * @param [参数名] [参数说明]
 * @return [实体名称]信息，如果不存在则返回 null
 */
@Select("SELECT * FROM [表名] WHERE [条件] = #{[参数名]}")
[Entity] selectBy[Condition](@Param("[参数名]") [ParamType] [paramName]);
```

## 使用示例

### MyBatis-Plus Mapper 示例

```java
/**
 * 用户数据访问接口
 * 
 * <p>对应数据库中的 users 表，提供用户相关的数据访问操作。
 * 本接口使用 MyBatis-Plus 框架，继承 BaseMapper 提供基础的 CRUD 操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>基础的增删改查操作</li>
 *   <li>根据用户名查询用户</li>
 *   <li>根据邮箱查询用户</li>
 *   <li>检查用户名是否存在</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@Mapper
public interface UserMapper extends BaseMapper<User> {
    
    /**
     * 根据用户名查询用户
     * 
     * <p>根据用户名从数据库查询对应的用户信息。
     * 
     * @param username 用户名
     * @return 用户信息，如果不存在则返回 null
     */
    @Select("SELECT * FROM users WHERE username = #{username}")
    User selectByUsername(@Param("username") String username);
    
    /**
     * 根据邮箱查询用户
     * 
     * <p>根据邮箱地址从数据库查询对应的用户信息。
     * 
     * @param email 邮箱地址
     * @return 用户信息，如果不存在则返回 null
     */
    @Select("SELECT * FROM users WHERE email = #{email}")
    User selectByEmail(@Param("email") String email);
    
    /**
     * 检查用户名是否存在
     * 
     * <p>检查指定的用户名是否已经在数据库中存在。
     * 
     * @param username 用户名
     * @return 如果存在返回 true，否则返回 false
     */
    @Select("SELECT COUNT(*) > 0 FROM users WHERE username = #{username}")
    boolean existsByUsername(@Param("username") String username);
}
```

### MyBatis XML Mapper 示例

```java
/**
 * 订单数据访问接口
 * 
 * <p>对应数据库中的 orders 表，提供订单相关的数据访问操作。
 * 本接口使用 MyBatis 框架，SQL 语句定义在对应的 XML 映射文件中。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>基础的增删改查操作</li>
 *   <li>根据用户 ID 查询订单列表</li>
 *   <li>根据订单状态查询订单列表</li>
 *   <li>统计用户的订单数量</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@Mapper
public interface OrderMapper {
    
    /**
     * 根据用户 ID 查询订单列表
     * 
     * <p>根据用户 ID 从数据库查询该用户的所有订单信息。
     * 
     * @param userId 用户唯一标识符
     * @return 订单列表，如果不存在则返回空列表
     */
    List<Order> selectByUserId(Long userId);
    
    /**
     * 根据订单状态查询订单列表
     * 
     * <p>根据订单状态从数据库查询符合条件的订单列表。
     * 
     * @param status 订单状态（0-待支付，1-已支付，2-已取消）
     * @return 订单列表，如果不存在则返回空列表
     */
    List<Order> selectByStatus(Integer status);
    
    /**
     * 统计用户的订单数量
     * 
     * <p>统计指定用户的订单总数。
     * 
     * @param userId 用户唯一标识符
     * @return 订单数量
     */
    int countByUserId(Long userId);
}
```

## 注释要点

1. **类注释**：
   - 说明对应的数据库表
   - 说明使用的 ORM 框架（MyBatis 或 MyBatis-Plus）
   - 列出主要功能点

2. **方法注释**：
   - 清晰描述查询/更新/删除的目的
   - 详细说明所有参数
   - 说明返回值类型和含义
   - 对于自定义 SQL，可以说明 SQL 的作用

3. **参数注释**：
   - 使用 `@Param` 注解时，参数说明要清晰
   - 说明参数的数据类型和约束
