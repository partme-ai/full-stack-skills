# Swagger 2 vs OpenAPI 3 注解示例

## 场景

展示同一个 Entity 和 Controller 在使用 Swagger 2 和 OpenAPI 3 注解时的区别。

## Entity 示例

### Swagger 2 注解

```java
package com.example.app.entity;

import com.baomidou.mybatisplus.annotation.*;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import java.time.LocalDateTime;

/**
 * <p>用户实体类</p>
 * 
 * <p>对应数据库中的 user 表，用于存储用户的基本信息。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Data
@TableName("user")
@ApiModel(value = "用户对象", description = "用户实体类")
public class User {
    
    /**
     * <p>用户主键 ID</p>
     */
    @TableId(type = IdType.AUTO)
    @ApiModelProperty(value = "用户主键ID")
    private Long id;
    
    /**
     * <p>用户名</p>
     */
    @TableField("username")
    @ApiModelProperty(value = "用户名", required = true)
    private String username;
    
    /**
     * <p>邮箱地址</p>
     */
    @TableField("email")
    @ApiModelProperty(value = "邮箱地址", required = true)
    private String email;
}
```

### OpenAPI 3 注解

```java
package com.example.app.entity;

import com.baomidou.mybatisplus.annotation.*;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import java.time.LocalDateTime;

/**
 * <p>用户实体类</p>
 * 
 * <p>对应数据库中的 user 表，用于存储用户的基本信息。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Data
@TableName("user")
@Schema(description = "用户实体类")
public class User {
    
    /**
     * <p>用户主键 ID</p>
     */
    @TableId(type = IdType.AUTO)
    @Schema(description = "用户主键ID")
    private Long id;
    
    /**
     * <p>用户名</p>
     */
    @TableField("username")
    @Schema(description = "用户名", required = true)
    private String username;
    
    /**
     * <p>邮箱地址</p>
     */
    @TableField("email")
    @Schema(description = "邮箱地址", required = true)
    private String email;
}
```

## Controller 示例

### Swagger 2 注解

```java
package com.example.app.controller;

import com.example.app.entity.User;
import com.example.app.service.UserService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
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
    
    /**
     * <p>创建用户</p>
     * 
     * @param user 用户实体对象
     * @return 用户实体对象
     */
    @ApiOperation(value = "创建用户", notes = "创建新的用户记录")
    @PostMapping
    public User create(@RequestBody User user) {
        return userService.save(user);
    }
    
    /**
     * <p>根据ID查询用户</p>
     * 
     * @param id 用户唯一标识符
     * @return 用户实体对象
     */
    @ApiOperation(value = "根据ID查询用户", notes = "根据ID查询用户详细信息")
    @ApiParam(name = "id", value = "用户ID", required = true)
    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getById(id);
    }
}
```

### OpenAPI 3 注解

```java
package com.example.app.controller;

import com.example.app.entity.User;
import com.example.app.service.UserService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
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
@Tag(name = "用户管理", description = "用户管理接口")
@RestController
@RequestMapping("/user")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    /**
     * <p>创建用户</p>
     * 
     * @param user 用户实体对象
     * @return 用户实体对象
     */
    @Operation(summary = "创建用户", description = "创建新的用户记录")
    @PostMapping
    public User create(@RequestBody User user) {
        return userService.save(user);
    }
    
    /**
     * <p>根据ID查询用户</p>
     * 
     * @param id 用户唯一标识符
     * @return 用户实体对象
     */
    @Operation(summary = "根据ID查询用户", description = "根据ID查询用户详细信息")
    @Parameter(name = "id", description = "用户ID", required = true)
    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getById(id);
    }
}
```

## DTO 示例

### Swagger 2 注解

```java
package com.example.app.dto;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import javax.validation.constraints.*;

/**
 * <p>用户创建DTO</p>
 * 
 * <p>用于用户注册的数据传输对象。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Data
@ApiModel(value = "用户创建DTO", description = "用户创建数据传输对象")
public class UserCreateDTO {
    
    @ApiModelProperty(value = "用户名", required = true)
    @NotBlank(message = "用户名不能为空")
    @Size(max = 50, message = "用户名长度不能超过50个字符")
    private String username;
    
    @ApiModelProperty(value = "邮箱地址", required = true)
    @NotBlank(message = "邮箱地址不能为空")
    @Email(message = "邮箱格式不正确")
    private String email;
}
```

### OpenAPI 3 注解

```java
package com.example.app.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import javax.validation.constraints.*;

/**
 * <p>用户创建DTO</p>
 * 
 * <p>用于用户注册的数据传输对象。</p>
 * 
 * @author System
 * @since 2024-12-19
 */
@Data
@Schema(description = "用户创建数据传输对象")
public class UserCreateDTO {
    
    @Schema(description = "用户名", required = true)
    @NotBlank(message = "用户名不能为空")
    @Size(max = 50, message = "用户名长度不能超过50个字符")
    private String username;
    
    @Schema(description = "邮箱地址", required = true)
    @NotBlank(message = "邮箱地址不能为空")
    @Email(message = "邮箱格式不正确")
    private String email;
}
```

## 主要区别总结

### 1. 导入包

**Swagger 2:**
```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
```

**OpenAPI 3:**
```java
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.tags.Tag;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
```

### 2. 注解名称

| Swagger 2 | OpenAPI 3 |
|:---|:---|
| `@ApiModel` | `@Schema` |
| `@ApiModelProperty` | `@Schema` |
| `@Api` | `@Tag` |
| `@ApiOperation` | `@Operation` |
| `@ApiParam` | `@Parameter` |

### 3. 注解属性

| Swagger 2 | OpenAPI 3 |
|:---|:---|
| `value = "..."` | `description = "..."` |
| `notes = "..."` | `description = "..."` |
| `tags = "..."` | `name = "..."` |

## 选择建议

- **Spring Boot 2.x (2.0-2.6)**: 推荐使用 Swagger 2
- **Spring Boot 2.2+ 或 3.x**: 推荐使用 OpenAPI 3
- **新项目**: 推荐使用 OpenAPI 3（符合最新规范）
