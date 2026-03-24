# Components API | 组件 API

## API Reference

uView UI component APIs and props.

### Common Props

Most components share common props:

- `custom-style`: Custom style object
- `custom-class`: Custom CSS class
- `disabled`: Disabled state
- `loading`: Loading state

### Button API

**Props:**
- `type`: Button type (primary, success, error, warning, info)
- `size`: Button size (default, medium, mini)
- `shape`: Button shape (square, circle)
- `plain`: Plain button style
- `disabled`: Disabled state
- `loading`: Loading state
- `icon`: Icon name
- `@click`: Click handler

### Input API

**Props:**
- `v-model`: Input value
- `type`: Input type (text, number, password, etc.)
- `placeholder`: Placeholder text
- `clearable`: Show clear button
- `disabled`: Disabled state
- `error`: Error state
- `error-message`: Error message
- `prefix-icon`: Prefix icon
- `suffix-icon`: Suffix icon
- `@input`: Input event
- `@change`: Change event

### Form API

**Props:**
- `:model`: Form data object
- `:rules`: Validation rules
- `ref`: Form reference

**Methods:**
- `validate()`: Validate form
- `resetFields()`: Reset form fields

**Form.Item Props:**
- `label`: Field label
- `prop`: Field name (for validation)
- `required`: Required indicator

### Modal API

**Props:**
- `v-model`: Modal visibility
- `title`: Modal title
- `content`: Modal content
- `show-cancel-button`: Show cancel button
- `confirm-text`: Confirm button text
- `cancel-text`: Cancel button text
- `@confirm`: Confirm handler
- `@cancel`: Cancel handler

### Toast API

**Props (via $u.toast):**
- `type`: Toast type (success, error, warning, loading)
- `message`: Toast message
- `duration`: Toast duration (milliseconds)
- `position`: Toast position (top, center, bottom)

### Key Points

- All components support custom-style and custom-class props
- Most components support disabled and loading props
- Form components use v-model for two-way binding
- Modal uses v-model for visibility control
- Toast is available via $u.toast() method
- Components work in uni-app pages
