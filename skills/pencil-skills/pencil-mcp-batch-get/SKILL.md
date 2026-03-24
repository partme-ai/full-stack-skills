---
name: pencil-mcp-batch-get
description: Batch search and read node information. The Agent's 'Eyes'. Use to find specific components e.g. all nodes named 'Button' or get child structure within a container.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `batch_get`

If your client namespaces MCP tools, it may appear as `mcp__pencil__batch_get`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., if the user just says "Find the button" in a general context, they might mean simple text search or other tools).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You need to **Find** specific nodes by name or ID.
- You need to **Read** the properties of specific nodes.
- You need to inspect the children of a Frame.
- The user asks to "Find the button", "Get properties of X" **in Pencil**.

**Trigger phrases include:**
- "Pencil find all buttons" (Pencil 查找所有按钮)
- "Get node info with Pencil" (用 Pencil 获取节点信息)
- "Read properties using Pencil" (使用 Pencil 读取属性)
- "Pencil search components" (Pencil 搜索组件)

## Input Parameters

*   **`filePath`** (string, optional): Path to file.
*   **`patterns`** (array, optional): Search patterns (e.g., `["name=Button"]`).
*   **`nodeIds`** (array, optional): Specific IDs to read.
*   **`searchDepth`** (integer, optional): Depth for search.
*   **`readDepth`** (integer, optional): Depth for reading children structure. **Keep low (<3)**.
*   **`includePathGeometry`** (boolean, optional): Include vector path data.
*   **`resolveVariables`** (boolean, optional): Return computed values instead of variable refs.

## How to use this skill

1.  **Combine Requests**: If you need to search AND read by ID, do it in ONE call.
2.  **Smart Traversal**:
    *   Start with top-level or known IDs.
    *   If you see `...` (truncated children), make a new call with those specific child IDs.
3.  **Design Systems**: To list available components, search for reusable nodes inside the design system frame.

## Examples

### 1. Simple: Get Root Children
Get the top-level nodes of the document to understand the general structure.
See [1-get-root.json](examples/1-get-root.json).

### 2. Medium: Search by Name
Find all nodes that contain "Button" in their name.
See [2-search-name.json](examples/2-search-name.json).

### 3. Complex: Detailed Search
Search for specific nodes by ID and name pattern, resolving variables to see actual values, and getting full geometry.
See [3-detailed-search.json](examples/3-detailed-search.json).

## Keywords

**English keywords:**
batch get, search nodes, find elements, read properties, inspect structure, get components

**Chinese keywords (中文关键词):**
批量获取, 搜索节点, 查找元素, 读取属性, 检查结构, 获取组件
