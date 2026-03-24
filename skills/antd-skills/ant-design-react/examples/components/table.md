# Table | 表格

**官方文档**: https://4x-ant-design.antgroup.com/components/table-cn


## Instructions

This example demonstrates how to use the Table component in Ant Design React.

### Key Concepts

- Table columns definition
- Table data source
- Table pagination
- Table sorting and filtering
- Table selection
- Table row operations

### Example: Basic Table

```javascript
import React from 'react';
import { Table } from 'antd';

const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
  },
];

const data = [
  {
    key: '1',
    name: 'John Brown',
    age: 32,
    address: 'New York No. 1 Lake Park',
  },
  {
    key: '2',
    name: 'Jim Green',
    age: 42,
    address: 'London No. 1 Lake Park',
  },
];

function App() {
  return <Table columns={columns} dataSource={data} />;
}
```

### Example: Table with Pagination

```javascript
import React from 'react';
import { Table } from 'antd';

function App() {
  return (
    <Table
      columns={columns}
      dataSource={data}
      pagination={{
        current: 1,
        pageSize: 10,
        total: 100,
        showSizeChanger: true,
        showTotal: (total) => `Total ${total} items`,
      }}
    />
  );
}
```

### Example: Table with Sorting

```javascript
import React from 'react';
import { Table } from 'antd';

const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
    sorter: (a, b) => a.name.localeCompare(b.name),
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age',
    sorter: (a, b) => a.age - b.age,
  },
];

function App() {
  return <Table columns={columns} dataSource={data} />;
}
```

### Example: Table with Selection

```javascript
import React, { useState } from 'react';
import { Table, Button } from 'antd';

function App() {
  const [selectedRowKeys, setSelectedRowKeys] = useState([]);

  const rowSelection = {
    selectedRowKeys,
    onChange: (newSelectedRowKeys) => {
      setSelectedRowKeys(newSelectedRowKeys);
    },
  };

  return (
    <>
      <Button onClick={() => console.log(selectedRowKeys)}>
        Get Selected
      </Button>
      <Table
        rowSelection={rowSelection}
        columns={columns}
        dataSource={data}
      />
    </>
  );
}
```

### Example: Table with Actions

```javascript
import React from 'react';
import { Table, Button, Space } from 'antd';

const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Action',
    key: 'action',
    render: (_, record) => (
      <Space size="middle">
        <Button type="link">Edit</Button>
        <Button type="link" danger>Delete</Button>
      </Space>
    ),
  },
];

function App() {
  return <Table columns={columns} dataSource={data} />;
}
```

### Key Points

- Define columns with `title`, `dataIndex`, and `key`
- Use `dataSource` for table data
- Configure pagination with `pagination` prop
- Use `sorter` for sorting
- Use `rowSelection` for row selection
- Use `render` function for custom cell content
- Each row needs a unique `key` property
