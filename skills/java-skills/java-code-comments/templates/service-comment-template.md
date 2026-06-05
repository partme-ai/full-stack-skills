# Service 类注释模板

## Service 接口注释模板

```java
/**
 * [业务领域]服务接口
 * 
 * <p>定义[业务领域]相关的业务逻辑接口，包括[主要功能列表]。
 * 本接口遵循领域驱动设计（DDD）原则，封装[业务领域]领域的核心业务逻辑。
 * 
 * <p>主要职责：
 * <ul>
 *   <li>[职责1]</li>
 *   <li>[职责2]</li>
 *   <li>[职责3]</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
public interface [Resource]Service {
}
```

## ServiceImpl 实现类注释模板

```java
/**
 * [业务领域]服务实现类
 * 
 * <p>实现 {@link [Resource]Service} 接口，提供[业务领域]相关的业务逻辑实现。
 * 本类负责处理[主要功能列表]等核心业务操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>[功能1]：包括[详细说明]</li>
 *   <li>[功能2]：包括[详细说明]</li>
 *   <li>[功能3]：包括[详细说明]</li>
 * </ul>
 * 
 * @author [作者名]
 * @since [版本号或日期]
 */
@Service
public class [Resource]ServiceImpl implements [Resource]Service {
}
```

## 字段注释模板

```java
/**
 * [依赖名称]
 * 
 * <p>用于[用途说明]
 */
private final [DependencyType] [dependencyName];
```

## 方法注释模板

### 创建方法

```java
/**
 * 创建[资源名称]
 * 
 * <p>实现[资源名称]创建的业务逻辑，包括：
 * <ol>
 *   <li>[步骤1]</li>
 *   <li>[步骤2]</li>
 *   <li>[步骤3]</li>
 * </ol>
 * 
 * @param request [资源名称]创建请求对象，包含[字段列表]等信息
 * @return 创建成功的[资源名称]信息 DTO
 * @throws IllegalArgumentException 当请求参数不合法时抛出
 * @throws BusinessException 当[业务规则]时抛出
 */
@Override
public [ResourceDTO] create[Resource]([Resource]CreateRequest request) {
}
```

### 查询方法

```java
/**
 * 根据 ID 查询[资源名称]
 * 
 * <p>根据[资源名称] ID 从数据库查询[资源名称]信息，如果[资源名称]不存在则抛出异常。
 * 
 * @param id [资源名称]唯一标识符
 * @return [资源名称]信息 DTO
 * @throws ResourceNotFoundException 当[资源名称]不存在时抛出
 */
@Override
public [ResourceDTO] findById(Long id) {
}
```

### 更新方法

```java
/**
 * 更新[资源名称]信息
 * 
 * <p>根据[资源名称] ID 和更新请求，更新[资源名称]的指定字段信息。
 * 
 * @param id [资源名称]唯一标识符
 * @param request [资源名称]更新请求对象
 * @return 更新后的[资源名称]信息 DTO
 * @throws ResourceNotFoundException 当[资源名称]不存在时抛出
 * @throws IllegalArgumentException 当更新参数不合法时抛出
 */
@Override
public [ResourceDTO] update[Resource](Long id, [Resource]UpdateRequest request) {
}
```

### 删除方法

```java
/**
 * 根据 ID 删除[资源名称]
 * 
 * <p>根据[资源名称] ID 删除指定[资源名称]，删除操作会级联删除[资源名称]相关的数据。
 * 
 * @param id [资源名称]唯一标识符
 * @throws ResourceNotFoundException 当[资源名称]不存在时抛出
 */
@Override
public void deleteById(Long id) {
}
```

## 使用示例

### Service 接口示例

```java
/**
 * 用户服务接口
 * 
 * <p>定义用户相关的业务逻辑接口，包括用户的增删改查操作。
 * 本接口遵循领域驱动设计（DDD）原则，封装用户领域的核心业务逻辑。
 * 
 * <p>主要职责：
 * <ul>
 *   <li>用户创建和注册</li>
 *   <li>用户信息查询</li>
 *   <li>用户信息更新</li>
 *   <li>用户删除</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
public interface UserService {
    
    /**
     * 创建新用户
     * 
     * <p>根据用户创建请求创建新用户，包括数据验证、密码加密等处理。
     * 
     * @param request 用户创建请求对象
     * @return 创建成功的用户信息 DTO
     * @throws IllegalArgumentException 当请求参数不合法时抛出
     * @throws BusinessException 当用户名或邮箱已存在时抛出
     */
    UserDTO createUser(UserCreateRequest request);
}
```

### ServiceImpl 实现类示例

```java
/**
 * 用户服务实现类
 * 
 * <p>实现 {@link UserService} 接口，提供用户相关的业务逻辑实现。
 * 本类负责处理用户创建、查询、更新、删除等核心业务操作。
 * 
 * <p>主要功能：
 * <ul>
 *   <li>用户创建：包括数据验证、密码加密、重复性检查</li>
 *   <li>用户查询：支持按 ID 查询和全量查询</li>
 *   <li>用户更新：支持部分字段更新</li>
 *   <li>用户删除：级联删除相关数据</li>
 * </ul>
 * 
 * @author System
 * @since 1.0.0
 */
@Service
public class UserServiceImpl implements UserService {
    
    /**
     * 用户数据访问对象
     * 
     * <p>用于执行用户相关的数据库操作
     */
    private final UserMapper userMapper;
    
    /**
     * 密码编码器
     * 
     * <p>用于对用户密码进行加密处理
     */
    private final PasswordEncoder passwordEncoder;
    
    /**
     * 构造函数
     * 
     * @param userMapper 用户数据访问对象，由 Spring 容器注入
     * @param passwordEncoder 密码编码器，由 Spring 容器注入
     */
    public UserServiceImpl(UserMapper userMapper, PasswordEncoder passwordEncoder) {
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
    }
    
    /**
     * 创建新用户
     * 
     * <p>实现用户创建的业务逻辑，包括：
     * <ol>
     *   <li>验证用户名是否已存在</li>
     *   <li>验证邮箱是否已存在</li>
     *   <li>对密码进行加密处理</li>
     *   <li>创建用户实体并保存到数据库</li>
     *   <li>转换为 DTO 返回</li>
     * </ol>
     * 
     * @param request 用户创建请求对象，包含用户名、邮箱、密码等信息
     * @return 创建成功的用户信息 DTO
     * @throws IllegalArgumentException 当请求参数不合法时抛出
     * @throws BusinessException 当用户名或邮箱已存在时抛出
     */
    @Override
    public UserDTO createUser(UserCreateRequest request) {
        // 实现代码
    }
}
```
