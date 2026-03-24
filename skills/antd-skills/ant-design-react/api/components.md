# Components API | 组件 API

## API Reference

Ant Design React component APIs and props.

### Common Props

Most components share common props:

- `className`: Additional CSS class
- `style`: Inline style object
- `disabled`: Disabled state
- `loading`: Loading state
- `size`: Component size (large, middle, small)

### Button API

**Props:**
- `type`: Button type (primary, default, dashed, text, link)
- `size`: Button size (large, middle, small)
- `shape`: Button shape (default, round, circle)
- `icon`: Icon component
- `loading`: Loading state
- `disabled`: Disabled state
- `onClick`: Click handler

### Form API

**Props:**
- `form`: Form instance from Form.useForm()
- `layout`: Form layout (horizontal, vertical, inline)
- `onFinish`: Submit handler
- `onFinishFailed`: Failed submit handler
- `initialValues`: Initial form values

**Form.Item Props:**
- `name`: Field name
- `label`: Field label
- `rules`: Validation rules
- `required`: Required indicator

### Table API

**Props:**
- `columns`: Column definitions
- `dataSource`: Table data
- `pagination`: Pagination config
- `rowSelection`: Row selection config
- `onChange`: Table change handler

**Column Props:**
- `title`: Column title
- `dataIndex`: Data field name
- `key`: Unique key
- `sorter`: Sort function
- `render`: Custom render function

### Input API

**Props:**
- `value`: Input value
- `defaultValue`: Default value
- `placeholder`: Placeholder text
- `size`: Input size
- `prefix`: Prefix element
- `suffix`: Suffix element
- `onChange`: Change handler

### Select API

**Props:**
- `value`: Selected value
- `defaultValue`: Default value
- `mode`: Selection mode (multiple, tags)
- `showSearch`: Enable search
- `onChange`: Change handler

### Modal API

**Props:**
- `open`: Modal visibility
- `title`: Modal title
- `onOk`: OK button handler
- `onCancel`: Cancel button handler
- `footer`: Custom footer
- `width`: Modal width

**Static Methods:**
- `Modal.info()`, `Modal.success()`, `Modal.error()`, `Modal.warning()`, `Modal.confirm()`

### Key Points

- All components support className and style props
- Most components support size and disabled props
- Form components use controlled/uncontrolled pattern
- Table uses columns and dataSource pattern
- Modal supports both component and static method usage
