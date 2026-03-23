# Scatter Chart

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 散点图

散点图用于展示两个变量之间的关系。

### 基础散点图

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
  </view>
</template>

<script>
import * as echarts from 'echarts'
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts,
      option: {
        xAxis: {},
        yAxis: {},
        series: [{
          symbolSize: 20,
          data: [
            [10.0, 8.04],
            [8.0, 6.95],
            [13.0, 7.58],
            [9.0, 8.81],
            [11.0, 8.33],
            [14.0, 9.96],
            [6.0, 7.24],
            [4.0, 4.26],
            [12.0, 10.84],
            [7.0, 4.82],
            [5.0, 5.68]
          ],
          type: 'scatter'
        }]
      }
    }
  }
}
</script>
```

### 气泡图

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
  </view>
</template>

<script>
import * as echarts from 'echarts'
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts,
      option: {
        xAxis: {
          scale: true
        },
        yAxis: {
          scale: true
        },
        series: [{
          type: 'scatter',
          data: [
            [161.2, 51.6], [167.5, 59.0], [159.5, 49.2],
            [157.0, 63.0], [155.8, 53.6], [170.0, 59.0],
            [160.0, 52.2], [153.0, 49.0], [169.0, 62.0]
          ],
          symbolSize: function (data) {
            return Math.sqrt(data[2]) / 5e2
          }
        }]
      }
    }
  }
}
</script>
```
