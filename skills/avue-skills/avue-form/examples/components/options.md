# Form Options

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates form options configuration in Avue-form.

### Key Concepts

- Option properties
- Layout options
- Button options
- Display options

### Example: Basic Options

```javascript
option: {
  labelWidth: 120,        // Label width
  labelPosition: 'right', // Label position
  size: 'medium',         // Form size
  submitBtn: true,        // Show submit button
  emptyBtn: true          // Show reset button
}
```

### Example: Layout Options

```javascript
option: {
  gutter: 20,             // Grid gutter
  span: 24,               // Default column span
  column: []              // Column definitions
}
```

### Example: Button Options

```javascript
option: {
  submitBtn: true,         // Show submit button
  submitText: 'Submit',   // Submit button text
  emptyBtn: true,         // Show reset button
  emptyText: 'Reset',     // Reset button text
  submitSize: 'medium',   // Submit button size
  emptySize: 'medium'     // Reset button size
}
```

### Example: Display Options

```javascript
option: {
  menuBtn: false,          // Show menu button
  menuAlign: 'center',    // Menu alignment
  menuSpan: 24,           // Menu span
  labelWidth: 120,        // Label width
  labelPosition: 'right'  // Label position
}
```

### Key Points

- Configure form appearance
- Control button display
- Set layout properties
- Customize form size
- Configure label position
