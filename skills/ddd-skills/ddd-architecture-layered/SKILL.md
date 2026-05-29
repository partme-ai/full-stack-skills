---
name: ddd-architecture-layered
description: Comprehensive guidance for DDD Layered Architecture (DDD 四层架构) — Traditional 3-layer to DDD 4-layer transformation with Interface/Application/Domain/Infrastructure layers. Covers complete directory structure, dependency inversion, ArchUnit validation, Spring Boot integration, and step-by-step migration guide. Use when user asks about layered architecture, DDD four-layer, 分层架构, traditional layering with DDD, or needs a simple DDD entry point for small to medium teams.
license: Apache-2.0
---

# DDD Layered Architecture — 分层架构落地指南

DDD Layered Architecture 是 DDD 生态中最简的入门架构。它将传统三层（Controller/Service/DAO）重构为四层（Interface/Application/Domain/Infrastructure），通过依赖倒置使领域层成为系统核心。

## Workflow — 在 DDD 技能树中的位置

```
User Journey:
  awesome (入门) → selector (选型)
                      ↓
              layered (分层) ★ ← 你在这里
              ┌──────┴──────┐
              ↓              ↓
        domain-designer   cqrs-architecture
              ↓              ↓
         code-reviewer → evaluator → doc
```

分层架构是**从三层向更严格架构演进的第一站**。建议阅读顺序：
1. [ddd-architecture-awesome](../ddd-architecture-awesome/) — DDD 入门与全景
2. [ddd-architecture-selector](../ddd-architecture-selector/) — 为什么选分层架构？
3. **→ ddd-architecture-layered**（当前）
4. [ddd-domain-designer](../ddd-domain-designer/) — 设计领域模型
5. [ddd-code-reviewer](../ddd-code-reviewer/) — 审查分层合规

---

## 1. When to Use — 适用边界

### ✅ 适用场景
| 场景 | 说明 |
|------|------|
| 团队 < 10 人 | 学习曲线最低，不需要额外框架 |
| 中等复杂业务 | 有明确领域模型，但还不复杂到需要六边形/整洁 |
| 已有三层项目 | 渐进式演进，逐步引入 DDD 概念 |
| Spring Boot 技术栈 | MyBatis/Spring Data JPA 天然适配 |
| DDD 刚起步 | 想试 DDD 但还不准备全面投入 |

### ❌ 不适用场景
| 场景 | 替代方案 |
|------|---------|
| 纯 CRUD 无业务规则 | 标准 Spring Boot MVC 即可 |
| 多入口系统（REST+CLI+MQ） | [ddd-architecture-hexagonal](../ddd-architecture-hexagonal/) |
| 需要物理模块隔离 | [ddd-architecture-clean](../ddd-architecture-clean/) 或 COLA |
| 高频基础设施替换 | 六边形架构 |
| 10+ 微服务的复杂系统 | [ddd-architecture-selector](../ddd-architecture-selector/) 综合选型 |

### ⚠️ 使用前提
- 有稳定的领域专家或产品负责人
- 团队愿意从贫血模型切换到充血模型
- 分层架构是起点，未来可演进到 Hexagonal/Clean

---

## 2. Core Principles — 核心原理

### 传统三层 → DDD 四层

```
Traditional 3-Layer:           DDD 4-Layer:

Controller                     Interface (用户接口层) — 协议转换
  ↓                              ↓
Service                        Application (应用层) — 纯编排，无业务
  ↓                              ↓
Repository/DAO                 Domain (领域层) ★ — 核心业务逻辑
                                 ↓
                               Infrastructure (基础设施层)
```

### 四个核心原则

| # | 原则 | 说明 | 违反后果 |
|---|------|------|---------|
| 1 | **Domain 零依赖** | 领域层不 import 任何框架（Spring/JPA/MyBatis） | 框架耦合，数据库迁移灾难 |
| 2 | **依赖倒置** | Infrastructure 实现 Domain 定义的接口 | 层间耦合，无法替换基础设施 |
| 3 | **Application 薄层** | 应用层只做编排，不包含 if/else 业务判断 | 领域模型失焦，退化为三层 |
| 4 | **Interface 协议转换** | 接口层只做 DTO/协议转换，不含业务逻辑 | 业务逻辑泄露到控制器 |

### 依赖方向图

```
Interface ──→ Application ──→ Domain ←── Infrastructure
    |              |              |            |
  Controller     AppService    Entity/     RepositoryImpl
  DTO/Request    Command/Query  Aggregate   Mapper/PO
  Converter      Transaction    Repository  EventPublisher
                                Interface   Cache/MQ Config
```

**关键**：Domain 层处于依赖关系的最下游，All arrows point inward。

---

## 3. Directory Structure — 完整目录结构

```
{project}/
├── {project}-interface/              # 用户接口层
│   ├── controller/                   # REST API 控制器
│   ├── dto/                          # 接口层 DTO
│   │   ├── request/                  # 请求 DTO
│   │   └── response/                 # 响应 DTO
│   ├── converter/                    # DTO ↔ Command/Query 转换
│   ├── advice/                       # 全局异常处理
│   └── filter/                       # 认证/日志过滤器
├── {project}-application/            # 应用层
│   ├── service/                      # 应用服务（纯编排）
│   ├── command/                      # 命令对象（CQRS 写）
│   ├── query/                        # 查询对象（CQRS 读）
│   ├── assembler/                    # DO ↔ DTO 组装
│   ├── event/                        # 事件处理（应用级）
│   └── validator/                    # 应用验证器
├── {project}-domain/                 # 领域层（核心，零依赖）
│   ├── {aggregate}/                  # 按聚合分包
│   │   ├── entity/                   # 实体 + 聚合根（充血模型）
│   │   ├── valueobject/              # 值对象（不可变）
│   │   ├── event/                    # 领域事件
│   │   ├── service/                  # 领域服务
│   │   ├── repository/               # 仓储接口（只定义）
│   │   ├── specification/            # 规约模式
│   │   └── exception/                # 领域异常
│   ├── factory/                      # 领域工厂
│   ├── policy/                       # 业务策略
│   └── shared/                       # 共享值对象/枚举
└── {project}-infrastructure/         # 基础设施层
    ├── repository/                   # 仓储实现（JPA/MyBatis/Memory）
    │   ├── jpa/                      # JPA 实现
    │   ├── mybatis/                  # MyBatis 实现
    │   └── memory/                   # 内存实现（测试用）
    ├── persistence/                  # 持久化实体（PO）
    │   ├── entity/                   # JPA Entity
    │   └── mapper/                   # PO ↔ DO 映射器
    ├── messaging/                    # 消息队列
    │   ├── publisher/                # 事件发布
    │   └── consumer/                 # 事件消费
    ├── external/                     # 外部服务
    │   ├── payment/                  # 支付集成
    │   └── notification/             # 通知集成
    ├── config/                       # 配置
    └── security/                     # 安全基础设施
```

**多模块 vs 单模块**：
- 多模块（Maven/Gradle modules）：适合 5-15 人团队，物理隔离更严格
- 单模块（package 分包）：适合 < 5 人团队，降低构建复杂度

---

## 4. Development Conventions — 开发规范

### 依赖方向矩阵

| 层 | 可依赖 | 不可依赖 |
|----|--------|---------|
| Interface | Application | Domain 直接、Infrastructure |
| Application | Domain | Interface、Infrastructure 直接 |
| Domain | 自身、JDK | Application、Interface、Infrastructure、Spring/JPA |
| Infrastructure | Domain | Interface、Application 直接 |

### 各层禁止项

| 层 | ❌ 禁止 | ✅ 替代 |
|----|--------|---------|
| Interface | if/else 业务判断、SQL 语句 | 协议转换、参数校验 |
| Application | 业务 if/else、SQL 语句 | 编排领域服务、管理事务 |
| Domain | Spring `@Service`、`@Entity` 注解 | 纯 POJO + 充血模型 |
| Infrastructure | 业务逻辑 | 技术实现 |

### 代码规范要点

```
聚合根命名：Order（业务名称，非 OrderEntity）
值对象命名：Money, Email, OrderStatus（不可变，无 setter）
仓储命名：OrderRepository（接口在 Domain，实现在 Infra）
领域事件：OrderPlaced（过去式），OrderPaid
领域服务：OrderPricingService（多实体协作）

聚合大小：≤ 5 个实体
聚合间引用：通过 ID（聚合 B 引用聚合 A 的 ID，非 A 对象）
事务边界：Application 层，不在 Domain 层
跨聚合操作：领域事件（最终一致性）
```

---

## 5. Implementation Phases — 落地实施步骤

```
Phase 1: 识别聚合（1-2 天）
  ├── 事件风暴 → 识别聚合根
  ├── 划分子域边界 → 定义不变式
  └── 输出：聚合设计清单 + 通用语言表

Phase 2: 搭建分层骨架（1 天）
  ├── 生成 pom.xml / build.gradle（多模块）
  ├── 生成基类：Entity/AggregateRoot/ValueObject/DomainEvent
  ├── 配置 Spring Boot + 数据库
  └── 输出：可编译的空项目

Phase 3: 实现领域层（2-5 天）
  ├── 充血模型实体 → 值对象 → 聚合根
  ├── 仓储接口（只定义方法签名）
  ├── 领域服务（多个实体的业务协作）
  ├── 领域事件定义
  └── 输出：纯 POJO 领域模型 + 单元测试

Phase 4: 实现基础设施层（2-3 天）
  ├── Repository 实现（JPA/MyBatis）
  ├── PO ↔ DO 转换器（MapStruct/手动）
  ├── 数据库表设计 + Flyway 迁移脚本
  └── 输出：可运行的持久化 + 集成测试

Phase 5: 实现应用层（1-2 天）
  ├── AppService 编排领域服务
  ├── Command/Query 对象定义
  ├── 事务管理（@Transactional）
  └── 输出：完整的业务用例

Phase 6: 实现接口层（1-2 天）
  ├── REST Controller → DTO → 请求/响应
  ├── 参数校验（@Valid + JSR-303）
  ├── 全局异常处理
  └── 输出：可调用的 API

Phase 7: 审查验证（0.5 天）
  ├── ddd-code-reviewer 检查
  ├── ArchUnit 依赖方向自动化测试
  ├── 领域层单元测试覆盖率 ≥ 80%
  └── 输出：审查报告 + 修复清单
```

---

## 6. Evolution Roadmap — 演进路线

```
Level 1: 传统三层（当前）
  └── Controller ──→ Service ──→ DAO
       ↓
Level 2: 四层基础（Phase 1-2）
  └── Interface ──→ Application ──→ Domain ←── Infrastructure
       ↓
Level 3: 充血模型（Phase 3）
  └── 实体含业务方法，非 getter/setter
       ↓
Level 4: 领域事件 + CQRS L1（Phase 4-5）
  └── 事件驱动跨聚合通信
       ↓
Level 5: 升级架构（可选）
  ├── 需求六边形 → ddd-architecture-hexagonal
  ├── 需求整洁 → ddd-architecture-clean
  └── 需求 COLA → ddd-architecture-cola
```

**何时升级**：
- 频繁切换基础设施（DB/MQ）→ 六边形
- 需要严格模块隔离 → 整洁架构
- 采用阿里技术生态 → COLA
- 团队扩展到 15+ 人 → 整洁或 COLA

---

## 7. Gotchas — 15 个常见陷阱

| # | 陷阱 | 现象 | 修复 |
|---|------|------|------|
| 1 | **贫血模型** | Entity 只有 getter/setter | 将 `setStatus()` 改为 `pay()`、`cancel()` |
| 2 | **Application 膨胀** | AppService > 50 行，含 if/else | 业务逻辑下沉到 Domain |
| 3 | **Domain 框架污染** | `@Entity`、`@Service` 出现在 Domain | 用 PO 分离持久化 |
| 4 | **跨聚合直接引用** | Order 中引用了 Customer 对象 | 改为 CustomerId 引用 |
| 5 | **Controller 有业务** | Controller 中有 if/else 判断 | 移到 Application 或 Domain |
| 6 | **大聚合** | 一个聚合 > 5 实体或 > 500 行 | 拆分为多个小聚合 |
| 7 | **跨聚合事务** | 一个 `@Transactional` 涉及多个聚合 | 用领域事件最终一致 |
| 8 | **Repo 返回 DTO** | Repository 返回非聚合根类型 | Repository 只操作聚合根 |
| 9 | **跳过 Application** | Controller 直接调用 Repository | 必须经过 AppService |
| 10 | **测试只测 API** | 只测 Controller，忽视 Domain | Domain 单元测试覆盖 ≥ 80% |
| 11 | **值对象可变** | ValueObject 有 setter 或 public 字段 | 用 `final` + 构造器初始化 |
| 12 | **Infra 反向依赖** | Infrastructure 直接引用 Interface | Infrastructure 只依赖 Domain |
| 13 | **忽略领域事件** | 关键业务操作不发布事件 | 为状态变更添加领域事件 |
| 14 | **上帝 Service** | 一个 Service 超过 200 行 | 拆分为多个领域服务 |
| 15 | **过度设计** | 简单 CRUD 也用 DDD | 评估业务复杂度，不滥用 DDD |

---

## 8. FAQ — 15 个常见问题

| # | 问题 | 回答 |
|---|------|------|
| 1 | 分层架构和六边形架构有什么区别？ | 分层架构只有四层，依赖方向是单向向下；六边形通过 Port/Adapter 实现双向接口隔离。分层更简单，六边形更灵活。 |
| 2 | 一定要用多模块吗？ | 不一定。小团队可以用单模块 + package 分包，但要严格遵守依赖规则。多模块在 5+ 人团队时推荐。 |
| 3 | Domain 层不能有任何 Spring 依赖吗？ | 是的。Domain 层应该是纯 POJO，不能有 `@Service`、`@Entity`、`@Repository` 等注解。 |
| 4 | 值对象一定要不可变吗？ | 是的。值对象的本质是"描述性"的，不应有生命周期。用 `final` 字段 + 只读方法。 |
| 5 | 事务注解放在哪层？ | Application 层。Domain 层的方法不应该有 `@Transactional`，因为领域方法不知道调用上下文。 |
| 6 | 聚合间如何通信？ | 聚合间通过 ID 引用，跨聚合操作通过领域事件实现最终一致性。 |
| 7 | Repository 应该返回什么？ | 聚合根对象。Repository 不应返回 DTO 或 Page 等查询结果。查询用专门的 QueryService。 |
| 8 | 一个聚合可以包含多少实体？ | 建议 ≤ 5 个。超过 5 个实体的聚合通常可以考虑拆分。 |
| 9 | DDD 四层和三层架构能混合吗？ | 可以。建议新功能用四层，老功能逐步迁移。但不要在同一功能中混用。 |
| 10 | 需要引入 CQRS 吗？ | 如果需要读写分离优化查询性能，可以引入 CQRS L1（模型分离）。Layered 架构支持轻量 CQRS。 |
| 11 | 怎么防止团队违反依赖规则？ | 用 ArchUnit 在 CI 中自动检查。关键规则：Domain 不能依赖 Infra。 |
| 12 | 分层架构适合微服务吗？ | 适合。每个微服务内部可以采用四层架构。但多入口微服务推荐六边形。 |
| 13 | Application Service 命名有规范吗？ | 推荐 `{聚合}ApplicationService`，如 `OrderApplicationService`。方法用业务用例名。 |
| 14 | 领域服务和应用服务的区别？ | 领域服务：多个实体的业务协作（在 Domain 层）。应用服务：编排领域服务 + 管理事务（在 Application 层）。 |
| 15 | 如何判断某段代码属于哪层？ | 问三个问题：① 涉及框架/数据库？→ Infra。② 是编排还是业务？→ 编排→App，业务→Domain。③ 前端交互？→ Interface。 |

---

## 9. Keywords — 触发关键词

```
分层架构, DDD 四层, 传统分层, 四层架构, 三层变四层, DDD 分层,
layered architecture, DDD layered, three tier to DDD four layer,
分层落地, 架构分层, 领域层, 应用层, 基础设施层, 接口层,
依赖倒置, 充血模型, 贫血模型, 仓储模式, Repository 模式,
DDD 入门实践, 小团队 DDD, Spring Boot DDD, MyBatis DDD,
目录结构 DDD, 模块划分, 聚合分包, CQRS 轻量集成,
ArchUnit 分层检查, 依赖方向验证
```

---

## 10. References — 参考文档

### 核心参考
| 文件 | 内容 |
|------|------|
| [references/01-domain-layer.md](references/01-domain-layer.md) | 领域层详解：实体、值对象、聚合、领域服务、领域事件 |
| [references/02-application-layer.md](references/02-application-layer.md) | 应用层详解：AppService、Command/Query、事务管理 |
| [references/03-interface-layer.md](references/03-interface-layer.md) | 接口层详解：Controller、DTO、Converter、异常处理 |
| [references/04-infrastructure-layer.md](references/04-infrastructure-layer.md) | 基础设施层详解：Repository 实现、PO 映射、事件发布 |

### 规范与集成
| 文件 | 内容 |
|------|------|
| [references/05-dependency-rules.md](references/05-dependency-rules.md) | 依赖方向规则与层间通信约定 |
| [references/06-migration-guide.md](references/06-migration-guide.md) | 三层→四层渐进式迁移指南 |
| [references/07-archunit-config.md](references/07-archunit-config.md) | ArchUnit 自动化验证配置 |
| [references/08-cqrs-integration.md](references/08-cqrs-integration.md) | CQRS 轻量集成（L1：模型分离） |

### 示例
| 文件 | 内容 |
|------|------|
| [examples/spring-boot-order-example.md](examples/spring-boot-order-example.md) | Spring Boot 订单系统完整示例 |
| [examples/ddd4j-springboot-practice.md](examples/ddd4j-springboot-practice.md) | DDD4J Spring Boot 实战（Nova Coffee 场景） |
| [examples/partme-91-code-example.md](examples/partme-91-code-example.md) | 在线请假考勤系统完整代码参考 |
| [examples/ddd4j-spring-boot-guide.md](examples/ddd4j-spring-boot-guide.md) | Spring Boot DDD 分层架构实操指南 |
| [examples/ddd4j-springboot-practice.md](examples/ddd4j-springboot-practice.md) | 不依赖框架的 DDD 实战 |

### 理论依据
- Eric Evans 《领域驱动设计》（蓝皮书）— 四层架构原始定义
- Vaughn Vernon 《实现领域驱动设计》（红皮书）— 分层架构实现细节
- Martin Fowler 《企业应用架构模式》— 分层模式总结
- Robert C. Martin Clean Architecture — 依赖规则与边界
- Microsoft DDD-oriented Microservice Guide — 微服务 DDD 实践

---

## 11. Output — 输出交付

当使用本 Skill 时，提供以下产出：

1. **项目骨架**：完整的分层项目目录结构（多模块或单模块）
2. **基类模板**：Entity/AggregateRoot/ValueObject/DomainEvent/base Repository
3. **依赖配置**：Maven/Gradle pom.xml（含 ArchUnit、Spring Boot、JPA）
4. **完整 Demo**：一个聚合的端到端实现（实体→仓储→应用服务→控制器）
5. **ArchUnit 配置**：依赖方向自动化验证
6. **演进路线图**：Traditional 3-Layer → DDD 4-Layer → 可选架构升级
7. **迁移指南**：存量三层项目逐步迁移到 DDD 四层的步骤

## Security & Stability

- 代码模板均为教学示例，请将占位符（数据库 URL、凭据）替换为环境配置
- ArchUnit 规则在构建时强制分层边界，建议集成到 CI 流水线
- DDD 四层结构将领域逻辑与基础设施隔离，天然减少攻击面
- 本 Skill 不包含可执行脚本，所有操作为代码生成和审查
