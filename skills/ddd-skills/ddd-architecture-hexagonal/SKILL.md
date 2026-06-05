---
name: ddd-architecture-hexagonal
description: Comprehensive guidance for Hexagonal Architecture (Ports & Adapters) — Alistair Cockburn's hexagonal architecture with domain core, port definitions, adapter implementations, and full Java/Spring Boot implementation steps. Covers primary/driving adapters, secondary/driven adapters, use case ports, repository ports, and dependency injection configuration. Use when user asks about hexagonal architecture, 六边形架构, ports and adapters, 端口适配器, Alistair Cockburn, or needs DDD with clean separation.
license: Apache-2.0
---

# DDD Architecture — Hexagonal (Ports & Adapters)

**Alistair Cockburn (2005)** — 业务逻辑通过端口（Ports）隔离，外部系统通过适配器（Adapters）接入。**适用受众**: 后端架构师/技术负责人（团队 > 5 人）、DDD 实践者。**定制机制**: 提供技术栈/入口类型/团队规模三个配置维度。加载本技能时，建议先阅读 Workflow 和 When to Use 确认匹配度。

> "允许应用被用户、程序、自动化测试或批处理脚本平等驱动，并在脱离最终运行设备和数据库的情况下开发和测试。" — Alistair Cockburn

## Workflow

### Step 1: 主适配器协议转换 — REST Controller/CLI 接收请求，完成参数校验与协议转换
### Step 2: 入站端口调用 — 适配器调用 UseCase 接口，触发应用层用例编排
### Step 3: 应用服务编排 — Application Service 编排用例，调用领域模型执行业务逻辑
### Step 4: 领域模型执行 — 聚合根/实体执行业务逻辑，输出结果或领域事件
### Step 5: 出站端口持久化 — 应用服务通过 Repository 接口保存领域状态
### Step 6: 次适配器技术实现 — Adapter 执行 DB/MQ/外部 API 的技术实现

> **定义验证法**: 脱离数据库和 HTTP 即可跑通全部领域层单元测试 → 边界正确。

## Rules

1. **依赖规则**: 依赖方向必须从外到内——Adapter → Application → Domain。Domain 层零外部依赖。
2. **端口粒度规则**: 每个端口职责单一，包含 10+ 方法的端口需立即拆分。
3. **异常转换规则**: 技术异常（SQLException、TimeoutException）必须在 Adapter 内部捕获并转换为领域异常，不得向上泄漏。

## When to Use

### ✅ 适合场景
1. **多入口系统**（REST + CLI + MQ + gRPC）：多个外部系统同时驱动同一业务逻辑
2. **基础设施频繁变更**（换 DB/MQ/缓存）：只需换 Adapter 实现，Domain 零修改
3. **极致可测试性**：Mock 端口即可测试全部领域逻辑，不依赖数据库
4. **微服务架构标准化**：团队 > 5 人，需要各服务一致的架构约定
5. **团队熟悉抽象设计**：能合理设计端口粒度，避免过度抽象

## Boundary

### ⚠️ 需要条件
1. **团队理解抽象设计**：端口粒度需要领域知识和抽象能力，否则可能定义不当
2. **项目规模适中**：小项目用 Layered 更简单，六边形增加间接层成本
3. **需要 DDD 领域模型配合**：Port 接口定义需要领域建模前置知识
4. **良好的 DI 容器支持**：Spring/Guice 等框架可简化适配器装配

### ❌ 不适用（附替代方案）
1. **单一 REST API + 简单 CRUD** → 用 `ddd-architecture-layered`
2. **中文企业 MyBatis 生态** → 用 `ddd-architecture-cola`
3. **需 UseCase + Entity 严格分离** → 用 `ddd-architecture-clean`
4. **快速原型 / MVP 阶段** → 直接用传统三层（不引入六边形架构的开销）

## 核心原理

### 三大抽象

```
Driving Side (REST/CLI/gRPC/Test) → Domain Core ← Driven Side (PostgreSQL/RabbitMQ/Redis/Stripe)
```

| 概念 | 说明 | 代码体现 |
|------|------|---------|
| **Port（端口）** | 领域层定义的接口 | `interface OrderRepository` |
| **Primary Adapter（主适配器）** | 外部如何驱动系统 | REST Controller、CLI Command、gRPC Service |
| **Secondary Adapter（次适配器）** | 系统如何驱动外部 | JPA RepositoryImpl、Kafka Producer、StripeClient |

### Strong Port vs Weak Port

```java
// ❌ Weak — 泄漏 SQL 概念
interface OrderRepository { List<Order> findByQuery(String sql, Map<String, Object> params); }

// ✅ Strong — 纯领域概念
interface OrderRepository {
    Optional<Order> findById(OrderId id);
    List<Order> findByCustomerId(CustomerId customerId);
    void save(Order order);
}
```

## 目录结构

```
{project}/
├── {project}-domain/              # 领域核心 + 端口定义（零框架依赖）
│   └── port/{inbound, outbound}/  # ★ 端口接口
├── {project}-application/         # 应用层（UseCase 实现）
├── {project}-adapter/             # 适配器层
│   ├── inbound/                   # ★ 主适配器（REST/CLI/gRPC/MQ）
│   └── outbound/                  # ★ 次适配器（Persistence/Messaging/External）
└── {project}-configuration/       # 配置层（DI 装配）
```

## 开发规范

### 层职责

| 层 | 依赖 | 允许做的事 | 禁止做的事 |
|------|------|----------|----------|
| Domain | 无 | 实体行为、值对象、领域事件、端口定义 | import 框架注解、SQL、HTTP |
| Application | Domain | 用例编排、事务管理、端口调用 | if/else 业务判断、直接操作 DB |
| Adapter | Application | 协议转换、参数校验、异常映射 | 包含业务逻辑、直接操作 Domain 内部状态 |
| Configuration | 全部 | DI 装配、Profile 配置 | 包含业务代码 |

### 代码规范

```java
// 入站端口（Domain）
public interface CreateOrderUseCase { OrderCreatedResult execute(CreateOrderCommand command); }
// 出站端口（Domain）
public interface OrderRepository { void save(Order order); Optional<Order> findById(OrderId id); }
// 应用服务（实现入站端口，注入出站端口）
@ApplicationService
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepository orderRepository;
    @Override @Transactional
    public OrderCreatedResult execute(CreateOrderCommand command) {
        Order order = Order.create(command.getCustomerId());
        orderRepository.save(order);
        return OrderCreatedResult.from(order);
    }
}
// 主适配器（仅协议转换）
@RestController
public class OrderController {
    @PostMapping("/orders")
    public ResponseEntity<CreateOrderResponse> create(@RequestBody @Valid CreateOrderRequest req) {
        var result = createOrderUseCase.execute(req.toCommand());
        return ResponseEntity.status(201).body(CreateOrderResponse.from(result));
    }
}
// 次适配器（技术实现）
@Repository
public class PostgresOrderRepository implements OrderRepository {
    @Override public void save(Order order) { jpaRepo.save(mapper.toPO(order)); }
}
```

## 落地步骤

```
Phase 1: 定义端口（1-2 天）→ 入站端口(UseCase) → 出站端口(Repository/Gateway)
Phase 2: 领域模型（2-3 天）→ 聚合根/实体/值对象 → 领域服务 → 领域事件
Phase 3: 应用服务（1-2 天）→ UseCase 实现（注入端口，编排调用）
Phase 4: 适配器（2-4 天） → 主适配器(REST/gRPC/CLI) → 次适配器(DB/MQ/External)
Phase 5: DI 装配 + 测试（1-2 天）→ DI 配置 → 端口 Mock 测试 → 适配器集成测试
```

## Security & Stability

- 本技能为纯文档型架构指南，**不收集、不处理、不上传用户数据**。
- 所有代码模板均为教学参考。替换外部服务 URL、密钥和凭证为环境变量配置。
- Port/Adapter 隔离确保领域逻辑不直接依赖 HTTP/DB/MQ 库——Adapter 层处理所有 I/O。
- 实现 Secondary Adapter 时，始终设置连接/读取超时，对关键路径实现断路器模式。

## Gotchas（8 条常见陷阱）

1. **端口定义过宽**: 每个端口只做一件事。包含 10+ 方法的端口视为"上帝端口"，立即拆分。
2. **主适配器包含业务逻辑**: Controller 只能做参数转换和调用 UseCase，不能包含 if/else 业务判断。
3. **次适配器忘记异常转换**: 技术异常（SQLException、TimeoutException）必须在适配器内部转换为领域异常。
4. **领域层框架依赖**: Domain 模块不能 import Spring/JPA/MyBatis 注解。
5. **端口命名不一致**: 入站端口用动作命名（`CreateOrderUseCase`），出站端口用资源命名（`OrderRepository`）。
6. **事务放在适配器层**: 事务由应用层控制，适配器不负责事务管理。
7. **过度抽象**: 不为"未来可能会换"提前创建端口。等真正需要替换时再抽取端口。
8. **用户需求不清晰时先给假设**: 用户没说技术栈/入口类型/团队规模时，先给假设版本再补充提问。

## FAQ（8 条常见问题）

**Q1: 六边形和整洁架构有什么区别？** A: 六边形由 Cockburn 提出（2005），核心是端口/适配器；整洁由 Uncle Bob 提出（2012），强调 UseCase 和 Entity 分离。六边形更关注"对称性"（主/次适配器），整洁更关注"依赖规则"。
**Q2: 端口应该放在 Domain 层还是 Application 层？** A: 推荐放在 Domain 层。Domain 是业务核心，端口是业务对外部依赖的抽象。
**Q3: 如何避免端口过度抽象？** A: YAGNI 原则：只为当前确定的变更需求定义端口。
**Q4: 一个 UseCase 接口一个方法还是多个方法？** A: 推荐一个接口一个方法（接口隔离原则）。但高度相关的方法（如 OrderRepository 的 save/findById）可放同一接口。
**Q5: Controller 层的 DTO 和 Domain 层的 Entity 能否共用？** A: 不能。DTO 是适配器层的数据载体，Entity 是领域层的业务模型，需要 Mapper 转换。
**Q6: 六边形架构如何处理查询？** A: 查询也通过端口进行。使用 `QueryOrderUseCase` 返回只读 DTO，复杂查询可用 CQRS。
**Q7: 如何验证六边形边界是否正确？** A: 能否不启动数据库和 HTTP 就跑通 Domain 层全部单元测试？能 → 正确。不能 → 有泄漏。
**Q8: 团队不熟悉六边形架构怎么办？** A: 逐步引入。先做好 Domain 层纯净度和端口定义，再逐步抽取适配器。
## References

| 文件 | 目的 |
|------|------|
| [references/01-port-definitions.md](references/01-port-definitions.md) | 端口定义规范 — 入站/出站端口、命名、粒度、Strong/Weak |
| [references/02-primary-adapters.md](references/02-primary-adapters.md) | 主适配器详解 — REST/CLI/gRPC/MQ 四种适配器实现 |
| [references/03-secondary-adapters.md](references/03-secondary-adapters.md) | 次适配器详解 — JPA/MyBatis/Stripe/RabbitMQ/InMemory |
| [references/04-domain-model.md](references/04-domain-model.md) | 领域模型设计 — 聚合根、实体、值对象、领域服务、领域事件 |
| [references/05-application-services.md](references/05-application-services.md) | 应用服务层 — UseCase 实现、编排规范、命令对象 |
| [references/06-di-configuration.md](references/06-di-configuration.md) | DI 配置 — Spring Config、Profile 切换、多环境适配器 |
| [references/07-testing.md](references/07-testing.md) | 测试策略 — 领域层/应用层/适配器/架构 四级测试 |
| [references/08-migration.md](references/08-migration.md) | 渐进迁移 — 从传统三层到六边形的迁移指南 |
| [examples/01-order-hexagonal-complete.md](examples/01-order-hexagonal-complete.md) | 完整订单六边形示例 — Domain/Port/Service/Adapter 全流程 |
| [examples/02-user-registration-example.md](examples/02-user-registration-example.md) | 用户注册示例 — 值对象、验证码、领域事件 |
| [examples/03-multi-entry-points-example.md](examples/03-multi-entry-points-example.md) | 多入口系统示例 — 同一 UseCase 供 REST/CLI/Kafka/gRPC 调用 |
| [examples/04-adapter-swapping-example.md](examples/04-adapter-swapping-example.md) | 适配器可替换性示例 — Postgres→MongoDB、Stripe→PayPal 零代码修改 |
| [examples/05-port-swapping-test.md](examples/05-port-swapping-test.md) | 主适配器可替换性示例 — REST/gRPC/CLI 三种入口 + 端口级测试 |
| [examples/06-monolith-simple.md](examples/06-monolith-simple.md) | 单体简单六边形 — 单模块四包 + ports/adapters 子包结构 |
| [examples/07-monolith-complex.md](examples/07-monolith-complex.md) | 单体复杂六边形 — 多端口 + 多适配器 + 多聚合根 |
| [examples/08-monolith-multi-module.md](examples/08-monolith-multi-module.md) | 单体多模块六边形 — Maven 多模块编译期边界约束 |
| [examples/09-microservice-simple.md](examples/09-microservice-simple.md) | 微服务简单六边形 — 单微服务内最小六边形结构 |
| [examples/10-microservice-complex.md](examples/10-microservice-complex.md) | 微服务复杂六边形 — 多聚合 + Saga + 跨服务调用 |
| [examples/11-microservice-multi-module.md](examples/11-microservice-multi-module.md) | 微服务多模块六边形 — 每服务内部 Maven 多模块 |
| [examples/12-microservice-complex-multi.md](examples/12-microservice-complex-multi.md) | 微服务复杂多模块 — CQRS + 读写分离 + CDC + 分布式 Saga |

### Primary Sources
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — Alistair Cockburn (2005)
- [Hexagonal Architecture Explained](https://openlibrary.org/works/OL38388131W) — Cockburn & Garrido de Paz (2024)
- [Domain-Driven Design: The Blue Book](https://www.domainlanguage.com/ddd/blue-book/) — Eric Evans (2003)
- [AWS: Hexagonal Architecture Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

### 导航

- **→ Next**: [domain-designer](../ddd-domain-designer/) — 为六边形架构设计领域模型
- **🔗 Related**: [testing-strategist](../ddd-testing-strategist/) — 端口 Mock 测试 | [api-designer](../ddd-api-designer/) — 六边形 API 设计
> 💡 六边形 = 端口 + 适配器。验证法：不启动数据库和 HTTP，只跑 CLI/单元测试就能执行业务逻辑 → 边界正确。
