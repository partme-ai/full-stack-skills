# Document Structure Reference

Detailed file listings, naming conventions, cross-reference rules, and quality metrics for the PartMe/Octo documentation standard. This file is loaded on-demand when agents need exact filenames, mapping details, or validation rules.

## Contents

- [Root directory: 10 standard docs](#root-directory-10-standard-docs)
- [Version directory: 7 standard docs](#version-directory-7-standard-docs)
- [Module directory: 3 docs per module](#module-directory-3-docs-per-module)
- [Delivery templates: 5 optional docs](#delivery-templates-5-optional-docs)
- [Special directories](#special-directories)
- [Cross-document dependency map](#cross-document-dependency-map)
- [Mermaid diagram type guide](#mermaid-diagram-type-guide)
- [Quality metrics by document](#quality-metrics-by-document)
- [Legacy template mapping](#legacy-template-mapping)

---

## Root directory: 10 standard docs

Path: `{项目根}/`

| # | Filename | Template | Primary Concern |
|:---:|:---|:---|:---|
| 1 | `1、{Name}-命名与品牌说明.md` | [`templates/root/1、命名与品牌说明.md`](../templates/root/1、命名与品牌说明.md) | 品牌口径、命名、边界 |
| 2 | `2、{Name}-术语表与词汇表.md` | [`templates/root/2、术语表与词汇表.md`](../templates/root/2、术语表与词汇表.md) | 统一语言、中英对照 |
| 3 | `3、{Name}-市场与商业分析.md` | [`templates/root/3、市场与商业分析.md`](../templates/root/3、市场与商业分析.md) | 市场规模、竞品、商业模式 |
| 4 | `4、{Name}-技术与可行性分析.md` | [`templates/root/4、技术与可行性分析.md`](../templates/root/4、技术与可行性分析.md) | 技术评估、风险、POC |
| 5 | `5、{Name}-技术方案与路线.md` | [`templates/root/5、技术方案与路线.md`](../templates/root/5、技术方案与路线.md) | 技术选型、ADR、里程碑 |
| 6 | `6、{Name}-产品与版本规划.md` | [`templates/root/6、产品与版本规划.md`](../templates/root/6、产品与版本规划.md) | 版本矩阵、定价、发布 |
| 7 | `7、{Name}-领域模型设计.md` | [`templates/root/7、领域模型设计.md`](../templates/root/7、领域模型设计.md) | DDD 限界上下文、聚合 |
| 8 | `8、{Name}-系统架构设计.md` | [`templates/root/8、系统架构设计.md`](../templates/root/8、系统架构设计.md) | 分层架构、部署、安全 |
| 9 | `9、{Name}-视觉与交互DNA规范.md` | [`templates/root/9、视觉与交互DNA规范.md`](../templates/root/9、视觉与交互DNA规范.md) | 色彩、字体、组件、动效 |
| 10 | `10、{Name}-功能菜单与版本规划.md` | [`templates/root/10、功能菜单与版本规划.md`](../templates/root/10、功能菜单与版本规划.md) | 导航、功能清单、优先级 |

`10、{Name}-功能菜单与版本规划.md` includes the full detailed feature list section. The old standalone `6、{Name}-详细功能清单.md` has been merged.

---

## Version directory: 7 standard docs

Path: `{项目根}/{V}/` (e.g., `V1/`, `V2/`)

| # | Filename | Template | Primary Concern |
|:---:|:---|:---|:---|
| 1 | `1、{Name}-需求调研文档-{V}.md` | [`templates/version/1、需求调研文档.md`](../templates/version/1、需求调研文档.md) | 用户调研、场景分析 |
| 2 | `2、{Name}-需求分析文档-{V}.md` | [`templates/version/2、需求分析文档.md`](../templates/version/2、需求分析文档.md) | 用户故事、功能规则 |
| 3 | `3、{Name}-系统架构设计-{V}.md` | [`templates/version/3、系统架构设计.md`](../templates/version/3、系统架构设计.md) | 版本级架构细化 |
| 4 | `4、{Name}-功能与界面规划-{V}.md` | [`templates/version/4、功能与界面规划.md`](../templates/version/4、功能与界面规划.md) | 模块划分、界面规划 |
| 5 | `5、{Name}-PRD文档-{V}.md` | [`templates/version/5、PRD文档.md`](../templates/version/5、PRD文档.md) | 需求规格说明 |
| 6 | `6、{Name}-功能菜单与版本规划-{V}.md` | [`templates/version/6、功能菜单与版本规划.md`](../templates/version/6、功能菜单与版本规划.md) | 版本级菜单与功能 |
| 7 | `7、{Name}-UI设计说明-{V}.md` | [`templates/version/7、UI设计说明.md`](../templates/version/7、UI设计说明.md) | 页面、组件、动效说明 |

Sequence numbers 1–7 are **reserved**. Non-standard docs in version folders must use `8+` or be placed in `其他/`.

---

## Module directory: 3 docs per module

Path: `{项目根}/{V}/{序号}、{模块中文名}/`

| File | Template | Purpose |
|:---|:---|:---|
| `{Name}-{模块简称}-PRD-{V}.md` | [`templates/module/模块-PRD.md`](../templates/module/模块-PRD.md) | 模块级产品需求文档 |
| `{Name}-{模块简称}-Stitch设计提示词.md` | [`templates/module/模块-Stitch设计提示词.md`](../templates/module/模块-Stitch设计提示词.md) | AI 设计生成提示词 |
| `{Name}-{模块简称}-UI设计说明-{V}.md` | [`templates/module/模块-UI设计说明.md`](../templates/module/模块-UI设计说明.md) | UI 页面说明与切图规范 |

The Stitch file may omit the `-{V}` suffix per project convention.

---

## Delivery templates: 5 optional docs

Located in [`templates/delivery/`](../templates/delivery/). These do **not** occupy root-level sequence numbers. Place deliverables in `其他/` or a dedicated delivery folder.

| # | File | Original Legacy # | Purpose |
|:---:|:---|:---:|:---|
| 1 | `1、技术细分模板.md` | Legacy #10 | 技术栈、架构、工时、风险 |
| 2 | `2、功能提测模板.md` | Legacy #11 | 提测范围、环境、部署 |
| 3 | `3、测试结果模板.md` | Legacy #12 | 测试统计、问题、发布建议 |
| 4 | `4、上线通知模板.md` | Legacy #13 | 上线范围、时间、回滚计划 |
| 5 | `5、项目运维模板.md` | Legacy #14 | 部署、监控、故障、备份 |

---

## Special directories

These directories follow their own conventions — do **not** reorganize unless the user explicitly requests it:

| Directory | Purpose | Notes |
|:---|:---|:---|
| `技术调研/` | Tech research, feasibility studies, protocol analysis | 版本无关，可包含独立调研报告 |
| `其他/` | Non-standard docs: task lists, gate checklists, benchmarks | 交付模板通常放在这里 |
| `demo/`, `assets/`, `article/`, `article-cn/` | Project-specific content | 项目特有的示例、图片、文章 |
| `archive/`, `.stitch/`, `stitch_*`, `实施指南/` | Tool-specific or historical | 不主动修改 |

---

## Cross-document dependency map

文档间的引用关系（→ 表示「应引用」）：

| Source | Must Reference | Reason |
|:---|:---|:---|
| Doc 2 术语表 | Doc 1 品牌 | 术语源于品牌定位 |
| Doc 3 市场分析 | Doc 1 品牌, Doc 5 技术 | 市场机会需产品边界和技术约束 |
| Doc 4 可行性 | Doc 3 市场, Doc 5 技术 | 评估技术是否匹配市场机会 |
| Doc 5 技术方案 | Doc 4 可行性 | 方案基于可行性结论 |
| Doc 6 版本规划 | Doc 3 商业, Doc 5 路线 | 版本节奏对齐商业与技术 |
| Doc 7 领域模型 | Doc 2 术语, Doc 6 功能边界 | 聚合名称须在术语表中定义 |
| Doc 8 系统架构 | Doc 5 技术栈, Doc 7 领域 | 架构承接技术选型与领域划分 |
| Doc 9 视觉DNA | Doc 1 品牌气质 | 视觉语言源于品牌 |
| Doc 10 功能菜单 | Doc 6, Doc 8, Doc 9 | 功能列表对齐版本、架构、UI |

**关键一致性约束**：

1. **时间线一致**：Doc 5 Gantt、Doc 6 版本路线图、Doc 10 发布节奏的日期必须对齐
2. **术语一致**：Doc 7 聚合/实体名 → Doc 2 必须有定义 → Doc 8 组件名应匹配
3. **版本一致**：Doc 6 版本功能矩阵 → Doc 10 功能列表的版本标注必须相同
4. **技术栈一致**：Doc 5 技术选型 → Doc 8 分层架构 → Doc 4 可行性评估三者对应

---

## Mermaid diagram type guide

每类文档推荐使用的 Mermaid 图表类型：

| Document | Recommended Types | Example Usage |
|:---|:---|:---|
| 1、命名与品牌 | `graph LR` | 品牌家族关系图 |
| 2、术语表 | (无) | 纯表格驱动 |
| 3、市场分析 | `quadrantChart`, `funnel`, `flowchart` | 竞品象限、转化漏斗、价值链 |
| 4、可行性分析 | `flowchart TD`, `sequenceDiagram` | 技术验证流程、集成序列 |
| 5、技术方案 | `flowchart`, `gantt`, `erDiagram` | 架构拓扑、技术路线、RBAC ER 图 |
| 6、版本规划 | `graph`, `timeline`, `flowchart` | 产品边界、版本时间线、升级漏斗 |
| 7、领域模型 | `graph TB`, `classDiagram`, `sequenceDiagram` | 限界上下文、聚合类图、事件流 |
| 8、系统架构 | `flowchart`, `sequenceDiagram`, `stateDiagram-v2` | 分层架构、数据流、状态机 |
| 9、视觉DNA | `flowchart TD` | 页面骨架流、组件层级 |
| 10、功能菜单 | `mindmap`, `flowchart`, `pie` | 功能全景、导航结构、优先级分布 |

---

## Quality metrics by document

Based on OctoEcom and OpenEcom production examples:

| Doc | Target Lines | Min Mermaid | Min Tables | Must-Have Sections |
|:---:|:---:|:---:|:---:|:---|
| 1 | 100–120 | 1 | 2 | 品牌定位、命名由来、产品边界、核心公式、品牌关系 |
| 2 | 100–160 | 0 | 8 | 文档信息、产品/架构/业务术语、缩略词、使用规则 |
| 3 | 160–220 | 1 | 10 | 市场机会、TAM/SAM/SOM、竞品矩阵、SWOT、商业模式 |
| 4 | 180–230 | 2 | 10 | 分层评估（每层一节）、安全合规、风险总表、结论 |
| 5 | 260–400 | 3 | 9 | 技术选型、分层方案、ADR、Gantt 路线、部署方案 |
| 6 | 200–340 | 2 | 5 | 产品定位、版本矩阵、路线图、定价、发布策略 |
| 7 | 300–410 | 7 | 7 | 限界上下文、聚合 classDiagram、事件表、仓储接口 |
| 8 | 400–510 | 7 | 9 | 分层架构、DDD 映射、数据流、安全、部署架构 |
| 9 | 250–300 | 0–1 | 12 | 设计原则、色彩、字体、布局、组件、动效、暗色、无障碍 |
| 10 | 400–560 | 3 | 20 | 全景 mindmap、菜单枚举、功能清单、优先级统计 |

---

## Legacy template mapping

The original 14-phase lifecycle templates have been merged into the current structure:

| Legacy # | Legacy Name | Current Location |
|:---:|:---|:---|
| 1 | 市场分析模板 | → `root/3、市场与商业分析.md` |
| 2 | 需求调研模板 | → `version/1、需求调研文档.md` |
| 3 | 技术调研模板 | → `root/4、技术与可行性分析.md` + `root/5、技术方案与路线.md` |
| 4 | 交互原型模板 | → `version/4、功能与界面规划.md` |
| 5 | PRD 文档模板 | → `version/5、PRD文档.md` + `module/模块-PRD.md` |
| 6 | 视觉规范模板 | → `root/9、视觉与交互DNA规范.md` |
| 7 | UI 设计说明模板 | → `version/7、UI设计说明.md` + `module/模块-UI设计说明.md` |
| 8 | 领域模型说明模板 | → `root/7、领域模型设计.md` |
| 9 | 系统架构模板 | → `root/8、系统架构设计.md` + `version/3、系统架构设计.md` |
| 10 | 技术细分模板 | → `delivery/1、技术细分模板.md` |
| 11 | 功能提测模板 | → `delivery/2、功能提测模板.md` |
| 12 | 测试结果模板 | → `delivery/3、测试结果模板.md` |
| 13 | 上线通知模板 | → `delivery/4、上线通知模板.md` |
| 14 | 项目运维模板 | → `delivery/5、项目运维模板.md` |

The `templates/legacy-lifecycle/` and `templates/project-standard/` directories have been removed; all content lives in `templates/root/`, `templates/version/`, `templates/module/`, and `templates/delivery/`.
