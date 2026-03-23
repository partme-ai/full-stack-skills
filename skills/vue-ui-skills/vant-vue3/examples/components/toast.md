# Toast | 提示

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Toast / 轻提示


## Instructions

This example demonstrates how to use the Toast component in Vant.

### Key Concepts

- Basic toast
- Toast types (success, fail, loading)
- Toast with custom message
- Toast duration
- Toast position

### Example: Basic Toast

```vue
<template>
  <van-button @click="showToast">Show Toast</van-button>
</template>

<script setup>
import { Button as VanButton, showToast } from 'vant'

const showToast = () => {
  showToast('This is a toast message')
}
</script>
```

### Example: Toast Types

```vue
<template>
  <van-button @click="showSuccess">Success</van-button>
  <van-button @click="showFail">Fail</van-button>
  <van-button @click="showLoading">Loading</van-button>
</template>

<script setup>
import { Button as VanButton, showToast, showSuccessToast, showFailToast, showLoadingToast } from 'vant'

const showSuccess = () => {
  showSuccessToast('Success message')
}

const showFail = () => {
  showFailToast('Fail message')
}

const showLoading = () => {
  showLoadingToast('Loading...')
}
</script>
```

### Example: Toast with Options

```vue
<template>
  <van-button @click="showCustomToast">Custom Toast</van-button>
</template>

<script setup>
import { Button as VanButton, showToast } from 'vant'

const showCustomToast = () => {
  showToast({
    type: 'success',
    message: 'Custom toast',
    duration: 3000,
    position: 'top'
  })
}
</script>
```

### Example: Using Toast Component

```vue
<template>
  <van-button @click="show = true">Show Toast</van-button>
  <van-toast v-model:show="show" message="Toast message" />
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Toast as VanToast } from 'vant'

const show = ref(false)
</script>
```

### Key Points

- Use `showToast()` function for toast messages
- Use `showSuccessToast()`, `showFailToast()`, `showLoadingToast()` for specific types
- Use options object for custom configuration
- Use `duration` prop for toast duration (milliseconds)
- Use `position` prop for toast position (top, middle, bottom)
- Use `van-toast` component for component-based usage
- Toast is available globally via showToast function

### Related local files

- API summary: `api/components.md`
- Dialog comparison: `examples/components/dialog.md`
