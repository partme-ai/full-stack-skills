# Installation

## Using npm or yarn

We recommend using npm or yarn for development.

```bash
$ npm install ant-design-vue@4.x --save
# or
$ yarn add ant-design-vue@4.x
```

## Import

### Global Import

```typescript
import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import App from './App.vue';
import 'ant-design-vue/dist/reset.css';

const app = createApp(App);

app.use(Antd).mount('#app');
```

### On-demand Import (Recommended)

Use `unplugin-vue-components` for auto-importing components.

```bash
npm install unplugin-vue-components -D
```

`vite.config.ts`:

```typescript
import { defineConfig } from 'vite';
import Components from 'unplugin-vue-components/vite';
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers';

export default defineConfig({
  plugins: [
    // ...
    Components({
      resolvers: [
        AntDesignVueResolver({
          importStyle: false, // css in js
        }),
      ],
    }),
  ],
});
```
