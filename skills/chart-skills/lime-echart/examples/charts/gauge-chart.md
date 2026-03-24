# Gauge Chart

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 仪表盘

仪表盘用于展示进度或完成度。

### 基础仪表盘

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
        series: [{
          type: 'gauge',
          progress: {
            show: true,
            width: 18
          },
          axisLine: {
            lineStyle: {
              width: 18
            }
          },
          axisTick: {
            show: false
          },
          splitLine: {
            length: 15,
            lineStyle: {
              width: 2,
              color: '#999'
            }
          },
          axisLabel: {
            distance: 25,
            color: '#999',
            fontSize: 20
          },
          anchor: {
            show: true,
            showAbove: true,
            size: 25,
            itemStyle: {
              borderWidth: 10
            }
          },
          title: {
            show: false
          },
          detail: {
            valueAnimation: true,
            fontSize: 50,
            offsetCenter: [0, '70%']
          },
          data: [{
            value: 70,
            name: 'SCORE'
          }]
        }]
      }
    }
  }
}
</script>
```
