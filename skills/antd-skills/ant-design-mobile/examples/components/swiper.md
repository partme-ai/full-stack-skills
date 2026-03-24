# Swiper | 走马灯

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Swiper component in Ant Design Mobile.

### Key Concepts

- Basic swiper
- Swiper with autoplay
- Swiper with loop
- Swiper with dots
- Swiper with pagination

### Example: Basic Swiper

```javascript
import React from 'react';
import { Swiper } from 'antd-mobile';

const colors = ['#ace0ff', '#bcffbd', '#e4fabd', '#ffcfac'];

function App() {
  return (
    <Swiper>
      {colors.map((color, index) => (
        <Swiper.Item key={index}>
          <div
            style={{
              background: color,
              height: '200px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {index + 1}
          </div>
        </Swiper.Item>
      ))}
    </Swiper>
  );
}
```

### Example: Swiper with Autoplay

```javascript
import React from 'react';
import { Swiper } from 'antd-mobile';

const colors = ['#ace0ff', '#bcffbd', '#e4fabd', '#ffcfac'];

function App() {
  return (
    <Swiper autoplay>
      {colors.map((color, index) => (
        <Swiper.Item key={index}>
          <div
            style={{
              background: color,
              height: '200px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {index + 1}
          </div>
        </Swiper.Item>
      ))}
    </Swiper>
  );
}
```

### Example: Swiper with Loop

```javascript
import React from 'react';
import { Swiper } from 'antd-mobile';

const colors = ['#ace0ff', '#bcffbd', '#e4fabd', '#ffcfac'];

function App() {
  return (
    <Swiper loop>
      {colors.map((color, index) => (
        <Swiper.Item key={index}>
          <div
            style={{
              background: color,
              height: '200px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {index + 1}
          </div>
        </Swiper.Item>
      ))}
    </Swiper>
  );
}
```

### Example: Swiper with Dots

```javascript
import React from 'react';
import { Swiper } from 'antd-mobile';

const colors = ['#ace0ff', '#bcffbd', '#e4fabd', '#ffcfac'];

function App() {
  return (
    <Swiper indicator={(total, current) => (
      <div style={{ textAlign: 'center', padding: '10px' }}>
        {current + 1} / {total}
      </div>
    )}>
      {colors.map((color, index) => (
        <Swiper.Item key={index}>
          <div
            style={{
              background: color,
              height: '200px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            {index + 1}
          </div>
        </Swiper.Item>
      ))}
    </Swiper>
  );
}
```

### Key Points

- Use `Swiper` for swiper container
- Use `Swiper.Item` for swiper items
- Use `autoplay` prop for autoplay
- Use `loop` prop for loop
- Use `indicator` prop for custom indicator
- Swiper is optimized for mobile touch interactions
