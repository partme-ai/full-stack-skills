# Modules

**官方文档**: https://sass-lang.com/documentation/


## 模块系统

Sass 的模块系统使用 `@use` 和 `@forward` 来组织和共享代码。

### @use 基础

#### 加载模块

```scss
// _variables.scss
$primary-color: #409EFF;
$font-size: 16px;

// main.scss
@use 'variables';

.button {
  background-color: variables.$primary-color;
  font-size: variables.$font-size;
}
```

#### 命名空间

默认使用文件名作为命名空间：

```scss
@use 'variables'; // 命名空间: variables
@use 'mixins'; // 命名空间: mixins

.button {
  @include mixins.button-style;
  color: variables.$primary-color;
}
```

#### 自定义命名空间

```scss
@use 'variables' as vars;
@use 'mixins' as m;

.button {
  @include m.button-style;
  color: vars.$primary-color;
}
```

#### 不使用命名空间

```scss
@use 'variables' as *;

.button {
  color: $primary-color; // 直接使用，无需前缀
}
```

### @forward

#### 转发模块

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
  color: index.$primary;
}
```

#### 控制可见性

```scss
// 只转发指定的成员
@forward 'library' show $primary, button;

// 隐藏指定的成员
@forward 'library' hide $private;
```

#### 添加前缀

```scss
@forward 'library' as lib-*;

// 使用时
@use 'index';
.button {
  @include index.lib-button;
  color: index.lib-$primary;
}
```

### 模块配置

#### 配置变量

```scss
// _library.scss
$primary-color: #409EFF !default;
$font-size: 16px !default;

// main.scss
@use 'library' with (
  $primary-color: #67C23A,
  $font-size: 18px
);
```

### 实际应用

#### 项目结构

```
styles/
  ├── _variables.scss
  ├── _mixins.scss
  ├── _functions.scss
  ├── _base.scss
  ├── _components.scss
  └── main.scss
```

#### 模块文件示例

`_variables.scss`:

```scss
$primary-color: #409EFF;
$secondary-color: #67C23A;
$font-size-base: 16px;
```

`_mixins.scss`:

```scss
@use 'variables' as vars;

@mixin button {
  background-color: vars.$primary-color;
  font-size: vars.$font-size-base;
}
```

`main.scss`:

```scss
@use 'variables' as vars;
@use 'mixins' as m;
@use 'base';
@use 'components';

.button {
  @include m.button;
}
```

### 最佳实践

1. **使用 @use 替代 @import**：@import 已弃用
2. **组织模块**：按功能组织模块文件
3. **使用命名空间**：避免命名冲突
4. **使用 @forward**：创建模块库
5. **配置变量**：使用 !default 和 with
