# Controller 类注释模板

## 类注释模板

### 标准 JavaDoc 格式

```java
/**
 * [资源名称]控制器
 * 
 * <p>提供[资源名称]相关的 REST API 接口，包括[主要功能列表]。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>[功能1]</li>
 *   <li>[功能2]</li>
 *   <li>[功能3]</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
```

### Java 编程规范格式（严格）

```java
/**
 * <p>[资源名称]控制器</p>
 * 
 * <p>提供[资源名称]相关的 REST API 接口，包括[主要功能列表]。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。</p>
 * 
 * <p>主要功能：
 * <ul>
 *   <li>[功能1]</li>
 *   <li>[功能2]</li>
 *   <li>[功能3]</li>
 * </ul>
 * </p>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
```

## 字段注释模板

```java
/**
 * [服务名称]
 * 
 * <p>用于处理[资源名称]相关的业务逻辑
 */
private final [ServiceType] [serviceName];
```

## 方法注释模板

### POST 方法（创建资源）

#### 标准 JavaDoc 格式

```java
/**
 * 创建[资源名称]
 * 
 * <p>接收[资源名称]创建请求，验证数据后创建新[资源名称]并返回[资源名称]信息。
 * 
 * @param request [资源名称]创建请求对象，包含[字段列表]等信息
 * @return 创建成功的[资源名称]信息 DTO
 * @throws IllegalArgumentException 当请求参数不合法时抛出
 * @throws BusinessException 当[业务规则]时抛出
 */
@PostMapping
public [ResourceDTO] create[Resource](@RequestBody [Resource]CreateRequest request) {
}
```

#### Java 编程规范格式（严格）

```java
/**
 * <p>创建[资源名称]</p>
 * 
 * <p>接收[资源名称]创建请求，验证数据后创建新[资源名称]并返回[资源名称]信息。</p>
 * 
 * @param request com.example.dto.[Resource]CreateRequest [资源名称]创建请求对象，包含[字段列表]等信息
 * @return com.example.dto.[Resource]DTO 创建成功的[资源名称]信息 DTO
 * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
 * @exception com.example.exception.BusinessException 当[业务规则]时抛出
 */
@PostMapping
public [ResourceDTO] create[Resource](@RequestBody [Resource]CreateRequest request) {
}
```

### GET 方法（查询资源）

#### 标准 JavaDoc 格式

```java
/**
 * 根据[资源名称] ID 查询[资源名称]信息
 * 
 * <p>根据提供的[资源名称] ID 查询对应的[资源名称]详细信息。
 * 
 * @param id [资源名称]唯一标识符
 * @return [资源名称]信息 DTO，包含[资源名称]的基本信息
 * @throws ResourceNotFoundException 当[资源名称]不存在时抛出
 */
@GetMapping("/{id}")
public [ResourceDTO] get[Resource]ById(@PathVariable Long id) {
}
```

#### Java 编程规范格式（严格）

```java
/**
 * <p>根据[资源名称] ID 查询[资源名称]信息</p>
 * 
 * <p>根据提供的[资源名称] ID 查询对应的[资源名称]详细信息。</p>
 * 
 * @param id java.lang.Long [资源名称]唯一标识符，不能为null
 * @return com.example.dto.[Resource]DTO [资源名称]信息 DTO，包含[资源名称]的基本信息
 * @exception com.example.exception.ResourceNotFoundException 当[资源名称]不存在时抛出
 */
@GetMapping("/{id}")
public [ResourceDTO] get[Resource]ById(@PathVariable Long id) {
}
```

### PUT 方法（更新资源）

```java
/**
 * 更新[资源名称]信息
 * 
 * <p>根据[资源名称] ID 和更新请求，更新[资源名称]的指定字段信息。
 * 
 * @param id [资源名称]唯一标识符
 * @param request [资源名称]更新请求对象，包含需要更新的字段信息
 * @return 更新后的[资源名称]信息 DTO
 * @throws ResourceNotFoundException 当[资源名称]不存在时抛出
 * @throws IllegalArgumentException 当更新参数不合法时抛出
 */
@PutMapping("/{id}")
public [ResourceDTO] update[Resource](@PathVariable Long id, @RequestBody [Resource]UpdateRequest request) {
}
```

### DELETE 方法（删除资源）

```java
/**
 * 删除[资源名称]
 * 
 * <p>根据[资源名称] ID 删除指定的[资源名称]。删除操作会级联删除[资源名称]相关的数据。
 * 
 * @param id [资源名称]唯一标识符
 * @throws ResourceNotFoundException 当[资源名称]不存在时抛出
 */
@DeleteMapping("/{id}")
public void delete[Resource](@PathVariable Long id) {
}
```

## 使用示例

### 标准 JavaDoc 格式示例

```java
/**
 * 用户管理控制器
 * 
 * <p>提供用户相关的 REST API 接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>创建新用户</li>
 *   <li>根据 ID 查询用户信息</li>
 *   <li>更新用户信息</li>
 *   <li>删除用户</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    /**
     * 用户服务接口
     * 
     * <p>用于处理用户相关的业务逻辑
     */
    private final UserService userService;
    
    /**
     * 构造函数
     * 
     * @param userService 用户服务实例，由 Spring 容器注入
     */
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    /**
     * 创建新用户
     * 
     * <p>接收用户创建请求，验证数据后创建新用户并返回用户信息。
     * 
     * @param request 用户创建请求对象，包含用户名、邮箱、密码等信息
     * @return 创建成功的用户信息 DTO
     * @throws IllegalArgumentException 当请求参数不合法时抛出
     * @throws BusinessException 当用户名或邮箱已存在时抛出
     */
    @PostMapping
    public UserDTO createUser(@RequestBody UserCreateRequest request) {
        return userService.createUser(request);
    }
}
```

### Java 编程规范格式示例（严格）

```java
/**
 * <p>用户管理控制器</p>
 * 
 * <p>提供用户相关的 REST API 接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。</p>
 * 
 * <p>主要功能：
 * <ul>
 *   <li>创建新用户</li>
 *   <li>根据 ID 查询用户信息</li>
 *   <li>更新用户信息</li>
 *   <li>删除用户</li>
 * </ul>
 * </p>
 * 
 * @author System
 * @since 1.0.0
 */
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    /**
     * <p>用户服务接口</p>
     * 
     * <p>用于处理用户相关的业务逻辑</p>
     */
    private final UserService userService;
    
    /**
     * <p>构造函数</p>
     * 
     * @param userService com.example.service.UserService 用户服务实例，由 Spring 容器注入
     */
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    /**
     * <p>创建新用户</p>
     * 
     * <p>接收用户创建请求，验证数据后创建新用户并返回用户信息。</p>
     * 
     * @param request com.example.dto.UserCreateRequest 用户创建请求对象，包含用户名、邮箱、密码等信息
     * @return com.example.dto.UserDTO 创建成功的用户信息 DTO
     * @exception java.lang.IllegalArgumentException 当请求参数不合法时抛出
     * @exception com.example.exception.BusinessException 当用户名或邮箱已存在时抛出
     */
    @PostMapping
    public UserDTO createUser(@RequestBody UserCreateRequest request) {
        return userService.createUser(request);
    }
}
```
