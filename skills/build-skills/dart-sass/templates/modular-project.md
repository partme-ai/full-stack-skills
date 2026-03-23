# Modular Project Template

## 模块化项目模板

这是一个使用 Sass 模块系统的项目模板。

### 项目结构

```
project/
├── src/
│   └── scss/
│       ├── abstracts/
│       │   ├── _variables.scss
│       │   ├── _functions.scss
│       │   └── _mixins.scss
│       ├── base/
│       │   └── _reset.scss
│       ├── components/
│       │   ├── _button.scss
│       │   └── _card.scss
│       ├── layout/
│       │   ├── _header.scss
│       │   └── _footer.scss
│       └── main.scss
└── dist/
    └── css/
        └── main.css
```

### 文件内容

#### abstracts/_variables.scss

```scss
// 颜色
$primary-color: #409EFF !default;
$secondary-color: #67C23A !default;
$danger-color: #F56C6C !default;

// 字体
$font-size-base: 16px !default;
$font-family-base: 'Arial', sans-serif !default;

// 间距
$spacing-unit: 8px !default;
```

#### abstracts/_functions.scss

```scss
@use 'sass:math';

@function rem($pixels, $base: 16px) {
  @return math.div($pixels, $base) * 1rem;
}

@function spacing($multiplier) {
  @return $multiplier * $spacing-unit;
}
```

#### abstracts/_mixins.scss

```scss
@use 'variables' as vars;
@use 'functions' as f;

@mixin button-style {
  padding: f.spacing(2) f.spacing(3);
  border-radius: 4px;
  cursor: pointer;
  border: none;
  font-size: vars.$font-size-base;
}

@mixin respond-to($breakpoint) {
  @if $breakpoint == 'medium' {
    @media (min-width: 768px) {
      @content;
    }
  } @else if $breakpoint == 'large' {
    @media (min-width: 1024px) {
      @content;
    }
  }
}
```

#### base/_reset.scss

```scss
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-family-base);
  font-size: var(--font-size-base);
}
```

#### components/_button.scss

```scss
@use '../abstracts/variables' as vars;
@use '../abstracts/mixins' as m;

.button {
  @include m.button-style;
  background-color: vars.$primary-color;
  color: white;
  
  &:hover {
    background-color: darken(vars.$primary-color, 10%);
  }
  
  @include m.respond-to('medium') {
    padding: m.spacing(3) m.spacing(4);
  }
}
```

#### main.scss

```scss
// Abstracts
@use 'abstracts/variables' as vars;
@use 'abstracts/functions' as f;
@use 'abstracts/mixins' as m;

// Base
@use 'base/reset';

// Components
@use 'components/button';
@use 'components/card';

// Layout
@use 'layout/header';
@use 'layout/footer';
```

### package.json

```json
{
  "name": "modular-sass-project",
  "version": "1.0.0",
  "scripts": {
    "sass": "sass src/scss/main.scss dist/css/main.css",
    "sass:watch": "sass --watch src/scss:dist/css",
    "sass:build": "sass src/scss:dist/css --style compressed --no-source-map"
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

# 编译
npm run sass

# 监听模式
npm run sass:watch

# 生产构建
npm run sass:build
```
