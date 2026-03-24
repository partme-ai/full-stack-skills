# Form | 表单

**官方文档**: https://4x-ant-design.antgroup.com/components/form-cn


## Instructions

This example demonstrates how to use the Form component with validation in Ant Design React.

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
import { Form, Input, Button } from 'antd';

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
        <Input />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
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
import { Form, Input, Button } from 'antd';

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
        <Input />
      </Form.Item>
      <Form.Item
        name="password"
        label="Password"
        rules={[
          { required: true, message: 'Please input your password!' },
          { min: 6, message: 'Password must be at least 6 characters!' }
        ]}
      >
        <Input.Password />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
}
```

### Example: Form Layout

```javascript
import React from 'react';
import { Form, Input, Button } from 'antd';

function App() {
  return (
    <Form layout="vertical">
      <Form.Item label="Username" name="username">
        <Input />
      </Form.Item>
      <Form.Item label="Password" name="password">
        <Input.Password />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">
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
import { Form, Input, Button } from 'antd';

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
        <Input />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit">Submit</Button>
        <Button htmlType="button" onClick={onReset}>Reset</Button>
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
- Use `layout` prop for form layout (horizontal, vertical, inline)
- Use `Form.useForm()` for form instance and methods
- Use `htmlType="submit"` for submit button
