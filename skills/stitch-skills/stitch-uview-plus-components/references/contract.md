# uview-plus Design Contract (Stitch HTML → uni-app Page Mapping)

This file defines how to turn Stitch-generated HTML into **uni-app + Vue 3 + uview-plus** output. The target convention is **`up-*`** components, theme-aware styles, and a safe-area-aware page shell.

## 1. Framework assumptions

- Use **Vue 3**
- Use **`uview-plus`**
- Default generated tags to **`up-*`**
- Use **`rpx`** for spacing and typography
- Prefer **`<script setup>`**
- Register pages in `pages.json`

## 2. Theme and runtime rules

### Prefer current uview-plus theme guidance

- In `.vue` / `.uvue` pages, prefer CSS variables such as:
  - `var(--up-primary)`
  - `var(--up-bg-color)`
  - `var(--up-border-color)`
  - `var(--up-content-color)`
  - `var(--up-navbar-bg-color)`
- When the generated page needs explicit runtime color sync, describe or use `setConfig({ color })`.
- Keep legacy `uni.scss` bridge guidance compatible with `@import 'uview-plus/theme.scss';`.

### Page shell rules

- Normal page header: use **`up-navbar`**
- Custom branded header: use **`up-status-bar`** plus a custom header view
- Fixed bottom CTA: wrap it with **`up-safe-bottom`**
- Empty page state: use **`up-empty`**
- Vertical spacing between large sections: use **`up-gap`**
- Divider line: use **`up-line`** or **`up-divider`**

## 3. Output structure rules

- Prefer:
  - page shell
  - shared components
  - extracted data lists / tabs / options
  - theme-aware styles
- Avoid a single huge page file when the design naturally splits into cards, upload zones, or repeated list rows.

## 4. Component mapping

| Stitch / generic pattern | Use in uview-plus | Notes |
|---|---|---|
| sticky mobile header | `up-navbar` | use `autoBack` for back flows |
| custom branded top spacer | `up-status-bar` | for custom top chrome, not ordinary pages |
| top tabs / category tabs | `up-tabs` | do not keep custom `<view>` tab bars |
| segmented filter pills | `up-subsection` | for short mutually exclusive option sets |
| card block with title/content | `up-card` | use card slots for richer content |
| dense settings rows | `up-cell-group` + `up-cell` | better than ad hoc rows |
| form wrapper | `up-form` + `up-form-item` | use page model and rules where appropriate |
| text input | `up-input` | use inside form item |
| multi-line field | `up-textarea` | prefer component over raw textarea |
| picker / option sheet | `up-picker` | use `v-model:show` and `columns` |
| popup / bottom sheet | `up-popup` | use for custom content containers |
| destructive / confirm dialog | `up-modal` or `up-popup` | do not hand-roll overlays |
| upload area | `up-upload` | use component events and file list |
| radio choices | `up-radio-group` + `up-radio` | in `uview-plus`, radio examples use `name` + `label` |
| switch / boolean toggle | `up-switch` | instead of peer checkbox UI |
| bottom navigation | `up-tabbar` + `up-tabbar-item` | use `value` + `name` |
| empty state | `up-empty` | not plain text |
| section spacing | `up-gap` | avoid random spacer views |
| separators | `up-line` / `up-divider` | avoid raw border divs |

## 5. Strong API expectations

### Tabs

- Use:
  ```vue
  <up-tabs :list="tabList" :current="current" @change="handleTabChange" />
  ```
  or `v-model:current` where appropriate.
- `up-tabs` is the default for broad mobile top tab switching.
- Do not implement tabs with raw views/buttons.

### Subsection

- Use `up-subsection` for short segmented switches where `up-tabs` would be visually too heavy.
- Good fit for two-to-four mode toggles or filter capsules.

### Picker

- Use:
  ```vue
  <up-picker v-model:show="showPicker" :columns="columns" @confirm="onConfirm" />
  ```
- Prefer `v-model:show` when possible.
- `uview-plus` picker uses **`columns`**, not the `:range` convention from the other skill.
- When the design is really a full bottom sheet, use `up-popup` and put a richer selection UI inside it instead of abusing picker.

### Popup

- Use:
  ```vue
  <up-popup v-model:show="showPopup" mode="bottom" :round="16" />
  ```
- This is the default fix for custom fixed overlays, action drawers, and sheet panels exported from Stitch.

### Upload

- Use:
  ```vue
  <up-upload :fileList="fileList" @afterRead="afterRead" @delete="onDelete" />
  ```
- Prefer component-provided preview/add/delete behavior over hand-built dashed boxes.

### Radio

- Follow current `uview-plus` examples:
  ```vue
  <up-radio-group v-model="value">
    <up-radio :name="item.name" :label="item.label" />
  </up-radio-group>
  ```
- Do not carry over the `value`-based radio rule from `stitch-uviewpro-components`.

### Tabbar

- Use:
  ```vue
  <up-tabbar :value="currentTab" @change="name => currentTab = name">
    <up-tabbar-item name="home" text="首页" icon="home" />
  </up-tabbar>
  ```
- Use for app-level bottom navigation only, not ordinary page actions.

### Safe bottom

- Fixed submit bars, purchase bars, or footer CTAs should use:
  ```vue
  <up-safe-bottom>
    <view class="footer-bar">
      <up-button type="primary">提交</up-button>
    </view>
  </up-safe-bottom>
  ```

## 6. Anti-patterns

- Do not generate `u-*` tags in this skill. Use `up-*`.
- Do not leave Tailwind classes in the final template unless the project explicitly uses Tailwind.
- Do not keep native `<button>`, `<input>`, `<select>`, or raw popup overlays when `up-*` components exist.
- Do not hardcode top spacer heights when `up-navbar` or `up-status-bar` solves the problem.
- Do not create bottom fixed CTAs without `up-safe-bottom`.
- Do not render "No data" as plain text if `up-empty` is a fit.
- Do not hand-build separators if `up-line`, `up-divider`, or `up-gap` expresses the intent.
- Do not assume the `uView Pro` picker/radio API. This skill must follow **current `uview-plus` docs**.
- In Vue 3 output, prefer named template slots such as `#suffix`, `#foot`, or `#body` over legacy `slot="..."` syntax.

## 7. Root bridge guidance

- If the consuming project has the Root bridge enabled, global methods like `uni.$u.toast()` are preferred over placing `up-toast` on every page.
- If the consuming project does not use the Root bridge, add the required feedback component explicitly.

## 8. Before writing code

Read:
- [component-index.md](component-index.md)
- [stitch-html-patterns.md](stitch-html-patterns.md)
- [tailwind-to-uview-plus.md](tailwind-to-uview-plus.md)
