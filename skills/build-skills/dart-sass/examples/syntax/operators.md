# Operators

**官方文档**: https://sass-lang.com/documentation/


## 运算符

Sass 支持各种数学和逻辑运算符。

### 数学运算符

#### 基本运算

```scss
$width: 100px;
$padding: 20px;

.container {
  width: $width + $padding * 2; // 140px
  height: $width - 10px; // 90px
  margin: $width / 2; // 50px
  font-size: $width * 0.16; // 16px
}
```

#### 除法注意事项

使用 `/` 作为除法时，需要满足以下条件之一：
- 值或值的一部分存储在变量中
- 值被括号包围
- 值是另一个数学表达式的一部分

```scss
// 正确
$width: 100px;
.container {
  width: $width / 2; // 50px
  margin: (20px / 2); // 10px
  padding: 10px + 5px / 2; // 12.5px
}

// 错误（会被当作 CSS 分隔符）
.container {
  width: 20px / 2; // 20px / 2（不会计算）
}
```

### 字符串运算符

#### 连接字符串

使用 `+` 连接字符串：

```scss
$prefix: 'button';
$suffix: 'primary';

.#{$prefix}-#{$suffix} {
  // .button-primary
}
```

或直接拼接：

```scss
$font-family: 'Arial' + ', sans-serif';
// 'Arial, sans-serif'
```

### 比较运算符

#### 相等性

```scss
@if $value == 10 {
  // 等于
}

@if $value != 10 {
  // 不等于
}
```

#### 比较

```scss
@if $width > 100px {
  // 大于
}

@if $width < 100px {
  // 小于
}

@if $width >= 100px {
  // 大于等于
}

@if $width <= 100px {
  // 小于等于
}
```

### 逻辑运算符

#### and, or, not

```scss
@if $width > 100px and $height > 200px {
  // 两个条件都满足
}

@if $width > 100px or $height > 200px {
  // 至少一个条件满足
}

@if not $disabled {
  // 非
}
```

### 颜色运算符

#### 颜色运算

```scss
$primary: #409EFF;

.button {
  background-color: $primary + #111; // 颜色相加
  border-color: $primary - #111; // 颜色相减
}
```

### 实际应用示例

#### 响应式计算

```scss
$container-width: 1200px;
$columns: 12;
$gutter: 20px;

@function column-width($span) {
  @return ($container-width - ($gutter * ($columns - 1))) / $columns * $span + ($gutter * ($span - 1));
}

.col-6 {
  width: column-width(6);
}
```

#### 间距计算

```scss
$base-spacing: 8px;

.spacing-xs { margin: $base-spacing; } // 8px
.spacing-sm { margin: $base-spacing * 2; } // 16px
.spacing-md { margin: $base-spacing * 3; } // 24px
.spacing-lg { margin: $base-spacing * 4; } // 32px
```

#### 条件样式

```scss
$theme: 'dark';

.container {
  @if $theme == 'dark' {
    background-color: #333;
    color: #fff;
  } @else {
    background-color: #fff;
    color: #333;
  }
}
```

### 运算符优先级

Sass 遵循标准的数学运算符优先级：

1. `()` - 括号
2. `*`, `/`, `%` - 乘、除、取模
3. `+`, `-` - 加、减
4. `<`, `>`, `<=`, `>=` - 比较
5. `==`, `!=` - 相等性
6. `and` - 逻辑与
7. `or` - 逻辑或
8. `not` - 逻辑非

```scss
$result: 10 + 5 * 2; // 20（不是 30）
$result: (10 + 5) * 2; // 30
```

### 最佳实践

1. **使用括号**：明确运算优先级
2. **注意除法**：确保除法运算正确执行
3. **类型一致**：确保运算数类型匹配
4. **可读性**：复杂表达式使用函数封装
5. **单位处理**：注意单位在运算中的行为
