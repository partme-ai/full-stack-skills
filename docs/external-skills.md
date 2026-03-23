# 外部技能库索引（全栈开发）

本文档列出与 **full-stack-skills** 互补的第三方 Agent Skills 仓库：可直接安装使用的外部技能、可整合候选，以及发现更多技能库的聚合资源。Stars 数为撰写时参考值，以 GitHub 为准。

**与 [full-stack-skills](../README.md) 的关系**：本仓库提供按 `skills/` 分组的全栈基础技能；外部库侧重官方示例、单一框架深度、ML/设计/产品流程等。建议按需并行注册多个 marketplace，组合使用。

---

## 1. 概述

| 类型 | 说明 |
|------|------|
| **直接使用** | 维护活跃、文档完整，推荐通过各平台 CLI / 插件市场安装，无需并入本仓库 |
| **可整合** | 可评估将部分技能迁入 `full-stack-skills/skills/<组>/`，需审许可证与重复度；详见 [integration-plan.md](integration-plan.md) |
| **发现资源** | Awesome 列表与 Hub，用于持续发现新技能库 |

安装方式因工具而异：**Claude Code** 常用 `/plugin marketplace add <owner/repo>`；**Codex** 常用 `$skill-installer`；**通用** 可用 [skills CLI](https://github.com/vercel-labs/skills)：`npx skills add <owner/repo>`（以各仓库 README 为准）。

---

## 2. 官方与平台技能库

### 2.1 [anthropics/skills](https://github.com/anthropics/skills)

- **Stars**：约 98k+
- **技能数**：约 17（含 document-skills、example-skills、claude-api）
- **类别**：文档（docx/pdf/pptx/xlsx）、创意与设计、企业与沟通、开发类（frontend-design、webapp-testing、mcp-builder、web-artifacts-builder 等）
- **全栈相关**：前端界面质量、Playwright 测本地 Web、MCP 构建、Claude API 集成、办公文档自动化
- **安装（Claude Code）**：
  ```text
  /plugin marketplace add anthropics/skills
  /plugin install document-skills@anthropic-agent-skills
  /plugin install example-skills@anthropic-agent-skills
  ```
- **互补**：本仓库偏框架与基础设施；Anthropic 官方偏「高质量通用技能」与文档能力示范。

### 2.2 [openai/skills](https://github.com/openai/skills)

- **Stars**：约 14k+
- **技能数**：`.system` 预装约 3 + `.curated` 约 33
- **类别**：部署（Vercel/Netlify/Cloudflare/Render）、Playwright、安全（threat model、best practices）、Figma 实现、ASP.NET Core、Jupyter、Sentry、Notion/Linear 等
- **全栈相关**：前后端发布流水线、E2E 测试、安全基线、设计稿落地
- **安装（Codex）**：
  ```text
  $skill-installer <skill-name>
  $skill-installer install https://github.com/openai/skills/tree/main/skills/.experimental/<skill-folder>
  ```
- **互补**：本仓库有测试/DevOps/云技能条目；OpenAI curated 更贴近 Codex 工作流与一键部署场景。

### 2.3 [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)

- **Stars**：约 2.7k+
- **技能数**：7（stitch-design、stitch-loop、design-md、enhance-prompt、react-components、remotion、shadcn-ui）
- **类别**：Stitch MCP、UI 生成、React/shadcn、Remotion
- **全栈相关**：设计到代码、多页站点生成、设计系统文档
- **安装**：
  ```bash
  npx skills add google-labs-code/stitch-skills --list
  npx skills add google-labs-code/stitch-skills --skill stitch-design --global
  ```
- **互补**：本仓库含 **stitch-skills** 扩展组（非官方重复项）；官方 stitch-skills 仍建议单独安装以获得完整官方技能集。

### 2.4 [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills)

- **Stars**：约 2.2k+
- **类别**：Gemini API、SDK、模型与智能体交互
- **全栈相关**：在应用中集成 Gemini、多模态与 Agent 模式
- **安装**：以仓库 README 为准（Gemini CLI / 插件说明）
- **互补**：本仓库以通用全栈为主；Gemini 技能专注 Google 模型栈。

### 2.5 [huggingface/skills](https://github.com/huggingface/skills)

- **Stars**：约 9k+
- **技能数**：约 14（Gradio、transformers.js、数据集、训练与评测等）
- **全栈相关**：Gradio 演示、浏览器/Node 侧推理、Hub CLI、数据集浏览
- **安装（Claude Code）**：
  ```text
  /plugin marketplace add huggingface/skills
  /plugin install <skill-name>@huggingface/skills
  ```
- **互补**：本仓库覆盖传统 Web/后端；HF 技能覆盖 ML 生命周期与演示部署。

---

## 3. 框架与技术栈专用

### 3.1 [vuejs-ai/skills](https://github.com/vuejs-ai/skills)

- **Stars**：约 2k+
- **技能数**：8（Vue 3 最佳实践、Router、Pinia、测试、JSX、调试、可组合函数等）
- **安装**：
  ```bash
  npx skills add vuejs-ai/skills
  ```
  Claude Code：`/plugin marketplace add vuejs-ai/skills` 后按提示安装
- **触发**：提示中可写 `Use vue skill, ...`（以官方 README 为准）
- **互补**：本仓库 **vue-skills** 偏 API 与项目结构；vuejs-ai 偏深度实践与测试。

### 3.2 [antfu/skills](https://github.com/antfu/skills)

- **Stars**：约 4k+
- **技能数**：约 17（Vue、Nuxt、Vite、VitePress、Vitest、UnoCSS、pnpm、Slidev、Turborepo、web-design-guidelines 等）
- **安装**：
  ```bash
  pnpx skills add antfu/skills --skill='*'
  ```
- **互补**：本仓库含 Vite/Vue；antfu 集合并维护 Nuxt/VitePress/Vitest 等一条龙内容。

### 3.3 [analogjs/angular-skills](https://github.com/analogjs/angular-skills)

- **Stars**：见 GitHub
- **技能数**：10（组件、DI、指令、表单、HTTP、路由、Signals、SSR、测试、工具链）
- **安装**：
  ```bash
  npx skills add analogjs/angular-skills
  ```
- **互补**：本仓库 **angular-skills** 单技能概览；analogjs 为 Angular v20+ 细分技能。

### 3.4 [remotion-dev/skills](https://github.com/remotion-dev/skills)

- **Stars**：约 2.2k+
- **结构**：以 `skills/remotion` 为主技能，内含多份规则（动画、字幕、音频、图表等）
- **全栈相关**：React 驱动视频/动效产品
- **安装**：仓库 README 较简，可能以 npm 包形式使用；以官方文档为准
- **互补**：本仓库无 Remotion 垂直技能；视频类产品可并行安装。

---

## 4. 内容、设计与工具类

### 4.1 [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills)

- **类别**：内容（小红书图、信息图、封面、幻灯片、公众号/X 发布等）、AI 生图、工具（URL 转 Markdown、翻译、压缩图片等）
- **安装**：
  ```bash
  npx skills add jimliu/baoyu-skills
  ```
- **互补**：本仓库偏工程实现；baoyu 偏运营与内容生产管线。

### 4.2 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

- **Stars**：约 15k+
- **类别**：Obsidian（Markdown、Bases、JSON Canvas、CLI）
- **全栈相关**：知识库、技术文档与个人笔记工作流
- **安装**：以仓库 README 为准
- **互补**：与 **document-skills** 文档工程场景互补，偏 Obsidian 生态。

### 4.3 [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

- **Stars**：约 46k+
- **类别**：多平台 UI/UX 设计情报与规范
- **安装**：以仓库 README 为准
- **互补**：强化界面与体验决策；与本仓库 **design-skills**、**frontend-design** 类能力互补。

---

## 5. 产品与流程类

### 5.1 [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills)

- **技能数**：46+ 技能与 6 条工作流命令（用户故事、PRD、路线图、发现访谈等）
- **安装**：
  ```text
  /plugin marketplace add deanpeters/Product-Manager-Skills
  /plugin install <skill-name>@pm-skills
  ```
  或 `npx skills find/add deanpeters/Product-Manager-Skills`
- **互补**：本仓库含 speckit/openspec 等规格技能；PM Skills 偏产品发现与优先级，与「做什么」衔接「怎么做」。

---

## 6. 方法论与个人仓库

### 6.1 [obra/superpowers](https://github.com/obra/superpowers)

- **Stars**：约 100k+
- **类别**：智能体技能框架与软件开发方法论（可组合技能与工作流）
- **安装**：以仓库 README 为准
- **互补**：提供宏观工作方式；与本仓库「按技术栈拆分的技能」叠加使用。

### 6.2 [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)

- **Stars**：约 89k+
- **类别**：Claude Code / Codex / Cursor 等用的技能、本能、记忆、安全与研究优先开发
- **安装**：以仓库 README 为准
- **互补**：偏「智能体装备与性能」；与本仓库「业务与栈技能」互补。

### 6.3 [mattpocock/skills](https://github.com/mattpocock/skills)

- **Stars**：约 7.6k+
- **说明**：个人 `.claude` 技能目录导出；内容随作者迭代
- **安装**：克隆后按需复制技能目录或参考作者说明
- **可整合**：见 [integration-plan.md](integration-plan.md)

### 6.4 [Dimillian/Skills](https://github.com/Dimillian/Skills)

- **Stars**：约 2.2k+
- **说明**：个人 Codex 技能集合
- **可整合**：见 [integration-plan.md](integration-plan.md)

### 6.5 [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills)

- **Stars**：约 1.1k+
- **类别**：视频剪辑 Agent（Claude Code Skills）
- **可整合**：若本仓库扩展「多媒体/内容工程」组，可评估是否迁入或仅外链

---

## 7. 技能库发现资源（聚合）

用于持续检索「适合全栈」的新技能库：

| 资源 | 说明 |
|------|------|
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 大量官方与社区技能索引 |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 多语言精选与教程 |
| [christophacham/agent-skills-library](https://github.com/christophacham/agent-skills-library) | 多来源、多类别聚合 |
| [agent-skills-hub/agent-skills-hub](https://github.com/agent-skills-hub/agent-skills-hub) | Hub 与 CLI 发现 |
| [ZhanlinCui/Agent-Skills-Hunter](https://github.com/ZhanlinCui/Agent-Skills-Hunter) | 生产向技能与 skillctl |

**GitHub 搜索**：[`skills` topics](https://github.com/search?q=topic%3Aagent-skills&type=repositories) 或关键词 `agent skills`、`claude skills`、`codex skills`。

**建议关注领域**：NestJS/FastAPI/Django/Spring 专项、React/Svelte/Solid 专项、K8s/Terraform 专项、Playwright/Jest 专项、云厂商专项、安全/OWASP 专项。

---

## 8. 快速命令速查

```text
# Claude Code：注册市场后安装插件（示例）
/plugin marketplace add anthropics/skills
/plugin marketplace add huggingface/skills
/plugin marketplace add vuejs-ai/skills
/plugin marketplace add deanpeters/Product-Manager-Skills

# 通用 skills CLI（示例）
npx skills add google-labs-code/stitch-skills --list
npx skills add vuejs-ai/skills
npx skills add analogjs/angular-skills
npx skills add jimliu/baoyu-skills
pnpx skills add antfu/skills --skill='*'

# Codex（示例）
$skill-installer playwright
```

---

## 相关链接

- [技能生态总览](skills-ecosystem.md)（本仓库 + PartMe 关联仓 + 外部库组合方式）
- [阶段→技能映射](pipeline-stage-to-skills.md)
- [可整合技能库评估](integration-plan.md)
