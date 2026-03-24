# Element Plus Design Contract (Stitch HTML → Vue SFC Mapping)

When converting Stitch-generated HTML to Vue 3 + Element Plus, map structure and styles to the following. Align with stitch-ui-design-spec-element-plus (same repo) for generation-time constraints.

## 1. Design Tokens

### Colors (Standard Theme)
- **Primary**: `#409EFF` (Blue)
- **Success**: `#67C23A` (Green)
- **Warning**: `#E6A23C` (Orange)
- **Danger**: `#F56C6C` (Red)
- **Info**: `#909399` (Gray)
- **Text Primary**: `#303133`, **Text Regular**: `#606266`, **Text Secondary**: `#909399`, **Border**: `#DCDFE6` / `#E4E7ED`

### Typography
- **Font Family**: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif.
- **Sizes**: Extra Large 20px, Large 18px, Medium 16px, Base 14px (default), Small 13px, Extra Small 12px.

### Radius
- Small: `2px`, Base: `4px`, Round: `20px` (or `9999px` for capsules).

## 2. Component Mapping (Stitch HTML → Element Plus)

**Rule: Use framework components when available; do not replace with generic div/span + custom class.** Use **el-card** for cards (shadow, #header slot), **el-alert** for tips/notices. No custom `.card`, `.card-header`, `.card-title`, `.label-optional`, `.tips-text` when el-* equivalents exist.

### Layout (24-column Grid)
- **Row**: `<el-row :gutter="20">`
- **Col**: `<el-col :span="12" :xs="24" :sm="12" :md="8">`
- **Container**: `<el-container>`, `<el-header>`, `<el-aside>`, `<el-main>`, `<el-footer>`
- **Card**: **el-card** with `shadow="hover"` and `#header` slot if needed; do not use `<div class="card">` + custom header.
- **Tips / notice**: **el-alert** with `type="info"` or `type="warning"`; do not use raw div + .tips-text.

### Buttons
- **Tag**: `<el-button>`
- **Types**: `type="primary" | success | warning | danger | info"`
- **Props**: `plain`, `round`, `circle`; **Sizes**: `large`, `default`, `small`

### Forms
- **Wrapper**: `<el-form :model="form" label-width="120px">`
- **Item**: `<el-form-item label="...">`
- **Input**: `<el-input v-model="form.name" placeholder="..." />`
- **Select**: `<el-select v-model="form.region">` with `<el-option label="..." value="..." />`
- **Switch**: `<el-switch v-model="form.delivery" />`
- **Checkbox**: `<el-checkbox-group v-model="form.type">`

### Data Display
- **Table**: `<el-table :data="tableData">` + `<el-table-column prop="..." label="..." />`
- **Card**: **el-card** `<el-card shadow="hover">` with `#header` slot if needed — use for all card/section blocks; do not use div.card.
- **Tag**: `<el-tag type="success">...</el-tag>`
- **Empty**: `<el-empty description="No Data" />`

### Navigation
- **Menu**: `<el-menu mode="horizontal">` + `<el-sub-menu>`, `<el-menu-item>`
- **Breadcrumb**: `<el-breadcrumb>` + `<el-breadcrumb-item>`
- **Tabs**: `<el-tabs v-model="activeName">` + `<el-tab-pane label="..." name="...">`

### Feedback
- **Dialog**: `<el-dialog v-model="visible" title="...">`
- **Drawer**: `<el-drawer v-model="drawer" title="...">`
- **Alert**: `<el-alert title="..." type="info" />`

## 3. Icons
- Use `@element-plus/icons-vue`; wrap in `<el-icon :size="20" color="#409EFC">` with icon component inside.

## 4. Component API quick reference
- See [api/component-api.md](../api/component-api.md) for Layout / Button / Form / Table / Card / Dialog / Tabs props and events.

## 5. Invariants

- **Use framework components when available**: Card → **el-card**; tips/notices → **el-alert**. No custom .card, .card-header, .card-title, .tips-text when el-* components exist.
- Do not use raw `<button class="...">` when `<el-button>` applies; do not use `<div class="card">` when `<el-card>` applies.
- Use prop-driven configuration (e.g. `el-table :data`, `el-table-column`) over manual thead/tbody.
- Ensure form items have labels; use tooltip for icon-only buttons.
- Form validation: bind `:rules` on `el-form-item`, call `formRef.validate()` on submit.
