# Map Chart

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 地图

地图用于展示地理数据分布。

### 基础地图

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
        geo: {
          map: 'china',
          roam: true,
          label: {
            emphasis: {
              show: false
            }
          },
          itemStyle: {
            normal: {
              areaColor: '#323c48',
              borderColor: '#111'
            },
            emphasis: {
              areaColor: '#2a333d'
            }
          }
        },
        series: [{
          name: '数据',
          type: 'scatter',
          coordinateSystem: 'geo',
          data: [
            { name: '北京', value: [116.46, 39.92, 100] },
            { name: '上海', value: [121.48, 31.22, 200] },
            { name: '广州', value: [113.23, 23.16, 150] }
          ],
          symbolSize: function (val) {
            return val[2] / 10
          },
          itemStyle: {
            color: '#ff6b6b'
          }
        }]
      }
    }
  },
  onLoad() {
    // 注意：需要先注册地图数据
    // 可以通过 echarts.registerMap('china', chinaJson) 注册
  }
}
</script>
```
