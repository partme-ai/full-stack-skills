# DDD 架构代码生成示例

## 场景

为 user 表生成 DDD（领域驱动设计）架构的完整代码，包括 Entity、Mapper、Service、ServiceImpl、Controller、DTO、VO、BO。

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
- Entity 包：domain.entity
- Mapper 包：infrastructure.mapper
- Service 包：domain.service
- ServiceImpl 包：application.service.impl
- Controller 包：interfaces.controller
- DTO 包：interfaces.dto
- VO 包：interfaces.vo
- BO 包：domain.bo

架构类型：DDD
编程语言：Java
```

## 功能需求

```
用户管理功能：
1. 用户注册（创建用户，需要 DTO）
2. 根据ID查询用户（返回 VO）
3. 根据邮箱查询用户
4. 用户信息更新（需要 DTO）
5. 删除用户
6. 用户列表查询（分页，返回 VO 列表）
```

## 生成的代码结构

### DDD 分层结构

```
com.example.app/
├── domain/                    # 领域层
│   ├── entity/               # 实体
│   │   └── User.java
│   ├── bo/                   # 业务对象
│   │   └── UserBO.java
│   └── service/              # 领域服务接口
│       └── UserService.java
├── application/              # 应用层
│   └── service/
│       └── impl/
│           └── UserServiceImpl.java
├── infrastructure/           # 基础设施层
│   └── mapper/
│       └── UserMapper.java
└── interfaces/               # 接口层
    ├── controller/
    │   └── UserController.java
    ├── dto/
    │   ├── UserCreateDTO.java
    │   └── UserUpdateDTO.java
    └── vo/
        └── UserVO.java
```

## 生成的代码示例

### 1. UserCreateDTO.java

```java
package com.example.app.interfaces.dto;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import javax.validation.constraints.*;

/**
 * <p>用户创建DTO</p>
 * 
 * <p>用于用户注册的数据传输对象。
 * 本DTO包含用户注册所需的字段，用于用户注册场景。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@ApiModel(value = "用户创建DTO", description = "用户注册数据传输对象")
@Data
public class UserCreateDTO implements Serializable {
    
    @ApiModelProperty(value = "用户名", required = true)
    @NotBlank(message = "用户名不能为空")
    @Size(max = 50, message = "用户名长度不能超过50个字符")
    private String username;
    
    @ApiModelProperty(value = "邮箱地址", required = true)
    @NotBlank(message = "邮箱地址不能为空")
    @Email(message = "邮箱格式不正确")
    @Size(max = 100, message = "邮箱长度不能超过100个字符")
    private String email;
    
    @ApiModelProperty(value = "密码", required = true)
    @NotBlank(message = "密码不能为空")
    @Size(min = 8, max = 255, message = "密码长度必须在8-255个字符之间")
    private String password;
}
```

### 2. UserVO.java

```java
package com.example.app.interfaces.vo;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import java.time.LocalDateTime;

/**
 * <p>用户视图对象</p>
 * 
 * <p>用于用户的视图展示，包含用户的展示字段。
 * 本VO用于API响应，不包含敏感信息（如密码）。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@ApiModel(value = "用户VO", description = "用户视图对象")
@Data
public class UserVO implements Serializable {
    
    @ApiModelProperty(value = "用户ID")
    private Long id;
    
    @ApiModelProperty(value = "用户名")
    private String username;
    
    @ApiModelProperty(value = "邮箱地址")
    private String email;
    
    @ApiModelProperty(value = "用户状态：0-禁用，1-启用")
    private Integer status;
    
    @ApiModelProperty(value = "创建时间")
    private LocalDateTime createTime;
    
    @ApiModelProperty(value = "更新时间")
    private LocalDateTime updateTime;
}
```

### 3. UserBO.java

```java
package com.example.app.domain.bo;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * <p>用户业务对象</p>
 * 
 * <p>封装用户的业务逻辑对象，包含业务规则和业务方法。
 * 本BO用于业务层处理，包含业务逻辑和业务规则验证。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@ApiModel(value = "用户BO", description = "用户业务对象")
@Data
public class UserBO implements Serializable {
    
    @ApiModelProperty(value = "用户ID")
    private Long id;
    
    @ApiModelProperty(value = "用户名")
    private String username;
    
    @ApiModelProperty(value = "邮箱地址")
    private String email;
    
    @ApiModelProperty(value = "用户状态")
    private Integer status;
    
    /**
     * <p>验证用户状态是否可用</p>
     * 
     * @return boolean 用户是否可用
     */
    public boolean isActive() {
        return status != null && status == 1;
    }
}
```

### 4. UserController.java (DDD 版本)

```java
package com.example.app.interfaces.controller;

import com.example.app.interfaces.dto.UserCreateDTO;
import com.example.app.interfaces.dto.UserUpdateDTO;
import com.example.app.interfaces.vo.UserVO;
import com.example.app.application.service.impl.UserServiceImpl;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * <p>用户控制器</p>
 * 
 * <p>提供用户相关的 REST API 接口，遵循 DDD 架构设计。
 * 本控制器位于接口层，负责接收请求和返回响应。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Api(value = "用户管理", tags = "用户管理接口")
@RestController
@RequestMapping("/user")
public class UserController {
    
    @Autowired
    private UserServiceImpl userService;
    
    @ApiOperation(value = "创建用户", notes = "用户注册")
    @PostMapping
    public UserVO create(@RequestBody UserCreateDTO dto) {
        // TODO: 调用应用层服务，将 DTO 转换为实体，返回 VO
        return null;
    }
    
    @ApiOperation(value = "根据ID查询用户", notes = "查询用户详细信息")
    @GetMapping("/{id}")
    public UserVO getById(@PathVariable Long id) {
        // TODO: 调用应用层服务，返回 VO
        return null;
    }
    
    @ApiOperation(value = "更新用户", notes = "更新用户信息")
    @PutMapping("/{id}")
    public UserVO update(@PathVariable Long id, @RequestBody UserUpdateDTO dto) {
        // TODO: 调用应用层服务，更新用户信息，返回 VO
        return null;
    }
    
    @ApiOperation(value = "删除用户", notes = "根据ID删除用户")
    @DeleteMapping("/{id}")
    public boolean delete(@PathVariable Long id) {
        // TODO: 调用应用层服务，删除用户
        return false;
    }
}
```

## DDD 架构特点

### 1. 分层清晰

- **领域层（Domain）**：包含实体、业务对象、领域服务接口
- **应用层（Application）**：包含服务实现，协调领域层和基础设施层
- **基础设施层（Infrastructure）**：包含数据访问（Mapper）
- **接口层（Interfaces）**：包含控制器、DTO、VO

### 2. 对象职责明确

- **Entity**：领域实体，包含业务属性和业务方法
- **BO**：业务对象，封装业务逻辑
- **DTO**：数据传输对象，用于接口输入
- **VO**：视图对象，用于接口输出

### 3. 依赖方向

- 接口层 → 应用层 → 领域层
- 基础设施层 → 领域层
- 遵循依赖倒置原则

## 生成统计

```
生成对象总数：8 个
生成方法总数：15 个
生成文件总数：8 个
代码总行数：约 600 行
```
