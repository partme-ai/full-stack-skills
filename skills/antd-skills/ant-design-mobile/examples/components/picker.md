# Picker | 选择器

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Picker component in Ant Design Mobile.

### Key Concepts

- Basic Picker
- Picker with columns
- Picker with multiple columns
- Picker with async data
- Picker with custom rendering

### Example: Basic Picker

```javascript
import React, { useState } from 'react';
import { Picker, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  const columns = [
    [
      { label: 'Option 1', value: '1' },
      { label: 'Option 2', value: '2' },
      { label: 'Option 3', value: '3' },
    ],
  ];

  return (
    <>
      <Button onClick={() => setVisible(true)}>
        {value ? columns[0].find(item => item.value === value[0])?.label : 'Select'}
      </Button>
      <Picker
        visible={visible}
        columns={columns}
        value={value}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
        onCancel={() => setVisible(false)}
      />
    </>
  );
}
```

### Example: Multi-column Picker

```javascript
import React, { useState } from 'react';
import { Picker, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  const columns = [
    [
      { label: 'Province 1', value: '1' },
      { label: 'Province 2', value: '2' },
    ],
    [
      { label: 'City 1', value: '1' },
      { label: 'City 2', value: '2' },
    ],
  ];

  return (
    <>
      <Button onClick={() => setVisible(true)}>Select</Button>
      <Picker
        visible={visible}
        columns={columns}
        value={value}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
        onCancel={() => setVisible(false)}
      />
    </>
  );
}
```

### Example: Cascading Picker

```javascript
import React, { useState } from 'react';
import { Picker, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  const [columns, setColumns] = useState([
    [
      { label: 'Province 1', value: '1' },
      { label: 'Province 2', value: '2' },
    ],
  ]);

  const handleColumnChange = (val, index) => {
    // Update columns based on selection
    const newColumns = [...columns];
    if (index === 0) {
      newColumns[1] = [
        { label: 'City 1', value: '1' },
        { label: 'City 2', value: '2' },
      ];
      setColumns(newColumns);
    }
  };

  return (
    <>
      <Button onClick={() => setVisible(true)}>Select</Button>
      <Picker
        visible={visible}
        columns={columns}
        value={value}
        onColumnChange={handleColumnChange}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
        onCancel={() => setVisible(false)}
      />
    </>
  );
}
```

### Key Points

- Use `Picker` component for selection
- Use `columns` prop for picker options
- Use `visible` prop to control picker visibility
- Use `value` prop for selected value
- Use `onConfirm` for confirmation handler
- Use `onCancel` for cancel handler
- Use `onColumnChange` for cascading pickers
- Picker is optimized for mobile touch interaction
