# DDD Skills 生态体系设计说明

> 版本：v4.0 | 架构落地全面升级：5 种架构独立 Skill + CQRS 混合方案 + 16 个 Skill 生态

---

## 一、设计哲学

### 1.1 为什么重新设计

v1.x 的问题：**按 DDD 学术概念组织技能**（事件风暴 → 领域建模 → CQRS → 审查），隐含前提是用户已经懂 DDD。

v3.x 的局限：**架构落地只有一个 COLA**，缺少 Layered/Onion/Hexagonal/Clean 等主流架构的独立 Skill，且 CQRS 定位模糊。

现实是：**大多数后端开发者不懂 DDD 的复杂概念**。他们想知道的是：

| 用户真正想问的 | v3.x 技能名 | v4.0 改进 |
|--------------|------------|----------|
| "什么是 DDD？我该不该用？" | `awesome` | ✓ 保留 |
| "我的项目该用哪种架构？" | `selector` | ✓ 保留，增强到 5 种架构对比 |
| "每种架构具体怎么落地？" | 只有一个 COLA | **新增 5 个独立架构 Skill** |
| "怎么搭一个 COLA 项目？" | `cola-creator` | 合并进 `ddd-architecture-cola` |
| "CQRS 怎么落地？" | `cqrs-implementer` | **独立 Skill + 内嵌各架构** |
| "怎么审查代码是否符合 DDD？" | `code-reviewer` | ✓ 保留 |
| "架构文档怎么写？" | `doc` | ✓ 保留 |
| "架构怎么演进？" | 无 | **新增 `architecture-evaluator`** |

### 1.2 v4.0 设计原则

**技能按用户学习和使用路径组织，而非 DDD 学术概念**：

```
用户旅程：我不知道 DDD → 我学一下 → 我选个架构 → 我落地实现 → 我审查代码 → 我评估演进 → 我出文档
                                ↓
                    ┌───────────┼───────────┬───────────┬───────────┐
                    ↓           ↓           ↓           ↓           ↓
               Layered      Onion     Hexagonal     Clean       COLA
```

| 原则 | 说明 |
|------|------|
| **教学优先** | `awesome` 是第一入口，从零教 DDD，不假设用户已有知识 |
| **架构平等** | 5 种架构各有独立 Skill，不是 COLA 一家独大 |
| **按需取用** | 用户不需要走完整链路，每个 skill 可独立使用 |
| **输出可操作** | 每个 skill 输出代码、配置、DDL、文档，不是泛泛建议 |
| **反例驱动** | 用"常见错误+怎么改"比纯理论更有用 |
| **多语言兼容** | 概念讲清楚后，Go/Rust/Python/TypeScript/Java/C# 各自落地 |
| **CQRS 独立存在** | 既是架构 Skill 间的共享设计模式，又可作为独立 Skill 深度落地 |

---

## 二、知识输入全景图

### 2.1 知识来源总览

```
                    clean-ddd-hexagonal              xfg-ddd-skills
               ┌─────────────────────────┐    ┌──────────────────────┐
               │ SKILL.md (全貌)          │    │ 六边形架构编码规范     │
               │ LAYERS.md (分层详解)      │    │ 实体/值对象/聚合模板   │
               │ DDD-STRATEGIC.md (战略)   │    │ 仓储/工厂/服务模板     │
               │ DDD-TACTICAL.md (战术)    │    │ 测试规范              │
               │ HEXAGONAL.md (六边形)     │    └──────────────────────┘
               │ CQRS-EVENTS.md (CQRS)    │
               │ TESTING.md (测试策略)     │    cleanddd-skills
               │ CHEATSHEET.md (速查)     │    ┌──────────────────────┐
               └──────────┬──────────────┘    │ 需求分析 → 领域建模   │
                          │                   │ → 项目初始化 → 编码   │
    ┌──────────────────────────────┐
    │ DDD思维导图 / CQRS思维导图    │       partme-docs/ddd
    │ ddd/1-4 四种架构目录          │  ┌────────────────────────────┐
    │ blogs/ 三篇深度文章           │  │ 01-05 基础篇 (战略设计)     │
    └──────────┬───────────────────┘  │ 06-10 进阶篇 (架构落地)     │
               │                      │ 11-20 实战篇 (端到端实战)   │
               │                      │ 91    加餐 (完整代码)       │
               │                      └──────────┬─────────────────┘
               │           ┌─────────────────────┘
               ▼           ▼
        ┌──────────────────────────────────────────────────────────┐
        │                  DDD Skills 生态 (v4.0) 16 Skills         │
        └──────────────────────────────────────────────────────────┘
```

### 2.2 每份知识源对各 Skill 的贡献矩阵

| 知识源 | awesome | selector | layered | onion | hexa | clean | cola | cqrs | domain | api | reviewer | evaluator | storming | testing | devops | doc |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **clean-ddd-hexagonal** SKILL.md | ● | ● | ○ | ○ | ● | ○ | ○ | ● | ● | ● | ● | ○ | ○ | ○ | ○ | ○ |
| clean-ddd LAYERS.md | ● | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ |
| clean-ddd DDD-STRATEGIC.md | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| clean-ddd DDD-TACTICAL.md | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ● | ○ | ○ | ○ | ○ | ○ |
| clean-ddd HEXAGONAL.md | ○ | ● | ○ | ○ | ● | ● | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| clean-ddd CQRS-EVENTS.md | ○ | ● | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| clean-ddd TESTING.md | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ● | ○ | ○ |
| clean-ddd CHEATSHEET.md | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| **cleanddd-skills** | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| **xfg-ddd-skills** | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ |
| **partme-docs** 01-05 基础篇 | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ● | ○ | ● | ○ | ● | ○ | ○ | ○ |
| partme-docs 06-10 进阶篇 | ○ | ● | ○ | ○ | ● | ○ | ● | ● | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| partme-docs 11-20 实战篇 | ○ | ○ | ○ | ○ | ○ | ● | ● | ● | ● | ● | ● | ● | ○ | ● | ● | ● |
| partme-docs 91 加餐 | ○ | ○ | ○ | ○ | ○ | ○ | ● | ● | ● | ○ | ● | ○ | ○ | ○ | ○ | ○ |

> ● 核心依赖  ○ 参考依赖

---

## 三、技能全景图

### 3.1 按用户旅程排列（v4.0）

```
第1步：我该不该用DDD？
        │
        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  ddd-architecture-awesome                                       │
  │  DDD 入门教学 + 概念速查 + 适用性判断                             │
  │  "什么是DDD？核心概念是什么？我该用吗？"                            │
  └────────────────────────────┬────────────────────────────────────┘
                               │
第2步：我该选哪种架构？           │
        │                      ▼
        │   ┌─────────────────────────────────────────────────────────┐
        │   │  ddd-architecture-selector                              │
        │   │  5 种架构对比 + 决策矩阵 + 域划分                          │
        │   │  "Layered/Onion/Hexagonal/Clean/COLA 我该选哪个？"        │
        │   └────────────────────────────┬────────────────────────────┘
        │                                │
第3步：落地实现（5 种架构独立 Skill）     │
        │     ┌──────────┬──────────┬──────────┬──────────┬──────────┐
        │     ▼          ▼          ▼          ▼          ▼          ▼
        │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────────────┐
        │  │layered│ │onion │ │hexa- │ │clean │ │      cola        │
        │  │      │ │      │ │gonal │ │      │ │ (creator+validator│
        │  │分层  │ │洋葱  │ │六边形│ │整洁  │ │    合并)          │
        │  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └────────┬─────────┘
        │     │        │        │        │               │
        │     └────────┴────────┴────────┴───────────────┘
        │                      │
第4步：领域设计与API设计          │
        │     ┌─────────────────┼──────────────────┐
        │     ▼                 ▼                  ▼
        │  ┌──────────────┐ ┌────────────────┐ ┌──────────────────┐
        │  │ddd-domain-   │ │ddd-cqrs-       │ │ddd-api-designer  │
        │  │designer      │ │architecture    │ │                  │
        │  │(从domain-    │ │(混合方案C:      │ │领域模型→API规范  │
        │  │ modeling重命名)│ │独立Skill+各架构 │ │BFF+数据转换链    │
        │  │领域建模全流程 │ │内嵌CQRS模式)   │ │                  │
        │  └──────┬───────┘ └───────┬────────┘ └────────┬─────────┘
        │         │                │                    │
第5步：质量保障                    │                    │
        │         └────────────────┼────────────────────┘
        │                          ▼
        │  ┌──────────────────────────────────────────────────────────┐
        │  │  ddd-code-reviewer                                        │
        │  │  DDD 反模式检测 + 分层合规检查 + 代码质量评分                 │
        │  │  "我的代码符合 DDD 吗？"                                    │
        │  └────────────────────────────┬─────────────────────────────┘
        │                               │
第6步：辅助能力层                       │
        │     ┌──────────┬──────────┬──────────┬──────────┐
        │     ▼          ▼          ▼          ▼          │
        │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐    │
        │  │event-  │ │testing │ │devops- │ │evalua- │    │
        │  │storming│ │strategist│ │integ-  │ │tor     │    │
        │  │        │ │        │ │ration  │ │        │    │
        │  │事件风暴│ │测试策略│ │DevOps  │ │架构评估│    │
        │  │工作坊  │ │        │ │集成    │ │与演进  │    │
        │  └────────┘ └────────┘ └────────┘ └────────┘    │
        │                                                  │
第7步：文档输出                                            │
        │                                                  │
        └──────────────────────────────────────────────────┘
                               ▼
        ┌──────────────────────────────────────────────────────────┐
        │  ddd-architecture-doc                                     │
        │  架构文档生成 + ADR + C4 图 + 架构决策记录                   │
        │  "怎么把架构讲清楚给团队看？"                                 │
        └──────────────────────────────────────────────────────────┘
```

### 3.2 技能调用路径（v4.0）

| 用户类型 | 推荐路径 |
|----------|---------|
| **DDD 新手** | awesome → selector → (选架构 Skill) → code-reviewer |
| **架构师/技术负责人** | selector → (选架构 Skill) → domain-designer → doc |
| **已有项目迁移 DDD** | awesome → selector → (选架构 Skill) → reviewer → evaluator |
| **选 Layered 架构** | selector → architecture-layered → domain-designer |
| **选 Onion 架构** | selector → architecture-onion → domain-designer |
| **选 Hexagonal 架构** | selector → architecture-hexagonal → domain-designer + api-designer |
| **选 Clean 架构** | selector → architecture-clean → domain-designer |
| **选 COLA 架构** | selector → architecture-cola → domain-designer → api-designer |
| **需要 CQRS** | selector → cqrs-architecture（独立使用）或 → (选架构 Skill，内嵌 CQRS 模式) |
| **微服务+事件驱动** | selector → (架构 Skill) → cqrs-architecture → api-designer |
| **代码审查** | code-reviewer (独立使用) |
| **架构评估** | evaluator (按周期使用) |
| **出架构文档** | doc (独立使用，读现有代码) |
| **事件风暴工作坊** | event-storming (独立使用或配合 domain-designer) |
| **制定测试策略** | testing-strategist (独立使用或配合架构 Skill) |
| **DevOps 集成** | devops-integration (配合 CI/CD 流水线) |

### 3.3 技能与实现语言解耦

所有 skill 的描述、概念、决策树均为**语言无关**。语言相关的代码模板和脚手架放在各 skill 的 references 目录中：

```
ddd-architecture-awesome/
├── SKILL.md                          # 语言无关的教学内容
└── references/
    ├── java-examples.md              # Java 代码示例
    ├── go-examples.md                # Go 代码示例
    ├── typescript-examples.md        # TypeScript 代码示例
    └── ...
```

### 3.4 目录结构约定

每个 Skill 拥有独立目录，命名遵循 `ddd-{domain}-{name}` 格式：

```
skills/
├── ddd-skills/
│   ├── DESIGN.md                      # 本文件
│   ├── ddd-architecture-awesome/      # Skill 1
│   ├── ddd-architecture-selector/     # Skill 2
│   ├── ddd-architecture-layered/      # Skill 3
│   ├── ddd-architecture-onion/        # Skill 4
│   ├── ddd-architecture-hexagonal/    # Skill 5
│   ├── ddd-architecture-clean/        # Skill 6
│   ├── ddd-architecture-cola/         # Skill 7（合并 creator+validator）
│   ├── ddd-domain-designer/           # Skill 8（重命名自 domain-modeling）
│   ├── ddd-cqrs-architecture/         # Skill 9（混合方案 C）
│   ├── ddd-api-designer/              # Skill 10
│   ├── ddd-code-reviewer/             # Skill 11
│   ├── ddd-architecture-evaluator/    # Skill 12
│   ├── ddd-event-storming/            # Skill 13
│   ├── ddd-testing-strategist/        # Skill 14
│   ├── ddd-devops-integration/        # Skill 15
│   └── ddd-architecture-doc/          # Skill 16
```

---

## 四、Skill 详细设计

---

### Skill 1：ddd-architecture-awesome

**定位**：DDD 入门教学 — 生态的第一入口

**触发词**：`DDD 入门`、`什么是领域驱动设计`、`DDD 概念`、`DDD vs 传统三层`、`充血模型 vs 贫血模型`、`什么时候用 DDD`、`entity value object aggregate`、`DDD tutorial`

**核心能力**：

```
用户问：             awesome 回答：
──────────────────────────────────────────────
什么是 DDD？         → 一句话定义 + 战略/战术二分
DDD 解决什么问题？    → 复杂业务建模 vs CRUD 困境
核心概念有哪些？      → Entity/ValueObject/Aggregate/Repository/DomainEvent/DomainService
我该不该用 DDD？     → 决策树（团队规模/业务复杂度/项目生命周期）
有什么架构可选？      → 5 种架构概览（Layered/Onion/Hexagonal/Clean/COLA）+ CQRS/EventSourcing
和传统三层有什么不同？ → 依赖方向对比图 + 代码对比
```

**架构概览（5 种 + CQRS + Event Sourcing）**：

```
传统分层    洋葱架构    六边形架构     整洁架构       COLA v5       CQRS      Event Sourcing
┌──────┐  ┌──────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───┐┌───┐  ┌──────────┐
│ 表现  │  │ 表现  │  │ Adapter  │  │ Frameworks│  │ Adapter  │  │ C ││ Q │  │EventStore│
├──────┤  ├──────┤  ├──────────┤  ├──────────┤  ├──────────┤  │ M ││ R │  ├──────────┤
│ 业务  │  │ Domain│  │  Ports   │  │ Adapter   │  │   App    │  │ D ││ Y │  │ Projector│
├──────┤  │ ★    │  ├──────────┤  ├──────────┤  ├──────────┤  │ ★ ││ ★ │  ├──────────┤
│ 持久  │  │ Infra │  │ Domain ★ │  │ Domain ★ │  │ Domain ★ │  └───┘└───┘  │  Query   │
└──────┘  └──────┘  └──────────┘  └──────────┘  └──────────┘             └──────────┘
```

**充血模型 vs 贫血模型（最直观的对比）**：

```java
// 贫血模型（传统三层）— 不推荐
public class Order {
    private Long id;
    private String status;       // 只有数据，没行为
    // getter/setter ...
}
public class OrderService {
    public void pay(Long orderId) {  // 行为在 Service
        Order order = orderRepo.findById(orderId);
        if ("DRAFT".equals(order.getStatus())) {
            order.setStatus("PAID");    // 直接 set，无业务语义
        }
    }
}

// 充血模型（DDD）— 推荐
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;      // 用值对象代替字符串

    public void pay() {              // 行为在实体
        if (!status.canPay()) {
            throw new OrderException("当前状态不可支付");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaid(this.id));
    }
}
```

**输出**：
- DDD 概念速查表
- "我该不该用 DDD"决策结果
- 推荐架构模式（引导到 selector）
- 推荐下一步技能

**参考来源**：
- clean-ddd-hexagonal SKILL.md（决策树、反模式表、什么时候用/不用）
- clean-ddd-hexagonal CHEATSHEET.md（概念速查）
- partme-docs 01（DDD 是什么）、02（域三分法）、04（实体与值对象）、05（聚合）

---

### Skill 2：ddd-architecture-selector

**定位**：架构选型决策 — 帮用户从 5 种架构中选出最适合的那个

**触发词**：`架构选型`、`COLA vs 六边形`、`整洁架构 vs 洋葱`、`微服务拆分`、`该用哪种架构`、`分层策略`、`CQRS 要不要`、`项目结构怎么定`

**核心能力**：

#### 1. 5 种架构决策矩阵

| 维度 | 传统分层 | 洋葱 | 六边形 | 整洁 | COLA |
|------|:--:|:--:|:--:|:--:|:--:|
| 学习成本 | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ |
| 业务复杂项目适用度 | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| 简单 CRUD 效率 | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★☆ |
| 基础设施可替换性 | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★☆ |
| 测试友好度 | ★☆☆ | ★★★ | ★★★ | ★★★ | ★★★ |
| 国内社区活跃度 | ★★★ | ★☆☆ | ★☆☆ | ★☆☆ | ★★★ |
| 适合团队规模 | 1-5人 | 5-15人 | 5-15人 | 15-50人 | 5-50人 |
| 架构来源 | Martin Fowler | Jeffrey Palermo | Alistair Cockburn | Robert C. Martin | Alibaba |

#### 2. 团队规模与架构匹配

```
团队 1-5 人    → 传统分层（简单场景）或 COLA（单模块简化版）
团队 5-15 人   → 六边形 / 洋葱 / COLA（单模块）
团队 15-50 人  → 整洁 / COLA（多模块）
团队 50+ 人    → 微服务 + 六边形（每个服务内部选 COLA 或整洁）
```

#### 3. 架构推荐决策树

```
你的项目复杂度？
├── 简单 CRUD（80% 以上的 CRUD） → 传统分层
│   └── 想为未来 DDD 留余地？ → COLA 简化版
│
├── 中等复杂（核心业务复杂） → COLA 或 六边形
│   ├── 阿里系/国内生态 → COLA
│   ├── 追求领域层纯净度 → 六边形
│   └── 有 Spring Boot / MyBatis 基础设施 → COLA
│
└── 高复杂（多 BC、微服务） → 整洁架构 或 六边形+COLA
    ├── 企业级、国际化团队 → 整洁架构
    ├── 每个微服务内部 COLA → 六边形+COLA 混合
    └── 已有清晰领域划分 → 整洁架构
```

#### 4. 域划分+微服务拆分

```
核心域 (Core Domain)   → 优先投入，自研       → 电商的订单、支付
通用域 (Generic Domain)→ 尽量采购/复用        → 认证、权限
支撑域 (Supporting)    → 可外包/低优先        → 数据报表、运营后台
```

**输出**：
- 推荐架构模式 + 决策理由
- CQRS 级别建议（none/L1/L2/L3）
- 域划分建议（核心/通用/支撑）
- 分层策略推荐（松散 vs 严格）
- 微服务拆分建议（如适用）
- 跳转到对应架构 Skill 的指引

**下一步引导**：
- 选传统分层 → `ddd-architecture-layered`
- 选洋葱 → `ddd-architecture-onion`
- 选六边形 → `ddd-architecture-hexagonal`
- 选整洁 → `ddd-architecture-clean`
- 选 COLA → `ddd-architecture-cola`

---

### Skill 3：ddd-architecture-layered

**定位**：传统分层架构落地指南 — DDD 分层思想的最简实践

**目录**：`ddd-architecture-layered/`

**触发词**：`分层架构`、`传统分层`、`DDD 四层`、`三层变四层`、`layered architecture`

**核心能力**：

#### 1. 架构核心思想

```
传统三层 → DDD 四层

三层：              四层：
Controller          Interface（用户接口层）
  ↓                   ↓
Service             Application（应用层） — 编排，无业务逻辑
  ↓                   ↓
Repository/Mapper   Domain（领域层）★     — 核心，零依赖
                      ↓
                    Infrastructure（基础设施层）
```

**核心原则**：
- 领域层不依赖任何其他层（零依赖原则）
- 基础设施层实现领域层定义的接口（依赖倒置）
- 应用层薄薄一层，只做编排，不放业务逻辑
- 用户接口层只做协议转换，不包含业务判断

#### 2. 适用场景判断

| 适用 | 不适用 |
|------|--------|
| 团队 < 10 人，DDD 概念刚起步 | 需要频繁替换基础设施 |
| 业务中等复杂，有明确领域模型 | 严格的分层隔离要求 |
| 已有三层项目，逐步演进 | 单元测试覆盖率要求极高 |
| Spring Boot / MyBatis 技术栈 | 需要物理隔离的模块边界 |

#### 3. 完整目录结构

```
{project}/
├── {project}-interface/           # 用户接口层
│   ├── controller/                # REST API 控制器
│   ├── dto/                       # 接口层 DTO
│   │   ├── request/
│   │   └── response/
│   └── converter/                 # DTO ↔ DO 转换器
├── {project}-application/         # 应用层
│   ├── service/                   # 应用服务（纯编排）
│   ├── command/                   # 命令对象
│   ├── query/                     # 查询对象
│   └── assembler/                 # 数据组装器
├── {project}-domain/              # 领域层（核心）
│   ├── {aggregate}/               # 按聚合分包
│   │   ├── entity/                # 实体 + 聚合根
│   │   ├── valueobject/           # 值对象
│   │   ├── service/               # 领域服务
│   │   └── repository/            # 仓储接口（只定义）
│   ├── event/                     # 领域事件
│   └── shared/                    # 共享值对象/异常/枚举
└── {project}-infrastructure/      # 基础设施层
    ├── repository/                # 仓储实现
    ├── converter/                 # PO ↔ DO 转换
    ├── event/                     # 事件发布实现
    └── config/                    # 配置
```

#### 4. 开发规范

| 规范 | 说明 |
|------|------|
| 依赖方向 | Interface → App → Domain ← Infrastructure |
| Domain 纯净度 | Domain 零 Spring/JPA/MyBatis 依赖 |
| App 层职责 | 只编排，不包含 if/else 业务判断 |
| 事务边界 | 事务在 App 层，不在 Domain 层 |
| 跨聚合操作 | 通过领域事件（最终一致性） |
| 聚合大小 | 单一聚合 ≤ 5 个实体 |
| 禁止 | 禁止 Controller 有业务逻辑、禁止 Domain import `@Service` |

#### 5. 落地实施步骤

```
Phase 1: 识别聚合（1-2 天）
  → 找聚合根 → 划边界 → 定不变式

Phase 2: 搭建分层骨架（1 天）
  → 生成 pom.xml/gradle → 生成基类（Entity/VO/AggregateRoot）

Phase 3: 实现领域层（2-5 天）
  → 充血模型实体 → Repository 接口 → Domain Service

Phase 4: 实现基础设施层（2-3 天）
  → Repository 实现 → PO ↔ DO 转换 → 数据库配置

Phase 5: 实现应用层（1-2 天）
  → AppService 编排 → Command/Query 对象

Phase 6: 实现接口层（1-2 天）
  → Controller → DTO → Swagger

Phase 7: 审查验证（0.5 天）
  → ddd-code-reviewer 检查 → 依赖方向验证
```

**输出**：
- 完整的分层项目目录结构
- 基础类代码（Entity、ValueObject、AggregateRoot、Repository 接口）
- Maven/Gradle 依赖配置
- 一个完整 Demo（含聚合、应用服务、控制器、仓储）
- 依赖方向检查配置（ArchUnit）
- 演进路线图（传统三层 → DDD 四层）

**参考来源**：
- clean-ddd-hexagonal LAYERS.md
- partme-docs 07（分层）

---

### Skill 4：ddd-architecture-onion

**定位**：洋葱架构落地指南 — 以 Domain 为中心的内外层隔离

**目录**：`ddd-architecture-onion/`

**触发词**：`洋葱架构`、`onion architecture`、`Jeffrey Palermo`

**核心能力**：

#### 1. 架构核心思想

```
洋葱架构核心：所有的依赖都指向中心（Domain）

     ┌──────────────────────┐
     │      Infrastructure  │  ← 最外层：技术细节（DB、MQ、HTTP）
     │  ┌────────────────┐  │
     │  │     Application│  │  ← 应用层：用例编排
     │  │  ┌──────────┐  │  │
     │  │  │  Domain  │  │  │  ← 核心层：领域模型（零依赖）
     │  │  └──────────┘  │  │
     │  └────────────────┘  │
     └──────────────────────┘
```

**核心原则**（来自 Jeffrey Palermo）：
1. 应用核心独立于基础设施
2. 内层定义接口，外层实现接口
3. 所有依赖关系指向内层（Domain）
4. 外层可以引用内层，内层绝不知道外层的实现细节

**与六边形/整洁架构的区别**：
- 洋葱更强调"层次嵌套"，可视化更直观
- 六边形更强调"端口/适配器"的接口抽象
- 整洁更强调"用例 + 实体"的业务规则分离

#### 2. 适用于

| 适用 | 不适用 |
|------|--------|
| 基础设施经常变更（换 DB、换缓存） | 简单 CRUD 项目（过度设计） |
| 单元测试覆盖率要求极高 | 工期紧张的小项目 |
| 团队有抽象能力（能设计好接口） | 团队刚接触 DDD |
| 多入口系统（API + CLI + MQ） | 单一 REST API 入口 |

#### 3. 完整目录结构

```
{project}/
├── {project}-core/                # 核心层（Domain）
│   ├── domain/                    # 领域模型
│   │   ├── model/                 # 实体、值对象、聚合根
│   │   ├── service/               # 领域服务
│   │   └── repository/            # 仓储接口（纯抽象）
│   ├── application/               # 应用服务接口
│   │   └── service/               # 应用服务接口（定义契约）
│   └── shared/                    # 共享类型、异常
├── {project}-infrastructure/      # 基础设施层
│   ├── data/                      # 数据访问
│   │   ├── repository/            # 仓储实现
│   │   ├── entity/                # JPA Entity（PO）
│   │   └── mapper/                # PO ↔ Domain 映射
│   ├── messaging/                 # 消息队列
│   ├── external/                  # 外部 API 客户端
│   └── config/                    # 基础设施配置
├── {project}-api/                 # 用户接口 / 适配器
│   ├── controller/                # REST 控制器
│   ├── dto/
│   ├── middleware/                # 请求拦截、异常处理
│   └── swagger/                   # API 文档
└── {project}-composition/         # 装配/依赖注入
    └── config/                    # DI 容器配置（组装所有层）
```

#### 4. 洋葱架构开发规范

```java
// 洋葱架构关键规范

// Domain 层 — 纯 POJO，零框架注入
public class Order extends AggregateRoot<OrderId> {
    private Money totalAmount;              // 值对象
    private List<OrderItem> items;          // 实体集合
    private OrderStatus status;

    public Money calculateTotal() {         // 领域逻辑在实体
        return items.stream()
            .map(OrderItem::getSubtotal)
            .reduce(Money.ZERO, Money::add);
    }
}

// Domain 定义仓储接口
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
}

// Infrastructure 实现仓储接口
@Repository
public class OrderRepositoryImpl implements OrderRepository {
    private final JpaOrderRepository jpaRepo;  // Spring Data JPA
    private final OrderMapper mapper;

    @Override
    public Optional<Order> findById(OrderId id) {
        return jpaRepo.findById(id.getValue())
            .map(mapper::toDomain);             // PO → Domain
    }
}
```

#### 5. 洋葱架构落地实施步骤

```
Phase 1: 识别核心域模型（1-2 天）
  → 实体/值对象/聚合根 → Repository 接口

Phase 2: 搭建核心层（1 天）
  → Domain 模块 → Application 接口

Phase 3: 实现基础设施层（2-3 天）
  → DB 实现 → MQ 实现 → 外部 API 客户端

Phase 4: 实现 API 适配器（1-2 天）
  → Controller → DTO → 中间件

Phase 5: 组装与测试（1-2 天）
  → DI 组装 → 单元测试 → 集成测试
```

**输出**：
- 完整的洋葱架构项目目录结构
- Domain/Core/Infra/API 各层代码模板
- Demo 聚合实现（含内外层接口注入）
- 单元测试 + 集成测试骨架
- 依赖方向 DMZ（非军事区）配置

**参考来源**：
- Jeffrey Palermo "The Onion Architecture" (blog)
- clean-ddd-hexagonal SKILL.md

---

### Skill 5：ddd-architecture-hexagonal

**定位**：六边形架构落地指南 — 端口与适配器

**目录**：`ddd-architecture-hexagonal/`

**触发词**：`六边形架构`、`端口适配器`、`Ports & Adapters`、`hexagonal architecture`、`Alistair Cockburn`

**核心能力**：

#### 1. 架构核心思想

```
六边形架构核心：业务逻辑通过"端口（Ports）"与外界隔离，
                 外部通过"适配器（Adapters）"接入

            ┌───────────────────────┐
    Web ──▶│                       │──▶ DB
            │    ┌───────────┐     │
    CLI ──▶│    │  Domain   │     │──▶ MQ
            │    │   ★       │     │
    Event▶│    └───────────┘     │──▶ Cache
            │                       │
    Test ──▶│                       │──▶ External API
            └───────────────────────┘

    Driving Side (左侧/主适配器)   Domain Core   Driven Side (右侧/次适配器)
```

**三大核心抽象**：

| 概念 | 说明 | 代码体现 |
|------|------|---------|
| **Port（端口）** | 领域层定义的接口，隔离外部依赖 | `interface OrderRepository`（在 Domain） |
| **Primary/Driving Adapter（主适配器）** | 外部如何驱动你的系统 | REST Controller、CLI Command |
| **Secondary/Driven Adapter（次适配器）** | 你的系统驱动哪些外部 | JPA RepositoryImpl、Kafka Producer |

#### 2. 适用场景

| 适用 | 不适用 |
|------|--------|
| 多入口系统（REST + CLI + MQ + gRPC） | 单一 REST API + 简单 CRUD |
| 基础设施频繁更换（换 DB、换 MQ） | 基础设施稳定不变 |
| 需要高超的测试可测性 | 团队层少（< 3 人） |
| 微服务内部架构标准化 | 快速原型 |

#### 3. 完整目录结构

```
{project}/
├── {project}-domain/              # 领域核心 + 端口定义
│   ├── model/                     # 聚合、实体、值对象
│   │   ├── order/
│   │   │   ├── Order.java         # 聚合根
│   │   │   ├── OrderItem.java     # 实体
│   │   │   ├── OrderId.java       # 值对象
│   │   │   └── OrderStatus.java   # 值对象/枚举
│   │   └── shared/
│   ├── service/                   # 领域服务
│   ├── event/                     # 领域事件
│   └── port/                      # ★ 端口（接口定义）
│       ├── inbound/               # 入站端口（UseCase 接口）
│       │   ├── CreateOrderUseCase.java
│       │   ├── PayOrderUseCase.java
│       │   └── QueryOrderUseCase.java
│       └── outbound/              # 出站端口（Repository/External 接口）
│           ├── OrderRepository.java
│           ├── PaymentGateway.java
│           └── NotificationPort.java
├── {project}-application/         # 应用层（UseCase 实现）
│   └── service/
│       ├── CreateOrderService.java
│       ├── PayOrderService.java
│       └── QueryOrderService.java
├── {project}-adapter/             # 适配器层
│   ├── inbound/                   # ★ 主适配器（驱动侧）
│   │   ├── web/                   # REST API
│   │   │   ├── controller/
│   │   │   └── dto/
│   │   ├── cli/                   # 命令行
│   │   └── event/                 # 事件监听
│   └── outbound/                  # ★ 次适配器（被驱动侧）
│       ├── persistence/           # 数据库
│       │   ├── OrderRepositoryImpl.java
│       │   ├── entity/            # JPA Entity
│       │   └── mapper/            # PO ↔ Domain
│       ├── messaging/             # 消息队列
│       └── external/              # 外部 API 客户端
└── {project}-configuration/       # 配置 + DI 组装
    └── config/
```

#### 4. 六边形架构开发规范

```java
// ★ 入站端口（UseCase）— 定义在 Domain
public interface CreateOrderUseCase {
    OrderCreated handle(CreateOrderCommand command);
}

// ★ 出站端口（Repository）— 定义在 Domain
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
}

// ★ 应用层 — 实现入站端口（UseCase）
@ApplicationService  // 自定义注解，不是 Spring @Service
public class CreateOrderService implements CreateOrderUseCase {
    private final OrderRepository orderRepository;   // 注入出站端口

    @Override
    public OrderCreated handle(CreateOrderCommand command) {
        Order order = Order.create(command);    // 领域逻辑
        orderRepository.save(order);            // 出站端口
        return OrderCreated.from(order);
    }
}

// ★ 主适配器 — REST Controller
@RestController
public class OrderController {
    private final CreateOrderUseCase createOrderUseCase;

    @PostMapping("/orders")
    public OrderResponse createOrder(@RequestBody CreateOrderRequest request) {
        var command = request.toCommand();
        var result = createOrderUseCase.handle(command);
        return OrderResponse.from(result);
    }
}

// ★ 次适配器 — JPA Repository 实现
@Repository
public class JpaOrderRepository implements OrderRepository {
    private final JpaOrderRepo jpaRepo;   // Spring Data JPA
    private final OrderMapper mapper;     // PO ↔ Domain

    @Override
    public Order save(Order order) {
        OrderPO po = mapper.toPO(order);
        OrderPO saved = jpaRepo.save(po);
        return mapper.toDomain(saved);
    }
}
```

#### 5. 落地实施步骤

```
Phase 1: 定义端口（1-2 天）
  → 入站端口（UseCase 接口）→ 出站端口（Repository/External 接口）

Phase 2: 实现领域模型（2-3 天）
  → 聚合根/实体/值对象 → 领域服务 → 领域事件

Phase 3: 实现应用层（1-2 天）
  → UseCase 实现（注入端口，编排调用）

Phase 4: 实现适配器（2-4 天）
  → 主适配器：REST/gRPC/CLI → 次适配器：DB/MQ/External API

Phase 5: DI 组装 + 测试（1-2 天）
  → 依赖注入配置 → 端口 Mock 测试 → 适配器集成测试
```

**输出**：
- 完整的六边形项目目录结构
- Domain Ports（UseCase + Repository 接口）
- 主适配器 + 次适配器代码模板
- Demo 聚合实现
- Mock 测试 + 适配器集成测试
- 完整的 UseCase 调用链（Controller → UseCase → Port → Adapter）

**参考来源**：
- clean-ddd-hexagonal HEXAGONAL.md
- Alistair Cockburn "Hexagonal Architecture"
- xfg-ddd-skills（六边形架构编码规范）
- partme-docs 08

---

### Skill 6：ddd-architecture-clean

**定位**：整洁架构落地指南 — Robert C. Martin 的 Clean Architecture

**目录**：`ddd-architecture-clean/`

**触发词**：`整洁架构`、`Clean Architecture`、`Robert Martin`、`Uncle Bob`、`用例驱动`

**核心能力**：

#### 1. 架构核心思想

```
整洁架构：以用例（UseCase）为组织核心，层与层之间严格遵守依赖规则

                    ┌──────────────────────┐
                    │    Frameworks &       │
                    │    Drivers             │
                    │  ┌────────────────┐   │
                    │  │  Interface      │   │
                    │  │  Adapters       │   │
                    │  │  ┌──────────┐   │   │
                    │  │  │   App    │   │   │
                    │  │  │ Business │   │   │
                    │  │  │  Rules   │   │   │
                    │  │  │ ┌──────┐ │   │   │
                    │  │  │ │ Entity│ │   │   │
                    │  │  │ │  ★   │ │   │   │
                    │  │  │ └──────┘ │   │   │
                    │  │  └──────────┘   │   │
                    │  └────────────────┘   │
                    └──────────────────────┘
```

**依赖规则**：源码依赖必须只指向内层。外层可依赖内层，内层绝不知道外层。

**四层结构**：

| 层（从外到内） | 职责 | 依赖 |
|:---|------|------|
| Frameworks & Drivers | Web 框架、DB、UI | → Adapters |
| Interface Adapters | Controller、Gateway、Presenter | → Application |
| Application Business Rules | Use Cases（用例编排） | → Enterprise |
| Enterprise Business Rules | Entity、核心业务规则 ★ | 无依赖 |

#### 2. 适用场景

| 适用 | 不适用 |
|------|--------|
| 企业级核心系统（订单、支付） | 临时脚本、小工具 |
| 业务规则独立于交付机制 | 前端重、后端轻的 CRUD |
| 需要严格的模块物理隔离 | 团队 < 5 人、快速迭代 |
| 微服务内部标准化架构 | 简单三层够用 |

#### 3. 完整目录结构

```
{project}/
├── {project}-core/                # 企业业务规则（Enterprise）
│   ├── entity/                    # ★ 核心实体
│   │   ├── Order.java
│   │   ├── OrderId.java
│   │   ├── OrderStatus.java
│   │   └── Money.java
│   ├── rule/                      # ★ 企业级业务规则
│   │   ├── OrderValidationRule.java
│   │   └── PricingRule.java
│   └── exception/                 # ★ 领域异常
├── {project}-usecase/             # 应用业务规则（Application = UseCase）
│   ├── port/                      # UseCase 输入/输出端口
│   │   ├── input/                 # 输入端口（UseCase 接口）
│   │   │   ├── CreateOrderUseCase.java
│   │   │   └── PayOrderUseCase.java
│   │   └── output/                # 输出端口（Repository/Gateway 接口）
│   │       ├── OrderRepository.java
│   │       └── PaymentGateway.java
│   ├── interactor/                # UseCase 实现（Interactor）
│   │   ├── CreateOrderInteractor.java
│   │   └── PayOrderInteractor.java
│   └── dto/                       # UseCase 专用 DTO
│       ├── CreateOrderRequest.java
│       └── PayOrderResponse.java
├── {project}-adapter/             # 接口适配器层
│   ├── controller/                # REST / gRPC 控制器
│   ├── presenter/                 # 响应格式转换
│   ├── repository/                # DB 实现（实现 UseCase 层定义的接口）
│   ├── gateway/                   # 外部 API 实现
│   └── converter/                 # DTO/PO ↔ Entity 转换
└── {project}-framework/           # 框架 & 驱动层
    ├── config/                    # Spring/DI 配置
    ├── persistence/               # JPA Entity、Mapper
    └── web/                       # Web 配置（CORS、Security）
```

#### 4. 整洁架构开发规范

```java
// ★ Enterprise 层 — 核心实体，零框架依赖
public class Order {
    private final OrderId id;
    private Money totalAmount;
    private OrderStatus status;

    public void pay() {
        if (!this.status.canPay()) {
            throw new OrderDomainException("不可支付");
        }
        this.status = OrderStatus.PAID;
    }
}

// ★ UseCase 层 — 输入端口（UseCase 接口）
public interface CreateOrderUseCase {
    CreateOrderOutput execute(CreateOrderInput input);
}

// ★ UseCase 层 — 输出端口（Repository 接口）
public interface OrderRepository {
    Order save(Order order);
    Optional<Order> findById(OrderId id);
}

// ★ UseCase 层 — Interactor（UseCase 实现）
public class CreateOrderInteractor implements CreateOrderUseCase {
    private final OrderRepository orderRepository;

    @Override
    public CreateOrderOutput execute(CreateOrderInput input) {
        Order order = Order.create(/* ... */);   // Enterprise 层
        orderRepository.save(order);              // 通过端口
        return CreateOrderOutput.from(order);
    }
}

// ★ Adapter 层 — Controller
@RestController
public class OrderController {
    private final CreateOrderUseCase createOrderUseCase;

    @PostMapping("/orders")
    public ResponseEntity<CreateOrderResponse> createOrder(
            @RequestBody CreateOrderRequest request) {
        var input = request.toInput();
        var output = createOrderUseCase.execute(input);
        return ResponseEntity.ok(CreateOrderResponse.from(output));
    }
}
```

#### 5. 落地实施步骤

```
Phase 1: 企业业务规则（1-3 天）
  → 核心实体 → 业务规则 → 领域异常

Phase 2: UseCase + 端口（1-2 天）
  → 输入端口（UseCase）→ 输出端口（Repository/Gateway）

Phase 3: UseCase Interactor（1-2 天）
  → UseCase 实现 → DTO 定义

Phase 4: 适配器 + 框架（2-3 天）
  → Controller/Gateway → Repository 实现 → DI 配置

Phase 5: 测试（1-2 天）
  → Enterprise 单元测试 → UseCase 集成测试（Mock 端口） → 适配器 E2E 测试
```

**输出**：
- 完整的整洁架构项目目录结构
- Enterprise 实体基类 + 规则模板
- UseCase 端口（Input/Output）+ Interactor 模板
- Adapter 层代码模板
- Framework 层 DI 配置
- 完整测试策略（单元 → 集成 → E2E）

**参考来源**：
- Robert C. Martin "Clean Architecture"
- clean-ddd-hexagonal SKILL.md

---

### Skill 7：ddd-architecture-cola

**定位**：COLA v5 架构落地指南（合并原 cola-creator + cola-validator）

**目录**：`ddd-architecture-cola/`

**触发词**：`COLA 架构`、`cola-creator`、`创建 COLA 项目`、`COLA 脚手架`、`COLA 校验`、`cola-validator`、`检查架构`、`依赖方向检查`、`模块结构`

**核心能力**：

#### 1. 架构核心思想

```
COLA v5（菱形架构）：

                ┌──────────────┐
                │   Adapter    │  ← 适配层：HTTP、MQ、RPC
                └──────┬───────┘
                       │
                ┌──────▼───────┐
                │   Application│  ← 应用层：编排、事务、CQRS 分流
        ┌───────┴───────┬───────┴───────┐
        ▼               ▼               ▼
  ┌──────────┐   ┌──────────┐   ┌──────────┐
  │  Domain  │   │  Domain  │   │  Domain  │  ← 领域层：核心业务逻辑
  │   ★      │   │   ★      │   │   ★      │
  └──────────┘   └──────────┘   └──────────┘
        ▲               ▲               ▲
        └───────────────┴───────────────┘
                       │
                ┌──────▼───────┐
                │Infrastructure│  ← 基础设施层：DB、MQ、缓存、外部 API
                └──────────────┘
```

**四大核心约束**：
1. Domain 零依赖（不允许 import Spring/JPA/MyBatis）
2. App 层不能有业务 if/else
3. Adapter 层不能有 SQL/业务判断
4. 模块间不可循环依赖

#### 2. 生成 & 校验能力（二合一）

**cola-creator 能力（项目脚手架）**：

```
用户：帮我创建一个 COLA 项目
  →
交互确认：
  1. 项目名和包名
  2. Java/Kotlin
  3. Spring Boot 版本
  4. 是否需要 CQRS（默认不启用）
  5. 是否需要 Demo 代码（默认 Order 示例）
  →
生成：
  ├── 完整 pom.xml / build.gradle（多模块）
  ├── COLA 标准目录结构
  ├── 基础类：Entity/AggregateRoot/ValueObject/DomainEvent
  ├── Demo 聚合（Order 完整示例）
  ├── DDD 中间件配置（DomainEventBus 等）
  └── ArchUnit 测试（依赖方向自动化检查）
  →
指引下一步：ddd-domain-designer、ddd-api-designer
```

**cola-validator 能力（架构合规检查）**：

| 检查项 | 严重级别 | 说明 |
|--------|:--:|------|
| **依赖方向** | P0 | domain 不能依赖 infrastructure/app/adapter |
| **包命名规范** | P1 | 必须符合 COLA 分包命名约定 |
| **层职责** | P0 | Adapter 不应有业务逻辑、App 不应有 SQL |
| **Domain 纯净度** | P0 | Domain 层零框架依赖（无 Spring/JPA/MyBatis import） |
| **模块间依赖** | P1 | 模块间不可循环依赖 |
| **聚合设计** | P1 | 聚合大小、聚合间引用 |

依赖方向检查算法：

```
规则:
  domain/       → 不可依赖任何其他模块
  infrastructure/ → 可依赖 domain/
  app/          → 可依赖 domain/ + infrastructure/
  adapter/      → 可依赖 app/ + domain/

检测方法:
  1. 解析每个模块的 import 语句
  2. 检查 domain/ 下是否有 import com.example.infrastructure.* → P0
  3. 检查 domain/ 下是否有 import org.springframework.*     → P0
  4. 检查 domain/ 下是否有 import javax.persistence.*        → P0
  5. 检查 app/ 下是否有 import java.sql.*                    → P1
  6. 检查 adapter/ 下是否有 if-else 业务分支                 → P0
```

**评分**：

```
合规度 = (通过检查项 / 总检查项) * 100%
≥ 90%  → 🟢 优秀
70-89% → 🟡 良好
50-69% → 🟠 一般
< 50%  → 🔴 不合格，建议重建结构
```

#### 3. 目录结构（COLA v5 多模块）

```
{project}/
├── {project}-adapter/           # 适配层
│   ├── web/                     # REST 控制器
│   │   ├── controller/
│   │   └── dto/                 # 接口层 DTO
│   └── consumer/                # 消息消费者
├── {project}-app/               # 应用层
│   ├── service/                 # 应用服务（编排，不放业务逻辑）
│   ├── command/                 # 命令对象
│   ├── query/                   # 查询对象
│   └── event/                   # 事件处理
├── {project}-domain/            # 领域层（核心，零依赖）
│   ├── {aggregate}/             # 按聚合分包
│   │   ├── entity/              # 实体 + 聚合根
│   │   ├── valueobject/         # 值对象
│   │   ├── event/               # 领域事件
│   │   ├── service/             # 领域服务
│   │   └── repository/          # 仓储接口（只定义接口）
│   ├── gateway/                 # 防腐层接口
│   └── shared/                  # 共享值对象/枚举/异常
├── {project}-infrastructure/    # 基础设施层
│   ├── repository/              # 仓储实现
│   ├── gateway/                 # 防腐层实现
│   ├── converter/               # PO ↔ DO 转换器
│   └── config/                  # 配置
└── start/                       # 启动模块
    └── Application.java
```

#### 4. 生成内容（cola-creator 部分）

| 生成项 | 说明 |
|--------|------|
| 目录结构 | 完整的 Maven/Gradle 多模块结构 |
| 基础类 | Entity、AggregateRoot、ValueObject、DomainEvent 基类 |
| 依赖配置 | pom.xml / build.gradle 含 COLA + Spring 依赖 |
| Demo 代码 | 一个简单的 Order 聚合（含实体、仓储、应用服务、控制器） |
| 单元测试骨架 | 领域层 + 应用层测试模板 |
| ArchUnit 测试 | 依赖方向自动化验证 |
| .gitignore / README | 项目配置 |

#### 5. 落地实施步骤

```
Phase 1: 项目脚手架创建（1 天）
  → ddd-architecture-cola creator → 生成完整项目骨架

Phase 2: 领域建模（2-3 天）
  → 配合 ddd-domain-designer → 生成聚合代码

Phase 3: 基础设施实现（2-3 天）
  → Repository 实现 → Gateway 实现 → Config

Phase 4: 应用层 + 适配器（1-2 天）
  → AppService → Controller → DTO

Phase 5: 架构校验（0.5 天）
  → ddd-architecture-cola validator → 违规修复

Phase 6: 随项目演化持续校验
  → CI/CD 集成 ArchUnit → 每次提交自动检查
```

**输出**：
- 完整 COLA v5 项目脚手架
- 架构校验报告（违规清单 + 修复建议）
- 合规度评分
- ArchUnit 自动化校验配置

**参考来源**：
- COLA 5.0 架构规范
- partme-docs 13（代码模型目录结构）、14（代码对象映射）、15（三层边界）、16（松散vs严格分层）、91（完整代码）
- xfg-ddd-skills（六边形架构编码规范）

---

### Skill 8：ddd-domain-designer

**定位**：领域设计全流程（重命名自 ddd-domain-modeling，聚焦"设计"能力）

**目录**：`ddd-domain-designer/`

**触发词**：`领域建模`、`领域设计`、`事件风暴`、`聚合设计`、`限界上下文`、`domain modeling`、`怎么设计聚合`、`domain designer`

**核心能力**：

#### 1. 事件风暴驱动 6 步流程

```
Step 1: 产品愿景 — 电梯演讲
Step 2: 场景分析 — 用户旅程
Step 3: 领域建模 — 聚合 + 限界上下文
Step 4: 微服务拆分 — 限界上下文 → 微服务
Step 5: 详细设计 — 实体、值对象、聚合根、领域事件
Step 6: 开发测试 — 以聚合为单位组织开发
```

#### 2. 聚合设计五步法 + 六原则

| 原则 | 说明 | 审查要点 |
|------|------|---------|
| 1. 在一致性边界内建模真正的不变条件 | 聚合封装不变性 | 不变式是否被外部破坏？ |
| 2. 设计小聚合 | 过大导致并发冲突 | 实体数 > 5？有 N+1 隐患？ |
| 3. 通过唯一标识引用其它聚合 | 聚合间 ID 关联 | 存在跨聚合对象直接引用？ |
| 4. 边界外使用最终一致性 | 聚合内强一致，聚合间最终一致 | 一个事务涉及多个聚合？ |
| 5. 通过应用层实现跨聚合服务调用 | 避免跨聚合领域服务调用 | 领域服务直接跨聚合？ |
| 6. 适合自己才是最好的 | 可突破原则 | — |

#### 3. 设计产出

| 产出 | 格式 |
|------|------|
| 事件风暴记录 | Markdown |
| 限界上下文划分 + 上下文映射图 | Mermaid |
| 聚合设计清单 | 表格（每个聚合：根、实体、值对象、领域事件） |
| 领域对象→代码对象映射表 | Markdown 表格 |
| 值对象持久化策略建议 | Markdown |
| 非典型场景处理说明 | Markdown |

**与 ddd-event-storming 的关系**：
- `ddd-event-storming` — 专注于事件风暴工作坊主持（面向多角色协作）
- `ddd-domain-designer` — 从事件风暴结果进入聚合设计和代码落地（面向开发者）
- 推荐路径：`event-storming`（工作坊产出） → `domain-designer`（详细设计） → `(架构 Skill)`（落地）

**输出**：
- 事件风暴 6 步完整记录
- 限界上下文划分 + 上下文映射
- 聚合设计清单
- 领域对象→代码对象映射表
- 微服务拆分建议

**参考来源**：
- clean-ddd-hexagonal references/DDD-STRATEGIC.md、DDD-TACTICAL.md
- cleanddd-skills requirements-analysis / modeling
- partme-docs 04、05、12、14
- Vernon Effective Aggregate Design

---

### Skill 9：ddd-cqrs-architecture

**定位**：CQRS 架构独立 Skill — 混合方案 C：独立 Skill + 各架构 Skill 内嵌 CQRS 模式

**目录**：`ddd-cqrs-architecture/`

**触发词**：`CQRS`、`读写分离`、`事件溯源`、`Event Sourcing`、`领域事件`、`Command Bus`、`Query Model`、`Command Query Responsibility Segregation`

**架构原理**：

```
CQRS 核心：命令（Command）与查询（Query）职责分离

传统 CRUD：                     CQRS：
         ┌──────────┐          ┌──────────┐     ┌──────────┐
         │   CRUD   │          │ Command  │     │  Query   │
         │  Service │          │  Model   │     │  Model   │
         └────┬─────┘          └────┬─────┘     └────┬─────┘
              │                     │                  │
         ┌────┴────┐            ┌───┴───┐          ┌───┴───┐
         │   DB    │            │ Write │          │ Read  │
         └─────────┘            │  DB   │          │  DB   │
                                └───────┘          └───────┘
```

**混合方案 C 的定义**：

```
ddd-cqrs-architecture 作为独立 Skill：
  ├── CQRS 三级落地策略（L1/L2/L3）★ 本 Skill 核心
  ├── 事件溯源 (Event Sourcing) 详解
  ├── 幂等设计完整方案
  ├── 事件风暴 → 领域事件映射
  └── 各架构 Skill 的 CQRS 集成点 ↓

各架构 Skill 内嵌 CQRS 集成点：
  ├── architecture-layered → CQRS 轻量集成（CommandService + QueryService 分离）
  ├── architecture-onion → CQRS 作为 Application 层的读写分离
  ├── architecture-hexagonal → CQRS 落地六边形端口（Command Port + Query Port）
  ├── architecture-clean → CQRS 作为 UseCase 级别的读写分离
  └── architecture-cola → CQRS 融入 COLA 的 Command/Query 模块
```

#### 1. CQRS 三级落地策略

```
L1 — 模型分离（最低成本）：
  OrderCommandService（写）→ 共用 OrderRepository → 同一 DB
  OrderQueryService（读）  → 共用 OrderRepository

L2 — 数据库分离（中成本）：
  OrderCommandService → Command DB（主库）
  OrderQueryService   → Query DB（从库/ES）同步机制：领域事件 → MQ → Query DB

L3 — Event Sourcing（高成本）：
  写 → EventStore（事件流），读 → Projection（物化视图）
  适用：审计追踪、时间旅行查询、事件重放
```

#### 2. 事件处理全流程

```
领域行为 → 构建领域事件 → 事件持久化 → EventBus 发布
                                           ↓
                              ┌────────────┴──────────────┐
                              ↓                            ↓
                        本地事件处理（同步）          MQ 外发（异步）
                        （同一进程内）              （跨微服务）
                                                       ↓
                                                 外部事件处理
                                                 （幂等 + 补偿）
```

#### 3. 各架构下的 CQRS 集成模式

| 架构 | CQRS 集成点 | 目录体现 |
|------|----------|---------|
| **Layered** | Application 层 Command/Query Service 分离 | `app/service/command/` + `app/service/query/` |
| **Onion** | Core 层定义 Command/Query UseCase 接口 | `core/application/command/` + `core/application/query/` |
| **Hexagonal** | Port 层 Command Port + Query Port | `domain/port/command/` + `domain/port/query/` |
| **Clean** | UseCase 层 Command Interactor + Query Interactor | `usecase/interactor/command/` + `usecase/interactor/query/` |
| **COLA** | App 层 Command + Query 子模块 | `app/command/` + `app/query/` |

#### 4. 幂等设计

```
1. 事件表 + 唯一事件ID  → 数据库唯一约束防重复
2. 状态机              → 已处理状态不可再触发
3. Redis + TTL          → 轻量级去重
4. 业务幂等             → UPDATE … SET stock=stock-1 WHERE stock>=1
```

**输出**：
- CQRS 级别推荐 + 理由
- 写模型（Command）设计
- 读模型（Query/DTO）设计
- 领域事件列表 + 触发关系
- 事件处理全流程设计
- 幂等策略选型
- 对应架构的 CQRS 集成指导

**参考来源**：
- clean-ddd-hexagonal CQRS-EVENTS.md
- partme-docs 06
- Microsoft DDD+CQRS microservices guide

---

### Skill 10：ddd-api-designer

**定位**：从领域模型到 API 设计

**目录**：`ddd-api-designer/`

**触发词**：`API 设计`、`REST API`、`OpenAPI`、`BFF`、`DTO 设计`、`接口设计`、`数据对象转换`

**核心能力**：

#### 1. CQRS 读写分离的 API 差异化

```
命令 API (写):
  POST   /orders             → CreateOrderCommand
  PUT    /orders/{id}/confirm → ConfirmOrderCommand
  DELETE /orders/{id}        → CancelOrderCommand

查询 API (读):
  GET /orders/{id}           → OrderDetailDTO (从 Materialized View)
  GET /orders?status=PAID    → OrderListDTO[] (从 Read Model)
```

#### 2. 数据对象转换链

```
前端 VO ←→ 用户接口层 DTO ←→ 应用层 DO ←→ 基础层 PO
  │               │               │              │
展示层          接口层          领域层         基础层

PO (Persistent Object)    — 数据库结构映射
DO (Domain Object)        — 运行时实体，充血模型
DTO (Data Transfer Object)— 前后端/微服务间传输载体
VO (View Object)          — 展示层指定页面/组件的数据

转换规则：
  DO → PO：仓储服务完成持久化
  PO → DO：仓储服务完成持久化加载

  转换规则（续）：
  DO → DTO：Assembler/Converter 完成。DTO 面向特定用例，
            一个 DO 可对应多个 DTO（不同场景返回不同字段）
  DTO → VO：前端组装层（BFF）。VO 面向页面，一个页面
            可能组合多个 DTO 的数据
  VO → DTO → DO：Command/Request → DTO → Domain（写方向）
```

#### 3. API 设计规范

```yaml
# 命令 API（写操作）— 动词驱动
POST   /api/v1/orders                 # 创建订单
PUT    /api/v1/orders/{id}/confirm     # 确认订单
DELETE /api/v1/orders/{id}             # 取消订单

# 查询 API（读操作）— 资源驱动
GET    /api/v1/orders/{id}             # 订单详情
GET    /api/v1/orders?status=PAID      # 订单列表

# 子资源
GET    /api/v1/orders/{id}/items       # 订单项列表
POST   /api/v1/orders/{id}/items       # 添加订单项

命名规范：
  - 使用名词复数（/orders 而非 /order）
  - 避免深层嵌套（最多 2 层：/orders/{id}/items）
  - 写操作用动词后缀（confirm、cancel、approve）
```

#### 4. 统一响应格式

```json
// 成功响应（命令）
{
  "code": 0,
  "message": "success",
  "data": { "orderId": "ORD-2024-001", "status": "PAID" }
}

// 成功响应（查询 — 单体）
{
  "code": 0,
  "message": "success",
  "data": { "id": "ORD-2024-001", "totalAmount": "99.00", "status": "PAID" }
}

// 成功响应（查询 — 分页）
{
  "code": 0,
  "message": "success",
  "data": {
    "records": [...],
    "total": 100,
    "page": 1,
    "pageSize": 20
  }
}

// 错误响应
{
  "code": 40001,
  "message": "订单状态不允许支付",
  "detail": "当前状态：CANCELLED，可支付状态：DRAFT"
}
```

#### 5. BFF（Backend for Frontend）设计

```
BFF 模式：

      ┌──────────┐  ┌──────────┐  ┌──────────┐
      │  Web BFF │  │ iOS BFF  │  │ MiniApp  │
      │          │  │          │  │ BFF      │
      └────┬─────┘  └────┬─────┘  └────┬─────┘
           │              │              │
    ┌──────┼──────────────┼──────────────┼──────────┐
    │      ▼              ▼              ▼          │
    │  ┌──────────────────────────────────────┐    │
    │  │         API Gateway                   │    │
    │  └────┬──────────────┬─────────────┬────┘    │
    │       ▼              ▼             ▼         │
    │  ┌─────────┐  ┌──────────┐  ┌─────────┐     │
    │  │ Order   │  │ Payment  │  │ Product │     │
    │  │ Service │  │ Service  │  │ Service │     │
    │  └─────────┘  └──────────┘  └─────────┘     │
    └───────────────── 微服务集群 ────────────────┘

BFF 层职责：
  - 聚合多个微服务的数据 → 组合成页面需要的 VO
  - 适配不同端的数据格式需求（Web 全量 / 移动端精简）
  - 协议转换（内部 gRPC → 外部 REST）
```

#### 6. API 版本管理策略

| 策略 | 适用场景 | 方式 |
|------|---------|------|
| URL 路径 | 破坏性变更 | `/api/v1/orders` → `/api/v2/orders` |
| 请求头 | 客户端可控 | `Accept: application/vnd.company.v2+json` |
| 查询参数 | 临时调试 | `/api/orders?version=2` |
| 内容协商 | RESTful 标准 | `Accept: application/json;version=2` |

**推荐策略**：URL 路径版本（最直观，Swagger 兼容最好）

#### 7. API 安全设计

```
认证（Authentication）：
  - JWT Bearer Token
  - OAuth2 / OpenID Connect
  - API Key（服务间调用）

授权（Authorization）：
  - 按限界上下文授权（Order BC 权限独立于 Payment BC）
  - 基于资源的所有权检查（用户只能操作自己的订单）

输入校验：
  - Controller 层：格式校验（@Valid + JSR-303）
  - Application 层：业务校验（幂等性、状态机）
  - Domain 层：不变式校验（聚合根内部）

限流：
  - 命令 API：较低 QPS（防止滥用写操作）
  - 查询 API：较高 QPS（可加缓存层）
```

**输出**：
- REST API 端点设计（命令 + 查询分离）
- 统一响应格式规范
- DTO/VO 代码模板
- OpenAPI 3.0 规范文件（Swagger）
- BFF 层架构设计（如适用）
- API 版本管理方案
- 数据对象转换链（PO→DO→DTO→VO）完整 Mapping

**下一步引导**：
- `ddd-code-reviewer`（检查 API 设计是否符合 DDD 规范）
- `ddd-architecture-doc`（将 API 设计输出为文档）

**参考来源**：
- clean-ddd-hexagonal SKILL.md
- partme-docs 14（代码对象映射）

---

### Skill 11：ddd-code-reviewer

**定位**：DDD 代码审查 + 反模式检测 + 合规评分

**目录**：`ddd-code-reviewer/`

**触发词**：`代码审查`、`DDD 审查`、`架构审查`、`反模式检测`、`code review`、`检查代码`、`充血模型检查`、`分层合规`

**核心能力**：

#### 1. DDD 反模式检测清单

| 反模式 | 严重级别 | 检测要点 |
|--------|:--:|------|
| **贫血模型** | P0 | Entity 只有 getter/setter，无业务方法 |
| **上帝 Service** | P0 | 单个 Service 超过 500 行，包含所有业务逻辑 |
| **跨聚合直接引用** | P0 | 聚合 A 的字段类型是聚合 B（应为 ID 引用） |
| **领域层框架依赖** | P0 | Domain 层 import Spring/JPA/MyBatis |
| **Repository 返回 DTO** | P1 | Repository 返回非聚合根类型 |
| **Controller 中有业务逻辑** | P1 | if/else 业务判断出现在 Controller 层 |
| **Application Service 中有 SQL** | P1 | App 层直接操作 Mapper/JdbcTemplate |
| **值对象可变** | P1 | ValueObject 有 setter 或非 final 字段 |
| **聚合过大** | P2 | 单个聚合内实体超过 5 个 |
| **循环依赖** | P0 | A→B→A 模块循环依赖 |
| **缺少领域事件** | P2 | 关键业务动作无领域事件发布 |
| **跨聚合事务** | P2 | 一个事务涉及两个以上聚合 |

#### 2. 分层合规检查矩阵

```
检查规则（基于 ArchUnit）：

┌──────────────┬─────┬─────┬─────┬─────┐
│ 层/可依赖    │ Infra│ Dom │ App │ Adap│
├──────────────┼─────┼─────┼─────┼─────┤
│ Infrastructure│  ✓  │  ✗  │  ✗  │  ✗  │
│ Domain       │  ✗  │  ✓  │  ✗  │  ✗  │
│ Application │  ✓  │  ✓  │  ✓  │  ✗  │
│ Adapter     │  ✓  │  ✓  │  ✓  │  ✓  │
└──────────────┴─────┴─────┴─────┴─────┘

Domain 层零依赖规则（P0）：
  ✗ import org.springframework.stereotype.Service
  ✗ import javax.persistence.Entity
  ✗ import org.apache.ibatis.annotations.Mapper
  ✓ import java.util.Optional
  ✓ import java.math.BigDecimal
```

#### 3. 充血模型检查

```java
// 通过审查 ✅
public class Order extends AggregateRoot<OrderId> {
    private OrderStatus status;
    private List<OrderItem> items;

    public void pay() {                    // 行为在实体
        if (!status.canPay()) {
            throw new OrderException("不可支付");
        }
        this.status = OrderStatus.PAID;
        addDomainEvent(new OrderPaidEvent(this.id));
    }
}

// 不通过审查 ❌ — 贫血模型
public class Order {
    private Long id;
    private String status;                // 字符串代替值对象
    // 只有 getter/setter，无业务方法 ← 反模式
}
public class OrderService {               // 上帝 Service
    @Transactional
    public void pay(Long orderId) {       // 行为在 Service
        Order order = orderMapper.findById(orderId);
        if ("DRAFT".equals(order.getStatus())) { // 裸字符串比较
            order.setStatus("PAID");
            orderMapper.update(order);
        }
    }
}
```

#### 4. 审查评分体系

```
评分维度：

1. 分层合规 (30%)
   - 依赖方向正确性
   - 层职责单一性
   - 跨层调用检测

2. 领域模型质量 (30%)
   - 充血模型覆盖度（实体含业务方法 / 总实体数）
   - 值对象使用率（值对象数 / 基础类型字段数）
   - 聚合设计合理性

3. 命名规范 (15%)
   - 聚合根 → Order（业务名称）
   - 仓储 → OrderRepository
   - 领域服务 → OrderPricingService
   - 领域事件 → OrderPaid（过去式）

4. 代码结构 (15%)
   - 包结构是否按聚合组织
   - 类大小（聚合根 < 200 行，Service < 100 行）
   - 方法复杂度（圈复杂度 < 10）

5. 测试覆盖 (10%)
   - 领域层单元测试覆盖率
   - 聚合根测试覆盖率

总分 = Σ(维度得分 × 权重)

≥ 85  → 🟢 A级：DDD 优秀实践
70-84 → 🟡 B级：基本合规，有改进空间
50-69 → 🟠 C级：存在明显反模式
< 50  → 🔴 D级：需要重构
```

#### 5. 审查报告结构

```markdown
# DDD 代码审查报告

## 总体评分：78/100 (B级 🟡)

### 一、分层合规检查 (24/30)
| 检查项 | 结果 | 说明 |
|--------|:--:|------|
| Domain 层零依赖 | ✅ | 无框架依赖 |
| App 层无 SQL | ❌ | OrderAppService L45 直接调用 Mapper |
| 依赖方向 | ✅ | 无反向依赖 |

### 二、领域模型质量 (22/30)
| 检查项 | 结果 | 说明 |
|--------|:--:|------|
| 充血模型 | ⚠️ | User 实体仍为贫血模型 |
| 值对象 | ⚠️ | Money/Email 已用，Phone 仍为 String |

### 三、反模式清单
| 反模式 | 位置 | 修复建议 |
|--------|------|---------|
| 上帝 Service | OrderService.java:45-320 | 拆分为 OrderPricingService + OrderFulfillmentService |

### 四、改进建议（按优先级）
1. [P0] 将 OrderAppService 中的 SQL 移到 Repository 实现
2. [P1] 将 User 实体改为充血模型
3. [P2] 为关键业务操作补充领域事件
```

**输出**：
- 代码审查评分报告（5 维度 + 总分）
- 反模式清单（含位置 + 修复建议）
- 分层合规检查矩阵
- 充血模型改造指引
- ArchUnit 合规检测脚本

**下一步引导**：
- `ddd-architecture-evaluator`（架构级别评估）
- 对应架构 Skill（修改目录结构）

**参考来源**：
- clean-ddd-hexagonal LAYERS.md（分层反模式）
- partme-docs 15（三层边界）

---

### Skill 12：ddd-architecture-evaluator

**定位**：架构评估与演进 — 定期评估 DDD 架构健康状况，制定演进路线

**目录**：`ddd-architecture-evaluator/`

**触发词**：`架构评估`、`架构演进`、`技术债务`、`DDD 成熟度`、`architecture assessment`、`架构重构`、`architecture fitness`、`迁移评估`

**核心能力**：

#### 1. DDD 成熟度评估模型

```
DDD 成熟度 5 级：

Level 1 — 初始级（Ad Hoc）
  □ 使用三层架构但无 DDD 概念
  □ 实体纯贫血模型
  □ 无聚合、无领域事件

Level 2 — 认知级（Aware）
  □ 部分实体具备充血模型
  □ 开始使用值对象（Money、Email 等）
  □ Service 中仍有业务逻辑

Level 3 — 实践级（Applied）
  □ 明确聚合边界，聚合间 ID 引用
  □ 仓储接口在 Domain 层，实现在 Infra 层
  □ 核心流程使用领域事件
  □ 分层依赖方向正确

Level 4 — 规模化（Scaled）
  □ 多限界上下文，上下文映射明确
  □ CQRS 在适当场景落地
  □ 架构自动校验（CI/CD 集成 ArchUnit）
  □ 事件驱动跨上下文通信

Level 5 — 优化级（Optimized）
  □ 持续架构演进机制
  □ Event Sourcing 在审计场景落地
  □ 领域模型与业务语言 100% 对齐
  □ 架构决策记录（ADR）完整可追溯
```

#### 2. 架构适配度评估

| 评估维度 | 检查内容 |
|---------|---------|
| **业务对齐度** | 当前架构是否匹配业务复杂度？是否过度设计/设计不足？ |
| **团队适配度** | 团队是否理解并遵循架构约定？是否需要简化？ |
| **技术适配度** | 所选架构与技术栈是否匹配？是否有阻碍？ |
| **演进能力** | 架构是否支持未来的业务扩展？重构成本多高？ |
| **交付效率** | 当前架构下新功能交付周期是否合理？ |

#### 3. 技术债务量化

```
技术债务类别：

结构性债务（P0）：
  - 分层违规数 / 模块总数
  - 循环依赖数
  - 贫血实体占比

设计性债务（P1）：
  - 聚合过大数（> 5 实体）
  - 缺少领域事件的关键业务操作
  - 值对象缺失率（String 代替值对象的字段占比）

测试性债务（P2）：
  - 领域层单元测试覆盖率
  - 聚合根测试覆盖率

债务评分：
  总分 = 结构性×0.5 + 设计性×0.3 + 测试性×0.2
  ≤ 20  → 🟢 健康
  21-40 → 🟡 轻度
  41-60 → 🟠 中度（建议制定偿还计划）
  > 60  → 🔴 重度（立即启动重构）
```

#### 4. 架构演进路线图

```
传统三层 → DDD 四层 → DDD 分层 + 部分充血 → 整洁/六边形 → 微服务+DDD

演进策略：

Phase 1: 止血（紧急）— 1-2 周
  → 修复 P0 分层违规
  → 切断循环依赖
  → 修复跨聚合直接引用

Phase 2: 微重构（短期）— 2-4 周
  → 核心聚合充血化（Order → Pay）
  → 引入值对象（Money → Phone → Address）
  → 补充关键领域事件

Phase 3: 架构升级（中期）— 1-3 月
  → 单体拆分限界上下文
  → 引入 CQRS（从 L1 开始）
  → 升级架构模式（根据需要）

Phase 4: 持续演进（长期）— 持续
  → 定期架构评估（每月）
  → 技术债务看板
  → ADR 持续记录
```

#### 5. 架构迁移评估

```
迁移前检查清单：
  □ 当前架构模式识别
  □ 团队 DDD 知识储备评估
  □ 业务复杂度评估（是否值得迁移）
  □ 迁移范围界定（全量 vs 渐进）
  □ 回退方案制定

渐进迁移策略（Strangler Fig Pattern）：
  1. 新功能 → 目标架构（DDD）
  2. 老功能 → 保持现状，逐步替换
  3. 核心聚合 → 优先迁移
  4. 非核心模块 → 最后迁移或永不迁移

迁移风险矩阵：
  ┌──────────┬──────────┬──────────┐
  │ 风险等级 │ 影响     │ 应对     │
  ├──────────┼──────────┼──────────┤
  │ 高       │ 核心业务 │ 灰度+回退 │
  │ 中       │ 非核心   │ 并行运行  │
  │ 低       │ 只读查询 │ 直接切换  │
  └──────────┴──────────┴──────────┘
```

**输出**：
- DDD 成熟度等级评估报告
- 技术债务量化评分 + 偿还优先级
- 架构适配度分析
- 架构演进路线图（分阶段）
- 迁移风险评估 + 回退方案
- 下次评估时间建议

**参考来源**：
- clean-ddd-hexagonal SKILL.md
- partme-docs 15（分层边界对照）

---

### Skill 13：ddd-event-storming

**定位**：事件风暴工作坊 — 多角色协作的领域探索方法论

**目录**：`ddd-event-storming/`

**触发词**：`事件风暴`、`Event Storming`、`工作坊`、`领域探索`、`workshop`、`领域事件`、`业务梳理`、`collaborative modeling`

**核心能力**：

#### 1. 事件风暴工作坊流程

```
事件风暴 6 步法：

Step 1: 混沌探索（Brainstorming）— 30 min
  参与者自由贴出领域事件（橙色便签）
  关注："发生了什么？"（用过去式动词）
  规则：不讨论、不质疑、不排序

Step 2: 时间线排序（Timeline）— 20 min
  按时间顺序排列事件
  识别事件流的分支与合并

Step 3: 关键事件标记（Pivotal Events）— 15 min
  标记业务流程的关键转折点
  如：订单已支付、用户已注册

Step 4: 命令与角色（Commands & Actors）— 30 min
  为每个事件添加：
    蓝色便签 — 命令（触发事件的动作）
    黄色便签 — 角色（谁触发了命令）

Step 5: 聚合识别（Aggregate Discovery）— 30 min
  将相关事件、命令聚类 → 识别聚合边界
  聚合命名（业务语言，非技术语言）

Step 6: 限界上下文划分（Bounded Context）— 20 min
  根据聚合间的耦合度划分上下文边界
  确定上下文映射关系

总时长：约 2.5 小时
参与角色：领域专家、产品经理、架构师、开发 Lead
```

#### 2. 便签颜色规范

```
橙色 (Domain Event)  — 领域事件（发生了什么）
  格式：动词过去式
  示例：订单已创建、支付已完成、库存已扣减

蓝色 (Command)       — 命令（触发了什么）
  格式：动词原形
  示例：创建订单、确认支付、扣减库存

黄色 (Actor/Policy)  — 角色或策略
  角色示例：买家、卖家、客服
  策略示例：自动取消未支付订单（30分钟超时）

绿色 (Read Model)    — 读模型
  格式：名词
  示例：订单详情页、订单列表、待支付订单看板

粉色 (External System)— 外部系统
  示例：支付宝、微信支付、物流系统

紫色 (Policy/Constraint)— 业务规则
  示例：单笔订单不超过 ¥50000、VIP 享 9 折
```

#### 3. 工作坊产出物

| 产出 | 格式 | 用途 |
|------|------|------|
| 事件时间线 | Mermaid 时序图 | 理解业务流程全貌 |
| 聚合候选清单 | Markdown 表格 | 输入给 domain-designer |
| 限界上下文划分 | Mermaid C4 图 | 输入给架构 Skill + 微服务设计 |
| 上下文映射图 | 战略设计图 | 上下文关系（ACL/OpenHost/Partner） |
| 热力图（Hot Spot） | Markdown | 标记有争议/不确定的区域 |
| 行动清单 | Markdown | 工作坊后的跟进任务 |

#### 4. 工作坊主持要点

```
会前准备：
  - 准备便签（5 种颜色） + 大白板/在线协作工具（Miro/Mural）
  - 邀请关键角色：领域专家 2-3 人、开发 2-3 人、产品 1 人
  - 明确本次工作坊范围（一个限界上下文 vs 整个系统）

会中主持：
  - 保持"不讨论"原则（Step 1），避免过早陷入细节
  - 引导用业务语言（非技术术语）
  - 记录 Hot Spot（有争议的地方），不立即解决

会后跟进：
  - 拍照/记录白板 → 数字化
  - 整理产出 → 输入给 ddd-domain-designer
  - Hot Spot 专项讨论（1-2 天后）
```

#### 5. 在线工作坊工具

| 工具 | 适用场景 | 特点 |
|------|---------|------|
| Miro | 分布式团队 | 内置事件风暴模板 |
| Mural | 分布式团队 | 协作白板 |
| draw.io | 简单场景 | 免费 |
| 实体白板 | 同地团队 | 互动感最强 |

**输出**：
- 事件时间线（Mermaid 格式）
- 聚合候选清单
- 限界上下文划分
- 上下文映射图
- Hot Spot 列表
- 下一步行动清单

**下一步引导**：
- `ddd-domain-designer`（将事件风暴结果转为详细领域设计）
- 对应架构 Skill（落地实现）

**参考来源**：
- Alberto Brandolini "Introducing Event Storming"
- clean-ddd-hexagonal DDD-STRATEGIC.md
- cleanddd-skills requirements-analysis / modeling
- partme-docs 03（域三分法）

---

### Skill 14：ddd-testing-strategist

**定位**：DDD 测试策略 — 从聚合测试到端到端验证

**目录**：`ddd-testing-strategist/`

**触发词**：`DDD 测试`、`聚合测试`、`领域测试`、`测试策略`、`testing strategy`、`单元测试 DDD`、`mock repository`、`六边形测试`

**核心能力**：

#### 1. DDD 测试金字塔

```
DDD 测试金字塔（自底向上）：

         ╱  E2E 测试      ╲       ← 10%：用户旅程、跨服务集成
        ╱─── 集成测试 ───╲         ← 20%：Repository 实现、Gateway、API
       ╱──── 领域测试 ────╲        ← 60%：聚合根、领域服务、领域事件
      ╱────── 单元测试 ────╲       ← 10%：值对象、工具方法

与经典测试金字塔的区别：
  - 聚合根测试 = 经典的 Service 层测试，但更聚焦业务规则
  - 领域事件测试 = DDD 独有的测试维度
  - Repository 测试 = 确保聚合根完整加载与保存
```

#### 2. 各层测试策略

```java
// ① 值对象测试 — 最简单，纯函数
@Test
public void money_should_prevent_negative_amount() {
    assertThrows(IllegalArgumentException.class, () -> new Money(-1.0, "CNY"));
}

@Test
public void money_add_should_sum_correctly() {
    Money m1 = new Money(10.0, "CNY");
    Money m2 = new Money(20.0, "CNY");
    assertEquals(new Money(30.0, "CNY"), m1.add(m2));
}

// ② 聚合根测试 — 核心，测试业务规则
@Test
public void order_pay_should_change_status_when_draft() {
    // Given: 一个草稿订单
    Order order = Order.create(customerId, items);

    // When: 支付
    order.pay(mockPaymentGateway);

    // Then: 状态变为已支付 + 发布领域事件
    assertEquals(OrderStatus.PAID, order.getStatus());
    assertTrue(order.getDomainEvents().stream()
        .anyMatch(e -> e instanceof OrderPaidEvent));
}

@Test
public void order_pay_should_fail_when_cancelled() {
    Order order = Order.create(customerId, items);
    order.cancel("客户请求");

    assertThrows(OrderException.class,
        () -> order.pay(mockPaymentGateway));
}

// ③ 领域服务测试 — Mock 仓储
@Test
public void pricing_service_should_apply_vip_discount() {
    // Given
    Order order = Order.create(vipCustomerId, items);
    when(orderRepository.findById(order.getId()))
        .thenReturn(Optional.of(order));

    // When
    pricingService.calculatePrice(order.getId());

    // Then
    assertEquals(new Money(90.0, "CNY"), order.getTotalAmount()); // 9折
}

// ④ 仓储实现测试 — 集成测试（含真实 DB 或 Testcontainers）
@SpringBootTest
@Testcontainers
public class OrderRepositoryImplTest {
    @Autowired private OrderRepository orderRepository;

    @Test
    public void should_save_and_load_aggregate_completely() {
        Order order = Order.create(customerId, items);
        orderRepository.save(order);

        Optional<Order> loaded = orderRepository.findById(order.getId());

        assertTrue(loaded.isPresent());
        assertEquals(order.getTotalAmount(), loaded.get().getTotalAmount());
        assertEquals(order.getItems().size(), loaded.get().getItems().size());
    }
}
```

#### 3. 测试策略选型指南

| 场景 | 推荐策略 | 原因 |
|------|---------|------|
| 简单 CRUD | 传统 Service + Repository 测试 | 无复杂领域逻辑 |
| 中等复杂（DDD 分层） | 聚合根测试为主 | 业务逻辑在聚合内 |
| 高复杂（六边形/整洁） | 端口 Mock + 适配器集成测试 | 内外隔离 |
| CQRS | Command 聚合测试 + Query 集成测试 | 读写分离 |
| Event Sourcing | 事件流重放测试 + 投影测试 | 事件即数据源 |
| 微服务 | 契约测试 + 聚合测试 + E2E | 多服务协作 |

#### 4. Mock 策略

```
Mock 策略矩阵：

┌──────────────────┬──────────┬──────────┬──────────┐
│ 测试目标 / Mock  │ Repository│ Gateway  │ EventBus │
├──────────────────┼──────────┼──────────┼──────────┤
│ 聚合根测试       │ 不需要   │ 不需要   │ 捕获验证 │
│ 领域服务测试     │ Mock     │ Mock     │ 捕获验证 │
│ 应用服务测试     │ Mock     │ Mock     │ Mock     │
│ 仓储集成测试     │ 真实DB   │ N/A      │ N/A      │
└──────────────────┴──────────┴──────────┴──────────┘

领域事件验证：
  // 捕获方式（Domain Event Assertion）
  assertThat(order.getDomainEvents())
      .hasSize(1)
      .first()
      .isInstanceOf(OrderPaidEvent.class)
      .hasFieldOrPropertyWithValue("orderId", order.getId());
```

#### 5. 持续测试策略

```
CI/CD 集成测试策略：

提交阶段（< 5 min）：
  ✓ 值对象单元测试
  ✓ 聚合根测试
  ✓ 领域服务测试（Mock Repository）

PR 阶段（< 15 min）：
  ✓ 仓储集成测试（Testcontainers）
  ✓ 应用服务集成测试
  ✓ API 契约测试

发布阶段（< 30 min）：
  ✓ E2E 测试（关键用户旅程）
  ✓ 性能测试（聚合加载 N+1 检测）
```

**输出**：
- DDD 测试策略文档（按层分级）
- 测试代码模板（值对象/聚合根/仓储/领域事件）
- Mock 策略指南
- CI/CD 集成测试配置
- 测试覆盖率目标建议
- N+1 查询检测方案

**下一步引导**：
- `ddd-devops-integration`（CI/CD 流水线集成）
- `ddd-code-reviewer`（测试覆盖率审查）

**参考来源**：
- clean-ddd-hexagonal TESTING.md
- xfg-ddd-skills（六边形架构测试规范）
- partme-docs 20（全面测试）

---

### Skill 15：ddd-devops-integration

**定位**：DDD 与 DevOps 集成 — CI/CD 流水线、容器化、可观测性

**目录**：`ddd-devops-integration/`

**触发词**：`DevOps DDD`、`CI/CD 流水线`、`DDD 容器化`、`DDD 监控`、`部署策略`、`架构自动化`、`pipeline`、`Docker`

**核心能力**：

#### 1. CI/CD 流水线中的 DDD 质量门禁

```
DDD 质量门禁流水线：

代码提交 → 静态分析 → 构建 → 测试 → 架构验证 → 安全扫描 → 部署
           │          │      │       │           │
           ▼          ▼      ▼       ▼           ▼
        Checkstyle  Maven  单元测试  ArchUnit   OWASP
        PMD        Gradle  集成测试  模块依赖
                            覆盖检查  命名检查

架构验证阶段（关键门禁）：
  1. ArchUnit 分层依赖方向检查
  2. Domain 层零依赖检查（无 Spring/JPA/MyBatis import）
  3. 模块间循环依赖检测
  4. 包命名是否符合 COLA/DDD 约定
  5. 公共路径访问检查

失败策略：
  P0 检查失败 → 阻止合并
  P1 检查失败 → 告警 + 需审批
  P2 检查失败 → 仅报告
```

#### 2. ArchUnit 自动化配置

```java
// CI/CD 集成的 ArchUnit 测试
@AnalyzeClasses(packages = "com.example")
public class ArchitectureComplianceTest {

    @ArchTest
    static final ArchRule domain_no_spring =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("org.springframework..")
            .because("Domain 层不允许依赖 Spring 框架");

    @ArchTest
    static final ArchRule domain_no_infrastructure =
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infrastructure..")
            .because("Domain 层不允许依赖基础设施层");

    @ArchTest
    static final ArchRule app_no_sql =
        noClasses()
            .that().resideInAPackage("..app..")
            .should().dependOnClassesThat()
            .resideInAPackage("java.sql..")
            .because("App 层不应直接操作 SQL");
}
```

#### 3. 容器化策略

```yaml
# 多模块 DDD 项目的 Docker 构建策略

场景 1：单体 DDD 应用
  构建策略：单 Dockerfile，打包全部模块
  部署：单容器 / K8s Pod

场景 2：DDD + CQRS（读写分离）
  构建策略：
    - Command 服务：Dockerfile（command 模块）
    - Query 服务：Dockerfile（query 模块）
  部署：两个独立 Pod，共享同一 Service

场景 3：微服务 + DDD（每个 BC 一个服务）
  构建策略：每个 BC 独立 Dockerfile
  部署：每个 BC 独立 Deployment + Service

Dockerfile 最佳实践：
  FROM eclipse-temurin:17-jre-alpine
  COPY start/target/*.jar app.jar
  HEALTHCHECK --interval=30s CMD curl -f http://localhost:8080/actuator/health
  ENTRYPOINT ["java", "-jar", "app.jar"]
```

#### 4. 可观测性

```
DDD 可观测性三支柱：

日志（Logging）：
  - 领域事件发布时记录（Event Type + Aggregate ID）
  - Repository 慢查询日志（> 100ms）
  - 跨聚合操作链路追踪（TraceId）

指标（Metrics）：
  - 领域事件发布速率（events/sec）
  - Repository 查询耗时分布（p50/p95/p99）
  - 聚合加载实体数分布（检测 N+1）
  - CQRS 命令处理延迟（Command → Event 延迟）

追踪（Tracing）：
  Controller → AppService → DomainService → Repository
  TraceId 贯穿整个调用链
  关键节点：UseCase 入口、Repository 调用、领域事件发布
```

#### 5. 数据库部署策略

| 场景 | 策略 | 工具 |
|------|------|------|
| DDD 分层/洋葱 | 单数据库 + Flyway/Liquibase | Flyway |
| CQRS L2（读写分离） | 主从同步 + 读库延迟容错 | MySQL 主从 / PG 流复制 |
| Event Sourcing | Event Store + 投影 DB | Axon / EventStoreDB |
| 微服务 + DDD | 每个 BC 独立数据库 | 每服务独立 Flyway 迁移 |

**输出**：
- CI/CD 流水线配置文件（GitHub Actions / GitLab CI）
- ArchUnit 依赖检查规则配置
- Dockerfile 模板（单体/CQRS/微服务）
- 可观测性配置（Logback/Micrometer/OpenTelemetry）
- 数据库迁移策略建议

**参考来源**：
- clean-ddd-hexagonal TESTING.md
- partme-docs 20
- COLA 5.0 架构规范

---

### Skill 16：ddd-architecture-doc

**定位**：架构文档生成 — ADR + C4 模型 + 架构决策记录

**目录**：`ddd-architecture-doc/`

**触发词**：`架构文档`、`ADR`、`C4 模型`、`架构图`、`architecture documentation`、`架构决策记录`、`技术文档`、`architecture decision record`

**核心能力**：

#### 1. ADR（Architecture Decision Record）

```markdown
# ADR-001：选择 COLA 架构作为项目基础架构

## 状态
已采纳 (2024-03-15)

## 背景
项目为电商中台系统，预计 5 个限界上下文，
团队 8 人（4 后端 + 2 前端 + 1 PM + 1 QA）。
需要统一的架构规范约束开发行为。

## 决策
采用 COLA v5 架构（菱形架构）作为项目基础架构，
单模块简化版。

## 备选方案
| 方案 | 优点 | 缺点 | 决定 |
|------|------|------|:--:|
| 传统三层 | 团队熟悉 | 复杂业务难以维护 | ✗ |
| 六边形 | 可测试性强 | 学习成本高 | ✗ |
| 整洁架构 | 企业级规范 | 过于复杂 | ✗ |
| **COLA v5** | 国内生态好，文档齐全 | — | ✓ |

## 决策理由
1. 团队使用 Spring Boot + MyBatis，COLA 对此生态最佳
2. COLA 5.0 中文文档齐全，降低团队学习成本
3. 具备架构校验能力，可持续约束开发行为

## 影响
- 模块数从 1 个增加到 4 个（adapter/app/domain/infrastructure）
- 新人上手需要 1 周 DDD + COLA 培训
- CI/CD 需增加 ArchUnit 检查步骤

## 关联
- ADR-002：CQRS 实施策略
- ADR-003：领域事件中间件选型
```

**ADR 模板**：
```
标准 ADR 格式：
  1. 标题（ADR-NNN：简短描述）
  2. 状态（提议/已采纳/已废弃/已替代）
  3. 背景（为什么需要这个决策）
  4. 决策（我们决定做什么）
  5. 备选方案（考虑过哪些方案）
  6. 决策理由（为什么选择这个方案）
  7. 影响（这个决策会改变什么）
  8. 关联（与其他 ADR 的关系）
```

#### 2. C4 模型图

```
C4 模型四层结构：

L1 — System Context（系统上下文图）：
  展示系统与外部用户/系统的交互

L2 — Container（容器图）：
  展示系统内部的主要容器（Web App / DB / MQ / 移动 App）

L3 — Component（组件图）：
  展示每个容器内部的主要组件
  DDD 语境下 = 限界上下文 + 聚合根 + 应用服务

L4 — Code（代码图）：
  展示组件内部的类/接口层次
  DDD 语境下 = 聚合内部结构（实体/值对象/领域服务/仓储）

DDD 与 C4 的映射：
  L1 = 系统整体（含所有限界上下文）
  L2 = 各限界上下文独立部署单元
  L3 = 限界上下文内部的模块结构（Adapter/App/Domain/Infra）
  L4 = 聚合内部细节（可选，通常由代码本身表达）
```

#### 3. 架构文档结构模板

```markdown
# {项目名} 架构文档

## 1. 架构概览
- 架构模式：COLA v5
- CQRS 级别：L1（模型分离）
- 架构图（C4 L1 + L2）

## 2. 限界上下文划分
| 上下文 | 类型 | 职责 | 微服务 |
|--------|------|------|:--:|
| Order Context | 核心域 | 订单管理 | ✓ |
| Payment Context | 核心域 | 支付处理 | ✓ |

## 3. 分层规范
（引用对应架构 Skill 的开发规范）

## 4. 技术栈
| 组件 | 技术 | 版本 |
|------|------|------|
| 框架 | Spring Boot | 3.4.x |
| ORM | MyBatis Plus | 3.5.x |

## 5. 部署架构
（K8s/Docker Compose 部署图）

## 6. 架构决策记录
（ADR 列表 + 索引）

## 7. 安全架构
（认证/授权/数据保护）

## 8. 运维手册
（监控/告警/日志/灾备）
```

**输出**：
- 架构决策记录（ADR 模板 + 示例）
- C4 模型 L1/L2/L3 图（Mermaid 格式）
- 架构文档完整模板
- ADR 索引 + 状态跟踪表
- 架构评审 Checklist

**参考来源**：
- Michael Nygard "Documenting Architecture Decisions"
- Simon Brown "C4 Model"
- clean-ddd-hexagonal SKILL.md
- partme-docs

---

## 五、Skill 间协作与数据流

### 5.1 Skill 协作全景图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         DDD Skills 协作流程                               │
└─────────────────────────────────────────────────────────────────────────┘

Phase 1: 学习 & 决策
  awesome ──→ selector
     │            │
     │  输出: 推荐架构 + CQRS级别 + 域划分
     │            │
     └────────────┘
          │
Phase 2: 架构落地（并行可选）
          │
     ┌────┼─────────────────────────────┐
     ▼    ▼        ▼        ▼          ▼
  layered onion hexagonal clean      cola
     │    │        │        │          │
     │    │   输出: 完整项目骨架 + Demo + 开发规范
     │    │        │        │          │
     └────┴────────┴────────┴──────────┘
          │
Phase 3: 领域设计（顺序或并行）
          │
     ┌────┼─────────────────────────────┐
     ▼    ▼                             ▼
  event-storming                  domain-designer
     │                                  │
     │  输出: 事件时间线 + 聚合候选        │
     │  输出: 聚合设计清单 + 限界上下文     │
     │                                  │
     └──────────┬───────────────────────┘
                │
Phase 4: 架构深化
                │
        ┌───────┼───────────┐
        ▼       ▼           ▼
    cqrs-arch  api-designer testing-strategist
        │       │           │
        │  输出: CQRS模型    │
        │  输出: REST API    │
        │  输出: 测试策略    │
        │       │           │
        └───────┼───────────┘
                │
Phase 5: 质量保障 & DevOps
                │
        ┌───────┼───────────┐
        ▼       ▼           ▼
    code-reviewer evaluator devops-integration
        │       │           │
        │  输出: 审查报告    │
        │  输出: 演进路线    │
        │  输出: CI/CD配置   │
        │       │           │
        └───────┼───────────┘
                │
Phase 6: 文档输出
                ▼
          architecture-doc
                │
           输出: ADR + C4 图 + 架构文档
```

### 5.2 数据流与共享契约

| 上游 Skill | 输出 | 下游 Skill | 输入 |
|-----------|------|-----------|------|
| **awesome** | DDD 概念理解 + 推荐架构类型 | **selector** | 用户初步认知 |
| **selector** | 架构推荐 + CQRS 级别 + 域划分 | **5 个架构 Skill** | 选定的架构类型 |
| **event-storming** | 事件时间线 + 聚合候选 | **domain-designer** | 已识别的事件和聚合 |
| **domain-designer** | 聚合设计清单 + 限界上下文 | **api-designer** | 聚合 + DTO 候选 |
| **domain-designer** | 聚合设计清单 + 限界上下文 | **cqrs-architecture** | 需要 CQRS 的聚合 |
| **5 个架构 Skill** | 项目骨架 + 代码模板 | **code-reviewer** | 待审查代码 |
| **code-reviewer** | 审查报告 + 违规清单 | **evaluator** | 技术债务数据 |
| **evaluator** | 演进路线 + 迁移方案 | **5 个架构 Skill** | 架构升级目标 |
| **testing-strategist** | 测试策略 + 覆盖率目标 | **devops-integration** | CI/CD 质量门禁 |
| **全部 Skill** | 各类设计产出 | **architecture-doc** | 文档素材 |

### 5.3 执行优先级

```
P0 — 必须优先实现（核心价值）：
  ├── ddd-architecture-awesome          # 入口，所有用户的第一步
  ├── ddd-architecture-selector         # 选型决策
  ├── ddd-architecture-cola             # COLA 是项目强关联
  ├── ddd-domain-designer               # 领域设计核心能力
  └── ddd-code-reviewer                 # 审查是高频使用场景

P1 — 重要但可后续补充：
  ├── ddd-architecture-hexagonal        # 与项目强关联（xfg-ddd-skills）
  ├── ddd-cqrs-architecture             # CQRS 作为独立能力
  ├── ddd-architecture-clean            # 整洁架构
  ├── ddd-api-designer                  # API 设计规范
  └── ddd-architecture-doc              # 文档输出

P2 — 增强能力：
  ├── ddd-architecture-layered          # 分层入门
  ├── ddd-architecture-onion            # 洋葱架构
  ├── ddd-architecture-evaluator        # 架构评估
  ├── ddd-event-storming                # 工作坊
  ├── ddd-testing-strategist            # 测试策略
  └── ddd-devops-integration            # DevOps 集成
```

---

## 六、与外部知识源的对应关系

### 6.1 每个 Skill 的参考来源明细

|-------|--------------------|----------------|-----------------|------------|-------------|
| **awesome** | SKILL.md, CHEATSHEET.md, LAYERS.md | — | — | DDD思维导图 | 01-05 |
| **selector** | SKILL.md, HEXAGONAL.md, CQRS-EVENTS.md | — | — | CQRS思维导图, 四种架构 | 01-10 |
| **layered** | LAYERS.md | — | — | ddd/1 | 07 |
| **onion** | SKILL.md | — | — | ddd/三种架构 | — |
| **hexagonal** | HEXAGONAL.md | 六边形架构编码规范 | — | ddd/2 | 08 |
| **clean** | SKILL.md | — | — | ddd/3 | — |
| **cola** | LAYERS.md | 六边形架构编码规范 | — | ddd/4, blogs/ | 13-16, 91 |
| **domain-designer** | DDD-STRATEGIC.md, DDD-TACTICAL.md | — | 需求→建模→编码 | — | 04, 05, 12, 14 |
| **cqrs-architecture** | CQRS-EVENTS.md | — | — | CQRS思维导图 | 06 |
| **api-designer** | SKILL.md | — | — | ddd/4 | 14 |
| **code-reviewer** | LAYERS.md（反模式), DDD-TACTICAL.md | — | — | blogs/ | 15 |
| **evaluator** | SKILL.md | — | — | DDD思维导图 | 15 |
| **event-storming** | DDD-STRATEGIC.md | — | 需求分析→建模 | DDD思维导图 | 03 |
| **testing-strategist** | TESTING.md | 测试规范 | — | — | 20 |
| **devops-integration** | TESTING.md | — | — | — | 20 |
| **architecture-doc** | SKILL.md | — | — | — | — |

### 6.2 知识复用优先级

```
编写 Skill 时知识源查阅优先级：

1. clean-ddd-hexagonal  # 最全面的 DDD 知识库（决策树、反模式表）
3. partme-docs          # 分层/渐进教学（01-20 + 91 加餐）
4. xfg-ddd-skills       # 六边形架构编码规范 + 测试规范
5. cleanddd-skills      # 需求分析 → 领域建模流程
```

---

## 七、实施路线图

### 7.1 迭代计划

```
Sprint 1（P0 Skills）：
  ├── ddd-architecture-awesome
  ├── ddd-architecture-selector
  ├── ddd-architecture-cola
  ├── ddd-domain-designer
  └── ddd-code-reviewer

Sprint 2（P1 Skills）：
  ├── ddd-architecture-hexagonal
  ├── ddd-cqrs-architecture
  ├── ddd-architecture-clean
  ├── ddd-api-designer
  └── ddd-architecture-doc

Sprint 3（P2 Skills）：
  ├── ddd-architecture-layered
  ├── ddd-architecture-onion
  ├── ddd-architecture-evaluator
  ├── ddd-event-storming
  ├── ddd-testing-strategist
  └── ddd-devops-integration
```

### 7.2 每个 Skill 的标准交付物

```
每个 Skill 目录标准结构：

ddd-{domain}-{name}/
├── SKILL.md                        # Skill 定义（遵循 Agent Skills 规范）
├── references/                     # 参考资料
│   ├── architecture-principles.md  # 架构原则与理论
│   ├── directory-structure.md     # 完整目录结构
│   ├── code-templates.md          # 代码模板
│   ├── java-examples.md           # Java 示例
│   ├── go-examples.md             # Go 示例（可选）
│   └── typescript-examples.md     # TypeScript 示例（可选）
└── outputs/                        # 输出物模板
    ├── templates/                  # 输出模板
    └── examples/                   # 示例输出
```

---

> 版本历史：v1.x（按 DDD 概念组织，已废弃） → v3.x（按用户旅程双层结构，已重构） → v4.0（5 种架构独立 Skill + CQRS 混合方案 + 16 个 Skill 生态）
> 最后更新：2026-05-28
> 维护者：ddd-skills 团队