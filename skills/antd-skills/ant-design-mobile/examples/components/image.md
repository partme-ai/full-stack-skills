# Image | 图片

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Image component in Ant Design Mobile.

### Key Concepts

- Basic image
- Image with lazy load
- Image with placeholder
- Image with error fallback
- Image with preview

### Example: Basic Image

```javascript
import React from 'react';
import { Image } from 'antd-mobile';

function App() {
  return (
    <Image
      src="https://via.placeholder.com/300x200"
      alt="示例图片"
      width={300}
      height={200}
    />
  );
}
```

### Example: Image with Lazy Load

```javascript
import React from 'react';
import { Image } from 'antd-mobile';

function App() {
  return (
    <Image
      src="https://via.placeholder.com/300x200"
      alt="示例图片"
      width={300}
      height={200}
      lazy
    />
  );
}
```

### Example: Image with Placeholder

```javascript
import React from 'react';
import { Image } from 'antd-mobile';

function App() {
  return (
    <Image
      src="https://via.placeholder.com/300x200"
      alt="示例图片"
      width={300}
      height={200}
      placeholder="加载中..."
    />
  );
}
```

### Example: Image with Error Fallback

```javascript
import React from 'react';
import { Image } from 'antd-mobile';

function App() {
  return (
    <Image
      src="https://invalid-url.com/image.jpg"
      alt="示例图片"
      width={300}
      height={200}
      fallback="https://via.placeholder.com/300x200?text=Error"
    />
  );
}
```

### Example: Image with Preview

```javascript
import React from 'react';
import { Image } from 'antd-mobile';

function App() {
  return (
    <Image
      src="https://via.placeholder.com/300x200"
      alt="示例图片"
      width={300}
      height={200}
      fit="cover"
      preview
    />
  );
}
```

### Example: Image Fit Modes

```javascript
import React from 'react';
import { Image } from 'antd-mobile';

function App() {
  return (
    <>
      <Image
        src="https://via.placeholder.com/300x200"
        width={150}
        height={150}
        fit="contain"
      />
      <Image
        src="https://via.placeholder.com/300x200"
        width={150}
        height={150}
        fit="cover"
      />
      <Image
        src="https://via.placeholder.com/300x200"
        width={150}
        height={150}
        fit="fill"
      />
    </>
  );
}
```

### Key Points

- Use `src` prop for image URL
- Use `alt` prop for alt text
- Use `width` and `height` props for dimensions
- Use `lazy` prop for lazy loading
- Use `placeholder` prop for loading placeholder
- Use `fallback` prop for error fallback
- Use `preview` prop for preview
- Use `fit` prop for image fit mode (contain, cover, fill)
- Image is optimized for mobile display
