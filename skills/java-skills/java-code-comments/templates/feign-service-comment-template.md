# Feign Service Interface 类注释模板

## 类注释模板

### Java 编程规范格式（严格）

```java
/**
 * {服务名称}Feign远程服务接口
 *
 * <p>通过Feign调用{目标服务}的远程接口</p>
 * <p>主要功能:</p>
 * <ul>
 *   <li>{接口功能1}</li>
 *   <li>{接口功能2}</li>
 * </ul>
 *
 * @author system
 * @since 2025-01-21
 */
@FeignClient(name = "{service-name}", path = "/api/{resource}")
public interface [Resource]FeignService {
}
```

### 标准 JavaDoc 格式

```java
/**
 * {服务名称}Feign远程服务接口
 * 
 * <p>通过Feign调用{目标服务}的远程接口
 * 
 * <p>主要功能:
 * <ul>
 *   <li>{接口功能1}</li>
 *   <li>{接口功能2}</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
@FeignClient(name = "{service-name}", path = "/api/{resource}")
public interface [Resource]FeignService {
}
```

## 方法注释模板

### GET 请求方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>查询{资源名称}</p>
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，查询{资源名称}信息。</p>
 * 
 * @param id java.lang.Long {资源名称}唯一标识符
 * @return [Resource]DTO {返回类型} {资源名称}信息 DTO
 * @exception com.example.exception.FeignException 当远程调用失败时抛出
 */
@GetMapping("/{id}")
[Resource]DTO get[Resource](@PathVariable("id") Long id);
```

#### 标准 JavaDoc 格式

```java
/**
 * 查询{资源名称}
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，查询{资源名称}信息。
 * 
 * @param id {资源名称}唯一标识符
 * @return {资源名称}信息 DTO
 * @throws FeignException 当远程调用失败时抛出
 */
@GetMapping("/{id}")
[Resource]DTO get[Resource](@PathVariable("id") Long id);
```

### POST 请求方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>创建{资源名称}</p>
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，创建{资源名称}。</p>
 * 
 * @param request [Resource]CreateRequest {资源名称}创建请求对象
 * @return [Resource]DTO {返回类型} 创建成功的{资源名称}信息 DTO
 * @exception com.example.exception.FeignException 当远程调用失败时抛出
 */
@PostMapping
[Resource]DTO create[Resource](@RequestBody [Resource]CreateRequest request);
```

#### 标准 JavaDoc 格式

```java
/**
 * 创建{资源名称}
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，创建{资源名称}。
 * 
 * @param request {资源名称}创建请求对象
 * @return 创建成功的{资源名称}信息 DTO
 * @throws FeignException 当远程调用失败时抛出
 */
@PostMapping
[Resource]DTO create[Resource](@RequestBody [Resource]CreateRequest request);
```

### PUT 请求方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>更新{资源名称}</p>
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，更新{资源名称}信息。</p>
 * 
 * @param id java.lang.Long {资源名称}唯一标识符
 * @param request [Resource]UpdateRequest {资源名称}更新请求对象
 * @return [Resource]DTO {返回类型} 更新后的{资源名称}信息 DTO
 * @exception com.example.exception.FeignException 当远程调用失败时抛出
 */
@PutMapping("/{id}")
[Resource]DTO update[Resource](@PathVariable("id") Long id, @RequestBody [Resource]UpdateRequest request);
```

#### 标准 JavaDoc 格式

```java
/**
 * 更新{资源名称}
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，更新{资源名称}信息。
 * 
 * @param id {资源名称}唯一标识符
 * @param request {资源名称}更新请求对象
 * @return 更新后的{资源名称}信息 DTO
 * @throws FeignException 当远程调用失败时抛出
 */
@PutMapping("/{id}")
[Resource]DTO update[Resource](@PathVariable("id") Long id, @RequestBody [Resource]UpdateRequest request);
```

### DELETE 请求方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>删除{资源名称}</p>
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，删除{资源名称}。</p>
 * 
 * @param id java.lang.Long {资源名称}唯一标识符
 * @exception com.example.exception.FeignException 当远程调用失败时抛出
 */
@DeleteMapping("/{id}")
void delete[Resource](@PathVariable("id") Long id);
```

#### 标准 JavaDoc 格式

```java
/**
 * 删除{资源名称}
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，删除{资源名称}。
 * 
 * @param id {资源名称}唯一标识符
 * @throws FeignException 当远程调用失败时抛出
 */
@DeleteMapping("/{id}")
void delete[Resource](@PathVariable("id") Long id);
```

### 查询列表方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>查询{资源名称}列表</p>
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，查询{资源名称}列表，支持{查询条件}等条件筛选。</p>
 * 
 * @param query [Resource]QueryRequest {资源名称}查询请求对象，包含查询条件
 * @return java.util.List&lt;[Resource]DTO&gt; {返回类型} {资源名称}列表
 * @exception com.example.exception.FeignException 当远程调用失败时抛出
 */
@GetMapping("/list")
List<[Resource]DTO> list[Resource]([Resource]QueryRequest query);
```

#### 标准 JavaDoc 格式

```java
/**
 * 查询{资源名称}列表
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，查询{资源名称}列表，支持{查询条件}等条件筛选。
 * 
 * @param query {资源名称}查询请求对象，包含查询条件
 * @return {资源名称}列表
 * @throws FeignException 当远程调用失败时抛出
 */
@GetMapping("/list")
List<[Resource]DTO> list[Resource]([Resource]QueryRequest query);
```

### 分页查询方法

#### Java 编程规范格式（严格）

```java
/**
 * <p>分页查询{资源名称}列表</p>
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，分页查询{资源名称}列表。</p>
 * 
 * @param query [Resource]QueryRequest {资源名称}查询请求对象，包含分页参数和查询条件
 * @return com.baomidou.mybatisplus.core.metadata.IPage&lt;[Resource]DTO&gt; {返回类型} 分页结果，包含{资源名称}列表和分页信息
 * @exception com.example.exception.FeignException 当远程调用失败时抛出
 */
@PostMapping("/page")
IPage<[Resource]DTO> page[Resource](@RequestBody [Resource]QueryRequest query);
```

#### 标准 JavaDoc 格式

```java
/**
 * 分页查询{资源名称}列表
 * 
 * <p>通过Feign调用{目标服务}的{接口路径}接口，分页查询{资源名称}列表。
 * 
 * @param query {资源名称}查询请求对象，包含分页参数和查询条件
 * @return 分页结果，包含{资源名称}列表和分页信息
 * @throws FeignException 当远程调用失败时抛出
 */
@PostMapping("/page")
IPage<[Resource]DTO> page[Resource](@RequestBody [Resource]QueryRequest query);
```

## 使用说明

1. **替换占位符**：
   - `{服务名称}` - 替换为实际的服务名称，如"用户"、"订单"等
   - `{目标服务}` - 替换为实际的目标服务名称，如"用户服务"、"订单服务"等
   - `{service-name}` - 替换为实际的 Feign 服务名称（配置中的服务名）
   - `{resource}` - 替换为实际的资源路径
   - `{资源名称}` - 替换为实际的资源名称，如"用户"、"订单"等
   - `[Resource]` - 替换为实际的类名，如"User"、"Order"等
   - `{接口功能}` - 替换为实际的接口功能描述
   - `{接口路径}` - 替换为实际的接口路径

2. **选择格式**：
   - 如果项目遵循《JAVA 编程规范》，使用"Java 编程规范格式（严格）"
   - 如果项目使用标准 JavaDoc，使用"标准 JavaDoc 格式"

3. **方法注释**：
   - Feign 接口方法注释应明确说明调用的目标服务和接口路径
   - 所有方法都应说明可能抛出的 FeignException
   - 参数和返回值应与远程服务接口保持一致

4. **Feign 接口特点**：
   - 接口方法通常对应远程服务的 REST API
   - 方法签名应与远程服务接口保持一致
   - 异常处理通常统一为 FeignException
   - 需要配置正确的 @FeignClient 注解参数
