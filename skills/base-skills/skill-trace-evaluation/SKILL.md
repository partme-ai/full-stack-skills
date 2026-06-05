---
name: skill-trace-evaluation
description: 对任意 Agent Skill 做 TRACE 五维度评测（T/R/A/C/E），输出 Markdown/HTML 报告与雷达图；当用户要求“TRACE 评测/打分/生成 TRACE 报告/五维度评估”或需要改进建议时使用。
license: Apache-2.0
---

# Skill TRACE 质量评测

> **评估模型：脚本计算确定性基分 + AI 阅读内容后语义校准（±0.3）→ 最终分。**
> 详细评分标准见 [references/scoring-criteria.md](references/scoring-criteria.md)，校准规则见 [references/calibration-guide.md](references/calibration-guide.md)。

---

## ⚡ 新手 30 秒入门

**干什么？** 对任意 Agent Skill 做 TRACE 五维度质量评分，输出带子项分的评估报告。

**什么时候触发？**
- 刚写完一个新 Skill，想知道质量怎么样 → 直接用
- 用户要求 "检查 Skill 质量"、"TRACE 评测"、"技能打分"
- 提供了 Skill 目录路径 + "评估"/"评测"/"打分" 关键词

**触发示例：**
```
✅ "用 TRACE 评测 /path/to/skill"
✅ "TRACE 评测 ddd-architecture-awesome"
✅ "对 skill-trace-evaluation 做五维度评估"
✅ "生成 TRACE 报告 + HTML 雷达图"
✅ "严格评测 jimeng-prompt-text2image"       （全部子项需 5.0）
✅ "快速检查这个 Skill 有哪些扣分项"          （仅输出扣分项）
✅ "只检查 T 维度"                            （单维度聚焦）
✅ "我修改了 FAQ，重新评测一下规范性"
✅ "输出 TRACE 五维画像 + 基线对比"
✅ "技能评估报告 + 官方合规检查"
```

**一句话流程：** 运行脚本拿基分 → 阅读 SKILL.md → 对照评分细则校准 → 产出报告。

---

## 执行时机

以下场景适合触发 TRACE 评测：

1. **新 Skill 完成编写**：刚写完 SKILL.md，想知道质量基线
2. **Skill 重大修改后**：修改了功能说明、FAQ、边界条件、触发词等核心内容
3. **用户明确要求**："检查 Skill 质量"、"TRACE 评测"、"技能打分"
4. **第三方评审**：平台审核员或社区用户对 Skill 做质量评估

---

## 能力边界说明

### ✅ 擅长处理

1. 评估任意 Agent Skill，输出 20 子项评分
2. 定位具体扣分原因，每个分数附证据
3. 生成标准化报告（dimension-level 中文评语 + 子项分表 + 改进建议）
4. 验证修改是否有效：修改后重新评测，对比前后分数变化
5. 对比两个版本差异：判断新版本比旧版本在哪些子项有实质提升
6. 支持标准/严格/快速/单维度四种模式

### ⚠️ 需要素材

1. 完整评估需要 Skill 目录路径（含 SKILL.md），只凭名称无法评测
2. R1/E1/E3 评分需要 AI 自己阅读正文判断语义质量——脚本只提供结构基分

### ❌ 超出范围（附替代方案）

1. 帮你写 Skill 内容 → 用 `skill-awesome`（规范知识）或 `skill-trace-checker`（发布前自检）
2. 评测非 Skill 类文档 → 找对应工具
3. 自动发布 Skill → 手动完成

---

## 评估流程

```
Step 1 ──── Step 2 ──── Step 3 ──── Step 4
收集基分    阅读技能    逐项校准    产出报告
────────────────────────────────────────────
trace_ev-   AI 直接    基分 ±0.3    Markdown
aluate.py   阅读正文    附调整理由    + 可选 HTML
```

### Step 1：收集基分

```bash
python3 scripts/trace_evaluate.py --skill-dir <path> --format json
```

输出含 `base_scores`：每子项 `base`（1.0-5.0）、`formula`（计算公式）、`evidence`（证据字段）。

### Step 2：阅读技能

必须自己阅读 SKILL.md 正文 + 扫描 references/、examples/ 目录。脚本提供结构数据，AI 判断内容质量。

**AI 阅读时的检查思路示例：**

```
【T 维】
  安全 → 查有无密钥/secrets/脚本，正文有无安全声明
  国内 → 查全文中文化程度、示例是否基于国内平台
  边界 → 查有无独立边界章节、三分类是否每类≥3例
  隐私 → 查有无数据隐私说明（FAQ 或专项章节）

【R 维】
  异常 → 查 Gotchas 是否包含"交互式引导模板"（先假设版本→列缺失项）
  功能 → 查 workflow 步骤是否覆盖所有声明功能
  稳定 → 查有无 validate-plan-execute 循环或等效约束
  降级 → 查边界章节中超范围后是否给替代方案

【A 维】
  边界定义 → 查三分类是否有场景化判断逻辑（"什么时候该用/不该用/模糊怎么判"）
  触发 → 查 description 信息量，是关键词堆砌还是场景化路由
  受众 → 查有无显式说明适用用户类型
  定制 → 查有无风格/参数传递机制

【C 维】
  文档 → 查 examples 数量是否达标（prompt≥10/cli≥4/doc≥5）
  披露 → 查 body 行数 + references 文件数，是否三层结构
  结构 → 查 name 规范 + refs 子目录≥2
  反模式/FAQ → 查 Gotchas 数量是否≥5 + FAQ 是否≥6且非充数

【E 维】
  准确 → 查有无"禁止胡编"规则或等效约束
  完整 → 查 examples 数量是否达阈值（prompt≥25/cli≥4/doc≥5）
  增值 → 查 refs 子目录≥2 + 是否有评估框架/决策树等深度领域知识
  开箱 → 查有无快速开始章节 + ≥3 个可复制开场白
```

### Step 3：逐项校准

查 `base` → 读 [references/scoring-criteria.md](references/scoring-criteria.md) 中该子项的满分标准 + 扣分原因 → 判断正文内容匹配哪一档 → 按 [references/calibration-guide.md](references/calibration-guide.md) 调整（±0.3）→ 附一句调整理由。

### Step 4：产出报告 ⚠️ 必须执行

**评分完成后必须输出报告，不允许只口头报告分数而不写入文件。**

报告使用统一模板，模板文件中有 `{...}` 占位符，替换为实际评估结果后写入目标文件。

#### 报告模板

| 格式 | 模板文件 | 说明 |
|------|----------|------|
| **Markdown** | `examples/trace-report.generated.md` | 纯文本，控制台可读，适合存档和 diff |
| **HTML** | `examples/trace-report.generated.html` | 可视化雷达图 + Tailwind 卡片，适合浏览器展示和分享 |

#### 让用户选择格式

**评分完成后，必须用 AskUserQuestion 工具询问用户选择输出格式：**

```
问题：评估完成，请选择报告输出格式
选项：
- "Markdown 报告" — 使用 examples/trace-report.generated.md 模板，输出纯文本报告
- "HTML 报告" — 使用 examples/trace-report.generated.html 模板，输出含 SVG 雷达图的交互式报告
- "两者都要" — 同时输出 Markdown + HTML
```

**用户选择后：**
- 选 "Markdown" → 基于 `trace-report.generated.md` 模板填入数据 → 写入 `{skill-dir}/trace-report.md`
- 选 "HTML" → 基于 `trace-report.generated.html` 模板填入数据 → 写入 `{skill-dir}/evaluation-report.html`
- 选 "两者都要" → 同时生成上述两个文件

**写入完成后，必须向用户报告文件路径。**

#### Markdown 报告结构

1. 综合评分表（5 维 + 综合）
2. 一句结语
3. 五维详析（每维 4 子项：得分 + 证据 + 建议）
4. no-skill 基线对比表
5. 官方规范合规表（10 项 agentskills.io 检查）
6. 优化建议（优先级排序 P1/P2/P3）
7. Skill 基础画像

#### HTML 报告包含

- SVG 雷达图（T/R/A/C/E 五轴）
- 五维评分卡片 + 进度条
- 20 子项详表（每子项：得分 + 证据 + 建议）
- 基线对比 + 官方合规 + 优化建议 + Skill 画像
- 支持 Print 和移动端响应式

### 评测后的改进指引

TRACE 评测不只是打一个分数，最终目标是帮助 Skill 达到更高质量。评测报告产出后：

1. **定位扣分项**：查看报告中 < 5.0 的子项，对照 [scoring-criteria.md](references/scoring-criteria.md) 中该子项的"满分标准"和"修改对比"示例
2. **修改对应文件**：每个扣分点都必须对应 SKILL.md 或 references/ 文件的实质改动（禁止只改报告措辞不修改文件）
3. **重新评测验证**：修改后再次运行评测，确认分数有实质提升
4. **参考案例**：不知道怎么改时，查看 [trace-anti-patterns.md](references/trace-anti-patterns.md) 中同类问题的正确修复方式

> 评分在 4.8 及以上时可视为达到实用标准，不必无限追求字面上的 5.0。

---

## 评分标准速查

评分细则全文在 [references/scoring-criteria.md](references/scoring-criteria.md)，校准规则全文在 [references/calibration-guide.md](references/calibration-guide.md)。以下为 20 子项的基分公式 + 满分标准摘要。

### T · Trust（可信任度）

| ID | 名称 | 基分公式 | 满分标准摘要 |
|----|------|---------|------------|
| T1 | 安全性扫描 | `4.5 + no_scripts(+0.3) + secdecl(+0.2) - secrets(-1.0)` | 无密钥+无scripts+有安全声明 |
| T2 | 国内适配性 | `has_chinese ? 5.0 : 2.0` | 全中文，示例基于国内平台 |
| T3 | 边界透明度 | `boundary ? 4.5+0.3(when_to_use) : 3.0` | 三分类（✅/⚠/❌），每类≥3例 |
| T4 | 数据隐私规范 | `4.5 + secdecl(+0.5) - scripts(-0.2)` | 声明"不收集/不处理数据" |

**T 维扣分常见原因：** 示例全是英文场景；没有隐私使用说明；边界描述模糊（只说"有些场景不支持"）。

### R · Reliability（可靠性）

| ID | 名称 | 基分公式 | 满分标准摘要 |
|----|------|---------|------------|
| R1 | 异常处理 | `gotchas ? 4.0+0.5(val) : 3.0` | Gotchas + 交互式引导模板 |
| R2 | 功能完善性 | `WF ? 4.5+0.3(steps≥5或exs≥10) : 3.5~4.0` | Workflow+场景覆盖无死角 |
| R3 | 运行稳定性 | `4.0 + gotchas/rules(+0.3) + val(+0.2)` | 约束规则+校验清单 |
| R4 | 降级兜底 | `boundary ? 4.5 : 3.5` | 超出范围给替代工具引导 |

**R 维扣分常见原因：** 用户输入不完整时 AI 直接停下问，没有先给假设版本；超范围请求直接拒绝，没有替代方案引导。

### A · Adaptability（适用性）

| ID | 名称 | 基分公式 | 满分标准摘要 |
|----|------|---------|------------|
| A1 | 能力边界定义 | `boundary+when_to_use ? 4.5 : 4.0` | 场景化判断逻辑 |
| A2 | 触发方式 | `desc≥100 ? 5.0 : 3.5~4.5` | 场景化路由，非关键词堆砌 |
| A3 | 受众广度 | `4.0 + chinese(+0.3)` | 显式说明适用用户类型 |
| A4 | 定制化支持 | `type=cli或exs≥10 ? 4.5 : 4.0` | 风格卡片/场景参数/配置机制 |

**A 维扣分常见原因：** 触发方式只有关键词列表，没有"什么情况用哪个功能"的判断逻辑；没有说明不同类型用户如何使用。

### C · Convention（规范性）

| ID | 名称 | 基分公式 | 满分标准摘要 |
|----|------|---------|------------|
| C1 | 文档质量 | `exs≥阈值(cli=4/prompt=10) ? 5.0 : 3.5~4.5` | 示例可直接复制、格式规范 |
| C2 | 渐进式披露 | `refs≥8+body<200 ? 5.0 : 3.0~4.5+th(+0.2)` | 三层结构30秒上手 |
| C3 | 结构清晰 | `4.5 + name(+0.2) + refsd≥2(+0.3)` | refs子目录≥2 |
| C4 | 反模式与FAQ | `gotchas ? 4.5+0.3(gc≥5) : 3.5` | Gotchas≥5 + FAQ≥6非充数 |

**C 维扣分常见原因：** 没有 references/ 深度文档；FAQ 只有 3~4 题覆盖面不够；无反模式案例，用户不知道什么做法会导致差输出。

### E · Effectiveness（有效性）

| ID | 名称 | 基分公式 | 满分标准摘要 |
|----|------|---------|------------|
| E1 | 输出准确性 | `WF ? 4.5+0.3(val) : 4.0` | 场景区分明确、禁止胡编规则 |
| E2 | 内容完整度 | `exs≥阈值(prompt=25/cli=4/doc=5) ? 5.0 : 3.0~4.5` | 场景全覆盖、E2E示例 |
| E3 | 创造力与增值 | `refsd≥2 ? 4.5+0.2(refs≥10) : 4.0` | 评估框架/决策树/领域知识体系 |
| E4 | 开箱即用度 | `4.0 + WF(+0.3) + val(+0.3) + gotchas(+0.2) + cli(+0.2)` | 快速开始章节+可复制开场白 |

**E 维扣分常见原因：** 没有新手入门引导，用户不知道从哪里开始；输出示例不够真实（用通用模板而非真实场景）；缺乏增值特性，只是机械执行指令。

---

## 定制化使用指南

在触发时可传入以下参数定制评测行为：

| 模式 | 触发关键词 | 行为 |
|------|-----------|------|
| **标准模式** | `"TRACE 评测"`（默认） | 全量 20 子项评测，输出完整报告 |
| **严格模式** | `"严格评测"` | 所有子项必须达到 5.0，中间分视为不合格 |
| **快速模式** | `"快速检查"` / `"只看扣分项"` | 仅输出 < 4.5 的扣分项，跳过满分说明 |
| **专项模式** | `"只检查 [维度]"` | 聚焦单个维度，其他维度跳过 |
| **对比模式** | `"对比修改前后"` | 提供两版路径 → 输出差异对比表 |
| **HTML 报告** | `"生成雷达图"` / `"可视化"` | 除 Markdown 外，额外生成含 radar 图的 HTML |

---

## 校准规则速查

| # | 规则 | 说明 |
|---|------|------|
| 1 | 仅在有语义信号时调整 | 正文有满分模式→上调，有扣分模式→下调。都不匹配→不调 |
| 2 | 调幅 ±0.3 | 单子项 max ±0.3。4.5 不能跳到 5.0（只能到 4.8） |
| 3 | 附调整理由 | 一句中文，引用具体内容 |
| 4 | 去重降档 | `ref_names` 有 ≥3 同版本前缀 → C2/E2 降一档（max 4.5） |
| 5 | 完美阈值缓冲 | 同维 4 子项全可到 5.0 → 查隐性瑕疵 → 有则 max 4.8 |
| 6 | 类型感知 | CLI型 C2=150行 E2=4exs。脚本已内置 |

---

## 综合评分

五维均分 = Overall。

| Rating | Score |
|--------|-------|
| **Excellent (优秀)** | ≥ 4.5 |
| **Good (良好)** | 3.5 – 4.4 |
| **Needs improvement (需改进)** | < 3.5 |

---

## 报告模板

```md
# TRACE Evaluation Report

Target: `<path>`

## Overall Assessment

**Overall Score: X.X / 5**
**Overall Rating: Excellent (优秀) / Good (良好) / Needs improvement (需改进)**

One-sentence conclusion: ...（自然中文，具体不空洞）

## TRACE Dimension Explanation

SkillHub TRACE 评测体系从**可信任度、可靠性、适用性、规范性、有效性**五个维度全面评估。
[了解详情](https://skillhub.cn/tutorials#trace-evaluation)

评测基于 AI 自动化检测，结果供参考。

## Evaluation Details

### T · Trust — X.X / 5
（1-2 句中文）

| Sub-item | Score | Commentary |
|----------|-------|------------|
| 安全性扫描 | X.X | 一句话证据 |
| 国内适配性 | X.X | ... |
| 边界透明度 | X.X | ... |
| 数据隐私规范 | X.X | ... |

### R · Reliability — X.X / 5
（中文评语）

| Sub-item | Score | Commentary |
|----------|-------|------------|
| 异常处理 | X.X | ... |
| 功能完善性 | X.X | ... |
| 运行稳定性 | X.X | ... |
| 降级兜底 | X.X | ... |

### A · Adaptability — X.X / 5
| Sub-item | Score | Commentary |
|----------|-------|------------|
| 能力边界定义 | X.X | ... |
| 触发方式 | X.X | ... |
| 受众广度 | X.X | ... |
| 定制化支持 | X.X | ... |

### C · Convention — X.X / 5
| Sub-item | Score | Commentary |
|----------|-------|------------|
| 文档质量 | X.X | ... |
| 渐进式披露 | X.X | ... |
| 结构清晰 | X.X | ... |
| 反模式与FAQ | X.X | ... |

### E · Effectiveness — X.X / 5
| Sub-item | Score | Commentary |
|----------|-------|------------|
| 输出准确性 | X.X | ... |
| 内容完整度 | X.X | ... |
| 创造力与增值 | X.X | ... |
| 开箱即用度 | X.X | ... |

## Improvement Suggestions (prioritized)

1. ...（具体、可行动）
2. ...
3. ...
```

### 评语规范

- **dimension-level**：1-2 句自然中文，抓住核心。✅ "纯文档型零风险，全中文专为即梦打造。边界清晰但未声明数据隐私" ❌ "整体表现良好"
- **sub-item**：一句话引用证据。✅ "Gotchas 13 条+checklist，但缺交互式引导模板" ❌ "安全方面没问题"

**各维度建议措辞：**

| 维度 | 正面措辞示例 | 负面措辞示例 |
|------|------------|------------|
| **T** | 未发现敏感信息硬编码；安全声明完整 | 发现疑似凭据模式需移除；缺少数据边界说明 |
| **R** | 异常输入有自检与提示；失败路径处理清晰 | 对异常输入缺少自检提示；缺少降级兜底策略 |
| **A** | 明确了不适用边界因此不易误用；有 near-miss 防范 | 描述过泛导致误触发；与相邻技能能力边界冲突 |
| **C** | 结构遵循快速上手→流程→示例且细节下沉 references/ | 内容堆在 SKILL.md 缺索引/目录；示例不可复制 |
| **E** | 示例覆盖主流场景拿来就能用；能显著减少返工 | 高级场景指导不足；只能完成浅层输出 |

---

## 受众说明

| 用户类型 | 使用方式 |
|---------|---------|
| **Skill 评测者** | 对社区或平台上的 Skill 做第三方质量评估，输出标准化报告 |
| **平台审核员** | 使用本标准作为统一评审框架，确保审核口径一致 |
| **Skill 作者自查** | 发布前自检，定位短板并针对性修改 |
| **社区用户** | 选 Skill 前快速了解质量，或对比多个同类型 Skill |

---

## 常见问题 FAQ

**Q1：脚本基分和 AI 校准分不一致，以哪个为准？**
最终报告中的分数 = 基分 ± AI 语义校准。校准只允许 ±0.3，所以两者不会差太远。如果差幅超过 0.3，说明该子项的满分标准描述模糊，建议对照 [scoring-criteria.md](references/scoring-criteria.md) 中该子项的"4.5 vs 5.0 比对"案例找到客观标准。

**Q2：我只改了 Skill 的几行文字，需要重新做 TRACE 吗？**
修改了功能说明、FAQ、边界条件、触发词等影响使用体验的内容 → 需要重新评测。只修正了错别字或格式 → 不需要。

**Q3：TRACE 评测结果是 AI 自动打的还是人工打的？**
脚本计算确定性基分（结构检测），AI 阅读正文后做语义校准（±0.3），最终由 AI 综合输出。具有一致性但不保证与 SkillHub 官方评测结果完全一致——官方还涉及用户行为数据维度。

**Q4：某个子项反复评测还是不给满分，怎么办？**
对照 [references/scoring-criteria.md](references/scoring-criteria.md) 中该子项的"满分标准"和"4.5 vs 5.0 对比"案例。对比案例展示了刚好 5.0 的具体格式要求，找到差距后针对性修改文件。

**Q5：references/ 下的文件不存在，该子项怎么评分？**
不存在 = 该标准未满足 = 脚本基分最多给 4.0。必须创建对应文件并填充实质内容，AI 校准后才可能达到 5.0。

**Q6：我可以只检查某一个维度吗？**
可以。触发时明确说明"只检查 E·有效性"或"只看 C 维度"，评测会聚焦该维度打分并给出改进建议。深度 FAQ（第 7-15 题）见 [references/trace-faq-deep.md](references/trace-faq-deep.md)。

---

## 禁忌清单

| 行为 | 原因 |
|------|------|
| 无论据就调基分（纯为凑数） | 校准必须有语义信号支撑 |
| 无 evidence 就说"表现良好" | 每分必须有可引用证据 |
| CLI 和 Prompt 型用同一标准 | 必须应用类型感知 |
| FAQ 充数判满分 | 读内容判断实质价值 |
| 忽视去重信号 | `ref_names` 前缀 ≥3 必须降档 |

---

## TRACE 评测体系（原文）

> 以下内容来自腾讯科技、SkillHub 与腾讯玄武实验室于 2026 年 5 月 21 日联合发布的 TRACE 严选框架官方公告。

距离 Anthropic 推出 Agent Skills 不过半年，国内 Skill 社区 SkillHub 上的 Skill 数量已进入 7 万量级。5 月 21 日，腾讯科技、SkillHub 与腾讯玄武实验室联合发布 TRACE —— **国内首个面向 Skill 真实使用场景的严选评测体系**。

**T（Trust，安全可信）** — 红线维度。**R（Reliability，运行可靠）** — 稳定性、可复现性和交付可靠性。**A（Adaptability，场景适用）** — Agent 能否自然识别并加载目标 Skill。**C（Convention，结构规范）** — 不是判断写得是否漂亮，而是具备被理解运行评测复用和维护的基础。**E（Effectiveness，效果增益）** — 结果必须明显优于 no-skill 参照组，且改善值得付出代价。

TRACE 是质量观测坐标系，采用"热度信号 + 时间切片 + 系统评测 + 编辑精选"的严选机制，不追求全量评分排名。

---

## References

- [SkillHub TRACE Evaluation System](https://skillhub.cn/tutorials#trace-evaluation)
- [references/scoring-criteria.md](references/scoring-criteria.md) — 20 子项满分标准 + 扣分原因 + 修改对比 + 五维度速查（含原 trace-criteria-detail、trace-rubric 内容）
- [references/calibration-guide.md](references/calibration-guide.md) — 校准规则 + 反模式案例 + 调幅指南
- [references/trace-anti-patterns.md](references/trace-anti-patterns.md) — Skill 创作者自检反模式案例集（来源：skill-trace-checker/东四联周博远）
- [references/trace-skill-checklist.md](references/trace-skill-checklist.md) — 一页纸自检清单（scoring-criteria 浓缩版）（来源：skill-trace-checker/东四联周博远）
- [references/trace-sample-reports.md](references/trace-sample-reports.md) — 真实评分报告案例集（来源：skill-trace-checker/东四联周博远）
- [references/trace-faq-deep.md](references/trace-faq-deep.md) — TRACE 深度 FAQ（来源：skill-trace-checker/东四联周博远）
- [examples/trace-report.generated.md](examples/trace-report.generated.md) — 真实评测输出样例（Markdown）
- [examples/trace-report.generated.html](examples/trace-report.generated.html) — 真实评测输出样例（HTML 雷达图）

---

## Keywords

**English:** trace-evaluation, trace-scoring, trace-report, skill-quality, five-dimension-evaluation

**中文：** TRACE 评测, TRACE 评分, TRACE 报告, 五维度评估, T/R/A/C/E 评估, 技能质量评测, Trace 严选, 严格评测, 快速检查
