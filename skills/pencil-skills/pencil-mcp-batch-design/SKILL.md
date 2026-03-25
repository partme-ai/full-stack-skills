---
name: pencil-mcp-batch-design
description: "Batch execute insert, update, replace, move, and delete operations on Pencil .pen design nodes via the batch_design MCP tool. Use when the user explicitly mentions Pencil and needs to draw, insert, change, remove, or move elements on the canvas."
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `batch_design`

If your client namespaces MCP tools, it may appear as `mcp__pencil__batch_design`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., if the user just says "Draw a rectangle" in a general context, they might mean Stitch, SVG, or Mermaid).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need to **Create**, **Update**, **Delete**, or **Move** elements on the canvas.
- The user asks to "Draw", "Insert", "Change", "Remove" something **using Pencil**.
- You are executing a design plan.

**Trigger phrases include:**
- "Draw a rectangle with Pencil" (用 Pencil 画一个矩形)
- "Pencil update text content" (Pencil 更新文本内容)
- "Insert component using Pencil" (使用 Pencil 插入组件)
- "Pencil move node" (Pencil 移动节点)
- "Delete selection with Pencil" (用 Pencil 删除选区)

## Input Parameters

The `batch_design` tool accepts a JSON structure defining a list of operations.

*   **`operations`** (array, required): A list of operation objects.
    *   **Insert (`I`)**: `{ "type": "insert", "targetId": "...", "node": { ... } }`
    *   **Update (`U`)**: `{ "type": "update", "targetId": "...", "props": { ... } }`
    *   **Replace (`R`)**: `{ "type": "replace", "targetId": "...", "node": { ... } }`
    *   **Delete (`D`)**: `{ "type": "delete", "targetId": "..." }`
    *   **Move (`M`)**: `{ "type": "move", "targetId": "...", "parentId": "..." }`

**Important Notes:**
*   **Batch Limit**: Keep each call to max **25 operations**. Split larger tasks.
*   **Binding Names**: Create new binding names for every operation list. DO NOT reuse.
*   **Component Instances**:
    *   Use `type: "ref"` and `ref: "ComponentID"` to insert instances.
    *   Use `U()` with instance path to override properties.

## How to use this skill

1.  **Plan Operations**: specific exactly what needs to change.
2.  **Construct JSON**: Build the valid JSON payload matching the `.pen` schema.
3.  **Call Tool**: Invoke `batch_design`.
4.  **Handle Errors**: If an operation fails, the batch rolls back. Check the error message and retry with corrections.

## Examples

### 1. Simple: Insert Text
Insert a simple text node into the current context.
See [1-insert-text.json](examples/1-insert-text.json).

### 2. Medium: Create Layout Frame
Create an Auto-Layout Frame with a child button.
See [2-create-layout.json](examples/2-create-layout.json).

### 3. Complex: Component Instance & Overrides
Insert a component instance and override its internal properties (e.g., changing button text) in one go.
See [3-component-instance.json](examples/3-component-instance.json).

## Keywords

**English keywords:**
batch design, draw ui, update props, insert node, delete element, move layer, modify canvas

**Chinese keywords (中文关键词):**
批量设计, 绘制UI, 更新属性, 插入节点, 删除元素, 移动图层, 修改画布
