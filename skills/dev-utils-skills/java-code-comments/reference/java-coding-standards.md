# Java 编程规范 - 严格格式要求

## 概述

本文档基于《JAVA 编程规范》第10节"文档化"的要求，说明与标准 JavaDoc 的**差异**和**严格格式要求**。

> **重要提示**：本文档只说明严格格式的特殊要求。标准 JavaDoc 格式请参考 [javadoc-standards.md](./javadoc-standards.md)。

## 核心要求

根据《JAVA 编程规范》，必须用 javadoc 来为类生成文档，这是被各种 Java 编译器都认可的标准方法。但规范对格式有更严格的要求。

## 与标准 JavaDoc 的区别

本规范与标准 JavaDoc 的主要区别：

### 1. 描述信息必须使用 `<p>` 标签包裹

**标准 JavaDoc**：
```java
/**
 * 类描述
 * 
 * <p>详细说明（可选）
 */
```

**Java 编程规范（严格）**：
```java
/**
 * <p>类描述</p>
 *
 * <p>详细说明（必须用 <p> 标签包裹）</p>
 */
```

**要求**：
- 类、方法、字段的描述**必须**使用 `<p> </p>` 括起来
- 不能直接写描述，必须包裹在 `<p>` 标签中

### 2. 参数类型必须明确声明

**标准 JavaDoc**：
```java
/**
 * @param username 用户名，长度3-20个字符
 */
```

**Java 编程规范（严格）**：
```java
/**
 * @param username java.lang.String 用户名，长度3-20个字符
 */
```

**要求**：
- 格式：`@param 参数名 参数类型 参数说明`
- 参数类型使用完整类名（如 `java.lang.String`）或简单类型（如 `int`）

### 3. 返回值类型必须明确声明

**标准 JavaDoc**：
```java
/**
 * @return 用户信息DTO
 */
```

**Java 编程规范（严格）**：
```java
/**
 * @return com.example.dto.UserDTO 用户信息DTO
 */
```

**要求**：
- 格式：`@return 返回类型 返回值说明`
- 返回类型使用完整类名或简单类型

### 4. 异常类型必须使用完整包名

**标准 JavaDoc**：
```java
/**
 * @throws IllegalArgumentException 当参数不合法时抛出
 */
```

**Java 编程规范（严格）**：
```java
/**
 * @exception java.lang.IllegalArgumentException 当参数不合法时抛出
 */
```

**要求**：
- 格式：`@exception 完整异常类型 异常说明` 或 `@throws 完整异常类型 异常说明`
- 异常类型必须包含完整包名（如 `java.lang.Exception`）

## 格式示例

### 类注释格式

```java
/**
 * <p>用户管理服务类</p>
 *
 * <p>提供用户相关的业务逻辑处理，包括用户的创建、查询、更新和删除操作。
 * 本服务遵循领域驱动设计（DDD）原则，封装用户领域的核心业务逻辑。</p>
 *
 * @author System
 * @since 1.0.0
 */
public class UserService {
}
```

### 方法注释格式

```java
/**
 * <p>根据用户ID查询用户信息</p>
 *
 * <p>根据提供的用户ID从数据库查询对应的用户详细信息。
 * 如果用户不存在，将抛出ResourceNotFoundException异常。</p>
 *
 * @param id java.lang.Long 用户唯一标识符，不能为null
 * @return com.example.dto.UserDTO 用户信息DTO，包含用户的基本信息
 * @exception com.example.exception.ResourceNotFoundException 当用户不存在时抛出
 * @exception java.lang.IllegalArgumentException 当id为null时抛出
 */
@GetMapping("/{id}")
public UserDTO getUserById(@PathVariable Long id) {
    // 实现代码
}
```

### 字段注释格式

```java
/**
 * <p>用户数据访问对象</p>
 *
 * <p>用于执行用户相关的数据库操作，由Spring容器注入</p>
 */
private final UserMapper userMapper;
```

### 多参数方法示例

```java
/**
 * <p>创建新用户</p>
 *
 * <p>根据用户创建请求创建新用户，包括数据验证、密码加密等处理。</p>
 *
 * @param username java.lang.String 用户名，长度3-20个字符
 * @param email java.lang.String 邮箱地址，必须符合邮箱格式
 * @param password java.lang.String 密码，长度至少8个字符
 * @return com.example.dto.UserDTO 创建成功的用户信息DTO
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 * @exception com.example.exception.BusinessException 当用户名或邮箱已存在时抛出
 */
public UserDTO createUser(String username, String email, String password) 
    throws IllegalArgumentException, BusinessException {
}
```

## 标签使用规范

### @param 标签

**格式**：`@param 参数名 参数类型 参数说明`

**示例**：
```java
/**
 * @param userId java.lang.Long 用户唯一标识符，不能为null
 * @param username java.lang.String 用户名，长度3-20个字符
 */
```

### @return 标签

**格式**：`@return 返回类型 返回值说明`

**示例**：
```java
/**
 * @return int 返回操作结果，0表示成功，-1表示失败
 * @return com.example.dto.UserDTO 用户信息DTO，如果用户不存在则返回null
 */
```

### @exception / @throws 标签

**格式**：`@exception 完整异常类型 异常说明` 或 `@throws 完整异常类型 异常说明`

**示例**：
```java
/**
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 * @exception com.example.exception.BusinessException 当业务规则违反时抛出
 * @exception java.lang.Exception 当系统发生未知错误时抛出
 */
```

## 规范要点总结

1. **必须使用 `<p>` 标签包裹描述信息**
   - 类描述：`<p>类描述</p>`
   - 方法描述：`<p>方法描述</p>`
   - 字段描述：`<p>字段描述</p>`

2. **必须声明所有参数类型**
   - 格式：`@param 参数名 参数类型 参数说明`
   - 参数类型使用完整类名（如 `java.lang.String`）或简单类型（如 `int`）

3. **必须声明返回值类型**
   - 格式：`@return 返回类型 返回值说明`
   - 返回类型使用完整类名或简单类型

4. **必须声明异常类型（包含完整包名）**
   - 格式：`@exception 完整异常类型 异常说明` 或 `@throws 完整异常类型 异常说明`
   - 异常类型必须包含完整包名

5. **标签顺序**
   - 描述信息（`<p>` 标签）
   - `@param` 标签（按参数顺序）
   - `@return` 标签
   - `@exception` / `@throws` 标签
   - 其他标签（`@author`, `@since` 等）

## 完整示例对比

### 标准 JavaDoc 格式

```java
/**
 * 用户管理控制器
 * 
 * <p>提供用户相关的REST API接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循RESTful设计规范，使用标准的HTTP方法进行资源操作。
 * 
 * @author System
 * @since 1.0.0
 */
```

### Java 编程规范格式（严格）

```java
/**
 * <p>用户管理控制器</p>
 *
 * <p>提供用户相关的REST API接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循RESTful设计规范，使用标准的HTTP方法进行资源操作。</p>
 *
 * @author System
 * @since 1.0.0
 */
```

## 何时使用本规范

使用本严格格式规范的情况：

- 项目明确要求遵循《JAVA 编程规范》
- 项目要求所有描述信息必须使用 `<p>` 标签包裹
- 项目要求参数和返回值类型必须在注释中明确声明
- 项目要求异常类型必须使用完整包名

## 参考资料

- 《JAVA 编程规范》第10节 - 文档化
- 标准 JavaDoc 规范：参见 [javadoc-standards.md](./javadoc-standards.md)
