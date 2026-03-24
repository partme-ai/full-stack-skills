# Basic Chart Template

## 基础图表模板

这是一个基础图表模板，可以直接使用或根据需求修改。

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
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      }
    }
  },
  onReady() {
    // 监听窗口尺寸变化
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
    })
  }
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 400px;
}
</style>
```

## 使用说明

1. 复制模板代码到你的页面
2. 根据需求修改 `option` 配置
3. 调整容器高度和样式
4. 添加数据获取逻辑
