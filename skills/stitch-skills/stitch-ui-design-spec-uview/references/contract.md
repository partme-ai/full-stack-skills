# uView Design Contract (uView 2.0 / Vue2)

This reference contains:

- Hard constraints prefix (paste-ready)
- Layout invariants for beautify mode
- Component snippets (uView look & feel)

---

## Trigger Keywords

Use this contract when the request mentions **Stitch** and any of the following keywords:

- `uview`
- `uview2`
- `uview2.0`
- `u-view`

Chinese trigger keywords (only for triggering):

- `uview 风格`

---

## Hard Constraints (Must Follow)

### Color Tokens (from uView theme variables)

Only use this palette (text/border/background/icons/states). Do not introduce new brand colors:

- Text
  - `u-main-color`: `#303133`
  - `u-content-color`: `#606266`
  - `u-tips-color`: `#909193`
  - `u-light-color`: `#c0c4cc`
- Surfaces
  - `u-bg-color`: `#f3f4f6`
  - `u-border-color`: `#dadbde`
  - `u-disabled-color`: `#c8c9cc`
- Semantic / Brand
  - `u-primary`: `#3c9cff` / `u-primary-dark`: `#398ade` / `u-primary-light`: `#ecf5ff` / `u-primary-disabled`: `#9acafc`
  - `u-success`: `#5ac725` / `u-success-dark`: `#53c21d` / `u-success-light`: `#f5fff0` / `u-success-disabled`: `#a9e08f`
  - `u-warning`: `#f9ae3d` / `u-warning-dark`: `#f1a532` / `u-warning-light`: `#fdf6ec` / `u-warning-disabled`: `#f9d39b`
  - `u-error`: `#f56c6c` / `u-error-dark`: `#e45656` / `u-error-light`: `#fef0f0` / `u-error-disabled`: `#f7b2b2`
  - `u-info`: `#909399` / `u-info-dark`: `#767a82` / `u-info-light`: `#f4f4f5` / `u-info-disabled`: `#c4c6c9`

Forbidden:
- No gradients as the default style (unless a single button explicitly requests a gradient via `color`).
- No new “primary brand color” outside this palette.

### Type Scale

Only use these font sizes (px): `12, 14, 16, 18, 20, 24`.

Font weights:
- Titles: 600
- Body: 400
- Emphasis: 500

Default text colors:
- Title: `#303133`
- Body: `#606266`
- Secondary: `#909193`
- Disabled: `#c8c9cc`
- Error: `#f56c6c`

### Spacing Scale

Only use spacing (px): `4, 8, 12, 16, 20, 24, 32, 40`.

Forbidden:
- No 13/18/22 etc.
- Keep section spacing consistent within a screen (choose 24 or 32 and stick to it).

### Radius + Border + Shadow

Radius only: `8, 12, 999`.

Borders:
- Default border color: `#dadbde`
- Hairline feel is acceptable (visual thinness; implementation not required)

Shadows:
- Minimal. At most one subtle shadow style for the whole screen.

### Motion

Transitions:
- 200ms
- ease-out

Forbidden:
- No bouncy/long animations.

---

## Component Contracts (uView 2.0 Specifics)

### Layout
- **Flex**: Use `u-row` and `u-col` for grid layouts.
  ```html
  <u-row justify="space-between" gutter="10">
      <u-col span="6">...</u-col>
      <u-col span="6">...</u-col>
  </u-row>
  ```
- **Cell**: Use `u-cell-group` and `u-cell` for list items.

### Forms
- **Form**: `<u--form>` (note the double dash for 2.0 components when required, or standard `u-form`).
- **Input**: `<u--input>` or `<u-input>` with `border="surround"`.
- **Button**: `<u-button type="primary" text="Submit"></u-button>`.

### Navigation
- **Navbar**: `<u-navbar title="Title" @leftClick="leftClick" :autoBack="true">`.
- **Tabs**: `<u-tabs :list="list1"></u-tabs>`.
- **Steps**: `<u-steps :current="1">...</u-steps>`.

### List & Data
- **SwipeAction**: `<u-swipe-action><u-swipe-action-item ...>...</u-swipe-action-item></u-swipe-action>`.
- **IndexList**: `<u-index-list :indexList="indexList">...</u-index-list>`.
- **Waterfall**: `<u-waterfall v-model="flowList">...</u-waterfall>`.

### Feedback
- **Toast**: Use `this.$refs.uToast.show({...})`.
- **Modal**: `<u-modal :show="show" ...>`.
- **Code**: `<u-code :seconds="60" ref="uCode" @change="codeChange"></u-code>`.

---

## Beautify Mode (Layout-Locked)

When the task is **beautify / polish / refine** for an existing screen, you must add layout invariants to avoid layout drift (e.g., centering a previously left-aligned logo).
