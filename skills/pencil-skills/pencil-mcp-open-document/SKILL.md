---
name: pencil-mcp-open-document
description: Open or create a design document. Use when you need to initialize design tasks, create new files, or switch to specific designs.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `open_document`

If your client namespaces MCP tools, it may appear as `mcp__pencil__open_document`. Full parameter details: [docs/pencil-mcp-tools.md](../../docs/pencil-mcp-tools.md).

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., "Open file" might refer to reading a code file, not a .pen design).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- The user asks to create a **new** design document **in Pencil**.
- The user provides a file path and asks to open it **with Pencil**.
- You need to switch the active editor to a specific `.pen` file.

**Trigger phrases include:**
- "Create a new document in Pencil" (在 Pencil 中新建文档)
- "Pencil open file..." (Pencil 打开文件...)
- "Start a new design with Pencil" (用 Pencil 开始新设计)
- "Pencil switch to [path]" (Pencil 切换到 [路径])

## Input Parameters

*   **`filePathOrTemplate`** (string, required):
    *   Value: `'new'` to create a fresh, empty document.
    *   Value: Absolute file path (e.g., `/path/to/design.pen`) to open an existing file.
    *   **Note**: No other template names are valid.

## How to use this skill

1.  **Analyze Request**: Determine if it's a "New" or "Open" request.
2.  **Call Tool**:
    *   For new: `open_document(filePathOrTemplate='new')`
    *   For existing: `open_document(filePathOrTemplate='/path/to/file.pen')`

## Examples

- **New document**: `open_document(filePathOrTemplate='new')` — initialize a fresh canvas.
- **Open file**: `open_document(filePathOrTemplate='/path/to/design.pen')` — open existing .pen file.
- **Switch context**: Same as open file; use when switching to another .pen in the same session.

## Keywords

**English keywords:**
open document, create file, new design, load file, switch document, initialize canvas

**Chinese keywords (中文关键词):**
打开文档, 创建文件, 新建设计, 加载文件, 切换文档, 初始化画布

## References

- [Pencil MCP 工具说明](../../docs/pencil-mcp-tools.md) — open_document 等方法的完整参数。
