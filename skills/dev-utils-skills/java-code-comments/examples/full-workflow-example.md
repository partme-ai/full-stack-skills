# 完整工作流程示例

## 场景

为一个完整的 Spring Boot 项目添加代码注释，包括 Controller、Service、ServiceImpl、Mapper、Entity 等组件。

## 工作流程

### Step 1: 扫描和理解代码库

**执行操作：**
1. 扫描项目中的所有 Java 文件
2. 读取 README.md 和架构文档
3. 理解项目结构和业务逻辑

**输出示例：**

```
## 代码库分析结果

### 项目结构
- 项目类型：Spring Boot 2.7.x
- 架构模式：MVC + DDD
- 数据库：MySQL + MyBatis-Plus

### 识别的组件类型
- Controller: 5 个类
  - UserController
  - OrderController
  - ProductController
  - PaymentController
  - AuthController

- Service: 5 个接口
  - UserService
  - OrderService
  - ProductService
  - PaymentService
  - AuthService

- ServiceImpl: 5 个实现类
  - UserServiceImpl
  - OrderServiceImpl
  - ProductServiceImpl
  - PaymentServiceImpl
  - AuthServiceImpl

- Mapper: 5 个接口
  - UserMapper
  - OrderMapper
  - ProductMapper
  - PaymentMapper
  - AuthMapper

- Entity: 5 个实体类
  - User
  - Order
  - Product
  - Payment
  - AuthToken

### 业务领域
- 用户管理：用户注册、登录、信息管理
- 订单管理：订单创建、查询、更新、取消
- 商品管理：商品信息管理
- 支付管理：支付处理
- 认证授权：JWT 令牌管理
```

### Step 2: 确认组件类型

**向用户展示选择列表：**

```
请确认需要进行代码注释的分类（可多选）：

- [x] Controller（控制器）
- [x] Service（服务接口）
- [x] ServiceImpl（服务实现）
- [x] Mapper（数据访问层）
- [ ] Model（数据模型）
- [x] Entity（实体类）
- [ ] BO（业务对象）
- [ ] DTO（数据传输对象）
- [ ] VO（视图对象）

请确认需要进行注释的类型：
- [x] 类注释（Class-level comments）
- [x] 方法注释（Method-level comments）
- [x] 属性注释（Field-level comments）
```

**用户确认后继续。**

### Step 3: 创建 Todo 清单

**生成的 Todo 清单：**

```markdown
## Todo List: Java Code Comments

### Controller 层
- [ ] UserController
  - [ ] 类注释
  - [ ] createUser() - 方法注释
  - [ ] getUserById() - 方法注释
  - [ ] updateUser() - 方法注释
  - [ ] deleteUser() - 方法注释
  - [ ] userService - 属性注释

- [ ] OrderController
  - [ ] 类注释
  - [ ] createOrder() - 方法注释
  - [ ] getOrderById() - 方法注释
  - [ ] cancelOrder() - 方法注释
  - [ ] orderService - 属性注释

### Service 层
- [ ] UserService
  - [ ] 类注释
  - [ ] createUser() - 方法注释
  - [ ] findById() - 方法注释
  - [ ] updateUser() - 方法注释
  - [ ] deleteById() - 方法注释

- [ ] OrderService
  - [ ] 类注释
  - [ ] createOrder() - 方法注释
  - [ ] findById() - 方法注释
  - [ ] cancelOrder() - 方法注释

### ServiceImpl 层
- [ ] UserServiceImpl
  - [ ] 类注释
  - [ ] createUser() - 方法注释
  - [ ] findById() - 方法注释
  - [ ] updateUser() - 方法注释
  - [ ] deleteById() - 方法注释
  - [ ] userMapper - 属性注释
  - [ ] passwordEncoder - 属性注释

- [ ] OrderServiceImpl
  - [ ] 类注释
  - [ ] createOrder() - 方法注释
  - [ ] findById() - 方法注释
  - [ ] cancelOrder() - 方法注释
  - [ ] orderMapper - 属性注释

### Mapper 层
- [ ] UserMapper
  - [ ] 类注释
  - [ ] insert() - 方法注释
  - [ ] selectById() - 方法注释
  - [ ] updateById() - 方法注释
  - [ ] deleteById() - 方法注释

- [ ] OrderMapper
  - [ ] 类注释
  - [ ] insert() - 方法注释
  - [ ] selectById() - 方法注释
  - [ ] updateById() - 方法注释

### Entity 层
- [ ] User
  - [ ] 类注释
  - [ ] id - 属性注释
  - [ ] username - 属性注释
  - [ ] email - 属性注释
  - [ ] password - 属性注释
  - [ ] status - 属性注释
  - [ ] createTime - 属性注释
  - [ ] updateTime - 属性注释

- [ ] Order
  - [ ] 类注释
  - [ ] id - 属性注释
  - [ ] userId - 属性注释
  - [ ] totalAmount - 属性注释
  - [ ] status - 属性注释
  - [ ] createTime - 属性注释
```

### Step 4: 执行注释工作

**按顺序处理每个类：**

#### 处理 UserController

**1. 添加类注释：**

```java
/**
 * 用户管理控制器
 * 
 * <p>提供用户相关的 REST API 接口，包括用户的创建、查询、更新和删除操作。
 * 本控制器遵循 RESTful 设计规范，使用标准的 HTTP 方法进行资源操作。
 * 
 * @author System
 * @since 1.0.0
 */
@RestController
@RequestMapping("/api/users")
public class UserController {
```

**2. 添加方法注释：**

```java
/**
 * 创建新用户
 * 
 * @param request 用户创建请求对象
 * @return 创建成功的用户信息 DTO
 * @throws IllegalArgumentException 当请求参数不合法时抛出
 */
@PostMapping
public UserDTO createUser(@RequestBody UserCreateRequest request) {
    return userService.createUser(request);
}
```

**3. 添加属性注释：**

```java
/**
 * 用户服务接口
 * 
 * <p>用于处理用户相关的业务逻辑
 */
private final UserService userService;
```

**4. 更新 Todo 清单：**

```markdown
### Controller 层
- [x] UserController
  - [x] 类注释
  - [x] createUser() - 方法注释
  - [x] getUserById() - 方法注释
  - [x] updateUser() - 方法注释
  - [x] deleteUser() - 方法注释
  - [x] userService - 属性注释

- [ ] OrderController
  ...
```

**继续处理下一个类，直到所有类都完成。**

## 最终结果

所有组件都已添加完整的 JavaDoc 注释：
- ✅ 5 个 Controller 类
- ✅ 5 个 Service 接口
- ✅ 5 个 ServiceImpl 实现类
- ✅ 5 个 Mapper 接口
- ✅ 5 个 Entity 类

所有注释都遵循 JavaDoc 规范，包含完整的类、方法和字段说明。
