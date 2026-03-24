# Chart with Data Binding Template

## 带数据绑定的图表模板

这是一个包含数据绑定和动态更新的图表模板。

```vue
<template>
  <view class="chart-container">
    <view class="chart-header">
      <text class="chart-title">{{ chartTitle }}</text>
      <button @click="refreshData" :loading="loading">刷新</button>
    </view>
    <l-echart 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
      :loading="loading"
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
      chartTitle: '数据图表',
      chartData: {
        categories: [],
        values: []
      },
      option: {
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: [],
          boundaryGap: false
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          name: '数据',
          type: 'line',
          data: [],
          smooth: true,
          areaStyle: {}
        }]
      }
    }
  },
  watch: {
    // 监听数据变化，自动更新图表
    'chartData.categories': {
      handler(newVal) {
        this.option.xAxis.data = newVal
      },
      deep: true
    },
    'chartData.values': {
      handler(newVal) {
        this.option.series[0].data = newVal
      },
      deep: true
    }
  },
  onLoad() {
    this.loadData()
  },
  onReady() {
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
    })
  },
  methods: {
    async loadData() {
      this.loading = true
      try {
        // 模拟数据获取
        const res = await this.fetchChartData()
        
        // 更新数据
        this.chartData = {
          categories: res.categories,
          values: res.values
        }
      } catch (error) {
        console.error('加载数据失败', error)
        uni.showToast({
          title: '加载失败',
          icon: 'none'
        })
      } finally {
        this.loading = false
      }
    },
    async fetchChartData() {
      // 实际项目中替换为真实的 API 调用
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({
            categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            values: [120, 200, 150, 80, 70, 110, 130]
          })
        }, 1000)
      })
    },
    async refreshData() {
      await this.loadData()
    },
    updateChartData(categories, values) {
      // 手动更新数据
      this.chartData = {
        categories,
        values
      }
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

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.chart-title {
  font-size: 16px;
  font-weight: bold;
  color: #333;
}
</style>
```

## 功能说明

1. **数据绑定**：使用 `watch` 监听数据变化，自动更新图表
2. **数据获取**：从接口获取数据
3. **刷新功能**：支持手动刷新数据
4. **加载状态**：显示加载动画
5. **响应式**：自动调整图表尺寸

## 使用说明

1. 修改 `fetchChartData` 方法，替换为真实的 API 调用
2. 根据需求调整图表配置
3. 可以调用 `updateChartData` 方法手动更新数据
