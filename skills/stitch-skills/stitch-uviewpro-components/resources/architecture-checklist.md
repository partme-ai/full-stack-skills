# Architecture Quality Gate (uni-app + uView Pro)

## Structural integrity
- [ ] Pages under `pages/`; shared components under `components/`.
- [ ] Logic in script setup or composables; no monolithic single page.
- [ ] Static text, image URLs, lists in data or `data/mockData.js`.

## uView Pro usage
- [ ] **Component discovery**: Consulted [references/component-index.md](../references/component-index.md) for full uView Pro component list; used u-modal, u-popup, u-action-sheet, u-empty, u-avatar, u-picker, u-tabbar, etc., where design requires them (no raw div/button/input for these).
- [ ] **Use framework components when available**: Card/section → **u-card** (title or + **u-section** #right), not `<view class="card">` + card-header + card-title. Label hints / tips / unit → **u-text** (type="info"/"warning", size="24"/28), not `<text class="label-optional">` / .tips-text / .unit. Divider → **u-line** or **u-divider**, not view + border only. See [stitch-html-patterns.md](../references/stitch-html-patterns.md) §7 and [component-index.md](../references/component-index.md) “Design element → Component mapping”.
- [ ] Layout: Use `<u-row>`, `<u-col>`, `<u-gap>`, `<u-line>`/`<u-divider>`; rpx for typography/spacing.
- [ ] Buttons: Use `<u-button type="primary">` etc.; no raw `<button>`.
- [ ] Forms: Use `<u-form>`, `<u-form-item>`, `<u-input>`; labels present; hint text in #label use **u-text**.
- [ ] Navigation: Use `<u-navbar>`, `<u-tabs>`, `<u-tabbar>` per contract.
- [ ] List/feedback: Use `<u-swipe-action>`, `<u-list>`, `<u-empty>`, `<u-toast>`, `<u-modal>`/`<u-popup>` where needed; `uni.$u` per contract.

## Styling and tokens
- [ ] Use uView Pro design tokens (primary, main text, etc.); rpx for sizes.
- [ ] Scoped styles; avoid hardcoded hex when token exists.

## Quality
- [ ] Pages registered in `pages.json`; no placeholder "StitchPage" left.
- [ ] Run in HBuilderX or CLI; verify layout on simulator/device; script setup (Vue 3) used.
