# Form Component API

## API Reference

Avue-form component props, events, and methods.

### Props

**v-model / value**
- Type: `Object`
- Default: `{}`
- Description: Form data object

**option**
- Type: `Object`
- Required: `true`
- Description: Form configuration options

**disabled**
- Type: `Boolean`
- Default: `false`
- Description: Disable form

**readonly**
- Type: `Boolean`
- Default: `false`
- Description: Readonly form

### Events

**@submit**
- Parameters: `(form, done)`
- Description: Form submit event

**@reset-change**
- Parameters: `()`
- Description: Form reset event

**@change**
- Parameters: `(value, column)`
- Description: Form value change event

**@column-change**
- Parameters: `(value, column)`
- Description: Column value change event

### Methods

**validate(callback)**
- Validate entire form
- Callback: `(valid) => void`

**validateField(prop, callback)**
- Validate specific field
- Parameters: `prop` - field property, `callback` - callback function

**resetFields()**
- Reset all form fields

**clearValidate()**
- Clear all validation errors

**getPropRef(prop)**
- Get field reference
- Parameters: `prop` - field property
- Returns: Field component reference

**See also:** `examples/components/` for detailed component examples
