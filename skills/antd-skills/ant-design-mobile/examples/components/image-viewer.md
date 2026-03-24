# ImageViewer | 图片查看器

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the ImageViewer component in Ant Design Mobile.

### Key Concepts

- Basic image viewer
- Image viewer with multiple images
- Image viewer with index
- Image viewer with controls
- Image viewer with zoom

### Example: Basic ImageViewer

```javascript
import React, { useState } from 'react';
import { ImageViewer, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>查看图片</Button>
      <ImageViewer
        image="https://via.placeholder.com/800x600"
        visible={visible}
        onClose={() => setVisible(false)}
      />
    </>
  );
}
```

### Example: ImageViewer with Multiple Images

```javascript
import React, { useState } from 'react';
import { ImageViewer, Button, Image } from 'antd-mobile';

const images = [
  'https://via.placeholder.com/800x600/ff0000',
  'https://via.placeholder.com/800x600/00ff00',
  'https://via.placeholder.com/800x600/0000ff',
];

function App() {
  const [visible, setVisible] = useState(false);
  const [index, setIndex] = useState(0);

  return (
    <>
      <div>
        {images.map((img, i) => (
          <Image
            key={i}
            src={img}
            width={100}
            height={100}
            onClick={() => {
              setIndex(i);
              setVisible(true);
            }}
          />
        ))}
      </div>
      <ImageViewer
        image={images}
        visible={visible}
        onClose={() => setVisible(false)}
        defaultIndex={index}
      />
    </>
  );
}
```

### Example: ImageViewer with Index

```javascript
import React, { useState } from 'react';
import { ImageViewer, Button } from 'antd-mobile';

const images = [
  'https://via.placeholder.com/800x600/ff0000',
  'https://via.placeholder.com/800x600/00ff00',
  'https://via.placeholder.com/800x600/0000ff',
];

function App() {
  const [visible, setVisible] = useState(false);
  const [index, setIndex] = useState(0);

  return (
    <>
      <Button onClick={() => setVisible(true)}>查看图片</Button>
      <ImageViewer
        image={images}
        visible={visible}
        onClose={() => setVisible(false)}
        defaultIndex={index}
        onIndexChange={(idx) => setIndex(idx)}
      />
    </>
  );
}
```

### Example: ImageViewer with Controls

```javascript
import React, { useState } from 'react';
import { ImageViewer, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>查看图片</Button>
      <ImageViewer
        image="https://via.placeholder.com/800x600"
        visible={visible}
        onClose={() => setVisible(false)}
        renderFooter={() => (
          <div style={{ padding: '20px', color: '#fff' }}>
            图片描述
          </div>
        )}
      />
    </>
  );
}
```

### Key Points

- Use `image` prop for image URL or array of URLs
- Use `visible` prop to control visibility
- Use `onClose` callback for close event
- Use `defaultIndex` prop for initial index
- Use `onIndexChange` callback for index change
- Use `renderFooter` prop for custom footer
- ImageViewer supports zoom and pan gestures
- ImageViewer is optimized for mobile display
