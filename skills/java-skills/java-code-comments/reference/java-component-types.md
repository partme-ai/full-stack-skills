# Java 组件类型参考

## 概述

本文档说明常见的 Java 组件类型及其特点，帮助正确识别和注释不同类型的组件。

## Controller 层

### 特点

- 位于 `controller` 或 `web` 包下
- 通常以 `Controller` 结尾
- 使用 `@RestController` 或 `@Controller` 注解
- 处理 HTTP 请求和响应
- 调用 Service 层处理业务逻辑

### 注释要点

- 说明处理的资源类型（如：用户、订单）
- 说明遵循的 RESTful 规范
- 列出主要的 API 端点
- 方法注释包含 HTTP 方法、路径、参数、返回值

### 示例命名

- `UserController`
- `OrderController`
- `ProductController`

## Service 层

### Service 接口

#### 特点

- 位于 `service` 包下
- 通常以 `Service` 结尾
- 定义业务逻辑接口
- 不包含实现代码

#### 注释要点

- 说明服务的职责和业务领域
- 说明遵循的设计原则（如：DDD）
- 列出主要功能点
- 方法注释说明业务逻辑

### ServiceImpl 实现类

#### 特点

- 位于 `service.impl` 包下
- 通常以 `ServiceImpl` 结尾
- 实现 Service 接口
- 使用 `@Service` 注解
- 调用 Mapper 层访问数据库

#### 注释要点

- 说明实现类的职责
- 描述实现的主要功能
- 字段注释说明依赖关系
- 方法注释详细说明实现逻辑

### 示例命名

- `UserService` / `UserServiceImpl`
- `OrderService` / `OrderServiceImpl`

## Mapper 层

### 特点

- 位于 `mapper` 或 `dao` 包下
- 通常以 `Mapper` 或 `Dao` 结尾
- 使用 MyBatis 或 MyBatis-Plus
- 使用 `@Mapper` 注解
- 定义数据库操作方法

### 注释要点

- 说明对应的数据库表
- 说明使用的 ORM 框架
- 方法注释说明 SQL 操作类型
- 参数和返回值说明

### 示例命名

- `UserMapper`
- `OrderMapper`
- `ProductMapper`

## Entity 层

### 特点

- 位于 `entity` 或 `model` 包下
- 对应数据库表
- 使用 JPA 或 MyBatis-Plus 注解
- 包含实体字段和 getter/setter

### 注释要点

- 说明对应的数据库表
- 说明使用的 ORM 框架
- 字段注释说明数据库字段映射
- 说明字段的约束和类型

### 示例命名

- `User`
- `Order`
- `Product`

## DTO (Data Transfer Object)

### 特点

- 位于 `dto` 包下
- 通常以 `DTO` 结尾
- 用于数据传输
- 不包含业务逻辑

### 注释要点

- 说明数据传输的用途
- 说明来源和目标
- 字段注释说明数据含义

### 示例命名

- `UserDTO`
- `OrderDTO`
- `UserCreateRequest`
- `UserUpdateRequest`

## VO (Value Object / View Object)

### 特点

- 位于 `vo` 包下
- 通常以 `VO` 结尾
- 用于视图展示
- 可能包含格式化后的数据

### 注释要点

- 说明视图展示的用途
- 说明数据格式和展示方式

### 示例命名

- `UserVO`
- `OrderVO`

## BO (Business Object)

### 特点

- 位于 `bo` 包下
- 通常以 `BO` 结尾
- 封装业务逻辑对象
- 可能包含业务规则

### 注释要点

- 说明业务对象的职责
- 说明包含的业务规则
- 字段注释说明业务含义

### 示例命名

- `UserBO`
- `OrderBO`

## Repository 层

### 特点

- 位于 `repository` 包下
- 通常以 `Repository` 结尾
- 使用 Spring Data JPA
- 继承 `JpaRepository` 或 `CrudRepository`

### 注释要点

- 说明管理的实体类型
- 说明提供的查询方法

### 示例命名

- `UserRepository`
- `OrderRepository`

## Configuration 类

### 特点

- 位于 `config` 包下
- 通常以 `Config` 结尾
- 使用 `@Configuration` 注解
- 定义 Spring Bean

### 注释要点

- 说明配置的用途
- 说明配置的组件或功能

### 示例命名

- `WebConfig`
- `SecurityConfig`
- `DatabaseConfig`

## Component 类

### 特点

- 位于 `component` 或 `util` 包下
- 使用 `@Component` 注解
- 提供通用功能

### 注释要点

- 说明组件的功能
- 说明使用场景

### 示例命名

- `EmailComponent`
- `FileComponent`

## Utility 类

### 特点

- 位于 `util` 或 `utils` 包下
- 通常以 `Util` 或 `Utils` 结尾
- 包含静态方法
- 提供工具函数

### 注释要点

- 说明工具类的用途
- 方法注释说明工具函数的功能

### 示例命名

- `StringUtil`
- `DateUtil`
- `JsonUtil`

## Exception 类

### 特点

- 位于 `exception` 包下
- 通常以 `Exception` 结尾
- 继承 `Exception` 或 `RuntimeException`
- 定义自定义异常

### 注释要点

- 说明异常的使用场景
- 说明异常的含义和处理方式

### 示例命名

- `BusinessException`
- `ResourceNotFoundException`
- `ValidationException`

## 识别规则

### 通过包名识别

- `controller` / `web` → Controller
- `service` → Service
- `service.impl` → ServiceImpl
- `mapper` / `dao` → Mapper
- `entity` / `model` → Entity
- `dto` → DTO
- `vo` → VO
- `bo` → BO
- `repository` → Repository
- `config` → Configuration
- `component` / `util` → Component / Utility
- `exception` → Exception

### 通过类名识别

- `*Controller` → Controller
- `*Service` → Service
- `*ServiceImpl` → ServiceImpl
- `*Mapper` / `*Dao` → Mapper
- `*DTO` → DTO
- `*VO` → VO
- `*BO` → BO
- `*Repository` → Repository
- `*Config` → Configuration
- `*Util` / `*Utils` → Utility
- `*Exception` → Exception

### 通过注解识别

- `@RestController` / `@Controller` → Controller
- `@Service` → Service
- `@Mapper` → Mapper
- `@Entity` → Entity
- `@Repository` → Repository
- `@Configuration` → Configuration
- `@Component` → Component

## 注释优先级

根据组件类型，注释的优先级：

1. **Controller** - 高优先级（对外接口，需要详细说明）
2. **Service** - 高优先级（核心业务逻辑）
3. **ServiceImpl** - 高优先级（业务实现）
4. **Entity** - 中优先级（数据模型）
5. **Mapper** - 中优先级（数据访问）
6. **DTO/VO/BO** - 低优先级（数据传输对象）
7. **Utility** - 低优先级（工具类）
