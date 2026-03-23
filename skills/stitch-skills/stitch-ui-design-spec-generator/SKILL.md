---
name: stitch-ui-design-spec-generator
description: Translates user requirements into structured Design Specs for Theme, Color, and Typography.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# Design Spec Generator

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" or when orchestrating a Stitch design task.

This skill acts as a **Creative Director**. It takes a high-level user request and outputs a structured **Design Specification**.

## Input

Input may be either:

*   **User Request** (one-shot): e.g., "A cyberpunk login page" or "A clean medical dashboard".
*   **PRD document or PRD summary**: When the user provides a PRD file path or pasted PRD content, first extract **function overview** and **page/screen list** (and any visual/theme preferences from non-functional requirements), then apply the Logic Rules below to produce the design spec. For the full PRD-driven workflow (spec-generator → framework spec → prompt-architect → MCP), see [docs/prd-to-stitch-workflow.md](../../docs/prd-to-stitch-workflow.md).

## Output Format (JSON)
The skill must produce a JSON block like this:

```json
{
  "theme": "DARK" | "LIGHT",
  "primaryColor": "Hex Code",
  "font": "Font Name",
  "roundness": "High" | "Medium" | "Low",
  "density": "COMPACT" | "COMFORTABLE" | "SPACIOUS",
  "designMode": "WIREFRAME" | "HIGH_FIDELITY",
  "styleKeywords": ["Keyword1", "Keyword2"],
  "deviceType": "MOBILE" | "TABLET" | "DESKTOP" | "SMART_WATCH"
}
```

## Logic Rules
1.  **Analyze Tone**:
    *   "Corporate/Medical/Finance" -> Clean, Blue/Grey, Low Roundness, Inter font.
    *   "Creative/Gaming" -> Dark Mode, Neon colors, High Contrast.
    *   "Lifestyle/Food" -> Warm colors, High Roundness, Serif fonts.
2.  **Determine Device**:
    *   "Dashboard/Admin" -> DESKTOP.
    *   "App/Instagram-like" -> MOBILE.
    *   "Watch Face" -> SMART_WATCH.
    *   Default to MOBILE if unspecified.
3.  **Determine Mode**:
    *   "Sketch/Blueprint/Draft" -> WIREFRAME.
    *   Default to HIGH_FIDELITY.

## Usage
Call this skill *internally* (by thinking) before creating a project or generating a prompt.
