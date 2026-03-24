# Textarea | 文本域

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Textarea component in Ant Design Mobile.

### Key Concepts

- Basic textarea
- Textarea with placeholder
- Textarea with max length
- Auto resize textarea
- Textarea with count

### Example: Basic Textarea

```javascript
import React, { useState } from 'react';
import { TextArea } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <TextArea
      value={value}
      onChange={(val) => setValue(val)}
      placeholder="请输入内容"
    />
  );
}
```

### Example: Textarea with Max Length

```javascript
import React, { useState } from 'react';
import { TextArea } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <TextArea
      value={value}
      onChange={(val) => setValue(val)}
      placeholder="最多输入100字"
      maxLength={100}
      showCount
    />
  );
}
```

### Example: Auto Resize Textarea

```javascript
import React, { useState } from 'react';
import { TextArea } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <TextArea
      value={value}
      onChange={(val) => setValue(val)}
      placeholder="自动调整高度"
      autoSize={{ minRows: 2, maxRows: 5 }}
    />
  );
}
```

### Example: Textarea with Count

```javascript
import React, { useState } from 'react';
import { TextArea } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <TextArea
      value={value}
      onChange={(val) => setValue(val)}
      placeholder="输入内容"
      showCount
      maxLength={200}
    />
  );
}
```

### Example: Textarea with Form

```javascript
import React from 'react';
import { Form, TextArea } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="content" label="内容">
        <TextArea
          placeholder="请输入内容"
          showCount
          maxLength={200}
        />
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `value` prop for textarea value
- Use `onChange` callback for value change
- Use `placeholder` prop for placeholder text
- Use `maxLength` prop to limit input length
- Use `showCount` prop to show character count
- Use `autoSize` prop for auto resize
- TextArea works well with Form component
- TextArea is optimized for mobile display
