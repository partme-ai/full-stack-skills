# Uploader | 文件上传

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Uploader component in Ant Design Mobile.

### Key Concepts

- Basic uploader
- Uploader with preview
- Uploader with multiple
- Uploader with max count
- Uploader with custom upload

### Example: Basic Uploader

```javascript
import React, { useState } from 'react';
import { Uploader } from 'antd-mobile';

function App() {
  const [fileList, setFileList] = useState([]);

  return (
    <Uploader
      value={fileList}
      onChange={setFileList}
    />
  );
}
```

### Example: Uploader with Preview

```javascript
import React, { useState } from 'react';
import { Uploader } from 'antd-mobile';

function App() {
  const [fileList, setFileList] = useState([]);

  return (
    <Uploader
      value={fileList}
      onChange={setFileList}
      preview
    />
  );
}
```

### Example: Uploader with Multiple

```javascript
import React, { useState } from 'react';
import { Uploader } from 'antd-mobile';

function App() {
  const [fileList, setFileList] = useState([]);

  return (
    <Uploader
      value={fileList}
      onChange={setFileList}
      multiple
    />
  );
}
```

### Example: Uploader with Max Count

```javascript
import React, { useState } from 'react';
import { Uploader } from 'antd-mobile';

function App() {
  const [fileList, setFileList] = useState([]);

  return (
    <Uploader
      value={fileList}
      onChange={setFileList}
      maxCount={3}
    />
  );
}
```

### Example: Uploader with Custom Upload

```javascript
import React, { useState } from 'react';
import { Uploader } from 'antd-mobile';

function App() {
  const [fileList, setFileList] = useState([]);

  const upload = async (file) => {
    // 自定义上传逻辑
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await fetch('/api/upload', {
      method: 'POST',
      body: formData,
    });
    
    const result = await response.json();
    return {
      url: result.url,
    };
  };

  return (
    <Uploader
      value={fileList}
      onChange={setFileList}
      upload={upload}
    />
  );
}
```

### Example: Uploader with Form

```javascript
import React from 'react';
import { Form, Uploader } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="files" label="上传文件">
        <Uploader maxCount={5} />
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `value` prop for file list
- Use `onChange` callback for file list change
- Use `preview` prop for preview
- Use `multiple` prop for multiple files
- Use `maxCount` prop to limit file count
- Use `upload` prop for custom upload function
- Uploader works well with Form component
- Uploader is optimized for mobile file selection
