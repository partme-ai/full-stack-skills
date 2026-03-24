# Form | 表单

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Form component with validation in Ant Design Mobile.

### Key Concepts

- Form component setup
- Form.Item for form fields
- Form validation rules
- Form submission
- Form layout
- Form methods

### Example: Basic Form

```javascript
import React from 'react';
import { Form, Input, Button } from 'antd-mobile';

function App() {
  const onFinish = (values) => {
    console.log('Success:', values);
  };

  return (
    <Form onFinish={onFinish}>
      <Form.Item
        name="username"
        label="Username"
        rules={[{ required: true, message: 'Please input your username!' }]}
      >
        <Input placeholder="Enter username" />
      </Form.Item>
      <Form.Item>
        <Button color="primary" block type="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
}
```

### Example: Form with Validation

```javascript
import React from 'react';
import { Form, Input, Button } from 'antd-mobile';

function App() {
  const onFinish = (values) => {
    console.log('Success:', values);
  };

  return (
    <Form onFinish={onFinish}>
      <Form.Item
        name="email"
        label="Email"
        rules={[
          { required: true, message: 'Please input your email!' },
          { type: 'email', message: 'Please enter a valid email!' }
        ]}
      >
        <Input type="email" placeholder="Enter email" />
      </Form.Item>
      <Form.Item
        name="password"
        label="Password"
        rules={[
          { required: true, message: 'Please input your password!' },
          { min: 6, message: 'Password must be at least 6 characters!' }
        ]}
      >
        <Input type="password" placeholder="Enter password" />
      </Form.Item>
      <Form.Item>
        <Button color="primary" block type="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
}
```

### Example: Form with Form.useForm()

```javascript
import React from 'react';
import { Form, Input, Button } from 'antd-mobile';

function App() {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    console.log('Success:', values);
  };

  const onReset = () => {
    form.resetFields();
  };

  return (
    <Form form={form} onFinish={onFinish}>
      <Form.Item name="username" label="Username">
        <Input placeholder="Enter username" />
      </Form.Item>
      <Form.Item>
        <Button color="primary" block type="submit">Submit</Button>
        <Button block onClick={onReset}>Reset</Button>
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `Form` component to wrap form fields
- Use `Form.Item` for each form field
- Use `rules` prop for validation
- Use `onFinish` for form submission
- Use `Form.useForm()` for form instance and methods
- Use `type="submit"` for submit button
- Form is optimized for mobile input experience
