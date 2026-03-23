# Select | 选择器

**官方文档**: https://4x-ant-design.antgroup.com/components/select-cn


## Instructions

This example demonstrates how to use the Select component in Ant Design React.

### Key Concepts

- Basic Select
- Multiple selection
- Select with search
- Select with groups
- Custom option rendering
- Select with tags

### Example: Basic Select

```javascript
import React from 'react';
import { Select } from 'antd';

const { Option } = Select;

function App() {
  const handleChange = (value) => {
    console.log(`selected ${value}`);
  };

  return (
    <Select
      defaultValue="lucy"
      style={{ width: 120 }}
      onChange={handleChange}
    >
      <Option value="jack">Jack</Option>
      <Option value="lucy">Lucy</Option>
      <Option value="disabled" disabled>
        Disabled
      </Option>
      <Option value="yiminghe">Yiminghe</Option>
    </Select>
  );
}
```

### Example: Multiple Selection

```javascript
import React from 'react';
import { Select } from 'antd';

const { Option } = Select;

function App() {
  return (
    <Select
      mode="multiple"
      style={{ width: '100%' }}
      placeholder="Select items"
      defaultValue={['lucy']}
    >
      <Option value="jack">Jack</Option>
      <Option value="lucy">Lucy</Option>
      <Option value="tom">Tom</Option>
    </Select>
  );
}
```

### Example: Select with Search

```javascript
import React from 'react';
import { Select } from 'antd';

const { Option } = Select;

function App() {
  return (
    <Select
      showSearch
      style={{ width: 200 }}
      placeholder="Select a person"
      optionFilterProp="children"
      filterOption={(input, option) =>
        option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
      }
    >
      <Option value="jack">Jack</Option>
      <Option value="lucy">Lucy</Option>
      <Option value="tom">Tom</Option>
    </Select>
  );
}
```

### Example: Select with Groups

```javascript
import React from 'react';
import { Select } from 'antd';

const { Option, OptGroup } = Select;

function App() {
  return (
    <Select defaultValue="lucy" style={{ width: 200 }}>
      <OptGroup label="Manager">
        <Option value="jack">Jack</Option>
        <Option value="lucy">Lucy</Option>
      </OptGroup>
      <OptGroup label="Engineer">
        <Option value="tom">Tom</Option>
      </OptGroup>
    </Select>
  );
}
```

### Example: Select with Tags

```javascript
import React from 'react';
import { Select } from 'antd';

const { Option } = Select;

function App() {
  return (
    <Select
      mode="tags"
      style={{ width: '100%' }}
      placeholder="Tags Mode"
    >
      <Option value="tag1">Tag 1</Option>
      <Option value="tag2">Tag 2</Option>
    </Select>
  );
}
```

### Key Points

- Use `Select` component with `Option` children
- Use `mode="multiple"` for multiple selection
- Use `showSearch` for searchable select
- Use `OptGroup` for option groups
- Use `mode="tags"` for tag mode
- Use `onChange` to handle selection changes
- Use `defaultValue` or `value` for controlled/uncontrolled
