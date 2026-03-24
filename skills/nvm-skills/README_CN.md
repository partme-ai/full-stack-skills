<div align="center">

# nvm Skills（Alpha）

**Node 版本管理器（nvm）Agent Skills 集合**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-15-orange)
![Plugins](https://img.shields.io/badge/Plugins-4-brightgreen)

</div>

## 📖 简介

**nvm Skills** 是一套面向 **Node Version Manager (nvm)** 安装、配置、日常使用、Shell 集成、Docker/CI 及排障的开源 Agent Skills 集合，严格遵循 [Agent Skills 规范](https://agentskills.io/)。提供 **15 个技能**，按 **4 个插件类别** 组织，覆盖从安装、环境配置、验证、版本切换、.nvmrc、全局包、镜像到 macOS/Linux 排障的完整 nvm 使用链路。

本仓库参与「需求→部署」全链路的**开发阶段**（基础环境）。全链路阶段映射与技能生态见 [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) 与 [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md)。

> **⚠️ 注意：** 当前项目处于 Alpha 阶段，尚未经过严格测试。欢迎反馈与建议。

## 什么是 Skills？

Skills 是由说明、脚本和资源组成的文件夹，Claude 会按需动态加载，以提升在特定任务上的表现。例如：用 curl/wget 安装 nvm、配置 shell 与 PROFILE、验证安装、切换 Node 版本、排查 PATH 问题等。

### 更多信息

- [什么是技能？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills 规范](https://agentskills.io/)

## 关于本仓库

**nvm-skills** 面向需要在脚本、文档或自动化中安装、配置和排障 **nvm**（https://github.com/nvm-sh/nvm）的开发者与 AI 智能体。

### ✨ 核心特性

#### 1. 开源免费
- **Apache 2.0 许可证**：所有技能采用 Apache 2.0，完全开源。
- **规范标准**：遵循 Agent Skills 规范，保证兼容性。

#### 2. 覆盖全面
- **15 个技能**：安装、配置、验证、日常使用、默认版本/.nvmrc、全局包、镜像与认证、Shell 集成、Docker/CI、卸载、杂项、项目元信息及 macOS/Linux 排障。
- **4 个插件类别**：核心、进阶、运维、排障。

#### 3. AI 赋能
- **智能识别**：Claude 根据「安装 nvm」「修复 PATH」「使用 .nvmrc」「Docker 里用 nvm」等需求自动调用对应技能。
- **渐进式披露**：SKILL.md 保持精简，细节放在 `examples/` 中按需加载。

### 🏗️ 项目架构

```
nvm-skills/
├── .claude-plugin/
│   └── marketplace.json          # 插件市场配置
├── skills/                       # 技能目录
│   ├── nvm-install/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── LICENSE.txt
│   └── ...                       # 15 个技能
├── spec/
│   └── agent-skills-spec.md
├── template/
│   └── SKILL.md
├── README.md                     # 英文说明
└── README_CN.md                  # 本文件（中文）
```

**插件类别**：

| 插件类别           | 技能数 | 说明                     |
|--------------------|--------|--------------------------|
| nvm-core           | 5      | 安装、配置、验证、日常使用 |
| nvm-advanced       | 4      | 默认/.nvmrc、全局包、镜像、Shell |
| nvm-ops            | 4      | Docker/CI、卸载、杂项、项目元信息 |
| nvm-troubleshooting | 2     | macOS 与 Linux 排障      |

## 📖 快速开始

### 支持的 Agent

本仓库技能符合 [Agent Skills](https://agentskills.io/) 标准，可在 Claude Code、Cursor、Trae、Windsurf、GitHub Copilot、Continue、CodeBuddy 等支持该标准的平台使用。

### 在 Claude Code 中使用

#### 1. 注册市场

```bash
/plugin marketplace add https://github.com/partme-ai/nvm-skills.git
```

简写（若已发布）：

```bash
/plugin marketplace add partme-ai/nvm-skills
```

移除：

```bash
/plugin marketplace remove nvm-skills
```

#### 2. 安装插件

```bash
# 核心：安装、配置、验证、使用
/plugin install nvm-core@nvm-skills

# 进阶：.nvmrc、全局包、镜像、Shell 集成
/plugin install nvm-advanced@nvm-skills

# 运维：Docker/CI、卸载、杂项
/plugin install nvm-ops@nvm-skills

# 排障：macOS 与 Linux
/plugin install nvm-troubleshooting@nvm-skills
```

#### 3. 使用技能

安装后，在对话中描述需求即可，Claude 会调用对应技能。例如：

- 「在 macOS 上怎么安装 nvm？」
- 「让 nvm 在 zsh 里自动加载。」
- 「检查 nvm 是否安装成功。」
- 「在当前项目里用 .nvmrc。」
- 「在 Docker 里用 nvm 安装 Node。」
- 「安装后 nvm 命令找不到怎么办？」

## 插件与技能列表

### 📦 nvm-core（安装、配置、验证、使用）

**安装命令：** `/plugin install nvm-core@nvm-skills`

- `nvm` - 总览与入口
- `nvm-install` - 安装/更新 nvm（curl/wget、PROFILE、NVM_DIR）
- `nvm-setup` - Shell 配置与环境（NVM_DIR、nvm.sh、bash/zsh/fish）
- `nvm-verify` - 验证安装（nvm --version、node -v、npm -v、PATH）
- `nvm-usage-basics` - 安装/切换/列出 Node 版本、LTS、系统 Node

---

### 🔧 nvm-advanced（默认版本、全局包、镜像、Shell）

**安装命令：** `/plugin install nvm-advanced@nvm-skills`

- `nvm-defaults-and-nvmrc` - 默认 Node 版本与 .nvmrc 使用
- `nvm-global-packages` - 全局包迁移与 default-packages
- `nvm-mirror-and-auth` - Node 二进制镜像与认证 header
- `nvm-shell-integration` - 深度 Shell 集成（bash/zsh/fish）、PATH 恢复

---

### 🚀 nvm-ops（Docker、CI、卸载、杂项）

**安装命令：** `/plugin install nvm-ops@nvm-skills`

- `nvm-docker-ci` - Docker 与 CI/CD 中的 nvm（BASH_ENV、ENTRYPOINT）
- `nvm-uninstall` - 卸载与清理（NVM_DIR、profile 移除）
- `nvm-misc` - 颜色、Ansible、测试等
- `nvm-project-meta` - 项目支持、许可证、维护者

---

### 🔍 nvm-troubleshooting（macOS 与 Linux）

**安装命令：** `/plugin install nvm-troubleshooting@nvm-skills`

- `nvm-troubleshooting-macos` - macOS 常见问题（profile、权限、PATH）
- `nvm-troubleshooting-linux` - Linux 常见问题（发行版差异、PATH）

---

### 免责声明

**这些技能仅供演示与教育使用。** 实际环境中的行为可能有所不同，请在关键任务前自行充分测试。
