# Layer API

## API Reference

Layer API methods for modals, dialogs, and messages.

### layer.open(options)

**Type:** `Function`

Open a modal/dialog layer.

**Parameters:**
- `options` - Configuration object

**Options:**
- `title` - Layer title
- `content` - Layer content
- `area` - Layer size [width, height]
- `type` - Layer type (0: info, 1: page, 2: iframe)
- `shade` - Show shade (default: true)
- `shadeClose` - Close on shade click (default: true)
- `offset` - Layer offset [x, y]
- `anim` - Animation type

**Returns:** `number` - Layer index

**Example:**
```javascript
import { layer } from '@layui/layui-vue'

const index = layer.open({
  title: 'Title',
  content: 'Content',
  area: ['500px', '300px']
})
```

### layer.close(index)

**Type:** `Function`

Close a layer by index.

**Parameters:**
- `index` - Layer index

**Example:**
```javascript
layer.close(index)
```

### layer.msg(content, options?)

**Type:** `Function`

Show a message.

**Parameters:**
- `content` - Message content
- `options` - Options (time, icon, etc.)

**Example:**
```javascript
layer.msg('Hello World')
layer.msg('Success', { icon: 1 })
```

### layer.confirm(content, options?)

**Type:** `Function`

Show a confirmation dialog.

**Parameters:**
- `content` - Confirmation message
- `options` - Options with yes/no callbacks

**Example:**
```javascript
layer.confirm('Are you sure?', {
  yes: (index) => {
    console.log('Confirmed')
    layer.close(index)
  }
})
```

### layer.load(content?, options?)

**Type:** `Function`

Show loading layer.

**Returns:** `number` - Layer index

**Example:**
```javascript
const index = layer.load()
setTimeout(() => {
  layer.close(index)
}, 2000)
```

### layer.drawer(options)

**Type:** `Function`

Open a drawer.

**Options:**
- `content` - Drawer content
- `direction` - Drawer direction (left, right, top, bottom)

**Example:**
```javascript
layer.drawer({
  content: 'Drawer Content',
  direction: 'right'
})
```

**See also:** `examples/components/layer.md`
