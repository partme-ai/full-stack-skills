# stitch-shadcn-ui Usage

## When to use

- User wants to **add or customize shadcn/ui** in a React project (including Stitch→React projects).
- User asks how to discover, install, or theme shadcn components.

## Common tasks

1. **Init**: `npx shadcn@latest init` (existing project) or `npx shadcn@latest create` (new).
2. **Add component**: `npx shadcn@latest add button card dialog`.
3. **Theme**: Edit `globals.css` and Tailwind config; use CSS variables and `.dark` for dark mode.
4. **Blocks**: Use MCP list_blocks / get_block to add auth, dashboard, sidebar blocks.

## With Stitch

Use **stitch-react-components** to get React from Stitch screens; then use this skill to add forms, modals, tables (shadcn) and keep DESIGN.md alignment if present.
