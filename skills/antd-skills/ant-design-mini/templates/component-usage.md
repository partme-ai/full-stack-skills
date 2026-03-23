# Component Usage Templates

## Button Usage

```xml
<!-- Alipay -->
<ant-button type="primary" onTap="handleTap">
  Click Me
</ant-button>

<!-- WeChat -->
<ant-button type="primary" bindtap="handleTap">
  Click Me
</ant-button>
```

```javascript
Page({
  handleTap() {
    console.log('Clicked')
  }
})
```

## Form Usage

```xml
<ant-form onFinish="handleSubmit">
  <ant-form-item label="Name" name="name">
    <ant-input 
      value="{{form.name}}" 
      onInput="handleNameInput" 
    />
  </ant-form-item>
  <ant-form-item>
    <ant-button type="primary" formType="submit">
      Submit
    </ant-button>
  </ant-form-item>
</ant-form>
```

```javascript
Page({
  data: {
    form: {
      name: ''
    }
  },
  handleNameInput(e) {
    this.setData({
      'form.name': e.detail.value
    })
  },
  handleSubmit() {
    console.log('Form:', this.data.form)
  }
})
```

## List Usage

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
Page({
  data: {
    items: [
      { title: 'Item 1' },
      { title: 'Item 2' }
    ]
  },
  handleItemTap(e) {
    const index = e.currentTarget.dataset.index
    console.log('Item:', this.data.items[index])
  }
})
```

## Modal Usage

```xml
<ant-modal 
  visible="{{visible}}"
  title="Title"
  onClose="handleClose"
>
  <view>Content</view>
</ant-modal>
<ant-button onTap="showModal">Show</ant-button>
```

```javascript
Page({
  data: {
    visible: false
  },
  showModal() {
    this.setData({ visible: true })
  },
  handleClose() {
    this.setData({ visible: false })
  }
})
```
