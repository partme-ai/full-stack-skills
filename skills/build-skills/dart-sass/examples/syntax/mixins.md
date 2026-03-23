# Mixins

**官方文档**: https://sass-lang.com/documentation/


## 混合（Mixins）

Mixins 允许定义可重用的样式块，可以在多个地方使用。

### 基本语法

#### 定义 Mixin

使用 `@mixin` 定义：

```scss
@mixin button-style {
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  border: none;
}
```

#### 使用 Mixin

使用 `@include` 引入：

```scss
.button {
  @include button-style;
  background-color: #409EFF;
  color: white;
}
```

编译后：

```css
.button {
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  border: none;
  background-color: #409EFF;
  color: white;
}
```

### 带参数的 Mixin

#### 单个参数

```scss
@mixin border-radius($radius) {
  border-radius: $radius;
}

.button {
  @include border-radius(4px);
}
```

#### 多个参数

```scss
@mixin button($bg-color, $text-color, $padding) {
  background-color: $bg-color;
  color: $text-color;
  padding: $padding;
  border: none;
  border-radius: 4px;
}

.primary-button {
  @include button(#409EFF, white, 10px 20px);
}
```

#### 命名参数

```scss
@mixin button($bg-color, $text-color: white, $padding: 10px) {
  background-color: $bg-color;
  color: $text-color;
  padding: $padding;
}

.button {
  @include button($bg-color: #409EFF, $padding: 15px);
}
```

#### 默认参数

```scss
@mixin button($bg-color: #409EFF, $text-color: white, $padding: 10px 20px) {
  background-color: $bg-color;
  color: $text-color;
  padding: $padding;
}

.button {
  @include button; // 使用所有默认值
}

.custom-button {
  @include button(#67C23A); // 只覆盖第一个参数
}
```

### 参数列表

#### 可变参数

使用 `...` 接受多个参数：

```scss
@mixin box-shadow($shadows...) {
  box-shadow: $shadows;
}

.card {
  @include box-shadow(0 2px 4px rgba(0,0,0,0.1), 0 4px 8px rgba(0,0,0,0.1));
}
```

### Mixin 内容块

#### 传递内容块

使用 `@content` 接收内容：

```scss
@mixin media-query($breakpoint) {
  @media (min-width: $breakpoint) {
    @content;
  }
}

.container {
  width: 100%;
  
  @include media-query(768px) {
    width: 750px;
    margin: 0 auto;
  }
}
```

编译后：

```css
.container {
  width: 100%;
}

@media (min-width: 768px) {
  .container {
    width: 750px;
    margin: 0 auto;
  }
}
```

### 常用 Mixin 示例

#### Flexbox 居中

```scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  @include flex-center;
  height: 100vh;
}
```

#### 清除浮动

```scss
@mixin clearfix {
  &::after {
    content: '';
    display: table;
    clear: both;
  }
}

.row {
  @include clearfix;
}
```

#### 文本截断

```scss
@mixin text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.title {
  @include text-truncate;
  max-width: 200px;
}
```

#### 响应式断点

```scss
@mixin respond-to($breakpoint) {
  @if $breakpoint == 'small' {
    @media (min-width: 480px) {
      @content;
    }
  } @else if $breakpoint == 'medium' {
    @media (min-width: 768px) {
      @content;
    }
  } @else if $breakpoint == 'large' {
    @media (min-width: 1024px) {
      @content;
    }
  }
}

.container {
  width: 100%;
  
  @include respond-to('medium') {
    width: 750px;
  }
  
  @include respond-to('large') {
    width: 970px;
  }
}
```

### Mixin 文件组织

#### 创建 Mixin 文件

`_mixins.scss`:

```scss
@mixin button-style {
  // ...
}

@mixin flex-center {
  // ...
}

@mixin clearfix {
  // ...
}
```

#### 使用 Mixin 文件

```scss
@use 'mixins';

.button {
  @include mixins.button-style;
}
```

或使用命名空间：

```scss
@use 'mixins' as m;

.button {
  @include m.button-style;
}
```

### 最佳实践

1. **命名清晰**：Mixin 名称应该清楚表达功能
2. **参数合理**：使用默认参数提高灵活性
3. **组织文件**：将相关 mixins 放在单独文件中
4. **避免过度使用**：不是所有样式都需要 mixin
5. **使用 @use**：使用模块系统而不是 @import
