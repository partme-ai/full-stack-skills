<div align="center">

# Full Stack Skills

**460+ 个 Agent Skills。42+ 个技能包。一个统一生态。**

*前端 · 后端 · 移动端 · DevOps · AI 设计工具 — 生产级品质，独立安装。*

[![Stars](https://img.shields.io/github/stars/partme-ai/full-stack-skills?style=social)](https://github.com/partme-ai/full-stack-skills)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple)](https://agentskills.io)

[English](./README.en.md)

[简介](#-简介) ·
[安装](#-安装) ·
[技能目录](#-技能目录) ·
[架构](#-架构) ·
[Claude Code 用户](#-claude-code-用户) ·
[生态](#-生态) ·
[贡献](#-贡献指南)

</div>

---

## 简介

**Full Stack Skills** 是面向 AI 编码智能体的最全面 Agent Skills 集合的导航站。原为 460+ stars 的 monorepo，现已拆分为 [full-stack-skills](https://github.com/full-stack-skills) GitHub 组织下的 **42 个可独立安装的包**。

每个包提供专业知识、工作流和参考资料，AI 智能体按需加载 — 保持上下文占用最小化，同时在需要时提供深度领域专业知识。

> **迁移完成（2026 年 6 月）**：全部 454 个技能已迁移到独立仓库。本仓库现在是目录和导航站。所有现有 stars 和历史记录均保留在此。

### 我们要解决的问题

| 缺口 | 问题 | 解决方案 |
|------|------|----------|
| **上下文溢出** | 一次加载所有技能会超过 token 限制 | 通过 `npx skills add` 按包按需加载 |
| **领域专业知识** | 通用 AI 缺乏深度框架知识 | 跨 15 个领域的 454 个专业技能 |
| **可发现性** | 技能分散在各个仓库，难以查找 | 本目录 — 一个 README，所有包链接 |
| **版本锁定** | monorepo 强制协调发布 | 每个包独立版本管理和发布 |

---

## 安装

一条命令安装任意技能包：

```bash
npx skills add full-stack-skills/vue-skills      # Vue.js 生态（7 个技能）
npx skills add full-stack-skills/tauri-skills     # Tauri 桌面/移动（52 个技能）
npx skills add full-stack-skills/spring-skills    # Spring Boot 生态（7 个技能）
```

或安装包中的特定技能：

```bash
npx skills add full-stack-skills/vue-skills --skill vue3
```

---

## 技能目录

### 🌟 推荐技能包

| 包 | ⭐ Stars | 技能数 | 安装 |
|---|:------:|:------:|------|
| [baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 21.4k | 21 | `npx skills add JimLiu/baoyu-skills` |

### 前端框架（15 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [vue-skills](https://github.com/full-stack-skills/vue-skills) | 7 | `npx skills add full-stack-skills/vue-skills` |
| [react-skills](https://github.com/full-stack-skills/react-skills) | 6 | `npx skills add full-stack-skills/react-skills` |
| [angular-skills](https://github.com/full-stack-skills/angular-skills) | 1 | `npx skills add full-stack-skills/angular-skills` |
| [svelte-skills](https://github.com/full-stack-skills/svelte-skills) | 1 | `npx skills add full-stack-skills/svelte-skills` |

### 前端 UI 库（13 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [vue-ui-skills](https://github.com/full-stack-skills/vue-ui-skills) | 4 | `npx skills add full-stack-skills/vue-ui-skills` |
| [antd-skills](https://github.com/full-stack-skills/antd-skills) | 4 | `npx skills add full-stack-skills/antd-skills` |
| [uview-skills](https://github.com/full-stack-skills/uview-skills) | 2 | `npx skills add full-stack-skills/uview-skills` |
| [avue-skills](https://github.com/full-stack-skills/avue-skills) | 3 | `npx skills add full-stack-skills/avue-skills` |

### 构建与工具（44 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [build-skills](https://github.com/full-stack-skills/build-skills) | 6 | `npx skills add full-stack-skills/build-skills` |
| [nvm-skills](https://github.com/full-stack-skills/nvm-skills) | 15 | `npx skills add full-stack-skills/nvm-skills` |
| [vscode-skills](https://github.com/full-stack-skills/vscode-skills) | 4 | `npx skills add full-stack-skills/vscode-skills` |
| [utility-skills](https://github.com/full-stack-skills/utility-skills) | 7 | `npx skills add full-stack-skills/utility-skills` |
| [dev-utils-skills](https://github.com/full-stack-skills/dev-utils-skills) | 12 | `npx skills add full-stack-skills/dev-utils-skills` |

### 图表与 ASCII 艺术（15 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [chart-skills](https://github.com/full-stack-skills/chart-skills) | 2 | `npx skills add full-stack-skills/chart-skills` |
| [ascii-skills](https://github.com/full-stack-skills/ascii-skills) | 13 | `npx skills add full-stack-skills/ascii-skills` |

### 后端框架（19 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [spring-skills](https://github.com/full-stack-skills/spring-skills) | 7 | `npx skills add full-stack-skills/spring-skills` |
| [nodejs-skills](https://github.com/full-stack-skills/nodejs-skills) | 4 | `npx skills add full-stack-skills/nodejs-skills` |
| [python-skills](https://github.com/full-stack-skills/python-skills) | 3 | `npx skills add full-stack-skills/python-skills` |
| [go-skills](https://github.com/full-stack-skills/go-skills) | 2 | `npx skills add full-stack-skills/go-skills` |
| [java-skills](https://github.com/full-stack-skills/java-skills) | 3 | `npx skills add full-stack-skills/java-skills` |
| [rust-skills](https://github.com/actionbook/rust-skills) | — | `npx skills add actionbook/rust-skills` |
| [zig-skills](https://github.com/full-stack-skills/zig-skills) | 5 | `npx skills add full-stack-skills/zig-skills` |

### 跨平台与桌面（72 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [uniapp-skills](https://github.com/full-stack-skills/uniapp-skills) | 13 | `npx skills add full-stack-skills/uniapp-skills` |
| [flutter-skills](https://github.com/full-stack-skills/flutter-skills) | 2 | `npx skills add full-stack-skills/flutter-skills` |
| [electron-skills](https://github.com/full-stack-skills/electron-skills) | 3 | `npx skills add full-stack-skills/electron-skills` |
| [tauri-skills](https://github.com/full-stack-skills/tauri-skills) | 52 | `npx skills add full-stack-skills/tauri-skills` |
| [mobile-native-skills](https://github.com/full-stack-skills/mobile-native-skills) | 2 | `npx skills add full-stack-skills/mobile-native-skills` |

### 3D 与游戏（19 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [threejs-skills](https://github.com/full-stack-skills/threejs-skills) | 18 | `npx skills add full-stack-skills/threejs-skills` |
| [cocos-skills](https://github.com/full-stack-skills/cocos-skills) | 1 | `npx skills add full-stack-skills/cocos-skills` |

### 架构与设计模式（35 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [ddd-skills](https://github.com/full-stack-skills/ddd-skills) | 16 | `npx skills add full-stack-skills/ddd-skills` |
| [design-skills](https://github.com/full-stack-skills/design-skills) | 4 | `npx skills add full-stack-skills/design-skills` |
| [drawio-skills](https://github.com/full-stack-skills/drawio-skills) | 2 | `npx skills add full-stack-skills/drawio-skills` |
| [document-skills](https://github.com/full-stack-skills/document-skills) | 8 | `npx skills add full-stack-skills/document-skills` |
| [ocrmypdf-skills](https://github.com/full-stack-skills/ocrmypdf-skills) | 5 | `npx skills add full-stack-skills/ocrmypdf-skills` |

### 数据库与存储（5 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [database-skills](https://github.com/full-stack-skills/database-skills) | 5 | `npx skills add full-stack-skills/database-skills` |

### DevOps 与容器（22 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [devops-skills](https://github.com/full-stack-skills/devops-skills) | 6 | `npx skills add full-stack-skills/devops-skills` |
| [docker-skills](https://github.com/full-stack-skills/docker-skills) | 16 | `npx skills add full-stack-skills/docker-skills` |

### 测试（9 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [testing-skills](https://github.com/full-stack-skills/testing-skills) | 9 | `npx skills add full-stack-skills/testing-skills` |

### 规范驱动开发（28 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [speckit-skills](https://github.com/full-stack-skills/speckit-skills) | 13 | `npx skills add full-stack-skills/speckit-skills` |
| [openspec-skills](https://github.com/full-stack-skills/openspec-skills) | 15 | `npx skills add full-stack-skills/openspec-skills` |

### AI 设计工具 — MCP（153 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [stitch-skills](https://github.com/full-stack-skills/stitch-skills) | 28 | `npx skills add full-stack-skills/stitch-skills` |
| [pencil-skills](https://github.com/full-stack-skills/pencil-skills) | 28 | `npx skills add full-stack-skills/pencil-skills` |
| [t2ui-skills](https://github.com/full-stack-skills/t2ui-skills) | 97 | `npx skills add full-stack-skills/t2ui-skills` |

### 教学与学习（3 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [teaching-skills](https://github.com/full-stack-skills/teaching-skills) | 3 | `npx skills add full-stack-skills/teaching-skills` |

### 社交与沟通（2 个技能）

| 包 | 技能数 | 安装 |
|---|--------|------|
| [social-skills](https://github.com/full-stack-skills/social-skills) | 2 | `npx skills add full-stack-skills/social-skills` |

---

## 架构

### 技能工作原理

每个技能遵循 [Agent Skills 规范](https://agentskills.io)：

```
<package>/
├── skills/
│   ├── <skill-name>/
│   │   ├── SKILL.md          # 必需 — AI 智能体按需加载
│   │   ├── examples/         # 可选 — 使用示例
│   │   ├── references/       # 可选 — 详细参考文档
│   │   └── scripts/          # 可选 — 可执行脚本
│   └── ...
├── .claude-plugin/           # 插件元数据
└── README.md
```

### 按需加载

技能使用**渐进式披露**：
1. **启动时**：仅加载技能名称和描述（最小上下文）
2. **按需**：当智能体识别到相关任务时加载完整的 `SKILL.md`
3. **深入**：仅在明确需要时读取参考文件

这保持上下文占用最小化，同时在需要时提供深度专业知识。

### 包组织

| 分类 | 包数 | 技能总数 |
|------|------|----------|
| 前端框架 | 4 | 15 |
| 前端 UI 库 | 4 | 13 |
| 构建与工具 | 5 | 44 |
| 图表与 ASCII 艺术 | 2 | 15 |
| 后端框架 | 5 | 19 |
| 跨平台与桌面 | 5 | 72 |
| 3D 与游戏 | 2 | 19 |
| 架构与设计 | 5 | 35 |
| 数据库与存储 | 1 | 5 |
| DevOps 与容器 | 2 | 22 |
| 测试 | 1 | 9 |
| 规范驱动开发 | 2 | 28 |
| AI 设计工具（MCP） | 3 | 153 |
| 教学与学习 | 1 | 3 |
| 社交与沟通 | 1 | 2 |
| **总计** | **42** | **454** |

---

## Claude Code 用户

安装单个技能包：

```bash
npx skills add full-stack-skills/tauri-skills    # 52 个 Tauri 技能
npx skills add full-stack-skills/spring-skills   # 7 个 Spring Boot 技能
npx skills add full-stack-skills/threejs-skills  # 18 个 Three.js 技能
```

或手动复制技能到项目：

```bash
git clone https://github.com/full-stack-skills/<skill-name>.git
cp -r <skill-name>/skills/* .claude/skills/
```

---

## 生态

| 资源 | 链接 |
|------|------|
| **所有包** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills 规范** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |
| **Skills 目录** | [skills.sh](https://skills.sh) |
| **PartMe.AI** | [github.com/partme-ai](https://github.com/partme-ai) |

---

## 贡献指南

欢迎贡献！每个技能包是 [full-stack-skills](https://github.com/full-stack-skills) 组织下的独立仓库。

1. Fork 相关包仓库
2. 按照 [Agent Skills 规范](https://agentskills.io) 添加你的技能
3. 提交 PR

详见 [AGENTS.md](AGENTS.md) 创建技能的详细指南。

---

## 许可证

Apache 2.0 — 详见 [LICENSE](LICENSE)。

---

<div align="center">

**如果这个项目对你有帮助，请给我们一个 ⭐️**

Made with ❤️ by PartMe.AI Team

</div>
