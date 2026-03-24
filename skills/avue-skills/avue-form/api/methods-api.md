# Methods API

## API Reference

Avue-form methods API.

### validate(callback)

Validate entire form.

**Parameters:**
- `callback`: `(valid: boolean) => void` - Validation callback

**Example:**
```javascript
this.$refs.form.validate((valid) => {
  if (valid) {
    console.log('Validation passed')
  } else {
    console.log('Validation failed')
  }
})
```

### validateField(prop, callback)

Validate specific field.

**Parameters:**
- `prop`: `string` - Field property name
- `callback`: `(errorMessage?: string) => void` - Validation callback

**Example:**
```javascript
this.$refs.form.validateField('name', (errorMessage) => {
  if (errorMessage) {
    console.log('Error:', errorMessage)
  } else {
    console.log('Valid')
  }
})
```

### resetFields()

Reset all form fields to initial values.

**Example:**
```javascript
this.$refs.form.resetFields()
```

### clearValidate()

Clear all validation errors.

**Example:**
```javascript
this.$refs.form.clearValidate()
```

### getPropRef(prop)

Get field component reference.

**Parameters:**
- `prop`: `string` - Field property name

**Returns:** Field component reference

**Example:**
```javascript
const fieldRef = this.$refs.form.getPropRef('name')
```

**See also:** `examples/components/methods.md` for detailed examples
