# Global Configuration | 全局配置

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to configure Avue globally.

### Key Concepts

- Global configuration
- Internationalization setup
- Default settings
- Custom configuration

### Example: Basic Global Config

```javascript
// main.js
import Vue from 'vue'
import Avue from '@smallwei/avue'
import '@smallwei/avue/lib/index.css'

Vue.use(Avue, {
  // Global configuration options
})
```

### Example: Internationalization

```javascript
// main.js
import Vue from 'vue'
import Avue from '@smallwei/avue'
import AvueLocale from '@smallwei/avue/lib/locale'
import zhLocale from '@smallwei/avue/lib/locale/lang/zh-CN'
import enLocale from '@smallwei/avue/lib/locale/lang/en'

// Set default locale
AvueLocale.use(zhLocale)

Vue.use(Avue)
```

### Example: Custom Configuration

```javascript
// main.js
import Vue from 'vue'
import Avue from '@smallwei/avue'

Vue.use(Avue, {
  size: 'small', // Default size
  menuType: 'icon', // Menu type
  theme: 'light' // Theme
})
```

### Key Points

- Configure Avue via Vue.use() options
- Set internationalization with AvueLocale
- Configure default size, theme, etc.
- Global config affects all Avue components
- Can override in component level
