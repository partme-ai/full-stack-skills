# Document Structure Reference

Detailed file listings and naming conventions for the PartMe/Octo documentation standard. This file is loaded on-demand when agents need exact filenames or mapping details.

## Contents

- [Root directory: 11 standard docs](#root-directory-11-standard-docs)
- [Version directory: 7 standard docs](#version-directory-7-standard-docs)
- [Module directory: 3 docs per module](#module-directory-3-docs-per-module)
- [Delivery templates: 5 optional docs](#delivery-templates-5-optional-docs)
- [Special directories](#special-directories)
- [Legacy template mapping](#legacy-template-mapping)

## Root directory: 11 standard docs

Path: `{项目根}/`

| # | Filename | Template |
|---|----------|----------|
| 1 | `1、{Name}-命名与品牌说明.md` | [`templates/root/1、命名与品牌说明.md`](../templates/root/1、命名与品牌说明.md) |
| 2 | `2、{Name}-术语表与词汇表.md` | [`templates/root/2、术语表与词汇表.md`](../templates/root/2、术语表与词汇表.md) |
| 3 | `3、{Name}-市场与商业分析.md` | [`templates/root/3、市场与商业分析.md`](../templates/root/3、市场与商业分析.md) |
| 4 | `4、{Name}-技术与可行性分析.md` | [`templates/root/4、技术与可行性分析.md`](../templates/root/4、技术与可行性分析.md) |
| 5 | `5、{Name}-技术方案与路线.md` | [`templates/root/5、技术方案与路线.md`](../templates/root/5、技术方案与路线.md) |
| 6 | `6、{Name}-产品与版本规划.md` | [`templates/root/6、产品与版本规划.md`](../templates/root/6、产品与版本规划.md) |
| 6 | `6、{Name}-详细功能清单.md` | [`templates/root/6、详细功能清单.md`](../templates/root/6、详细功能清单.md) |
| 7 | `7、{Name}-领域模型设计.md` | [`templates/root/7、领域模型设计.md`](../templates/root/7、领域模型设计.md) |
| 8 | `8、{Name}-系统架构设计.md` | [`templates/root/8、系统架构设计.md`](../templates/root/8、系统架构设计.md) |
| 9 | `9、{Name}-视觉与交互DNA规范.md` | [`templates/root/9、视觉与交互DNA规范.md`](../templates/root/9、视觉与交互DNA规范.md) |
| 10 | `10、{Name}-功能菜单与版本规划.md` | [`templates/root/10、功能菜单与版本规划.md`](../templates/root/10、功能菜单与版本规划.md) |

Two files share sequence number `6、` — this is intentional and matches the production convention.

## Version directory: 7 standard docs

Path: `{项目根}/{V}/` (e.g., `V1/`, `V2/`)

| # | Filename | Template |
|---|----------|----------|
| 1 | `1、{Name}-需求调研文档-{V}.md` | [`templates/version/1、需求调研文档.md`](../templates/version/1、需求调研文档.md) |
| 2 | `2、{Name}-需求分析文档-{V}.md` | [`templates/version/2、需求分析文档.md`](../templates/version/2、需求分析文档.md) |
| 3 | `3、{Name}-系统架构设计-{V}.md` | [`templates/version/3、系统架构设计.md`](../templates/version/3、系统架构设计.md) |
| 4 | `4、{Name}-功能与界面规划-{V}.md` | [`templates/version/4、功能与界面规划.md`](../templates/version/4、功能与界面规划.md) |
| 5 | `5、{Name}-PRD文档-{V}.md` | [`templates/version/5、PRD文档.md`](../templates/version/5、PRD文档.md) |
| 6 | `6、{Name}-功能菜单与版本规划-{V}.md` | [`templates/version/6、功能菜单与版本规划.md`](../templates/version/6、功能菜单与版本规划.md) |
| 7 | `7、{Name}-UI设计说明-{V}.md` | [`templates/version/7、UI设计说明.md`](../templates/version/7、UI设计说明.md) |

Sequence numbers 1–7 are **reserved**. Non-standard docs in version folders must use `8+` or be placed in `其他/`.

## Module directory: 3 docs per module

Path: `{项目根}/{V}/{序号}、{模块中文名}/`

| File | Template |
|------|----------|
| `{Name}-{模块简称}-PRD-{V}.md` | [`templates/module/模块-PRD.md`](../templates/module/模块-PRD.md) |
| `{Name}-{模块简称}-Stitch设计提示词.md` | [`templates/module/模块-Stitch设计提示词.md`](../templates/module/模块-Stitch设计提示词.md) |
| `{Name}-{模块简称}-UI设计说明-{V}.md` | [`templates/module/模块-UI设计说明.md`](../templates/module/模块-UI设计说明.md) |

The Stitch file may omit the `-{V}` suffix per project convention.

## Delivery templates: 5 optional docs

Located in [`templates/delivery/`](../templates/delivery/). These do **not** occupy root-level sequence numbers. Place deliverables in `其他/` or a dedicated delivery folder.

| # | File | Original legacy # |
|---|------|--------------------|
| 1 | `1、技术细分模板.md` | Legacy #10 |
| 2 | `2、功能提测模板.md` | Legacy #11 |
| 3 | `3、测试结果模板.md` | Legacy #12 |
| 4 | `4、上线通知模板.md` | Legacy #13 |
| 5 | `5、项目运维模板.md` | Legacy #14 |

## Special directories

These directories follow their own conventions — do **not** reorganize unless the user explicitly requests it:

| Directory | Purpose |
|-----------|---------|
| `技术调研/` | Tech research, feasibility studies, protocol analysis (non-version-specific) |
| `其他/` | Non-standard docs: task lists, gate checklists, benchmarks, temporary indexes |
| `demo/`, `assets/`, `article/`, `article-cn/` | Project-specific content directories |
| `archive/`, `.stitch/`, `stitch_*`, `实施指南/` | Tool-specific or historical directories |

## Legacy template mapping

The original 14-phase lifecycle templates have been merged into the current structure:

| Legacy # | Legacy name | Current location |
|----------|-------------|------------------|
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
