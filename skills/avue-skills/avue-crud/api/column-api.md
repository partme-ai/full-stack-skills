# Column API | 列 API

## API Reference

Avue CRUD column configuration API.

### Column Properties

**Basic:**
- `label`: Column label (string, required)
- `prop`: Column property (string, required)
- `type`: Input type (string: input/select/date/etc.)

**Display:**
- `width`: Column width (string/number)
- `minWidth`: Minimum width (string/number)
- `fixed`: Fixed column (string: left/right)
- `align`: Column alignment (string: left/center/right)
- `headerAlign`: Header alignment (string)
- `hide`: Hide column (boolean)
- `overHidden`: Overflow hidden (boolean)

**Functionality:**
- `search`: Enable search (boolean)
- `searchType`: Search input type (string)
- `searchPlaceholder`: Search placeholder (string)
- `sortable`: Enable sorting (boolean)
- `disabled`: Disable field (boolean)
- `readonly`: Readonly field (boolean)

**Validation:**
- `rules`: Validation rules (array)
- `required`: Required field (boolean)

**Data:**
- `dicData`: Dictionary data (array)
- `dicUrl`: Dictionary URL (string)
- `dicMethod`: Dictionary method (string)
- `dicQuery`: Dictionary query (object)

**Form:**
- `span`: Form span (number)
- `labelWidth`: Label width (number)
- `formatter`: Value formatter (function)
- `value`: Default value

### Column Types

- `input`: Text input
- `select`: Select dropdown
- `date`: Date picker
- `datetime`: DateTime picker
- `time`: Time picker
- `number`: Number input
- `switch`: Switch
- `checkbox`: Checkbox
- `radio`: Radio
- `upload`: Upload
- `textarea`: Textarea
- `password`: Password input
- `url`: URL input
- `email`: Email input

### Example: Column Configuration

```javascript
{
  label: 'Name',
  prop: 'name',
  type: 'input',
  width: 200,
  search: true,
  sortable: true,
  rules: [
    { required: true, message: 'Please enter name' }
  ]
}
```

### Key Points

- label and prop are required
- Use type for different input types
- Use rules for validation
- Use search for searchable columns
- Use dicData for select options
- Use formatter for value formatting
- All column properties are optional except label and prop
