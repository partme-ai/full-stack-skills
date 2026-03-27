# Templates

Ready-to-copy Markdown templates for the PartMe/Octo documentation standard.

## Quick Start

1. Copy templates from the appropriate directory
2. Replace `{Name}` with the product name in **both filenames and content**
3. Replace `{V}` with the version identifier (e.g., `V1`) for version-level docs
4. Replace `{模块简称}` with the module short name for module-level docs
5. Fill in `{YYYY-MM-DD}` dates, `{姓名}` author names, and other placeholders
6. Follow the inline `{例如：...}` guidance to populate each section

## Template Directories

| Directory | Contents | Count | Description |
|:---|:---|:---:|:---|
| [`root/`](root/) | Root-level standard docs | 10 | 产品级规划文档，与版本无关 |
| [`version/`](version/) | Per-version standard docs | 7 | 版本级实施文档，每个版本目录一套 |
| [`module/`](module/) | Per-module PRD / Stitch / UI triplet | 3 | 可选，按功能模块细化 |
| [`delivery/`](delivery/) | Tech details + delivery phase docs | 5 | 可选，研发交付阶段 |

## Root Templates (10)

Root 文档为产品级基线，覆盖从品牌到功能的完整规划链：

| # | Template | Lines | Mermaid | Key Content |
|:---:|:---|:---:|:---:|:---|
| 1 | `1、命名与品牌说明.md` | ~120 | 1 | 品牌定位、命名规则、产品边界、品牌家族关系 |
| 2 | `2、术语表与词汇表.md` | ~150 | 0 | 产品/架构/业务/平台术语、缩略词、使用规则 |
| 3 | `3、市场与商业分析.md` | ~220 | 3 | 市场机会、TAM/SAM/SOM、竞品矩阵、SWOT、定价 |
| 4 | `4、技术与可行性分析.md` | ~230 | 3 | 分层可行性、安全合规、性能评估、风险总表、结论 |
| 5 | `5、技术方案与路线.md` | ~300 | 4 | 技术选型、分层方案、ADR、Gantt 路线、部署 |
| 6 | `6、产品与版本规划.md` | ~240 | 3 | 产品定位、版本矩阵、路线图、定价、发布策略 |
| 7 | `7、领域模型设计.md` | ~350 | 9 | 限界上下文、聚合 classDiagram、事件、仓储 |
| 8 | `8、系统架构设计.md` | ~400 | 8 | 分层架构、DDD/COLA、数据流、安全、部署 |
| 9 | `9、视觉与交互DNA规范.md` | ~280 | 1 | 设计原则、色彩、字体、布局、组件、动效、无障碍 |
| 10 | `10、功能菜单与版本规划.md` | ~450 | 5 | 功能全景 mindmap、菜单枚举、功能清单、优先级统计 |

## Version Templates (7)

版本文档为某一具体版本（如 V1）的实施级细化：

| # | Template | Description |
|:---:|:---|:---|
| 1 | `1、需求调研文档.md` | 用户调研、访谈、场景分析 |
| 2 | `2、需求分析文档.md` | 用户故事、功能规则、验收标准 |
| 3 | `3、系统架构设计.md` | 版本级架构细化、技术决策 |
| 4 | `4、功能与界面规划.md` | 模块划分、界面规划 |
| 5 | `5、PRD文档.md` | 版本级需求规格说明 |
| 6 | `6、功能菜单与版本规划.md` | 版本级菜单与功能规划 |
| 7 | `7、UI设计说明.md` | 页面结构、组件、动效、切图 |

## Module Templates (3)

模块文档为版本内某一功能模块的三件套：

| Template | Description |
|:---|:---|
| `模块-PRD.md` | 模块级产品需求文档，含功能规则、数据、交互 |
| `模块-Stitch设计提示词.md` | AI 设计生成提示词（英文） |
| `模块-UI设计说明.md` | 页面结构、组件使用、动效、适配、切图 |

## Delivery Templates (5)

交付文档为研发过程中的阶段性输出：

| # | Template | Description |
|:---:|:---|:---|
| 1 | `1、技术细分模板.md` | 技术栈、架构拆分、接口、数据库、工时、风险 |
| 2 | `2、功能提测模板.md` | 提测范围、环境、功能清单、部署步骤 |
| 3 | `3、测试结果模板.md` | 测试统计、问题汇总、发布建议 |
| 4 | `4、上线通知模板.md` | 上线范围、时间窗口、回滚计划 |
| 5 | `5、项目运维模板.md` | 部署架构、监控、故障处理、备份 |

## Authoring Guidelines

- **每份文档头部必须包含** H1 标题 + `>` blockquote 文档说明 + 版本号 + 日期
- **每份文档尾部必须包含** 文档版本 / 创建日期 / 最后更新 / 文档状态
- **章节编号严格递增**：`## 1.` → `## 2.` → ...；子节使用 `### N.M`
- **表格使用 `:---` 左对齐**
- **Mermaid 图前后保留空行**
- **中英混排加空格**：`OpenAI 模型` 而非 `OpenAI模型`
- **跨文档引用使用相对路径**：`[术语表](2、{Name}-术语表与词汇表.md)`

See [`SKILL.md`](../SKILL.md) for the complete scaffolding workflow and quality standards. See [`references/structure.md`](../references/structure.md) for detailed file mappings and cross-document dependencies.
