---
name: pencil-mcp-get-style-guide
description: "Retrieve detailed style guide metadata (color palettes, typography rules, visual specs) by tags or ID from Pencil via the get_style_guide MCP tool. Use when the user explicitly mentions Pencil and needs to apply a specific visual style, retrieve theme colors and fonts, or look up a style guide by keyword tags."
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `get_style_guide`

If your client namespaces MCP tools, it may appear as `mcp__pencil__get_style_guide`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.**

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You have selected a specific style (from tags) and need its **Details** **for Pencil**.
- You need the color palette or font stack of a specific "Look and Feel".
- The user says "Use the 'Cyberpunk' style" **in Pencil**.

**Trigger phrases include:**
- "Get Pencil style details" (获取 Pencil 风格详情)
- "Apply style X in Pencil" (在 Pencil 中应用风格 X)
- "Retrieve Pencil style guide" (检索 Pencil 风格指南)

## Input Parameters

*   **`id`** (string, optional): The Style Guide ID.
*   **`tags`** (array, optional): 5-10 tags matching the desired style (from `get_style_guide_tags`).

## How to use this skill

1.  **Prerequisite**: Usually call `get_style_guide_tags` first to know what's available.
2.  **Call Tool**: `get_style_guide(tags=["Modern", "SaaS"])` or `get_style_guide(id="...")`.
3.  **Apply**: Use the returned metadata (colors, fonts) in your `batch_design` or `set_variables` calls.

## Examples

### 1. Simple: Get by ID
Retrieve a specific style guide using its unique identifier.

```json
{
  "id": "style:12345"
}
```

### 2. Medium: Search by Single Tag
Find a style guide that matches a specific keyword (e.g., "Modern").

```json
{
  "tags": ["Modern"]
}
```

### 3. Complex: Multi-Tag Search
Find a style guide that fits a complex criteria (e.g., "Dark" mode "SaaS" dashboard).

```json
{
  "tags": ["Dark", "SaaS", "Dashboard"]
}
```

## Keywords

**English keywords:**
get style guide, style details, visual specs, color palette, font rules, apply theme

**Chinese keywords (中文关键词):**
获取风格指南, 风格详情, 视觉规范, 调色板, 字体规则, 应用主题
