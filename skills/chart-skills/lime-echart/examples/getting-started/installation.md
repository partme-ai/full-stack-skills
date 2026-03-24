# Installation

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 安装 lime-echart

lime-echart 是为 UniApp 和 UniAppX 提供 ECharts 图表兼容支持的插件，使 ECharts 图表能在 H5、小程序、App 中运行。

### 方式一：通过 DCloud 插件市场安装

1. 访问 DCloud 插件市场：https://ext.dcloud.net.cn/plugin?id=4899
2. 点击"使用 HBuilderX 导入插件"或下载插件
3. 将插件导入到项目的 `uni_modules` 目录

### 方式二：通过 npm 安装

```bash
npm install echarts --save
```

然后从插件市场下载 lime-echart 插件，或使用 npm：

```bash
npm install lime-echart --save
```

### 方式三：手动安装

1. 下载 lime-echart 插件
2. 将插件文件复制到项目的 `uni_modules/lime-echart` 目录
3. 安装 ECharts 依赖：

```bash
npm install echarts --save
```

## 引入 ECharts 资源

### UMD 方式（推荐用于小程序）

1. 下载 `echarts.min.js` 文件
2. 将文件放入项目的 `static` 目录
3. 在页面中引入：

```javascript
// 在页面 script 中
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  onLoad() {
    // 动态引入 echarts
    this.echarts = require('@/static/echarts.min.js')
  }
}
```

### ES 模块方式（推荐用于 H5 和 App）

```javascript
import * as echarts from 'echarts'
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts
    }
  }
}
```

## 平台兼容性

lime-echart 支持以下平台：

- ✅ UniApp (Vue2/Vue3)
- ✅ UniAppX
- ✅ H5
- ✅ 微信小程序
- ✅ 支付宝小程序
- ✅ 抖音小程序
- ✅ 百度小程序
- ✅ 快手小程序
- ✅ App (Android/iOS)

## 注意事项

1. **小程序环境**：建议使用 UMD 方式引入，避免打包体积过大
2. **H5 和 App**：推荐使用 ES 模块方式，支持按需引入
3. **路径问题**：在小程序中，静态资源路径需要使用相对路径或绝对路径
4. **版本兼容**：确保 ECharts 版本与 lime-echart 版本兼容

## 验证安装

创建测试页面验证安装是否成功：

```vue
<template>
  <view class="container">
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

<style>
.container {
  width: 100%;
  height: 400px;
}
</style>
```

如果图表正常显示，说明安装成功。
