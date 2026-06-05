---
name: ddd-architecture-layered
description: Comprehensive guidance for DDD Layered Architecture (DDD 四层架构) — Traditional 3-layer to DDD 4-layer transformation with Interface/Application/Domain/Infrastructure layers. Covers complete directory structure, dependency inversion, ArchUnit validation, Spring Boot integration, and step-by-step migration guide. Use when user asks about layered architecture, DDD four-layer, 分层架构, traditional layering with DDD, or needs a simple DDD entry point for small to medium teams.
license: Apache-2.0
---

# DDD Layered Architecture — 分层架构落地指南

DDD Layered Architecture 是 DDD 生态中最简的入门架构。它将传统三层（Controller/Service/DAO）重构为四层（Interface/Application/Domain/Infrastructure），通过依赖倒置使领域层成为系统核心。

## Audience — 目标用户

| 用户类型 | 特征 | 推荐入口 |
|---------|------|---------|
| **DDD 初学者** | 了解 MVC 三层，想入门 DDD | 先读 Core Principles → 看 06 单体简单示例 → 跟随 Implementation Phases |
| **架构师** | 负责项目架构选型和技术规划 | 先读 When to Use 边界 → 对照 06-12 规模谱系选型 → 看 Evolution 演进路径 |
| **高级开发者** | 有三层开发经验，需要落地分层 | 直接看 Directory Structure + Writing Rules → 使用 07/08 示例启动项目 |
| **技术负责人** | 评估团队引入 DDD 的可行性和成本 | 先读 When to Use + 场景边界 → 评估 Implementation Phases 时间 → 参考 09-12 微服务规划 |

## Workflow

```
Step 1: awesome (入门)              →  了解 DDD 概念
Step 2: selector (架构选型)         →  确认分层架构适合
Step 3: layered (分层架构) ★         ← 你在这里
Step 4: domain-designer (领域设计)  →  设计领域模型
Step 5: code-reviewer (审查)        →  分层合规检查
```

## When to Use — 场景边界

### ✅ 适用场景

| # | 场景 | 说明 |
|---|------|------|
| 1 | 团队 < 10 人，DDD 刚起步 | 学习曲线低，分层架构是最简入口 |
| 2 | 中等复杂业务，有明确领域模型 | 聚合根清晰，充血模型收益大 |
| 3 | 已有三层项目逐步演进 | 三层→四层渐进迁移，不颠覆原架构 |
| 4 | Spring Boot/MyBatis 技术栈 | 国内主流技术栈，示例可直接复用 |

### ⚠️ 需要条件（慎重评估后可用）

| # | 场景 | 条件 |
|---|------|------|
| 1 | 团队 10-20 人 | 需先评估是否要物理模块隔离 → 见 08 多模块方案 |
| 2 | 多聚合根复杂业务 | 需确认聚合边界清晰 → 先做事件风暴再落地分层 |
| 3 | 已有微服务拆分意向 | 先按分层架构落地单服务 → 再参考 09-12 微服务方案拆分 |
| 4 | 非 Spring Boot 技术栈 | DDD 分层思想通用，但目录结构和代码示例需自行适配 |

### ❌ 不适用场景

| # | 场景 | 替代方案 |
|---|------|---------|
| 1 | 纯 CRUD 无业务规则 | 直接用 Spring Boot 三层 + MyBatis-Plus 更省成本 |
| 2 | 多入口系统（REST+CLI+MQ） | 参考 Hexagonal Architecture（六边形架构）更合适 |
| 3 | 需要物理模块隔离 | 使用 COLA 架构或微服务方案（见 09-12 示例） |
| 4 | 高频基础设施替换 | 基础设施频繁变化时，推荐 Clean Architecture |

**使用前提**：有稳定领域专家 + 团队愿意切换到充血模型。

## Core Principles — 核心原理

### 三层 → 四层

```
三层架构:           DDD 四层:
Controller          Interface (用户接口层)
  ↓                   ↓
Service             Application (应用层) — 纯编排
  ↓                   ↓
DAO                 Domain (领域层) ★ — 核心业务
                      ↓
                    Infrastructure (基础设施层)
```

### 四个核心原则

| # | 原则 | 说明 |
|---|------|------|
| 1 | **Domain 零依赖** | 不 import Spring/JPA/MyBatis |
| 2 | **依赖倒置** | Infra 实现 Domain 定义的接口 |
| 3 | **Application 薄层** | 只编排，不放业务 if/else |
| 4 | **Interface 协议转换** | 只做 DTO 转换，不含业务 |

## Directory Structure

```
{project}/
├── {project}-interface/              # 用户接口层
│   ├── controller/                   # REST 控制器
│   ├── dto/                          # 请求/响应 DTO
│   │   ├── request/
│   │   └── response/
│   ├── converter/                    # DTO ↔ Command 转换
│   └── advice/                       # 全局异常处理
├── {project}-application/            # 应用层
│   ├── service/                      # 应用服务（纯编排）
│   ├── command/                      # 命令对象（写）
│   ├── query/                        # 查询对象（读）
│   ├── assembler/                    # DO ↔ DTO 组装
│   └── event/                        # 事件处理
├── {project}-domain/                 # 领域层 ★（零依赖）
│   ├── {aggregate}/                  # 按聚合分包
│   │   ├── entity/                   # 实体+聚合根（充血）
│   │   ├── valueobject/              # 值对象（不可变）
│   │   ├── service/                  # 领域服务
│   │   ├── repository/               # 仓储接口（只定义）
│   │   └── event/                    # 领域事件
│   ├── factory/                      # 领域工厂
│   └── shared/                       # 共享值对象
└── {project}-infrastructure/         # 基础设施层
    ├── repository/                   # 仓储实现
    ├── persistence/                  # PO 实体+映射
    ├── messaging/                    # 消息队列
    ├── external/                     # 外部服务
    └── config/                       # 配置
```

## Writing Rules — 开发规范

**依赖方向**：Interface → Application → Domain ← Infrastructure

| 层 | 可依赖 | 不可依赖 |
|----|--------|---------|
| Interface | Application | Domain、Infrastructure |
| Application | Domain | Interface、Infrastructure |
| Domain | JDK 原生类型 | 所有其他层 + 框架 |
| Infrastructure | Domain | Interface、Application |

**代码命名**：
- 聚合根：`Order`（业务名，非 OrderEntity）
- 值对象：`Money`、`Email`（不可变，无 setter）
- 仓储接口：`OrderRepository`（在 Domain）
- 仓储实现：`JpaOrderRepository`（在 Infra）
- 领域事件：`OrderPlaced`（过去式）

**禁止事项**：
- 禁止 Controller 中出现 if/else 业务判断
- 禁止 Application Service 写 SQL
- 禁止 Domain 层 import Spring 或 JPA 注解
- 禁止跨聚合直接引用对象（用 ID 引用）

## Implementation Phases

```
Phase 1: 识别聚合（1-2天）
  → 事件风暴 → 聚合根 → 不变式 → 通用语言表

Phase 2: 搭建分层骨架（1天）
  → 多模块 pom.xml → 基类（Entity/VO/AggregateRoot）

Phase 3: 实现领域层（2-5天）
  → 充血模型 → Repository 接口 → 领域服务 → 领域事件

Phase 4: 实现基础设施层（2-3天）
  → Repository 实现 → PO↔DO 映射 → DB 配置

Phase 5: 实现应用层（1-2天）
  → AppService 编排 → Command/Query → 事务管理

Phase 6: 实现接口层（1-2天）
  → Controller → DTO → 参数校验 → 异常处理

Phase 7: 审查验证（0.5天）
  → ddd-code-reviewer → ArchUnit → Domain 测试 ≥ 80%
```

## Evolution

```
Phase 1: 传统三层       ← 当前状态
Phase 2: 四层基础       ← 抽取 Domain + Infra
Phase 3: 充血模型       ← 实体含业务方法
Phase 4: 领域事件+CQRS  ← L1 模型分离
Phase 5: 升级架构       ← 根据需要选 Hexagonal/Clean/COLA
```

## Gotchas

15 个常见陷阱详见 [references/09-gotchas.md](references/09-gotchas.md)。

## FAQ

15 个常见问题详见 [references/10-faq.md](references/10-faq.md)。

## Keywords

分层架构, DDD 四层, 传统分层, 三层变四层, DDD 分层, layered architecture, DDD layered, three tier to DDD four layer, 依赖倒置, 充血模型, 贫血模型, 仓储模式, Repository 模式, Spring Boot DDD, MyBatis DDD, 目录结构 DDD, ArchUnit 分层检查, 依赖方向验证

## References

| 文件 | 内容 |
|------|------|
| [references/01-domain-layer.md](references/01-domain-layer.md) | 领域层详解：实体、值对象、聚合、领域服务 |
| [references/02-application-layer.md](references/02-application-layer.md) | 应用层详解：AppService、Command/Query、事务 |
| [references/03-interface-layer.md](references/03-interface-layer.md) | 接口层详解：Controller、DTO、异常处理 |
| [references/04-infrastructure-layer.md](references/04-infrastructure-layer.md) | 基础设施层详解：Repository 实现、PO 映射 |
| [references/05-dependency-rules.md](references/05-dependency-rules.md) | 依赖方向规则与层间通信约定 |
| [references/06-migration-guide.md](references/06-migration-guide.md) | 三层→四层渐进式迁移指南 |
| [references/07-archunit-config.md](references/07-archunit-config.md) | ArchUnit 自动化验证配置 |
| [references/08-cqrs-integration.md](references/08-cqrs-integration.md) | CQRS 轻量集成（L1 模型分离） |
| [references/09-gotchas.md](references/09-gotchas.md) | 15 个常见陷阱 |
| [references/10-faq.md](references/10-faq.md) | 15 个常见问题 |

## Examples

| 文件 | 内容 |
|------|------|
| [examples/spring-boot-order-example.md](examples/spring-boot-order-example.md) | Spring Boot 订单系统完整示例 |
| [examples/ddd4j-springboot-practice.md](examples/ddd4j-springboot-practice.md) | DDD4J Spring Boot 实战（Nova Coffee） |
| [examples/partme-91-code-example.md](examples/partme-91-code-example.md) | 在线请假系统完整代码 |
| [examples/ddd4j-spring-boot-guide.md](examples/ddd4j-spring-boot-guide.md) | Spring Boot DDD 分层实操指南 |
| [examples/05-archunit-layered-config.md](examples/05-archunit-layered-config.md) | ArchUnit 分层验证配置 |
| [examples/06-monolith-simple.md](examples/06-monolith-simple.md) | 单体简单项目：单模块四层分包 |
| [examples/07-monolith-complex.md](examples/07-monolith-complex.md) | 单体复杂项目：多聚合根 + 跨聚合编排 |
| [examples/08-monolith-multi-module.md](examples/08-monolith-multi-module.md) | 单体多模块：四层 Maven 模块隔离 |
| [examples/09-microservice-simple.md](examples/09-microservice-simple.md) | 微服务简单：每服务一个 DDD 分层单体 |
| [examples/10-microservice-complex.md](examples/10-microservice-complex.md) | 微服务复杂：事件驱动 + Saga 编排 |
| [examples/11-microservice-multi-module.md](examples/11-microservice-multi-module.md) | 微服务多模块：每服务四层子模块 |
| [examples/12-microservice-complex-multi.md](examples/12-microservice-complex-multi.md) | 微服务复杂多模块：Shared Kernel + CQRS |

## Output

当使用本 Skill 时，提供以下产出：
1. **项目骨架**：完整的分层目录结构（多模块或单模块）
2. **基类模板**：Entity/AggregateRoot/ValueObject/DomainEvent
3. **依赖配置**：Maven/Gradle（含 ArchUnit、Spring Boot、JPA）
4. **完整 Demo**：一个聚合端到端实现
5. **ArchUnit 配置**：依赖方向自动化验证
6. **演进路线图**：三层→四层→可选架构升级
7. **迁移指南**：存量三层项目迁移步骤

## Security & Stability

- 代码模板为教学示例，请替换占位符为环境配置
- ArchUnit 规则强制分层边界，建议集成 CI 流水线
- DDD 四层结构隔离领域逻辑与基础设施，减少攻击面
- 本 Skill 不包含可执行脚本，所有操作为代码生成和审查
- **本 Skill 为纯文档型 Skill：不收集、不处理、不存储任何用户数据；不访问网络或外部服务；不使用任何第三方脚本。**
