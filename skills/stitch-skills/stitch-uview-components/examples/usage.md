# stitch-uview-components Usage

## When to use

- User has a Stitch screen and wants **uni-app + Vue 2 + uView 2.0** pages/components that match the design.
- You need to download Stitch HTML reliably (use `scripts/fetch-stitch.sh` when web_fetch fails on GCS URLs).

## Steps

1. Get projectId and screenId (e.g. via stitch-mcp-list-projects, stitch-mcp-list-screens).
2. Call Stitch MCP get_screen; get `htmlCode.downloadUrl`.
3. Run `bash scripts/fetch-stitch.sh "<url>" temp/source.html`.
4. Parse HTML; map to uView 2 components per references/contract.md; create pages using resources/page-template.vue and data/mockData.js.
5. Register pages in pages.json; verify against resources/architecture-checklist.md; run in HBuilderX or CLI.

## Example user prompt

> "Convert the Stitch login screen to a uni-app + uView 2 project."
