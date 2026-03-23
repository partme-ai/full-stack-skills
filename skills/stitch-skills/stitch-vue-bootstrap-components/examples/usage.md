# stitch-vue-bootstrap-components Usage

## When to use

- User has a Stitch screen and wants **Vue 3 + Bootstrap** (Vite, .vue SFC) components using [BootstrapVue Vue 3](https://bootstrap-vue.org/vue3) or BootstrapVueNext.
- You need to download Stitch HTML reliably (use `scripts/fetch-stitch.sh` when web_fetch fails on GCS URLs).

## Steps

1. Get projectId and screenId (e.g. via stitch-mcp-list-projects, stitch-mcp-list-screens).
2. Call Stitch MCP get_screen; get `htmlCode.downloadUrl`.
3. Run `bash scripts/fetch-stitch.sh "<url>" temp/source.html`.
4. Parse HTML; map to Bootstrap Vue components per references/contract.md; create Vue SFCs using resources/component-template.vue and src/data/mockData.js.
5. Wire components in App.vue or router; verify against resources/architecture-checklist.md; run `npm run dev`.

## Example user prompt

> "Convert the Stitch dashboard to a Vue 3 + Bootstrap project."
