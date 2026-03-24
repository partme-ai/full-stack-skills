# Functions

**官方文档**: https://sass-lang.com/documentation/


## 函数

Sass 函数用于计算和返回值，可以在样式表中使用。

### 自定义函数

#### 基本语法

使用 `@function` 定义函数：

```scss
@function calculate-rem($pixels) {
  @return $pixels / 16px * 1rem;
}

.text {
  font-size: calculate-rem(24px); // 1.5rem
}
```

#### 多个参数

```scss
@function calculate-width($container-width, $columns, $gap) {
  @return ($container-width - ($gap * ($columns - 1))) / $columns;
}

.column {
  width: calculate-width(1200px, 3, 20px);
}
```

#### 条件逻辑

```scss
@function get-color($type) {
  @if $type == 'primary' {
    @return #409EFF;
  } @else if $type == 'secondary' {
    @return #67C23A;
  } @else {
    @return #333;
  }
}

.button {
  background-color: get-color('primary');
}
```

### 内置函数

#### 颜色函数

```scss
$primary: #409EFF;

.button {
  background-color: $primary;
  border-color: darken($primary, 10%);
  color: lighten($primary, 20%);
  
  &:hover {
    background-color: adjust-hue($primary, 30deg);
  }
}
```

常用颜色函数：
- `lighten($color, $amount)` - 变亮
- `darken($color, $amount)` - 变暗
- `saturate($color, $amount)` - 增加饱和度
- `desaturate($color, $amount)` - 降低饱和度
- `adjust-hue($color, $degrees)` - 调整色相
- `mix($color1, $color2, $weight)` - 混合颜色

#### 数学函数

```scss
$width: 100px;
$height: 200px;

.container {
  width: $width;
  height: $height;
  max-width: max($width, 200px);
  min-height: min($height, 150px);
  padding: percentage(0.1); // 10%
}
```

常用数学函数：
- `abs($number)` - 绝对值
- `ceil($number)` - 向上取整
- `floor($number)` - 向下取整
- `round($number)` - 四舍五入
- `max($numbers...)` - 最大值
- `min($numbers...)` - 最小值
- `percentage($number)` - 转换为百分比

#### 字符串函数

```scss
$text: 'Hello World';

.title {
  content: quote($text); // "Hello World"
  text-transform: to-upper-case($text); // HELLO WORLD
}
```

常用字符串函数：
- `quote($string)` - 添加引号
- `unquote($string)` - 移除引号
- `to-upper-case($string)` - 转大写
- `to-lower-case($string)` - 转小写
- `str-length($string)` - 字符串长度

#### 列表函数

```scss
$colors: red, blue, green;

.button {
  background-color: nth($colors, 1); // red
  color: length($colors); // 3
}
```

常用列表函数：
- `length($list)` - 列表长度
- `nth($list, $n)` - 获取第 n 个元素
- `append($list, $val)` - 追加元素
- `join($list1, $list2)` - 合并列表
- `index($list, $value)` - 查找索引

#### 映射函数

```scss
$breakpoints: (
  'small': 480px,
  'medium': 768px,
  'large': 1024px
);

.container {
  @media (min-width: map-get($breakpoints, 'medium')) {
    width: 750px;
  }
}
```

常用映射函数：
- `map-get($map, $key)` - 获取值
- `map-keys($map)` - 获取所有键
- `map-values($map)` - 获取所有值
- `map-has-key($map, $key)` - 检查键是否存在
- `map-merge($map1, $map2)` - 合并映射

### 函数示例

#### 计算 rem

```scss
@function rem($pixels, $base: 16px) {
  @return $pixels / $base * 1rem;
}

.text {
  font-size: rem(24px); // 1.5rem
  margin: rem(16px); // 1rem
}
```

#### 获取断点值

```scss
$breakpoints: (
  'xs': 0,
  'sm': 480px,
  'md': 768px,
  'lg': 1024px,
  'xl': 1280px
);

@function breakpoint($name) {
  @return map-get($breakpoints, $name);
}

.container {
  @media (min-width: breakpoint('md')) {
    width: 750px;
  }
}
```

#### 颜色工具函数

```scss
@function tint($color, $percentage) {
  @return mix(white, $color, $percentage);
}

@function shade($color, $percentage) {
  @return mix(black, $color, $percentage);
}

.button {
  background-color: tint(#409EFF, 20%);
  border-color: shade(#409EFF, 10%);
}
```

### 函数文件组织

#### 创建函数文件

`_functions.scss`:

```scss
@function rem($pixels, $base: 16px) {
  @return $pixels / $base * 1rem;
}

@function breakpoint($name) {
  // ...
}
```

#### 使用函数文件

```scss
@use 'functions' as f;

.text {
  font-size: f.rem(24px);
}
```

### 最佳实践

1. **单一职责**：每个函数只做一件事
2. **命名清晰**：函数名应该清楚表达功能
3. **参数验证**：检查参数有效性
4. **使用内置函数**：优先使用内置函数
5. **组织文件**：将相关函数放在单独文件中
