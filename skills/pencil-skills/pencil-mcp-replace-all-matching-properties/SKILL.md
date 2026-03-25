---
name: pencil-mcp-replace-all-matching-properties
description: "Batch replace matching style properties (colors, fonts, sizes) across nodes in a Pencil .pen file via the replace_all_matching_properties MCP tool. Use when the user explicitly mentions Pencil and needs to globally swap colors, update font families, migrate to a new brand style, or batch-adjust spacing across frames."
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `replace_all_matching_properties`

If your client namespaces MCP tools, it may appear as `mcp__pencil__replace_all_matching_properties`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., "Replace properties" might refer to refactoring code).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need to make **Global Changes** or **Batch Updates** **in Pencil**.
- The user asks to "Change all X to Y".
- You are refactoring styles (e.g., "Replace hex codes with variables").

**Trigger phrases include:**
- "Replace Pencil properties" (替换 Pencil 属性)
- "Change all colors in Pencil" (修改 Pencil 所有颜色)
- "Batch update Pencil fonts" (批量更新 Pencil 字体)
- "Pencil global style replace" (Pencil 全局样式替换)

## Input Parameters

*   **`filePath`** (string, optional).
*   **`parents`** (array, required): IDs of parent nodes to search within.
*   **`properties`** (array, required): List of replacement rules.
    *   Each rule defines the `property`, `match` (value to find), and `replace` (new value).

## How to use this skill

1.  **Define Rules**: "Find `fills: #FF0000`, Replace with `fills: #0000FF`".
2.  **Call Tool**: `replace_all_matching_properties(...)`.
3.  **Verify**: Call `get_screenshot` to verify the global change.

## Examples

### 1. Simple: Global Color Swap
Replace all instances of Red (#FF0000) with Blue (#0000FF) across the entire document.

```json
{
  "properties": [
    {
      "property": "fills",
      "from": { "color": "#FF0000" },
      "to": { "color": "#0000FF" }
    }
  ]
}
```

### 2. Medium: Local Font Update
Change the font family from "Arial" to "Roboto" only within the Footer section.

```json
{
  "parents": ["frame:footer"],
  "properties": [
    {
      "property": "fontFamily",
      "from": "Arial",
      "to": "Roboto"
    }
  ]
}
```

### 3. Complex: Batch Style Migration
Update multiple properties (color and font) simultaneously across several frames to migrate to a new brand style.

```json
{
  "parents": ["frame:home", "frame:profile"],
  "properties": [
    {
      "property": "fills",
      "from": { "color": "#OLD_COLOR" },
      "to": { "color": "#NEW_COLOR" }
    },
    {
      "property": "fontSize",
      "from": 12,
      "to": 14
    }
  ]
}
```

## Keywords

**English keywords:**
replace properties, batch update, global change, style refactor, bulk edit, theme switch

**Chinese keywords (中文关键词):**
替换属性, 批量更新, 全局修改, 样式重构, 批量编辑, 主题切换
