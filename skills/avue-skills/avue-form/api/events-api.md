# Events API

## API Reference

Avue-form events API.

### Form Events

**@submit**
- Parameters: `(form, done)`
- Description: Form submit event
- `form`: Form data object
- `done`: Callback function to close loading

**@reset-change**
- Parameters: `()`
- Description: Form reset event

**@change**
- Parameters: `(value, column)`
- Description: Form value change event
- `value`: Changed value
- `column`: Column configuration

**@column-change**
- Parameters: `(value, column)`
- Description: Column value change event

### Column Events

**change**
- Type: `Function`
- Parameters: `(value)`
- Description: Column value change handler

**click**
- Type: `Function`
- Parameters: `(value)`
- Description: Column click handler

### Event Usage

```vue
<template>
  <avue-form 
    :option="option" 
    v-model="form"
    @submit="handleSubmit"
    @reset-change="handleReset"
    @change="handleChange"
  ></avue-form>
</template>
```

### Column Event Usage

```javascript
column: [
  {
    label: 'Select',
    prop: 'select',
    type: 'select',
    change: (value) => {
      console.log('Changed:', value)
    }
  }
]
```

**See also:** `examples/components/events.md` for detailed examples
