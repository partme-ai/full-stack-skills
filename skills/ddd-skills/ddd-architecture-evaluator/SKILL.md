---
name: ddd-architecture-evaluator
description: DDD architecture evaluation and evolution — DDD maturity 5-level model (AdHoc/Aware/Applied/Scaled/Optimized), architecture fitness assessment (business alignment/team fit/tech fit/evolution capability), technical debt quantification with scoring, architecture evolution roadmap (4 phases), and migration risk assessment. Use when user asks about architecture evaluation, 架构评估, DDD maturity, 技术债务, architecture evolution, 架构演进, or needs to assess DDD implementation health.
license: Apache-2.0
---

# DDD Architecture Evaluator

Architecture evaluation & evolution — systematically assess DDD health, quantify technical debt, and plan architecture evolution. Supports any project type (Java/Go/Python/TS/.NET) with a structured, repeatable process.

## When to read

**打开此文档参考流程时可以开始评估**。当用户问及架构评估、DDD 成熟度、技术债务量化或架构演进时参考：
- "帮我评估一下项目架构" → 直接开始 Workflow
- "我们的 DDD 做得怎么样" → 从成熟度评估开始
- "技术债务太高了怎么办" → 从技术债务量化开始
- "需要从 MVC 迁移到 DDD" → 从演进路线图开始

## Workflow

```
Step 1: Assess Maturity
  → Run 5-level DDD maturity checklist (L1 → L5)
  → Identify current level vs target level (L3 is sufficient for most projects)
  → Output: Maturity level + per-level pass/fail + key gaps

Step 2: Evaluate Fitness
  → Score 5 dimensions: Business Alignment (25%), Team Fit (25%),
    Technology Fit (20%), Evolution Capability (15%), Delivery Efficiency (15%)
  → Calculate weighted fitness score
  → Output: Dimension scores + total fitness + green/yellow/orange/red rating

Step 3: Quantify Debt
  → Structural debt (P0, weight 0.5) — layer violations, circular deps, anemic entities
  → Design debt (P1, weight 0.3) — oversized aggregates, missing VOs/events
  → Testing debt (P2, weight 0.2) — domain unit test coverage
  → Output: Total debt score + health rating (green/mild/moderate/severe)

Step 4: Plan Evolution
  → 4-phase roadmap: Emergency (1-2w) → Short-term (2-4w) →
    Mid-term (1-3m) → Long-term (ongoing)
  → Migration risk assessment with Strangler Fig strategy
  → Output: Phased roadmap + risk matrix + next assessment date
```

## Boundary

### ✅ 擅长处理

| Area | What It Delivers |
|------|-----------------|
| DDD 成熟度评估 | L1-L5 逐级检查清单 + 得分计算 + 关键差距分析 |
| 架构适配度五维评估 | Business / Team / Technology / Evolution / Delivery 加权评分 |
| 技术债务量化 | 结构/设计/测试三类债务 + 加权分数 + 四档健康评级 |
| 架构演进路线图 | 4 阶段演进计划 + 每阶段时间估算 + 优先级排序 |
| 迁移风险评估 | Strangler Fig 渐进迁移方案 + 风险矩阵 + 回退策略 |
| 周期性架构健康检查 | 结构化评估报告 + 改进项追踪 + 下一次评估时间建议 |

### ⚠️ 需要条件

1. **项目有代码可审**：项目已运行一段时间，有实际代码库（全新项目建议用 `ddd-architecture-selector`）
2. **团队可提供项目背景**：需要参考架构文档、代码结构、团队规模等信息
3. **明确的评估目标**：建议指定评估焦点（整体成熟度 / 特定模块评估 / 迁移可行性）

### ❌ 不适用 / 超出范围

1. **代码级审查** → 使用 `ddd-code-reviewer`（反模式检测、分层合规检查）
2. **新项目架构选型** → 使用 `ddd-architecture-selector`（5 种架构对比决策矩阵）
3. **DDD 入门学习** → 使用 `ddd-architecture-awesome`（概念速查、充血vs贫血对比）
4. **架构具体落地实现** → 分别使用 `ddd-architecture-layered` / `onion` / `hexagonal` / `clean` / `cola`

## Security & 安全说明

本 Skill 是**非侵入式分析框架**。评估时不访问代码库、不收集项目数据、不上传任何信息。所有评估结果基于用户提供的上下文在当前对话中完成，不存储、不传输至第三方。用户自行决定是否披露项目结构信息。

## DDD Maturity 5-Level Model

| Level | Name | Focus | Pass Threshold |
|:-----:|------|-------|:-------------:|
| L1 | Ad Hoc（初始级） | 3-layer + anemic entities + all logic in Service | ≥ 5/7 |
| L2 | Aware（认知级） | Partial rich model + VOs in use + team awareness | ≥ 3/5 |
| L3 | Applied（实践级） | Aggregate boundaries + Domain zero-deps + rich entities | ≥ 5/7 |
| L4 | Scaled（规模化级） | Multi-BC + CQRS + automated ArchUnit CI | ≥ 5/7 |
| L5 | Optimized（优化级） | Continuous evolution + ES + ADR + debt dashboard | ≥ 5/7 |

> 完整逐级检查清单见 [maturity-levels-detail.md](references/maturity-levels-detail.md)。

## Architecture Fitness 5-Dimension Assessment

| Dimension | Weight | Score 1-5 | What to Check |
|-----------|:------:|:---------:|---------------|
| **Business Alignment** | 25% | 1-5 | Does architecture match business complexity? Over/under-engineered? |
| **Team Fit** | 25% | 1-5 | Does team understand and follow conventions? Violation rate? |
| **Technology Fit** | 20% | 1-5 | Does tech stack support the architecture? Friction points? |
| **Evolution Capability** | 15% | 1-5 | Can new BCs be added? Refactoring cost? Module coupling? |
| **Delivery Efficiency** | 15% | 1-5 | Feature delivery cycle vs industry baseline? Architecture overhead? |

```
Total Fitness = BA×0.25 + TF×0.25 + TechF×0.20 + EC×0.15 + DE×0.15

Score interpretation:
  ≥ 4.0 → 🟢 Excellent
  3.0-3.9 → 🟡 Adequate
  2.0-2.9 → 🟠 Concerning
  < 2.0  → 🔴 Critical
```

See [fitness-assessment-template.md](references/fitness-assessment-template.md) for full scoring rubrics and assessment prompts.

## Technical Debt Quantification

### Category Breakdown

| Category (Priority) | Weight | Metrics |
|--------------------|:------:|---------|
| **Structural Debt (P0)** | 0.5 | Layer violation ratio, circular dependency count, anemic entity %, framework leak % |
| **Design Debt (P1)** | 0.3 | Oversized aggregate ratio, missing domain event ratio, VO missing rate, cross-aggregate refs |
| **Testing Debt (P2)** | 0.2 | Domain unit test coverage, aggregate root test coverage, integration test coverage |

### Calculation

Total Debt = Structural×0.5 + Design×0.3 + Testing×0.2

| Score | Rating | Action |
|:-----:|:------:|--------|
| ≤ 20 | 🟢 Healthy | 无需干预 |
| 21–40 | 🟡 Mild | 定期偿还 |
| 41–60 | 🟠 Moderate | 本季度制定计划 |
| > 60 | 🔴 Severe | 立即启动重构 |

> 详细方法论和计算示例见 [debt-calculation-guide.md](references/debt-calculation-guide.md)。

## 4-Phase Evolution Roadmap

```
Traditional 3-Layer → DDD 4-Layer → DDD + Rich Domain → Hexagonal/Clean → Microservices + DDD
```

| Phase | Duration | Focus | Key Actions |
|-------|----------|-------|-------------|
| **1. Emergency** (止血) | 1-2 weeks | Fix P0 violations | Cut layer violations, remove circular deps, fix cross-aggregate refs |
| **2. Short-term** (微重构) | 2-4 weeks | Core domain richness | Rich-fy core aggregates, introduce VOs (Money/Phone/Address), add domain events |
| **3. Mid-term** (架构升级) | 1-3 months | Architecture upgrade | Split monolith into BCs, adopt CQRS (L1 start), upgrade pattern as needed |
| **4. Long-term** (持续演进) | Ongoing | Continuous evolution | Monthly fitness check, debt dashboard, ADR recording, team DDD training |

## Migration Risk Assessment

### Pre-Migration Checklist

- ☐ Architecture documented (C4 / ADR)
- ☐ Business complexity assessment done
- ☐ Team DDD knowledge assessed
- ☐ Migration scope defined (full vs incremental)
- ☐ Target architecture agreed (team + stakeholders)
- ☐ Rollback plan established (≤ 4 hours)

### Strangler Fig — New features → target arch; old features → keep + gradually replace; core aggregates → migrate first.

### Risk Matrix

| Risk Level | Impact | Response |
|:----------:|--------|----------|
| **High** | Core business logic | Canary release + automated rollback |
| **Medium** | Non-core features | Parallel run with traffic mirroring |
| **Low** | Read-only / queries | Direct switch with performance validation |

See [migration-risk-checklist.md](references/migration-risk-checklist.md) for full migration assessment templates.

## Gotchas

> 常见评估陷阱见 [references/gotchas.md](references/gotchas.md)。

## FAQ

| Question | Answer |
|----------|--------|
| 评估频率？ | 推荐季度评估。新功能频繁受阻、债务影响交付、重大业务变更时应触发。 |
| 一次评估要多久？ | 小型 1-2h，中型 0.5-1 天，大型 2-3 天。首次较长，后续可复用基线。 |
| 所有项目都需要 Level 5？ | 不是。Level 3 对大多数业务系统已足够。Level 4-5 适用于核心金融、交易系统。 |
| 如何度量进步？ | 建立基线，每次对比：成熟度变化、债务分数、改进项完成率（目标 ≥ 80%）。 |
| 评估后下一步？ | 修复 P0 → 核心域充血 → 架构升级 → 持续演进。每个阶段后快速复审。 |

## Keywords

DDD maturity, architecture fitness, technical debt, architecture evolution, migration assessment, Strangler Fig, bounded context, CQRS, Event Sourcing, architecture decision record, ADR, technical debt quantification, 架构评估, 成熟度模型, 技术债务量化, 架构演进, 迁移风险, 架构适配度, 分层合规

## References

- [maturity/assessment-workflow.md](references/maturity/assessment-workflow.md) — Maturity assessment preparation, session workflow, and common traps
- [maturity/maturity-levels-detail.md](references/maturity/maturity-levels-detail.md) — Per-level detailed checklists with scoring
- [fitness/scoring-rubric.md](references/fitness/scoring-rubric.md) — Scoring rubric with context-based calibration
- [fitness/fitness-assessment-template.md](references/fitness/fitness-assessment-template.md) — 5-dimension scoring rubrics and prompts
- [debt/repayment-strategies.md](references/debt/repayment-strategies.md) — Debt repayment strategies and prioritization matrix
- [debt/debt-calculation-guide.md](references/debt/debt-calculation-guide.md) — Technical debt methodology with examples
- [migration/strangler-fig-detailed.md](references/migration/strangler-fig-detailed.md) — Detailed Strangler Fig migration planning
- [migration/migration-risk-checklist.md](references/migration/migration-risk-checklist.md) — Migration readiness checklist and risk matrix
- [evolution-cases.md](references/evolution-cases.md) — Real-world evolution case studies (e-commerce, FinTech, SaaS)
- [code-smells-diagnosis.md](references/code-smells-diagnosis.md) — Architecture anti-patterns and diagnosis
- [migration-path.md](references/migration-path.md) — 6-step MVC-to-DDD migration path
- [partme-11-ddd-refactoring.md](references/partme-11-ddd-refactoring.md) — DDD refactoring case study with enterprise modeling
- [gotchas.md](references/gotchas.md) — 评估常见陷阱（评分偏差、迁移成本、团队能力等）
