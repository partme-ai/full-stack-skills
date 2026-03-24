# Modal | 对话框

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Modal component in Ant Design Mobile.

### Key Concepts

- Basic Modal
- Modal with content
- Confirm Modal
- Modal methods (Modal.show, Modal.alert, etc.)
- Modal with custom content
- Modal actions

### Example: Basic Modal

```javascript
import React, { useState } from 'react';
import { Modal, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button color="primary" onClick={() => setVisible(true)}>
        Open Modal
      </Button>
      <Modal
        visible={visible}
        content="Modal content"
        closeOnAction
        onClose={() => setVisible(false)}
        actions={[
          {
            key: 'cancel',
            text: 'Cancel',
          },
          {
            key: 'confirm',
            text: 'Confirm',
            primary: true,
          },
        ]}
      />
    </>
  );
}
```

### Example: Modal Methods

```javascript
import React from 'react';
import { Modal, Button } from 'antd-mobile';

function App() {
  const showAlert = () => {
    Modal.alert({
      content: 'This is an alert',
      onConfirm: () => {
        console.log('Confirmed');
      },
    });
  };

  const showConfirm = () => {
    Modal.confirm({
      content: 'Are you sure?',
      onConfirm: () => {
        console.log('Confirmed');
      },
      onCancel: () => {
        console.log('Cancelled');
      },
    });
  };

  return (
    <>
      <Button onClick={showAlert}>Show Alert</Button>
      <Button onClick={showConfirm}>Show Confirm</Button>
    </>
  );
}
```

### Example: Modal with Custom Content

```javascript
import React, { useState } from 'react';
import { Modal, Button, Input } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState('');

  return (
    <>
      <Button color="primary" onClick={() => setVisible(true)}>
        Open Modal
      </Button>
      <Modal
        visible={visible}
        content={
          <Input
            placeholder="Enter text"
            value={value}
            onChange={(val) => setValue(val)}
          />
        }
        closeOnAction
        onClose={() => setVisible(false)}
        actions={[
          {
            key: 'confirm',
            text: 'Confirm',
            primary: true,
            onClick: () => {
              console.log(value);
              setVisible(false);
            },
          },
        ]}
      />
    </>
  );
}
```

### Key Points

- Use `visible` prop to control modal visibility
- Use `content` prop for modal content
- Use `actions` prop for action buttons
- Use `onClose` for close handler
- Use `Modal.alert()`, `Modal.confirm()` for static methods
- Use `closeOnAction` to close on action click
- Modal is optimized for mobile screens
