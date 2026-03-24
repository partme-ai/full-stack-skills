# Chart Events

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates chart events in uCharts.

### Key Concepts

- Event types
- Event handlers
- Event parameters
- Event usage

### Example: Complete Event

```vue
<template>
  <qiun-data-chart 
    type="line" 
    :chartData="chartData" 
    :opts="opts"
    @complete="handleComplete"
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
  methods: {
    handleComplete(chart) {
      console.log('Chart rendered:', chart)
    }
  }
}
</script>
```

### Example: Render Complete Event

```vue
<template>
  <qiun-data-chart 
    type="line" 
    :chartData="chartData" 
    :opts="opts"
    @renderComplete="handleRenderComplete"
  />
</template>

<script>
export default {
  methods: {
    handleRenderComplete(chart) {
      console.log('Chart render complete:', chart)
      // Access chart instance
      this.chartInstance = chart
    }
  }
}
</script>
```

### Example: Using Chart Instance

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
    @complete="handleComplete"
  />
</template>

<script>
export default {
  data() {
    return {
      chartInstance: null
    }
  },
  methods: {
    handleComplete(chart) {
      this.chartInstance = chart
      // Use chart methods
      chart.showTooltip(0, 0)
    }
  }
}
</script>
```

### Key Points

- Handle @complete event
- Access chart instance
- Use chart methods
- Handle render completion
- Store chart instance for later use
