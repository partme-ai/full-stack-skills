# Heatmap

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 热力图

热力图用于展示数据的密度分布。

### 基础热力图

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
        tooltip: {
          position: 'top'
        },
        grid: {
          height: '50%',
          top: '10%'
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          splitArea: {
            show: true
          }
        },
        yAxis: {
          type: 'category',
          data: ['Morning', 'Afternoon', 'Evening'],
          splitArea: {
            show: true
          }
        },
        visualMap: {
          min: 0,
          max: 10,
          calculable: true,
          orient: 'horizontal',
          left: 'center',
          bottom: '15%'
        },
        series: [{
          name: 'Punch Card',
          type: 'heatmap',
          data: [
            [0, 0, 5], [0, 1, 1], [0, 2, 0],
            [1, 0, 0], [1, 1, 0], [1, 2, 0],
            [2, 0, 0], [2, 1, 0], [2, 2, 0],
            [3, 0, 0], [3, 1, 1], [3, 2, 0],
            [4, 0, 1], [4, 1, 9], [4, 2, 0],
            [5, 0, 3], [5, 1, 2], [5, 2, 0],
            [6, 0, 1], [6, 1, 0], [6, 2, 0]
          ],
          label: {
            show: true
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }]
      }
    }
  }
}
</script>
```
