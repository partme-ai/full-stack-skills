<div align="center">

# Pencil Skills

**Pencil UI 生成的 Agent Skills 集合**

![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-11-orange)

</div>

## 📖 简介

**Pencil Skills** 是一个 Agent Skills 集合，旨在赋能 AI 智能体模拟真实设计师的操作流程，将 UI 规范转化为可执行的 "Design System Components" 初始化动作。与 Stitch 的 "提示词 -> 视觉" 模式不同，Pencil 专注于 "规范 -> 动作 -> 组件落地"。

## 🏗️ 架构

技能被组织成逻辑层，以实现自主的 "规范 -> 动作" 循环。

- **`pencil-ui-designer`**: **编排器 (Orchestrator)**。负责分析需求，选择合适的设计系统，并调用相应的初始化技能。
- **`pencil-ui-design-system-*`**: **执行者 (Executor)**。负责针对特定框架（Layui, Antd, Vant 等）生成详细的组件初始化计划。

## 📦 可用技能

### 编排器
*   **`pencil-ui-designer`**: 主技能。处理 "初始化 X 框架组件" 或 "基于 X 规范设计" 的请求。

### 设计系统初始化技能 (Design System Components)
这些技能的输出是结构化的组件初始化动作（模拟 `shadcn` 风格的 `add component`）。

*   **`pencil-ui-design-system-layui`**: Layui 组件初始化。
*   **`pencil-ui-design-system-antd`**: Ant Design 组件初始化。
*   **`pencil-ui-design-system-bootstrap`**: Bootstrap 组件初始化。
*   **`pencil-ui-design-system-element`**: Element Plus 组件初始化。
*   **`pencil-ui-design-system-uview`**: uView 2.0 组件初始化。
*   **`pencil-ui-design-system-uviewpro`**: uView Pro 组件初始化。
*   **`pencil-ui-design-system-vant`**: Vant 4 组件初始化。
*   **`pencil-ui-design-system-ucharts`**: uCharts 图表组件初始化。
*   **`pencil-ui-design-system-echarts`**: ECharts 图表组件初始化。

### 原子工具
*   **`pencil-skill-creator`**: 用于生成新 Pencil Skill 的脚手架工具。

## 🚀 使用方法

在对话中提及 "Pencil" 和目标框架，例如：

- "Pencil, 为我初始化 Layui 的表格和表单组件"
- "使用 Pencil 规范流，基于 Ant Design 设计一个后台管理系统"

## 📑 文档

- [自我论证报告 (Self-Argumentation)](./SELF_ARGUMENTATION.md): 架构合理性与目标达成情况分析。
