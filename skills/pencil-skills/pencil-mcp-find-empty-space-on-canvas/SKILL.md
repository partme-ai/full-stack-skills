---
name: pencil-mcp-find-empty-space-on-canvas
description: Smartly find empty canvas space. Use to automatically plan artboard placement to avoid overlap and keep the canvas organized.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `find_empty_space_on_canvas`

If your client namespaces MCP tools, it may appear as `mcp__pencil__find_empty_space_on_canvas`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.**

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You are about to insert a new Frame or Artboard **in Pencil**.
- You want to ensure the new element doesn't overlap with existing work **on the Pencil canvas**.
- You need to organize the canvas.

**Trigger phrases include:**
- "Find space for new screen in Pencil" (为 Pencil 新页面找位置)
- "Where can I draw in Pencil?" (我在 Pencil 哪里画？)
- "Pencil avoid overlap" (Pencil 避免重叠)

## Input Parameters

*   **`width`** (number, required): The width of the required space.
*   **`height`** (number, required): The height of the required space.
*   **`direction`** (string, optional): Search direction relative to node (e.g., "RIGHT", "BOTTOM").
*   **`nodeId`** (string, optional): Starting reference node. If omitted, searches around entire canvas content.
*   **`padding`** (number, optional): Minimum padding distance (default: 100).

## How to use this skill

1.  **Estimate Size**: Determine the size of the element you plan to create.
2.  **Call Tool**: `find_empty_space_on_canvas(width=..., height=...)`.
3.  **Use Result**: The tool returns `{x, y}` coordinates. Use these coordinates in your subsequent `batch_design` call to insert the Frame.

## Examples

### 1. Simple: Find Any Space
Find a spot for a small element (e.g., 100x100).
See [1-find-any.json](examples/1-find-any.json).

### 2. Medium: Place Next to Node
Find space to the right of an existing frame.
See [2-place-next-to.json](examples/2-place-next-to.json).

### 3. Complex: Organized Layout
Find space for a large dashboard with ample padding below the header section.
See [3-organized-layout.json](examples/3-organized-layout.json).

## Keywords

**English keywords:**
find space, empty canvas, layout planning, avoid overlap, next to node, smart placement

**Chinese keywords (中文关键词):**
查找空白, 空画布, 布局规划, 避免重叠, 节点旁, 智能放置
