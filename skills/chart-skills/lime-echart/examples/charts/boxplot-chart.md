# Boxplot Chart

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 箱线图

箱线图用于展示数据的分布情况。

### 基础箱线图

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
        dataset: [{
          source: [
            [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
            [960, 940, 960, 940, 880, 880, 800, 850, 880, 880, 830, 790],
            [880, 880, 880, 860, 720, 720, 620, 860, 970, 950, 880, 910]
          ]
        }, {
          transform: {
            type: 'boxplot',
            config: { itemNameFormatter: 'expr {value}' }
          }
        }, {
          fromDatasetIndex: 1,
          fromTransformResult: 1
        }],
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '10%',
          right: '10%',
          bottom: '15%'
        },
        xAxis: {
          type: 'category',
          boundaryGap: true,
          nameGap: 30,
          splitArea: {
            show: false
          },
          splitLine: {
            show: false
          }
        },
        yAxis: {
          type: 'value',
          name: 'Value',
          splitArea: {
            show: true
          }
        },
        series: [
          {
            name: 'boxplot',
            type: 'boxplot',
            datasetIndex: 1
          },
          {
            name: 'outlier',
            type: 'scatter',
            datasetIndex: 2
          }
        ]
      }
    }
  }
}
</script>
```
