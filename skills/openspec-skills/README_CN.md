<div align="center">

# OpenSpec-Skills（Alpha）

**OpenSpec Spec 驱动开发的 Agent Skills 集合**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-15-orange)
![Plugins](https://img.shields.io/badge/Plugins-3-brightgreen)

</div>

## 简介

**OpenSpec-Skills** 是一套面向 [OpenSpec](https://github.com/Fission-AI/OpenSpec) 的开源 Agent Skills 集合——OpenSpec 是一个流动、迭代式的 Spec 驱动开发框架。提供 **15 个技能**，按 **3 个插件** 组织：环境准备（install、init、update）、核心 OPSX 工作流（explore、new、continue、ff、apply、verify、archive）和可选/高级（sync、bulk-archive、onboard、schema、config）。

本仓库参与「需求 → 部署」全链路的**产品阶段**与**开发阶段**。阶段映射与技能生态见 [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) 与 [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md)。

> **注意：** 当前项目处于 Alpha 阶段，欢迎反馈。

## 什么是 Skills？

Skills 是由说明与资源组成的文件夹，智能体会按需加载，用于执行结构化工作流——例如发起变更、创建制品、实现任务、验证完整性、归档等。

### 更多信息

- [什么是技能？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills 规范](https://agentskills.io/)

## 关于本仓库

**OpenSpec-Skills** 提供实现 OpenSpec OPSX 工作流的 Agent Skills，可在 Claude Code、Cursor 等支持 Agent Skills 的环境中按步骤执行 explore、new、continue、ff、apply、verify、archive 及可选的 sync、bulk-archive、onboard、schema、config。

### 核心特性

- **开源**：Apache 2.0，遵循 Agent Skills 规范。
- **15 个技能**：覆盖完整 OpenSpec OPSX 流程、环境准备及可选/高级功能。
- **3 个插件**：openspec-env（3 个技能）、openspec-core（7 个技能）、openspec-optional（5 个技能）。

### 项目结构

```
openspec-skills/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── openspec-install/
│   ├── openspec-initial/
│   └── ...                     # 15 个技能
├── spec/
│   └── agent-skills-spec.md
├── template/
│   └── SKILL.md
├── README.md
└── README_CN.md
```

**插件类别**

| 插件              | 技能数 | 说明                                                         |
|-------------------|--------|--------------------------------------------------------------|
| openspec-env      | 3      | install、initial、update                                     |
| openspec-core     | 7      | explore、new、continue、ff、apply、verify、archive           |
| openspec-optional | 5      | sync、bulk-archive、onboard、schema、config                  |

## 安装与环境

在使用 OpenSpec 工作流前，请先准备环境：

1. **安装 OpenSpec CLI** — 使用技能 **openspec-install**（或执行 `npm install -g @fission-ai/openspec@latest`）。支持 npm、pnpm、yarn、bun、nix。
2. **初始化项目** — 使用技能 **openspec-initial**（或执行 `openspec init`）。支持 20+ AI 工具，通过 `--tools` 指定。
3. **升级后更新** — 使用技能 **openspec-update**（或执行 `openspec update`），在升级 CLI 后刷新工具配置。

## 快速开始

### 支持的 Agent

Claude Code、Cursor、Windsurf、GitHub Copilot、Cline、CodeBuddy、Codex、Continue、Gemini、RooCode、Trae 及 [20+ 更多](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md)。

### 在 Claude Code 中使用

**1. 注册市场**

```bash
/plugin marketplace add https://github.com/partme-ai/openspec-skills.git
```

或：`/plugin marketplace add partme-ai/openspec-skills`

**2. 安装插件**

```bash
/plugin install openspec-env@openspec-skills
/plugin install openspec-core@openspec-skills
/plugin install openspec-optional@openspec-skills
```

**3. 使用技能**

在对话中直接描述需求即可，例如：「安装 OpenSpec」「在项目中初始化 OpenSpec」「探索认证改进方案」「为暗色模式发起新变更」「快速前进生成所有制品」「实现任务」「验证并归档」。

### OpenSpec 环境

若需完整 OpenSpec OPSX 流程，请安装 CLI 并初始化：

```bash
npm install -g @fission-ai/openspec@latest
openspec init --tools claude,cursor
```

然后使用 OPSX 命令：`/opsx:explore`、`/opsx:new`、`/opsx:ff`、`/opsx:apply`、`/opsx:verify`、`/opsx:archive`。

## 插件与技能列表

### openspec-env

**安装命令：** `/plugin install openspec-env@openspec-skills`

- `openspec-install` — 全局安装 OpenSpec CLI（npm/pnpm/yarn/bun/nix）。*对应：npm install -g @fission-ai/openspec。*
- `openspec-initial` — 执行 `openspec init` 初始化项目（创建 openspec/、配置 AI 工具）。*对应：openspec init。*
- `openspec-update` — 执行 `openspec update`，在 CLI 升级后刷新工具配置。*对应：openspec update。*

### openspec-core

**安装命令：** `/plugin install openspec-core@openspec-skills`

- `openspec-explore` — 思考创意、调查问题、澄清需求。*对应：/opsx:explore。*
- `openspec-new` — 发起新变更（创建变更目录与元数据）。*对应：/opsx:new。*
- `openspec-continue` — 根据依赖图创建下一个制品。*对应：/opsx:continue。*
- `openspec-ff` — 快速前进：一次性创建所有规划制品。*对应：/opsx:ff。*
- `openspec-apply` — 实现任务，编写代码并勾选完成项。*对应：/opsx:apply。*
- `openspec-verify` — 验证实现与制品是否匹配（完整性、正确性、一致性）。*对应：/opsx:verify。*
- `openspec-archive` — 归档已完成的变更，将增量规格合并到主规格。*对应：/opsx:archive。*

### openspec-optional

**安装命令：** `/plugin install openspec-optional@openspec-skills`

- `openspec-sync` — 将增量规格同步到主规格而不归档（适用于长期变更）。*对应：/opsx:sync。*
- `openspec-bulk-archive` — 批量归档多个已完成的变更，处理冲突。*对应：/opsx:bulk-archive。*
- `openspec-onboard` — 使用真实代码的完整工作流引导教程。*对应：/opsx:onboard。*
- `openspec-schema` — 创建和管理自定义工作流架构（init、fork、validate、which）。*对应：openspec schema。*
- `openspec-config` — 项目配置（上下文、制品规则、默认架构）。*对应：openspec/config.yaml + openspec config。*

## 致谢

本技能集合基于并对齐 [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) 构建。感谢 OpenSpec 项目及其贡献者。

## 免责声明

这些技能仅供演示与教育使用。关键任务前请在自身环境中验证行为。
