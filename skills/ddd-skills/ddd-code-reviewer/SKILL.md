---
name: ddd-code-reviewer
description: DDD code review and anti-pattern detection — anemia model detection, layered compliance checking, aggregate design review, rich model verification, scoring system (5 dimensions), and ArchUnit automated validation. Use when user asks about code review, 代码审查, DDD review, 架构审查, anti-pattern detection, 反模式检测, or needs to check if code follows DDD.
license: Apache-2.0
---

# DDD Code Reviewer

DDD 代码审查 + 反模式检测 + 5 维度合规评分。验证代码是否遵循 DDD 最佳实践，输出结构化审查报告。

## Workflow

DDD 代码审查三步走：

```
Step 1: 代码扫描 — 反模式检测清单逐项检查 + 源代码扫描
Step 2: 评分计算 — 5 维度逐项评分（分层/领域/命名/结构/测试）
Step 3: 报告输出 — 结构化审查报告（评分 + 反模式列表 + 修复建议）
```

每次审查必须走完三步，输出完整报告。只口述问题不输出文档，团队无法追踪改进。

## When to Use

### 触发词（触发即用）

`代码审查` `DDD review` `反模式检测` `anti-pattern` `贫血模型` `充血模型检查` `架构审查` `分层合规` `代码质量评分` `layering compliance` `rich domain check` `review my DDD code`

### 适用前提

| 条件 | 说明 |
|------|------|
| 项目已采用 DDD 思想 | 非 DDD 项目无审查基础 |
| 有可审查的源代码 | 需提供代码路径或片段 |
| 期望发现反模式 | 不只是格式检查，更关注领域模型健康度 |

### 不适用场景

| 跳过 | 改用 |
|------|------|
| 非 DDD 项目（纯 CRUD） | 标准代码审查（SonarQube / Checkstyle） |
| 项目尚未引入 DDD | `ddd-architecture-awesome`（先学习 DDD 概念） |
| 刚写完第一个 DDD 代码 | 先写完再审查 |
| 需要架构选型 | `ddd-architecture-selector` |
| 需要架构健康度评估 | `ddd-architecture-evaluator` |

## Audience

This skill is designed for: **Backend developers** (implementing DDD architectures), **Software architects** (evaluating and selecting patterns), **Tech leads** (reviewing team implementations), and **DDD beginners** (learning domain-driven design fundamentals).

## Rules

1. Every code review must include a 5-dimension scoring report.
2. P0 anti-patterns (anemia model, layer violation, cross-aggregate ref) block merge.
3. Domain layer must have zero framework dependencies — verified via ArchUnit.
4. Review reports must include fix suggestions ordered by priority (P0→P1→P2).

## Anti-Pattern Checklist

12 种 DDD 反模式，按 P0（阻塞合并）/P1（下个版本前修复）/P2（持续改进）分级。

- **P0 — 必须修复**: 贫血模型、上帝 Service、跨聚合直接引用、领域层框架依赖、循环依赖、Repository 返回非聚合根
- **P1 — 应该修复**: Controller 业务逻辑、Application Service 有 SQL、值对象可变
- **P2 — 持续改进**: 聚合过大、缺少领域事件、跨聚合事务

> 完整反模式速查表见 [references/checklist.md](references/checklist.md)，含 Java 代码示例和修复路径。

## Layered Compliance Matrix

分层依赖检查规则（基于 ArchUnit）：

```
    ┌─────────────────┬─────┬─────┬─────┬─────┐
    │ 层 / 可依赖     │ Infra│ Dom │ App │ Adap│
    ├─────────────────┼─────┼─────┼─────┼─────┤
    │ Infrastructure  │  ✓  │  ✗  │  ✗  │  ✗  │
    │ Domain          │  ✗  │  ✓  │  ✗  │  ✗  │
    │ Application     │  ✓  │  ✓  │  ✓  │  ✗  │
    │ Adapter         │  ✓  │  ✓  │  ✓  │  ✓  │
    └─────────────────┴─────┴─────┴─────┴─────┘
```

**Domain 层零依赖规则（P0）**：
  - ✗ `import org.springframework.stereotype.Service`
  - ✗ `import javax.persistence.Entity`
  - ✗ `import org.apache.ibatis.annotations.Mapper`
  - ✓ `import java.util.Optional`
  - ✓ `import java.math.BigDecimal`

ArchUnit 完整配置见 [references/archunit-config.md](references/archunit-config.md)。

## Rich Domain Model Validation

Rich models encapsulate behavior in entities (pass); anemic models expose state via getters/setters (fail). Key: behavior in Entity vs behavior in Service.

> 完整代码示例和重构对比见 [examples/rich-model-refactoring.md](examples/rich-model-refactoring.md)，含 3 个实战案例。

## Scoring System

### 5 维度评分

| 维度 | 权重 | 检查项 | 满分 |
|------|:----:|--------|:----:|
| **1. 分层合规** | 30% | Domain 零依赖、依赖方向、App 无 SQL、Controller 无业务逻辑 | 30 |
| **2. 领域模型质量** | 30% | 充血模型覆盖率、值对象使用率、聚合设计、领域事件 | 30 |
| **3. 命名规范** | 15% | 聚合根 = 业务名称、Repository = 标准命名、事件 = 过去式 | 15 |
| **4. 代码结构** | 15% | 包按聚合组织、类大小、圈复杂度 | 15 |
| **5. 测试覆盖** | 10% | Domain 层测试覆盖、聚合根行为测试、事件验证 | 10 |

**总分 = Σ(维度得分 × 权重)**

### 分数等级

| 范围 | 等级 | 含义 | 行动 |
|:----:|:----:|------|------|
| ≥ 85 | 🟢 A | 优秀 DDD 实践 | 可上生产 |
| 70-84 | 🟡 B | 基本合规，有改进空间 | 修 P1 问题 |
| 50-69 | 🟠 C | 存在明显反模式 | 规划重构 Sprint |
| < 50 | 🔴 D | 需要大面积重构 | 阻塞合并，必须先重构 |

评分细则和计算示例见 [references/scoring-criteria.md](references/scoring-criteria.md)、[examples/scoring-example.md](examples/scoring-example.md)。

## Review Report Template

每次审查输出结构化报告，包含：

```markdown
# DDD Code Review Report

## Overall Score: 78/100 (🟡 B)

### 分层合规 (24/30)
| 检查项 | 结果 | 说明 |
|--------|:----:|------|
| Domain 零依赖 | ✅ | 无框架依赖 |
| App 层无 SQL | ❌ | OrderAppService L45 直接调用 Mapper |
| 依赖方向 | ✅ | 无反向依赖 |

### 领域模型质量 (22/30)
| 检查项 | 结果 | 说明 |
|--------|:----:|------|
| 充血模型 | ⚠️ | User 实体仍为贫血模型 |
| 值对象 | ⚠️ | Money/Email 已用，Phone 仍为 String |

### 反模式清单
| 严重级别 | 反模式 | 位置 | 修复建议 |
|:------:|--------|------|---------|
| P0 | 上帝 Service | OrderService.java:45-320 | 拆分为 OrderPricingService + OrderFulfillmentService |

### 改进建议（按优先级）
1. [P0] 将 OrderAppService 中的 SQL 移到 Repository 实现
2. [P1] 将 User 实体改为充血模型
3. [P2] 为关键业务操作补充领域事件
```

完整模板见 [references/report-template.md](references/report-template.md)、示例见 [examples/review-report-example.md](examples/review-report-example.md)。

## Gotchas

常见审查陷阱见 [references/gotchas.md](references/gotchas.md)。

## FAQ

| 问题 | 回答 |
|------|------|
| 一次审查要多久？ | 小项目（1-2 聚合）约 30-60 分钟；大项目按模块分次审查 |
| 评分是主观的吗？ | 每个检查项有明确检测标准（见 references/scoring-criteria.md），可重复、可验证 |
| ArchUnit 检查必须自己写吗？ | 直接使用 references/archunit-config.md 中的配置，复制到项目即可 |
| 找到了反模式，改不动怎么办？ | 以 P0 优先修复。P1/P2 记入技术债务，制定偿还计划 |
| 审查频率建议？ | 代码审查推荐 PR 合并前做。架构级审查推荐每季度一次 |
| 与非 DDD 架构的审查区别？ | DDD 审查关注领域模型健康度，非 DDD 审查关注代码规范/性能/安全 |

## Security & Safety

This skill is pure documentation. It contains no executable scripts, collects no user data, accesses no external services or networks.

## Keywords

DDD 代码审查、反模式检测、贫血模型、充血模型、上帝 Service、分层合规、依赖方向、ArchUnit、领域事件、值对象不可变、聚合设计、5 维度评分、代码质量门禁

## References

| 文件 | 用途 |
|------|------|
| [references/checklist.md](references/checklist.md) | 反模式速查表 — P0/P1/P2 分级 + 修复路径 |
| [references/scoring-criteria.md](references/scoring-criteria.md) | 5 维度评分细则 — 每项检查的权重和检测方法 |
| [references/archunit-config.md](references/archunit-config.md) | ArchUnit 完整配置 — Maven/Gradle 依赖 + 全套检查规则 |
| [references/report-template.md](references/report-template.md) | 审查报告模板 — Markdown + 快速摘要格式 |
| [references/clean-ddd-hexagonal-layers.md](references/clean-ddd-hexagonal-layers.md) | 四层架构结构详解 — Domain/App/Infra/Presentation |
| [references/clean-ddd-hexagonal-tactical.md](references/clean-ddd-hexagonal-tactical.md) | DDD 战术模式参考 — Entity/VO/Aggregate/Repository |
| [references/clean-ddd-hexagonal-testing.md](references/clean-ddd-hexagonal-testing.md) | 测试模式 — 单元测试/集成测试/架构测试 |
| [references/partme-15-boundaries.md](references/partme-15-boundaries.md) | 微服务边界理论 — 逻辑边界/物理边界/代码边界 |
| [references/gotchas.md](references/gotchas.md) | 审查常见陷阱 — 跨聚合引用、PO/DTO 混用等 |

## Examples

| 文件 | 用途 |
|------|------|
| [examples/review-report-example.md](examples/review-report-example.md) | 完整审查报告示例（62/100 🟠 C 级） |
| [examples/scoring-example.md](examples/scoring-example.md) | 评分计算全过程 + 修复 ROI 分析 |
| [examples/rich-model-refactoring.md](examples/rich-model-refactoring.md) | 贫血→充血模型重构：3 个实战案例 |
| [examples/anti-pattern-fix-guide.md](examples/anti-pattern-fix-guide.md) | 反模式修复路径速查 |
| [examples/archunit-compliance-test.md](examples/archunit-compliance-test.md) | ArchUnit 合规测试 — P0/P1/P2 门禁实现 |

## Next Steps

审查完成后，根据结果进入后续步骤：

- 架构级别评估 → `ddd-architecture-evaluator`
- 修复架构目录结构 → 对应架构 Skill（`ddd-architecture-layered` / `ddd-architecture-hexagonal` / `ddd-architecture-cola` 等）
- 提升测试覆盖率 → `ddd-testing-strategist`
- 输出架构文档 → `ddd-architecture-doc`
