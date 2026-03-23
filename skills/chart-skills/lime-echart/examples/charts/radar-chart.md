# Radar Chart

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 雷达图

雷达图用于展示多维度数据的对比。

### 基础雷达图

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
        radar: {
          indicator: [
            { name: '销售', max: 6500 },
            { name: '管理', max: 16000 },
            { name: '信息技术', max: 30000 },
            { name: '客服', max: 38000 },
            { name: '研发', max: 52000 },
            { name: '市场', max: 25000 }
          ]
        },
        series: [{
          type: 'radar',
          data: [
            {
              value: [4200, 3000, 20000, 35000, 50000, 18000],
              name: '预算分配'
            },
            {
              value: [5000, 14000, 28000, 26000, 42000, 21000],
              name: '实际开销'
            }
          ]
        }]
      }
    }
  }
}
</script>
```
