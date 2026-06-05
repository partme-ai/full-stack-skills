# Base Skills 评估工具链设计说明

> 版本：v1.0 | 3 个核心 Skill，形成完整的 Agent Skill 质量评估工具链

---

## 一、设计哲学

### 1.1 为什么需要这套工具链

当前 AI Skill 生态以指数级增长（SkillHub 上已超 7 万 Skills），但质量参差不齐。对普通用户而言，判断一个 Skill 是否值得使用，主要依赖下载量、收藏数和星标数等热度指标。

对 Skill 开发者而言，缺少系统化的质量检测工具：写完一个 Skill 后，不知道它是否符合官方规范，不知道它在市场上算不算高质量。

Base Skills 以此为出发点，构建了从"知识整理"到"规范审查"再到"多维度质量评测"的完整评估链路。

| 用户真正想问的 | base-skills 对应 Skill |
|--------------|----------------------|
| "怎么写一个合格的 Skill？规范是什么？" | `skill-awesome` |
| "我的 Skill 符合 agentskills.io 官方规范吗？" | `skill-official-evaluation` |
| "我的 Skill 在市场上算高质量吗？能进 SkillHub 推荐吗？" | `skill-trace-evaluation` |

### 1.2 设计原则

**技能按评估深度组织，层层递进**：

```
用户旅程：我不知道规范 → 我学习规范 → 我检查合规 → 我评测质量
                       │                │              │
                       ▼                ▼              ▼
                  skill-awesome   skill-official   skill-trace
                                 -evaluation      -evaluation
```

| 原则 | 说明 |
|------|------|
| **知识先行** | `skill-awesome` 是第一入口，提供完整的 Skill 设计知识库，不让用户从零查文档 |
| **准绳对照** | `skill-official-evaluation` 以 agentskills.io 官方规范为唯一准绳，不做额外要求 |
| **多维度评测** | `skill-trace-evaluation` 引入 SkillHub TRACE 体系，从安全到效果全链路评分 |
| **各自独立** | 三个 Skill 可独立使用，不需要走完整链路 |
| **证据驱动** | 所有评测必须附证据，不接受"推测""感觉" |
| **输出可操作** | 每个 Skill 输出结构化评分 + 具体改进建议，不是泛泛评语 |

### 1.3 与 DDD Skills 的关系

| 维度 | DDD Skills | Base Skills |
|------|-----------|-------------|
| **目标用户** | 后端开发者（学 DDD、落地架构） | Skill 开发者（写 Skill、评估 Skill） |
| **技能数量** | 16 个 | 3 个 |
| **组织方式** | 按用户学习和使用路径（入门 → 选型 → 落地 → 审查 → 评估 → 文档） | 按评估深度递进（知识 → 合规 → 质量） |
| **输出产物** | 代码、配置、DDL、架构文档 | 评估报告（Markdown / JSON / HTML） |
| **核心概念** | DDD 战略/战术设计、5 种架构模式、CQRS | Agent Skills 规范、TRACE 评测体系 |

---

## 二、知识输入全景图

### 2.1 知识来源总览

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         Base Skills 知识输入                              │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   agentskills.io（官方规范）              SkillHub TRACE 体系              │
│   ┌────────────────────────────┐    ┌──────────────────────────────┐    │
│   │ Specification              │    │ T · Trust（安全可信）         │    │
│   │ Best Practices             │    │ R · Reliability（运行可靠）    │    │
│   │ Quickstart                 │    │ A · Adaptability（场景适用）   │    │
│   │ Optimizing Descriptions    │    │ C · Convention（结构规范）     │    │
│   │ Evaluating Skills          │    │ E · Effectiveness（效果增益）  │    │
│   │ Using Scripts              │    │                              │    │
│   └──────────────┬─────────────┘    │ 发布方：腾讯科技 × SkillHub   │    │
│                  │                  │        × 腾讯玄武实验室        │    │
│   Claude 官方指南 │                  │ 发布时间：2026-05-21           │    │
│   ┌──────────────┴─────────────┐    └──────────────┬───────────────┘    │
│   │ How to Create Custom Skills│                   │                    │
│   └──────────────┬─────────────┘                   │                    │
│                  │                                 │                    │
│                  ▼                                 ▼                    │
│   ┌──────────────────────────────────────────────────────────────────┐  │
│   │                    Base Skills (v1.0)                              │  │
│   │                    3 个核心 Skill                                   │  │
│   │                                                                    │  │
│   │  skill-awesome ──────────────► skill-official-evaluation            │  │
│   │  (知识层：规范+最佳实践)         (合规层：官方规范审查)                │  │
│   │                                      │                             │  │
│   │                                      ▼                             │  │
│   │                            skill-trace-evaluation                   │  │
│   │                            (质量层：五维度综合评测)                   │  │
│   └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### 2.2 知识源对各 Skill 的贡献矩阵

| 知识源 | skill-awesome | skill-official-evaluation | skill-trace-evaluation |
|--------|:---:|:---:|:---:|
| agentskills.io Specification | ● | ● | ○ |
| agentskills.io Best Practices | ● | ● | ○ |
| agentskills.io Quickstart | ● | ○ | ○ |
| agentskills.io Optimizing Descriptions | ● | ● | ○ |
| agentskills.io Evaluating Skills | ● | ● | ○ |
| agentskills.io Using Scripts | ● | ● | ○ |
| agentskills.io llms.txt | ● | ○ | ○ |
| Claude Custom Skills Guide | ● | ● | ○ |
| SkillHub TRACE 官方公告（中文原文） | ○ | ○ | ● |
| SkillHub TRACE 评分 Rubric | ○ | ○ | ● |
| SkillHub TRACE 写作指南 | ○ | ○ | ● |
| Script Safety Checklist | ● | ● | ○ |

> ● 核心依赖  ○ 参考依赖

---

## 三、技能全景图

### 3.1 按用户旅程排列

```
第1步：了解 Skill 设计规范
        │
        ▼
  ┌─────────────────────────────────────────────────────────────────┐
  │  skill-awesome                                                  │
  │  Agent Skills 设计知识库                                          │
  │  "怎么写一个合格的 Skill？命名规范、frontmatter、最佳实践是什么？"     │
  └────────────────────────────┬────────────────────────────────────┘
                               │
第2步：检查是否符合官方规范        │
        │                      ▼
        │   ┌─────────────────────────────────────────────────────────┐
        │   │  skill-official-evaluation                              │
        │   │  官方规范合规性审查                                        │
        │   │  "我的 Skill 符合 agentskills.io 官方规范吗？"              │
        │   │  检查：Spec合规 / 渐进式披露 / 描述触发 / 脚本安全 / 安全卫生    │
        │   │  结论：Pass / Needs improvement / Fail                   │
        │   └────────────────────────────┬────────────────────────────┘
        │                                │
第3步：多维度质量评测                    │
        │                                ▼
        │   ┌─────────────────────────────────────────────────────────┐
        │   │  skill-trace-evaluation                                 │
        │   │  TRACE 五维度质量评测                                     │
        │   │  "我的 Skill 在市场上算高质量吗？能进 SkillHub 推荐吗？"       │
        │   │  评分：T（安全可信）/ R（运行可靠）/ A（场景适用）              │
        │   │        C（结构规范）/ E（效果增益）                          │
        │   │  结论：优秀 / 良好 / 需改进（含雷达图 + 子项分）               │
        │   └─────────────────────────────────────────────────────────┘
```

### 3.2 技能调用路径

| 用户类型 | 推荐路径 |
|----------|---------|
| **刚写完第一个 Skill** | awesome（了解规范）→ official-evaluation（检查合规） |
| **准备发布 Skill** | official-evaluation（合规过关）→ trace-evaluation（质量评分） |
| **已有 Skill 想提升质量** | trace-evaluation（独立使用，看五维强弱项） |
| **只想快速判断合规性** | official-evaluation（独立使用） |
| **团队建立 Skill 质量标准** | awesome（知识库建立）→ 用两个评估 Skill 建立 CI 检查 |
| **提交 SkillHub Trace 严选** | trace-evaluation（必须通过 TRACE 评测） |

### 3.3 三种 Skill 的关系

```
┌─────────────────────────────────────────────────┐
│            base-skills 评估工具链                │
│                                                 │
│  knowledge (知识层)                               │
│  ┌─────────────────────────────────────────┐    │
│  │ skill-awesome                           │    │
│  │ 输入：官方文档/规范/最佳实践             │    │
│  │ 输出：Skill 设计知识（智能体内化）        │    │
│  │ 关心：该知道什么、怎么写才对             │    │
│  └───────────────┬─────────────────────────┘    │
│                  │                              │
│  compliance (规范层)                             │
│                  ▼                              │
│  ┌─────────────────────────────────────────┐    │
│  │ skill-official-evaluation               │    │
│  │ 输入：目标 Skill 目录                    │    │
│  │ 评分：agentskills.io 官方 Rubric         │    │
│  │ 输出：Pass/Needs improvement/Fail        │    │
│  │ 关心：合不合规范、有没有硬伤             │    │
│  └───────────────┬─────────────────────────┘    │
│                  │                              │
│  quality (质量层)                                │
│                  ▼                              │
│  ┌─────────────────────────────────────────┐    │
│  │ skill-trace-evaluation                  │    │
│  │ 输入：目标 Skill 目录                    │    │
│  │ 评分：SkillHub TRACE 5 维模型            │    │
│  │ 输出：综合评分 + 子项分 + 雷达图          │    │
│  │ 关心：好不好用、值不值得推荐             │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
│  official-evaluation 回答 "对不对"                │
│  trace-evaluation 回答 "好不好"                  │
│  awesome 回答 "该知道什么"                       │
└─────────────────────────────────────────────────┘
```

### 3.4 评估流程对比

| 对比维度 | skill-official-evaluation | skill-trace-evaluation |
|----------|--------------------------|------------------------|
| **评估框架** | agentskills.io 官方规范 | SkillHub TRACE 体系 |
| **发布方** | Anthropic（开源标准） | 腾讯科技 × SkillHub × 玄武实验室 |
| **核心问题** | "符合规范吗？" | "值得推荐吗？" |
| **输出** | Pass / Needs improvement / Fail | 优秀 / 良好 / 需改进（1-5 分） |
| **检查项** | 5 大检查项（Must/Should/Conditional） | 5 维度 × 若干子项（1.0-5.0 分） |
| **视觉呈现** | 清单表 | 雷达图 + 子项分表 |
| **使用时机** | 发布前合规检查 | 质量评估与排行榜 |
| **脚本输出** | Markdown / JSON | Markdown / JSON / HTML |

### 3.5 目录结构约定

每个 Skill 拥有独立目录，命名遵循 `skill-{name}` 格式：

```
skills/
├── base-skills/
│   ├── README.md                        # 本文件
│   │
│   ├── skill-awesome/                   # Skill 1：设计知识库
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   │   └── sample-awesome.md        # Awesome 列表示例
│   │   ├── references/
│   │   │   └── tag-taxonomy.md          # 标签分类体系
│   │   ├── scripts/
│   │   │   └── build_awesome.py         # 自动生成 Awesome 列表
│   │   └── LICENSE.txt
│   │
│   ├── skill-official-evaluation/       # Skill 2：官方规范评估
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   │   ├── sample-report.md         # 手工示例报告
│   │   │   └── mermaid-official-report.generated.md  # 脚本生成示例
│   │   ├── references/
│   │   │   ├── official-rubric.md       # 官方评分 Rubric
│   │   │   ├── official-sources.md      # 官方来源索引
│   │   │   └── script-safety-checklist.md # 脚本安全检查清单
│   │   ├── scripts/
│   │   │   └── official_evaluate.py     # 官方评估脚本
│   │   └── LICENSE.txt
│   │
│   ├── skill-trace-evaluation/          # Skill 3：TRACE 评测
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   │   └── trace-report.template.html  # HTML 报告模板（SkillHub 风格）
│   │   ├── examples/
│   │   │   ├── sample-report.md            # 手工示例报告
│   │   │   ├── mermaid-trace-report.generated.md   # 脚本生成 Markdown 示例
│   │   │   ├── mermaid-trace-report.generated.html # 脚本生成 HTML 示例
│   │   │   ├── jimeng-trace-report.generated.html   # 即梦技能 HTML 示例
│   │   │   └── mermaid-trace-report.template.generated.html  # 模板渲染示例
│   │   ├── references/
│   │   │   ├── trace-model-source.md    # TRACE 定义基线
│   │   │   ├── trace-rubric.md          # TRACE 评分 Checklist
│   │   │   └── trace-writing-guide.md   # TRACE 写作规范
│   │   ├── scripts/
│   │   │   └── trace_evaluate.py        # TRACE 评估脚本
│   │   └── LICENSE.txt
```

---

## 四、Skill 详细设计

---

### Skill 1：skill-awesome

**定位**：Agent Skills 设计知识库 — 评估工具链的第一入口

**触发词**：`设计技能`、`创建技能`、`技能规范`、`技能命名规则`、`SKILL.md 怎么写`、`frontmatter 规范`、`技能最佳实践`、`技能目录结构`、`渐进式披露`、`Agent Skills 规范`、`design a skill`、`skill specification`

**核心能力**：

```
用户问：                                awesome 回答：
──────────────────────────────────────────────────────────────────
SKILL.md 的 frontmatter 有哪些字段？     → name/description/license/compatibility/metadata 完整字段表 + 约束
name 有什么命名规则？                    → 正例（mermaid, roll-dice）+ 反例（My-Skill, -skill, skill--x）
渐进式披露怎么用？                       → 三阶段加载模型 + 正文不超 500 行的硬约束
怎么写一个能稳定触发的 description？      → 祈使语气 + 用户意图语言 + trigger/not-trigger 边界 + eval queries 测试法
脚本安全有哪些要求？                     → Required（非交互/--help/无密钥/安全默认值）+ Recommended（结构化输出/幂等/dry-run）
Gotchas/Template/Checklist 模式怎么写？   → 四种指令模式 + 完整 Markdown 示例
TRACE 评测体系是什么？                   → 五维度概览：T 安全/R 可靠/A 适用/C 规范/E 效果
```

**知识章节**（6 大章）：

| 章节 | 内容 |
|------|------|
| 1. Agent Skills Specification | 目录结构、SKILL.md 格式、frontmatter 字段约束、name 正反例、progressive disclosure 三阶段 |
| 2. Best Practices | 真实经验提取、Context 精打细算、控制粒度校准、Gotchas/Template/Checklist/Validation Loop 四种指令模式 |
| 3. Description Optimization | 四条原则（祈使语气/用户意图/bepushy/简洁）、Trigger 测试方法（eval queries + train/validation split） |
| 4. Script Safety Guidelines | Required（6 项）+ Recommended（5 项）+ 自包含脚本模式（PEP 723/Deno/Bun） |
| 5. Evaluation Frameworks | Official Rubric（5 维度 Must/Should/Conditional）+ TRACE 5 维模型概览 |
| 6. Complete Checklist | 创建 Skill 前的全套自检清单（Structure / Frontmatter / Body / Progressive Disclosure / Scripts / Trigger 共 18 项） |

**参考来源**：
- agentskills.io 全套官方文档（Spec / Best Practices / Quickstart / Optimizing Descriptions / Evaluating Skills / Using Scripts）
- Claude Custom Skills 官方指南
- SkillHub TRACE 评测体系

**配套脚本**：`scripts/build_awesome.py` — 自动扫描 skills 仓库生成 Awesome 列表索引

---

### Skill 2：skill-official-evaluation

**定位**：官方规范合规性审查 — 以 agentskills.io 官方规范为唯一准绳

**触发词**：`审查技能合规`、`官方规范评估`、`Skill 规范检查`、`技能安全审计`、`检查 SKILL.md 格式`、`生成官方评估报告`、`根据官方规范评估技能`、`review skill for spec compliance`、`official evaluation`

**核心能力**：

#### 五大检查维度（Must/Should/Conditional 分层）

| 维度 | 级别 | 检查内容 |
|------|------|---------|
| **Spec Compliance** | Must | SKILL.md 存在、frontmatter 完整、name 匹配目录且格式合法、description 非空且≤1024 字符、可选字段格式、目录结构 |
| **Progressive Disclosure** | Should | 正文简洁（≤500 行）、细节下沉 references/、引用有明确"何时读"触发条件、无深层引用链 |
| **Description Triggering** | Should | 使用用户意图语言、非纯实现描述、包含 trigger/not-trigger 边界 |
| **Script Readiness** | Conditional | 非交互 CLI、`--help` 可用、错误信息清晰、无密钥、安全默认值、结构化输出（推荐）、幂等（推荐） |
| **Security Hygiene** | Must | 无硬编码密钥、无可疑下载/外泄指令、破坏性操作需用户确认 |

#### 结论等级

| 等级 | 判定标准 |
|------|---------|
| **Pass** | Must 项全部通过，Should 项基本满足，无安全发现 |
| **Needs improvement** | Must 项通过，Should 项有较大 gap，无安全发现 |
| **Fail** | 存在 Must 项不通过，或有安全发现 |

**输出模板**：
- 结论 + Top 3 问题
- 规范对照清单表（项目/结果/证据/建议）
- 风险与限制
- 按优先级排序的改进建议

**配套脚本**：`scripts/official_evaluate.py` — 支持 `--format md/json`，自动检测 frontmatter、name 格式、密钥模式、交互式脚本

---

### Skill 3：skill-trace-evaluation

**定位**：多维度质量评测 — 基于 SkillHub TRACE 体系的全链路评估

**触发词**：`TRACE 评测`、`TRACE 评分`、`生成 TRACE 报告`、`T/R/A/C/E 评估`、`五维度技能评估`、`技能质量评测`、`技能质量报告`、`trace evaluation`、`trace scoring`

**核心能力**：

#### TRACE 五维度模型（SkillHub 官方中文原文内嵌）

| 维度 | 核心问题 | 重点关注 |
|------|---------|---------|
| **T · Trust**（安全可信） | "能安全使用吗？" | 红线维度。依赖来源、系统命令、数据泄露、越权访问、提示词攻击、远程执行、代码混淆 |
| **R · Reliability**（运行可靠） | "能稳定使用吗？" | 正常加载运行、过程稳定、输出完整、交付物可收集可评审、无超时/异常/依赖缺失 |
| **A · Adaptability**（场景适用） | "适合这个场景吗？" | 用户请求落入范围时 Agent 能否自然识别加载、描述是否清晰、相近 Skill 并存时能否正确选择 |
| **C · Convention**（结构规范） | "能被理解维护复用吗？" | SKILL.md 说明用途/范围/触发、元信息完整、目录组织合理、前置条件清楚、产物边界明确 |
| **E · Effectiveness**（效果增益） | "真正解决问题了吗？" | 效果底线（必须优于 no-skill 参照组）、正确性、完整度、归因分析、代价评估（token/耗时/复杂度） |

#### 评分体系

| 等级 | 分数 | 含义 |
|------|------|------|
| 优秀 | ≥ 4.5 | 五维均衡，明显优于 no-skill 基线，安全稳定 |
| 良好 | 3.5 – 4.4 | 整体扎实，特定维度有提升空间 |
| 需改进 | < 3.5 | 一个或多个维度有显著 gap |

每个维度含 2-4 个子项（共约 15 个子项），每项 1.0-5.0 分，含 dimension-level 中文评语。

#### 报告格式

支持三种输出：

| 格式 | 用途 | 特色 |
|------|------|------|
| **Markdown** | 人可读评测报告 | 五维度分项表 + 中文评语 + 改进建议 |
| **JSON** | 机器可读、CI 集成 | 结构化数据 |
| **HTML** | SkillHub 风格可视化 | 雷达图 + 综合评分 + 子项分表，匹配 `dashboard/evaluation` 页面布局 |

**输出模板**：
- 综合评分 + 评级 + 一句话结论
- 亮点/不足摘要
- 五维度详情（每个维度：dimension-level 中文评语 + 子项分表）
- 按优先级排序的改进建议

**配套脚本**：`scripts/trace_evaluate.py` — 支持 `--format md/json/html`，自动检测 frontmatter、密钥模式、目录结构、Workflow/Rules/验证模式，HTML 模式下生成雷达图

---

## 五、完整使用流程

### 5.1 典型场景：准备发布一个 Skill

```
                     skill-awesome
                    ┌──────────────────┐
Step 1: 学习规范     │ 智能体加载知识库   │
                    │ Spec + Best       │
                    │ Practices +       │
                    │ Script Safety     │
                    └────────┬─────────┘
                             │
                     skill-official-evaluation
                    ┌──────────────────┐
Step 2: 合规检查     │ 检查 frontmatter  │
                    │ 检查渐进式披露     │
                    │ 检查脚本安全性     │
                    │ → Pass/Fail       │
                    └────────┬─────────┘
                             │ (Pass)
                     skill-trace-evaluation
                    ┌──────────────────┐
Step 3: 质量评测     │ T 安全可信        │
                    │ R 运行可靠        │
                    │ A 场景适用        │
                    │ C 结构规范        │
                    │ E 效果增益        │
                    │ → 综合评分+雷达图  │
                    └──────────────────┘
```

### 5.2 CI/CD 集成思路

可以在 Skill 仓库的 CI 流程中集成两个评估 Skill 的脚本：

```bash
# 官方规范合规检查（阻断性：Fail 则阻止合并）
python3 skills/base-skills/skill-official-evaluation/scripts/official_evaluate.py \
  --skill-dir skills/my-skill \
  --format json > report.json

# TRACE 质量评测（非阻断性：评分低于阈值则告警）
python3 skills/base-skills/skill-trace-evaluation/scripts/trace_evaluate.py \
  --skill-dir skills/my-skill \
  --format html --output TRACE_REPORT.html
```

---

## 六、版本历史

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v1.0 | 2026-05 | 初始版本：skill-awesome、skill-official-evaluation、skill-trace-evaluation |
| v1.0.1 | 2026-05 | 合并 `skill-official-evaluating` 废弃目录，删除冗余文件 |
| v1.0.2 | 2026-05 | 合并 `skill-trace-evaluating` 废弃目录，迁移 4 个 generated 示例报告 |
| v1.0.3 | 2026-05 | TRACE 评测体系章节替换为 SkillHub 官方中文原文 |
