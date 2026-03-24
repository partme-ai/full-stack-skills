---
name: stitch-react-components
description: Convert Stitch designs into modular Vite/React components with validation and design token consistency. Uses Stitch MCP get_screen to retrieve design JSON and HTML; supports high-reliability fetch via scripts; enforces modular structure, type safety, and theme-mapped Tailwind.
allowed-tools:
  - "stitch*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
---


# Stitch to React Components

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" and converting Stitch screens to React (Vite/React, TypeScript).

You are a **frontend engineer** turning Stitch designs into clean, modular React code. Use Stitch MCP (or **stitch-mcp-get-screen**) to retrieve screen metadata and HTML; use scripts and resources in this skill for reliable fetch and quality checks.

## Prerequisites

- Stitch MCP Server (https://stitch.withgoogle.com/docs/mcp/guide/)
- Node.js and npm (for Vite/React project and optional validation)
- Stitch project and screen IDs — **two ways**: (1) From a **Stitch design URL**: parse **projectId** (path) and **screenId** (`node-id` query). (2) When no URL or when browsing: use **stitch-mcp-list-projects** and **stitch-mcp-list-screens** to discover and obtain IDs.

## Retrieval and Networking

1. **Discover Stitch MCP prefix**: Run `list_tools` to find the prefix (e.g. `mcp_stitch__stitch:`).
2. **Fetch screen metadata**: Call `[prefix]:get_screen` with `projectId` and `screenId` (numeric IDs) to get design JSON, `htmlCode.downloadUrl`, `screenshot.downloadUrl`, dimensions, deviceType.
3. **High-reliability HTML download**: AI fetch tools can fail on Google Cloud Storage URLs. Use Bash to run the skill script:
   ```bash
   bash scripts/fetch-stitch.sh "<htmlCode.downloadUrl>" "temp/source.html"
   ```
   This uses `curl -L` for redirects and TLS. Ensure the URL is quoted.
4. **Visual reference**: Use `screenshot.downloadUrl` to confirm layout and details.

## Architectural Rules

- **Modular components**: Split the design into separate files; avoid one giant file.
- **Logic isolation**: Put event handlers and business logic in `src/hooks/`.
- **Data decoupling**: Move static text, image URLs, and lists into `src/data/mockData.ts`.
- **Type safety**: Every component must have a `Readonly` TypeScript interface `[ComponentName]Props`.
- **Project-specific**: Omit third-party license headers from generated components.
- **Style mapping**: Extract `tailwind.config` from HTML `<head>`; sync with `resources/style-guide.json` if present; use theme-mapped Tailwind classes instead of raw hex.

## Execution Steps

1. **Environment**: If the project has no `node_modules`, run `npm install` so validation (if used) works.
2. **Data layer**: Create `src/data/mockData.ts` from the design content.
3. **Component drafting**: Use `resources/component-template.tsx` as base; replace all `StitchComponent` with the real component name.
4. **Wiring**: Update the app entry (e.g. `App.tsx`) to render the new components.
5. **Quality check**: Run `npm run validate <file_path>` if the project has a validate script; verify against `resources/architecture-checklist.md`; run `npm run dev` to confirm visually.

## Integration with This Repo

- **Get screen**: Use **stitch-mcp-get-screen** (or MCP `get_screen`) with projectId and screenId. Obtain IDs either by parsing a **Stitch design URL** or by using **stitch-mcp-list-projects** and **stitch-mcp-list-screens** when no URL or when the user needs to browse/select.
- **Design system**: If the project has DESIGN.md (from **stitch-design-md**), align colors and typography with that semantic system when mapping to Tailwind. When converting Stitch HTML to React, use [references/tailwind-to-react.md](references/tailwind-to-react.md) for theme-mapped Tailwind (tokens → tailwind.config); keep Tailwind classes in output, map Stitch tokens to project theme.

## Troubleshooting

- **Fetch errors**: Quote the URL in the bash command to avoid shell issues; ensure `scripts/fetch-stitch.sh` is executable.
- **Validation errors**: Fix missing Props interfaces and hardcoded styles per the AST report; follow `references/architecture-checklist.md`.

## Keywords

**English:** Stitch, React, Vite, components, validation, mockData, Tailwind.  
**中文关键词：** Stitch、React、组件、校验、Tailwind。

## References

- **Examples**: [examples/usage.md](examples/usage.md)
- **Style Mapping**: [references/tailwind-to-react.md](references/tailwind-to-react.md) — Theme-mapped Tailwind when converting Stitch HTML; keep Tailwind classes, sync Stitch tokens to tailwind.config.
- **Resources**:
    - [resources/architecture-checklist.md](resources/architecture-checklist.md)
    - [resources/component-template.tsx](resources/component-template.tsx)
- **Scripts**: [scripts/fetch-stitch.sh](scripts/fetch-stitch.sh)
- [Stitch API / MCP](https://stitch.withgoogle.com/docs/mcp/guide/)
