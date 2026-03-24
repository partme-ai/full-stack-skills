# Toast | 提示

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates how to use the Toast tool ($u.toast) in uView UI.

### Key Concepts

- Basic toast
- Toast types (success, error, warning, loading)
- Toast with custom message
- Toast duration
- Toast position

### Example: Basic Toast

```vue
<template>
  <u-button @click="showToast">Show Toast</u-button>
</template>

<script>
export default {
  methods: {
    showToast() {
      this.$u.toast('This is a toast message')
    }
  }
}
</script>
```

### Example: Toast Types

```vue
<template>
  <view>
    <u-button @click="showSuccess">Success</u-button>
    <u-button @click="showError">Error</u-button>
    <u-button @click="showWarning">Warning</u-button>
    <u-button @click="showLoading">Loading</u-button>
  </view>
</template>

<script>
export default {
  methods: {
    showSuccess() {
      this.$u.toast({
        type: 'success',
        message: 'Success message'
      })
    },
    showError() {
      this.$u.toast({
        type: 'error',
        message: 'Error message'
      })
    },
    showWarning() {
      this.$u.toast({
        type: 'warning',
        message: 'Warning message'
      })
    },
    showLoading() {
      this.$u.toast({
        type: 'loading',
        message: 'Loading...'
      })
    }
  }
}
</script>
```

### Example: Toast with Options

```vue
<template>
  <u-button @click="showCustomToast">Custom Toast</u-button>
</template>

<script>
export default {
  methods: {
    showCustomToast() {
      this.$u.toast({
        type: 'success',
        message: 'Custom toast',
        duration: 3000,
        position: 'top'
      })
    }
  }
}
</script>
```

### Key Points

- Use `this.$u.toast()` for toast messages
- Use `type` prop for toast type (success, error, warning, loading)
- Use `message` prop for toast message
- Use `duration` prop for toast duration (milliseconds)
- Use `position` prop for toast position (top, center, bottom)
- Toast is available globally via $u object
- Works in uni-app pages
