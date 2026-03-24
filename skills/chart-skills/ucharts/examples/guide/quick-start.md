# Quick Start

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example provides a quick start guide for uCharts.

### Key Concepts

- Basic chart setup
- Data format
- Options configuration
- Chart rendering

### Example: Basic Line Chart

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13, 34, 27]
          }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Basic Column Chart

```vue
<template>
  <qiun-data-chart type="column" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13]
          }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

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

### Example: With Options

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13]
          }
        ]
      },
      opts: {
        color: ['#1890FF'],
        padding: [15, 15, 0, 15],
        enableScroll: false,
        legend: {
          show: true
        },
        xAxis: {
          disableGrid: false
        },
        yAxis: {
          gridType: 'dash',
          dashLength: 2
        }
      }
    }
  }
}
</script>
```

### Key Points

- Use qiun-data-chart component
- Set chart type with type prop
- Provide chartData with categories and series
- Configure options with opts prop
- Support multiple chart types
