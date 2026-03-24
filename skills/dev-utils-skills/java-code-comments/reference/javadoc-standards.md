# JavaDoc 注释规范

## 概述

JavaDoc 是 Java 的文档生成工具，通过标准化的注释格式生成 API 文档。本文档说明如何编写符合规范的 JavaDoc 注释。

> **注意**：本文档基于标准 JavaDoc 规范。如果项目遵循《JAVA 编程规范》，请参考 [java-coding-standards.md](./java-coding-standards.md) 获取更严格的格式要求（该文档只说明与标准 JavaDoc 的差异，避免重复）。

## 注释格式

### 基本格式

```java
/**
 * 注释内容
 */
```

### 多行注释

```java
/**
 * 第一行注释
 * 第二行注释
 * 第三行注释
 */
```

### 段落分隔

使用 `<p>` 标签分隔段落：

```java
/**
 * 第一段内容
 * 
 * <p>第二段内容
 * 
 * <p>第三段内容
 */
```

## 类注释

### 基本结构

```java
/**
 * 类描述
 * 
 * <p>详细说明
 * 
 * @author 作者名
 * @since 版本号或日期
 * @version 版本号（可选）
 */
public class MyClass {
}
```

### 必需标签

- `@author`: 作者信息
- `@since`: 首次引入的版本或日期

### 可选标签

- `@version`: 版本号
- `@see`: 相关类或方法的引用
- `@deprecated`: 标记为已废弃

### 示例

```java
/**
 * 用户管理服务
 * 
 * <p>提供用户相关的业务逻辑处理，包括用户的创建、查询、更新和删除操作。
 * 本服务遵循领域驱动设计（DDD）原则，封装用户领域的核心业务逻辑。
 * 
 * @author System
 * @since 1.0.0
 * @version 1.0.0
 */
public class UserService {
}
```

## 方法注释

### 基本结构

```java
/**
 * 方法描述
 * 
 * <p>详细说明（可选）
 * 
 * @param 参数名 参数说明
 * @return 返回值说明
 * @throws 异常类型 异常说明
 */
public ReturnType methodName(ParamType param) {
}
```

### 必需标签

- `@param`: 每个参数都需要一个 @param 标签
- `@return`: 如果方法有返回值，必须包含 @return 标签
- `@throws`: 如果方法可能抛出异常，必须包含 @throws 标签

### 示例

```java
/**
 * 根据用户 ID 查询用户信息
 * 
 * <p>根据提供的用户 ID 从数据库查询对应的用户详细信息。
 * 如果用户不存在，将抛出 ResourceNotFoundException 异常。
 * 
 * @param id 用户唯一标识符，不能为 null
 * @return 用户信息 DTO，如果用户不存在则返回 null
 * @throws ResourceNotFoundException 当用户不存在时抛出
 * @throws IllegalArgumentException 当 id 为 null 时抛出
 */
public UserDTO findById(Long id) {
    // 实现代码
}
```

## 字段注释

### 基本结构

```java
/**
 * 字段描述
 * 
 * <p>详细说明（可选）
 */
private FieldType fieldName;
```

### 示例

```java
/**
 * 用户数据访问对象
 * 
 * <p>用于执行用户相关的数据库操作，由 Spring 容器注入
 */
private final UserMapper userMapper;
```

## 常用标签

### @param

用于描述方法参数：

```java
/**
 * @param username 用户名，长度 3-20 个字符
 * @param password 密码，长度至少 8 个字符
 */
public void login(String username, String password) {
}
```

### @return

用于描述返回值：

```java
/**
 * @return 用户信息列表，如果不存在则返回空列表
 */
public List<UserDTO> findAll() {
}
```

### @throws

用于描述可能抛出的异常：

```java
/**
 * @throws IllegalArgumentException 当参数不合法时抛出
 * @throws BusinessException 当业务规则违反时抛出
 */
public void createUser(UserCreateRequest request) {
}
```

### @see

用于引用相关的类或方法：

```java
/**
 * @see UserService
 * @see #findById(Long)
 */
public class UserController {
}
```

### @deprecated

用于标记已废弃的方法或类：

```java
/**
 * @deprecated 使用 {@link #newMethod()} 替代
 */
@Deprecated
public void oldMethod() {
}
```

### @since

用于标记首次引入的版本：

```java
/**
 * @since 1.2.0
 */
public void newFeature() {
}
```

## HTML 标签

JavaDoc 支持在注释中使用 HTML 标签：

### 列表

```java
/**
 * <p>主要功能：
 * <ul>
 *   <li>创建用户</li>
 *   <li>查询用户</li>
 *   <li>更新用户</li>
 * </ul>
 */
```

### 有序列表

```java
/**
 * <p>处理流程：
 * <ol>
 *   <li>验证参数</li>
 *   <li>执行业务逻辑</li>
 *   <li>返回结果</li>
 * </ol>
 */
```

### 代码块

```java
/**
 * <p>使用示例：
 * <pre>{@code
 * UserService service = new UserService();
 * UserDTO user = service.findById(1L);
 * }</pre>
 */
```

### 内联代码

```java
/**
 * <p>使用 {@code UserService} 处理用户相关业务
 */
```

### 链接

```java
/**
 * <p>参考 {@link UserService#findById(Long)}
 */
```

## 最佳实践

1. **简洁明了**：注释应该清晰、简洁，避免冗余
2. **完整准确**：确保注释准确反映代码的实际行为
3. **及时更新**：代码修改时同步更新注释
4. **使用标准格式**：遵循 JavaDoc 标准格式
5. **包含示例**：对于复杂方法，提供使用示例
6. **说明副作用**：如果方法有副作用，必须在注释中说明

## 常见错误

### 错误 1: 缺少 @param 标签

```java
// ❌ 错误
/**
 * 创建用户
 */
public void createUser(String username) {
}

// ✅ 正确
/**
 * 创建用户
 * 
 * @param username 用户名
 */
public void createUser(String username) {
}
```

### 错误 2: 缺少 @return 标签

```java
// ❌ 错误
/**
 * 查询用户
 */
public UserDTO findById(Long id) {
}

// ✅ 正确
/**
 * 查询用户
 * 
 * @param id 用户 ID
 * @return 用户信息 DTO
 */
public UserDTO findById(Long id) {
}
```

### 错误 3: 注释与代码不一致

```java
// ❌ 错误：注释说返回 null，但实际抛出异常
/**
 * @return 用户信息，如果不存在则返回 null
 */
public UserDTO findById(Long id) {
    throw new ResourceNotFoundException();
}

// ✅ 正确
/**
 * @param id 用户 ID
 * @return 用户信息 DTO
 * @throws ResourceNotFoundException 当用户不存在时抛出
 */
public UserDTO findById(Long id) {
    throw new ResourceNotFoundException();
}
```

## 参考资源

- [Oracle JavaDoc Guide](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)
- [JavaDoc 规范](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html)
