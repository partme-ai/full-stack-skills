<div align="center">

# Tauri Skills（Alpha）

**基于 Agent Skills 规范的 Tauri 全栈开发技能集合**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-51-orange)
![Plugins](https://img.shields.io/badge/Plugins-7-brightgreen)

</div>

## 📖 简介

**Tauri Skills** 是一个专注于 **Tauri 跨平台应用开发** 的开源 Agent Skills 集合，严格遵循 [Agent Skills 规范](https://agentskills.io/)。它提供了 **51 个专业技能**，按功能领域组织为 **7 个插件类别**，覆盖了从环境搭建、应用开发、系统集成到移动端适配、安全加固的 Tauri 开发全生命周期。

通过这些技能，全栈开发者可以利用 Claude 等 AI 助手快速掌握 Tauri 开发最佳实践，高效构建跨平台桌面和移动端应用。

> **⚠️ 注意：** 当前项目处于 Alpha 阶段，尚未经过严格测试，还在自测中。欢迎反馈问题和建议。

## 什么是 Skills？

Skills 是由说明、脚本和资源组成的文件夹，Claude 会按需动态加载它们，以提升在特定任务上的表现。Skills 用于以可复用的方式教会 Claude 完成具体工作，例如：初始化 Tauri 项目、配置系统托盘、处理文件系统操作或集成移动端功能。

### 更多信息

- [什么是技能？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills 规范](https://agentskills.io/)

## 关于本仓库

**tauri-skills** 是一个面向 **Tauri 开发者** 的专业技能库，旨在通过 AI 赋能 Tauri 生态建设。

### ✨ 核心特性

#### 1. 开源免费
- **Apache 2.0 许可证**：所有技能采用 Apache 2.0 许可证，完全开源
- **规范标准**：严格遵循 Agent Skills 规范，确保技能质量和兼容性

#### 2. 全面覆盖
- **51 个技能集合**：覆盖核心框架、系统能力、网络通信、数据存储、UI 交互、移动端特性及安全机制
- **7 个插件类别**：按功能模块划分，结构清晰，便于检索和使用

#### 3. AI 赋能
- **智能识别**：Claude 会根据你的 Tauri 开发需求自动调用相关技能
- **最佳实践**：内置 Tauri 官方推荐的最佳实践和代码模板
- **丰富示例**：每个技能均包含至少 5 个具体使用场景和示例代码

### 🏗️ 项目架构

**Tauri Skills 技能组织结构**：

```
tauri-skills/
├── .claude-plugin/
│   └── marketplace.json          # 插件市场配置
├── skills/                       # 技能目录
│   ├── tauri-scaffold/           # 单个技能目录
│   │   ├── SKILL.md              # 技能主文档
│   │   ├── examples/             # 示例文件
│   │   ├── templates/            # 模板文件
│   │   └── LICENSE.txt           # 许可证
│   ├── tauri-app-window/
│   └── ...                       # 51 个技能
├── README.md                     # 项目说明（英文）
└── README_CN.md                  # 项目说明（中文）
```

**插件类别组织**：

| 插件类别 | 技能数量 | 说明 |
|---|---|---|
| tauri-core | 10 | 核心框架与项目配置技能 |
| tauri-system | 14 | 系统集成与原生能力技能 |
| tauri-network | 6 | 网络通信与 IPC 技能 |
| tauri-mobile | 6 | 移动端开发与硬件调用技能 |
| tauri-data | 4 | 数据持久化与存储技能 |
| tauri-ui | 5 | UI 交互与窗口管理技能 |
| tauri-security | 6 | 安全加固与权限管理技能 |

## � 快速开始

### 支持的 Agent

本项目的 Skills 符合 [Agent Skills](https://github.com/vercel-labs/skills) 标准，支持以下 Agent 环境：

- **Claude Code**
- **Trae**
- **Cursor**
- **Windsurf**
- **GitHub Copilot**
- **OpenHands**
- **Continue**
- **Roo Code**
- **CodeBuddy**
- 以及其他 20+ 种支持 Agent Skills 的工具 (Amp, Antigravity, Cline, Codex, etc.)

你可以使用 `npx skills` 命令行工具来管理和安装这些技能。

### 在 Claude Code 中使用

#### 1. 注册 Marketplace

在 Claude Code 中运行以下命令，将本仓库注册为 Claude Code 的插件市场：

```bash
/plugin marketplace add https://github.com/partme-ai/tauri-skills.git
```


![add_marketplace.png](./media/add_marketplace.png)

安装成功！

![add_marketplace_success.png](media/add_marketplace_success.png)

或者使用简写（如果已发布到官方源）：

```
/plugin marketplace add partme-ai/tauri-skills
```

删除插件：

```
/plugin marketplace remove tauri-skills
```

#### 2. 安装插件

你可以按需安装特定的插件类别：

```bash
# 安装核心开发技能
/plugin install tauri-core@tauri-skills

# 安装系统能力技能
/plugin install tauri-system@tauri-skills

# 安装所有插件（建议）
/plugin install tauri-core@tauri-skills
/plugin install tauri-system@tauri-skills
/plugin install tauri-network@tauri-skills
/plugin install tauri-mobile@tauri-skills
/plugin install tauri-data@tauri-skills
/plugin install tauri-ui@tauri-skills
/plugin install tauri-security@tauri-skills
```

#### 3. 使用技能

安装插件后，只需在对话中提到相关任务，Claude 就会自动调用技能。例如：
- "帮我创建一个基于 Vue 和 TypeScript 的 Tauri 项目"
- "如何配置 Tauri 的系统托盘？"
- "在 Tauri 中如何读取本地文件？"

### 在其他平台使用

这些 skills 也可以在其他支持 Agent Skills 规范的 AI 平台使用，如 Cursor、Trae 等。

## 可用插件和技能详细列表

本仓库包含 **51 个技能**，按功能分类如下：

---

### 📦 tauri-core（核心框架与配置）

**安装命令：** `/plugin install tauri-core@tauri-skills`

**描述：** 包含 Tauri 项目初始化、配置管理、构建流程及开发辅助工具。

- `tauri-scaffold` - 项目脚手架生成
- `tauri-setup` - 环境搭建与依赖检查
- `tauri-config` - `tauri.conf.json` 配置详解
- `tauri-build` - 构建与打包流程管理
- `tauri-app-develop` - 开发模式与调试技巧
- `tauri-app-creator` - 应用创建向导
- `tauri-app-frontend-selection` - 前端框架选择与集成
- `tauri-app-planning` - 项目规划与架构设计
- `tauri-framework-upgrade` - 框架版本升级指南
- `tauri-concept` - Tauri 核心概念解析

---

### 🖥️ tauri-system（系统集成）

**安装命令：** `/plugin install tauri-system@tauri-skills`

**描述：** 提供对操作系统原生能力的访问，如文件系统、剪贴板、通知、命令行交互等。

- `tauri-app-cli` - 命令行接口集成
- `tauri-app-clipboard` - 剪贴板读写操作
- `tauri-app-file-system` - 文件系统操作（Fs）
- `tauri-app-process` - 子进程管理与命令执行
- `tauri-app-shell` - Shell 命令执行
- `tauri-app-os-info` - 操作系统信息获取
- `tauri-app-dialog` - 原生对话框（打开/保存文件、消息提示）
- `tauri-app-notification` - 系统通知发送
- `tauri-app-global-shortcut` - 全局快捷键注册
- `tauri-app-autostart` - 开机自启动配置
- `tauri-app-deep-linking` - 深度链接（Deep Link）处理
- `tauri-app-single-instance` - 单实例锁应用
- `tauri-app-system-tray` - 系统托盘图标和菜单
- `tauri-app-window-menu` - 应用窗口菜单配置
- `tauri-app-logging` - 日志文件管理和调试

---

### 🌐 tauri-network（网络与通信）

**安装命令：** `/plugin install tauri-network@tauri-skills`

**描述：** 处理网络请求、WebSocket 通信以及前端与 Rust 后端的 IPC 通信。

- `tauri-app-http-client` - HTTP 客户端请求
- `tauri-app-websocket` - WebSocket 连接管理
- `tauri-app-upload` - 文件上传功能
- `tauri-app-localhost` - 本地服务器集成
- `tauri-ipc` - 前后端进程间通信（IPC）
- `tauri-app-sidecar-nodejs` - 集成 Node.js Sidecar

---

### 📱 tauri-mobile（移动端与硬件）

**安装命令：** `/plugin install tauri-mobile@tauri-skills`

**描述：** 专注于移动端特性（iOS/Android）及硬件传感器调用。

- `tauri-mobile` - 移动端开发配置
- `tauri-app-biometric` - 生物识别（指纹/面容）
- `tauri-app-barcode-scanner` - 条码/二维码扫描
- `tauri-app-haptics` - 触觉反馈（震动）
- `tauri-app-nfc` - NFC 读写
- `tauri-app-geolocation` - 地理位置定位

---

### � tauri-data（数据与存储）

**安装命令：** `/plugin install tauri-data@tauri-skills`

**描述：** 提供本地数据持久化方案，包括 SQL 数据库和键值存储。

- `tauri-app-store` - 简单键值存储（Store）
- `tauri-app-sql` - SQL 数据库集成（SQLite/MySQL/PostgreSQL）
- `tauri-app-stronghold` - 加密存储（Stronghold）
- `tauri-app-persisted-scope` - 持久化作用域管理

---

### 🎨 tauri-ui（UI 与窗口）

**安装命令：** `/plugin install tauri-ui@tauri-skills`

**描述：** 管理应用窗口、启动画面及 UI 相关交互。

- `tauri-window` - 窗口创建与管理
- `tauri-app-splashscreen` - 启动画面（Splashscreen）
- `tauri-app-window-state` - 窗口状态保存与恢复
- `tauri-app-positioner` - 窗口定位工具
- `tauri-app-opener` - 使用默认应用打开文件/链接

---

### 🔒 tauri-security（安全与权限）

**安装命令：** `/plugin install tauri-security@tauri-skills`

**描述：** Tauri 安全机制配置、权限管理及隔离策略。

- `tauri-security` - 安全最佳实践
- `tauri-framework-security` - 框架安全特性
- `tauri-app-plugin-permissions` - 插件权限配置
- `tauri-app-wasm` - WebAssembly 集成安全
- `tauri-allowlist` - (集成在配置中) 允许列表配置
- `tauri-csp` - (集成在配置中) 内容安全策略

---

### 免责声明

**这些技能仅用于演示与教育用途。** 虽然其中部分能力可能在 Claude 中可用，但你从 Claude 获得的实现与行为可能与这些技能所展示的不同。在依赖它们处理关键任务之前，请务必在你自己的环境中充分测试。
