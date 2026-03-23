---
name: pencil-mcp-get-editor-state
description: Get current design environment context. Use when you need to understand what is currently selected, canvas position, and environment state before any task.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `get_editor_state`

If your client namespaces MCP tools, it may appear as `mcp__pencil__get_editor_state`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., "What is selected?" might refer to selected text in the IDE, not the Pencil canvas).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need to know what the user has currently selected on the canvas.
- You need to check the active document path.
- You are starting a new design task and need to orient yourself.
- The user asks "What am I looking at?" or "Get context" **in Pencil**.

**Trigger phrases include:**
- "Get Pencil editor state" (获取 Pencil 编辑器状态)
- "Check current selection in Pencil" (检查 Pencil 当前选区)
- "What is selected in Pencil?" (Pencil 中选中了什么？)
- "Where am I on the Pencil canvas?" (我在 Pencil 画布哪里？)

## Input Parameters

*   **`include_schema`** (boolean, optional): 
    *   Set to `true` if you want the `.pen` file schema to be included. 
    *   If you are already aware of the schema, set to `false` (default) to save context.

## How to use this skill

1.  **Call the MCP Tool**: Invoke `get_editor_state`.
2.  **Analyze Output**:
    *   Check `selection`: List of selected node IDs.
    *   Check `activePageId`: Current page ID.
    *   Check `filePath`: Path of the current document.

## Examples

### 1. Simple: Basic State Check
Get the current state to understand what the user is looking at.
See [1-basic-check.json](examples/1-basic-check.json).

### 2. Medium: State with Schema
Get state including the .pen file schema to understand the document structure definitions.
See [2-with-schema.json](examples/2-with-schema.json).

### 3. Complex: State Verification (Explicit)
Explicitly checking state during a multi-step workflow where schema is already known.
See [3-explicit-check.json](examples/3-explicit-check.json).

## Keywords

**English keywords:**
get state, editor context, current selection, active document, canvas position, check environment

**Chinese keywords (中文关键词):**
获取状态, 编辑器上下文, 当前选区, 选中节点, 画布位置, 环境检查
