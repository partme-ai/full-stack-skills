# Swagger 2 vs OpenAPI 3 注解参考指南

## 概述

本文档说明 Swagger 2 和 OpenAPI 3 注解的区别和使用场景，帮助在代码生成时选择合适的注解类型。

## Swagger 2 vs OpenAPI 3 对比

### 版本说明

- **Swagger 2**：使用 `io.swagger.annotations.*` 包
- **OpenAPI 3**：使用 `io.swagger.v3.oas.annotations.*` 包

### 适用场景

#### Swagger 2
- **适用于**：Spring Boot 2.x 项目
- **依赖**：`springfox-swagger2`, `springfox-swagger-ui`
- **特点**：成熟稳定，广泛使用

#### OpenAPI 3
- **适用于**：Spring Boot 2.2+ 和 Spring Boot 3.x 项目
- **依赖**：`springdoc-openapi-ui`
- **特点**：符合 OpenAPI 3.0 规范，更好的 Spring Boot 3.x 支持

## 注解对比表

### 类级别注解

| 用途 | Swagger 2 | OpenAPI 3 |
|:---|:---|:---|
| 实体类/模型 | `@ApiModel(value = "...", description = "...")` | `@Schema(description = "...")` |
| 控制器 | `@Api(value = "...", tags = "...")` | `@Tag(name = "...", description = "...")` |
| 服务接口 | `@Api(value = "...", tags = "...")` | `@Tag(name = "...", description = "...")` |

### 方法级别注解

| 用途 | Swagger 2 | OpenAPI 3 |
|:---|:---|:---|
| API 操作 | `@ApiOperation(value = "...", notes = "...")` | `@Operation(summary = "...", description = "...")` |
| 参数说明 | `@ApiParam(name = "...", value = "...", required = true)` | `@Parameter(name = "...", description = "...", required = true)` |

### 字段级别注解

| 用途 | Swagger 2 | OpenAPI 3 |
|:---|:---|:---|
| 字段说明 | `@ApiModelProperty(value = "...", required = true)` | `@Schema(description = "...", required = true)` |

## 代码示例

### Entity 实体类

#### Swagger 2

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(value = "用户对象", description = "用户实体类")
public class User {
    
    @ApiModelProperty(value = "用户ID")
    private Long id;
    
    @ApiModelProperty(value = "用户名", required = true)
    private String username;
}
```

#### OpenAPI 3

```java
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(description = "用户实体类")
public class User {
    
    @Schema(description = "用户ID")
    private Long id;
    
    @Schema(description = "用户名", required = true)
    private String username;
}
```

### Controller 控制器

#### Swagger 2

```java
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;

@Api(value = "用户管理", tags = "用户管理接口")
@RestController
@RequestMapping("/user")
public class UserController {
    
    @ApiOperation(value = "创建用户", notes = "创建新的用户记录")
    @PostMapping
    public User create(@RequestBody User user) {
        return userService.save(user);
    }
    
    @ApiOperation(value = "根据ID查询用户", notes = "根据ID查询用户详细信息")
    @ApiParam(name = "id", value = "用户ID", required = true)
    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getById(id);
    }
}
```

#### OpenAPI 3

```java
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;

@Tag(name = "用户管理", description = "用户管理接口")
@RestController
@RequestMapping("/user")
public class UserController {
    
    @Operation(summary = "创建用户", description = "创建新的用户记录")
    @PostMapping
    public User create(@RequestBody User user) {
        return userService.save(user);
    }
    
    @Operation(summary = "根据ID查询用户", description = "根据ID查询用户详细信息")
    @Parameter(name = "id", description = "用户ID", required = true)
    @GetMapping("/{id}")
    public User getById(@PathVariable Long id) {
        return userService.getById(id);
    }
}
```

### DTO 数据传输对象

#### Swagger 2

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(value = "用户创建DTO", description = "用户创建数据传输对象")
public class UserCreateDTO {
    
    @ApiModelProperty(value = "用户名", required = true)
    private String username;
    
    @ApiModelProperty(value = "邮箱地址", required = true)
    private String email;
}
```

#### OpenAPI 3

```java
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(description = "用户创建数据传输对象")
public class UserCreateDTO {
    
    @Schema(description = "用户名", required = true)
    private String username;
    
    @Schema(description = "邮箱地址", required = true)
    private String email;
}
```

## 依赖配置

### Swagger 2 依赖

```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>3.0.0</version>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>3.0.0</version>
</dependency>
```

### OpenAPI 3 依赖

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-ui</artifactId>
    <version>1.7.0</version>
</dependency>
```

## 选择建议

### 选择 Swagger 2 的情况

1. 项目使用 Spring Boot 2.x（2.0 - 2.6）
2. 项目已经集成了 springfox
3. 团队熟悉 Swagger 2 注解

### 选择 OpenAPI 3 的情况

1. 项目使用 Spring Boot 2.2+ 或 Spring Boot 3.x
2. 新项目，希望使用最新的 OpenAPI 规范
3. 需要更好的 Spring Boot 3.x 支持
4. 希望符合 OpenAPI 3.0 标准

## 模板变量

在代码生成模板中，使用以下变量控制注解类型：

- `${swagger}` - 是否启用 API 文档（boolean）
- `${swaggerVersion}` - API 文档版本（"swagger2" 或 "openapi3"）

### 模板条件判断

```velocity
#if(${swagger})
#if(${swaggerVersion} == "swagger2")
    @ApiModel(value = "...", description = "...")
#elseif(${swaggerVersion} == "openapi3")
    @Schema(description = "...")
#end
#end
```

## 参考资料

- [Swagger 2 官方文档](https://swagger.io/specification/v2/)
- [OpenAPI 3 官方文档](https://swagger.io/specification/)
- [SpringDoc OpenAPI](https://springdoc.org/)
- [SpringFox Swagger](https://springfox.github.io/springfox/)
