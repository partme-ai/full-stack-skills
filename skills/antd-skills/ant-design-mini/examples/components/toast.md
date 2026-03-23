# Toast Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Toast component in Ant Design Mini.

### Key Concepts

- Toast display
- Toast types
- Toast duration
- Toast API

### Example: Toast Component

```xml
<ant-toast 
  visible="{{toastVisible}}"
  content="{{toastContent}}"
  type="{{toastType}}"
/>
```

### Example: Toast API

```javascript
// Using Toast API
import { Toast } from 'antd-mini'

// Success toast
Toast.show({
  type: 'success',
  content: 'Success!',
  duration: 2000
})

// Error toast
Toast.show({
  type: 'fail',
  content: 'Error!',
  duration: 2000
})

// Loading toast
Toast.show({
  type: 'loading',
  content: 'Loading...'
})

// Hide toast
Toast.hide()
```

### Example: Toast Types

```javascript
Toast.show({ type: 'success', content: 'Success' })
Toast.show({ type: 'fail', content: 'Error' })
Toast.show({ type: 'loading', content: 'Loading' })
Toast.show({ type: 'none', content: 'Message' })
```

### Key Points

- Use Toast API for programmatic control
- Multiple types: success, fail, loading, none
- Configure duration
- Auto-hide or manual hide
- Simple and easy to use
