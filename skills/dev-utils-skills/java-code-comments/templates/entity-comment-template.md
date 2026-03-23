# Entity 类注释模板

## 类注释模板

```java
/**
 * [实体名称]实体类
 * 
 * <p>对应数据库中的 [表名] 表，用于存储[实体描述]。
 * 本实体类使用 [ORM框架] 注解进行 ORM 映射，支持自动建表和字段映射。
 * 
 * <p>主要字段：
 * <ul>
 *   <li>[字段1]: [说明]</li>
 *   <li>[字段2]: [说明]</li>
 *   <li>[字段3]: [说明]</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
@Entity
@Table(name = "[表名]")
public class [EntityName] {
}
```

## 字段注释模板

### 主键字段

```java
/**
 * [实体名称]主键 ID
 * 
 * <p>数据库自增主键，唯一标识一个[实体名称]
 */
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
```

### 普通字段

```java
/**
 * [字段描述]
 * 
 * <p>[详细说明，包括约束、格式、用途等]
 */
@Column(name = "[列名]", nullable = [true/false], unique = [true/false], length = [长度])
private [FieldType] [fieldName];
```

### 枚举字段

```java
/**
 * [字段描述]
 * 
 * <p>[字段描述]标识：
 * <ul>
 *   <li>[值1]: [说明]</li>
 *   <li>[值2]: [说明]</li>
 *   <li>[值3]: [说明]</li>
 * </ul>
 */
@Column(name = "[列名]", nullable = false)
private [EnumType] [fieldName];
```

### 时间字段

```java
/**
 * [时间字段描述]
 * 
 * <p>[实体名称]记录的[创建/更新]时间，由数据库自动[设置/维护]
 */
@Column(name = "[列名]", nullable = [true/false])
private LocalDateTime [fieldName];
```

### 关联字段

```java
/**
 * [关联实体名称]
 * 
 * <p>与[关联实体名称]的[关联类型]关系，使用[关联方式]进行关联
 */
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "[外键列名]")
private [RelatedEntity] [fieldName];
```

## 使用示例

### 完整示例

```java
/**
 * 用户实体类
 * 
 * <p>对应数据库中的 users 表，用于存储用户的基本信息。
 * 本实体类使用 JPA 注解进行 ORM 映射，支持自动建表和字段映射。
 * 
 * <p>主要字段：
 * <ul>
 *   <li>id: 用户主键，自增</li>
 *   <li>username: 用户名，唯一，用于登录</li>
 *   <li>email: 邮箱地址，唯一，用于登录和找回密码</li>
 *   <li>password: 加密后的密码</li>
 *   <li>status: 用户状态（0-禁用，1-启用）</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@Entity
@Table(name = "users")
public class User {
    
    /**
     * 用户主键 ID
     * 
     * <p>数据库自增主键，唯一标识一个用户
     */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    /**
     * 用户名
     * 
     * <p>用户登录时使用的用户名，必须唯一，长度限制为 50 个字符
     */
    @Column(name = "username", nullable = false, unique = true, length = 50)
    private String username;
    
    /**
     * 邮箱地址
     * 
     * <p>用户的邮箱地址，用于登录和找回密码，必须唯一，长度限制为 100 个字符
     */
    @Column(name = "email", nullable = false, unique = true, length = 100)
    private String email;
    
    /**
     * 密码
     * 
     * <p>用户密码，存储时已加密（BCrypt），长度限制为 255 个字符
     */
    @Column(name = "password", nullable = false, length = 255)
    private String password;
    
    /**
     * 昵称
     * 
     * <p>用户显示昵称，可选字段，长度限制为 50 个字符
     */
    @Column(name = "nickname", length = 50)
    private String nickname;
    
    /**
     * 用户状态
     * 
     * <p>用户状态标识：
     * <ul>
     *   <li>0: 禁用</li>
     *   <li>1: 启用</li>
     * </ul>
     */
    @Column(name = "status", nullable = false)
    private Integer status;
    
    /**
     * 创建时间
     * 
     * <p>用户记录的创建时间，由数据库自动设置
     */
    @Column(name = "create_time", nullable = false)
    private LocalDateTime createTime;
    
    /**
     * 更新时间
     * 
     * <p>用户记录的最后更新时间，由数据库自动维护
     */
    @Column(name = "update_time")
    private LocalDateTime updateTime;
}
```

## 注释要点

1. **类注释**：
   - 说明对应的数据库表
   - 说明使用的 ORM 框架
   - 列出主要字段及其用途

2. **字段注释**：
   - 清晰描述字段的含义
   - 说明字段的约束（唯一性、长度、是否可空等）
   - 对于枚举类型字段，列出所有可能的值
   - 说明字段的数据类型和格式
   - 对于关联字段，说明关联关系类型
