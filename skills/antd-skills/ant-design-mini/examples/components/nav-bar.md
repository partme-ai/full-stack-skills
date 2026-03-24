# NavBar Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the NavBar component in Ant Design Mini.

### Key Concepts

- NavBar title
- NavBar back button
- NavBar actions
- NavBar events

### Example: Basic NavBar

```xml
<ant-nav-bar 
  title="Title"
  onBack="handleBack"
/>
```

```javascript
// page.js
Page({
  handleBack() {
    // Navigate back
    my.navigateBack()
  }
})
```

### Example: NavBar with Actions

```xml
<ant-nav-bar 
  title="Title"
  onBack="handleBack"
>
  <view slot="right">
    <ant-button size="small">Action</ant-button>
  </view>
</ant-nav-bar>
```

### Example: NavBar without Back

```xml
<ant-nav-bar 
  title="Title"
  showBack="{{false}}"
/>
```

### Key Points

- Set title for navbar
- Handle onBack event
- Show/hide back button
- Support right slot for actions
- Customize navbar appearance
