# MVC 架构代码生成示例

## 场景

为 user 表生成 MVC 架构的完整代码，包括 Entity、Mapper、Service、ServiceImpl、Controller。

## 配置信息

```
数据库信息：
- 数据库类型：MySQL
- 表名：user

全局配置：
- 作者：System
- 启用 Lombok：是
- 启用 Swagger：是

包配置：
- 父包名：com.example.app
- Entity 包：entity
- Mapper 包：mapper
- Service 包：service
- ServiceImpl 包：service.impl
- Controller 包：controller

架构类型：MVC
编程语言：Java
```

## 表结构

```sql
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '用户主键ID',
  `username` varchar(50) NOT NULL COMMENT '用户名',
  `email` varchar(100) NOT NULL COMMENT '邮箱地址',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `status` int(11) NOT NULL DEFAULT '1' COMMENT '用户状态：0-禁用，1-启用',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`),
  UNIQUE KEY `uk_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

## 功能需求

```
用户管理功能：
1. 用户注册（创建用户）
2. 根据ID查询用户
3. 根据邮箱查询用户
4. 根据用户名查询用户
5. 更新用户信息
6. 删除用户
```

## 生成的代码

### 1. User.java (Entity)

```java
package com.example.app.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;
import java.time.LocalDateTime;

/**
 * <p>用户实体类</p>
 * 
 * <p>对应数据库中的 user 表，用于存储用户的基本信息。
 * 本实体类使用 MyBatis-Plus 注解进行 ORM 映射，支持自动建表和字段映射。</p>
 * 
 * <p>主要字段：
 * <ul>
 *   <li>id: 用户主键ID</li>
 *   <li>username: 用户名</li>
 *   <li>email: 邮箱地址</li>
 *   <li>password: 密码</li>
 *   <li>status: 用户状态：0-禁用，1-启用</li>
 * </ul>
 * </p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Data
@TableName("user")
public class User {
    
    @TableId(type = IdType.AUTO)
    private Long id;
    
    @TableField("username")
    private String username;
    
    @TableField("email")
    private String email;
    
    @TableField("password")
    private String password;
    
    @TableField("status")
    private Integer status;
    
    @TableField(value = "create_time", fill = FieldFill.INSERT)
    private LocalDateTime createTime;
    
    @TableField(value = "update_time", fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
}
```

### 2. UserMapper.java (Mapper)

```java
package com.example.app.mapper;

import com.example.app.entity.User;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;

/**
 * <p>用户数据访问接口</p>
 * 
 * <p>对应数据库中的 user 表，提供用户相关的数据访问操作。
 * 本接口使用 MyBatis-Plus 框架，继承 BaseMapper 提供基础的 CRUD 操作。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Mapper
public interface UserMapper extends BaseMapper<User> {
    
    /**
     * <p>根据邮箱查询用户</p>
     * 
     * @param email java.lang.String 用户邮箱地址
     * @return com.example.app.entity.User 用户实体对象
     */
    User findByEmail(String email);
    
    /**
     * <p>根据用户名查询用户</p>
     * 
     * @param username java.lang.String 用户名
     * @return com.example.app.entity.User 用户实体对象
     */
    User findByUsername(String username);
}
```

### 3. UserService.java (Service)

```java
package com.example.app.service;

import com.example.app.entity.User;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * <p>用户服务接口</p>
 * 
 * <p>定义用户相关的业务逻辑接口，包括用户的增删改查操作。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
public interface UserService extends IService<User> {
    
    /**
     * <p>根据邮箱查询用户</p>
     * 
     * @param email java.lang.String 用户邮箱地址
     * @return com.example.app.entity.User 用户实体对象
     */
    User findByEmail(String email);
    
    /**
     * <p>根据用户名查询用户</p>
     * 
     * @param username java.lang.String 用户名
     * @return com.example.app.entity.User 用户实体对象
     */
    User findByUsername(String username);
}
```

### 4. UserServiceImpl.java (ServiceImpl)

```java
package com.example.app.service.impl;

import com.example.app.entity.User;
import com.example.app.mapper.UserMapper;
import com.example.app.service.UserService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>用户服务实现类</p>
 * 
 * <p>实现 UserService 接口，提供用户相关的业务逻辑实现。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {
    
    @Override
    public User findByEmail(String email) {
        // TODO: 实现根据邮箱查询用户的业务逻辑
        if (email == null || email.isEmpty()) {
            throw new IllegalArgumentException("邮箱地址不能为空");
        }
        return baseMapper.findByEmail(email);
    }
    
    @Override
    public User findByUsername(String username) {
        // TODO: 实现根据用户名查询用户的业务逻辑
        if (username == null || username.isEmpty()) {
            throw new IllegalArgumentException("用户名不能为空");
        }
        return baseMapper.findByUsername(username);
    }
}
```

### 5. UserController.java (Controller)

```java
package com.example.app.controller;

import com.example.app.entity.User;
import com.example.app.service.UserService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * <p>用户控制器</p>
 * 
 * <p>提供用户相关的 REST API 接口。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Api(value = "用户管理", tags = "用户管理接口")
@RestController
@RequestMapping("/user")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @ApiOperation(value = "创建用户", notes = "创建新的用户记录")
    @PostMapping
    public User create(@RequestBody User user) {
        return userService.save(user) ? user : null;
    }
    
    @ApiOperation(value = "根据ID查询用户", notes = "根据ID查询用户详细信息")
    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getById(id);
    }
    
    @ApiOperation(value = "根据邮箱查询用户", notes = "根据邮箱查询用户信息")
    @GetMapping("/email/{email}")
    public User getByEmail(@PathVariable String email) {
        return userService.findByEmail(email);
    }
    
    @ApiOperation(value = "根据用户名查询用户", notes = "根据用户名查询用户信息")
    @GetMapping("/username/{username}")
    public User getByUsername(@PathVariable String username) {
        return userService.findByUsername(username);
    }
    
    @ApiOperation(value = "更新用户", notes = "更新用户信息")
    @PutMapping("/{id}")
    public User update(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        return userService.updateById(user) ? user : null;
    }
    
    @ApiOperation(value = "删除用户", notes = "根据ID删除用户")
    @DeleteMapping("/{id}")
    public boolean delete(@PathVariable Long id) {
        return userService.removeById(id);
    }
}
```

## 生成统计

```
生成对象总数：5 个
生成方法总数：12 个
生成文件总数：5 个
代码总行数：约 350 行
```
