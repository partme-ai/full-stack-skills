# Loading Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Loading component in Ant Design Mini.

### Key Concepts

- Loading display
- Loading types
- Loading text
- Loading API

### Example: Loading Component

```xml
<ant-loading 
  visible="{{loading}}"
  type="spinner"
  tip="Loading..."
/>
```

### Example: Loading API

```javascript
// Using Loading API
import { Loading } from 'antd-mini'

// Show loading
Loading.show({
  type: 'spinner',
  tip: 'Loading...'
})

// Hide loading
Loading.hide()
```

### Example: Loading Types

```xml
<ant-loading type="spinner" />
<ant-loading type="circular" />
```

### Example: Loading with Text

```xml
<ant-loading 
  visible="{{loading}}"
  tip="Please wait..."
/>
```

### Key Points

- Control visibility with visible prop
- Use Loading API for programmatic control
- Multiple loading types
- Customize loading text
- Simple loading indicator
