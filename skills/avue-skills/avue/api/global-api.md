# Global API | 全局 API

## API Reference

Avue global API methods available via this.$avue or Vue.prototype.$avue.

### $DialogForm

Open a dialog form.

**Usage:**
```javascript
this.$avue.$dialogForm({
  title: 'Form Title',
  option: {
    column: [
      { label: 'Name', prop: 'name', type: 'input' }
    ]
  }
}).then(res => {
  console.log('Form data:', res)
})
```

### $Clipboard

Copy text to clipboard.

**Usage:**
```javascript
this.$avue.$clipboard('Text to copy').then(() => {
  this.$message.success('Copied!')
})
```

### $ImagePreview

Preview images.

**Usage:**
```javascript
this.$avue.$imagePreview([
  'https://example.com/image1.jpg',
  'https://example.com/image2.jpg'
], 0) // Start from index 0
```

### $Print

Print content.

**Usage:**
```javascript
this.$avue.$print({
  id: 'print-content',
  standard: 'html5'
})
```

### $Export

Export data.

**Usage:**
```javascript
this.$avue.$export.excel({
  title: 'Export Title',
  columns: [
    { label: 'Name', prop: 'name' },
    { label: 'Email', prop: 'email' }
  ],
  data: this.tableData
})
```

### $Log

Logging utility.

**Usage:**
```javascript
this.$avue.$log.info('Info message')
this.$avue.$log.warn('Warning message')
this.$avue.$log.error('Error message')
```

### Utility Functions

**findObject:**
```javascript
const obj = this.$avue.findObject(array, 'id', 1)
```

**findArray:**
```javascript
const arr = this.$avue.findArray(array, 'id', 1)
```

**findNode:**
```javascript
const node = this.$avue.findNode(treeData, 'id', 1)
```

**watermark:**
```javascript
this.$avue.watermark({
  text: 'Watermark Text',
  font: '16px Arial',
  color: 'rgba(0,0,0,0.1)'
})
```

**downFile:**
```javascript
this.$avue.downFile(url, filename)
```

**randomId:**
```javascript
const id = this.$avue.randomId()
```

**deepClone:**
```javascript
const cloned = this.$avue.deepClone(obj)
```

**validatenull:**
```javascript
const isEmpty = this.$avue.validatenull(value)
```

### Key Points

- All APIs available via this.$avue
- $DialogForm for dialog forms
- $Clipboard for clipboard operations
- $ImagePreview for image preview
- $Print for printing
- $Export for data export
- Utility functions for common operations
