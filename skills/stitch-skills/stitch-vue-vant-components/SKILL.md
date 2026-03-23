---
name: stitch-vue-vant-components
description: Convert Stitch designs into modular Vite/Vue 3 and Vant 4 mobile components. Uses Stitch MCP get_screen for retrieval; high-reliability fetch via scripts; enforces Vue SFC structure and Vant 4 component contracts van-button van-field van-nav-bar etc..
allowed-tools:
  - "stitch*:*"
  - "Bash"
  - "Read"
  - "Write"
  - "web_fetch"
---


# Stitch to Vue 3 + Vant 4 Components

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" and converting Stitch screens to **Vue 3 + Vant 4** (Vite, .vue SFC, mobile-first).

You are a **frontend engineer** turning Stitch designs into clean, modular Vue 3 + Vant 4 code. Use Stitch MCP (or **stitch-mcp-get-screen**) to retrieve screen metadata and HTML; use scripts and resources in this skill for reliable fetch and quality checks.

## Prerequisites

- Stitch MCP Server (https://stitch.withgoogle.com/docs/mcp/guide/)
- Node.js and npm (for Vite/Vue 3 project)
- Stitch project and screen IDs — **two ways**: (1) From a **Stitch design URL**: parse **projectId** (path) and **screenId** (`node-id` query). (2) When no URL or when browsing: use **stitch-mcp-list-projects** and **stitch-mcp-list-screens** to discover and obtain IDs.

## Official Documentation

- **Vant (Vue 3)**: [Official](https://vant-ui.github.io/) · [Guide / Components (zh-CN)](https://vant-ui.github.io/vant/#/zh-CN) · [GitHub](https://github.com/youzan/vant)
- Full links and usage: [references/official.md](references/official.md)

## Retrieval and Networking

1. **Discover Stitch MCP prefix**: Run `list_tools` to find the prefix (e.g. `mcp_stitch__stitch:`).
2. **Fetch screen metadata**: Call `[prefix]:get_screen` with `projectId` and `screenId` (numeric IDs) to get design JSON, `htmlCode.downloadUrl`, `screenshot.downloadUrl`, dimensions, deviceType.
3. **High-reliability HTML download**: AI fetch tools can fail on Google Cloud Storage URLs. Use Bash to run the skill script:
   ```bash
   bash scripts/fetch-stitch.sh "<htmlCode.downloadUrl>" "temp/source.html"
   ```
   Ensure the URL is quoted.
4. **Visual reference**: Use `screenshot.downloadUrl` to confirm layout and details.

## Architectural Rules

- **Modular components**: Split the design into separate .vue files; avoid one giant SFC.
- **Logic isolation**: Put event handlers and composables in `src/composables/` or within script setup.
- **Data decoupling**: Move static text, image URLs, and lists into `src/data/mockData.js` (or .ts).
- **Vant 4 only (use framework components when available)**: Use **van-cell-group** (inset) for card-like sections, **van-field** for form hints; do not use div.card or custom .card-header/.tips-text. Use `<van-*>` components per [references/contract.md](references/contract.md); mobile-first (375px base), safe area, flex layout.
- **Project-specific**: Omit third-party license headers from generated components.

## Execution Steps

1. **Environment**: If the project has no `node_modules`, run `npm install`.
2. **Data layer**: Create `src/data/mockData.js` from the design content.
3. **Component drafting**: Use `resources/component-template.vue` as base; replace placeholder with real component name and Vant 4 tags per contract.
4. **Wiring**: Update the app entry (e.g. `App.vue` or router) to render the new components.
5. **Quality check**: Verify against `resources/architecture-checklist.md`; run `npm run dev` to confirm visually (mobile viewport).

## Integration with This Repo

- **Get screen**: Use **stitch-mcp-get-screen** with projectId and screenId. Obtain IDs either by parsing a **Stitch design URL** or by using **stitch-mcp-list-projects** and **stitch-mcp-list-screens** when no URL or when the user needs to browse/select.
- **Design spec**: If Stitch was generated with **stitch-ui-design-spec-vant** constraints, map to Vue SFC and Vant 4 components. If converting from Stitch HTML (e.g. get_screen htmlCode), use [references/tailwind-to-vant.md](references/tailwind-to-vant.md) for Tailwind utility → px/theme, then [references/contract.md](references/contract.md) for component API.
- **Design system**: If the project has DESIGN.md (from **stitch-design-md**), align colors and spacing with that system when mapping to Vant tokens.

## Troubleshooting

- **Fetch errors**: Quote the URL in the bash command; ensure `scripts/fetch-stitch.sh` is executable.
- **Component mapping**: Follow [references/contract.md](references/contract.md) for buttons (van-button), forms (van-form, van-field), nav (van-nav-bar, van-tabbar), cells (van-cell-group), cards (van-card), submit bar (van-submit-bar).

## Keywords

**English:** Stitch, Vue 3, Vant, Vant 4, Vite, mobile, van-button, van-nav-bar.  
**中文关键词：** Stitch、Vue 3、Vant、移动端、组件。

## References

- [Examples](examples/usage.md)
- [Scripts](scripts/fetch-stitch.sh)
- [Component index (per-component doc links)](references/component-index.md)
- [Tailwind → Vant 4](references/tailwind-to-vant.md) — Tailwind utility → px/theme when converting Stitch HTML.
- [Contract (Vant 4 mapping)](references/contract.md)
- [Component API (props/events quick reference)](api/component-api.md)
- [Official documentation](references/official.md)
- [Architecture checklist](resources/architecture-checklist.md)
- [Component template](resources/component-template.vue)
- [Stitch API / MCP](https://stitch.withgoogle.com/docs/mcp/guide/)
