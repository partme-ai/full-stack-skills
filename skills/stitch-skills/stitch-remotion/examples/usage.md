# stitch-remotion Usage

## When to use

- User has a Stitch project and wants a **walkthrough video** of its screens (e.g. for demos, marketing).
- You need to list Stitch projects/screens and download screenshots, then build a Remotion composition.

## Steps

1. List Stitch projects (stitch-mcp-list-projects or MCP list_projects); get projectId.
2. List screens (stitch-mcp-list-screens or MCP list_screens); get screenIds.
3. For each screen call get_screen; download screenshot from screenshot.downloadUrl; save to assets/screens/.
4. Create screens.json manifest (see examples/screens.json).
5. Create Remotion project (or use existing); add ScreenSlide and WalkthroughComposition; use @remotion/transitions (fade/slide).
6. Preview with npm run dev; render with npx remotion render WalkthroughComposition output.mp4.

## Example user prompt

> "Build a Remotion walkthrough video from my Stitch project 'Calculator App'."
