# Entity 代码注释示例

## 场景

为 JPA Entity 类添加完整的 JavaDoc 注释。

## 原始代码

```java
package com.example.entity;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "users")
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "username", nullable = false, unique = true, length = 50)
    private String username;
    
    @Column(name = "email", nullable = false, unique = true, length = 100)
    private String email;
    
    @Column(name = "password", nullable = false, length = 255)
    private String password;
    
    @Column(name = "nickname", length = 50)
    private String nickname;
    
    @Column(name = "status", nullable = false)
    private Integer status;
    
    @Column(name = "create_time", nullable = false)
    private LocalDateTime createTime;
    
    @Column(name = "update_time")
    private LocalDateTime updateTime;
    
    // getters and setters
}
```

## 添加注释后的代码

```java
package com.example.entity;

import javax.persistence.*;
import java.time.LocalDateTime;

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
    
    // getters and setters
}
```

## 注释要点

1. **类注释**：
   - 说明实体类对应的数据库表
   - 说明使用的 ORM 框架
   - 列出主要字段及其用途

2. **字段注释**：
   - 清晰描述字段的含义
   - 说明字段的约束（唯一性、长度、是否可空等）
   - 对于枚举类型字段，列出所有可能的值
   - 说明字段的数据类型和格式
