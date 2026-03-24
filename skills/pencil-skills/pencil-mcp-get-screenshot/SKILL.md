---
name: pencil-mcp-get-screenshot
description: Get node visual screenshot. Visual Verification. Use to capture screenshots after operations to verify if the design meets expectations.
license: Complete terms in LICENSE.txt
---


## Tools

This skill is designed to call the Pencil MCP tool:

*   `get_screenshot`

If your client namespaces MCP tools, it may appear as `mcp__pencil__get_screenshot`.

## When to use this skill

### Intent Recognition (CRITICAL)
Even if a trigger phrase matches, you must **verify the user's intent**:
1.  Is the user explicitly asking to use "Pencil"?
2.  Is the current conversation context clearly about "Pencil" design tasks?

**If the answer is NO, do NOT use this skill.** (e.g., "Get screenshot" might refer to a browser screenshot via Puppeteer).

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Pencil".**

**ALWAYS use this skill when:**
- You have completed a design operation (`batch_design`) and need to **verify** the result **in Pencil**.
- The user asks to "Show me" or "Take a look" **at the Pencil design**.
- You need to check for visual bugs (text overflow, alignment, contrast).
- This is the **Verify** step in the Design Loop.

**Trigger phrases include:**
- "Get Pencil screenshot" (获取 Pencil 截图)
- "Pencil visual check" (Pencil 视觉检查)
- "Verify Pencil design" (验证 Pencil 设计)
- "Show me the button in Pencil" (给我看 Pencil 里的那个按钮)

## Input Parameters

*   **`filePath`** (string, optional): Path to access a specific `.pen` file.
*   **`nodeId`** (string, required): The ID of the node to screenshot.

## How to use this skill

1.  **Identify Target**: Get the `nodeId` of the element you just modified or created.
2.  **Call Tool**: `get_screenshot(nodeId='...')`.
3.  **Analyze Result**:
    *   The tool returns an image URL or data.
    *   **CRITICAL**: You must "look" at the image (if capabilities allow) or present it to the user for feedback.
    *   Check for: Alignment, Spacing, Text Truncation, Color correctness.

## Examples

### 1. Simple: Node Screenshot
Get a visual verification of a single element.
See [1-node-screenshot.json](examples/1-node-screenshot.json).

### 2. Medium: Frame Verification
Screenshot a whole frame to check layout and composition.
See [2-frame-verification.json](examples/2-frame-verification.json).

### 3. Complex: Design System Check
Screenshot a component master to ensure the design system update looks correct.
See [3-component-check.json](examples/3-component-check.json).

## Keywords

**English keywords:**
get screenshot, visual verification, check design, view node, render image, visual audit

**Chinese keywords (中文关键词):**
获取截图, 视觉验证, 检查设计, 查看节点, 渲染图片, 视觉审计
