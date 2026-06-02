<div align="center">

# Stitch Skills

**Stitch UI 生成的 Agent Skills 集合**

![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-29-orange)
![Plugins](https://img.shields.io/badge/Plugins-3-brightgreen)

</div>

## 📖 简介

**Stitch Skills** 是一个 Agent Skills 集合，旨在通过 Stitch MCP 赋能 AI 智能体（如 Claude, Trae）自主设计和生成 UI 界面。它遵循 [Agent Skills 规范](https://agentskills.io/) 并提供了一套 "自循环" 的设计工作流。

**English:** [README.md](README.md)

## 🔗 官方资源 (Official Resources)

来自 Google Stitch 官方团队的核心文档：

*   **[概览 (Overview)](https://stitch.withgoogle.com/docs/learn/overview/)**: Stitch 能力介绍。
*   **[提示词指南 (Prompting)](https://stitch.withgoogle.com/docs/learn/prompting/)**: 编写高效设计提示词的最佳实践。
*   **[设备类型 (Device Types)](https://stitch.withgoogle.com/docs/learn/device-types/)**: 理解移动端、桌面端和 Web 布局。
*   **[设计模式 (Design Modes)](https://stitch.withgoogle.com/docs/learn/design-modes/)**: 标准模式 (Flash) 与 实验模式 (Pro) 的区别。
*   **[变体 (Variants)](https://stitch.withgoogle.com/docs/learn/variants/)**: 生成和管理设计变体。
*   **[控件 (Controls)](https://stitch.withgoogle.com/docs/learn/controls/)**: 使用交互式控件优化设计。
*   **[MCP 指南 (MCP Guide)](https://stitch.withgoogle.com/docs/mcp/guide/)**: Model Context Protocol 集成技术指南。

## 与官方 Stitch Skills 的对照与差异

本仓库 **包含并强化** [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)：每个官方 skill 都有 **能力不低于官方** 的本地等价物。

### 对照表：官方 vs 本仓库

| 官方 | 本仓库（本地） | 差异说明（为何本地更强） |
|----------|-------------------|--------------------------------------|
| **design-md** | **stitch-design-md** | DESIGN.md 包含 **Section 6**（Design System Notes for Stitch Generation）；官方仅 1–5 节。显式使用 stitch-mcp-* 命名；与 stitch-ui-prompt-architect、stitch-loop 集成；引用框架设计规范。 |
| **enhance-prompt** | **stitch-ui-prompt-architect** | 双路径：(1) 模糊 → 增强提示（与官方一致）；(2) Design Spec + 请求 → 分段 Stitch 提示。另含框架契约前缀（uView、Element、Layui、Bootstrap、Vant）、KEYWORDS.md、以及 stitch-loop 的 next-prompt.md。 |
| **stitch-loop** | **stitch-loop** | 相同 baton/SITE.md；**Step 4.5** 可选 Chrome DevTools MCP 视觉校验；**编排方式**（CI/CD、人工介入、Agent 链、手动）；显式 stitch-mcp-* 命名；DESIGN.md Section 6；通过 stitch-ui-prompt-architect 提升提示质量。 |
| **react-components** | **stitch-react-components** | 相同拉取 + fetch 脚本 + 架构清单 + 组件模板；引用 stitch-mcp-* 做项目/屏幕发现；可选 DESIGN.md 对齐（stitch-design-md）。 |
| **remotion** | **stitch-remotion** | 相同走查流程；**常用模式**（幻灯片、功能高亮、用户流）；**旁白**与**动态文案提取**；**Remotion Skills** 与 **Remotion MCP** 链接；stitch-mcp-* 命名；DESIGN.md 用于叠加文案。 |
| **shadcn-ui** | **stitch-shadcn-ui** | 相同发现、安装、定制、blocks；**init 样式**（Vega、Nova、Maia、Lyra、Mira）；**自定义 registry**（get_project_registries、list_items_in_registries）；**校验与质量**清单；与 stitch-react-components、DESIGN.md 集成。 |

### 本仓库在官方基础上的新增

- **stitch-mcp-***：每个 MCP 工具对应一个 skill；技能名 = MCP 工具名下划线改为连字符（如 generate_screen_from_text → stitch-mcp-generate-screen-from-text）。完整映射：[docs/mcp-naming-convention.md](docs/mcp-naming-convention.md)。
- **stitch-ui-design-spec-***：面向 Stitch 提示的框架设计契约（Bootstrap、Element Plus、Layui、uView、uView Pro、Vant）。
- **stitch-ui-designer**：端到端设计任务的主编排技能。
- **stitch-ui-design-spec-generator**：从模糊需求生成结构化规范（主题、设备、风格）。
- **stitch-skill-creator**：新场景技能的工厂。
- **stitch-ued-guide**：UED 指南与视觉词汇。
- **Stitch → 框架组件**：七个转换技能（Vue 3 + Element/Bootstrap/Layui/Vant，uni-app + uView/uView Pro/uview-plus），将 Stitch 屏幕转为可运行项目。
- **agents/stitch-ui-designer.md**：Stitch UI 工作流专用 agent。

### 何时用哪个

- **所有 Stitch 流程**：优先使用本仓库的 skills（stitch-*）。它们互相引用且共用同一 MCP；本地 prompt-architect 在双路径与框架契约上强于官方 enhance-prompt。
- **仅作参考**：需要额外示例或脚本时（如 react-components validate.js、remotion 模板），可查阅官方 [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)。

完整说明：[docs/related-upstream.md](docs/related-upstream.md)。

## 🔌 MCP 配置（想要真实执行必须做）

本仓库包含的是 **skills 与 tool schema**，并不包含 Stitch MCP Server 本体。

要让 Agent 真正创建项目/生成页面，你需要：

*   按官方文档安装与配置 Stitch MCP Server：https://stitch.withgoogle.com/docs/mcp/guide/
*   确认客户端暴露出 Stitch MCP 工具（本仓库 `docs/*.json` 定义的 tool 名称）：
    *   `create_project`
    *   `list_projects`
    *   `get_project`
    *   `generate_screen_from_text`
    *   `list_screens`
    *   `get_screen`
*   技能名遵循 MCP 工具名：stitch-mcp-<tool>（如 get_screen → stitch-mcp-get-screen）。完整映射：[docs/mcp-naming-convention.md](docs/mcp-naming-convention.md)。

在部分客户端中，MCP 工具名可能带命名空间前缀，例如：

*   `mcp__<serverName>__create_project`
*   `mcp__<serverName>__generate_screen_from_text`

其中 `<serverName>` 必须与你 `mcpServers` 的配置名称一致。

## 🏗️ 架构

技能被组织成逻辑层，以实现自主的 "设计 -> 执行" 循环。

- **`stitch-ui-*`**: **大脑 (The Brain)**。负责设计逻辑、提示词工程和编排的技能。不产生外部 API 费用。
- **`stitch-mcp-*`**: **双手 (The Hands)**。Stitch MCP (Model Context Protocol) 的封装。负责执行实际的 API 调用。

```text
stitch-skills/
├── skills/
│   ├── stitch-ui-designer/          # [编排器] 主技能
│   ├── stitch-ui-design-spec-generator/ # [逻辑] 风格与规范逻辑
│   ├── stitch-ui-prompt-architect/      # [逻辑] 提示词工程
│   ├── stitch-mcp-create-project/   # [执行] 创建项目
│   ├── stitch-mcp-generate-screen-from-text/  # [执行] 生成 UI
│   ├── stitch-skill-creator/        # [元工具] 创建新技能
│   └── ...
├── docs/                            # API 规范
├── media/                           # 资源
├── LICENSE                          # Apache 2.0
└── README.md                        # 文档
```

## 📦 可用技能

### 编排器 (入口)
*   **`stitch-ui-designer`**: **主技能**。调用它来处理端到端的设计任务（例如 "设计一个登录页面"）。它会自动协调逻辑和执行技能。

### 逻辑与设计技能 (大脑)
*   **`stitch-ui-design-spec-generator`**: 分析模糊的用户请求，输出结构化的设计规范（主题、设备、风格）。
*   **`stitch-ui-prompt-architect`**: **双路径**：(1) 模糊 UI 想法 → 增强 Stitch 提示（关键词、DESIGN.md、结构）；(2) Design Spec + 请求 → 分段 [Context]/[Layout]/[Components] 提示。支持框架契约前缀（uView、Element、Layui 等）及 stitch-loop 的 next-prompt。
*   **`stitch-ui-design-variants`**: 为给定的屏幕概念生成设计变体（A/B 测试想法）。
*   **`stitch-design-md`**: 分析 Stitch 项目并综合为 DESIGN.md 语义设计系统；使用 stitch-mcp-* 拉取；与 stitch-loop、stitch-ui-prompt-architect 集成。

### 执行技能 (双手 - MCP)
*   **`stitch-mcp-create-project`**: 创建新的 Stitch 项目。
*   **`stitch-mcp-list-projects`**: 列出现有项目。
*   **`stitch-mcp-get-project`**: 获取项目详情。
*   **`stitch-mcp-generate-screen-from-text`**: **核心** 文本到 UI 生成。
*   **`stitch-mcp-list-screens`**: 列出生成的屏幕。
*   **`stitch-mcp-get-screen`**: 导出屏幕代码/资产。

### 原子工具
*   **`stitch-skill-creator`**: 一个用于生成新 **场景技能**（如 `stitch-ui-music-designer`）的原子工具。基于 "黄金模板" 生成，强制符合 SOP 规范。

### 设计规格工具 (约束)
*   **`stitch-ui-design-spec-uview`**: uView 2.0（uni-app / Vue2）设计规格工具：可输出 Hard constraints 前缀，或输出选择器 JSON + 拼装后的 Stitch Prompt（按需注入组件/状态约束）。
*   **`stitch-ui-design-spec-uviewpro`**: uView Pro（uni-app / Vue3）设计规格工具：支持输出硬约束前缀或组件选择器 JSON。
*   **`stitch-ui-design-spec-layui`**: Layui-Vue（Vue 3.0）设计规格工具：支持输出硬约束前缀或组件选择器 JSON。
*   **`stitch-ui-design-spec-bootstrap`**: Bootstrap 5（Vue）设计规格工具：响应式设计，支持输出硬约束前缀或组件选择器 JSON。
*   **`stitch-ui-design-spec-element-plus`**: Element Plus（Vue 3）设计规格工具：桌面端组件库，支持输出硬约束前缀或组件选择器 JSON。
*   **`stitch-ui-design-spec-vant`**: Vant 4（Mobile Vue）设计规格工具：移动端电商风格，支持输出硬约束前缀或组件选择器 JSON。

### 循环、React、视频与 UI 集成
*   **`stitch-loop`**: 多页站点迭代构建：baton（next-prompt.md）、Stitch MCP 生成/获取、集成到站点、更新 SITE.md 与下一 baton。与 stitch-design-md 配合使用。
*   **`stitch-react-components`**: 将 Stitch 屏幕转为模块化 React（Vite/TS），含校验与设计 token 一致性；高可靠 fetch 脚本。
*   **`stitch-remotion`**: 用 Remotion 从 Stitch 项目生成走查视频（转场、叠加）；使用 stitch-mcp-* 获取屏幕。
*   **`stitch-shadcn-ui`**: shadcn/ui 的发现、安装、定制、blocks 专家指引；与 stitch-react-components 配合使用。

### Stitch → 框架组件（Vue / uni-app）
*   **`stitch-vue-element-components`**: 将 Stitch 屏幕转为 Vue 3 + Element Plus（Vite、.vue SFC）；契约与 fetch 脚本。
*   **`stitch-vue-bootstrap-components`**: 将 Stitch 屏幕转为 Vue 3 + BootstrapVue/BootstrapVueNext（Vite、.vue SFC）。
*   **`stitch-vue-layui-components`**: 将 Stitch 屏幕转为 Vue 3 + Layui-Vue（Vite、.vue SFC）。
*   **`stitch-vue-vant-components`**: 将 Stitch 屏幕转为 Vue 3 + Vant 4（Vite、.vue SFC、移动优先）。
*   **`stitch-uview-components`**: 将 Stitch 屏幕转为 uni-app + Vue 2 + uView 2.0（pages/、u-* 组件）。
*   **`stitch-uviewpro-components`**: 将 Stitch 屏幕转为 uni-app + Vue 3 + uView Pro（pages/、u-* 组件、rpx）。
*   **`stitch-uview-plus-components`**: 将 Stitch 屏幕转为 uni-app + Vue 3 + `uview-plus`（pages/、`up-*` 组件、主题变量、安全区页壳，以及更强的 popup/upload/tabbar 约束）。

### 知识技能
*   **`stitch-ued-guide`**: 被其他技能引用的设计指南、视觉词汇和提示词策略。

## ⚡ 快速开始

### 支持的 Agent

本项目的 Skills 符合 Agent Skills 规范，支持以下环境：

- Claude Code
- Trae（本仓库在 Trae 环境下已通过 MCP 验收）
- Cursor
- Windsurf / Continue / Roo Code / CodeBuddy 等

### 在 Claude Code 中使用（仅 Claude Code 适用）

如果你在 Trae 中使用本仓库，可以跳过本节的 `/plugin ...` 命令。

#### 1) 注册 Marketplace

```bash
/plugin marketplace add https://github.com/partme-ai/stitch-skills.git
```

或者简写（如果已发布到官方源）：

```bash
/plugin marketplace add partme-ai/stitch-skills
```

删除 Marketplace：

```bash
/plugin marketplace remove stitch-skills
```

### 在 Trae 中使用（推荐）

#### 0) 安装 Skills（Trae 的加载方式）

Trae 不使用 Claude Code 的 `/plugin ...` 命令。Trae 会从以下位置加载 skills：

*   项目级：当前项目根目录的 `.trae/skills/`
*   全局：用户目录下的 `~/.trae/skills/`（或 `~/.trae-cn/skills/`）

你只需要把本仓库的 `stitch-skills/skills/*` 放到上述任一位置即可（项目级优先，便于按项目隔离）。

#### 1) 配置 Stitch MCP Server（必须）

Trae 的 MCP 配置文件路径：

- Trae：`~/Library/Application Support/Trae/User/mcp.json`
- Trae CN：`~/Library/Application Support/Trae CN/User/mcp.json`

在 `mcpServers` 中添加（或修正）：

```json
{
  "mcpServers": {
    "stitch": {
      "url": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

注意事项：

- `url` 必须是纯字符串，不能包含反引号、前后空格
- 浏览器直接打开该 URL 出现 405 属于正常现象（该端点不支持 GET）
- 不要把真实 API Key 提交到仓库或粘贴到公开聊天中
- 修改 `mcp.json` 后需要重启 Trae 才能生效

#### 2) 使用技能

只需要在对话中显式提到 “Stitch”，并描述你的目标即可，例如：

- “用 Stitch 列出我的项目”
- “使用 Stitch 实现 登录_PRD.md 文档中的设计”
- “使用 Stitch 和 uView 风格 实现 登录_PRD.md 文档要求的设计工作”
- “使用 Stitch 和 Layui 风格设计一个后台管理系统的仪表盘”
- “使用 Stitch 和 Bootstrap 风格设计一个响应式的登录页”
- “使用 Stitch 和 Element Plus 风格设计一个企业级后台管理系统”
- “使用 Stitch 和 uView Pro 风格设计一个电商首页”
- “使用 Stitch 和 uview-plus 风格设计一个移动电商首页”

### 端到端示例：使用 Stitch 实现 登录_PRD.md

示例输入：

> 使用 Stitch 实现 `docs/登录_PRD.md` 文档要求的设计工作（登录页 + 注册页）

预期行为（Agent 会自动编排并调用 MCP 工具）：

1. `create_project`：创建项目（返回 `projects/{id}`）
2. `generate_screen_from_text`：生成登录页
3. `generate_screen_from_text`：生成注册页
4. `list_screens`：列出项目内 screens
5. `get_screen`：获取截图与 HTML（导出用）

你可以在生成后继续说：

- “用 Stitch 导出登录页 HTML”
- “用 Stitch 把注册页改成 3 步分步向导”

更多可直接照抄的示例见：

- `skills/stitch-ui-designer/examples/partme_login_prd.md`

## 🔒 安全与触发

所有执行技能 (`stitch-mcp-*`) 和主编排器 (`stitch-ui-designer`) 都受 **关键先决条件 (Critical Prerequisite)** 保护：只有当用户 **显式提及 "Stitch"** 时，它们才会触发。这防止了在正常对话中意外调用昂贵的 API。

## 添加新技能

新技能应遵循本仓库的 [架构](#-架构) 与 [Agent Skills 规范](https://agentskills.io/specification)。

### 适合的新技能方向

- **校验**：将 Stitch HTML 转为其他 UI 框架并校验语法的技能。
- **数据解耦**：将静态设计内容移到外部 mock 数据文件的技能。
- **生成设计**：从给定数据集或规范生成新 Stitch 屏幕的技能。
- **框架规格**：更多 UI 框架的 `stitch-ui-design-spec-*` 技能（如 Ant Design、Naive UI）。

使用 **stitch-skill-creator** 创建场景技能；MCP 封装请沿用现有 `stitch-mcp-*` 命名与「一工具一技能」模式。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📚 相关文档

| 文档 | 说明 |
|------|------|
| [docs/related-upstream.zh-CN.md](docs/related-upstream.zh-CN.md) | 官方与本地技能对照及如何保持领先。English: [related-upstream.md](docs/related-upstream.md). |
| [docs/mcp-naming-convention.zh-CN.md](docs/mcp-naming-convention.zh-CN.md) | MCP 工具名 → 技能名（如 get_screen → stitch-mcp-get-screen）。English: [mcp-naming-convention.md](docs/mcp-naming-convention.md). |
| [docs/skills-compare-design-spec-and-react.zh-CN.md](docs/skills-compare-design-spec-and-react.zh-CN.md) | Design Spec 系与组件转换技能对比（角色、输入、输出）。English: [skills-compare-design-spec-and-react.md](docs/skills-compare-design-spec-and-react.md). |
| [AGENTS.md](AGENTS.md) | 面向 AI 编码智能体的 Agent 指引与技能结构。 |
| [spec/agent-skills-spec.md](spec/agent-skills-spec.md) | 本仓库采用的 Agent Skills 规范。 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 如何新增/更新技能与提交 PR。 |
| [docs/xx.md](docs/xx.md) | 将现有前端体系变为 Stitch 约束的推荐路径（进阶）。 |
| [SELF_ARGUMENTATION.md](SELF_ARGUMENTATION.md) | 项目自我论证（目标、架构、扩展性）。 |
| [docs/README.md](docs/README.md) | docs/ 目录下文档索引。 |

## 📄 许可证

Apache 2.0
