# Architecture Quality Gate (Vue 3 + Bootstrap Vue)

## Structural integrity
- [ ] Logic in composables or script setup; no monolithic single file.
- [ ] Modular .vue components; one primary concern per file.
- [ ] Static text, image URLs, lists in `src/data/mockData.js` (or .ts).

## Bootstrap Vue usage
- [ ] **Use framework components when available**: Card → **b-card** (not div.card); tips/notices → **b-alert**; form hints → **b-form-group** description. No custom .card, .card-header, .card-title, .tips-text. See [contract.md](../references/contract.md) and [component-index.md](../references/component-index.md).
- [ ] Layout: Use `<b-container>`, `<b-row>`, `<b-col>`; no raw CSS grid when contract applies.
- [ ] Buttons: Use `<b-button variant="primary">` etc.; no `<button class="btn">`.
- [ ] Forms: Use `<b-form-group>`, `<b-form-input>`, `<b-form-select>`; wrap in b-form-group.
- [ ] Cards/Tables: Use `<b-card>`, `<b-table :items="...">` per contract.

## Styling and tokens
- [ ] Use Bootstrap spacing utilities (m-*, p-*, gap-*); avoid hardcoded px when token exists.
- [ ] Radius/shadows: use `rounded`, `shadow-sm` etc. per contract.

## Quality
- [ ] Valid Vue 3 SFC syntax; no placeholder "StitchComponent" left.
- [ ] Run `npm run dev` and verify layout and components render correctly.
