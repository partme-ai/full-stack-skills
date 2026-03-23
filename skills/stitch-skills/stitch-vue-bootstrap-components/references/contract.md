# Bootstrap-Vue Design Contract (Stitch HTML → Vue SFC Mapping)

When converting Stitch-generated HTML to Vue 3 + BootstrapVue (or BootstrapVueNext), map structure and styles to the following. Align with stitch-ui-design-spec-bootstrap for generation-time constraints. Target: [BootstrapVue Vue 3](https://bootstrap-vue.org/vue3) or BootstrapVueNext (Bootstrap 5 + Vue 3).

## 1. Design Tokens

### Colors (Bootstrap 5 Standard)
- **Primary**: `#0d6efd`, **Secondary**: `#6c757d`, **Success**: `#198754`, **Danger**: `#dc3545`, **Warning**: `#ffc107`, **Info**: `#0dcaf0`, **Light**: `#f8f9fa`, **Dark**: `#212529`

### Spacing (Utility Classes)
- Scale: `0`–`5` (0, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem). Usage: `m-3`, `p-4`, `mb-2`, `py-5`, `gap-3`.

### Typography
- **Font**: System UI stack (San Francisco, Segoe UI, Roboto). **Headings**: `h1`–`h6` classes. **Lead**: `.lead`.

### Radius & Shadows
- **Radius**: `rounded`, `rounded-pill`, `rounded-circle`. **Shadows**: `shadow-sm`, `shadow`, `shadow-lg`, `shadow-none`.

## 2. Component Mapping (Stitch HTML → Bootstrap Vue)

**Rule: Use framework components when available; do not replace with generic div/span + custom class.** Use **b-card** for cards (title, body), **b-alert** for tips/notices, **b-form-group** with label/description for form hints. No custom `.card`, `.card-header`, `.card-title`, `.label-optional`, `.tips-text` when b-* equivalents exist.

### Layout (Grid)
- **Container**: `<b-container fluid>` or `<b-container>`
- **Row**: `<b-row>`
- **Column**: `<b-col cols="12" md="6" lg="4">`
- **Card**: **b-card** with `title` or `#header` slot; **b-card-text** for body. Do not use `<div class="card">` + custom header/title.
- **Alert / tips**: **b-alert** with `variant="info"` or `variant="warning"`; do not use raw div + .tips-text.
- **Invariant**: Do not use raw CSS grid when `<b-row>`/`<b-col>` or `d-flex` utilities apply.

### Buttons
- **Tag**: `<b-button>`
- **Variants**: `variant="primary" | outline-danger"` etc.
- **Sizes**: `size="sm" | lg"`
- **Invariant**: Do not write `<button class="btn btn-primary">`.

### Forms
- **Group**: `<b-form-group label="..." description="...">`
- **Input**: `<b-form-input type="email" placeholder="...">`
- **Select**: `<b-form-select :options="options">`
- **Checkbox**: `<b-form-checkbox>`
- **Invariant**: Wrap inputs in `b-form-group` for spacing and labeling.

### Cards
- **Tag**: `<b-card>` — use for all card/section blocks. **Structure**: `<b-card title="..." img-src="..." img-top>`, `<b-card-text>`, `<b-button href="#" variant="primary">`. Do not use `<div class="card">` or custom card markup.

### Tables
- **Tag**: `<b-table striped hover :items="items" :fields="fields">` — fields: [{ key, label }, ...]; optional selectable, sortable, v-model:selected.
- **Invariant**: Use prop-driven configuration over manual thead/tbody when possible.

### Modal and feedback
- **Modal**: `<b-modal v-model="visible" title="..." @ok="onOk" @cancel="onCancel">`; size="sm"|lg|xl".
- **Button Group**: `<b-button-group>` wrapping multiple `<b-button>`.

## 3. Component API quick reference

- See [api/component-api.md](../api/component-api.md) for Button / Grid / Form / Table / Card / Modal props and events.

## 4. Layout Invariants

- **Use framework components when available**: Card → **b-card**; tips/notices → **b-alert**; form hints → **b-form-group** description or label. No custom .card, .card-header, .card-title, .tips-text when b-* components exist.
- **Responsive first**: Define mobile layout (`cols="12"`) then override for larger screens (`md="6"`).
- **Accessibility**: All interactive elements must have aria-labels or visible text.
- **No raw HTML for UI**: Use `<b-button>` not `<button class="btn">`; use `<b-table :items :fields>` not raw `<table>`; use `<b-card>` not `<div class="card">`.
