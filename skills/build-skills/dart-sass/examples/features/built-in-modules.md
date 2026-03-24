# Built-in Modules

**官方文档**: https://sass-lang.com/documentation/


## 内置模块

Sass 提供了多个内置模块，包含常用的函数和工具。

### sass:math

数学函数模块。

```scss
@use 'sass:math';

.container {
  width: math.percentage(math.div(3, 4)); // 75%
  padding: math.ceil(10.7px); // 11px
  margin: math.floor(10.7px); // 10px
  font-size: math.max(12px, 14px, 16px); // 16px
}
```

常用函数：
- `math.ceil($number)` - 向上取整
- `math.floor($number)` - 向下取整
- `math.round($number)` - 四舍五入
- `math.max($numbers...)` - 最大值
- `math.min($numbers...)` - 最小值
- `math.percentage($number)` - 转换为百分比
- `math.div($dividend, $divisor)` - 除法

### sass:color

颜色函数模块。

```scss
@use 'sass:color';

$primary: #409EFF;

.button {
  background-color: $primary;
  border-color: color.adjust($primary, $lightness: -10%);
  color: color.adjust($primary, $lightness: 20%);
  
  &:hover {
    background-color: color.scale($primary, $lightness: 10%);
  }
}
```

常用函数：
- `color.adjust($color, ...)` - 调整颜色
- `color.scale($color, ...)` - 缩放颜色
- `color.change($color, ...)` - 改变颜色属性
- `color.mix($color1, $color2, $weight)` - 混合颜色
- `color.lighten($color, $amount)` - 变亮
- `color.darken($color, $amount)` - 变暗

### sass:string

字符串函数模块。

```scss
@use 'sass:string';

$text: 'hello world';

.title {
  content: string.to-upper-case($text); // HELLO WORLD
  text-transform: string.to-lower-case($text); // hello world
  font-family: string.quote($text); // "hello world"
}
```

常用函数：
- `string.quote($string)` - 添加引号
- `string.unquote($string)` - 移除引号
- `string.to-upper-case($string)` - 转大写
- `string.to-lower-case($string)` - 转小写
- `string.length($string)` - 字符串长度
- `string.index($string, $substring)` - 查找子串

### sass:list

列表函数模块。

```scss
@use 'sass:list';

$colors: red, blue, green;

.button {
  background-color: list.nth($colors, 1); // red
  color: list.length($colors); // 3
}
```

常用函数：
- `list.length($list)` - 列表长度
- `list.nth($list, $n)` - 获取第 n 个元素
- `list.append($list, $val)` - 追加元素
- `list.join($list1, $list2)` - 合并列表
- `list.index($list, $value)` - 查找索引

### sass:map

映射函数模块。

```scss
@use 'sass:map';

$breakpoints: (
  'small': 480px,
  'medium': 768px,
  'large': 1024px
);

.container {
  @media (min-width: map.get($breakpoints, 'medium')) {
    width: 750px;
  }
}
```

常用函数：
- `map.get($map, $key)` - 获取值
- `map.keys($map)` - 获取所有键
- `map.values($map)` - 获取所有值
- `map.has-key($map, $key)` - 检查键是否存在
- `map.merge($map1, $map2)` - 合并映射

### sass:meta

元函数模块。

```scss
@use 'sass:meta';

@mixin debug($value) {
  @debug meta.type-of($value);
}

.container {
  @include debug(10px); // number
}
```

常用函数：
- `meta.type-of($value)` - 获取类型
- `meta.variable-exists($name)` - 检查变量是否存在
- `meta.mixin-exists($name)` - 检查 mixin 是否存在
- `meta.function-exists($name)` - 检查函数是否存在

### 使用多个模块

```scss
@use 'sass:math';
@use 'sass:color';
@use 'sass:string';

$primary: #409EFF;

.button {
  width: math.percentage(math.div(1, 2)); // 50%
  background-color: color.lighten($primary, 10%);
  text-transform: string.to-upper-case('button');
}
```

### 最佳实践

1. **按需引入**：只引入需要的模块
2. **使用命名空间**：避免函数名冲突
3. **优先使用内置函数**：性能更好
4. **查看文档**：了解所有可用函数
5. **组合使用**：多个模块可以一起使用
