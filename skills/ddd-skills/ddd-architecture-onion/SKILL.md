---
name: ddd-architecture-onion
description: Comprehensive guidance for Onion Architecture (洋葱架构) — Jeffrey Palermo's onion architecture with domain-centric layered isolation, dependency inversion from outer to inner rings. Covers domain core, application interfaces, infrastructure implementation, and API adapters with full Java/Spring Boot examples. Use when user asks about onion architecture, 洋葱架构, Jeffrey Palermo, concentric architecture, or needs layered domain isolation.
license: Apache-2.0
---

# DDD Architecture — Onion (洋葱架构)

基于 Jeffrey Palermo（2008）提出的同心圆架构模型，以 Domain 为圆心，依赖方向严格指向内层。

## Workflow

```
用户提问                         本 Skill 回答流程
──────────                      ──────────────────
"帮我用洋葱架构建项目"       → 1. 判断适用性 → 2. 搭建目录骨架 → 3. 编写 Domain 核心 → 4. 编写 Application 接口
"我想把三层架构改成洋葱"     → 5. 编写 Infrastructure 实现 → 6. 编写 API 适配器 → 7. 配置 DI 组装 → 8. 编写测试
"洋葱架构有什么坑"           → 9. 对照 Gotchas 清单检查
```

**输出模板**：回答始终包含以下结构，用户可跳过已了解的部分：

```
1. [适用性判断] 项目是否符合洋葱架构条件
2. [目录结构]   四层模块骨架（core/infrastructure/api/composition）
3. [Domain 层]  聚合根、值对象、仓储接口
4. [Application] 应用服务接口与实现
5. [Infrastructure] 仓储实现、MQ、外部集成
6. [API 层]     REST 控制器
7. [Composition] DI 装配配置
8. [测试]       单元测试 + 集成测试
9. [Gotchas]    检查常见陷阱
```

## When to Use Onion Architecture

| ✅ 适用场景 | ❌ 不适用 |
|-----------|----------|
| 基础设施频繁变更（DB/MQ/缓存厂商更换） | 简单 CRUD 项目（过度设计，成本>收益） |
| 单元测试覆盖率要求 > 80% | 两周交付的原型/PoC |
| 多入口系统（REST + CLI + MQ + gRPC） | 单入口 + 单数据库的简单服务 |
| 团队有接口抽象和 DI 设计能力 | 团队刚接触 DDD，不熟悉依赖倒置 |
| 业务规则复杂，需要严格隔离 | 业务逻辑简单，三层架构够用 |

### Boundary：Skill 边界

| 区域 | 归属 |
|------|------|
| 三层→洋葱的迁移策略 | ✅ 本 Skill 处理（含 references/07-migration） |
| 洋葱 vs 六边形 vs 整洁对比 | ✅ 本 Skill 处理（含 references/08-comparison） |
| 选型决策 | ❌ 用 `ddd-architecture-selector` |
| 领域建模 | ❌ 用 `ddd-domain-designer` |
| 代码审查 | ❌ 用 `ddd-code-reviewer` |
| 中文企业 COLA 项目 | ❌ 用 `ddd-architecture-cola` |

## 核心原理：同心圆依赖规则

```
所有依赖关系指向圆心（Domain），内层定义接口，外层实现接口。

     ┌──────────────────────────────────────┐
     │        Infrastructure Layer           │  ← 最外层：技术细节
     │    ┌──────────────────────────────┐   │      DB 实现、MQ、HTTP 客户端
     │    │       API / Adapters          │   │  ← 用户界面层
     │    │    ┌──────────────────────┐   │   │      Controller、DTO、Middleware
     │    │    │   Application Layer   │   │   │  ← 应用层：用例编排
     │    │    │  ┌────────────────┐   │   │   │      事务边界、服务组合
     │    │    │  │   Domain Core   │   │   │   │  ← 核心层：零依赖
     │    │    │  │  ★              │   │   │   │      实体、值对象、聚合根
     │    │    │  └────────────────┘   │   │   │      仓储接口、领域服务
     │    │    └──────────────────────┘   │   │
     │    └──────────────────────────────┘   │
     └──────────────────────────────────────┘
```

### Jeffrey Palermo 四原则

1. **应用核心独立于基础设施** — Domain 层不 import 任何框架/数据库类
2. **内层定义接口，外层实现** — 如 `OrderRepository` 接口在 Domain，实现在 Infrastructure
3. **依赖指向圆心** — Infrastructure → Application → Domain，不允许逆向
4. **外层知道内层，内层不知道外层** — Domain 对 Infrastructure 一无所知

### 与六边形/整洁架构的对比

| 维度 | 洋葱架构 | 六边形架构 | 整洁架构 |
|------|---------|-----------|---------|
| 心智模型 | 同心圆嵌套 | 六边形 + 端口/适配器 | 四圈层 + 用例驱动 |
| 可视化程度 | ★★★ 最直观 | ★★☆ | ★★☆ |
| 接口组织 | 按层（Domain 定义仓储接口） | 按端口（inbound/outbound） | 按用例（Input/Output Port） |
| 典型目录 | core/infrastructure/api/composition | domain/adapter/configuration | usecase/entity/adapter/framework |
| 最佳场景 | 领域复杂的单体或多入口系统 | API 集成多的微服务 | 企业级大型系统 |

## 完整目录结构

```
{project}/
├── {project}-core/                        # 核心层（Domain + Application 接口）
│   ├── domain/                            # 领域模型（零框架依赖）
│   │   ├── model/                         # 实体、值对象、聚合根
│   │   │   ├── {aggregate-name}/
│   │   │   │   ├── {Aggregate}Root.java   # 聚合根
│   │   │   │   ├── {Entity}.java          # 实体
│   │   │   │   └── {ValueObject}.java     # 值对象
│   │   │   └── shared/                    # 共享值对象（Money, Email, Address）
│   │   ├── service/                       # 领域服务
│   │   ├── repository/                    # ★ 仓储接口（纯抽象，定义在 Domain）
│   │   ├── event/                         # 领域事件
│   │   └── exception/                     # 领域异常
│   └── application/                       # 应用服务接口（契约定义）
│       └── service/                       # 应用服务接口
├── {project}-infrastructure/              # 基础设施层
│   ├── data/                              # 数据访问
│   │   ├── repository/                    # ★ 仓储实现（实现 Domain 层接口）
│   │   ├── entity/                        # JPA Entity / PO 持久化对象
│   │   └── mapper/                        # PO ↔ Domain 映射
│   ├── messaging/                         # 消息队列
│   ├── external/                          # 外部 API 客户端
│   └── config/                            # 基础设施配置
├── {project}-api/                         # API / 适配器层
│   ├── controller/                        # REST 控制器
│   ├── dto/                               # 请求/响应 DTO
│   │   ├── request/
│   │   └── response/
│   ├── assembler/                         # DTO ↔ Domain 组装器
│   ├── middleware/                        # 拦截器、异常处理
│   └── swagger/                           # API 文档
└── {project}-composition/                 # DI 组装层（唯一知道所有实现的模块）
    └── config/                            # Spring Boot @Configuration / 手动 DI
```

### 模块职责边界

| 模块 | 可依赖 | 不可依赖 |
|------|--------|---------|
| core/domain | 无（纯 Java） | Spring/JPA/MyBatis/任何框架 |
| core/application | domain | infrastructure, api |
| infrastructure | core | api |
| api | core, infrastructure | — |
| composition | 所有模块 | — |

## 开发规范

### 规范清单

| # | 规范 | 说明 | 违规示例 |
|---|------|------|---------|
| 1 | Domain 零框架依赖 | 不 import `@Service`, `@Entity`, `JpaRepository` | `import org.springframework.stereotype.Service` |
| 2 | Repository 接口定义在 Domain | 接口在内层，实现在外层 Infrastructure | 接口和实现都在 Infrastructure |
| 3 | Application 只编排不实现 | 不放 if/else 业务规则，只协调领域对象 | AppService 包含状态机逻辑 |
| 4 | 事务边界在 Application | 用 `@Transactional` 在 AppService 层 | 在 Controller 或 Repository 开事务 |
| 5 | 跨聚合通过领域事件 | 聚合间用 ID 引用，跨聚合操作用事件最终一致 | 聚合 A 直接引用聚合 B 的实体 |
| 6 | 值对象不可变 | 字段 `final`，无 setter，提供工厂方法 | ValueObject 有 setter 方法 |
| 7 | 实体充血模型 | 业务方法在实体内部，不在 Service | 实体只有 getter/setter |
| 8 | DTO 在 API 层定义 | 不把 DTO 传到 Domain 层 | `import api.dto.OrderDTO` 在 Domain 中 |
| 9 | Composition Root 最外层 | DI 配置集中在一个地方，不散落到各层 | 各层自己 `new` 依赖对象 |
| 10 | 严格分层 | 每层只能调用直接下方层 | API 直接调用 Infrastructure |

### 代码规范示例

```java
// ✅ 正确：Domain 定义接口
// core/domain/repository/OrderRepository.java
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
}

// ✅ 正确：Infrastructure 实现接口
// infrastructure/data/repository/OrderRepositoryImpl.java
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    private final JpaOrderRepository jpaRepo;       // Spring Data
    private final OrderMapper mapper;               // PO ↔ Domain

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue())
            .map(mapper::toDomain);
    }
}

// ❌ 错误：Domain 直接依赖 JPA
// core/domain/repository/OrderRepository.java
public interface OrderRepository extends JpaRepository<Order, Long> {  // 违规！
}
```

## 落地实施步骤

```
Phase 1: 识别核心域模型（1-2 天）
  └─ 确定聚合根、实体、值对象 → 定义 Repository 接口 → 定义领域事件

Phase 2: 搭建 Core 层（1 天）
  └─ 创建 core/domain/ 模块 → 编写充血模型实体 → 定义 Application 接口

Phase 3: 实现 Infrastructure 层（2-3 天）
  └─ 实现 Repository（JPA/MyBatis）→ 实现 MQ → 实现外部 API 客户端
  └─ 编写 PO 实体和 Mapper 映射

Phase 4: 实现 API 适配层（1-2 天）
  └─ Controller → DTO → Assembler → 异常处理 → Swagger

Phase 5: 组装与测试（1-2 天）
  └─ Composition Root 配置 DI → 单元测试（Domain）→ 集成测试（Repository）
```

### 迁移路径：从三层层到洋葱

详见 [references/07-migration-from-layered.md](references/07-migration-from-layered.md)

## Gotchas — 常见陷阱（15 条）

| # | 陷阱 | 症状 | 修复 |
|---|------|------|------|
| 1 | **Domain 层泄露框架类型** | Domain 中 import `JpaRepository`, `@RestController` | 删除违规 import，接口放到 Domain，实现在 Infra |
| 2 | **Repository 接口位置错误** | 接口和实现都在 Infrastructure 层 | 把接口移到 Domain 层，Infra 实现它 |
| 3 | **Application 层过厚** | AppService 包含 if/else 业务判断 | 提取到 Domain Service |
| 4 | **过度抽象** | 日志/配置也定义成 Port 接口 | 只对需要替换的部分（DB/MQ/缓存）抽象 |
| 5 | **Composition Root 分散** | 各层用 `@Autowired` 或自己 `new` 依赖 | 集中到 composition/config |
| 6 | **值对象可变** | ValueObject 有 setter，`equals/hashCode` 未覆盖 | 改用 `final` 字段 + 构造器 |
| 7 | **聚合根过大** | 一个聚合包含超过 5 个实体 | 拆分聚合，用 ID 引用 |
| 8 | **跨聚合直接引用** | 聚合 A 的 `List<聚合B>` 字段 | 改为 `List<BId>`，用 ID 引用 |
| 9 | **Controller 包含业务逻辑** | Controller 中有 if/else 业务判断 | 移到 Application 或 Domain |
| 10 | **DTO 泄露到 Domain** | Domain 中引用 api.dto 包 | 用 Assembler 在 API 层转换 |
| 11 | **Domain 层放 PO 注解** | Domain model 上有 `@Entity`, `@Table` | PO 放在 Infrastructure，用 Mapper 转换 |
| 12 | **Application 层忽略编排职责** | AppService 直接暴露 Domain 实体 | AppService 返回 DTO，不暴露 Domain |
| 13 | **缺少领域事件** | 关键业务操作无事件记录 | 在实体方法中 `addDomainEvent()` |
| 14 | **事务跨多个聚合** | 一个 `@Transactional` 涉及 2+ 聚合 | 改用领域事件 + 最终一致性 |
| 15 | **Infrastructure 侵入测试** | 单元测试需要启动 Spring/数据库 | 用 Mock Repository 测试 Domain 和 Application |

## FAQ — 常见问题（15 条）

### Q1: 洋葱架构和六边形架构有什么区别？
A: 洋葱强调"同心圆分层"的心智模型，可视化更直观；六边形强调"端口+适配器"的抽象。两者本质都是依赖倒置，洋葱更适用于需要清晰层间隔离的场景。

### Q2: Domain 层真的不能有任何框架注解吗？
A: 是的。Domain 层必须是纯业务逻辑，不能 import `@Entity`, `@Service`, `@Repository`。这些注解出现在 Domain 层意味着依赖方向反了。

### Q3: 值对象和实体的判断标准是什么？
A: 有唯一标识且可变 → 实体；无标识且不可变 → 值对象。如 `OrderId` 是值对象，`Order` 是实体（聚合根）。

### Q4: Repository 接口为什么放在 Domain 层？
A: Domain 层定义"我需要什么持久化能力"，Infrastructure 层实现"怎么持久化"。接口在 Domain 确保了 Domain 不依赖 Infrastructure。

### Q5: 单个聚合内应该包含几个实体？
A: Vaughn Vernon 建议 ≤ 5 个。超过时考虑是否聚合边界过大，需要拆分。

### Q6: Application 层太薄怎么办？
A: 这是正确的。Application 层应该薄——它只做编排。业务逻辑应该在 Domain 层。如果觉得"空"，说明 Domain 层设计得好。

### Q7: 如何从三层架构迁移到洋葱架构？
A: 详见 [references/07-migration-from-layered.md](references/07-migration-from-layered.md)。推荐渐进式迁移：先抽 Repository 接口，再分离 Domain 模块。

### Q8: 洋葱架构支持 CQRS 吗？
A: 支持。在 Application 层做 Command/Query 分离，Command 走完整的 Domain 逻辑，Query 直接读 Repository。详见 `ddd-cqrs-architecture`。

### Q9: 单元测试要覆盖哪些层？
A: Domain 层 100% 覆盖（无框架依赖，最易测试），Application 层 Mock 所有依赖测试编排逻辑，Infrastructure 层用 Testcontainers 做集成测试。

### Q10: Composition Root 一定要单独模块吗？
A: 推荐。单独的 composition 模块是唯一知道所有实现类型的模块，它负责装配。小项目可以放在启动模块中，但不要分散。

### Q11: 多个聚合之间如何通信？
A: 通过 Application 层编排，或通过领域事件实现最终一致性。禁止聚合间直接调用领域服务。

### Q12: 洋葱架构适合微服务吗？
A: 非常适合。每个微服务内部按洋葱组织，对外暴露 API 适配层。多入口场景（REST + MQ + gRPC）是洋葱的强项。

### Q13: 值对象如何在数据库中持久化？
A: 两种方式：嵌入式（`@Embeddable` 在 JPA 中）→ 适合小值对象；序列化 → 适合复杂值对象。转换逻辑在 Mapper 中。

### Q14: 领域事件如何处理跨微服务通信？
A: Application 层发布领域事件 → Infrastructure 层的 EventPublisher 发送到 MQ → 其他微服务订阅处理。注意幂等设计。

### Q15: 为什么说洋葱架构"抗变化"？
A: 因为所有技术细节（DB/MQ/HTTP）都在外层 Infrastructure，内层 Domain 不受影响。换数据库只需改 Infrastructure 层，Domain 层完全不动。

## Keywords

```
onion architecture, 洋葱架构, Jeffrey Palermo, domain-centric architecture,
layered isolation, dependency inversion, 依赖倒置, concentric layers,
core/domain, application interfaces, infrastructure implementation,
API adapters, composition root, DI assembly, domain model,
repository pattern, aggregate root, value object, domain service,
严格分层, 内层定义接口, 外层实现接口, 依赖指向圆心,
DDD layered, clean architecture comparison, hexagonal comparison
```

## References

| 文件 | 用途 |
|------|------|
| [references/01-domain-model.md](references/01-domain-model.md) | 领域层设计详解：聚合根、值对象、领域服务 |
| [references/02-application-interfaces.md](references/02-application-interfaces.md) | 应用层接口设计：服务编排与事务边界 |
| [references/03-infrastructure-implementation.md](references/03-infrastructure-implementation.md) | 基础设施层实现：Repository、MQ、外部集成 |
| [references/04-api-adapters.md](references/04-api-adapters.md) | API 适配层：Controller、DTO、Assembler |
| [references/05-di-composition.md](references/05-di-composition.md) | DI 组装：Composition Root 配置 |
| [references/06-testing.md](references/06-testing.md) | 测试策略：单元测试、集成测试、契约测试 |
| [references/07-migration-from-layered.md](references/07-migration-from-layered.md) | 从三层架构迁移到洋葱架构的完整路径 |
| [references/08-comparison.md](references/08-comparison.md) | 洋葱 vs 六边形 vs 整洁架构详细对比 |

## Examples

| 示例 | 说明 |
|------|------|
| [examples/example-01-order-payment.md](examples/example-01-order-payment.md) | 订单支付完整示例（含 Domain/Application/Infra/API） |
| [examples/example-02-product-catalog.md](examples/example-02-product-catalog.md) | 产品目录管理示例（含多聚合协作） |
| [examples/example-03-multi-entry.md](examples/example-03-multi-entry.md) | 多入口系统示例（REST + MQ + CLI 三种适配器） |
| [examples/example-04-cqrs-onion.md](examples/example-04-cqrs-onion.md) | CQRS + 洋葱融合示例（Command/Query 分离） |

## Primary Sources

- [Onion Architecture: Part 1](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) — Jeffrey Palermo (2008)
- [Onion Architecture: Part 2](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-2/) — Jeffrey Palermo (2008)
- [Onion Architecture: Part 3](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-3/) — Jeffrey Palermo (2008)
- [Onion Architecture: Part 4](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-4/) — Jeffrey Palermo (2008)
- [Domain-Driven Design: The Blue Book](https://www.domainlanguage.com/ddd/blue-book/) — Eric Evans (2003)
- [Implementing Domain-Driven Design](https://www.domainlanguage.com/ddd/blue-book/) — Vaughn Vernon (2013)
- [Clean Architecture: Standing on the Shoulders of Giants](https://herbertograca.com/2017/09/28/clean-architecture-standing-on-the-shoulders-of-giants/) — Herberto Graça

## Implementation Guides

- [Microsoft: DDD-oriented Microservice](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice)
- [Testcontainers for Integration Testing](https://testcontainers.com/)

## Output

回答输出始终包含：
- 适用性判断（项目是否适合洋葱架构）
- 完整目录结构（四层模块）
- 每层代码模板（Domain / Application / Infrastructure / API）
- DI 装配配置
- 测试骨架
- Gotchas 合规检查
- 扩展参考（references/ 和 examples/ 目录的引导引用）

---

## 技能旅程

> 📍 **当前 Skill：洋葱架构落地**

← **上一步**：[selector](../ddd-architecture-selector/) — 架构选型
→ **下一步**：[domain-designer](../ddd-domain-designer/) — 设计领域模型
🔗 **相关**：[cqrs-architecture](../ddd-cqrs-architecture/) — CQRS 集成 | [code-reviewer](../ddd-code-reviewer/) — 架构审查
🏠 **首页**：[awesome](../ddd-architecture-awesome/) — DDD 入门全景

> 核心口诀：内层定义接口，外层实现接口，依赖指向圆心。
