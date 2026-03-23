# 架构目录快速参考

本文档提供不同架构类型下，各种对象类型的快速目录映射参考。

## 快速查找表

### Entity（实体类）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/entity/` |
| DDD | `{package}/domain/model/aggregate/{entity}/` 或 `{package}/domain/model/entity/` |
| 六边形 | `{package}/domain/model/entity/` |
| 整洁 | `{package}/domain/entity/` |
| COLA | `{package}/domain/model/entity/` |

### Mapper（数据访问接口）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/mapper/` |
| DDD | `{package}/domain/repository/`（仓储接口）<br>`{package}/infrastructure/persistence/mapper/`（MyBatis Mapper） |
| 六边形 | `{package}/application/ports/outbound/`（端口接口）<br>`{package}/infrastructure/adapter/outbound/persistence/mapper/`（MyBatis Mapper） |
| 整洁 | `{package}/application/ports/output/` 或 `{package}/domain/repository/`（接口）<br>`{package}/infrastructure/persistence/mapper/`（MyBatis Mapper） |
| COLA | `{package}/domain/repository/` |

### Service（服务接口）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/service/` |
| DDD | `{package}/application/service/` |
| 六边形 | `{package}/application/ports/inbound/` |
| 整洁 | `{package}/application/usecase/{entity}/` |
| COLA | `{package}/application/service/` |

### ServiceImpl（服务实现类）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/service/impl/` |
| DDD | `{package}/application/service/impl/` |
| 六边形 | `{package}/application/services/` |
| 整洁 | `{package}/application/service/` |
| COLA | `{package}/application/service/impl/` |

### Controller（控制器）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/controller/` |
| DDD | `{package}/interfaces/web/controller/` |
| 六边形 | `{package}/infrastructure/adapter/inbound/web/controller/` |
| 整洁 | `{package}/infrastructure/web/controller/` |
| COLA | `{package}/adapter/web/controller/` |

### DTO（数据传输对象）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/dto/` |
| DDD | Request: `{package}/interfaces/web/dto/request/`<br>Response: `{package}/interfaces/web/dto/response/` |
| 六边形 | `{package}/infrastructure/adapter/inbound/web/dto/` |
| 整洁 | `{package}/infrastructure/web/dto/` 或 `{package}/application/dto/` |
| COLA | `{package}/adapter/web/dto/` 或 `{package}/application/model/dto/` |

### VO（视图对象）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/vo/` |
| DDD | `{package}/interfaces/web/dto/response/` |
| 六边形 | `{package}/infrastructure/adapter/inbound/web/dto/` |
| 整洁 | `{package}/infrastructure/web/dto/` |
| COLA | `{package}/adapter/web/dto/` |

### BO（业务对象）

| 架构类型 | 目录路径 |
|:--------|:---------|
| MVC | `{package}/bo/` |
| DDD | `{package}/application/dto/` |
| 六边形 | `{package}/application/dto/` |
| 整洁 | `{package}/application/dto/` |
| COLA | `{package}/application/model/dto/` |

### Persistence Entity（持久化实体）

**注意**：仅在 DDD、六边形、整洁架构中需要区分领域实体和持久化实体。

| 架构类型 | 目录路径 |
|:--------|:---------|
| DDD | `{package}/infrastructure/persistence/entity/` |
| 六边形 | `{package}/infrastructure/adapter/outbound/persistence/entity/` |
| 整洁 | `{package}/infrastructure/persistence/entity/` |

### Repository Implementation（仓储实现）

| 架构类型 | 目录路径 |
|:--------|:---------|
| DDD | `{package}/infrastructure/persistence/repository/` |
| 六边形 | `{package}/infrastructure/adapter/outbound/persistence/repositoryimpl/` |
| 整洁 | `{package}/infrastructure/persistence/repository/` |

## 完整路径示例

假设基础包路径为 `com.example.order`，表名为 `user`：

### MVC 架构

```
src/main/java/com/example/order/
├── entity/User.java
├── mapper/UserMapper.java
├── service/UserService.java
├── service/impl/UserServiceImpl.java
├── controller/UserController.java
└── dto/UserCreateDTO.java
```

### DDD 架构

```
src/main/java/com/example/order/
├── domain/
│   ├── model/aggregate/user/User.java
│   └── repository/UserRepository.java
├── application/
│   ├── service/UserApplicationService.java
│   └── service/impl/UserApplicationServiceImpl.java
├── interfaces/web/
│   ├── controller/UserController.java
│   └── dto/
│       ├── request/UserCreateRequest.java
│       └── response/UserResponse.java
└── infrastructure/persistence/
    ├── entity/UserEntity.java
    └── mapper/UserMapper.java
```

### 六边形架构

```
src/main/java/com/example/order/
├── domain/model/entity/User.java
├── application/
│   ├── ports/
│   │   ├── inbound/IUserService.java
│   │   └── outbound/IUserRepository.java
│   └── services/UserServiceImpl.java
└── infrastructure/adapter/
    ├── inbound/web/
    │   ├── controller/UserController.java
    │   └── dto/UserRequest.java
    └── outbound/persistence/
        ├── repositoryimpl/UserRepositoryImpl.java
        ├── mapper/UserMapper.java
        └── entity/UserEntity.java
```

### 整洁架构

```
src/main/java/com/example/order/
├── domain/entity/User.java
├── application/
│   ├── usecase/user/CreateUserUseCase.java
│   ├── ports/output/UserOutputPort.java
│   └── service/UserApplicationService.java
└── infrastructure/
    ├── persistence/
    │   ├── repository/UserRepositoryImpl.java
    │   ├── mapper/UserMapper.java
    │   └── entity/UserEntity.java
    └── web/
        ├── controller/UserController.java
        └── dto/UserWebRequest.java
```

### COLA V5 架构

```
src/main/java/com/example/order/
├── domain/
│   ├── model/entity/User.java
│   └── repository/UserRepository.java
├── application/
│   ├── executor/
│   │   ├── command/user/UserCreateCmdExe.java
│   │   └── query/user/UserGetQryExe.java
│   ├── service/UserAppService.java
│   └── service/impl/UserAppServiceImpl.java
└── adapter/web/
    ├── controller/UserController.java
    └── dto/UserCreateRequest.java
```

## 使用步骤

1. **确认架构类型**（从 Step 2 获取）
2. **确认基础包路径**（从 Step 1 获取）
3. **查找对象类型**（Entity、Mapper、Service 等）
4. **使用上表查找对应目录路径**
5. **构建完整路径**：`src/main/java/{package}/{目录路径}/{ClassName}.java`
6. **验证目录存在**，不存在则创建
7. **生成文件**

## 注意事项

1. **领域实体 vs 持久化实体**：
   - DDD、六边形、整洁架构需要区分
   - 领域实体包含业务逻辑，放在领域层
   - 持久化实体是数据库映射，放在基础设施层

2. **Mapper 接口位置**：
   - 在 DDD、六边形、整洁架构中，通常有两个位置：
     - 仓储接口（领域层定义）
     - MyBatis Mapper（基础设施层实现）

3. **DTO 分类**：
   - DDD 架构中，Request 和 Response 分开存放
   - 其他架构可能统一放在一个目录

4. **包路径转换**：
   - 包路径使用点分隔：`com.example.order`
   - 文件路径使用斜杠分隔：`com/example/order/`
   - 基础路径：`src/main/java/`

## 参考文档

- 详细示例：`examples/architecture-directory-mapping.md`
- DDD 架构参考：`../ddd4j-project-creator/docs/1、DDD 经典分层架构目录结构.md`
- 六边形架构参考：`../ddd4j-project-creator/docs/2、六边形架构详细目录结构参考.md`
- 整洁架构参考：`../ddd4j-project-creator/docs/3、整洁架构详细目录结构参考.md`
- COLA V5 架构参考：`../ddd4j-project-creator/docs/4、COLA V5 架构详细目录结构参考.md`
