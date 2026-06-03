# uview-plus Component Index

Use framework components when available. For this skill, prefer **`up-*`** over raw HTML and over older `u-*` examples.

## Navigation and structure

| Need | Component | Notes |
|---|---|---|
| standard mobile header | `up-navbar` | default page header |
| custom top inset / branded header | `up-status-bar` | when not using navbar |
| top tab switching | `up-tabs` | full-width switching UI |
| short segmented switching | `up-subsection` | compact pills or mode switch |
| bottom app navigation | `up-tabbar` + `up-tabbar-item` | use `value` + `name` |
| section spacing | `up-gap` | vertical block spacing |
| separators | `up-line`, `up-divider` | semantic divider components |
| empty state | `up-empty` | empty list / no-result states |

## Cards and list rows

| Need | Component | Notes |
|---|---|---|
| marketing/info card | `up-card` | primary card container |
| settings rows | `up-cell-group` + `up-cell` | dense row content |
| swipe row actions | `up-swipe-action` | delete/archive/etc. |
| image or carousel section | `up-swiper`, `up-image` | visual display |

## Forms and input

| Need | Component | Notes |
|---|---|---|
| form shell | `up-form` + `up-form-item` | model + rules |
| single-line text | `up-input` | default input |
| multi-line content | `up-textarea` | long text |
| option selection | `up-picker` | uses `columns` |
| popup-based selector | `up-popup` | richer custom option UI |
| radio choices | `up-radio-group` + `up-radio` | current docs use `name` + `label` |
| toggle | `up-switch` | boolean switch |
| quantity | `up-number-box` | plus/minus stepper |
| search | `up-search` | search field |
| upload | `up-upload` | images/files |

## Feedback and overlays

| Need | Component | Notes |
|---|---|---|
| bottom sheet | `up-popup` | standard panel overlay |
| action menu | `up-action-sheet` | simple action list |
| confirm dialog | `up-modal` | destructive / confirm flows |
| toast / notify | `uni.$u.toast()` or `up-toast` | depends on Root bridge |
| loading | `up-loading-icon`, `up-overlay` | loading affordances |

## Safe-area and runtime helpers

| Need | Component / pattern | Notes |
|---|---|---|
| bottom CTA inset | `up-safe-bottom` | fixed submit/action bar |
| top safe-area inset | `up-status-bar` | custom top header alignment |
| dark-mode styling | `var(--up-*)` | prefer theme variables |
| runtime theme sync | `setConfig({ color })` | use when explicit runtime sync is needed |

## Design element → component mapping

| Design element | Use this | Do not use |
|---|---|---|
| button | `up-button` | raw `<button>` |
| tab row | `up-tabs` | custom button strip |
| segmented pills | `up-subsection` | custom rounded filter chips |
| select field | `up-picker` or `up-popup` + list | native `<select>` |
| card panel | `up-card` | styled `<view class="card">` |
| setting row | `up-cell` | custom flex row everywhere |
| upload box | `up-upload` | dashed box + hidden file input |
| fixed submit footer | `up-safe-bottom` + `up-button` | fixed footer without inset handling |
| empty state | `up-empty` | plain text placeholder |
| divider | `up-line`, `up-divider` | anonymous border block |
