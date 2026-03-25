---
name: pencil-ui-designer
description: "Orchestrates Pencil design system initialization by routing framework requests to the correct pencil-ui-design-system-* skill. Use when the user explicitly mentions Pencil and wants to initialize a design system (antd, Bootstrap, Element Plus, Layui, uView, Vant, uCharts, ECharts), set up component libraries, or create design tokens in a .pen file."
license: Apache 2.0
---

# Pencil Designer (Master Skill)

This is the entry point for all Pencil design system initialization tasks. It acts as the orchestrator that classifies the target framework, routes to the correct `pencil-ui-design-system-*` skill, and returns the structured initialization plan.

## When to use this skill

Use this skill when:
- The user explicitly mentions "Pencil" and wants to initialize a design system (antd, Bootstrap, Element Plus, Layui, uView, Vant, uCharts, ECharts)
- The user says "Pencil, initialize components for [framework]" or "Use Pencil to set up [framework] design system"
- The conversation context is about Pencil design tasks requiring framework-specific component setup

**Do NOT use this skill** if the user does not explicitly mention "Pencil" or if the request is about general design tasks unrelated to Pencil .pen files.

## Workflow

### 1) Intent Classification

Parse the user request to determine:
- **Target framework**: Which UI library or chart library (antd, Bootstrap, Element Plus, etc.)
- **Components scope**: Full initialization or specific component categories

### 2) Framework Routing

Route the request to the specific `pencil-ui-design-system-*` skill:

| User mentions | Routes to |
|---|---|
| `layui`, `layui-vue` | `pencil-ui-design-system-layui` |
| `antd`, `ant design` | `pencil-ui-design-system-antd` |
| `bootstrap` | `pencil-ui-design-system-bootstrap` |
| `element`, `element-plus` | `pencil-ui-design-system-element` |
| `uview` (2.x) | `pencil-ui-design-system-uview` |
| `uview pro`, `uviewpro` | `pencil-ui-design-system-uviewpro` |
| `vant`, `vant 4` | `pencil-ui-design-system-vant` |
| `ucharts`, `qiun-data-charts` | `pencil-ui-design-system-ucharts` |
| `echarts` | `pencil-ui-design-system-echarts` |

### 3) Execution

Invoke the target skill which generates a PENCIL_PLAN: a sequence of Pencil MCP tool calls (`open_document` -> `set_variables` -> `batch_design` -> `get_screenshot`).

### 4) Output

Return the structured plan (JSON/Action List) to the user for execution or approval.
