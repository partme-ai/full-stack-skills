# Installation Templates

## npm Installation

```bash
npm install @qiun/ucharts
```

## uni-app Easycom Configuration

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

## Component Import (uni-app)

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

## WeChat Mini Program Configuration

```json
// app.json
{
  "usingComponents": {
    "qiun-data-chart": "@qiun/ucharts/components/qiun-data-chart/qiun-data-chart"
  }
}
```
