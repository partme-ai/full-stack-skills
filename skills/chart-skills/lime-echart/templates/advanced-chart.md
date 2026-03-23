# Advanced Chart Template

## 高级图表模板

这是一个包含完整功能的高级图表模板。

```vue
<template>
  <view class="chart-container">
    <l-echart 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
      :loading="loading"
      :init-options="initOptions"
      @click="handleClick"
      @legendselectchanged="handleLegendSelect"
    ></l-echart>
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
      loading: false,
      initOptions: {
        renderer: 'canvas',
        devicePixelRatio: 2
      },
      option: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['系列1', '系列2'],
          top: '10%'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          top: '15%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisLabel: {
            rotate: 0
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: '{value}'
          }
        },
        series: [
          {
            name: '系列1',
            type: 'bar',
            data: [120, 200, 150, 80, 70, 110, 130],
            itemStyle: {
              color: '#409EFF'
            }
          },
          {
            name: '系列2',
            type: 'line',
            data: [220, 182, 191, 234, 290, 330, 310],
            itemStyle: {
              color: '#67C23A'
            }
          }
        ]
      }
    }
  },
  onLoad() {
    this.fetchData()
  },
  onReady() {
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
    })
  },
  methods: {
    async fetchData() {
      this.loading = true
      try {
        // 获取数据
        const res = await uni.request({
          url: 'https://api.example.com/chart-data',
          method: 'GET'
        })
        
        // 更新图表数据
        this.option.xAxis.data = res.data.categories
        this.option.series[0].data = res.data.values1
        this.option.series[1].data = res.data.values2
      } catch (error) {
        console.error('获取数据失败', error)
        uni.showToast({
          title: '加载失败',
          icon: 'none'
        })
      } finally {
        this.loading = false
      }
    },
    handleClick(params) {
      console.log('点击事件', params)
      uni.showToast({
        title: `点击了 ${params.name}`,
        icon: 'none'
      })
    },
    handleLegendSelect(params) {
      console.log('图例选择变化', params)
    },
    updateData() {
      // 更新数据
      const chartInstance = this.$refs.chart.getChart()
      chartInstance.setOption({
        series: [{
          data: [Math.random() * 200, Math.random() * 200, Math.random() * 200]
        }]
      })
    }
  }
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 500px;
  background: #fff;
  border-radius: 8px;
  padding: 10px;
}
</style>
```

## 功能说明

1. **数据加载**：从接口获取数据并更新图表
2. **加载状态**：显示加载动画
3. **事件处理**：处理点击和图例选择事件
4. **响应式**：自动调整图表尺寸
5. **多系列**：支持多个数据系列
