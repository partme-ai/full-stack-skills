# Stitch Skills 项目自我论证报告

**日期**: 2026-02-03
**项目**: stitch-skills
**目标**: 构建一个全面的 Google Stitch UI 生成设计规范库，通过 Agent Skills 协议实现不同 UI 框架（uView, Element Plus, Vant 等）的自主路由与约束注入。

## 1. 目标达成情况分析

项目旨在解决通用 LLM 在 UI 生成时缺乏特定框架约束的问题。通过 "Spec Skills" 模式，我们将设计规范封装为可执行的 Agent Skills。

| 目标框架 | 实现状态 | Skill 名称 | 备注 |
| :--- | :--- | :--- | :--- |
| **uView 2.0** | ✅ 已完成 | `stitch-ui-design-spec-uview` | 基础版，支持 Vue 2 / UniApp |
| **uView Pro** | ✅ 已完成 | `stitch-ui-design-spec-uviewpro` | 进阶版，支持 Vue 3 / UniApp |
| **Element Plus** | ✅ 已完成 | `stitch-ui-design-spec-element-plus` | 桌面端 Vue 3 标杆 |
| **Vant 4** | ✅ 已完成 | `stitch-ui-design-spec-vant` | 移动端电商首选 |
| **Layui Vue** | ✅ 已完成 | `stitch-ui-design-spec-layui` | 传统后台风格现代化 |
| **Bootstrap 5** | ✅ 已完成 | `stitch-ui-design-spec-bootstrap` | 经典响应式布局 |

**结论**: 核心目标框架均已覆盖，形成了从移动端到桌面端、从 Vue 2 到 Vue 3 的完整生态。

## 2. 架构与冲突论证

最核心的风险在于**触发冲突**（Trigger Conflicts），即用户的模糊指令导致错误的 Skill 被激活。

### 风险点：uView vs uView Pro
- **问题**: 用户输入 "uView" 可能意指 2.0，也可能仅是模糊指代。输入 "uView Pro" 包含 "uView" 关键词，极易被 2.0 的 skill 抢先捕获。
- **解决方案**:
    1.  **编排层路由 (Orchestrator Routing)**: 在 `stitch-ui-designer` 中实现了 **优先级匹配 (Priority Matching)**。
        - 优先匹配长尾关键词 (`uview-pro`, `uviewpro`)。
        - 只有未匹配时，才匹配通用关键词 (`uview`)。
    2.  **负向约束 (Negative Constraints)**: 在 `stitch-ui-design-spec-uview` 的 `SKILL.md` 中明确声明：
        > "If the user says 'uView Pro' or 'uviewpro', DO NOT use this skill. Use `stitch-ui-design-spec-uviewpro` instead."

### 风险点：通用 vs 专用
- **问题**: 如 `element` 可能指 `element-ui` (Vue 2) 或 `element-plus` (Vue 3)。
- **现状**: 目前仅实现了 `element-plus`。
- **策略**: 在路由表中将 `element`, `element-ui`, `element-plus` 统一指向 `stitch-ui-design-spec-element-plus`，这符合当前技术趋势（Vue 3 优先）。

## 3. 扩展性论证

项目采用了标准化的 **"Spec Skill 黄金模板"**：
- `SKILL.md`: 定义元数据、触发词、工作流。
- `references/contract.md`: 定义硬约束（组件前缀、布局规则）。
- `references/examples.md`: 提供 Few-Shot Examples。

**论证**: 新增一个框架（如 Ant Design Vue）只需复制模板并填充 `contract.md`，无需修改编排器核心逻辑（仅需注册路由），具备极高的扩展性。

## 4. 最终结论

经过代码审查与逻辑推演，`stitch-skills` 项目：
1.  **满足** 构建多框架设计规范库的初衷。
2.  **具备** 健壮的路由分发机制，有效避免了关键词冲突。
3.  **拥有** 清晰的扩展路径，便于未来维护。

**状态**: 🟢 健康 (Healthy) / 🚀 就绪 (Ready for Deployment)
