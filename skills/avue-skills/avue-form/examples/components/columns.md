# Form Columns

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates form columns configuration in Avue-form.

### Key Concepts

- Column properties
- Column types
- Column layout
- Column validation

### Example: Basic Column

```javascript
column: [
  {
    label: 'Name',
    prop: 'name',
    type: 'input'
  }
]
```

### Example: Column with Validation

```javascript
column: [
  {
    label: 'Name',
    prop: 'name',
    type: 'input',
    rules: [
      { required: true, message: 'Please input name' },
      { min: 3, max: 20, message: 'Length should be 3-20' }
    ]
  }
]
```

### Example: Column Layout

```javascript
column: [
  {
    label: 'Name',
    prop: 'name',
    type: 'input',
    span: 12,        // Column span
    offset: 0,       // Column offset
    order: 0,        // Column order
    display: true    // Display column
  }
]
```

### Example: Column Types

```javascript
column: [
  {
    label: 'Input',
    prop: 'input',
    type: 'input'
  },
  {
    label: 'Select',
    prop: 'select',
    type: 'select',
    dicData: [
      { label: 'Option 1', value: '1' },
      { label: 'Option 2', value: '2' }
    ]
  },
  {
    label: 'Date',
    prop: 'date',
    type: 'date'
  }
]
```

### Key Points

- Define column properties
- Set column type
- Configure column layout
- Add validation rules
- Control column display
