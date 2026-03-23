# Modal | 对话框

**官方文档**: https://4x-ant-design.antgroup.com/components/modal-cn


## Instructions

This example demonstrates how to use the Modal component in Ant Design React.

### Key Concepts

- Basic Modal
- Modal with form
- Confirm Modal
- Modal methods (Modal.info, Modal.success, etc.)
- Modal with custom content
- Modal sizes

### Example: Basic Modal

```javascript
import React, { useState } from 'react';
import { Modal, Button } from 'antd';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    setIsModalOpen(false);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Modal
      </Button>
      <Modal
        title="Basic Modal"
        open={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <p>Some contents...</p>
      </Modal>
    </>
  );
}
```

### Example: Modal with Form

```javascript
import React, { useState } from 'react';
import { Modal, Form, Input } from 'antd';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [form] = Form.useForm();

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    form.validateFields().then((values) => {
      console.log('Form values:', values);
      setIsModalOpen(false);
      form.resetFields();
    });
  };

  const handleCancel = () => {
    setIsModalOpen(false);
    form.resetFields();
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        Open Modal
      </Button>
      <Modal
        title="Form Modal"
        open={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <Form form={form} layout="vertical">
          <Form.Item name="name" label="Name" rules={[{ required: true }]}>
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
}
```

### Example: Confirm Modal

```javascript
import React from 'react';
import { Modal, Button } from 'antd';

function App() {
  const showConfirm = () => {
    Modal.confirm({
      title: 'Confirm',
      content: 'Are you sure you want to delete this item?',
      onOk() {
        console.log('OK');
      },
      onCancel() {
        console.log('Cancel');
      },
    });
  };

  return <Button onClick={showConfirm}>Show Confirm</Button>;
}
```

### Example: Modal Methods

```javascript
import React from 'react';
import { Modal, Button, Space } from 'antd';

function App() {
  const showInfo = () => {
    Modal.info({
      title: 'Info',
      content: 'This is an info message',
    });
  };

  const showSuccess = () => {
    Modal.success({
      title: 'Success',
      content: 'Operation successful',
    });
  };

  const showError = () => {
    Modal.error({
      title: 'Error',
      content: 'Operation failed',
    });
  };

  const showWarning = () => {
    Modal.warning({
      title: 'Warning',
      content: 'This is a warning message',
    });
  };

  return (
    <Space>
      <Button onClick={showInfo}>Info</Button>
      <Button onClick={showSuccess}>Success</Button>
      <Button onClick={showError}>Error</Button>
      <Button onClick={showWarning}>Warning</Button>
    </Space>
  );
}
```

### Key Points

- Use `open` prop to control modal visibility
- Use `onOk` and `onCancel` for button handlers
- Use `title` prop for modal title
- Use `Modal.confirm()`, `Modal.info()`, etc. for static methods
- Use `Form` inside Modal for form modals
- Use `footer` prop to customize footer
- Use `width` prop to set modal width
