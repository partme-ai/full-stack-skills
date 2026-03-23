# Architecture Quality Gate (Vue 3 + Vant 4)

## Structural integrity
- [ ] Logic in composables or script setup; no monolithic single file.
- [ ] Modular .vue components; one primary concern per file.
- [ ] Static text, image URLs, lists in `src/data/mockData.js` (or .ts).

## Vant 4 usage
- [ ] **Use framework components when available**: Card-like blocks → **van-cell-group** (inset) + **van-cell**; form hints → **van-field** label. No custom .card, .card-header, .card-title, .tips-text. See [contract.md](../references/contract.md) and [component-index.md](../references/component-index.md).
- [ ] Layout: Use `<van-row>`, `<van-col>`, `<van-cell-group>`; mobile-first viewport (375px).
- [ ] Buttons: Use `<van-button type="primary">` etc.; no raw `<button>`.
- [ ] Forms: Use `<van-form>`, `<van-field>`; labels and rules present.
- [ ] Navigation: Use `<van-nav-bar>`, `<van-tabbar>`, `<van-tabs>` per contract.
- [ ] Data display: Use `<van-cell>`, `<van-card>`, `<van-empty>` per contract.

## Styling and tokens
- [ ] Use Vant 4 design tokens (primary #1989fa, success, etc.); page bg #f7f8fa.
- [ ] Scoped styles; respect safe area for mobile.

## Quality
- [ ] Valid Vue 3 SFC syntax; no placeholder "StitchComponent" left.
- [ ] Run `npm run dev` and verify layout in mobile viewport; check NavBar/Tabbar placement.
