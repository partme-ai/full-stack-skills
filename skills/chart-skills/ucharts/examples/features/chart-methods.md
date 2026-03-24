# Chart Methods

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates chart methods in uCharts.

### Key Concepts

- Method types
- Method usage
- Method parameters
- Method return values

### Example: Update Data

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
  <button @click="updateData">Update Data</button>
</template>

<script>
export default {
  methods: {
    updateData() {
      this.$refs.chart.updateData({
        categories: ['New', 'Data'],
        series: [{ name: 'Test', data: [1, 2] }]
      })
    }
  }
}
</script>
```

### Example: Update Options

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
  <button @click="updateOptions">Update Options</button>
</template>

<script>
export default {
  methods: {
    updateOptions() {
      this.$refs.chart.updateOptions({
        color: ['#FF0000', '#00FF00']
      })
    }
  }
}
</script>
```

### Example: Show Tooltip

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
  <button @click="showTooltip">Show Tooltip</button>
</template>

<script>
export default {
  methods: {
    showTooltip() {
      this.$refs.chart.showTooltip(0, 0)
    }
  }
}
</script>
```

### Example: Get Chart Data

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
  />
  <button @click="getData">Get Data</button>
</template>

<script>
export default {
  methods: {
    getData() {
      const data = this.$refs.chart.getChartData()
      console.log('Chart data:', data)
    }
  }
}
</script>
```

### Key Points

- Use updateData to update chart data
- Use updateOptions to update options
- Use showTooltip to show tooltip
- Use getChartData to get current data
- Access chart via ref
