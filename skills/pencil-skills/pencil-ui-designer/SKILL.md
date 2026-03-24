---
name: pencil-ui-designer
description: The Pencil Orchestrator. Handles the flow of initializing Design System Components based on requirements.
license: Apache 2.0
---


# Pencil Designer (Master Skill)

This is the entry point for all Pencil design tasks. It acts as the **"Orchestrator Agent"** that plans and executes the component initialization workflow.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.**

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**Trigger phrases include:**
- "Pencil, initialize components for..." (Pencil, 初始化...组件)
- "Use Pencil to design system..." (使用 Pencil 设计系统...)
- "Pencil flow..." (Pencil 流...)

## Workflow

### 1) Intent Classification

Determine the target framework and components required.

### 2) Framework Routing

Route the request to the specific `pencil-ui-design-system-*` skill.

**Mapping:**
- `layui` -> `pencil-ui-design-system-layui`
- `antd`, `ant design` -> `pencil-ui-design-system-antd`
- `bootstrap` -> `pencil-ui-design-system-bootstrap`
- `element`, `element-plus` -> `pencil-ui-design-system-element`
- `uview` -> `pencil-ui-design-system-uview`
- `uview pro`, `uviewpro` -> `pencil-ui-design-system-uviewpro`
- `vant` -> `pencil-ui-design-system-vant`
- `ucharts` -> `pencil-ui-design-system-ucharts`
- `echarts` -> `pencil-ui-design-system-echarts`

### 3) Execution

Invoke the target skill to generate the "Design System Components" initialization plan.

### 4) Output

Return the structured plan (JSON/Action List) to the user.
