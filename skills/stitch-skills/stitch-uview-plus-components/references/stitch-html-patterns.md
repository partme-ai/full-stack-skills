# Stitch HTML → uview-plus Patterns

Stitch exports Tailwind-heavy HTML. Rebuild the layout into `uni-app + Vue 3 + uview-plus`; do not preserve the HTML literally.

## 1. Page shell

| Stitch pattern | uview-plus pattern |
|---|---|
| sticky mobile header with back icon and title | `up-navbar` |
| branded custom top bar with manual padding | `up-status-bar` + branded header view |
| full-page content area with large vertical spacing | `scroll-view` + `up-gap` + themed content container |
| fixed bottom button row | `up-safe-bottom` + footer bar + `up-button` |

## 2. Top switching UI

| Stitch pattern | uview-plus pattern |
|---|---|
| wide tab strip | `up-tabs` |
| short filter pill switch | `up-subsection` |
| custom underline tab bar | `up-tabs` with current/change binding |

## 3. Cards and lists

| Stitch pattern | uview-plus pattern |
|---|---|
| rounded shadow card with title/content | `up-card` |
| multiple dense settings or detail rows | `up-cell-group` + `up-cell` |
| list row with slide actions | `up-swipe-action` |
| empty list | `up-empty` |

## 4. Forms

| Stitch pattern | uview-plus pattern |
|---|---|
| label + input | `up-form-item` + `up-input` |
| label + multiline input | `up-form-item` + `up-textarea` |
| label + segmented mode selection | `up-subsection` or `up-radio-group` |
| label + option chooser | `up-picker` or `up-popup` |
| label + switch | `up-switch` |
| label + upload area | `up-upload` |

## 5. Popup and sheet interactions

| Stitch pattern | uview-plus pattern |
|---|---|
| bottom sheet panel | `up-popup mode="bottom"` |
| center dialog | `up-popup mode="center"` or `up-modal` |
| action list | `up-action-sheet` |

## 6. Tailwind-heavy visual blocks

When Stitch gives you combinations like:
- `rounded-xl shadow-soft bg-white`
- `sticky bottom-0`
- `space-y-4`
- `divide-y`

Translate them into:
- `up-card`
- `up-safe-bottom`
- `up-gap`
- `up-line` / `up-divider`

The goal is a semantic `uview-plus` page, not a Tailwind page rewritten into Vue.

## 7. Common conversions

### Auth screen

- header → `up-navbar`
- form → `up-form`
- fields → `up-input`
- CTA → `up-safe-bottom` + `up-button`

### Settings / profile screen

- page sections → `up-card` or `up-cell-group`
- boolean rows → `up-cell` + right-side content or `up-switch`
- navigation rows → `up-cell` with link affordance

### Publish / create screen

- type switch → `up-subsection`
- category / option selection → `up-picker`
- media area → `up-upload`
- bottom submit bar → `up-safe-bottom`

### Home / dashboard screen

- top switching → `up-tabs`
- content cards → `up-card`
- bottom app nav → `up-tabbar`

## 8. Anti-patterns

- Do not keep Tailwind utility classes in the final template.
- Do not use raw HTML form controls when a `up-*` component exists.
- Do not manually simulate safe areas with magic numbers.
- Do not hand-roll upload, popup, or tabbar behavior.
