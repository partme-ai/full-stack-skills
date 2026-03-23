# Component API

## API Reference

Element Plus component props, events, and methods.

### Common Props

Most components support:
- `size` - Component size (large, default, small)
- `disabled` - Disabled state
- `className` - Custom class name
- `style` - Custom style

### Common Events

Most components emit:
- `@click` - Click event
- `@change` - Change event
- `@focus` - Focus event
- `@blur` - Blur event

### Button Component

**Props:**
- `type` - Button type (primary, success, info, warning, danger)
- `size` - Button size (large, default, small)
- `disabled` - Disabled state
- `loading` - Loading state
- `plain` - Plain button
- `round` - Round button
- `circle` - Circle button
- `icon` - Icon component

**Events:**
- `@click` - Click event

### Input Component

**Props:**
- `v-model` - Input value
- `type` - Input type (text, password, textarea)
- `size` - Input size (large, default, small)
- `disabled` - Disabled state
- `readonly` - Readonly state
- `clearable` - Show clear button
- `show-password` - Show password toggle
- `placeholder` - Placeholder text
- `maxlength` - Max length

**Events:**
- `@input` - Input event
- `@change` - Change event
- `@focus` - Focus event
- `@blur` - Blur event

**Slots:**
- `prefix` - Prefix content
- `suffix` - Suffix content
- `prepend` - Prepend content
- `append` - Append content

### Form Component

**Props:**
- `model` - Form data object
- `rules` - Validation rules
- `label-width` - Label width
- `label-position` - Label position (left, right, top)

**Methods:**
- `validate` - Validate form
- `validateField` - Validate specific field
- `resetFields` - Reset form fields
- `clearValidate` - Clear validation

**Events:**
- `@validate` - Validation event

### Table Component

**Props:**
- `data` - Table data
- `columns` - Table columns
- `stripe` - Stripe rows
- `border` - Show border
- `size` - Table size

**Events:**
- `@selection-change` - Selection change event
- `@row-click` - Row click event
- `@sort-change` - Sort change event

**See also:** `examples/components/` for detailed component examples
