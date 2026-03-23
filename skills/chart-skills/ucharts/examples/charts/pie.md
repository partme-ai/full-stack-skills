# Pie Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Pie chart in uCharts.

### Key Concepts

- Pie chart setup
- Data format
- Pie configuration
- Customization

### Example: Basic Pie Chart

```vue
<template>
  <qiun-data-chart type="pie" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        series: [
          { name: 'A', value: 50 },
          { name: 'B', value: 30 },
          { name: 'C', value: 20 }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Pie Configuration

```javascript
opts: {
  color: ['#1890FF', '#2FC25B', '#FACC14', '#F04864', '#8543E0'],
  padding: [5, 5, 5, 5],
  dataLabel: true,
  legend: {
    show: true,
    position: 'bottom'
  },
  extra: {
    pie: {
      activeOpacity: 0.5,
      activeRadius: 10,
      offsetAngle: 0,
      labelWidth: 15,
      border: true,
      borderWidth: 3,
      borderColor: '#FFFFFF'
    }
  }
}
```

### Example: With Custom Colors

```vue
<template>
  <qiun-data-chart type="pie" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        series: [
          { name: 'A', value: 50 },
          { name: 'B', value: 30 },
          { name: 'C', value: 20 }
        ]
      },
      opts: {
        color: ['#FF6B6B', '#4ECDC4', '#45B7D1']
      }
    }
  }
}
</script>
```

### Key Points

- Use type="pie" for pie chart
- Provide series data with name and value
- Configure pie style in extra.pie
- Support custom colors
- Customize appearance with opts
