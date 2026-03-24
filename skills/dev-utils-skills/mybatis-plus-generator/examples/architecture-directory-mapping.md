# 架构目录映射示例

本文档提供不同架构类型下，MyBatis-Plus Generator 生成代码的目录映射示例。

## 示例场景

假设我们有一个 `user` 表，需要生成相关代码，基础包路径为 `com.example.order`。

## 1. 传统 MVC 架构

### 目录结构

```
src/main/java/com/example/order/
├── entity/
│   └── User.java                    # Entity 实体类
├── mapper/
│   └── UserMapper.java             # Mapper 接口
├── service/
│   ├── UserService.java            # Service 接口
│   └── impl/
│       └── UserServiceImpl.java    # ServiceImpl 实现类
├── controller/
│   └── UserController.java         # Controller 控制器
└── dto/
    ├── UserCreateDTO.java          # 创建用户DTO
    ├── UserUpdateDTO.java          # 更新用户DTO
    └── UserQueryDTO.java           # 查询用户DTO
```

### 文件路径示例

- Entity: `src/main/java/com/example/order/entity/User.java`
- Mapper: `src/main/java/com/example/order/mapper/UserMapper.java`
- Service: `src/main/java/com/example/order/service/UserService.java`
- ServiceImpl: `src/main/java/com/example/order/service/impl/UserServiceImpl.java`
- Controller: `src/main/java/com/example/order/controller/UserController.java`
- DTO: `src/main/java/com/example/order/dto/UserCreateDTO.java`

## 2. DDD (领域驱动设计) 架构

### 目录结构

```
src/main/java/com/example/order/
├── domain/                          # 领域层
│   ├── model/
│   │   ├── aggregate/
│   │   │   └── user/
│   │   │       └── User.java       # 聚合根（领域实体）
│   │   └── valueobject/
│   │       ├── UserId.java
│   │       └── Email.java
│   └── repository/
│       └── UserRepository.java     # 仓储接口（Mapper接口）
├── application/                     # 应用层
│   ├── service/
│   │   ├── UserApplicationService.java      # 应用服务接口
│   │   └── impl/
│   │       └── UserApplicationServiceImpl.java  # 应用服务实现
│   └── dto/
│       └── UserDTO.java            # 应用层DTO
├── interfaces/                      # 接口层
│   └── web/
│       ├── controller/
│       │   └── UserController.java # Controller
│       └── dto/
│           ├── request/
│           │   ├── UserCreateRequest.java
│           │   └── UserUpdateRequest.java
│           └── response/
│               └── UserResponse.java  # VO（视图对象）
│       └── assembler/
│           └── UserAssembler.java  # DTO装配器
└── infrastructure/                  # 基础设施层
    └── persistence/
        ├── repository/
        │   └── JpaUserRepository.java  # 仓储实现
        ├── mapper/
        │   └── UserMapper.java      # MyBatis Mapper
        └── entity/
            └── UserEntity.java      # 持久化实体
```

### 文件路径示例

- Domain Entity: `src/main/java/com/example/order/domain/model/aggregate/user/User.java`
- Repository Interface: `src/main/java/com/example/order/domain/repository/UserRepository.java`
- Application Service: `src/main/java/com/example/order/application/service/UserApplicationService.java`
- Application Service Impl: `src/main/java/com/example/order/application/service/impl/UserApplicationServiceImpl.java`
- Controller: `src/main/java/com/example/order/interfaces/web/controller/UserController.java`
- Request DTO: `src/main/java/com/example/order/interfaces/web/dto/request/UserCreateRequest.java`
- Response VO: `src/main/java/com/example/order/interfaces/web/dto/response/UserResponse.java`
- Persistence Entity: `src/main/java/com/example/order/infrastructure/persistence/entity/UserEntity.java`
- Mapper: `src/main/java/com/example/order/infrastructure/persistence/mapper/UserMapper.java`

### 注意事项

在 DDD 架构中：
- **领域实体（User）** 是业务模型，放在 `domain/model/aggregate/` 或 `domain/model/entity/`
- **持久化实体（UserEntity）** 是技术实现，放在 `infrastructure/persistence/entity/`
- **Mapper 接口** 在领域层定义（`domain/repository/`），在基础设施层实现（`infrastructure/persistence/mapper/`）

## 3. 六边形架构 (Hexagonal Architecture)

### 目录结构

```
src/main/java/com/example/order/
├── application/                     # 应用层
│   ├── ports/
│   │   ├── inbound/
│   │   │   └── IUserService.java   # 入站端口（Service接口）
│   │   └── outbound/
│   │       └── IUserRepository.java # 出站端口（Repository接口）
│   ├── services/
│   │   └── UserServiceImpl.java    # 应用服务实现
│   └── usecases/
│       └── user/
│           └── CreateUserUseCase.java
├── domain/                          # 领域层
│   ├── model/
│   │   ├── entity/
│   │   │   └── User.java          # 领域实体
│   │   └── valueobject/
│   │       └── Email.java
│   └── service/
│       └── UserDomainService.java
└── infrastructure/                  # 基础设施层
    └── adapter/
        ├── inbound/                 # 入站适配器
        │   └── web/
        │       ├── controller/
        │       │   └── UserController.java  # Controller
        │       └── dto/
        │           ├── CreateUserRequest.java
        │           └── UserResponse.java
        └── outbound/                # 出站适配器
            └── persistence/
                ├── repositoryimpl/
                │   └── UserRepositoryImpl.java  # Repository实现
                ├── mapper/
                │   └── UserMapper.java         # MyBatis Mapper
                └── entity/
                    └── UserEntity.java         # 持久化实体
```

### 文件路径示例

- Domain Entity: `src/main/java/com/example/order/domain/model/entity/User.java`
- Inbound Port: `src/main/java/com/example/order/application/ports/inbound/IUserService.java`
- Outbound Port: `src/main/java/com/example/order/application/ports/outbound/IUserRepository.java`
- Service Impl: `src/main/java/com/example/order/application/services/UserServiceImpl.java`
- Controller: `src/main/java/com/example/order/infrastructure/adapter/inbound/web/controller/UserController.java`
- Repository Impl: `src/main/java/com/example/order/infrastructure/adapter/outbound/persistence/repositoryimpl/UserRepositoryImpl.java`
- Mapper: `src/main/java/com/example/order/infrastructure/adapter/outbound/persistence/mapper/UserMapper.java`
- Persistence Entity: `src/main/java/com/example/order/infrastructure/adapter/outbound/persistence/entity/UserEntity.java`

## 4. 整洁架构 (Clean Architecture)

### 目录结构

```
src/main/java/com/example/order/
├── domain/                          # 领域层（最内层）
│   ├── entity/
│   │   └── User.java               # 业务实体
│   ├── valueobject/
│   │   └── Email.java
│   ├── repository/
│   │   └── UserRepository.java     # 仓储接口
│   └── service/
│       └── UserDomainService.java
├── application/                     # 应用层
│   ├── usecase/
│   │   └── user/
│   │       ├── CreateUserUseCase.java
│   │       └── GetUserUseCase.java
│   ├── ports/
│   │   ├── input/
│   │   │   └── UserInputPort.java
│   │   └── output/
│   │       └── UserOutputPort.java  # 输出端口（Repository接口）
│   ├── service/
│   │   └── UserApplicationService.java  # 应用服务（ServiceImpl）
│   └── dto/
│       └── UserDTO.java
└── infrastructure/                  # 基础设施层（最外层）
    ├── persistence/
    │   ├── repository/
    │   │   └── UserRepositoryImpl.java  # 仓储实现
    │   ├── mapper/
    │   │   └── UserMapper.java         # MyBatis Mapper
    │   └── entity/
    │       └── UserEntity.java         # 持久化实体
    └── web/
        ├── controller/
        │   └── UserController.java     # Controller
        └── dto/
            ├── CreateUserWebRequest.java
            └── UserWebResponse.java
```

### 文件路径示例

- Domain Entity: `src/main/java/com/example/order/domain/entity/User.java`
- Repository Interface: `src/main/java/com/example/order/application/ports/output/UserOutputPort.java`
- Use Case: `src/main/java/com/example/order/application/usecase/user/CreateUserUseCase.java`
- Application Service: `src/main/java/com/example/order/application/service/UserApplicationService.java`
- Controller: `src/main/java/com/example/order/infrastructure/web/controller/UserController.java`
- Repository Impl: `src/main/java/com/example/order/infrastructure/persistence/repository/UserRepositoryImpl.java`
- Mapper: `src/main/java/com/example/order/infrastructure/persistence/mapper/UserMapper.java`
- Persistence Entity: `src/main/java/com/example/order/infrastructure/persistence/entity/UserEntity.java`

## 5. COLA V5 架构

### 目录结构

```
src/main/java/com/example/order/
├── domain/                          # 领域层
│   ├── model/
│   │   ├── entity/
│   │   │   └── User.java           # 实体
│   │   └── valueobject/
│   │       └── Email.java
│   ├── repository/
│   │   └── UserRepository.java     # 仓储接口（Mapper接口）
│   ├── gateway/
│   │   └── UserGateway.java
│   ├── service/
│   │   └── UserDomainService.java
│   └── ability/
│       └── UserAbility.java
├── application/                     # 应用层
│   ├── executor/                   # 执行器（CQRS）
│   │   ├── command/
│   │   │   └── user/
│   │   │       └── UserCreateCmdExe.java
│   │   └── query/
│   │       └── user/
│   │           └── UserGetQryExe.java
│   ├── service/
│   │   ├── UserAppService.java     # 应用服务接口
│   │   └── impl/
│   │       └── UserAppServiceImpl.java  # 应用服务实现
│   └── model/
│       ├── command/
│       │   └── UserCreateCmd.java
│       ├── query/
│       │   └── UserGetQry.java
│       └── dto/
│           └── UserDTO.java
└── adapter/                        # 适配器层
    └── web/
        ├── controller/
        │   └── UserController.java  # Controller
        └── dto/
            ├── UserCreateRequest.java
            └── UserResponse.java
```

### 文件路径示例

- Domain Entity: `src/main/java/com/example/order/domain/model/entity/User.java`
- Repository Interface: `src/main/java/com/example/order/domain/repository/UserRepository.java`
- Application Service: `src/main/java/com/example/order/application/service/UserAppService.java`
- Application Service Impl: `src/main/java/com/example/order/application/service/impl/UserAppServiceImpl.java`
- Command Executor: `src/main/java/com/example/order/application/executor/command/user/UserCreateCmdExe.java`
- Query Executor: `src/main/java/com/example/order/application/executor/query/user/UserGetQryExe.java`
- Controller: `src/main/java/com/example/order/adapter/web/controller/UserController.java`
- DTO: `src/main/java/com/example/order/adapter/web/dto/UserCreateRequest.java`

## 如何确定输出目录

### 步骤 1: 确认架构类型

在 Step 2 中，用户已经选择了架构类型。根据选择，使用对应的目录映射。

### 步骤 2: 确认基础包路径

询问用户：
```
请提供项目的基础包路径（例如：com.example.order）
```

### 步骤 3: 确认项目结构

如果项目结构不标准，询问用户：
```
请确认项目的目录结构，以便我将生成的代码放在正确的位置。

例如：
- 实体类应该放在哪个目录？
- Controller 应该放在哪个目录？
- Service 应该放在哪个目录？
```

### 步骤 4: 构建完整路径

根据架构类型和基础包路径，构建完整的文件路径：

**示例：**
- 架构：DDD
- 基础包：`com.example.order`
- 表名：`user`
- Entity 路径：`src/main/java/com/example/order/domain/model/aggregate/user/User.java`

### 步骤 5: 验证目录存在

在生成代码前，检查目录是否存在：
- 如果目录不存在，创建目录
- 如果目录已存在，确认是否覆盖现有文件

## 常见问题

### Q1: 如何区分领域实体和持久化实体？

**A**: 
- **领域实体**：业务模型，包含业务逻辑，放在领域层（`domain/`）
- **持久化实体**：数据库映射，放在基础设施层（`infrastructure/persistence/entity/`）

在 DDD、六边形、整洁架构中，通常需要生成两种实体。

### Q2: Mapper 接口应该放在哪里？

**A**: 
- **MVC**: `{package}/mapper/`
- **DDD**: 仓储接口放在 `{package}/domain/repository/`，MyBatis Mapper 放在 `{package}/infrastructure/persistence/mapper/`
- **六边形**: 端口接口放在 `{package}/application/ports/outbound/`，MyBatis Mapper 放在 `{package}/infrastructure/adapter/outbound/persistence/mapper/`
- **整洁**: 输出端口放在 `{package}/application/ports/output/`，MyBatis Mapper 放在 `{package}/infrastructure/persistence/mapper/`
- **COLA**: `{package}/domain/repository/`

### Q3: 如何确定 DTO 的位置？

**A**: 
- **MVC**: `{package}/dto/`
- **DDD**: Request DTO 放在 `{package}/interfaces/web/dto/request/`，Response VO 放在 `{package}/interfaces/web/dto/response/`
- **六边形**: `{package}/infrastructure/adapter/inbound/web/dto/`
- **整洁**: `{package}/infrastructure/web/dto/` 或 `{package}/application/dto/`
- **COLA**: `{package}/adapter/web/dto/` 或 `{package}/application/model/dto/`

### Q4: 如果项目结构不标准怎么办？

**A**: 询问用户具体的目录结构，或者让用户提供项目的目录结构示例，然后根据实际情况调整。

## 参考文档

详细的架构目录结构参考：
- DDD 经典分层架构：`reference/ddd-architecture-directory-structure.md`
- 六边形架构：`reference/hexagonal-architecture-directory-structure.md`
- 整洁架构：`reference/clean-architecture-directory-structure.md`
- COLA V5 架构：`reference/cola-v5-architecture-directory-structure.md`
