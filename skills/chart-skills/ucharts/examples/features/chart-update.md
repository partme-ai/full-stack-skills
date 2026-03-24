# Chart Update

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates how to update charts in uCharts.

### Key Concepts

- Data update
- Options update
- Dynamic update
- Performance optimization

### Example: Update Chart Data

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
  <button @click="updateChartData">Update Data</button>
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed'],
        series: [{ name: 'Sales', data: [35, 36, 31] }]
      },
      opts: {}
    }
  },
  methods: {
    updateChartData() {
      this.chartData = {
        categories: ['Thu', 'Fri', 'Sat'],
        series: [{ name: 'Sales', data: [33, 13, 34] }]
      }
      // Or use method
      this.$refs.chart.updateData(this.chartData)
    }
  }
}
</script>
```

### Example: Update Chart Options

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
  <button @click="updateChartOptions">Update Options</button>
</template>

<script>
export default {
  data() {
    return {
      opts: {
        color: ['#1890FF']
      }
    }
  },
  methods: {
    updateChartOptions() {
      this.opts = {
        color: ['#FF0000']
      }
      // Or use method
      this.$refs.chart.updateOptions(this.opts)
    }
  }
}
</script>
```

### Example: Dynamic Data Update

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
</template>

<script>
export default {
  data() {
    return {
      chartData: {},
      opts: {}
    }
  },
  mounted() {
    this.loadData()
    // Update every 5 seconds
    setInterval(() => {
      this.loadData()
    }, 5000)
  },
  methods: {
    async loadData() {
      const response = await fetch('/api/data')
      const data = await response.json()
      this.chartData = {
        categories: data.categories,
        series: data.series
      }
    }
  }
}
</script>
```

### Key Points

- Update data reactively
- Use updateData method
- Use updateOptions method
- Handle dynamic updates
- Optimize performance
