# Input | 输入框

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates how to use the Input component in uView UI.

### Key Concepts

- Basic Input
- Input types
- Input with clear button
- Input validation
- Input with prefix/suffix

### Example: Basic Input

```vue
<template>
  <u-input
    v-model="value"
    placeholder="Enter text"
  />
</template>

<script>
export default {
  data() {
    return {
      value: ''
    }
  }
}
</script>
```

### Example: Input Types

```vue
<template>
  <view>
    <u-input v-model="text" type="text" placeholder="Text input" />
    <u-input v-model="number" type="number" placeholder="Number input" />
    <u-input v-model="password" type="password" placeholder="Password input" />
  </view>
</template>

<script>
export default {
  data() {
    return {
      text: '',
      number: '',
      password: ''
    }
  }
}
</script>
```

### Example: Input with Clear Button

```vue
<template>
  <u-input
    v-model="value"
    placeholder="Enter text"
    :clearable="true"
  />
</template>

<script>
export default {
  data() {
    return {
      value: ''
    }
  }
}
</script>
```

### Example: Input Validation

```vue
<template>
  <u-input
    v-model="value"
    placeholder="Enter text"
    :error="error"
    :error-message="errorMessage"
  />
</template>

<script>
export default {
  data() {
    return {
      value: '',
      error: false,
      errorMessage: ''
    }
  },
  watch: {
    value(newVal) {
      if (newVal.length < 6) {
        this.error = true
        this.errorMessage = 'At least 6 characters'
      } else {
        this.error = false
        this.errorMessage = ''
      }
    }
  }
}
</script>
```

### Example: Input with Prefix/Suffix

```vue
<template>
  <u-input
    v-model="value"
    placeholder="Search"
    prefix-icon="search"
    suffix-icon="arrow-right"
  />
</template>

<script>
export default {
  data() {
    return {
      value: ''
    }
  }
}
</script>
```

### Key Points

- Use `u-input` component for text input
- Use `v-model` for two-way binding
- Use `type` prop for input type
- Use `clearable` prop for clear button
- Use `error` and `error-message` for validation
- Use `prefix-icon` and `suffix-icon` for icons
- Input works in uni-app pages
