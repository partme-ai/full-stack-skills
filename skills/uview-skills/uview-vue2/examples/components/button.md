# Button | 按钮

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates how to use the Button component in uView UI.

### Key Concepts

- Button types (primary, success, error, warning, info)
- Button sizes (default, medium, mini)
- Button shapes (square, circle)
- Button states (disabled, loading)
- Button with icons

### Example: Button Types

```vue
<template>
  <view>
    <u-button type="primary">Primary</u-button>
    <u-button type="success">Success</u-button>
    <u-button type="error">Error</u-button>
    <u-button type="warning">Warning</u-button>
    <u-button type="info">Info</u-button>
  </view>
</template>

<script>
export default {
  name: 'ButtonExample'
}
</script>
```

### Example: Button Sizes

```vue
<template>
  <view>
    <u-button type="primary" size="default">Default</u-button>
    <u-button type="primary" size="medium">Medium</u-button>
    <u-button type="primary" size="mini">Mini</u-button>
  </view>
</template>

<script>
export default {
  name: 'ButtonExample'
}
</script>
```

### Example: Button with Icon

```vue
<template>
  <u-button type="primary" icon="search">
    Search
  </u-button>
</template>

<script>
export default {
  name: 'ButtonExample'
}
</script>
```

### Example: Loading State

```vue
<template>
  <u-button
    type="primary"
    :loading="loading"
    @click="handleClick"
  >
    Click Me
  </u-button>
</template>

<script>
export default {
  data() {
    return {
      loading: false
    }
  },
  methods: {
    handleClick() {
      this.loading = true
      setTimeout(() => {
        this.loading = false
      }, 2000)
    }
  }
}
</script>
```

### Example: Disabled Button

```vue
<template>
  <view>
    <u-button type="primary" :disabled="true">Disabled</u-button>
    <u-button :disabled="disabled">Toggle Disabled</u-button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      disabled: false
    }
  }
}
</script>
```

### Key Points

- Use `type` prop for button style (primary, success, error, etc.)
- Use `size` prop for button size (default, medium, mini)
- Use `icon` prop for icon buttons
- Use `loading` prop for loading state
- Use `disabled` prop to disable button
- Button supports all standard HTML button attributes
- Works in uni-app pages
