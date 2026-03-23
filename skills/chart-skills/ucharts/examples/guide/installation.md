# Installation

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates how to install uCharts.

### Key Concepts

- Package installation
- Component import
- Platform-specific setup

### Example: Package Installation

```bash
# Using npm
npm install @qiun/ucharts

# Using yarn
yarn add @qiun/ucharts

# Using pnpm
pnpm add @qiun/ucharts
```

### Example: Component Import (uni-app)

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
import qiunDataChart from '@qiun/ucharts/components/qiun-data-chart/qiun-data-chart.vue'

export default {
  components: {
    qiunDataChart
  },
  data() {
    return {
      chartData: {},
      opts: {}
    }
  }
}
</script>
```

### Example: Easycom Configuration (uni-app)

```json
// pages.json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "^qiun-(.*)": "@qiun/ucharts/components/qiun-$1/qiun-$1.vue"
    }
  }
}
```

### Example: WeChat Mini Program

```json
// app.json
{
  "usingComponents": {
    "qiun-data-chart": "@qiun/ucharts/components/qiun-data-chart/qiun-data-chart"
  }
}
```

### Key Points

- Install @qiun/ucharts package
- Import component in uni-app
- Configure easycom for auto-import
- Use components in WeChat Mini Program
- Support multiple platforms
