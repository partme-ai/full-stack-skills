# Component API

## API Reference

Layui Vue component props, events, and methods.

### Common Props

Most components support:
- `size` - Component size (lg, md, sm, xs)
- `disabled` - Disabled state
- `loading` - Loading state

### Common Events

Most components emit:
- `@click` - Click event
- `@change` - Change event
- `@input` - Input event

### Button Component

**Props:**
- `type` - Button type (primary, normal, warm, danger)
- `size` - Button size
- `disabled` - Disabled state
- `loading` - Loading state
- `icon` - Icon name

**Events:**
- `@click` - Click event

### Table Component

**Props:**
- `columns` - Column configuration
- `dataSource` - Table data
- `pagination` - Pagination config
- `sortable` - Enable sorting
- `checkbox` - Enable row selection

**Events:**
- `@change` - Pagination/sort change
- `@select` - Row selection change

### DatePicker Component

**Props:**
- `v-model` - Selected date
- `type` - Picker type (date, datetime, year, month, daterange)
- `format` - Date format
- `shortcuts` - Date shortcuts

**Events:**
- `@change` - Date change event

### Input Component

**Props:**
- `v-model` - Input value
- `placeholder` - Placeholder text
- `disabled` - Disabled state
- `readonly` - Readonly state
- `prefixIcon` - Prefix icon
- `suffixIcon` - Suffix icon

**Events:**
- `@input` - Input event
- `@change` - Change event
- `@blur` - Blur event
- `@focus` - Focus event

**See also:** `examples/components/` for detailed component examples
