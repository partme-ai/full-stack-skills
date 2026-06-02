# Architecture Quality Gate (uni-app + uview-plus)

## Structural integrity

- [ ] Page shell uses `up-navbar` or `up-status-bar` intentionally.
- [ ] Fixed bottom CTA uses `up-safe-bottom`.
- [ ] Repeated blocks are extracted into shared components when appropriate.
- [ ] Large option lists, tab lists, and upload state are not hardcoded everywhere.

## uview-plus usage

- [ ] Output uses **`up-*`** consistently, not `u-*`.
- [ ] Top switching uses `up-tabs` or `up-subsection`, not custom view/button tabs.
- [ ] Picker/select behavior uses `up-picker` or `up-popup`, not native `<select>`.
- [ ] Upload zones use `up-upload`.
- [ ] Empty states use `up-empty`.
- [ ] Bottom navigation uses `up-tabbar` when the screen is app-level navigation.
- [ ] Divider / spacing uses `up-line`, `up-divider`, or `up-gap` where appropriate.

## Theme and runtime

- [ ] Styles prefer `var(--up-*)` tokens when a theme variable exists.
- [ ] Dark-mode-aware pages avoid baking every color into raw hex values.
- [ ] Runtime guidance matches current `uview-plus` setup expectations.

## Stitch conversion quality

- [ ] Tailwind classes are not copied into the final template by default.
- [ ] Raw HTML controls are not left behind when `up-*` equivalents exist.
- [ ] The page looks like a `uview-plus` page, not a stitched HTML wrapper.

## Validation

- [ ] Discovery surfaces reference the new skill.
- [ ] `git diff --check` passes.
