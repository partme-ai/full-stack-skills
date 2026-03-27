---
name: full-stack-doc
description: Enforces the PartMe/Octo-style product documentation layout—11 root standard docs, 7 per version folder, optional module triplets (PRD/Stitch/UI), plus 技术调研/其他/special dirs. Markdown templates live under templates/ as root/, version/, module/, delivery/ (merged legacy 1–14 + OctoPanel examples). Use when organizing partme-docs, Octo* projects, scaffolding doc trees, or aligning repo docs to this standard.
---

## 概述

本技能将 **产品文档目录与文件命名** 固化为可复用标准（与 `partme-docs` 下 Octo 系列实践一致）。**正文模板** 位于 [`templates/`](templates/) 下四个子目录 [`root/`](templates/root/)、[`version/`](templates/version/)、[`module/`](templates/module/)、[`delivery/`](templates/delivery/)（已合并原全生命周期 14 阶段模板与 OctoPanel 实例结构）；不再维护单独的 `legacy-lifecycle` 或 `project-standard` 嵌套目录。

**关键词**: 产品文档、版本目录、PRD、功能菜单、技术调研、其他目录、Octo、partme-docs

## 占位符

- `{Name}`：产品或项目英文名/品牌名（如 `OctoPanel`、`OctoClaw-4j`），用于文件名前缀。
- `{V}`：版本目录名（如 `V1`、`V2`、`V1.5`），用于版本级文件名后缀。

生成实际文件时：将 `{Name}`、`{V}` 替换为真实值；**根目录与「详细功能清单」允许两个文件同用序号 `6、`**（与现网约定一致）。

## 一、项目根目录：11 份标准文档

路径：`{项目根}/`

| 序号 | 文件名 |
|------|--------|
| 1 | `1、{Name}-命名与品牌说明.md` |
| 2 | `2、{Name}-术语表与词汇表.md` |
| 3 | `3、{Name}-市场与商业分析.md` |
| 4 | `4、{Name}-技术与可行性分析.md` |
| 5 | `5、{Name}-技术方案与路线.md` |
| 6 | `6、{Name}-产品与版本规划.md` |
| 6 | `6、{Name}-详细功能清单.md` |
| 7 | `7、{Name}-领域模型设计.md` |
| 8 | `8、{Name}-系统架构设计.md` |
| 9 | `9、{Name}-视觉与交互DNA规范.md` |
| 10 | `10、{Name}-功能菜单与版本规划.md` |

**骨架模板目录**: [`templates/root/`](templates/root/)（每个文件对应上表一项，正文内含 `{Name}` 占位）。

## 二、版本目录：7 份标准文档

路径：`{项目根}/{V}/`（如 `V1/`、`V2/`）

| 序号 | 文件名 |
|------|--------|
| 1 | `1、{Name}-需求调研文档-{V}.md` |
| 2 | `2、{Name}-需求分析文档-{V}.md` |
| 3 | `3、{Name}-系统架构设计-{V}.md` |
| 4 | `4、{Name}-功能与界面规划-{V}.md` |
| 5 | `5、{Name}-PRD文档-{V}.md` |
| 6 | `6、{Name}-功能菜单与版本规划-{V}.md` |
| 7 | `7、{Name}-UI设计说明-{V}.md` |

**骨架模板目录**: [`templates/version/`](templates/version/)

**注意**: 版本目录内若还有对象字典、错误码、研发拆解等非标准文档，**不得占用** 1–7 序号与上述文件名语义；应使用 `8、` 及以后序号，或放入 `其他/`。

## 三、功能模块：每个模块 3 份文档（可选）

路径示例：`{项目根}/{V}/{序号}、{模块中文名}/`

每个功能点模块建议具备：

- `{Name}-{模块简称}-PRD-{V}.md`
- `{Name}-{模块简称}-Stitch设计提示词.md`（或无 `-{V}`，按项目约定）
- `{Name}-{模块简称}-UI设计说明-{V}.md`

**示例**（OctoPanel V1 用户登录）：

- `OctoPanel-登录页-PRD-V1.md`
- `OctoPanel-登录页-Stitch设计提示词.md`
- `OctoPanel-登录页-UI设计说明-V1.md`

**骨架模板**: [`templates/module/`](templates/module/) 下三个文件；复制后按模块改名。

## 四、技术调研目录

路径：`{项目根}/技术调研/`

凡技术选型、方案对比、协议与第三方集成调研等 **非版本定稿叙述**，放此目录（可再分子目录）。

## 五、其他目录

路径：`{项目根}/其他/`

凡 **非版本特定**、**非技术调研**、且 **不属于** 根 11 份 / 版本 7 份 / 模块 3 份 的文档（任务单、门禁清单、对标报告、临时索引等），统一放 `其他/`。

**技术细分模板**（接口/库表级细节）：[`templates/delivery/1、技术细分模板.md`](templates/delivery/1、技术细分模板.md)；落地时建议放入项目 `其他/` 或研发仓库。

## 五之一、交付阶段模板（可选）

不占用根目录标准序号时，可使用 [`templates/delivery/`](templates/delivery/)：`1、技术细分`，以及 `2～5`（功能提测、测试结果、上线通知、项目运维）。

## 六、特殊目录（保持不动）

已按约定组织的目录 **不要强行迁入标准序号**，例如：`demo/`、`assets/`、`article/`、`article-cn/`、`archive/`、`.stitch/`、`stitch_*`、`实施指南/` 等——除非用户明确要求重构。

## 七、与旧版「14 模板」的关系

原 **14 阶段模板** 已 **合并进** [`templates/`](templates/) 下 `root/`、`version/`、`module/`、`delivery/`，与 OctoPanel 实例正文同一套目录即可扩写；**独立 `templates/legacy-lifecycle/` 与 `templates/project-standard/` 目录已移除**，避免重复维护。

## 八、相关技能

- `documentation-builder`：通用文档编写与格式（[`../dev-utils-skills/documentation-builder`](../dev-utils-skills/documentation-builder)）
- `api-doc-generator`：OpenAPI 等 API 文档（同组 `document-skills`）

## 九、校验清单（Agent 自检）

1. 项目根是否存在 11 份标准文件（含两个 `6、`）与 `10、` 功能菜单。
2. 每个活跃版本目录是否存在 7 份标准文件，且 UI 为 `7、`、功能菜单为 `6、`。
3. 技术调研与其它目录是否未混放根级标准文档。
4. 模块目录是否具备 PRD / Stitch / UI 三件套（若该项目约定模块级文档）。
