# Extending RouterLink | 扩展 RouterLink

**官方文档**: https://router.vuejs.org/guide/advanced/extending-router-link.html

## 适用场景
- 自定义链接样式或行为
- 统一封装项目内导航

## 核心用法
```ts
import { defineComponent } from 'vue'
import { useLink } from 'vue-router'

// useCustomLink(): 封装 RouterLink 行为
export const useCustomLink = (props: any) => {
  const link = useLink(props)
  return link
}

// CustomLink: 自定义链接组件
export default defineComponent({
  props: ['to'],
  setup(props) {
    return useCustomLink(props)
  }
})
```
