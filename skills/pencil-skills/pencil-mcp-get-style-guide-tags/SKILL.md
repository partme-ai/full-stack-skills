---
name: pencil-mcp-get-style-guide-tags
description: Explore design style tags. Use to get design inspiration, such as 'Modern', 'Dark Mode', 'SaaS' directions.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `get_style_guide_tags`

If your client namespaces MCP tools, it may appear as `mcp__pencil__get_style_guide_tags`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.**

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need **Inspiration** **for a Pencil design**.
- The user gives vague style requirements ("Make it cool", "Modern look") **in Pencil**.
- You are exploring design directions.
- **Prerequisite** for `get_style_guide`.

**Trigger phrases include:**
- "Get Pencil style tags" (获取 Pencil 风格标签)
- "Explore Pencil styles" (探索 Pencil 风格)
- "Pencil inspiration" (Pencil 灵感)
- "What styles are available in Pencil?" (Pencil 有什么风格可用？)

## Input Parameters

*   **`id`** (string, optional): Specific style guide ID.
*   **`tags`** (array, optional): Filter tags.

## How to use this skill

1.  **Call Tool**: `get_style_guide_tags()`.
2.  **Analyze**: Look at the returned tags (e.g., "Minimalist", "Cyberpunk", "Corporate").
3.  **Next Step**: Use the interesting tags in `get_style_guide`.

## Examples

### 1. Simple: Explore All Tags
Get a list of all available style tags to find inspiration.

```json
{}
```

### 2. Medium: Get Tags for Specific Style
If a style ID is known (e.g., from a previous session), get its associated tags to find similar styles.

```json
{
  "id": "style:minimalist-dark"
}
```

### 3. Complex: Filter Tags (Conceptual)
Get tags that are relevant to a specific design context (if supported by the backend logic, otherwise same as Simple).

```json
{}
```

## Keywords

**English keywords:**
style tags, design inspiration, explore trends, visual direction, aesthetic tags, mood board

**Chinese keywords (中文关键词):**
风格标签, 设计灵感, 探索趋势, 视觉方向, 美学标签, 情绪板
