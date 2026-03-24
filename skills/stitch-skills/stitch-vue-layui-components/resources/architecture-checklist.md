# Architecture Quality Gate (Vue 3 + Layui-Vue)

## Structural integrity
- [ ] Logic in composables or script setup; no monolithic single file.
- [ ] Modular .vue components; one primary concern per file.
- [ ] Static text, image URLs, lists in `src/data/mockData.js` (or .ts).

## Layui-Vue usage
- [ ] **Use framework components when available**: Card → **lay-card** (not div.card); divider → **lay-divider**. No custom .card, .card-header, .card-title, .tips-text. See [contract.md](../references/contract.md) and [component-index.md](../references/component-index.md).
- [ ] Buttons: Use layui-btn style (height 38px, radius 2px) per contract.
- [ ] Inputs: Use layui-input style (height 38px, border #e2e2e2).
- [ ] Cards: Use **lay-card** component (white bg, header border #f6f6f6).
- [ ] Tables: Use layui-table style (header #f2f2f2, border #e2e2e2).
- [ ] Other: Use lay-page-header, lay-result, lay-skeleton, lay-timeline, lay-space when applicable.

## Styling and tokens
- [ ] Radius: Strictly 2px or 4px; no large radius (8px+) unless requested.
- [ ] Colors: Use Layui palette only (primary #16baaa, danger #FF5722, neutrals #333/#666/#999).

## Quality
- [ ] Valid Vue 3 SFC syntax; no placeholder "StitchComponent" left.
- [ ] Run `npm run dev` and verify layout and components render correctly.
