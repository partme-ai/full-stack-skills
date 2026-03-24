---
name: stitch-vue-element-components
description: Convert Stitch designs into modular Vite/Vue 3 and Element Plus components. Uses Stitch MCP get_screen to retrieve design JSON and HTML; supports high-reliability fetch via scripts; enforces Vue SFC structure, data decoupling, and Element Plus component contracts.
allowed-tools:
  - "stitch*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
---


# Stitch to Vue 3 + Element Plus Components

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" and converting Stitch screens to **Vue 3 + Element Plus** (Vite, .vue SFC).

You are a **frontend engineer** turning Stitch designs into clean, modular Vue 3 + Element Plus code. Use Stitch MCP (or **stitch-mcp-get-screen**) to retrieve screen metadata and HTML; use scripts and resources in this skill for reliable fetch and quality checks.

## Prerequisites

- Stitch MCP Server (https://stitch.withgoogle.com/docs/mcp/guide/)
- Node.js and npm (for Vite/Vue 3 project)
- Stitch project and screen IDs — **two ways**: (1) From a **Stitch design URL**: parse **projectId** from path and **screenId** from `node-id` query (see **stitch-mcp-get-screen**). (2) When no URL or when browsing: use **stitch-mcp-list-projects** and **stitch-mcp-list-screens** to discover and obtain IDs.

## Official Documentation

- **Element Plus**: [Official (zh-CN)](https://element-plus.org/zh-CN/) · [Design Guide](https://element-plus.org/en-US/guide/design) · [Component Overview](https://element-plus.org/en-US/component/overview) · [GitHub](https://github.com/element-plus/element-plus)
- Full links and usage: [references/official.md](references/official.md)

## Retrieval and Networking

1. **Discover Stitch MCP prefix**: Run `list_tools` to find the prefix (e.g. `mcp_stitch__stitch:`).
2. **Resolve projectId and screenId**: (1) If the user provided a **Stitch design URL**, parse **projectId** from the path and **screenId** from the `node-id` query. (2) Otherwise, or when the user wants to choose a project/screen, call **list_projects** (e.g. filter `view=owned`) then **list_screens** with the chosen projectId to get screenIds.
3. **Fetch screen metadata**: Call `[prefix]:get_screen` with `projectId` and `screenId` to get design JSON, `htmlCode.downloadUrl`, `screenshot.downloadUrl`, dimensions, deviceType.
4. **High-reliability HTML download**: AI fetch tools can fail on Google Cloud Storage URLs. Use Bash to run the skill script:
   ```bash
   bash scripts/fetch-stitch.sh "<htmlCode.downloadUrl>" "temp/source.html"
   ```
   This uses `curl -L` for redirects and TLS. Ensure the URL is quoted.
5. **Visual reference**: Use `screenshot.downloadUrl` to confirm layout and details.

## Architectural Rules

- **Modular components**: Split the design into separate .vue files; avoid one giant SFC.
- **Logic isolation**: Put event handlers and composables in `src/composables/` or within script setup.
- **Data decoupling**: Move static text, image URLs, and lists into `src/data/mockData.js` (or .ts).
- **Element Plus only (use framework components when available)**: Use **el-card** for cards, **el-alert** for tips; do not use div.card or custom .card-header/.tips-text. Use `<el-*>` components per [references/contract.md](references/contract.md); do not use raw HTML for buttons, forms, layout when an Element component exists.
- **Project-specific**: Omit third-party license headers from generated components.

## Execution Steps

1. **Environment**: If the project has no `node_modules`, run `npm install`.
2. **Data layer**: Create `src/data/mockData.js` from the design content.
3. **Component drafting**: Use `resources/component-template.vue` as base; replace placeholder with real component name and Element Plus tags per contract.
4. **Wiring**: Update the app entry (e.g. `App.vue` or router) to render the new components.
5. **Quality check**: Verify against `resources/architecture-checklist.md`; run `npm run dev` to confirm visually.

## Integration with This Repo

- **Get screen**: Use **stitch-mcp-get-screen** (or MCP `get_screen`) with projectId and screenId. Obtain IDs either by parsing a **Stitch design URL** or by using **stitch-mcp-list-projects** and **stitch-mcp-list-screens** when no URL is given or when the user needs to browse/select.
- **Design spec**: If Stitch was generated with **stitch-ui-design-spec-element-plus** constraints, map to Vue SFC and Element Plus components. If converting from Stitch HTML (e.g. get_screen htmlCode), use [references/tailwind-to-element-plus.md](references/tailwind-to-element-plus.md) for Tailwind utility → px/theme, then [references/contract.md](references/contract.md) for component API.
- **Design system**: If the project has DESIGN.md (from **stitch-design-md**), align colors and typography with that semantic system when mapping to Element tokens.

## Troubleshooting

- **Fetch errors**: Quote the URL in the bash command to avoid shell issues; ensure `scripts/fetch-stitch.sh` is executable.
- **Component mapping**: Follow [references/contract.md](references/contract.md) for layout (`el-row`/`el-col`), buttons (`el-button`), forms (`el-form`, `el-input`), etc.

## Keywords

**English:** Stitch, Vue 3, Element Plus, Vite, components, el-button, el-form.  
**中文关键词：** Stitch、Vue 3、Element Plus、组件、饿了么。

## References

- [Examples](examples/usage.md)
- [Scripts](scripts/fetch-stitch.sh)
- [Component index (per-component doc links)](references/component-index.md)
- [Tailwind → Element Plus](references/tailwind-to-element-plus.md) — Tailwind utility → px/theme when converting Stitch HTML.
- [Contract (Element Plus mapping)](references/contract.md)
- [Component API (props/events quick reference)](api/component-api.md)
- [Official documentation](references/official.md)
- [Architecture checklist](resources/architecture-checklist.md)
- [Component template](resources/component-template.vue)
- [Stitch API / MCP](https://stitch.withgoogle.com/docs/mcp/guide/)
