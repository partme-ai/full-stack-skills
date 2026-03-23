# Basic Usage | 基本用法

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates basic uView UI component usage in uni-app.

### Key Concepts

- Using components
- Component props
- Component events
- Vue 2 Options API

### Example: Button Component

```vue
<template>
  <view>
    <u-button type="primary">Primary</u-button>
    <u-button type="success">Success</u-button>
    <u-button type="error">Error</u-button>
  </view>
</template>

<script>
export default {
  name: 'Example'
}
</script>
```

### Example: Button with Events

```vue
<template>
  <u-button type="primary" @click="handleClick">
    Click Me
  </u-button>
</template>

<script>
export default {
  methods: {
    handleClick() {
      this.$u.toast('Button clicked!')
    }
  }
}
</script>
```

### Example: Input Component

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

### Example: Multiple Components

```vue
<template>
  <view>
    <u-card title="Example Card">
      <u-input v-model="value" placeholder="Enter text" />
      <u-button type="primary" class="u-m-t-20">Submit</u-button>
    </u-card>
  </view>
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

- Use uView UI components with u- prefix
- Use v-model for two-way binding
- Use @click for event handling
- Use Vue 2 Options API (data, methods, etc.)
- Components work in uni-app pages
- Use uView UI utility classes for styling
