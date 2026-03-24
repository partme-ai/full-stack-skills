---
name: vue2
description: Provides comprehensive guidance for Vue 2.x development including Options API, components, directives, lifecycle hooks, computed properties, watchers, Vuex state management, and Vue Router. Use when the user asks about Vue 2, needs to create Vue 2 components, implement reactive data binding, handle component communication, or work with Vue 2 ecosystem tools.
---

# Vue 2 开发指南

## 概述

本技能提供 Vue 2.x 框架的完整开发指南，包括 Options API、组件系统、路由管理、状态管理（Vuex）、生命周期等核心概念和最佳实践。

## 核心特性

### 1. Options API

Vue 2 使用 Options API 组织组件代码。

**基本结构**：

```vue
<template>
  <div>
    <p>{{ message }}</p>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  name: 'Counter',
  data() {
    return {
      message: 'Hello Vue 2',
      count: 0
    }
  },
  computed: {
    doubleCount() {
      return this.count * 2
    }
  },
  watch: {
    count(newVal, oldVal) {
      console.log(`count changed from ${oldVal} to ${newVal}`)
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    console.log('Component mounted')
  }
}
</script>
```

### 2. 响应式数据

**data**：定义响应式数据

```javascript
data() {
  return {
    message: 'Hello',
    count: 0,
    user: {
      name: 'Vue',
      age: 2
    }
  }
}
```

**注意事项**：
- 使用 `this.$set` 添加新属性
- 使用 `Vue.set` 或 `this.$set` 修改数组索引

### 3. 计算属性和监听器

**计算属性**：

```javascript
computed: {
  fullName() {
    return `${this.firstName} ${this.lastName}`
  }
}
```

**监听器**：

```javascript
watch: {
  // 简单监听
  count(newVal, oldVal) {
    // ...
  },
  // 深度监听
  user: {
    handler(newVal, oldVal) {
      // ...
    },
    deep: true
  }
}
```

### 4. 组件开发

**组件定义**：

```vue
<template>
  <div>
    <h3>{{ title }}</h3>
    <p>{{ content }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyComponent',
  props: {
    title: {
      type: String,
      required: true
    },
    content: {
      type: String,
      default: ''
    }
  },
  emits: ['update', 'delete'],
  methods: {
    handleClick() {
      this.$emit('update', this.title)
    }
  }
}
</script>
```

**组件通信**：
- Props：父 → 子
- `$emit`：子 → 父
- `$parent` / `$children`：父子组件直接访问
- `$refs`：访问子组件实例
- Vuex：全局状态管理
- EventBus：事件总线

### 5. 路由管理（Vue Router）

**基本配置**：

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: () => import('./views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('./views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})
```

**路由使用**：

```vue
<template>
  <div>
    <router-link to="/about">About</router-link>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    goToAbout() {
      this.$router.push('/about')
    }
  },
  mounted() {
    console.log(this.$route.params)
  }
}
</script>
```

### 6. 状态管理（Vuex）

**Store 定义**：

```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 0
  },
  getters: {
    doubleCount: state => state.count * 2
  },
  mutations: {
    INCREMENT(state) {
      state.count++
    }
  },
  actions: {
    increment({ commit }) {
      commit('INCREMENT')
    }
  }
})
```

**在组件中使用**：

```vue
<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState(['count']),
    ...mapGetters(['doubleCount'])
  },
  methods: {
    ...mapActions(['increment'])
  }
}
</script>
```

### 7. 生命周期钩子

```javascript
export default {
  beforeCreate() {
    // 实例初始化之后，数据观测之前
  },
  created() {
    // 实例创建完成，数据观测完成
  },
  beforeMount() {
    // 挂载开始之前
  },
  mounted() {
    // 挂载完成
  },
  beforeUpdate() {
    // 数据更新时，DOM 更新之前
  },
  updated() {
    // DOM 更新完成
  },
  beforeDestroy() {
    // 实例销毁之前
  },
  destroyed() {
    // 实例销毁完成
  }
}
```

## 最佳实践

### 1. 代码组织

- 使用单文件组件（.vue）
- 合理拆分组件
- 使用 mixins 复用逻辑

### 2. 性能优化

- 使用 `v-if` 和 `v-show` 合理选择
- 使用 `key` 优化列表渲染
- 懒加载路由组件
- 使用 `Object.freeze()` 冻结大对象

### 3. 组件通信

- 优先使用 Props 和 Events
- 复杂状态使用 Vuex
- 避免过度使用 `$parent` 和 `$children`

### 4. 响应式注意事项

```javascript
// 添加新属性
this.$set(this.user, 'age', 25)

// 修改数组索引
this.$set(this.items, 0, newItem)

// 修改数组长度
this.items.splice(newLength)
```

## 常用工具和插件

- **Vue CLI**：项目脚手架
- **Vue Router**：路由管理
- **Vuex**：状态管理
- **Element UI**：UI 组件库
- **Ant Design Vue**：UI 组件库
- **Axios**：HTTP 客户端

## 示例 Prompt

- "使用 Vue 2 创建一个计数器组件"
- "如何在 Vue 2 中使用 Vuex 进行状态管理？"
- "创建一个 Vue 2 项目，使用 Vue CLI"
- "Vue 2 的生命周期钩子有哪些？"
- "如何在 Vue 2 中实现组件通信？"
