# Configuration

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 配置选项

lime-echart 组件支持多种配置选项，用于自定义图表的行为和外观。

### 基本配置

```vue
<template>
  <l-echart 
    ref="chart"
    :option="option"
    :echarts="echarts"
    :init-options="initOptions"
    :loading="loading"
  ></l-echart>
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
        renderer: 'canvas', // 或 'svg'
        width: 'auto',
        height: 'auto'
      },
      option: {
        // ECharts 配置项
      }
    }
  }
}
</script>
```

### initOptions 配置

`initOptions` 用于配置 ECharts 实例的初始化选项：

```javascript
{
  // 渲染器类型：'canvas' 或 'svg'
  renderer: 'canvas',
  
  // 图表宽度，'auto' 表示自动
  width: 'auto',
  
  // 图表高度，'auto' 表示自动
  height: 'auto',
  
  // 设备像素比
  devicePixelRatio: 2,
  
  // 是否启用动画
  useDirtyRect: false
}
```

### 主题配置

```vue
<template>
  <l-echart 
    ref="chart"
    :option="option"
    :echarts="echarts"
    :theme="theme"
  ></l-echart>
</template>

<script>
import * as echarts from 'echarts'
// 引入主题
import 'echarts/theme/dark'
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts,
      theme: 'dark', // 使用暗色主题
      option: {
        // ECharts 配置项
      }
    }
  }
}
</script>
```

### 响应式配置

```vue
<template>
  <view class="chart-container" :style="{ height: chartHeight + 'px' }">
    <l-echart 
      ref="chart"
      :option="option"
      :echarts="echarts"
      @resize="handleResize"
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
      chartHeight: 400,
      option: {
        // ECharts 配置项
      }
    }
  },
  onReady() {
    // 监听页面尺寸变化
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
    })
  },
  methods: {
    handleResize() {
      // 处理图表尺寸变化
      console.log('图表尺寸已调整')
    }
  }
}
</script>
```

### 按需引入配置（H5/App）

```javascript
// 按需引入 ECharts 模块，减小打包体积
import * as echarts from 'echarts/core'
import { BarChart, LineChart, PieChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

// 注册必要的组件
echarts.use([
  BarChart,
  LineChart,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  CanvasRenderer
])

export default {
  data() {
    return {
      echarts
    }
  }
}
```

### 小程序配置优化

```javascript
// 小程序中使用 UMD 方式
export default {
  data() {
    return {
      echarts: null,
      option: {}
    }
  },
  onLoad() {
    // 使用相对路径引入
    this.echarts = require('../../static/echarts.min.js')
    
    // 或者使用绝对路径
    // this.echarts = require('@/static/echarts.min.js')
  }
}
```

### 自定义配置示例

```vue
<template>
  <l-echart 
    ref="chart"
    :option="option"
    :echarts="echarts"
    :init-options="initOptions"
    :loading="loading"
    :loading-options="loadingOptions"
  ></l-echart>
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
      loadingOptions: {
        text: '加载中...',
        color: '#409EFF',
        textColor: '#000',
        maskColor: 'rgba(255, 255, 255, 0.8)',
        zlevel: 0
      },
      initOptions: {
        renderer: 'canvas',
        devicePixelRatio: 2
      },
      option: {
        // ECharts 配置项
      }
    }
  }
}
</script>
```

## 配置项说明

### option
- **类型**: Object
- **必填**: 是
- **说明**: ECharts 的配置项对象，包含图表的全部配置

### echarts
- **类型**: Object
- **必填**: 是
- **说明**: ECharts 实例，通过 `import * as echarts from 'echarts'` 或 `require()` 获取

### initOptions
- **类型**: Object
- **必填**: 否
- **说明**: ECharts 初始化选项，包括渲染器类型、尺寸等

### loading
- **类型**: Boolean
- **必填**: 否
- **默认值**: false
- **说明**: 是否显示加载状态

### loadingOptions
- **类型**: Object
- **必填**: 否
- **说明**: 加载状态的配置选项

### theme
- **类型**: String
- **必填**: 否
- **说明**: 主题名称，需要先引入对应的主题文件

## 最佳实践

1. **H5/App 环境**：使用 ES 模块按需引入，减小打包体积
2. **小程序环境**：使用 UMD 方式，注意静态资源路径
3. **性能优化**：合理设置 `devicePixelRatio`，避免过高导致性能问题
4. **响应式设计**：监听窗口尺寸变化，及时调用 `resize()` 方法
5. **主题统一**：在应用中统一使用主题，保持视觉一致性
