# Theme Customization | 主题定制

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to customize the theme in Ant Design Mobile.

### Key Concepts

- CSS Variables
- Design tokens
- Theme configuration
- Custom colors
- Custom styles

### Example: Using CSS Variables

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import 'antd-mobile/es/global.css';

// Custom CSS variables
const customTheme = {
  '--adm-color-primary': '#409EFF',
  '--adm-color-success': '#67C23A',
  '--adm-color-warning': '#E6A23C',
  '--adm-color-danger': '#F56C6C',
};

function App() {
  return (
    <ConfigProvider theme={customTheme}>
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Example: Custom Theme with ConfigProvider

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';

const theme = {
  '--adm-color-primary': '#409EFF',
  '--adm-color-text': '#303133',
  '--adm-color-text-secondary': '#606266',
  '--adm-border-color': '#DCDFE6',
  '--adm-font-size-main': '16px',
};

function App() {
  return (
    <ConfigProvider theme={theme}>
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Example: Custom Component Styles

```css
/* Custom styles */
.custom-button {
  --adm-button-border-radius: 20px;
  --adm-button-font-size: 18px;
}
```

### Example: Using Design Tokens

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';

const theme = {
  // Colors
  '--adm-color-primary': '#409EFF',
  '--adm-color-success': '#67C23A',
  '--adm-color-warning': '#E6A23C',
  '--adm-color-danger': '#F56C6C',
  
  // Spacing
  '--adm-spacing-xs': '4px',
  '--adm-spacing-s': '8px',
  '--adm-spacing-m': '16px',
  '--adm-spacing-l': '24px',
  
  // Border radius
  '--adm-border-radius-s': '4px',
  '--adm-border-radius-m': '8px',
  '--adm-border-radius-l': '12px',
};

function App() {
  return (
    <ConfigProvider theme={theme}>
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Key Points

- Use CSS variables for theme customization
- Use `ConfigProvider` with `theme` prop for global theme
- Design tokens provide consistent theming
- Customize colors, spacing, border radius, etc.
- Theme customization is optimized for mobile display
