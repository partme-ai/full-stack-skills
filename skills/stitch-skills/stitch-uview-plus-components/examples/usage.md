# stitch-uview-plus-components Usage

## When to use

- The user explicitly mentions **Stitch** and wants a **uni-app + Vue 3 + uview-plus** page or component set.
- The target output should default to **`up-*`** tags, not `u-*`.
- The page needs stronger `uview-plus` engineering guidance: theme variables, safe area, dark mode, popup/upload/tabbar, or bottom CTA handling.

## Typical workflow

1. Resolve `projectId` and `screenId` from a Stitch URL or from project/screen browsing.
2. Call Stitch MCP `get_screen`.
3. Download `htmlCode` with `scripts/fetch-stitch.sh`.
4. Use the screenshot as the layout truth source.
5. Rebuild the page with `up-*` components and current `uview-plus` conventions.
6. Use the checklist in `resources/architecture-checklist.md`.

## Example user prompts

### Direct URL → page conversion

> Use the Stitch skill to convert `https://stitch.withgoogle.com/projects/123?node-id=abc` into a `uview-plus` page with `up-*` components.

### Browse project then convert one screen

> Use Stitch to list my screens, pick the order detail screen, and convert it into a uni-app Vue 3 `uview-plus` page.

### Login / register form flow

> Convert this Stitch auth screen into a `uview-plus` login page using `up-form`, `up-input`, `up-button`, and bottom safe-area handling.

### Home page with bottom navigation

> Convert this Stitch mobile home screen into `uview-plus` with `up-navbar`, `up-tabs`, cards, and `up-tabbar`.

### Popup + upload interaction

> Convert this Stitch product publish screen into `uview-plus`, using `up-picker`, `up-popup`, and `up-upload` instead of raw HTML controls.

### Dark-mode-aware page

> Convert this Stitch profile screen into a `uview-plus` page that uses `var(--up-*)` theme variables and respects dark mode.

## What good output looks like

- Uses `up-*` consistently
- Rebuilds structure instead of preserving Tailwind classes
- Uses `up-status-bar` / `up-safe-bottom` where the layout needs them
- Uses `up-tabbar`, `up-popup`, `up-upload`, `up-empty`, `up-gap`, and `up-line` when those patterns appear in the design
- Extracts repeated data into state or data modules rather than hardcoding everything inline
