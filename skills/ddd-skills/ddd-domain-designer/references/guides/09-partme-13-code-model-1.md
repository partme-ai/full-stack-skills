# DDD 代码模型与目录结构

## 一级目录（按分层）

```
{项目名}-service/
├── interfaces/       # 用户接口层 — REST Controller, DTO, Assembler
├── application/      # 应用层 — Service 编排, 事件发布/订阅
├── domain/           # 领域层 — 聚合、实体、值对象、领域服务
└── infrastructure/   # 基础层 — DB 实现、配置、工具类
```

## 二级目录详解

### interfaces/
```
interfaces/
├── controller/       # REST Controller（接收请求 → 调用 AppService）
├── dto/              # 数据传输对象（Request/Response DTO）
└── assembler/        # DTO ↔ Domain 对象转换
```

### application/
```
application/
├── service/          # 应用服务（编排领域服务 + 外部服务）
├── event/
│   ├── publish/      # 事件发布
│   └── subscribe/    # 事件订阅（调用领域层处理）
└── command/          # Command 对象（CQRS 场景）
```

### domain/
```
domain/{聚合名}/      # 每个聚合一个独立包
├── entity/           # 聚合根、实体、值对象（充血模型）
├── service/          # 领域服务（跨实体的业务逻辑）
├── repository/       # 仓储接口（实现在 infrastructure）
└── event/            # 领域事件定义
```

### infrastructure/
```
infrastructure/
├── repository/       # 仓储实现（MyBatis/JPA 映射）
├── config/           # 配置类
├── mq/               # 消息队列
├── cache/            # 缓存
└── util/             # 通用工具类
```

## 各层代码规范

| 层 | 允许的代码 | 禁止的代码 |
|----|----------|----------|
| **interfaces** | Controller, DTO, Assembler | 业务逻辑、数据库操作 |
| **application** | 服务编排、事务、权限 | 业务 if/else，SQL 查询 |
| **domain** | 聚合根、实体、VO、领域服务、仓储接口 | Spring 注解、JPA、JDBC |
| **infrastructure** | 仓储实现、配置、客户端 | 业务规则（Domain 层不处理的） |

## 聚合边界规则

```
原则：一个聚合 = 一个独立包 = 一个仓储

禁止：
  - 聚合之间直接调用领域服务
  - 聚合间传递实体对象（只能传 ID）

允许：
  - 通过应用层编排跨聚合操作
  - 通过领域事件异步通信
```

## 微服务演进时的重组策略

```
当需要拆分聚合为新微服务时：
  1. 复制整个 {聚合名}/ 包到新微服务的 domain/
  2. 复制仓储实现到新微服务的 infrastructure/
  3. 应用层通过事件/RPC 调用新微服务
```

## 常见错误

| 错误 | 修复 |
|------|------|
| 聚合包名为 `entity`/`model`（技术名） | 改为业务名（`order`/`payment`） |
| 领域服务放在 application 层 | 移到 `domain/{聚合名}/service/` |
| 仓储实现在 domain 层 | 接口在 domain，实现在 infrastructure |
| Controller 直接调 Repository | Controller → AppService → Repository |
