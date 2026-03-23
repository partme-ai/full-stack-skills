# Control Flow

**官方文档**: https://sass-lang.com/documentation/


## 控制流

Sass 提供了多种控制流语句。

### @if, @else, @else if

条件语句。

```scss
$theme: 'dark';

.container {
  @if $theme == 'dark' {
    background-color: #333;
    color: #fff;
  } @else if $theme == 'light' {
    background-color: #fff;
    color: #333;
  } @else {
    background-color: #f5f5f5;
    color: #333;
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

### 实际应用

#### 生成工具类

```scss
$spacings: 4, 8, 12, 16, 20, 24;

@each $spacing in $spacings {
  .m-#{$spacing} {
    margin: #{$spacing}px;
  }
  .p-#{$spacing} {
    padding: #{$spacing}px;
  }
}
```

#### 响应式断点

```scss
$breakpoints: (
  'sm': 480px,
  'md': 768px,
  'lg': 1024px
);

@each $name, $size in $breakpoints {
  @media (min-width: $size) {
    .container-#{$name} {
      max-width: $size;
    }
  }
}
```
