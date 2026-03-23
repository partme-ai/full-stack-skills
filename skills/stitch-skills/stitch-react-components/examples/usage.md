# stitch-react-components Usage

## When to use

- User has a Stitch screen and wants **React (Vite + TypeScript)** components that match the design.
- You need to download Stitch HTML reliably (use `scripts/fetch-stitch.sh` when web_fetch fails on GCS URLs).

## Steps

1. Get projectId and screenId (e.g. via stitch-mcp-list-projects, stitch-mcp-list-screens).
2. Call Stitch MCP get_screen; get `htmlCode.downloadUrl`.
3. Run `bash scripts/fetch-stitch.sh "<url>" temp/source.html`.
4. Parse HTML; extract Tailwind config and structure; create mockData.ts and components using resources/component-template.tsx.
5. Run validation (if project has npm run validate) and check resources/architecture-checklist.md.
