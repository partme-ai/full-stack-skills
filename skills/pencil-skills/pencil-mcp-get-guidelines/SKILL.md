---
name: pencil-mcp-get-guidelines
description: Get design system guidelines. Use to read and understand specifications e.g. Material Design iOS HIG or custom specs before designing.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `get_guidelines`

If your client namespaces MCP tools, it may appear as `mcp__pencil__get_guidelines`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.**

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need instructions on **How** to design for a specific system **in Pencil**.
- You are generating code (`topic='code'`).
- You are building a landing page (`topic='landing-page'`).
- You need to know the `.pen` schema details.

**Trigger phrases include:**
- "Get Pencil design guidelines" (获取 Pencil 设计指南)
- "How to use Tailwind in Pencil?" (怎么在 Pencil 里用 Tailwind？)
- "Pencil coding rules" (Pencil 编码规则)
- "Pencil landing page best practices" (Pencil 落地页最佳实践)

## Input Parameters

*   **`topic`** (string, required): The topic to retrieve.
    *   `design-system`: Composing screens with components.
    *   `code`: Code generation rules.
    *   `tables`: Working with tables.
    *   `tailwind`: Tailwind CSS specs.
    *   `landing-page`: High-conversion page design.

## How to use this skill

1.  **Select Topic**: Choose the relevant topic based on user intent.
2.  **Call Tool**: `get_guidelines(topic='design-system')`.
3.  **Read & Apply**: Use the returned text as instructions for your subsequent `batch_design` calls.

## Examples

### 1. Simple: Design System Guidelines
Understand how to use the available components.

```json
{
  "topic": "design-system"
}
```

### 2. Medium: Code Handoff Guidelines
Get rules for generating code from the design, useful for "Code Handoff" tasks.

```json
{
  "topic": "code"
}
```

### 3. Complex: Landing Page Best Practices
Get specific guidelines for designing high-conversion landing pages when the user asks for a marketing site.

```json
{
  "topic": "landing-page"
}
```

## Keywords

**English keywords:**
get guidelines, design rules, best practices, coding specs, documentation, how-to

**Chinese keywords (中文关键词):**
获取指南, 设计规则, 最佳实践, 编码规范, 文档, 如何做
