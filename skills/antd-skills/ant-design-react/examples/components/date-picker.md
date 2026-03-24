# DatePicker | 日期选择器

**官方文档**: https://4x-ant-design.antgroup.com/components/date-picker-cn


## Instructions

This example demonstrates how to use the DatePicker component in Ant Design React.

### Key Concepts

- Basic DatePicker
- Date range picker
- DatePicker with time
- DatePicker formats
- DatePicker with presets
- Disabled dates

### Example: Basic DatePicker

```javascript
import React, { useState } from 'react';
import { DatePicker } from 'antd';
import dayjs from 'dayjs';

function App() {
  const [date, setDate] = useState(null);

  const onChange = (date, dateString) => {
    setDate(date);
    console.log(date, dateString);
  };

  return <DatePicker onChange={onChange} />;
}
```

### Example: Date Range Picker

```javascript
import React from 'react';
import { DatePicker } from 'antd';

const { RangePicker } = DatePicker;

function App() {
  const onChange = (dates, dateStrings) => {
    console.log('From: ', dates[0], ', To: ', dates[1]);
    console.log('From: ', dateStrings[0], ', To: ', dateStrings[1]);
  };

  return <RangePicker onChange={onChange} />;
}
```

### Example: DatePicker with Time

```javascript
import React from 'react';
import { DatePicker } from 'antd';

function App() {
  return <DatePicker showTime onChange={onChange} />;
}
```

### Example: DatePicker Formats

```javascript
import React from 'react';
import { DatePicker } from 'antd';

function App() {
  return (
    <>
      <DatePicker format="YYYY-MM-DD" />
      <DatePicker format="DD/MM/YYYY" />
      <DatePicker format="YYYY/MM/DD HH:mm:ss" showTime />
    </>
  );
}
```

### Example: DatePicker with Presets

```javascript
import React from 'react';
import { DatePicker } from 'antd';
import dayjs from 'dayjs';

const { RangePicker } = DatePicker;

function App() {
  const rangePresets = [
    {
      label: 'Last 7 Days',
      value: [dayjs().add(-7, 'd'), dayjs()],
    },
    {
      label: 'Last 30 Days',
      value: [dayjs().add(-30, 'd'), dayjs()],
    },
  ];

  return <RangePicker presets={rangePresets} />;
}
```

### Key Points

- Use `DatePicker` for single date selection
- Use `RangePicker` for date range selection
- Use `showTime` for time selection
- Use `format` prop to customize date format
- Use `presets` for quick date selection
- Use `disabledDate` to disable specific dates
- Requires dayjs for date handling
