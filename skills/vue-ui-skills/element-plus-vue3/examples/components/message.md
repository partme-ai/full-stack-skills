# Message Component

**官方文档**: https://element-plus.org/en-US/component/message.html


## Instructions

This example demonstrates the Message component in Element Plus.

### Key Concepts

- Message types
- Message duration
- Message positioning
- Message methods

### Example: Message API

```vue
<template>
  <el-button @click="showMessage">Show Message</el-button>
</template>

<script setup>
import { ElMessage } from 'element-plus'

const showMessage = () => {
  ElMessage.success('Success message')
}
</script>
```

### Example: Message Types

```vue
<script setup>
import { ElMessage } from 'element-plus'

// Success
ElMessage.success('Success message')

// Warning
ElMessage.warning('Warning message')

// Error
ElMessage.error('Error message')

// Info
ElMessage.info('Info message')
</script>
```

### Example: Message Options

```vue
<script setup>
import { ElMessage } from 'element-plus'

ElMessage({
  message: 'Custom message',
  type: 'success',
  duration: 3000,
  showClose: true,
  center: true
})
</script>
```

### Example: Message Positioning

```vue
<script setup>
import { ElMessage } from 'element-plus'

ElMessage({
  message: 'Top message',
  position: 'top'
})

ElMessage({
  message: 'Top-right message',
  position: 'top-right'
})
</script>
```

### Key Points

- Use ElMessage API for programmatic messages
- Multiple types: success, warning, error, info
- Configure duration and position
- Auto-close by default
- Support custom message content
