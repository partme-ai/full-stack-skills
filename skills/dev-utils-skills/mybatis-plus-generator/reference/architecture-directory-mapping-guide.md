# 架构目录映射指南

本文档提供不同架构类型下，MyBatis-Plus Generator 生成代码的详细目录映射指南。

## 概述

根据选择的架构类型，生成的代码需要放在不同的目录结构中。本指南详细说明了 5 种常见架构的目录映射规则。

## 1. 传统 MVC (Model-View-Controller)

**Directory Structure:**
```
src/main/java/{package}/
├── entity/          # Entity 实体类
├── mapper/           # Mapper 接口
├── service/          # Service 接口
├── service/impl/     # ServiceImpl 实现类
├── controller/       # Controller 控制器
└── dto/              # DTO（可选）
```

**Mapping:**
- Entity → `{package}/entity/`
- Mapper → `{package}/mapper/`
- Service → `{package}/service/`
- ServiceImpl → `{package}/service/impl/`
- Controller → `{package}/controller/`
- DTO → `{package}/dto/` (if needed)

## 2. DDD (领域驱动设计)

**Directory Structure:**
```
src/main/java/{package}/
├── domain/                          # 领域层
│   ├── model/                       # 领域模型
│   │   ├── aggregate/               # 聚合
│   │   │   └── {entity}/            # 聚合根（Entity）
│   │   └── valueobject/            # 值对象
│   ├── repository/                  # 仓储接口（Mapper）
│   └── service/                      # 领域服务
├── application/                      # 应用层
│   ├── service/                     # 应用服务（Service）
│   │   └── impl/                    # 应用服务实现（ServiceImpl）
│   └── dto/                         # 应用层DTO
├── interfaces/                       # 接口层
│   ├── web/                         # Web接口
│   │   ├── controller/              # Controller
│   │   └── dto/                     # Web DTO
│   │       ├── request/             # 请求DTO
│   │       └── response/            # 响应DTO（VO）
│   └── assembler/                   # DTO装配器
└── infrastructure/                  # 基础设施层
    └── persistence/                  # 持久化实现
        ├── repository/               # 仓储实现（Mapper实现）
        └── entity/                   # 持久化实体（Entity）
```

**Mapping:**
- Entity (Domain Model) → `{package}/domain/model/aggregate/{entity}/` 或 `{package}/domain/model/entity/`
- Mapper (Repository Interface) → `{package}/domain/repository/`
- Service (Application Service) → `{package}/application/service/`
- ServiceImpl → `{package}/application/service/impl/`
- Controller → `{package}/interfaces/web/controller/`
- DTO (Request) → `{package}/interfaces/web/dto/request/`
- VO (Response) → `{package}/interfaces/web/dto/response/`
- BO (Application DTO) → `{package}/application/dto/`

**Note**: In DDD architecture, Entity is a domain model (aggregate root), not a persistence entity. The persistence entity should be placed in `infrastructure/persistence/entity/`.

## 3. 六边形架构 (Hexagonal Architecture / Ports and Adapters)

**Directory Structure:**
```
src/main/java/{package}/
├── application/                      # 应用层
│   ├── ports/                        # 端口定义
│   │   ├── inbound/                 # 入站端口（Service接口）
│   │   └── outbound/                 # 出站端口（Repository接口）
│   ├── services/                     # 应用服务实现（ServiceImpl）
│   └── usecases/                     # 用例
├── domain/                           # 领域层
│   ├── model/                        # 领域模型（Entity）
│   │   ├── entity/                   # 实体
│   │   └── valueobject/             # 值对象
│   └── service/                      # 领域服务
└── infrastructure/                   # 基础设施层
    ├── adapter/                      # 适配器
    │   ├── inbound/                  # 入站适配器
    │   │   └── web/                  # Web适配器
    │   │       ├── controller/       # Controller
    │   │       └── dto/              # Web DTO
    │   └── outbound/                  # 出站适配器
    │       ├── persistence/          # 持久化适配器
    │       │   ├── repositoryimpl/   # Repository实现（Mapper实现）
    │       │   ├── mapper/           # MyBatis Mapper
    │       │   └── entity/           # 持久化实体
    │       └── external/             # 外部服务适配器
```

**Mapping:**
- Entity (Domain Model) → `{package}/domain/model/entity/`
- Mapper (Repository Interface) → `{package}/application/ports/outbound/`
- Service (Application Port) → `{package}/application/ports/inbound/`
- ServiceImpl → `{package}/application/services/`
- Controller → `{package}/infrastructure/adapter/inbound/web/controller/`
- DTO → `{package}/infrastructure/adapter/inbound/web/dto/`
- Persistence Entity → `{package}/infrastructure/adapter/outbound/persistence/entity/`
- Repository Implementation → `{package}/infrastructure/adapter/outbound/persistence/repositoryimpl/`

## 4. 整洁架构 (Clean Architecture)

**Directory Structure:**
```
src/main/java/{package}/
├── domain/                           # 领域层（最内层）
│   ├── entity/                       # 业务实体（Entity）
│   ├── valueobject/                  # 值对象
│   ├── repository/                   # 仓储接口（Mapper接口）
│   └── service/                      # 领域服务
├── application/                      # 应用层
│   ├── usecase/                      # 用例（Service）
│   │   └── {entity}/                 # 按实体分组
│   ├── ports/                        # 端口
│   │   ├── input/                    # 输入端口
│   │   └── output/                   # 输出端口（Repository接口）
│   ├── service/                      # 应用服务（ServiceImpl）
│   └── dto/                          # 应用层DTO
└── infrastructure/                   # 基础设施层（最外层）
    ├── persistence/                  # 持久化实现
    │   ├── repository/               # 仓储实现（Mapper实现）
    │   ├── mapper/                   # MyBatis Mapper
    │   └── entity/                   # 持久化实体
    └── web/                          # Web层实现
        ├── controller/               # Controller
        └── dto/                      # Web DTO
```

**Mapping:**
- Entity (Domain Entity) → `{package}/domain/entity/`
- Mapper (Repository Interface) → `{package}/application/ports/output/` 或 `{package}/domain/repository/`
- Service (Use Case) → `{package}/application/usecase/{entity}/`
- ServiceImpl → `{package}/application/service/`
- Controller → `{package}/infrastructure/web/controller/`
- DTO → `{package}/infrastructure/web/dto/` 或 `{package}/application/dto/`
- Persistence Entity → `{package}/infrastructure/persistence/entity/`
- Repository Implementation → `{package}/infrastructure/persistence/repository/`

## 5. COLA V5 架构

**Directory Structure:**
```
src/main/java/{package}/
├── domain/                           # 领域层
│   ├── model/                        # 领域模型
│   │   ├── entity/                   # 实体（Entity）
│   │   └── valueobject/             # 值对象
│   ├── repository/                   # 仓储接口（Mapper接口）
│   ├── gateway/                      # 领域网关接口
│   ├── service/                      # 领域服务
│   └── ability/                      # 领域能力
├── application/                      # 应用层
│   ├── executor/                     # 执行器（CQRS）
│   │   ├── command/                  # 命令执行器
│   │   └── query/                    # 查询执行器
│   ├── service/                      # 应用服务（Service）
│   │   └── impl/                     # 应用服务实现（ServiceImpl）
│   └── model/                        # 应用模型
│       ├── command/                  # 命令对象
│       ├── query/                     # 查询对象
│       └── dto/                       # 应用DTO
└── adapter/                          # 适配器层
    ├── web/                          # Web适配器
    │   ├── controller/               # Controller
    │   └── dto/                      # Web DTO
    ├── rpc/                          # RPC适配器
    └── message/                      # 消息适配器
```

**Mapping:**
- Entity → `{package}/domain/model/entity/`
- Mapper (Repository Interface) → `{package}/domain/repository/`
- Service (Application Service) → `{package}/application/service/`
- ServiceImpl → `{package}/application/service/impl/`
- Controller → `{package}/adapter/web/controller/`
- DTO → `{package}/adapter/web/dto/` 或 `{package}/application/model/dto/`
- Command Executor → `{package}/application/executor/command/{entity}/`
- Query Executor → `{package}/application/executor/query/{entity}/`

## 如何确定输出目录

### 步骤 1: 确认基础包路径

询问用户：
```
请提供项目的基础包路径（例如：com.example.order）
```

### 步骤 2: 根据架构类型构建路径

根据架构类型和基础包路径，构建完整的文件路径：

**示例：**
- 架构：DDD
- 基础包：`com.example.order`
- 表名：`user`
- Entity 路径：`src/main/java/com/example/order/domain/model/aggregate/user/User.java`

### 步骤 3: 验证目录存在

在生成代码前，检查目录是否存在：
- 如果目录不存在，创建目录
- 如果目录已存在，确认是否覆盖现有文件

### 步骤 4: 生成文件

在正确的位置生成文件。

## 完整路径示例

假设基础包路径为 `com.example.order`，表名为 `user`：

- **MVC**: 
  - Entity: `src/main/java/com/example/order/entity/User.java`
  - Controller: `src/main/java/com/example/order/controller/UserController.java`

- **DDD**: 
  - Entity: `src/main/java/com/example/order/domain/model/aggregate/user/User.java`
  - Controller: `src/main/java/com/example/order/interfaces/web/controller/UserController.java`

- **Hexagonal**: 
  - Entity: `src/main/java/com/example/order/domain/model/entity/User.java`
  - Controller: `src/main/java/com/example/order/infrastructure/adapter/inbound/web/controller/UserController.java`

- **Clean**: 
  - Entity: `src/main/java/com/example/order/domain/entity/User.java`
  - Controller: `src/main/java/com/example/order/infrastructure/web/controller/UserController.java`

- **COLA**: 
  - Entity: `src/main/java/com/example/order/domain/model/entity/User.java`
  - Controller: `src/main/java/com/example/order/adapter/web/controller/UserController.java`

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

- 快速参考表：`architecture-directory-quick-reference.md`
- 详细示例：`../examples/architecture-directory-mapping.md`
- DDD 架构参考：`../../ddd4j-project-creator/docs/1、DDD 经典分层架构目录结构.md`
- 六边形架构参考：`../../ddd4j-project-creator/docs/2、六边形架构详细目录结构参考.md`
- 整洁架构参考：`../../ddd4j-project-creator/docs/3、整洁架构详细目录结构参考.md`
- COLA V5 架构参考：`../../ddd4j-project-creator/docs/4、COLA V5 架构详细目录结构参考.md`
