# Dialog Component

**官方文档**: https://element-plus.org/en-US/component/dialog.html


## Instructions

This example demonstrates the Dialog component in Element Plus.

### Key Concepts

- Dialog visibility
- Dialog content
- Dialog actions
- Dialog events
- Dialog methods

### Example: Basic Dialog

```vue
<template>
  <el-button @click="dialogVisible = true">Open Dialog</el-button>
  <el-dialog v-model="dialogVisible" title="Dialog Title">
    <span>Dialog Content</span>
    <template #footer>
      <el-button @click="dialogVisible = false">Cancel</el-button>
      <el-button type="primary" @click="dialogVisible = false">Confirm</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref } from 'vue'

const dialogVisible = ref(false)
</script>
```

### Example: Dialog with Form

```vue
<template>
  <el-button @click="dialogVisible = true">Open Dialog</el-button>
  <el-dialog v-model="dialogVisible" title="Form Dialog" width="500px">
    <el-form :model="form" label-width="100px">
      <el-form-item label="Name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="Email">
        <el-input v-model="form.email" />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="dialogVisible = false">Cancel</el-button>
      <el-button type="primary" @click="handleSubmit">Submit</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref } from 'vue'

const dialogVisible = ref(false)
const form = ref({
  name: '',
  email: ''
})

const handleSubmit = () => {
  console.log('Form:', form.value)
  dialogVisible.value = false
}
</script>
```

### Example: Dialog Methods

```vue
<template>
  <el-button @click="openDialog">Open Dialog</el-button>
</template>

<script setup>
import { ElMessageBox } from 'element-plus'

const openDialog = () => {
  ElMessageBox.confirm('Are you sure?', 'Confirm', {
    confirmButtonText: 'OK',
    cancelButtonText: 'Cancel',
    type: 'warning'
  }).then(() => {
    console.log('Confirmed')
  }).catch(() => {
    console.log('Cancelled')
  })
}
</script>
```

### Key Points

- Control visibility with v-model
- Use title prop for dialog title
- Customize footer with footer slot
- Support form inside dialog
- Use ElMessageBox for programmatic dialogs
