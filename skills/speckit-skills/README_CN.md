<div align="center">

# Speckit-Skills（Alpha）

**Spec 驱动开发的 Agent Skills 集合**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-13-orange)
![Plugins](https://img.shields.io/badge/Plugins-2-brightgreen)

</div>

## 简介

**Speckit-Skills** 是一套面向 **Spec 驱动开发（Spec-Driven Development）** 的开源 Agent Skills 集合，与 [GitHub spec-kit](https://github.com/github/spec-kit) 及 [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills) 对齐。**本仓库中部分技能与内容源自 [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills)。** 提供 **13 个技能**，按 **2 个插件** 组织：核心（安装、初始化、环境检查，再 constitution → specify → clarify → plan → tasks → implement）与可选步骤（baseline、analyze、checklist、taskstoissues）。

本仓库参与「需求→部署」全链路的**产品阶段**与**开发阶段**。阶段映射与技能生态见 [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) 与 [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md)。

> **注意：** 当前项目处于 Alpha 阶段，欢迎反馈。

## 什么是 Skills？

Skills 是由说明与资源组成的文件夹，智能体会按需加载，用于执行结构化工作流——例如制定项目原则、从自然语言生成规格、生成技术方案、拆解任务、按任务实现等。

### 更多信息

- [什么是技能？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills 规范](https://agentskills.io/)

## 关于本仓库

**Speckit-Skills** 提供实现 Spec Kit 工作流的 Agent Skills，可在 Claude Code、Cursor 等支持 Agent Skills 的环境中按步骤执行 constitution、specify、clarify、plan、tasks、implement 及可选的 baseline、analyze、checklist、taskstoissues。

### 核心特性

- **开源**：Apache 2.0，遵循 Agent Skills 规范。
- **13 个技能**：安装、初始化、环境检查，再覆盖完整 Spec Kit 流程及可选步骤。
- **2 个插件**：speckit-core（9 个技能）、speckit-optional（4 个技能）。

### 项目结构

```
speckit-skills/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── speckit-constitution/
│   ├── speckit-specify/
│   └── ...                     # 13 个技能
├── spec/
│   └── agent-skills-spec.md
├── template/
│   └── SKILL.md
├── README.md
└── README_CN.md
```

**插件类别**

| 插件            | 技能数 | 说明                                               |
|-----------------|--------|----------------------------------------------------|
| speckit-core    | 9      | install、initial、check、constitution、specify、clarify、plan、tasks、implement |
| speckit-optional| 4      | baseline、analyze、checklist、taskstoissues        |

## 安装与环境

在使用完整 Spec Kit 流程（如 `.specify/` 模板与 slash 命令）前，请先准备环境：

1. **安装 Specify CLI** – 使用技能 **speckit-install**（或执行 `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`）。支持多 OS、持久/一次性（uvx）及企业/限网环境。
2. **初始化项目** – 使用技能 **speckit-initial**（或执行 `specify init . --ai <agent>`）。支持多 AI Agent 及 `--script sh` / `--script ps`。
3. **验证** – 使用技能 **speckit-check**（或执行 `specify check`）确认工具与 Agent 已正确检测。

多 OS、多 Agent 或企业环境详见 **speckit-install**、**speckit-initial** 技能说明。

## 快速开始

### 支持的 Agent

Claude Code、Cursor、Trae、Windsurf、GitHub Copilot、Continue、CodeBuddy 等支持 Agent Skills 的环境。

### 在 Claude Code 中使用

**1. 注册市场**

```bash
/plugin marketplace add https://github.com/partme-ai/speckit-skills.git
```

或：`/plugin marketplace add partme-ai/speckit-skills`

**2. 安装插件**

```bash
/plugin install speckit-core@speckit-skills
/plugin install speckit-optional@speckit-skills
```

**3. 使用技能**

在对话中直接描述需求即可，例如：「制定项目原则」「为相册应用写一份需求规格」「用 Vue + SQLite 生成技术方案」「按方案拆成任务」「按 tasks.md 实现」。

### Spec Kit 环境

若需完整 Spec Kit 流程（如 `.specify/` 模板与脚本），请先使用 **speckit-install** 再使用 **speckit-initial**（或直接执行）：

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init . --ai claude
```

可用 **speckit-check** 或 `specify check` 验证。如需 Codex、Gemini、GitHub Copilot 等运行时的 slash 命令配置，可参考 [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills) 的 `.claude/commands`、`.codex/`、`.gemini/`、`.github/`。

## 插件与技能列表

### speckit-core

**安装命令：** `/plugin install speckit-core@speckit-skills`

- `speckit-install` – 在本机安装 Specify CLI（uv tool install 或 uvx；多 OS、企业/限网）。*对应：安装 CLI。*
- `speckit-initial` – 在项目中执行 `specify init`（拉取 `.specify/`、slash 命令；多 Agent、`--script sh`/`ps`）。*对应：specify init。*
- `speckit-check` – 执行 `specify check` 并解读结果（验证工具与 Agent）。*对应：specify check。*
- `speckit-constitution` – 创建或更新项目原则（`.specify/memory/constitution.md`）。
- `speckit-specify` – 从自然语言生成/更新功能规格（what/why）。
- `speckit-clarify` – 澄清规格歧义（建议在 plan 前执行）。
- `speckit-plan` – 生成技术方案（how、技术栈、架构）。
- `speckit-tasks` – 从方案生成有序任务列表。
- `speckit-implement` – 按 `tasks.md` 执行实现。

### speckit-optional

**安装命令：** `/plugin install speckit-optional@speckit-skills`

- `speckit-baseline` – 从现有代码生成规格（可选入口）。
- `speckit-analyze` – 跨制品一致性校验（tasks 之后、implement 之前）。
- `speckit-checklist` – 需求/规格质量检查清单。
- `speckit-taskstoissues` – 将任务转为 Issue（如 GitHub）。

### 致谢与上游

本仓库中部分代码与技能定义源自 [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills)，感谢上游项目及其贡献者。

### 免责声明

这些技能仅供演示与教育使用。关键任务前请在自身环境中验证行为。
