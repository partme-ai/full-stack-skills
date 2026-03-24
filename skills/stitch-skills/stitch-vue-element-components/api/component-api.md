# Element Plus Component API (Stitch conversion reference)

Use for precise Stitch HTML → Vue 3 + Element Plus mapping. Component prefix `el-`.

## Common conventions

- Form fields use v-model; layout uses el-row / el-col with :span, :gutter.
- Common props: disabled, loading, size (large / default / small).

## Layout

| Use | Syntax | Notes |
|-----|--------|-------|
| Row | `<el-row :gutter="20">` | gutter = column gap (px) |
| Col | `<el-col :span="12" :xs="24" :sm="12" :md="8">` | 24-column grid; xs/sm/md/lg responsive |
| Container | `<el-container>` with `<el-header>` `<el-aside>` `<el-main>` `<el-footer>` | page skeleton |

## Button

| Use | Syntax | Notes |
|-----|--------|-------|
| Type | `type="primary" \| success \| warning \| danger \| info"` | primary / success / warning / danger / info |
| Size | `size="large" \| default \| small"` | large / default / small |
| Style | `plain`, `round`, `circle` | plain / round / circle |
| Icon | `<el-button><el-icon><Search /></el-icon></el-button>` | use @element-plus/icons-vue |
| Event | `@click="handler"` | click |

Do not use `<button class="...">`; use `<el-button>` only.

## Form

| Use | Syntax | Notes |
|-----|--------|-------|
| Form | `<el-form :model="form" label-width="120px" @submit.prevent>` | model binds data |
| Item | `<el-form-item label="Name" prop="name">` | prop matches model key and validation |
| Input | `<el-input v-model="form.name" placeholder="..." />` | optional clearable, show-password |
| Select | `<el-select v-model="form.region">` + `<el-option label="..." value="..." />` | multiple for multi-select |
| Switch | `<el-switch v-model="form.delivery" />` | boolean |
| Checkbox group | `<el-checkbox-group v-model="form.type">` + `<el-checkbox label="..." />` | array |
| Validation | `:rules="[{ required: true, message: '...' }]"` on el-form-item | call validate() on el-form ref on submit |

## Data display

| Use | Syntax | Notes |
|-----|--------|-------|
| Table | `<el-table :data="tableData">` + `<el-table-column prop="name" label="Name" />` | prop = data field |
| Card | `<el-card shadow="hover">` with optional #header slot | title, body slot |
| Tag | `<el-tag type="success">...</el-tag>` | type: success, warning, danger, info |
| Empty | `<el-empty description="No Data" />` | empty state |

## Navigation

| Use | Syntax | Notes |
|-----|--------|-------|
| Menu | `<el-menu mode="horizontal">` + `<el-sub-menu>`, `<el-menu-item>` | horizontal/vertical mode |
| Breadcrumb | `<el-breadcrumb>` + `<el-breadcrumb-item>` | breadcrumb path |
| Tabs | `<el-tabs v-model="activeName">` + `<el-tab-pane label="..." name="...">` | v-model = current pane name |

## Feedback

| Use | Syntax | Notes |
|-----|--------|-------|
| Dialog | `<el-dialog v-model="visible" title="...">` | v-model controls visibility |
| Drawer | `<el-drawer v-model="drawer" title="...">` | side drawer |
| Alert | `<el-alert title="..." type="info" />` | type: success, warning, error, info |

## Icons

- Install `@element-plus/icons-vue`; use component names like `<Search />`, `<Edit />` in template; optionally wrap in `<el-icon :size="20" color="#409EFF">`.

## References

- [references/contract.md](../references/contract.md) — design tokens and mapping rules
- [references/official.md](../references/official.md) — official docs
