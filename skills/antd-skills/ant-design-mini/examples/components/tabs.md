# Tabs Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Tabs component in Ant Design Mini.

### Key Concepts

- Tab items
- Tab switching
- Tab events
- Tab styling

### Example: Basic Tabs

```xml
<ant-tabs 
  current="{{currentTab}}"
  onChange="handleTabChange"
>
  <ant-tab-item title="Tab 1" key="1">
    Content 1
  </ant-tab-item>
  <ant-tab-item title="Tab 2" key="2">
    Content 2
  </ant-tab-item>
  <ant-tab-item title="Tab 3" key="3">
    Content 3
  </ant-tab-item>
</ant-tabs>
```

```javascript
// page.js
Page({
  data: {
    currentTab: '1'
  },
  handleTabChange(e) {
    this.setData({
      currentTab: e.detail.key
    })
  }
})
```

### Example: Tabs with Data

```xml
<ant-tabs 
  current="{{currentTab}}"
  onChange="handleTabChange"
>
  <ant-tab-item 
    wx:for="{{tabs}}" 
    wx:key="key"
    title="{{item.title}}" 
    key="{{item.key}}"
  >
    {{item.content}}
  </ant-tab-item>
</ant-tabs>
```

### Example: Scrollable Tabs

```xml
<ant-tabs 
  current="{{currentTab}}"
  scrollable
  onChange="handleTabChange"
>
  <!-- Tab items -->
</ant-tabs>
```

### Key Points

- Use ant-tabs for container
- Use ant-tab-item for each tab
- Control current tab with current prop
- Handle onChange event
- Support scrollable tabs
