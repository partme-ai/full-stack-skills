# At-Rules

**官方文档**: https://sass-lang.com/documentation/


## At 规则

Sass 支持多种 @ 规则，用于控制编译和样式组织。

### @use

`@use` 用于加载模块（推荐使用，替代 @import）。

#### 基本用法

```scss
// _variables.scss
$primary-color: #409EFF;

// main.scss
@use 'variables';

.button {
  background-color: variables.$primary-color;
}
```

#### 使用命名空间

```scss
@use 'variables' as vars;

.button {
  background-color: vars.$primary-color;
}
```

#### 不使用命名空间

```scss
@use 'variables' as *;

.button {
  background-color: $primary-color; // 直接使用
}
```

### @forward

`@forward` 用于转发模块，使模块的成员可以被其他文件使用。

#### 基本用法

```scss
// _library.scss
$primary: #409EFF;
@mixin button { /* ... */ }

// _index.scss
@forward 'library';

// main.scss
@use 'index';
.button {
  @include index.button;
  background-color: index.$primary;
}
```

#### 控制可见性

```scss
@forward 'library' show $primary, button; // 只转发指定的
@forward 'library' hide $private; // 隐藏指定的
```

### @import（已弃用）

`@import` 已被弃用，建议使用 `@use` 和 `@forward`。

```scss
// 不推荐
@import 'variables';

// 推荐
@use 'variables';
```

### @include

`@include` 用于包含 mixin。

```scss
@mixin button-style {
  padding: 10px 20px;
}

.button {
  @include button-style;
}
```

### @mixin

`@mixin` 用于定义可重用的样式块。

```scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### @function

`@function` 用于定义函数。

```scss
@function rem($pixels) {
  @return $pixels / 16px * 1rem;
}
```

### @if, @else, @else if

条件语句。

```scss
$theme: 'dark';

.container {
  @if $theme == 'dark' {
    background-color: #333;
  } @else if $theme == 'light' {
    background-color: #fff;
  } @else {
    background-color: #f5f5f5;
  }
}
```

### @for

循环语句。

```scss
@for $i from 1 through 5 {
  .col-#{$i} {
    width: percentage($i / 12);
  }
}
```

`through` 包含结束值，`to` 不包含：

```scss
@for $i from 1 to 5 {
  // 1, 2, 3, 4（不包含 5）
}
```

### @each

遍历列表或映射。

```scss
$colors: red, blue, green;

@each $color in $colors {
  .text-#{$color} {
    color: $color;
  }
}
```

遍历映射：

```scss
$sizes: (
  'small': 12px,
  'medium': 16px,
  'large': 20px
);

@each $name, $size in $sizes {
  .text-#{$name} {
    font-size: $size;
  }
}
```

### @while

while 循环。

```scss
$i: 1;

@while $i <= 5 {
  .item-#{$i} {
    width: $i * 20px;
  }
  $i: $i + 1;
}
```

### @error

抛出错误。

```scss
@function divide($a, $b) {
  @if $b == 0 {
    @error "Cannot divide by zero";
  }
  @return $a / $b;
}
```

### @warn

发出警告。

```scss
@function old-function() {
  @warn "This function is deprecated";
  // ...
}
```

### @debug

输出调试信息。

```scss
$width: 100px;
@debug "Width is: #{$width}";
```

### @media

媒体查询（可以嵌套）。

```scss
.container {
  width: 100%;
  
  @media (min-width: 768px) {
    width: 750px;
  }
}
```

### @keyframes

关键帧动画。

```scss
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
```

### @extend

继承选择器（谨慎使用）。

```scss
.button {
  padding: 10px 20px;
}

.primary-button {
  @extend .button;
  background-color: #409EFF;
}
```

### 最佳实践

1. **使用 @use 替代 @import**：@import 已弃用
2. **合理使用 @forward**：用于创建模块库
3. **避免过度使用 @extend**：可能导致 CSS 体积增大
4. **使用 @error 验证**：在函数中验证参数
5. **组织 @ 规则**：按逻辑顺序组织
