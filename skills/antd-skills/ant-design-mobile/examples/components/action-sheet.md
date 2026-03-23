# ActionSheet | 动作面板

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the ActionSheet component in Ant Design Mobile.

### Key Concepts

- Basic action sheet
- Action sheet with options
- Action sheet with cancel
- Action sheet with danger
- Action sheet with icons

### Example: Basic ActionSheet

```javascript
import React from 'react';
import { ActionSheet, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        ActionSheet.show({
          actions: [
            { text: '选项1', key: '1' },
            { text: '选项2', key: '2' },
            { text: '选项3', key: '3' },
          ],
          onAction: (action) => {
            console.log(action);
          },
        });
      }}
    >
      显示动作面板
    </Button>
  );
}
```

### Example: ActionSheet with Cancel

```javascript
import React from 'react';
import { ActionSheet, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        ActionSheet.show({
          actions: [
            { text: '选项1', key: '1' },
            { text: '选项2', key: '2' },
          ],
          cancelText: '取消',
          onAction: (action) => {
            console.log(action);
          },
        });
      }}
    >
      显示动作面板
    </Button>
  );
}
```

### Example: ActionSheet with Danger

```javascript
import React from 'react';
import { ActionSheet, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        ActionSheet.show({
          actions: [
            { text: '选项1', key: '1' },
            { text: '删除', key: 'delete', danger: true },
          ],
          onAction: (action) => {
            console.log(action);
          },
        });
      }}
    >
      显示动作面板
    </Button>
  );
}
```

### Example: ActionSheet with Icons

```javascript
import React from 'react';
import { ActionSheet, Button } from 'antd-mobile';
import { AppOutline, UserOutline } from 'antd-mobile-icons';

function App() {
  return (
    <Button
      onClick={() => {
        ActionSheet.show({
          actions: [
            { text: '选项1', key: '1', icon: <AppOutline /> },
            { text: '选项2', key: '2', icon: <UserOutline /> },
          ],
          onAction: (action) => {
            console.log(action);
          },
        });
      }}
    >
      显示动作面板
    </Button>
  );
}
```

### Key Points

- Use `ActionSheet.show` to show action sheet
- Use `actions` prop for action options
- Use `cancelText` prop for cancel text
- Use `danger` prop for danger actions
- Use `icon` prop for action icons
- Use `onAction` callback for action selection
- ActionSheet is optimized for mobile display
