---
name: pencil-mcp-search-all-unique-properties
description: "Search and list all unique values for specific properties (fills, fonts, spacing) across nodes in a Pencil .pen file via the search_all_unique_properties MCP tool. Use when the user explicitly mentions Pencil and needs to audit design consistency, find all colors or font sizes used, or identify inconsistent styles."
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `search_all_unique_properties`

If your client namespaces MCP tools, it may appear as `mcp__pencil__search_all_unique_properties`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.**

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You are performing a **Design Audit** **in Pencil**.
- You need to find inconsistent usage (e.g., "Where did we use the wrong font?").
- You want to list all unique values for a specific property (e.g., "List all font sizes used").

**Trigger phrases include:**
- "Search Pencil properties" (搜索 Pencil 属性)
- "Find usage of color X in Pencil" (查找 Pencil 中颜色 X 的使用)
- "Audit Pencil fonts" (审计 Pencil 字体)
- "List unique values in Pencil" (列出 Pencil 唯一值)

## Input Parameters

*   **`filePath`** (string, optional).
*   **`parents`** (array, required): IDs of parent nodes to search within.
*   **`properties`** (array, required): List of property names to search (e.g., `["fills", "typography"]`).

## How to use this skill

1.  **Identify Scope**: Determine which parent nodes (e.g., Root Frame) to audit.
2.  **Call Tool**: `search_all_unique_properties(parents=[...], properties=["fills"])`.
3.  **Analyze**: The output groups nodes by property value.

## Examples

### 1. Simple: Find All Colors
Audit all fill colors used in the document to identify inconsistencies.

```json
{
  "properties": ["fills"]
}
```

### 2. Medium: Local Font Audit
Find all font families used within a specific frame (e.g., a card or section).

```json
{
  "parents": ["frame:card-123"],
  "properties": ["fontFamily"]
}
```

### 3. Complex: Comprehensive Style Audit
Search for fills, strokes, and font sizes across multiple key sections to generate a style report.

```json
{
  "parents": ["section:header", "section:footer"],
  "properties": ["fills", "strokes", "fontSize", "fontFamily"]
}
```

## Keywords

**English keywords:**
search properties, design audit, find usage, unique values, property check, style consistency

**Chinese keywords (中文关键词):**
搜索属性, 设计审计, 查找使用, 唯一值, 属性检查, 样式一致性
