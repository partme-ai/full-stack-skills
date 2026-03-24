# Layout | 布局

**官方文档**: https://4x-ant-design.antgroup.com/components/layout-cn


## Instructions

This example demonstrates how to use the Layout component in Ant Design React.

### Key Concepts

- Layout structure (Header, Sider, Content, Footer)
- Responsive layout
- Layout with Sider
- Fixed header and footer
- Layout customization

### Example: Basic Layout

```javascript
import React from 'react';
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

function App() {
  return (
    <Layout>
      <Header>Header</Header>
      <Content>Content</Content>
      <Footer>Footer</Footer>
    </Layout>
  );
}
```

### Example: Layout with Sider

```javascript
import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
} from '@ant-design/icons';

const { Header, Sider, Content } = Layout;

function App() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout>
      <Sider trigger={null} collapsible collapsed={collapsed}>
        <div className="logo" />
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={['1']}
          items={[
            { key: '1', label: 'Option 1' },
            { key: '2', label: 'Option 2' },
          ]}
        />
      </Sider>
      <Layout>
        <Header style={{ padding: 0 }}>
          {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
            className: 'trigger',
            onClick: () => setCollapsed(!collapsed),
          })}
        </Header>
        <Content style={{ margin: '24px 16px', padding: 24, minHeight: 280 }}>
          Content
        </Content>
      </Layout>
    </Layout>
  );
}
```

### Example: Fixed Header and Footer

```javascript
import React from 'react';
import { Layout } from 'antd';

const { Header, Footer, Content } = Layout;

function App() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
        Header
      </Header>
      <Content style={{ marginTop: 64, padding: '0 50px' }}>
        Content
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Ant Design ©2023 Created by Ant UED
      </Footer>
    </Layout>
  );
}
```

### Key Points

- Use `Layout` as container
- Use `Header`, `Sider`, `Content`, `Footer` as layout sections
- Use `collapsible` prop for collapsible Sider
- Use `trigger` prop for collapse trigger
- Layout supports responsive design
- Use style prop for layout customization
- Fixed header/footer requires position: fixed
