# Bootstrap-Vue Design Contract

## 1. Design Tokens (Hard Constraints)

### Colors (Bootstrap 5 Standard)
- **Primary**: `#0d6efd` (Blue)
- **Secondary**: `#6c757d` (Gray)
- **Success**: `#198754` (Green)
- **Danger**: `#dc3545` (Red)
- **Warning**: `#ffc107` (Yellow)
- **Info**: `#0dcaf0` (Cyan)
- **Light**: `#f8f9fa`
- **Dark**: `#212529`

### Spacing System (Utility Classes)
- `0`: 0
- `1`: 0.25rem (4px)
- `2`: 0.5rem (8px)
- `3`: 1rem (16px) - **Default**
- `4`: 1.5rem (24px)
- `5`: 3rem (48px)
- Usage: `m-3`, `p-4`, `mb-2`, `py-5`, `gap-3`.

### Typography
- **Font Family**: System UI stack (San Francisco, Segoe UI, Roboto).
- **Headings**: `h1` through `h6` classes.
- **Lead**: `.lead` for emphasis.

### Radius & Shadows
- **Radius**: `rounded` (0.25rem), `rounded-pill` (50rem), `rounded-circle`.
- **Shadows**: `shadow-sm`, `shadow`, `shadow-lg`, `shadow-none`.

## 2. Component Contracts

### Layout (Grid)
- **Container**: `<b-container fluid>` or `<b-container>`.
- **Row**: `<b-row>`.
- **Column**: `<b-col cols="12" md="6" lg="4">`.
- **Invariant**: Do not use raw CSS grid or flexbox unless strictly necessary; prefer `<b-row>`/`<b-col>` or `d-flex` utilities.

### Buttons
- **Tag**: `<b-button>`
- **Variants**: `variant="primary"`, `variant="outline-danger"`.
- **Sizes**: `size="sm"`, `size="lg"`.
- **Invariant**: Do not write `<button class="btn btn-primary">`.

### Forms
- **Group**: `<b-form-group label="Email address" description="...">`
- **Input**: `<b-form-input type="email" placeholder="...">`
- **Select**: `<b-form-select :options="options">`
- **Checkbox**: `<b-form-checkbox>`
- **Invariant**: Always wrap inputs in `b-form-group` for proper spacing and labeling.

### Cards
- **Tag**: `<b-card>`
- **Structure**:
  ```html
  <b-card title="Card Title" img-src="..." img-top>
    <b-card-text>
      Some quick example text.
    </b-card-text>
    <b-button href="#" variant="primary">Go somewhere</b-button>
  </b-card>
  ```

### Tables
- **Tag**: `<b-table striped hover :items="items">`
- **Invariant**: Use prop-driven configuration over manual `<thead>`/`<tbody>` construction when possible.

## 3. Layout Invariants

- **Responsive First**: Always define mobile layout (`cols="12"`) then override for larger screens (`md="6"`).
- **Accessibility**: All interactive elements must have aria-labels or visible text.
