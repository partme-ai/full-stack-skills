# Dialog | 对话框

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Dialog / 弹出框


## Instructions

This example demonstrates how to use the Dialog component in Vant.

### Key Concepts

- Basic Dialog
- Dialog with confirm
- Dialog with alert
- Dialog with custom content
- Dialog methods

### Example: Basic Dialog

```vue
<template>
  <van-button @click="show = true">Show Dialog</van-button>
  <van-dialog
    v-model:show="show"
    title="Title"
    message="This is a dialog message"
  />
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Dialog as VanDialog } from 'vant'

const show = ref(false)
</script>
```

### Example: Dialog with Confirm

```vue
<template>
  <van-button @click="showConfirm">Show Confirm</van-button>
</template>

<script setup>
import { Button as VanButton, showConfirmDialog } from 'vant'

const showConfirm = () => {
  showConfirmDialog({
    title: 'Confirm',
    message: 'Are you sure?'
  })
    .then(() => {
      console.log('Confirmed')
    })
    .catch(() => {
      console.log('Cancelled')
    })
}
</script>
```

### Example: Dialog with Alert

```vue
<template>
  <van-button @click="showAlert">Show Alert</van-button>
</template>

<script setup>
import { Button as VanButton, showDialog } from 'vant'

const showAlert = () => {
  showDialog({
    title: 'Alert',
    message: 'This is an alert'
  })
}
</script>
```

### Example: Dialog with Custom Content

```vue
<template>
  <van-button @click="show = true">Show Custom Dialog</van-button>
  <van-dialog
    v-model:show="show"
    title="Custom Dialog"
    show-cancel-button
    @confirm="handleConfirm"
    @cancel="show = false"
  >
    <van-field v-model="value" placeholder="Enter text" />
  </van-dialog>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Dialog as VanDialog, Field as VanField, showToast } from 'vant'

const show = ref(false)
const value = ref('')

const handleConfirm = () => {
  showToast(value.value)
  show.value = false
}
</script>
```

### Key Points

- Use `van-dialog` component for dialog display
- Use `v-model:show` for dialog visibility
- Use `title` prop for dialog title
- Use `message` prop for dialog message
- Use `showConfirmDialog()` for confirm dialogs
- Use `showDialog()` for alert dialogs
- Use `@confirm` and `@cancel` for button handlers

### Related local files

- API summary: `api/components.md`
- Feedback pattern: `examples/components/toast.md`
- Form-in-dialog pattern: `examples/components/form.md`
