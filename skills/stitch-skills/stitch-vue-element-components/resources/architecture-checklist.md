# Architecture Quality Gate (Vue 3 + Element Plus)

## Structural integrity
- [ ] Logic in composables or script setup; no monolithic single file.
- [ ] Modular .vue components; one primary concern per file.
- [ ] Static text, image URLs, lists in `src/data/mockData.js` (or .ts).

## Element Plus usage
- [ ] **Use framework components when available**: Card → **el-card** (not div.card); tips/notices → **el-alert**. No custom .card, .card-header, .card-title, .tips-text. See [contract.md](../references/contract.md) and [component-index.md](../references/component-index.md).
- [ ] Layout: Use `<el-row>`, `<el-col>`, `<el-container>`; no raw CSS grid when contract applies.
- [ ] Buttons: Use `<el-button type="primary">` etc.; no `<button class="...">`.
- [ ] Forms: Use `<el-form>`, `<el-form-item>`, `<el-input>`; labels present.
- [ ] Data display: Use `<el-table>`, `<el-card>`, `<el-tag>` per contract.

## Styling and tokens
- [ ] Use Element Plus design tokens (primary, success, etc.); avoid hardcoded hex when token exists.
- [ ] Scoped styles; no global overrides unless required.

## Quality
- [ ] Valid Vue 3 SFC syntax; no placeholder "StitchComponent" left.
- [ ] Run `npm run dev` and verify layout and components render correctly.
