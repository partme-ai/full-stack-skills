# uview-plus Component API (Stitch conversion reference)

Use this file as a quick contract reference when generating `up-*` output.

## up-tabs

| Concern | Contract |
|---|---|
| Basic usage | `<up-tabs :list="tabList" :current="current" @change="handleChange" />` |
| Two-way option | `v-model:current` |
| Data shape | list items are objects, commonly with `name` |
| Use case | top tab switching, category tabs |

## up-subsection

| Concern | Contract |
|---|---|
| Basic usage | `<up-subsection :list="list" :current="current" @change="handleChange" />` |
| Styling | `activeColor`, `inactiveColor` |
| Use case | compact segmented control |

## up-form

| Concern | Contract |
|---|---|
| Basic usage | `<up-form :model="form" ref="formRef">` |
| Field wrapper | `up-form-item` |
| Typical children | `up-input`, `up-textarea`, `up-switch`, `up-radio-group`, `up-picker` trigger |
| Notes | keep page model explicit; use Vue 3 slot syntax where needed |

## up-picker

| Concern | Contract |
|---|---|
| Visibility | `v-model:show="showPicker"` or `:show="showPicker"` |
| Data | `:columns="columns"` |
| Events | `@confirm`, `@change` |
| Optional selection binding | `v-model="selected"` |
| Notes | this skill follows the current `uview-plus` `columns` API |

## up-popup

| Concern | Contract |
|---|---|
| Visibility | `v-model:show="showPopup"` |
| Position | `mode="bottom"`, `mode="center"`, etc. |
| Events | `@open`, `@close` |
| Notes | default fix for exported custom sheets and overlays |

## up-upload

| Concern | Contract |
|---|---|
| Basic usage | `<up-upload :fileList="fileList" @afterRead="afterRead" @delete="onDelete" />` |
| Common props | `multiple`, `maxCount`, `previewFullImage`, `name` |
| Notes | prefer component-managed upload UX over custom dashed boxes |

## up-tabbar

| Concern | Contract |
|---|---|
| Basic usage | `<up-tabbar :value="value" @change="name => value = name">` |
| Items | `<up-tabbar-item name="home" text="首页" icon="home" />` |
| Notes | use `name` for route/app section identity |

## up-safe-bottom and up-status-bar

| Concern | Contract |
|---|---|
| Bottom CTA | wrap fixed action bars with `up-safe-bottom` |
| Top custom inset | use `up-status-bar` when not relying on `up-navbar` |
| Notes | these two components are part of the stronger page-shell guidance of this skill |
