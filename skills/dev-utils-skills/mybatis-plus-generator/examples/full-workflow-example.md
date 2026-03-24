# 完整工作流程示例

## 场景

为一个用户管理系统生成完整的 MyBatis-Plus 代码，包括 user 表和 order 表，使用 MVC 架构，Java 语言。

## 工作流程

### Step 1: 收集配置信息

**用户输入：**

```
数据库信息：
- 数据库类型：MySQL
- 数据库名：teaching_ai
- 表名：user, order

全局配置：
- 作者：System
- 输出目录：src/main/java
- 文件覆盖策略：询问
- 启用 Lombok：是
- 启用 Swagger：是
- 启用验证注解：是

包配置：
- 父包名：com.example.app
- Entity 包：entity
- Mapper 包：mapper
- Service 包：service
- ServiceImpl 包：service.impl
- Controller 包：controller

策略配置：
- 命名策略：驼峰命名
- 表前缀：无
- 主键策略：AUTO
```

**输出：**

```
## 配置信息确认

✅ 数据库信息：
- 数据库类型：MySQL
- 数据库名：teaching_ai
- 表名：user, order

✅ 全局配置：
- 作者：System
- 输出目录：src/main/java
- 文件覆盖策略：询问
- 启用 Lombok：是
- 启用 Swagger：是
- 启用验证注解：是

✅ 包配置：
- 父包名：com.example.app
- Entity 包：com.example.app.entity
- Mapper 包：com.example.app.mapper
- Service 包：com.example.app.service
- ServiceImpl 包：com.example.app.service.impl
- Controller 包：com.example.app.controller

✅ 策略配置：
- 命名策略：驼峰命名
- 表前缀：无
- 主键策略：AUTO
```

### Step 2: 确定架构类型

**询问用户：**

```
请选择项目架构类型：
- [x] 传统 MVC (Model-View-Controller)
  - 生成：Entity, Mapper, Service, ServiceImpl, Controller
```

**用户确认：MVC 架构**

### Step 3: 收集功能需求

**询问用户：**

```
请描述此次生成代码的功能需求：

例如：
- 用户管理：需要根据邮箱查询用户、根据用户名查询用户、用户登录验证
- 订单管理：需要订单统计、订单分页查询、订单状态更新
```

**用户输入：**

```
用户管理功能需求：
1. 用户注册（创建用户）
2. 用户登录（根据用户名和密码查询）
3. 根据邮箱查询用户
4. 根据用户名查询用户
5. 更新用户信息
6. 删除用户
7. 用户列表查询（分页）

订单管理功能需求：
1. 创建订单
2. 根据订单ID查询订单
3. 根据用户ID查询订单列表
4. 订单统计（按用户统计订单数量和总金额）
5. 更新订单状态
6. 删除订单
7. 订单分页查询
```

**需求分析输出：**

```
## 需求分析结果

### user 表

标准方法：
- saveUser() - 保存用户
- findById() - 根据ID查询
- updateUser() - 更新用户
- deleteById() - 删除用户
- findAll() - 查询所有（分页）

自定义方法：
- findByEmail(String email) - 根据邮箱查询用户
- findByUsername(String username) - 根据用户名查询用户
- login(String username, String password) - 用户登录验证

### order 表

标准方法：
- saveOrder() - 保存订单
- findById() - 根据ID查询
- updateOrder() - 更新订单
- deleteById() - 删除订单
- findAll() - 查询所有（分页）

自定义方法：
- findByUserId(Long userId) - 根据用户ID查询订单列表
- getOrderStatistics(Long userId) - 订单统计（订单数量、总金额）
- updateOrderStatus(Long orderId, Integer status) - 更新订单状态
```

### Step 4: 确定编程语言

**询问用户：**

```
请选择编程语言：
- [x] Java
- [ ] Kotlin
```

**用户确认：Java**

### Step 5: 创建 Todo 清单

**生成的 Todo 清单：**

```markdown
## Todo List: MyBatis-Plus Code Generation

### Table: user

#### Entity 层
- [ ] User.java - 实体类
  - [ ] 类注释
  - [ ] 字段定义（id, username, email, password, status, createTime, updateTime）
  - [ ] 字段注释

#### Mapper 层
- [ ] UserMapper.java - 数据访问接口
  - [ ] 类注释
  - [ ] 基础 CRUD 方法（继承 BaseMapper）
  - [ ] 自定义查询方法（findByEmail, findByUsername）

#### Service 层
- [ ] UserService.java - 服务接口
  - [ ] 类注释
  - [ ] saveUser() - 保存用户
  - [ ] findById() - 根据ID查询
  - [ ] updateUser() - 更新用户
  - [ ] deleteById() - 删除用户
  - [ ] findByEmail() - 根据邮箱查询
  - [ ] findByUsername() - 根据用户名查询
  - [ ] login() - 用户登录验证

#### ServiceImpl 层
- [ ] UserServiceImpl.java - 服务实现类
  - [ ] 类注释
  - [ ] 实现所有 Service 接口方法
  - [ ] 方法注释和实现骨架

#### Controller 层
- [ ] UserController.java - 控制器
  - [ ] 类注释
  - [ ] createUser() - 创建用户
  - [ ] getUserById() - 查询用户
  - [ ] updateUser() - 更新用户
  - [ ] deleteUser() - 删除用户
  - [ ] getUserByEmail() - 根据邮箱查询
  - [ ] getUserByUsername() - 根据用户名查询
  - [ ] login() - 用户登录

### Table: order
- [ ] Order.java - 实体类
- [ ] OrderMapper.java - 数据访问接口
- [ ] OrderService.java - 服务接口
- [ ] OrderServiceImpl.java - 服务实现类
- [ ] OrderController.java - 控制器
```

### Step 6: 生成代码

**生成进度更新：**

```markdown
## 代码生成进度

### Table: user

✅ 已完成：
- [x] User.java - 实体类（包含 7 个字段，完整注释）
- [x] UserMapper.java - 数据访问接口（继承 BaseMapper，包含 2 个自定义方法）

🔄 进行中：
- [ ] UserService.java - 服务接口
  - [x] 类注释
  - [x] saveUser() 方法
  - [x] findById() 方法
  - [x] updateUser() 方法
  - [x] deleteById() 方法
  - [ ] findByEmail() 方法
  - [ ] findByUsername() 方法
  - [ ] login() 方法

⏳ 待生成：
- [ ] UserServiceImpl.java - 服务实现类
- [ ] UserController.java - 控制器

### Table: order
...
```

**生成的代码示例：**

#### User.java (Entity)

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
 *   <li>id: 用户主键，自增</li>
 *   <li>username: 用户名，唯一，用于登录</li>
 *   <li>email: 邮箱地址，唯一，用于登录和找回密码</li>
 *   <li>password: 加密后的密码</li>
 *   <li>status: 用户状态（0-禁用，1-启用）</li>
 * </ul>
 * </p>
 * 
 * @author System
 * @since 1.0.0
 */
@Data
@TableName("user")
public class User {
    
    /**
     * <p>用户主键 ID</p>
     * 
     * <p>数据库自增主键，唯一标识一个用户</p>
     */
    @TableId(type = IdType.AUTO)
    private Long id;
    
    /**
     * <p>用户名</p>
     * 
     * <p>用户登录时使用的用户名，必须唯一，长度限制为 50 个字符</p>
     */
    @TableField("username")
    private String username;
    
    /**
     * <p>邮箱地址</p>
     * 
     * <p>用户的邮箱地址，用于登录和找回密码，必须唯一，长度限制为 100 个字符</p>
     */
    @TableField("email")
    private String email;
    
    /**
     * <p>密码</p>
     * 
     * <p>用户密码，存储时已加密（BCrypt），长度限制为 255 个字符</p>
     */
    @TableField("password")
    private String password;
    
    /**
     * <p>用户状态</p>
     * 
     * <p>用户状态标识：
     * <ul>
     *   <li>0: 禁用</li>
     *   <li>1: 启用</li>
     * </ul>
     * </p>
     */
    @TableField("status")
    private Integer status;
    
    /**
     * <p>创建时间</p>
     * 
     * <p>用户记录的创建时间，由数据库自动设置</p>
     */
    @TableField(value = "create_time", fill = FieldFill.INSERT)
    private LocalDateTime createTime;
    
    /**
     * <p>更新时间</p>
     * 
     * <p>用户记录的最后更新时间，由数据库自动维护</p>
     */
    @TableField(value = "update_time", fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime updateTime;
}
```

#### UserService.java (Service Interface)

```java
package com.example.app.service;

import com.example.app.entity.User;
import com.baomidou.mybatisplus.extension.service.IService;

/**
 * <p>用户服务接口</p>
 * 
 * <p>定义用户相关的业务逻辑接口，包括用户的增删改查操作。
 * 本接口遵循领域驱动设计（DDD）原则，封装用户领域的核心业务逻辑。</p>
 * 
 * <p>主要职责：
 * <ul>
 *   <li>用户创建和注册</li>
 *   <li>用户信息查询（包括按邮箱、用户名查询）</li>
 *   <li>用户登录验证</li>
 *   <li>用户信息更新</li>
 *   <li>用户删除</li>
 * </ul>
 * </p>
 * 
 * @author System
 * @since 1.0.0
 */
public interface UserService extends IService<User> {
    
    /**
     * <p>根据邮箱查询用户</p>
     * 
     * <p>根据用户邮箱地址查询用户信息，用于用户登录和邮箱验证场景。
     * 如果用户不存在，返回 null。</p>
     * 
     * @param email java.lang.String 用户邮箱地址，不能为空
     * @return com.example.app.entity.User 用户实体对象，如果不存在则返回 null
     * @exception java.lang.IllegalArgumentException 当邮箱地址为空时抛出
     */
    User findByEmail(String email);
    
    /**
     * <p>根据用户名查询用户</p>
     * 
     * <p>根据用户名查询用户信息，用于用户登录场景。
     * 如果用户不存在，返回 null。</p>
     * 
     * @param username java.lang.String 用户名，不能为空
     * @return com.example.app.entity.User 用户实体对象，如果不存在则返回 null
     * @exception java.lang.IllegalArgumentException 当用户名为空时抛出
     */
    User findByUsername(String username);
    
    /**
     * <p>用户登录验证</p>
     * 
     * <p>根据用户名和密码验证用户身份，用于用户登录场景。
     * 验证过程包括：查询用户、验证密码、检查用户状态。</p>
     * 
     * @param username java.lang.String 用户名，不能为空
     * @param password java.lang.String 密码（明文），不能为空
     * @return com.example.app.entity.User 用户实体对象，如果验证失败则返回 null
     * @exception java.lang.IllegalArgumentException 当用户名或密码为空时抛出
     */
    User login(String username, String password);
}
```

### Step 7: 进度更新

**实时进度输出：**

```
✅ 已完成 user 表的 Entity 生成
✅ 已完成 user 表的 Mapper 生成
🔄 正在生成 user 表的 Service 接口...
✅ 已完成 user 表的 Service 接口生成
🔄 正在生成 user 表的 ServiceImpl 实现类...
✅ 已完成 user 表的 ServiceImpl 实现类生成
🔄 正在生成 user 表的 Controller 生成...
✅ 已完成 user 表的 Controller 生成

✅ 已完成 order 表的 Entity 生成
...
```

### Step 8: 统计信息

**最终统计输出：**

```markdown
## 代码生成统计

### 总体统计
- **生成表数量**: 2 张表（user, order）
- **生成对象总数**: 10 个对象
- **生成方法总数**: 35 个方法
- **生成文件总数**: 10 个文件
- **代码总行数**: 约 1,800 行

### 按表统计

#### user 表
- Entity: 1 个（7 个字段）
- Mapper: 1 个（继承 BaseMapper，2 个自定义方法）
- Service: 1 个（7 个方法：4 个标准方法 + 3 个自定义方法）
- ServiceImpl: 1 个（7 个方法实现）
- Controller: 1 个（7 个接口）
- **小计**: 5 个对象，16 个方法

#### order 表
- Entity: 1 个（10 个字段）
- Mapper: 1 个（继承 BaseMapper，2 个自定义方法）
- Service: 1 个（8 个方法：4 个标准方法 + 4 个自定义方法）
- ServiceImpl: 1 个（8 个方法实现）
- Controller: 1 个（8 个接口）
- **小计**: 5 个对象，19 个方法

### 文件位置
所有文件已生成到以下目录：
- Entity: `src/main/java/com/example/app/entity/`
- Mapper: `src/main/java/com/example/app/mapper/`
- Service: `src/main/java/com/example/app/service/`
- ServiceImpl: `src/main/java/com/example/app/service/impl/`
- Controller: `src/main/java/com/example/app/controller/`

### 代码质量
- ✅ 所有类都有完整的 JavaDoc 注释
- ✅ 所有方法都有参数和返回值说明
- ✅ 所有字段都有业务含义注释
- ✅ 自定义方法都有业务逻辑说明
- ✅ 符合 Java 编程规范
- ✅ 包含 Lombok 注解
- ✅ 包含 Swagger 注解
```
