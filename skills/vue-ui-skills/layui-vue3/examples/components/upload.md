# Upload Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/upload


## Instructions

This example demonstrates the Upload component in Layui Vue.

### Key Concepts

- File upload
- Upload progress
- File validation
- Upload events

### Example: Basic Upload

```vue
<template>
  <lay-upload 
    :action="uploadUrl"
    @success="handleSuccess"
  ></lay-upload>
</template>

<script setup>
import { LayUpload } from '@layui/layui-vue'

const uploadUrl = '/api/upload'

const handleSuccess = (response) => {
  console.log('Upload success:', response)
}
</script>
```

### Example: Upload with Validation

```vue
<template>
  <lay-upload 
    :action="uploadUrl"
    :accept="'image/*'"
    :max-size="5 * 1024 * 1024"
    @error="handleError"
  ></lay-upload>
</template>

<script setup>
import { LayUpload } from '@layui/layui-vue'

const handleError = (error) => {
  console.log('Upload error:', error)
}
</script>
```

### Example: Multiple Files

```vue
<template>
  <lay-upload 
    :action="uploadUrl"
    multiple
    :max-count="5"
  ></lay-upload>
</template>
```

### Example: Upload with Preview

```vue
<template>
  <lay-upload 
    :action="uploadUrl"
    :file-list="fileList"
    @change="handleChange"
  ></lay-upload>
</template>

<script setup>
import { ref } from 'vue'
import { LayUpload } from '@layui/layui-vue'

const fileList = ref([])

const handleChange = (files) => {
  fileList.value = files
}
</script>
```

### Key Points

- Configure upload URL
- Set file validation rules
- Support multiple files
- Handle upload events
- Preview uploaded files
