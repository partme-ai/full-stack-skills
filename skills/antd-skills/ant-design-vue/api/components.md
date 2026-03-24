# Components API | 组件 API

## API Reference

Ant Design Vue component APIs and props.

### Common Props

Most components share common props:
- `class`: Additional CSS class
- `style`: Inline style object
- `disabled`: Disabled state
- `loading`: Loading state
- `size`: Component size (large, middle, small)

### Button API

**Props:**
- `type`: Button type (primary, default, dashed, text, link)
- `size`: Button size (large, middle, small)
- `shape`: Button shape (default, round, circle)
- `icon`: Icon component slot
- `loading`: Loading state
- `disabled`: Disabled state
- `onClick`: Click handler

### Form API

**Props:**
- `model`: Data object of form
- `rules`: Validation rules
- `layout`: Form layout (horizontal, vertical, inline)
- `labelCol`: Label layout
- `wrapperCol`: Input wrapper layout
- `onFinish`: Submit handler
- `onFinishFailed`: Failed submit handler

**Form.Item Props:**
- `name`: Field name
- `label`: Field label
- `rules`: Validation rules
- `required`: Required indicator
- `hasFeedback`: Display feed icon

### Table API

**Props:**
- `columns`: Column definitions
- `dataSource`: Table data
- `pagination`: Pagination config
- `rowSelection`: Row selection config
- `loading`: Loading state
- `onChange`: Table change handler

**Column Props:**
- `title`: Column title
- `dataIndex`: Data field name
- `key`: Unique key
- `sorter`: Sort function
- `customRender`: Custom render function (slot name or function)

### Input API

**Props:**
- `value`: Input value (v-model:value)
- `placeholder`: Placeholder text
- `size`: Input size
- `prefix`: Prefix element slot
- `suffix`: Suffix element slot
- `allowClear`: Allow clear content
- `onChange`: Change handler

### Select API

**Props:**
- `value`: Selected value (v-model:value)
- `options`: Data of the select options
- `mode`: Selection mode (multiple, tags)
- `showSearch`: Enable search
- `filterOption`: Filter option logic
- `onChange`: Change handler

### Modal API

**Props:**
- `open`: Modal visibility (v-model:open)
- `title`: Modal title
- `onOk`: OK button handler
- `onCancel`: Cancel button handler
- `footer`: Custom footer
- `width`: Modal width

**Static Methods:**
- `Modal.info()`, `Modal.success()`, `Modal.error()`, `Modal.warning()`, `Modal.confirm()`

### Key Points

- Use `v-model:value` for most input components in V4 (changed from `v-model` in V2)
- Use `v-model:open` for Modal/Drawer visibility (changed from `visible`)
- Use `v-model:checked` for Checkbox/Switch
- Use `v-model:fileList` for Upload
