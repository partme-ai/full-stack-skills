# Upload | 上传

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to use Avue upload component in forms.

### Key Concepts

- Upload configuration
- File upload
- Upload events
- Upload validation

### Example: Basic Upload

```vue
<template>
  <avue-form
    :option="option"
    v-model="form"
  />
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'File Upload',
            prop: 'file',
            type: 'upload',
            action: '/api/upload',
            propsHttp: {
              res: 'data',
              url: 'url'
            }
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Upload with Multiple Files

```vue
<template>
  <avue-form
    :option="option"
    v-model="form"
  />
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'Multiple Files',
            prop: 'files',
            type: 'upload',
            action: '/api/upload',
            limit: 5,
            multiple: true,
            propsHttp: {
              res: 'data',
              url: 'url'
            }
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Use type: 'upload' in form column
- Configure action for upload endpoint
- Use propsHttp for response mapping
- Use limit for file count limit
- Use multiple for multiple files
- Upload component handles file operations
