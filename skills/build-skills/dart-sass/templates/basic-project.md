# Basic Project Template

## 基础项目模板

这是一个基础的 Sass 项目结构模板。

### 项目结构

```
project/
├── src/
│   └── scss/
│       ├── _variables.scss
│       ├── _mixins.scss
│       ├── main.scss
│       └── components/
│           ├── _button.scss
│           └── _card.scss
├── dist/
│   └── css/
│       └── main.css
└── package.json
```

### 文件内容

#### _variables.scss

```scss
// 颜色
$primary-color: #409EFF;
$secondary-color: #67C23A;
$danger-color: #F56C6C;

// 字体
$font-size-base: 16px;
$font-family-base: 'Arial', sans-serif;

// 间距
$spacing-unit: 8px;
```

#### _mixins.scss

```scss
@use 'variables' as vars;

@mixin button-style {
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  border: none;
}

@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

#### _button.scss

```scss
@use '../variables' as vars;
@use '../mixins' as m;

.button {
  @include m.button-style;
  background-color: vars.$primary-color;
  color: white;
  
  &:hover {
    background-color: darken(vars.$primary-color, 10%);
  }
}
```

#### main.scss

```scss
@use 'variables' as vars;
@use 'mixins' as m;
@use 'components/button';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: vars.$font-family-base;
  font-size: vars.$font-size-base;
}

.container {
  @include m.flex-center;
  min-height: 100vh;
}
```

### package.json

```json
{
  "name": "sass-project",
  "version": "1.0.0",
  "scripts": {
    "sass": "sass src/scss/main.scss dist/css/main.css",
    "sass:watch": "sass --watch src/scss/main.scss:dist/css/main.css",
    "sass:build": "sass src/scss/main.scss dist/css/main.css --style compressed --no-source-map"
  },
  "devDependencies": {
    "sass": "^1.69.5"
  }
}
```

### 使用

```bash
# 安装依赖
npm install

# 编译一次
npm run sass

# 监听模式
npm run sass:watch

# 生产构建
npm run sass:build
```
