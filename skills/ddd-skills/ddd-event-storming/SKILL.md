---
name: ddd-event-storming
description: Event Storming workshop facilitation guide — collaborative domain exploration methodology with 6-step process (chaos exploration/timeline/pivotal events/commands & actors/aggregate discovery/bounded context), standardized sticky note color conventions (orange/blue/yellow/green/pink/purple), workshop preparation and facilitation tips, and digital tool recommendations. Use when user asks about event storming, 事件风暴, workshop, 工作坊, domain exploration, collaborative modeling, or needs to organize a DDD discovery workshop.
license: Apache-2.0
---

# DDD Event Storming

Event Storming (事件风暴) 是由 Alberto Brandolini 发明的协作式领域探索工作坊方法论。通过跨角色（领域专家 + 技术团队）的即时贴协作，在短时间内完成复杂业务领域的建模，产出聚合、限界上下文和领域事件。

## Workflow

6-Step Event Storming Workshop (约 2.5 小时):

1. **Step 1: 混沌探索** (30min) — 自由发散，贴出所有领域事件（🟠 橙色便签）
2. **Step 2: 时间线排序** (20min) — 按时间顺序排列事件，识别主线与分支
3. **Step 3: 关键事件标记** (15min) — 标记业务流程的转折点（★ 标记）
4. **Step 4: 命令与角色** (30min) — 为每个事件补全命令 + 角色
5. **Step 5: 聚合发现** (30min) — 聚类相关事件为聚合，命名聚合根
6. **Step 6: 限界上下文划分** (20min) — 按耦合度划分 BC，确定上下文映射

**产出物**: 事件时间线 / 聚合候选 / BC 映射 / Hot Spots

**参与角色**: 领域专家(2-3人) / 开发(2-3人) / 产品(1人) / 架构师(1人)

## When to Use

| 适用场景 | 不适用场景 |
|---------|-----------|
| 新项目启动，需要领域建模 | 领域知识已充分文档化，直接 `domain-designer` |
| 已有系统重构，业务不清晰 | 单人开发，无利益相关者参与 |
| 跨团队协作，需要统一语言 | 纯技术工具开发，无业务领域 |
| 微服务拆分，需确定服务边界 | 简单 CRUD 项目，领域模型清晰 |

### Skill Boundary

| 技能 | 定位 | 使用时机 |
|------|------|---------|
| `ddd-event-storming` | 工作坊主持 + 领域探索 | 项目前期，多角色协作 |
| `ddd-domain-designer` | 聚合详细设计 + 代码映射 | 工作坊之后，开发之前 |

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## 6-Step 流程详解

### Step 1: 混沌探索 — 30 min
参与者自由发散，用 🟠 **橙色便签** 贴出所有已知领域事件（动词过去式，如 OrderPlaced）。**禁止讨论**——主持人必须严格执行"先贴再说"原则。

```
活动: 自由贴出领域事件
格式: 动词过去式 (OrderPlaced, PaymentCompleted)
规则: 不讨论、不质疑、不排序
目标: 覆盖所有业务场景，包括异常流
```

### Step 2: 时间线排序 — 20 min
将所有 🟠 事件便签按时间顺序排列，识别主线与分支。主线用箭头连接，异常流从主线分叉标注条件。

### Step 3: 关键事件标记 — 15 min
标记业务流程的转折点，这些是关键事件（★ 标记），是领域模型的核心锚点。特征：触发后续流程、改变实体状态、跨上下文通信。

### Step 4: 命令与角色 — 30 min
为每个事件添加 🔵 **蓝色命令**（触发动作）和 🟡 **黄色角色**（执行者）。自动触发的事件也有命令发起者（System、Scheduler、ExternalSystem）。

```
👤 Customer  →  🔵 Create Order     →  🟠 OrderPlaced
👤 Admin     →  🔵 Approve Refund   →  🟠 RefundApproved
🤖 System    →  🔵 Deduct Stock     →  🟠 InventoryDeducted
```

### Step 5: 聚合发现 — 30 min
将相关的事件、命令聚类为聚合，并用业务语言命名聚合根。聚合是事务一致性边界——边界内强一致，边界间最终一致。

```
┌─ Order Aggregate ────────────────────────┐
│ 🟠 OrderPlaced / 🟠 OrderPaid           │
│ 🟠 OrderCancelled / 🟠 OrderCompleted   │
│ 🔵 PlaceOrder / 🔵 PayOrder             │
│ 👤 Customer                              │
│ 聚合根: Order  |  不变式: 已取消不可支付  │
└──────────────────────────────────────────┘
```

### Step 6: 限界上下文划分 — 20 min
根据聚合间的耦合度和业务语言变化划出 BC 边界，标注映射关系。上下文映射类型：Partnership、Shared Kernel、Customer-Supplier、Conformist、Anti-Corruption Layer、Open Host Service。

## 便签颜色规范

| 颜色 | 含义 | 格式要求 | 示例 |
|------|------|---------|------|
| 🟠 橙色 | Domain Event (领域事件) | 动词过去式 | OrderPaid, UserRegistered |
| 🔵 蓝色 | Command (命令) | 动词原形 | PayOrder, RegisterUser |
| 🟡 黄色 | Actor/Role (角色/参与者) | 名词 | Customer, System, Admin |
| 🟢 绿色 | Read Model (读模型/视图) | 名词 | OrderDetailPage, Dashboard |
| 🔴 粉色 | External System (外部系统) | 系统名 | Alipay, WeChatPay |
| 🟣 紫色 | Constraint/Hot Spot (约束/争议) | 业务规则语句 | Max ¥50000 per order |

## Workshop Outputs

产出物：Event Timeline (Mermaid 序列图)、Aggregate Candidates、Bounded Context Map (Mermaid C4 图)、Context Mapping、Hot Spot List、Ubiquitous Language 术语表。

## Facilitation Tips

- **会前**: 准备 5+ 色便签 + 大白板/Miro 模板；必须确保领域专家参与；明确工作坊范围；提前 5 分钟介绍颜色规范和流程
- **会中**: Step 1 禁止讨论（最常见的失败原因）；用业务语言优先；Hot Spot 用紫色便签标记不现场解决；严格时间盒管理；注意保持能量
- **会后**: 立刻拍照存档；24h 内将产出数字化为领域文档；安排 Hot Spot 跟进会；将产出物作为 `ddd-domain-designer` 的输入

## Online Tool Recommendations

Miro（分布式团队，推荐）| Mural（视频会议集成）| draw.io（免费轻量）| Physical Whiteboard（同地团队首选）

## Relationship with ddd-domain-designer

推荐路径: event-storming (工作坊产出) → domain-designer (聚合详细设计 + 代码落地) → Architecture Skill (架构实现)

event-storming 聚焦协作工作坊主持（领域专家 + 全体团队），产出便签墙、事件列表、BC 划分（概念级）；domain-designer 聚焦开发者聚合设计（开发者 + 架构师），产出代码结构、聚合类、仓储接口（代码级）。

## Customization

| 场景 | 建议调整 |
|------|---------|
| 小型团队(3-5人) | 合并 Step 1+2 为 20min+15min；Skip Step 6 直接讨论 |
| 大型团队(10+人) | Step 1 延长至 45min 分组并行贴便签；Step 6 增加 10min 分组汇报 |
| 时间受限(1小时) | 只做 Step 1-3（事件发散+排序），后续步骤单独安排 |
| 复杂领域(多 BC) | 每个 BC 单独一次工作坊，不要试图一次覆盖 |
| 跨语言团队 | 便签使用双语（中文事件+英文术语），以中文共识为准 |

## Quick Start

直接把需求发给 AI，以下开场白可直接使用：

```
"帮我组织一个电商订单履约的事件风暴工作坊，需要 6 步流程"
"我要做一个保险投保领域的事件风暴，领域专家有 2 位"
"做一次用户中台的事件风暴，重点关注认证和权限"
"之前做完了物流配送的事件风暴，帮我整理产出物"
```

如果你不确定从哪里开始，直接说"帮我做事件风暴"，AI 会自动引导你完成。

## Security & Safety

This skill is pure documentation. It contains no executable scripts, collects no user data, accesses no external services or networks.

## Gotchas — Common Pitfalls

1. **跳过 Brainstorming 直接讨论**: 必须先自由发散再排序。过早讨论事件正确性会扼杀创意。
2. **技术人员主导**: 必须由领域专家主导，开发做记录和提问。开发主导的模型不是真实业务。
3. **CRUD 式命令**: 不要写 "CRUD Order"，命令应该是业务动作：`PlaceOrder`、`CancelOrder`。
4. **遗忘 Hot Spot**: 所有分歧和不确定的边界必须记录为紫色便签。不记录的 Hot Spot 会后被遗忘。
5. **跳过 Aggregate Discovery**: 做完 Step 4 就结束。没有 Step 5 的聚类，事件风暴只是漂亮的便签墙。
6. **领域专家缺失**: 这是致命错误。没有领域专家参与事件风暴会产出错误的领域模型。
7. **试图一次覆盖整个企业**: 范围太大会导致浅尝辄止。建议从核心子域开始，一个 BC 一次。
8. **产出物不整理 → 便签墙变装饰品**: 工作坊结束后 24h 内必须将产出数字化，否则记忆会丢失。用 `workshop-output-template.md` 模板快速整理。
9. **没有通用语言记录**: 风暴中自然产生的术语定义的共识，必须记录下来成为 Ubiquitous Language 表。不记录等于没达成共识。

## FAQ

| 问题 | 回答 |
|------|------|
| 工作坊需要多长时间？ | 一次 BC 约 2.5 小时完整 6 步。中型项目总周期约 2 周。 |
| 没有正式领域专家怎么办？ | 从业务人员/产品经理/有领域经验的高级开发中选择。 |
| 线上和线下哪个更好？ | 线下（实体白板）互动感最强，线上（Miro）可异步协作。 |
| 需要多少参与者？ | 最小 3 人（领域专家+开发+产品），最优 6-8 人。 |
| 产出物如何使用？ | 作为 `ddd-domain-designer` 的输入，进入聚合详细设计和代码落地。 |
| 一个工作坊能覆盖多大范围？ | 推荐一个 BC 一次。复杂领域可按子域拆分多个工作坊。 |
| 主持人必须是 DDD 专家吗？ | 不需要精通 DDD，但需要理解 6 步流程和颜色规范，具备引导能力。 |
| 产出物怎么和代码对应？ | 聚合候选 → domain-designer Aggregate，事件 → Domain Event 类，BC → 微服务模块。 |

## References

详情见 [references/](references/) 和 [examples/](examples/)：
- **Templates**: sticky-note-template.md, timeline-example.md, workshop-output-template.md
- **Guides**: facilitation-checklist.md, workshop-deep-guide.md, context-mapping.md, partme-12-event-storming-modeling.md, ddd-strategic.md, clean-ddd-hexagonal-strategic.md
- **Examples**: 5 个工作坊案例（电商订单履约、保险投保、用户中台、物流配送、金融支付）
