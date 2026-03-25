---
name: pencil-mcp-get-variables
description: "Read design token variables (colors, fonts, spacing) from a Pencil .pen file via the get_variables MCP tool. Use when the user explicitly mentions Pencil and needs to list design tokens, check the current theme, or retrieve variable IDs for use in batch_design operations."
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `get_variables`

If your client namespaces MCP tools, it may appear as `mcp__pencil__get_variables`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., "Get variables" might refer to environment variables or code variables).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need to know the available Design Tokens (Colors, Typography, Spacing) **in Pencil**.
- You want to use semantic names (e.g., `primary-color`) instead of hardcoded hex codes.
- You are checking the current theme.

**Trigger phrases include:**
- "Get Pencil variables" (获取 Pencil 变量)
- "Read Pencil design tokens" (读取 Pencil 设计令牌)
- "Check Pencil colors" (检查 Pencil 颜色)
- "List Pencil theme values" (列出 Pencil 主题值)

## Input Parameters

*   **`filePath`** (string, optional): Path to the `.pen` file.

## How to use this skill

1.  **Call Tool**: `get_variables()`.
2.  **Analyze Output**: The result is a list/map of variable definitions.
3.  **Apply**: Use the variable IDs or names in `batch_design` operations (e.g., `fill: { type: "var", id: "var_123" }`).

## Examples

### 1. Simple: Get All Variables
Retrieve all variables defined in the current document.

```json
{}
```

### 2. Medium: Get from Specific File
Read variables from a different design file (e.g., a shared library).

```json
{
  "filePath": "/Users/design/system/tokens.pen"
}
```

### 3. Complex: Theme Audit (Conceptual)
Same as simple, but used when auditing themes.

```json
{}
```

## Keywords

**English keywords:**
get variables, read tokens, design system, theme values, color palette, typography tokens

**Chinese keywords (中文关键词):**
获取变量, 读取令牌, 设计系统, 主题值, 调色板, 字体令牌
