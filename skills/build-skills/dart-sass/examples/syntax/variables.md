# Variables

**官方文档**: https://sass-lang.com/documentation/


## 变量

Sass 变量用于存储值，可以在整个样式表中重复使用。

### 基本语法

#### 声明变量

使用 `$` 符号声明变量：

```scss
$primary-color: #409EFF;
$font-size: 16px;
$font-family: 'Arial', sans-serif;
```

#### 使用变量

```scss
.button {
  background-color: $primary-color;
  font-size: $font-size;
  font-family: $font-family;
}
```

编译后：

```css
.button {
  background-color: #409EFF;
  font-size: 16px;
  font-family: 'Arial', sans-serif;
}
```

### 变量作用域

#### 全局变量

在文件顶层声明的变量是全局的：

```scss
$global-color: #333;

.container {
  color: $global-color;
}
```

#### 局部变量

在规则块内声明的变量是局部的：

```scss
$global-color: #333;

.container {
  $local-color: #666; // 局部变量
  color: $local-color;
}

.other {
  // $local-color 在这里不可用
  color: $global-color;
}
```

#### 变量覆盖

局部变量可以覆盖全局变量：

```scss
$color: red;

.button {
  $color: blue; // 覆盖全局变量
  color: $color; // blue
}

.link {
  color: $color; // red（全局变量）
}
```

### 默认值

使用 `!default` 设置默认值：

```scss
$primary-color: #409EFF !default;

.button {
  background-color: $primary-color;
}
```

如果变量已定义，使用已定义的值；如果未定义，使用默认值。

#### 覆盖默认值

```scss
// 在导入前定义，会覆盖默认值
$primary-color: #67C23A;

@import 'variables';
```

### 变量类型

#### 数字

```scss
$width: 100px;
$height: 200px;
$opacity: 0.5;
```

#### 字符串

```scss
$font-family: 'Arial', sans-serif;
$url: 'https://example.com/image.png';
```

#### 颜色

```scss
$primary: #409EFF;
$secondary: rgb(64, 158, 255);
$tertiary: rgba(64, 158, 255, 0.5);
```

#### 布尔值

```scss
$enabled: true;
$disabled: false;
```

#### 空值

```scss
$value: null;
```

#### 列表

```scss
$spacing: 10px 20px 30px;
$colors: red, blue, green;
```

#### 映射

```scss
$breakpoints: (
  'small': 480px,
  'medium': 768px,
  'large': 1024px
);
```

### 字符串插值

使用 `#{}` 在字符串中插入变量：

```scss
$name: 'button';
$side: 'top';

.#{$name}-#{$side} {
  padding-#{$side}: 10px;
}
```

编译后：

```css
.button-top {
  padding-top: 10px;
}
```

### 变量命名

#### 命名约定

```scss
// kebab-case（推荐）
$primary-color: #409EFF;
$font-size-base: 16px;

// 或 camelCase
$primaryColor: #409EFF;
$fontSizeBase: 16px;
```

#### 命名空间

使用前缀组织变量：

```scss
// 颜色
$color-primary: #409EFF;
$color-secondary: #67C23A;
$color-danger: #F56C6C;

// 字体
$font-size-base: 16px;
$font-size-lg: 18px;
$font-size-sm: 14px;

// 间距
$spacing-xs: 4px;
$spacing-sm: 8px;
$spacing-md: 16px;
```

### 变量文件

#### 创建变量文件

`_variables.scss`:

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

#### 使用变量文件

```scss
@use 'variables' as vars;

.button {
  background-color: vars.$primary-color;
  font-size: vars.$font-size-base;
}
```

### 最佳实践

1. **使用有意义的名称**：变量名应该清晰表达用途
2. **组织变量文件**：将相关变量放在单独文件中
3. **使用命名空间**：避免变量名冲突
4. **设置默认值**：使用 `!default` 提供回退值
5. **避免深层嵌套**：保持变量结构简单
