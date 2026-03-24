# Tree Chart

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 树图

树图用于展示层级结构数据。

### 基础树图

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
          type: 'tree',
          data: [{
            name: 'tree',
            children: [
              {
                name: 'view',
                children: [
                  { name: 'graph', value: 1 },
                  { name: 'tree', value: 3 },
                  { name: 'force', value: 2 }
                ]
              },
              {
                name: 'chart',
                children: [
                  { name: 'bar', value: 4 },
                  { name: 'line', value: 4 },
                  { name: 'pie', value: 2 }
                ]
              }
            ]
          }],
          top: '5%',
          left: '7%',
          bottom: '5%',
          right: '20%',
          symbolSize: 7,
          label: {
            position: 'left',
            verticalAlign: 'middle',
            align: 'right'
          },
          leaves: {
            label: {
              position: 'right',
              verticalAlign: 'middle',
              align: 'left'
            }
          },
          emphasis: {
            focus: 'descendant'
          },
          expandAndCollapse: true,
          animationDuration: 550,
          animationDurationUpdate: 750
        }]
      }
    }
  }
}
</script>
```
