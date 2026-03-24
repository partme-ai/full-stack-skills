# Components API | 组件 API

## API Reference

Bootstrap Vue 3.0 component APIs and props.

### Common Props

Most components share common props:

- `variant`: Component variant (primary, success, danger, etc.)
- `size`: Component size (sm, md, lg)
- `disabled`: Disabled state
- `class`: Additional CSS classes

### Button API

**Props:**
- `variant`: Button variant (primary, success, danger, warning, info, light, dark)
- `size`: Button size (sm, md, lg)
- `disabled`: Disabled state
- `type`: Button type (button, submit, reset)
- `onClick`: Click handler

### Form API

**Props:**
- `@submit`: Submit handler
- `@reset`: Reset handler

**Form.Input Props:**
- `v-model`: Input value
- `type`: Input type (text, email, password, etc.)
- `placeholder`: Placeholder text
- `required`: Required field
- `:state`: Validation state

### Table API

**Props:**
- `items`: Table data array
- `fields`: Column definitions
- `sortable`: Enable sorting
- `selectable`: Enable row selection
- `select-mode`: Selection mode (single, multi)
- `v-model:selected`: Selected rows

### Modal API

**Props:**
- `v-model`: Modal visibility
- `title`: Modal title
- `size`: Modal size (sm, lg, xl)
- `@ok`: OK button handler
- `@cancel`: Cancel button handler

**Methods:**
- `show()`: Show modal
- `hide()`: Hide modal

### Grid API

**Container Props:**
- `fluid`: Fluid container

**Row Props:**
- `align-v`: Vertical alignment
- `align-h`: Horizontal alignment

**Col Props:**
- `cols`: Column width
- `sm`, `md`, `lg`, `xl`, `xxl`: Responsive widths
- `offset`: Column offset

### Key Points

- All components support variant and size props
- Form components use v-model for two-way binding
- Table uses items and fields pattern
- Modal uses v-model for visibility control
- Grid system follows Bootstrap 5 breakpoints
