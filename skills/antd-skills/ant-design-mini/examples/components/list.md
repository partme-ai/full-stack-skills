# List Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the List component in Ant Design Mini.

### Key Concepts

- List items
- List rendering
- List events
- List styling

### Example: Basic List

```xml
<ant-list>
  <ant-list-item>Item 1</ant-list-item>
  <ant-list-item>Item 2</ant-list-item>
  <ant-list-item>Item 3</ant-list-item>
</ant-list>
```

### Example: List with Data

```xml
<ant-list>
  <ant-list-item 
    wx:for="{{items}}" 
    wx:key="index"
    onTap="handleItemTap"
    data-index="{{index}}"
  >
    {{item.title}}
  </ant-list-item>
</ant-list>
```

```javascript
// page.js
Page({
  data: {
    items: [
      { title: 'Item 1' },
      { title: 'Item 2' },
      { title: 'Item 3' }
    ]
  },
  handleItemTap(e) {
    const index = e.currentTarget.dataset.index
    console.log('Item tapped:', this.data.items[index])
  }
})
```

### Example: List with Actions

```xml
<ant-list-item 
  title="Title"
  brief="Description"
  arrow
  onTap="handleTap"
>
  <view slot="extra">
    <ant-button size="small">Action</ant-button>
  </view>
</ant-list-item>
```

### Key Points

- Use ant-list for list container
- Use ant-list-item for list items
- Support title, brief, arrow props
- Handle item tap events
- Support custom slots
