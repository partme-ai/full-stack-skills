# Dialog | 对话框

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Dialog component in Ant Design Mobile.

### Key Concepts

- Basic dialog
- Dialog with title
- Dialog with content
- Dialog with actions
- Dialog with confirm

### Example: Basic Dialog

```javascript
import React from 'react';
import { Dialog, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Dialog.alert({
          content: '这是一个对话框',
        });
      }}
    >
      显示对话框
    </Button>
  );
}
```

### Example: Dialog with Title

```javascript
import React from 'react';
import { Dialog, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Dialog.alert({
          title: '标题',
          content: '这是对话框内容',
        });
      }}
    >
      显示对话框
    </Button>
  );
}
```

### Example: Dialog with Confirm

```javascript
import React from 'react';
import { Dialog, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Dialog.confirm({
          title: '确认',
          content: '确定要删除吗？',
          onConfirm: () => {
            console.log('确认');
          },
        });
      }}
    >
      显示确认对话框
    </Button>
  );
}
```

### Example: Dialog with Custom Actions

```javascript
import React from 'react';
import { Dialog, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Dialog.show({
          title: '标题',
          content: '内容',
          actions: [
            {
              key: 'cancel',
              text: '取消',
            },
            {
              key: 'confirm',
              text: '确认',
              bold: true,
              onClick: () => {
                console.log('确认');
              },
            },
          ],
        });
      }}
    >
      显示自定义对话框
    </Button>
  );
}
```

### Key Points

- Use `Dialog.alert` for alert dialog
- Use `Dialog.confirm` for confirm dialog
- Use `Dialog.show` for custom dialog
- Use `title` prop for dialog title
- Use `content` prop for dialog content
- Use `onConfirm` callback for confirm event
- Use `actions` prop for custom actions
- Dialog is optimized for mobile display
