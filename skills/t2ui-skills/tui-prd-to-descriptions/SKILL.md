---
name: tui-prd-to-descriptions
description: "Generate and render a pixel-precise ASCII TUI PRD to Descriptions component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a PRD to descriptions in a terminal UI, text-based interface, or Pencil MCP project."
---

# PRD 界面 → 多格式描述

将 **PRD 中的界面/屏幕描述** 转化为三种可交付物，供文档补充与下游 stitch-skills、pencil-skills 使用。本技能**只产出描述文本**，不调用 Stitch MCP 或 Pencil MCP。

## 何时使用

- 用户提供 PRD 文档或 PRD 界面章节，需要同时得到：ASCII 界面（补充 PRD）、Stitch 可识别的提示词、Pencil 可执行计划。
- 需要明确「PRD 界面 → 多格式」的产出结构，便于与 stitch-skills、pencil-skills 流水线衔接。

## 输入

- **PRD 文档** 或 **PRD 中的界面相关段落**：功能概述、页面/屏幕列表、详细功能需求中的界面说明、非功能需求中的视觉/主题偏好。
- 可选：目标框架或设计说明摘要（如 uView Pro、Element Plus），用于生成更贴合的 Stitch 与 Pencil 描述。

## 输出（三种块，均需产出）

### 1. TUI_RENDER（ASCII 界面）

- 等宽字符绘制的界面示意，可多屏，每屏可标注名称（如「登录页」「首页」）。
- 用途：补充 PRD 的「界面原型关联」或附录；不驱动 Stitch/Pencil 执行。
- 约定：无 TAB；每行宽度一致（如 widthCols=70）。

### 2. STITCH_PROMPT（Stitch 可执行描述）

- 分段结构，与 stitch-skills 的 [prd-to-stitch-workflow](https://github.com/partme-ai/stitch-skills/blob/main/docs/prd-to-stitch-workflow.md) 兼容：`[Context]`、`[Layout]`、`[Components]`、`[Content]`。
- 可直接或经微调后作为 `generate_screen_from_text` 的 prompt，或作为 stitch-ui-prompt-architect 的输入。
- 下游：由 **stitch-skills** 消费并执行 Stitch MCP；本技能不调用。

### 3. PENCIL_PLAN 或 PENCIL_BATCH_DESIGN（Pencil 可执行描述）

- **PENCIL_PLAN**：步骤序列，每步含工具名（如 `mcp__pencil__open_document`、`mcp__pencil__batch_design`）、意图、关键参数；与 pencil-skills 的 pencil-ui-design-spec-generator 输出格式一致。
- **PENCIL_BATCH_DESIGN**：可直接用于 Pencil MCP `batch_design` 的 operations（每批 ≤25 操作）。
- 下游：由 **pencil-skills** 或 Agent 按步执行 Pencil MCP；本技能不调用。

## 逻辑规则

1. **解析 PRD**：提取页面/屏幕列表、每屏功能与主要组件、交互要点、视觉/主题偏好。
2. **ASCII**：按屏或按区域生成线框式 ASCII，保持等宽与可读性。
3. **Stitch 描述**：按屏生成 Stitch 分段提示，包含设备类型、布局、组件与内容描述，便于 stitch-skills 直接使用。
4. **Pencil 描述**：按「后续界面设计」需求生成 PENCIL_PLAN 或 PENCIL_BATCH_DESIGN 片段，与 pencil-skills 的 PENCIL_PLAN 格式一致。

## 边界（无能力交叉）

- **不调用** Stitch MCP 或 Pencil MCP。
- Stitch 实际绘制由 **stitch-skills** 完成；Pencil 实际绘制由 **pencil-skills** 完成。本技能仅产出描述语言。

## 参考

- 边界与三种输出格式：[docs/boundary-and-outputs.md](../../docs/boundary-and-outputs.md)
- PRD 界面→多格式约定：[docs/prd-interface-to-multi-format.md](../../docs/prd-interface-to-multi-format.md)
- 组件词汇表：本库 `tui-*` 组件技能（tui-button、tui-input 等）可在组合界面时引用其语义与规范。
