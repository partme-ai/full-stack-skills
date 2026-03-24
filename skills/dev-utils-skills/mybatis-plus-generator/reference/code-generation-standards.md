# 代码生成标准

本文档详细说明 MyBatis-Plus Generator 生成代码的标准和要求。

## 注释标准

**IMPORTANT: Generated code must include intelligent, context-aware comments, not just template placeholders.**

### 1. 类注释（Class Comments）

**要求：**
- 必须基于表的业务上下文解释类的用途
- 必须包含表映射信息
- 必须列出主要字段及其用途
- 必须遵循 Java 编程规范格式（使用 `<p>` 标签）

**示例：**

```java
/**
 * <p>用户实体类</p>
 * 
 * <p>对应数据库中的 users 表，用于存储用户的基本信息。
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
```

### 2. 方法注释（Method Comments）

**要求：**
- 必须基于业务需求解释方法用途
- 必须包含所有参数的类型和描述
- 必须包含返回值的类型和描述
- 必须包含异常声明（完整包名）
- 必须解释业务逻辑，不仅仅是技术操作

**示例：**

```java
/**
 * <p>根据邮箱查询用户</p>
 * 
 * <p>根据用户邮箱地址查询用户信息，用于用户登录和邮箱验证场景。
 * 如果用户不存在，返回 null。</p>
 * 
 * @param email java.lang.String 用户邮箱地址，不能为空
 * @return com.example.entity.User 用户实体对象，如果不存在则返回 null
 * @exception java.lang.IllegalArgumentException 当邮箱地址为空时抛出
 */
User findByEmail(String email);
```

### 3. 字段注释（Field Comments）

**要求：**
- 必须基于业务上下文解释字段含义
- 必须包含数据类型和约束
- 必须解释与其他字段的关系（如果适用）
- 不能只是复制列名

**示例：**

```java
/**
 * <p>用户邮箱地址</p>
 * 
 * <p>用户的唯一邮箱地址，用于登录、找回密码和接收通知。
 * 必须符合邮箱格式规范，且在整个系统中唯一。</p>
 */
@TableField("email")
private String email;
```

## 模板使用标准

### 1. 模板选择

根据以下条件选择模板：
- 对象类型（Entity, Mapper, Service, etc.）
- 编程语言（Java 或 Kotlin）
- 架构模式（MVC, DDD, etc.）

### 2. 模板增强

使用模板作为基础，但需要增强：
- 基于表结构和需求的智能注释
- 基于配置的适当注解
- 自定义方法的方法骨架
- 业务逻辑提示

### 3. 模板变量

常用模板变量：
- `${packageName}` - 包名
- `${className}` - 类名
- `${tableName}` - 表名
- `${author}` - 作者名
- `${fields}` - 字段定义
- `${methods}` - 方法定义
- `${swagger}` - 是否启用 API 文档（boolean）
- `${swaggerVersion}` - API 文档版本（"swagger2" 或 "openapi3"）

详细变量列表请参考：`template-variables.md`

### 4. Swagger 注解选择

模板根据 `${swaggerVersion}` 变量自动选择注解：
- Swagger 2: 使用 `io.swagger.annotations.*`
- OpenAPI 3: 使用 `io.swagger.v3.oas.annotations.*`

详细对比请参考：`swagger-annotations-guide.md`

## 代码生成顺序

**CRITICAL: Follow this order when generating code:**

1. **Entity** - First (base for all other objects)
2. **Mapper** - Second (data access layer)
3. **Service** - Third (business interface)
4. **ServiceImpl** - Fourth (business implementation)
5. **Controller** - Fifth (API layer)
6. **DTO/VO/BO** - Sixth (if needed by architecture)

## 自定义方法生成

### 1. 方法签名生成

根据用户需求生成方法签名：
- 分析需求确定方法名
- 确定参数类型和名称
- 确定返回类型
- 添加适当的注解

### 2. 方法注释生成

为每个自定义方法生成详细注释：
- 解释方法用途和业务逻辑
- 列出所有参数及其类型
- 说明返回值
- 列出可能的异常

### 3. 方法骨架生成

生成方法骨架，包含：
- TODO 注释提示实现细节
- 参数验证提示
- 业务逻辑提示
- 返回值处理提示

**示例：**

```java
/**
 * <p>根据邮箱查询用户</p>
 * 
 * <p>根据用户邮箱地址查询用户信息，用于用户登录和邮箱验证场景。</p>
 * 
 * @param email java.lang.String 用户邮箱地址，不能为空
 * @return com.example.entity.User 用户实体对象，如果不存在则返回 null
 */
public User findByEmail(String email) {
    // TODO: 实现根据邮箱查询用户的逻辑
    // 1. 验证邮箱参数是否为空
    // 2. 调用 Mapper 查询用户
    // 3. 返回查询结果
    return null;
}
```

## 代码质量要求

### 1. 注释完整性

- ✅ 所有类都有完整的 JavaDoc 注释
- ✅ 所有方法都有参数和返回值说明
- ✅ 所有字段都有业务含义注释
- ✅ 自定义方法都有业务逻辑说明

### 2. 代码规范

- ✅ 符合 Java 编程规范
- ✅ 使用适当的注解（Lombok, Swagger, Validation）
- ✅ 遵循命名规范（camelCase, PascalCase）
- ✅ 适当的访问修饰符

### 3. 业务逻辑

- ✅ 注释反映业务含义，不仅仅是技术描述
- ✅ 方法名清晰表达业务意图
- ✅ 参数和返回值符合业务需求

## 参考文档

- Java 编程规范：`../java-code-comments/reference/java-coding-standards.md`
- JavaDoc 标准：`../java-code-comments/reference/javadoc-standards.md`
- 模板变量：`template-variables.md`
- Swagger 注解指南：`swagger-annotations-guide.md`
