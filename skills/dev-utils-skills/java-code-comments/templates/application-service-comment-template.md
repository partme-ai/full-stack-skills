# Application Service 类注释模板

## 类注释模板

### Java 编程规范格式（严格）

```java
/**
 * {服务名称}应用服务
 *
 * <p>{详细描述服务的业务功能、职责和应用场景}</p>
 * <p>主要功能包括:</p>
 * <ul>
 *   <li>{功能点1}</li>
 *   <li>{功能点2}</li>
 *   <li>{功能点3}</li>
 * </ul>
 *
 * @author system
 * @since 2025-01-21
 */
public class [Resource]ApplicationService {
}
```

### 标准 JavaDoc 格式

```java
/**
 * {服务名称}应用服务
 * 
 * <p>{详细描述服务的业务功能、职责和应用场景}
 * 
 * <p>主要功能包括:
 * <ul>
 *   <li>{功能点1}</li>
 *   <li>{功能点2}</li>
 *   <li>{功能点3}</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
public class [Resource]ApplicationService {
}
```

## 字段注释模板

```java
/**
 * <p>[依赖名称]</p>
 * 
 * <p>用于[用途说明]，负责[具体职责]
 */
private final [DependencyType] [dependencyName];
```

## 方法注释模板

### 创建方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>创建{资源名称}</p>
 * 
 * <p>实现{资源名称}创建的业务逻辑，包括：
 * <ol>
 *   <li>{步骤1}</li>
 *   <li>{步骤2}</li>
 *   <li>{步骤3}</li>
 * </ol>
 * </p>
 * 
 * @param request [Resource]CreateRequest {资源名称}创建请求对象，包含{字段列表}等信息
 * @return [Resource]DTO {返回类型} 创建成功的{资源名称}信息 DTO
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 * @exception com.example.exception.BusinessException 当{业务规则}时抛出
 */
public [Resource]DTO create[Resource]([Resource]CreateRequest request) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 创建{资源名称}
 * 
 * <p>实现{资源名称}创建的业务逻辑，包括：
 * <ol>
 *   <li>{步骤1}</li>
 *   <li>{步骤2}</li>
 *   <li>{步骤3}</li>
 * </ol>
 * 
 * @param request {资源名称}创建请求对象，包含{字段列表}等信息
 * @return 创建成功的{资源名称}信息 DTO
 * @throws IllegalArgumentException 当请求参数不合法时抛出
 * @throws BusinessException 当{业务规则}时抛出
 */
public [Resource]DTO create[Resource]([Resource]CreateRequest request) {
}
```

### 查询方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>根据 ID 查询{资源名称}</p>
 * 
 * <p>根据{资源名称} ID 从数据库查询{资源名称}信息，如果{资源名称}不存在则抛出异常。</p>
 * 
 * @param id java.lang.Long {资源名称}唯一标识符
 * @return [Resource]DTO {返回类型} {资源名称}信息 DTO
 * @exception com.example.exception.ResourceNotFoundException 当{资源名称}不存在时抛出
 */
public [Resource]DTO findById(Long id) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 根据 ID 查询{资源名称}
 * 
 * <p>根据{资源名称} ID 从数据库查询{资源名称}信息，如果{资源名称}不存在则抛出异常。
 * 
 * @param id {资源名称}唯一标识符
 * @return {资源名称}信息 DTO
 * @throws ResourceNotFoundException 当{资源名称}不存在时抛出
 */
public [Resource]DTO findById(Long id) {
}
```

### 更新方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>更新{资源名称}</p>
 * 
 * <p>实现{资源名称}更新的业务逻辑，包括：
 * <ol>
 *   <li>验证{资源名称}是否存在</li>
 *   <li>验证更新数据的合法性</li>
 *   <li>执行更新操作</li>
 * </ol>
 * </p>
 * 
 * @param id java.lang.Long {资源名称}唯一标识符
 * @param request [Resource]UpdateRequest {资源名称}更新请求对象
 * @return [Resource]DTO {返回类型} 更新后的{资源名称}信息 DTO
 * @exception com.example.exception.ResourceNotFoundException 当{资源名称}不存在时抛出
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 */
public [Resource]DTO update[Resource](Long id, [Resource]UpdateRequest request) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 更新{资源名称}
 * 
 * <p>实现{资源名称}更新的业务逻辑，包括：
 * <ol>
 *   <li>验证{资源名称}是否存在</li>
 *   <li>验证更新数据的合法性</li>
 *   <li>执行更新操作</li>
 * </ol>
 * 
 * @param id {资源名称}唯一标识符
 * @param request {资源名称}更新请求对象
 * @return 更新后的{资源名称}信息 DTO
 * @throws ResourceNotFoundException 当{资源名称}不存在时抛出
 * @throws IllegalArgumentException 当请求参数不合法时抛出
 */
public [Resource]DTO update[Resource](Long id, [Resource]UpdateRequest request) {
}
```

### 删除方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>删除{资源名称}</p>
 * 
 * <p>根据{资源名称} ID 删除{资源名称}，执行逻辑删除操作。</p>
 * 
 * @param id java.lang.Long {资源名称}唯一标识符
 * @exception com.example.exception.ResourceNotFoundException 当{资源名称}不存在时抛出
 */
public void delete[Resource](Long id) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 删除{资源名称}
 * 
 * <p>根据{资源名称} ID 删除{资源名称}，执行逻辑删除操作。
 * 
 * @param id {资源名称}唯一标识符
 * @throws ResourceNotFoundException 当{资源名称}不存在时抛出
 */
public void delete[Resource](Long id) {
}
```

### 分页查询方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>分页查询{资源名称}列表</p>
 * 
 * <p>根据查询条件分页查询{资源名称}列表，支持{查询条件列表}等条件筛选。</p>
 * 
 * @param query [Resource]QueryRequest {资源名称}查询请求对象，包含分页参数和查询条件
 * @return com.baomidou.mybatisplus.core.metadata.IPage&lt;[Resource]DTO&gt; {返回类型} 分页结果，包含{资源名称}列表和分页信息
 */
public IPage<[Resource]DTO> page[Resource]([Resource]QueryRequest query) {
}
```

#### 标准 JavaDoc 格式

```java
/**
 * 分页查询{资源名称}列表
 * 
 * <p>根据查询条件分页查询{资源名称}列表，支持{查询条件列表}等条件筛选。
 * 
 * @param query {资源名称}查询请求对象，包含分页参数和查询条件
 * @return 分页结果，包含{资源名称}列表和分页信息
 */
public IPage<[Resource]DTO> page[Resource]([Resource]QueryRequest query) {
}
```

## 使用说明

1. **替换占位符**：
   - `{服务名称}` - 替换为实际的服务名称，如"用户"、"订单"等
   - `{资源名称}` - 替换为实际的资源名称，如"用户"、"订单"等
   - `[Resource]` - 替换为实际的类名，如"User"、"Order"等
   - `{功能点}` - 替换为实际的功能点描述
   - `{字段列表}` - 替换为实际的字段列表

2. **选择格式**：
   - 如果项目遵循《JAVA 编程规范》，使用"Java 编程规范格式（严格）"
   - 如果项目使用标准 JavaDoc，使用"标准 JavaDoc 格式"

3. **方法注释**：
   - 根据方法的实际功能选择合适的模板
   - 补充具体的业务逻辑描述
   - 明确参数和返回值的含义
