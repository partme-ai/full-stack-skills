---
name: stitch-mcp-generate-screen-from-text
description: Generates high-fidelity UI screens or wireframes from text descriptions. The core Text-to-UI engine.
license: Complete terms in LICENSE.txt
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


## Tools

This skill is designed to call the Stitch MCP tool:

*   `generate_screen_from_text`

If your client namespaces MCP tools, it may appear as `mcp__<serverName>__generate_screen_from_text`.

## When to use this skill

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Stitch".**

**ALWAYS use this skill when the user:**
- Describes a UI interface **and asks Stitch to generate it**.
- Asks to "Design", "Generate", "Create", or "Make" a screen **using Stitch**.
- Provides specific visual requirements ("Dark mode", "Blue button") for a Stitch generation.
- Wants to visualize a wireframe or concept **via Stitch**.
- Is in the **Step 5** of the `stitch-ui-designer` SOP workflow.

**Trigger phrases include:**
- "Use Stitch to design a screen" (用 Stitch 设计一个页面)
- "Stitch generate UI" (Stitch 生成 UI)
- "Draw a login page with Stitch" (用 Stitch 画一个登录页)

## Input Parameters

The skill expects you to extract the following information from the user request:

*   **`projectId`** (required): The numeric Project ID. **Format**: Pure ID (e.g., `37803...`), **NO** `projects/` prefix.
*   **`prompt`** (required): The structured text description of the screen (see "Constructing the Prompt" below).
*   **`deviceType`** (optional): The target device.
    *   Values: `MOBILE` (default), `DESKTOP`, `TABLET`, `SMART_WATCH`.
*   **`modelId`** (optional): The model to use.
    *   Values: `GEMINI_3_PRO` (Recommended for quality), `GEMINI_3_FLASH` (Speed).

## How to use this skill

### 0. Call the MCP Tool

Invoke `generate_screen_from_text` with:

*   `projectId` (pure numeric string, no `projects/`)
*   `prompt`
*   `deviceType` (optional)
*   `modelId` (optional)

### 1. Constructing the Prompt (The Art of Prompting)
The `prompt` argument is the most critical factor for quality. Do not just pass the user's raw input. You **MUST** enrich it using the **Structure Strategy**:

`[Device] [Mode] [Screen Type]. [Style]. [Layout]. [Components].`

*   **Context**: "Mobile High-Fidelity login screen."
*   **Style**: "Cyberpunk aesthetic. Dark mode. Neon blue accents."
*   **Layout**: "Center-aligned vertical stack."
*   **Components**: "Glitch-effect Logo. Input fields with glowing borders. Primary 'Jack In' button."

### 2. Choosing Device Type (`deviceType`)
*   `MOBILE` (Default): Vertical layouts, ~375px width. Best for consumer apps.
*   `DESKTOP`: Horizontal layouts, ~1440px width. Best for SaaS, Dashboards, Landing Pages.
*   `TABLET`: Hybrid layouts.
*   `SMART_WATCH`: Tiny, compact layouts.

### 3. Choosing Model (`modelId`)
*   `GEMINI_3_PRO`: **Recommended**. High intelligence, better instruction following, superior aesthetics. Use for all complex/final designs.
*   `GEMINI_3_FLASH`: Faster, lower cost. Good for simple wireframes or rapid iteration.

## Best Practices

1.  **Detailed Components**: Don't just say "Form". Say "Form with Email, Password, and Eye toggle icon".
2.  **Color Precision**: Mention specific colors (e.g., "Emerald Green", "#FF5733") if the user specifies them.
3.  **Content Realism**: Ask for realistic text placeholders (e.g., "Welcome back, Alice" instead of "Lorem Ipsum").
4.  **Device Alignment**: Ensure the `prompt` description matches the `deviceType` (e.g., don't ask for a "Sidebar" on `MOBILE`).
5.  **No Code Generation**: This skill generates **Visual Designs**, not implementation code. Do not confuse with coding skills (like `uniappx-project-creator`).

## Output Handling

`generate_screen_from_text` returns session info (e.g., `sessionId` and `outputComponents`). It may not return a screenshot directly.

After the generation completes, retrieve the resulting screen(s) via:

1.  `list_screens` with `projectId` in the format `projects/{id}`.
2.  `get_screen` with the selected `screenId` to fetch screenshot / html assets.

## Keywords

**English keywords:**
generate screen, design ui, create interface, make page, draw wireframe, text to ui, ui generation, stitch gen, mobile design, desktop design, dashboard, login, prompt engineering

**Chinese keywords (中文关键词):**
生成页面, 设计UI, 创建界面, 画图, 制作网页, 文本生成UI, 界面设计, 移动端设计, 桌面端设计, 仪表盘, 登录页, 线框图, 生成代码

## References

- [Examples](examples/usage.md)
- [Desktop Dashboard Example](examples/desktop_dashboard.md)
- [Mobile App Example](examples/mobile_app.md)
- [Wireframe Example](examples/wireframe.md)
