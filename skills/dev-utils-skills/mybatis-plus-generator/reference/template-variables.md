# 模板变量参考

## 概述

本文档说明 MyBatis-Plus Generator 模板中可用的变量，用于在代码生成时替换模板占位符。

## 基础变量

### 包相关变量

- `${package.Entity}` - Entity 包路径（如：`com.example.app.entity`）
- `${package.Mapper}` - Mapper 包路径（如：`com.example.app.mapper`）
- `${package.Service}` - Service 包路径（如：`com.example.app.service`）
- `${package.ServiceImpl}` - ServiceImpl 包路径（如：`com.example.app.service.impl`）
- `${package.Controller}` - Controller 包路径（如：`com.example.app.controller`）
- `${package.DTO}` - DTO 包路径（如：`com.example.app.dto`）
- `${package.VO}` - VO 包路径（如：`com.example.app.vo`）
- `${package.BO}` - BO 包路径（如：`com.example.app.bo`）
- `${package.ModuleName}` - 模块名称（可选）

### 类名相关变量

- `${entity}` - 实体类名（如：`User`）
- `${table.entityName}` - 实体类名（同 `${entity}`）
- `${table.mapperName}` - Mapper 接口名（如：`UserMapper`）
- `${table.serviceName}` - Service 接口名（如：`UserService`）
- `${table.serviceImplName}` - ServiceImpl 类名（如：`UserServiceImpl`）
- `${table.controllerName}` - Controller 类名（如：`UserController`）
- `${table.entityPath}` - 实体路径（用于 URL，如：`user`）

### 表相关变量

- `${table.name}` - 表名（如：`user`）
- `${table.comment}` - 表注释（如：`用户表`）
- `${schemaName}` - 数据库 schema 名称（可选）

### 作者和日期

- `${author}` - 作者名称
- `${date}` - 当前日期（格式：`yyyy-MM-dd`）

## 字段相关变量

### 字段循环

在模板中使用 `#foreach($field in ${table.fields})` 循环遍历所有字段。

### 字段属性

- `${field.name}` - 数据库字段名（如：`user_name`）
- `${field.propertyName}` - Java 属性名（如：`userName`）
- `${field.type}` - 数据库字段类型（如：`varchar`）
- `${field.propertyType}` - Java 属性类型（如：`String`）
- `${field.comment}` - 字段注释（如：`用户名`）
- `${field.length}` - 字段长度（如：`50`）
- `${field.keyFlag}` - 是否为主键（boolean）
- `${field.fill}` - 字段填充策略（如：`INSERT`、`UPDATE`、`INSERT_UPDATE`）
- `${field.convert}` - 是否需要字段转换（boolean）
- `${field.versionField}` - 是否为版本字段（boolean）
- `${field.logicDeleteField}` - 是否为逻辑删除字段（boolean）

## 配置相关变量

### 全局配置

- `${swagger}` - 是否启用 API 文档（boolean）
- `${swaggerVersion}` - API 文档版本（"swagger2" 或 "openapi3"）
  - **"swagger2"**: 使用 `io.swagger.annotations.*` 包（Swagger 2）
  - **"openapi3"**: 使用 `io.swagger.v3.oas.annotations.*` 包（OpenAPI 3）
- `${entityLombokModel}` - 是否使用 Lombok（boolean）
- `${restControllerStyle}` - 是否使用 REST 风格（boolean）
- `${controllerMappingHyphenStyle}` - Controller 映射是否使用连字符（boolean）
- `${superEntityClass}` - 父实体类（可选）
- `${superEntityClassPackage}` - 父实体类包路径（可选）
- `${superMapperClass}` - 父 Mapper 类（默认：`BaseMapper`）
- `${superMapperClassPackage}` - 父 Mapper 类包路径（默认：`com.baomidou.mybatisplus.core.mapper.BaseMapper`）
- `${superServiceClass}` - 父 Service 类（默认：`IService`）
- `${superServiceClassPackage}` - 父 Service 类包路径（默认：`com.baomidou.mybatisplus.extension.service.IService`）
- `${superServiceImplClass}` - 父 ServiceImpl 类（默认：`ServiceImpl`）
- `${superServiceImplClassPackage}` - 父 ServiceImpl 类包路径（默认：`com.baomidou.mybatisplus.extension.service.impl.ServiceImpl`）
- `${superControllerClass}` - 父 Controller 类（可选）
- `${superControllerClassPackage}` - 父 Controller 类包路径（可选）

### 主键策略

- `${keyStrategy}` - 主键策略（如：`AUTO`、`UUID`、`ID_WORKER`）
- `${keyPropertyName}` - 主键属性名（如：`id`）

### 序列化

- `${serialVersionUID}` - 是否生成 serialVersionUID（boolean）

## 自定义方法变量

### 自定义方法循环

在模板中使用 `#foreach($method in ${customMethods})` 循环遍历自定义方法。

### 方法属性

- `${method.name}` - 方法名（如：`findByEmail`）
- `${method.description}` - 方法描述（如：`根据邮箱查询用户`）
- `${method.detailDescription}` - 方法详细描述
- `${method.returnType}` - 返回类型（如：`User`）
- `${method.returnDescription}` - 返回值描述
- `${method.mappingPath}` - Controller 映射路径（如：`email/{email}`）

### 方法参数循环

在方法中使用 `#foreach($param in ${method.parameters})` 循环遍历方法参数。

### 参数属性

- `${param.name}` - 参数名（如：`email`）
- `${param.type}` - 参数类型（如：`String`）
- `${param.description}` - 参数描述（如：`用户邮箱地址`）

### 方法异常循环

在方法中使用 `#foreach($exception in ${method.exceptions})` 循环遍历方法异常。

### 异常属性

- `${exception.type}` - 异常类型（如：`java.lang.IllegalArgumentException`）
- `${exception.description}` - 异常描述（如：`当邮箱地址为空时抛出`）

## DTO 相关变量

### DTO 类型

- `${dtoType}` - DTO 类型（如：`Create`、`Update`、`Query`）
- `${dtoPurpose}` - DTO 用途（如：`创建用户`、`更新用户`）
- `${dtoUsage}` - DTO 使用场景（如：`用户注册`、`用户信息更新`）

### DTO 字段循环

在 DTO 模板中使用 `#foreach($field in ${dtoFields})` 循环遍历 DTO 字段。

### DTO 字段属性

- `${field.required}` - 字段是否必填（boolean）
- 其他字段属性同普通字段

## 条件判断

### 条件语法

```velocity
#if(${condition})
    // 条件为真时的代码
#else
    // 条件为假时的代码
#end
```

### 常用条件

- `${swagger}` - 是否启用 Swagger
- `${entityLombokModel}` - 是否使用 Lombok
- `${customMethods}` - 是否有自定义方法
- `${superEntityClass}` - 是否有父实体类
- `${field.keyFlag}` - 是否为主键字段
- `${field.fill}` - 是否有字段填充策略

## 循环语法

### foreach 循环

```velocity
#foreach($item in ${items})
    // 循环体
    ${item.property}
#end
```

### 循环变量

- `${foreach.index}` - 当前索引（从 0 开始）
- `${foreach.count}` - 当前计数（从 1 开始）
- `${foreach.hasNext}` - 是否有下一个元素（boolean）
- `${foreach.first}` - 是否为第一个元素（boolean）
- `${foreach.last}` - 是否为最后一个元素（boolean）

## 字符串操作

### 大小写转换

- `${string.substring(0,1).toLowerCase()}` - 首字母小写
- `${string.substring(0,1).toUpperCase()}` - 首字母大写

### 字符串判断

- `"$!field.comment" != ""` - 判断字符串不为空

## 使用示例

### 示例 1：生成字段

```velocity
#foreach($field in ${table.fields})
    /**
     * ${field.comment}
     */
    private ${field.propertyType} ${field.propertyName};
#end
```

### 示例 2：条件生成

```velocity
#if(${swagger})
    @ApiModelProperty(value = "${field.comment}")
#end
```

### 示例 4：Swagger 注解选择

```velocity
#if(${swagger})
#if(${swaggerVersion} == "swagger2")
    @ApiModel(value = "${entity}对象", description = "${table.comment}")
    @ApiModelProperty(value = "${field.comment}")
    @Api(value = "${table.comment}管理", tags = "${table.comment}管理接口")
    @ApiOperation(value = "创建${table.comment}", notes = "创建新的${table.comment}记录")
#elseif(${swaggerVersion} == "openapi3")
    @Schema(description = "${table.comment}")
    @Schema(description = "${field.comment}")
    @Tag(name = "${table.comment}管理", description = "${table.comment}管理接口")
    @Operation(summary = "创建${table.comment}", description = "创建新的${table.comment}记录")
#end
#end
```

### 示例 3：自定义方法

```velocity
#foreach($method in ${customMethods})
    /**
     * ${method.description}
     */
    ${method.returnType} ${method.name}(#foreach($param in ${method.parameters})${param.type} ${param.name}#if($foreach.hasNext), #end#end);
#end
```

### 示例 4：Swagger 注解选择

```velocity
#if(${swagger})
#if(${swaggerVersion} == "swagger2")
    @ApiModel(value = "${entity}对象", description = "${table.comment}")
    @ApiModelProperty(value = "${field.comment}")
    @Api(value = "${table.comment}管理", tags = "${table.comment}管理接口")
    @ApiOperation(value = "创建${table.comment}", notes = "创建新的${table.comment}记录")
#elseif(${swaggerVersion} == "openapi3")
    @Schema(description = "${table.comment}")
    @Schema(description = "${field.comment}")
    @Tag(name = "${table.comment}管理", description = "${table.comment}管理接口")
    @Operation(summary = "创建${table.comment}", description = "创建新的${table.comment}记录")
#end
#end
```

## 参考资料

- [Velocity 模板语法](https://velocity.apache.org/engine/2.3/user-guide.html)
- [MyBatis-Plus Generator 文档](https://baomidou.com/pages/d357af/)
