# Element Plus Design Contract

## 1. Design Tokens (Hard Constraints)

### Colors (Standard Theme)
- **Primary**: `#409EFF` (Blue)
- **Success**: `#67C23A` (Green)
- **Warning**: `#E6A23C` (Orange)
- **Danger**: `#F56C6C` (Red)
- **Info**: `#909399` (Gray)
- **Text Primary**: `#303133`
- **Text Regular**: `#606266`
- **Text Secondary**: `#909399`
- **Text Placeholder**: `#A8ABB2`
- **Border**: `#DCDFE6` (Base), `#E4E7ED` (Light)

### Typography
- **Font Family**: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif.
- **Font Sizes**:
  - Extra Large: 20px
  - Large: 18px
  - Medium: 16px
  - Base: 14px (Default)
  - Small: 13px
  - Extra Small: 12px

### Borders & Radius
- **Border Radius**:
  - Small: `2px`
  - Base: `4px`
  - Round: `20px` (or `9999px` for capsules)

## 2. Component Contracts

### Layout (24-column Grid)
- **Row**: `<el-row :gutter="20">` (Common gutter: 20px)
- **Col**: `<el-col :span="12" :xs="24" :sm="12" :md="8">`
- **Container**: `<el-container>`, `<el-header>`, `<el-aside>`, `<el-main>`, `<el-footer>`.

### Buttons
- **Tag**: `<el-button>`
- **Types**: `primary`, `success`, `warning`, `danger`, `info`.
- **Props**: `plain` (outline), `round` (rounded corners), `circle` (icon only).
- **Sizes**: `large`, `default`, `small`.

### Forms
- **Wrapper**: `<el-form :model="form" label-width="120px">`
- **Item**: `<el-form-item label="Activity name">`
- **Input**: `<el-input v-model="form.name" placeholder="Please input" />`
- **Select**: `<el-select v-model="form.region" placeholder="Select">`
  - Option: `<el-option label="Zone No.1" value="shanghai" />`
- **Switch**: `<el-switch v-model="form.delivery" />`
- **Checkbox**: `<el-checkbox-group v-model="form.type">`

### Data Display
- **Table**: `<el-table :data="tableData" style="width: 100%">`
  - Column: `<el-table-column prop="date" label="Date" width="180" />`
- **Descriptions**: `<el-descriptions title="Info" :column="3" border>` (Key-value display)
  - Item: `<el-descriptions-item label="Username">kooriookami</el-descriptions-item>`
- **Card**: `<el-card class="box-card" shadow="hover">`
  - Header slot: `<template #header><div class="card-header">...</div></template>`
- **Tag**: `<el-tag type="success">Tag 2</el-tag>`
- **Timeline**: `<el-timeline><el-timeline-item timestamp="2023/4/12" placement="top">...</el-timeline-item></el-timeline>`
- **Empty**: `<el-empty description="No Data" />`
- **Carousel**: `<el-carousel height="150px"><el-carousel-item v-for="item in 4" :key="item">...</el-carousel-item></el-carousel>`

### Navigation
- **Menu**: `<el-menu mode="horizontal" :default-active="activeIndex">`
  - SubMenu: `<el-sub-menu index="1"><template #title>Workspace</template>...</el-sub-menu>`
  - Item: `<el-menu-item index="1">Processing Center</el-menu-item>`
- **Breadcrumb**: `<el-breadcrumb separator="/"><el-breadcrumb-item>Home</el-breadcrumb-item>...</el-breadcrumb>`
- **Tabs**: `<el-tabs v-model="activeName"><el-tab-pane label="User" name="first">...</el-tab-pane></el-tabs>`
- **Steps**: `<el-steps :active="1"><el-step title="Step 1" /></el-steps>`

### Feedback
- **Dialog**: `<el-dialog v-model="visible" title="Tips">...</el-dialog>`
- **Drawer**: `<el-drawer v-model="drawer" title="I am the title">...</el-drawer>`
- **Alert**: `<el-alert title="Info alert" type="info" />`
- **Message**: `ElMessage.success('Congrats, this is a success message.')` (JS usage)
- **Notification**: `ElNotification(...)`

## 3. Icons
- **Library**: `@element-plus/icons-vue`
- **Usage**:
  ```html
  <el-icon :size="20" color="#409EFC">
    <Edit />
  </el-icon>
  ```
- **Invariant**: Do not use raw SVG or FontAwesome unless specified. Use Element Plus icons wrapped in `<el-icon>`.

## 4. Accessibility & Interaction
- Use `tooltip` for icon-only buttons.
- Ensure form items have labels.
- Use `loading` state on buttons during async actions.
