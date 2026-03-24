# Components API | 组件 API

**适用范围**：本文件只总结当前本地 skill 已覆盖的组件与能力，不声称覆盖全部 Vant 组件。

**当前本地覆盖组件**：

- Button
- Cell
- Form / Field
- Dialog
- Toast
- Popup

**关联示例文件**：

- Button → `examples/components/button.md`
- Cell → `examples/components/cell.md`
- Form → `examples/components/form.md`
- Dialog → `examples/components/dialog.md`
- Toast → `examples/components/toast.md`
- Popup → `examples/components/popup.md`

## Common usage rules

- 所有组件示例默认使用 Vue 3 `script setup`
- 所有组件从 `vant` 导入
- 交互型组件优先保持移动端使用场景
- 需要主题配置时，配合 `api/config-provider.md`

## Button API summary

**Use when**:

- 需要操作按钮
- 需要提交、确认、触发事件入口

**Common props**:

- `type`: `primary` / `success` / `warning` / `danger` / `default`
- `size`: `large` / `normal` / `small` / `mini`
- `shape`: `square` / `round`
- `plain`: plain style
- `disabled`: disabled state
- `loading`: loading state
- `icon`: icon name

**Common events**:

- `@click`

**See also**:

- `examples/components/button.md`

## Cell API summary

**Use when**:

- 需要列表项、信息项、跳转入口

**Common props**:

- `title`
- `value`
- `label`
- `icon`
- `is-link`
- `arrow-direction`

**Common events**:

- `@click`

**Related components**:

- `CellGroup`

**See also**:

- `examples/components/cell.md`

## Form API summary

**Use when**:

- 需要登录、注册、资料编辑、校验提交

**Core components**:

- `Form`
- `Field`
- `CellGroup`
- `Button`

**Common events**:

- `@submit`
- `@failed`

**Common methods**:

- `validate()`
- `resetValidation()`

**Common field props**:

- `v-model`
- `name`
- `label`
- `placeholder`
- `:rules`
- `type`
- `disabled`

**See also**:

- `examples/components/form.md`

## Dialog API summary

**Use when**:

- 需要确认、警告、阻断式提示、带表单输入的弹窗

**Component props**:

- `v-model:show`
- `title`
- `message`
- `show-cancel-button`
- `confirm-button-text`
- `cancel-button-text`

**Component events**:

- `@confirm`
- `@cancel`

**Programmatic APIs**:

- `showDialog(options)`
- `showConfirmDialog(options)`

**See also**:

- `examples/components/dialog.md`

## Toast API summary

**Use when**:

- 需要轻提示、成功提示、失败提示、加载提示

**Programmatic APIs**:

- `showToast(message | options)`
- `showSuccessToast(message)`
- `showFailToast(message)`
- `showLoadingToast(message)`

**Common options**:

- `type`
- `message`
- `duration`
- `position`

**Component usage**:

- `van-toast` with `v-model:show`

**See also**:

- `examples/components/toast.md`

## Popup API summary

**Use when**:

- 需要底部弹层、侧边滑出层、中间弹层、可关闭容器

**Common props**:

- `v-model:show`
- `position`
- `round`
- `closeable`
- `close-icon-position`
- `overlay`

**Common events**:

- `@close`

**See also**:

- `examples/components/popup.md`

## Selection guide

- If the user asks for a primary action control, start with **Button**
- If the user asks for list-style navigation or info rows, start with **Cell**
- If the user asks for data entry or validation, start with **Form**
- If the user asks for confirmation or interruption, start with **Dialog**
- If the user asks for lightweight feedback, start with **Toast**
- If the user asks for overlay content or slide-up panels, start with **Popup**
