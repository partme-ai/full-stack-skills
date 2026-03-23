# Basic Usage

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 基本使用

lime-echart 提供了 `<l-echart>` 组件，用于在 UniApp/UniAppX 中显示 ECharts 图表。

### 最简单的示例

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

### 使用 ref 获取图表实例

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
    <button @click="resizeChart">调整大小</button>
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
  methods: {
    resizeChart() {
      // 获取图表实例并调用 resize 方法
      this.$refs.chart.resize()
    }
  }
}
</script>
```

### 动态更新数据

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
    <button @click="updateData">更新数据</button>
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
          type: 'line'
        }]
      }
    }
  },
  methods: {
    updateData() {
      // 更新 option，组件会自动响应
      this.option.series[0].data = [
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200
      ]
    }
  }
}
</script>
```

### 使用 loading 状态

```vue
<template>
  <view class="chart-container">
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
      loading: true,
      option: {}
    }
  },
  onLoad() {
    // 模拟数据加载
    setTimeout(() => {
      this.option = {
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
      this.loading = false
    }, 1000)
  }
}
</script>
```

### 小程序环境使用（UMD 方式）

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
  </view>
</template>

<script>
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts: null,
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
  onLoad() {
    // 小程序中使用 require 引入
    this.echarts = require('@/static/echarts.min.js')
  }
}
</script>
```

## 组件属性

- `option`: ECharts 配置项对象（必填）
- `echarts`: ECharts 实例（必填）
- `loading`: 是否显示加载状态（可选）
- `initOptions`: ECharts 初始化选项（可选）

## 注意事项

1. 必须提供 `echarts` 和 `option` 属性
2. 图表容器需要有明确的高度
3. 在小程序中使用时，注意静态资源路径
4. 使用 `ref` 可以获取图表实例，调用相关方法
