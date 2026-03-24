# stitch-design-md Usage

## When to use

- User has an existing Stitch project and wants a **DESIGN.md** so new screens stay consistent.
- Preparing for **stitch-loop** or multi-page generation: DESIGN.md Section 6 is copied into each baton prompt.

## Steps

1. **Get project and screen IDs** using Stitch MCP (or skills `stitch-mcp-list-projects`, `stitch-mcp-list-screens`).
2. **Fetch screen and project metadata** with `stitch-mcp-get-screen` and `stitch-mcp-get-project`; download HTML/screenshot from returned URLs.
3. **Analyze** colors, typography, components, layout from HTML and screenshot.
4. **Write DESIGN.md** in the project root following the skill’s output format (Visual Theme, Color Palette, Typography, Component Stylings, Layout, Section 6 for Stitch prompts).
5. **Optional:** Use with `stitch-ui-prompt-architect` (inject Section 6 into prompts) and `stitch-loop` (baton file includes DESIGN SYSTEM block from DESIGN.md).

## Example prompt

> "Analyze my Stitch project [Project Name] and generate a DESIGN.md from the Home screen so I can generate more pages with the same look and feel."
