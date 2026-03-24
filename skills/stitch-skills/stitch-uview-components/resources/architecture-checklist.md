# Architecture Quality Gate (uni-app + uView 2.0)

## Structural integrity
- [ ] Pages under `pages/`; shared components under `components/`.
- [ ] Logic in methods or mixins; no monolithic single page.
- [ ] Static text, image URLs, lists in data or `data/mockData.js`.

## uView 2 usage
- [ ] **Use framework components when available**: Card-like blocks → **u-cell-group** + **u-cell** or **u-text** for title; label hints/tips → **u-text**; divider → **u-line** / **u-divider**. No custom .card, .card-header, .card-title, .label-optional, .tips-text, .unit. See [contract.md](../references/contract.md) and [component-index.md](../references/component-index.md).
- [ ] Layout: Use `<u-row>`, `<u-col>`, `<u-cell-group>`; no raw grid when contract applies.
- [ ] Buttons: Use `<u-button type="primary">` etc.; no raw `<button>`.
- [ ] Forms: Use `<u-form>`, `<u-input>`; labels present.
- [ ] Navigation: Use `<u-navbar>`, `<u-tabs>` per contract.
- [ ] List/feedback: Use `<u-swipe-action>`, `<u-toast>`, `<u-modal>` per contract.

## Styling and tokens
- [ ] Use uView theme variables (u-primary, u-main-color, etc.); avoid hardcoded hex when token exists.
- [ ] Scoped styles; rpx for responsive where appropriate.

## Quality
- [ ] Pages registered in `pages.json`; no placeholder "StitchPage" left.
- [ ] Run in HBuilderX or CLI; verify layout on simulator/device.
