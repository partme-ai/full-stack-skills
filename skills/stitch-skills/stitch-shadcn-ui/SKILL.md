---
name: stitch-shadcn-ui
description: Expert guidance for integrating and building applications with shadcn/ui. Component discovery, installation npx shadcn@latest add customization, blocks, and best practices. Use with Stitch-generated React apps for consistent, accessible UI built on Radix/Base UI and Tailwind.
allowed-tools:
  - "shadcn*:*"
  - "mcp_shadcn*"
  - "Read"
  - "Write"
  - "Bash"
  - "web_fetch"
---

# shadcn/ui Component Integration

**Constraint**: Use when the user asks about shadcn/ui, Stitch + React + shadcn, or building React UIs with shadcn components.

You are a **frontend engineer** specializing in shadcn/ui—reusable, accessible, customizable components (Radix UI or Base UI + Tailwind). You help discover, install, customize, and extend components following best practices.

## Core Principles

shadcn/ui is **not a library**—components are **copied into your project**:

- **Full ownership**: Code lives in your repo, not node_modules
- **Full customization**: Style, behavior, and structure under your control
- **No version lock-in**: Update components when you choose
- **Zero runtime overhead**: No extra bundle, only the code you add

## Component Discovery and Installation

### Browse and install

- **List components**: Use shadcn MCP `list_components` (or browse [ui.shadcn.com](https://ui.shadcn.com)).
- **Install (recommended)**:
  ```bash
  npx shadcn@latest add [component-name]
  ```
  Downloads source, installs deps, places files in `components/ui/`, updates `components.json`.
- **Manual**: Use MCP `get_component` to get source; create `components/ui/[name].tsx`; install peer deps.

### Project setup

- **New project**: `npx shadcn@latest create` (style, baseColor, RSC, etc.).
- **Existing project**: `npx shadcn@latest init` → creates `components.json` with:
  - **style**: default, new-york (classic), or newer visual styles (Vega, Nova, Maia, Lyra, Mira).
  - **baseColor**: slate, gray, zinc, neutral, stone.
  - **cssVariables**, tailwind paths, aliases, **rsc** (React Server Components), **rtl** (optional).

**Dependencies**: React 18+, Tailwind 3+, Radix UI or Base UI, class-variance-authority, clsx, tailwind-merge.

### Custom registries (optional)

For custom or third-party registries (defined in `components.json`): use MCP `get_project_registries`, `list_items_in_registries`, `view_items_in_registries`, `search_items_in_registries` to discover and install components.

## Architecture

- **File structure**: `src/components/ui/` for shadcn components; `src/components/[custom]/` for your composed components.
- **cn() utility**: All shadcn components use `cn()` (clsx + tailwind-merge) for class merging; keep `lib/utils.ts` with this helper.

## Customization

- **Theme**: Edit Tailwind config and CSS variables in `globals.css` (`:root` and `.dark`).
- **Variants**: Use `cva` for variant logic (e.g. button variant/size).
- **Wrappers**: Create wrapper components in `components/` (not `components/ui/`) that extend shadcn components.

## Blocks and Complex Components

shadcn provides **blocks** (auth, dashboard, sidebar, etc.): use MCP `list_blocks`, `get_block` to retrieve and install. Blocks are organized by category (e.g. calendar, dashboard, login, sidebar, products).

## Validation and Quality (align with official)

Before committing components:

1. **Type check**: Run `tsc --noEmit`.
2. **Lint**: Run the project linter.
3. **Accessibility**: Use tools like axe DevTools.
4. **Visual QA**: Test light and dark modes.
5. **Responsive**: Verify at different breakpoints.

## Accessibility

Components use Radix primitives: keyboard navigation, ARIA, focus management. When customizing, preserve ARIA, keyboard handlers, and focus indicators.

## Integration with Stitch

- After converting Stitch screens to React with **stitch-react-components**, add shadcn components for forms, dialogs, tables, etc. using this skill.
- Align theme (colors, spacing) with DESIGN.md from **stitch-design-md** if the project uses it.

## Troubleshooting

- **Import errors**: Check `components.json` and `tsconfig.json` paths (`@/*`).
- **Style conflicts**: Ensure Tailwind and `globals.css` are configured; match CSS variable names.
- **Missing deps**: Run `npx shadcn@latest add [component]` to auto-install; or use `get_component_metadata` for dependency list.

## Keywords

**English:** shadcn, shadcn/ui, Radix, Tailwind, React, components, blocks.  
**中文关键词：** shadcn、Radix、Tailwind、组件。

## References

- [Examples](examples/usage.md)
- [Tailwind → shadcn/ui](references/tailwind-to-shadcn.md) — When converting Stitch HTML to React + shadcn: keep Tailwind, map Stitch tokens to globals.css (--primary, --background, etc.); use shadcn components (Button, Card, Input) with className/cn().
- [shadcn/ui docs](https://ui.shadcn.com/docs)
- [Radix UI](https://www.radix-ui.com/)
