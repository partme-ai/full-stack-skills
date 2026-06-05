---
name: ddd-architecture-cola
description: Comprehensive guidance for COLA v5 Architecture (菱形架构) — Alibaba's COLA framework with adapter/application/domain/infrastructure layers. Covers full project scaffolding, architecture validation (cola-creator + cola-validator combined), dependency rule checking with ArchUnit, CQRS integration, and multi-module Maven/Gradle project generation. Use when user asks about COLA architecture, 菱形架构, cola-creator, cola-validator, 创建 COLA 项目, or needs Alibaba DDD framework.
license: Apache-2.0
---
# DDD Architecture — COLA v5（菱形架构）

COLA v5 是阿里巴巴开源的 DDD 架构框架，采用**菱形架构**——Domain 居中，Adapter 和 Infrastructure 分居两侧。本 Skill 合并 cola-creator（脚手架生成）和 cola-validator（架构校验），提供从创建到持续校验的全流程能力。

## Workflow

```
输入 → 意图识别
  ├─ "创建 COLA 项目" → Creator 流程（5 步）
  │   Step 1: 确认项目名/包名/语言/Spring Boot 版本/CQRS 开关
  │   Step 2: 生成多模块 Maven/Gradle 骨架
  │   Step 3: 生成基类（AggregateRoot/Entity/VO/DomainEvent）
  │   Step 4: 生成 Demo 聚合代码（四层完整链路）
  │   Step 5: 生成 ArchUnit 测试 + check_cola.py 脚本
  └─ "检查架构合规" → Validator 流程（4 步）
      Step 1: 接收项目路径或代码片段
      Step 2: 执行 6 项合规检查
      Step 3: P0/P1/P2 权重扣分，输出评分报告
      Step 4: 输出违规清单 + 修复建议
完成后引导 → ddd-domain-designer / ddd-api-designer / ddd-code-reviewer
```

## When to Use / Boundary

### 什么时候该用（适用场景）
- Java + Spring Boot 企业级项目，MyBatis/JPA 技术栈
- 需要脚手架自动生成多模块 COLA 项目
- 需要 ArchUnit 自动校验架构合规
- 国内阿里系技术生态（Dubbo/RocketMQ/Nacos）
- 团队 5-50 人，业务中高复杂度

### 不适用场景
- 非 Java 项目 → 不适用，推荐 `ddd-architecture-clean` / `ddd-architecture-hexagonal`
- 非 Spring Boot → 不适用，COLA 强绑定 Spring 生态
- 2-3 人团队简单 CRUD → 不适用，`ddd-architecture-layered` 更轻量
- 已有整洁/六边形架构正常运行 → 不适用，无需迁移
- 快速原型/PoC 阶段 → 不适用，架构成本过高

## 菱形架构核心原理

```
          ┌──────────────┐
          │   Adapter    │  ← 适配层：HTTP/MQ/RPC 协议适配与 DTO 转换
          └──────┬───────┘
          ┌──────▼───────┐
          │   Application│  ← 应用层：用例编排、事务管理、CQRS 执行器
  ┌───────┴───────┬───────┴───────┐
  ▼               ▼               ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│  Domain  │ │  Domain  │ │  Domain  │  ← 领域层：业务规则 ★ 零框架依赖
│   ★      │ │   ★      │ │   ★      │
└──────────┘ └──────────┘ └──────────┘
  ▲               ▲               ▲
  └───────────────┴───────────────┘
                 │
          ┌──────▼───────┐
          │Infrastructure│  ← 基础设施层：DB/MQ/缓存/外部 API 实现
          └──────────────┘
```

| 层 | 模块 | 职责 | 依赖 |
|---|------|------|------|
| **Adapter** | `{p}-adapter` | REST/RPC/MQ 协议适配、DTO 转换、参数校验 | → app, domain |
| **Application** | `{p}-app` | Command/Query 执行器、事务编排、扩展点路由 | → domain, infra |
| **Domain** | `{p}-domain` | 聚合/E/VO、领域事件、Repository/Gateway 接口、Ability | 无依赖 |
| **Infrastructure** | `{p}-infrastructure` | Repository/Gateway 实现、PO↔DO 转换、配置、组件 | → domain |

**v5 新增特性**：Extension Point（@ExtensionPoint + @Extension(bizId) 多租户差异化）、Ability（领域能力抽象）、组件化基础设施（分布式锁/限流/熔断）、CQRS 强化（command/query 执行器严格分离）

## 生成能力：cola-creator

```
AI 交互确认 → 项目名/包名(com.example.order) / 语言(Java 17+/Kotlin) / Spring Boot(3.2+/3.1) / CQRS(否/L1/L2) / Demo(默认Order)
生成内容：
  ├── pom.xml/build.gradle（6 模块：start/adapter/app/domain/infrastructure/common）
  ├── COLA v5 标准目录结构 + 基类（AggregateRoot/Entity/VO/DomainEvent）
  ├── Demo 聚合（Order 四层完整示例）
  ├── DDD 中间件配置（DomainEventBus、ExtensionExecutor）
  ├── ArchUnit 测试 + check_cola.py 脚本
  └── .gitignore + README
```

两种方式：`mvn archetype:generate -DarchetypeGroupId=com.alibaba.cola -DarchetypeArtifactId=cola-archetype-web -DarchetypeVersion=5.0.0`（快速）或手动多模块（生产推荐，详见 references/02）。

## 校验能力：cola-validator

| 检查项 | 级别 | 说明 | 检测方式 |
|--------|:----:|------|---------|
| 依赖方向 | P0 | Domain 不可依赖 Infrastructure/App/Adapter | import 解析 |
| Domain 纯净度 | P0 | Domain 无 Spring/JPA/MyBatis/Hibernate import | import 扫描 |
| 层职责 | P0 | Adapter 无 SQL、App 无业务 if/else | AST 分析 |
| 包命名规范 | P1 | 按 COLA 约定命名 | 正则匹配 |
| 模块循环依赖 | P1 | DFS 检测依赖图 | 图遍历 |
| 聚合设计 | P1 | 聚合＞5 实体、跨聚合引用、值对象可变性 | AST 分析 |

评分模型：`评分 = 100 - 扣分（P0=10分/项，P1=5分/项，P2=2分/项）`。≥90→A，70-89→B，50-69→C，<50→D。

运行：`mvn test -Dtest=ArchitectureComplianceTest`（ArchUnit Java 测试）或 `python scripts/check_cola.py /path/to/project`（Python 轻量校验）。

## 目录结构（COLA v5 多模块）

```
{project}/
├── start/               — 启动模块：Application.java(@EnableCola), config/
├── adapter/             — 适配器层
│   ├── web/             — controller/dto/advice(GlobalExceptionHandler)
│   ├── rpc/             — Dubbo/gRPC provider/consumer/facade
│   ├── job/             — 定时任务调度
│   └── message/         — MQ consumer/producer
├── app/                 — 应用层
│   ├── executor/        — command/query/event/extension 执行器
│   ├── model/           — command/query/event/dto 对象
│   ├── eventhandler/    — 事件处理器
│   └── extension/       — 扩展点(point/biz/impl)
├── domain/ ★            — 领域层（零框架依赖）
│   ├── model/           — entity/vo/aggregate/event/enums
│   ├── service/         — 领域服务
│   ├── ability/         — 领域能力（v5 新概念）
│   ├── gateway/         — 防腐层接口
│   └── repository/      — 仓储接口
├── infrastructure/      — 基础设施层
│   ├── config/          — DB/缓存/MQ/RPC 配置
│   ├── persistence/     — repositoryimpl/mapper/dao/entity(PO)
│   ├── gatewayimpl/     — 网关实现
│   ├── external/        — 外部服务客户端
│   └── component/       — 分布式锁/限流/熔断/重试
└── common/              — 常量/异常/工具/注解/上下文
```

## 落地步骤

Phase 1 [1天] 脚手架 → Phase 2 [2-3天] 领域建模（配合 ddd-domain-designer）→ Phase 3 [2-3天] 基础设施（Repository/Gateway/PO）→ Phase 4 [1-2天] 应用+适配（Executor → Controller）→ Phase 5 [0.5天] 架构校验 → Phase 6 [持续] CI/CD 自动校验

## 核心规则（Core Rules）

**四大约束（P0）**：①Domain 零框架依赖（禁止 Spring/JPA/MyBatis）②App 层无业务 if/else ③Adapter 无 SQL/业务判断 ④模块间无循环依赖

**依赖方向**：`adapter → app → domain ← infrastructure`（domain 不依赖任何人）

## Gotchas — 常见坑（15条）

1. **Domain 层放 Controller** — Controller 在 Adapter 层。Domain 下出现 `@RestController` 说明分层全错。
2. **App 层直接操作 Mapper** — 必须通过 Repository 接口：`orderRepository.save(order)` 而非 `orderMapper.insert()`。
3. **模块命名不匹配 COLA** — 必须为 `{project}-adapter/app/domain/infrastructure`，否则 ArchUnit 校验失败。
4. **Command/Query 放 Domain 层** — 应放 `app/model/command/` 和 `app/model/query/`。
5. **Archetype 版本不匹配** — cola-archetype-web 5.0.0 要求 Spring Boot 3.x，2.x 需手动适配。
6. **Domain 层用 JPA @Entity** — 持久化映射在 Infrastructure 层用 PO 类。
7. **App 层抛框架异常** — 应抛 `BizException`，Adapter 层统一转换。
8. **跨聚合直接引用对象** — 聚合间通过 ID 引用，不直接 `Order.getCustomer()`。
9. **值对象带 setter** — ValueObject 应不可变（final + 无 setter），修改返回新对象。
10. **缺少领域事件** — 创建订单/支付/取消等关键操作必须发布领域事件。
11. **Adapter 层有业务判断** — Controller/Consumer 不应有任何 if-else。
12. **God Service 反模式** — Service 超 500 行应按聚合拆分。
13. **扩展点无默认实现** — 每个 `ExtensionPoint` 需有默认 `@Extension`。
14. **@EnableCola 缺失** — 启动类必须加 `@EnableCola` 启用的扩展点和事件总线。
15. **PO 与 DO 混用** — 持久化对象和领域对象必须分离，用 Converter 转换。

## FAQ（15条）

**Q1: COLA v5 和整洁架构的关系？** COLA v5 是整洁架构的阿里化实现，增加包命名规范、扩展点机制、CQRS 强化和脚手架。

**Q2: 为何不用 cola-archetype 直接生成？** Archetype 快速但固定，手动搭建更适合生产定制。

**Q3: COLA 支持微服务吗？** 支持。每个微服务内部按 COLA 四层组织，服务间通过 RPC/MQ 通信。

**Q4: CQRS 强制吗？** 否。简单场景用 `app/service/` 编排，复杂场景切到 CQRS executor。

**Q5: check_cola.py 和 ArchUnit 区别？** check_cola.py 轻量 import 扫描适合 CI，ArchUnit 强大 AST 分析需 Java 环境。

**Q6: Domain 层 @Autowired 怎么处理？** Domain 禁止 @Autowired，通过方法参数或构造器注入接口。

**Q7: 领域事件送达保证？** App 层事务提交后 `EventBus.publish()`，生产配合 Transactional Outbox 模式。

**Q8: COLA 和 Spring Cloud 关系？** COLA 是架构规范，Spring Cloud 是基础设施，可完全集成使用。

**Q9: 值对象存 JSON 还是拆列？** 简单值对象拆列，复杂嵌套存 JSON + Converter 类型转换。

**Q10: 聚合太大怎么办？** ≤ 5 实体，按业务操作频率拆分。

**Q11: 扩展点 bizId 来源？** 前端请求头、登录会员等级、租户 ID 路由。

**Q12: 无扩展点需求可删吗？** 可。`app/extension/` 和 `domain/ability/` 可不创建。

**Q13: common 模块内容？** 常量、异常基类、DTO 基类、上下文（UserContext/TenantContext）、自定义注解。

**Q14: start 和 adapter 关系？** start 启动入口 + 全局配置，adapter 协议适配，start 依赖 adapter。

**Q15: 如何确保不泄露敏感配置？** 外部化配置 + 环境变量，禁止硬编码密钥，Domain 层不读写配置文件。

## Keywords

`COLA` `COLA v5` `菱形架构` `diamond architecture` `cola-creator` `cola-validator` `ArchUnit` `CQRS` `Extension Point` `扩展点` `Ability` `领域能力` `Aggregate Root` `Entity` `Value Object` `Domain Event` `Repository` `Gateway` `防腐层` `DDD` `Spring Boot` `MyBatis` `@EnableCola` `CommandExecutor` `QueryExecutor`
## Project Scaffolding

**ddd4j Boot** 是 COLA v5 架构的 Java 参考实现，基于 Spring Boot 3.5.x，集成 ddd-4-java 和 cqrs-4-java 轻量库，完整实现 DDD、CQRS 和 Event Sourcing 模式。

- **项目生成**: 使用 `scripts/init_project.py` 可自动生成 COLA 多模块项目结构，支持单模块单体、多模块单体和微服务三种项目类型，涵盖 pom.xml、package-info.java、.gitignore、mvnw 等必需文件
- **合规验证**: 使用 `scripts/check_project.py` 可验证项目的 DDD 分层合规性、依赖方向正确性和包命名规范，输出详细的违规报告和修复建议
- **场景示例**: 参考 `examples/13-architecture-patterns.md`（四种架构模式）、`examples/14-single-module.md`（单模块单体）、`examples/15-multi-module.md`（多模块单体）、`examples/16-microservices.md`（微服务）
- **详细说明**: 参考 `references/14-ddd4j-scaffold.md` 了解完整的项目生成流程、验证规则、层依赖关系和包命名规范

## References

详细参考见 `references/` 目录：01-architecture-principles（架构原理）、02-project-scaffold（脚手架）、03-domain-layer（领域层）、04-app-layer（应用层）、05-adapter-layer（适配层）、06-infrastructure（基础设施）、07-archunit-validation（ArchUnit 校验）、08-cqrs-integration（CQRS 集成）

## Examples

完整代码见 `examples/` 目录：01-quickstart-order（Order 聚合完整实现）、02-customer-crud（CRUD 入门）、03-extension-point（扩展点机制）、04-cqrs-separation（CQRS 分离）、05-archunit-config（ArchUnit 校验 CI/CD 集成）

项目规模示例见 `examples/` 目录：06-monolith-simple（单体简单项目）、07-monolith-complex（单体复杂项目）、08-monolith-multi-module（单体多模块项目）、09-microservice-simple-monolith（微服务简单的单体项目）、10-microservice-complex-monolith（微服务复杂的单体项目，基于 ddd4j-gateway）、11-microservice-simple-multi-module（微服务简单的多模块项目，基于 ddd4j-rednote）、12-microservice-complex-multi-module（微服务复杂的多模块项目，基于 ddd4j-pay）
