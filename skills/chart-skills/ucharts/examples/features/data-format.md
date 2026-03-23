# Data Format

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates data format in uCharts.

### Key Concepts

- Data structure
- Categories format
- Series format
- Data transformation

### Example: Line/Column Chart Data

```javascript
chartData: {
  categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
  series: [
    {
      name: 'Sales',
      data: [35, 36, 31, 33, 13]
    }
  ]
}
```

### Example: Pie/Ring Chart Data

```javascript
chartData: {
  series: [
    { name: 'A', value: 50 },
    { name: 'B', value: 30 },
    { name: 'C', value: 20 }
  ]
}
```

### Example: Multiple Series

```javascript
chartData: {
  categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
  series: [
    {
      name: 'Sales',
      data: [35, 36, 31, 33, 13]
    },
    {
      name: 'Orders',
      data: [18, 27, 21, 24, 6]
    }
  ]
}
```

### Example: Data Transformation

```javascript
// Transform API data to chart data format
transformData(apiData) {
  return {
    categories: apiData.map(item => item.date),
    series: [
      {
        name: 'Sales',
        data: apiData.map(item => item.sales)
      }
    ]
  }
}
```

### Key Points

- Use categories for X-axis labels
- Use series for data series
- Each series has name and data
- Pie charts use different format
- Transform data as needed
