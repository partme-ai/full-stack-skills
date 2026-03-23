# Nesting

**官方文档**: https://sass-lang.com/documentation/


## 嵌套

Sass 允许嵌套 CSS 选择器，使代码更清晰、更有组织。

### 基本嵌套

#### 选择器嵌套

```scss
.nav {
  background-color: #fff;
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    display: inline-block;
  }
  
  a {
    text-decoration: none;
    color: #333;
    
    &:hover {
      color: #409EFF;
    }
  }
}
```

编译后：

```css
.nav {
  background-color: #fff;
}

.nav ul {
  list-style: none;
  padding: 0;
}

.nav li {
  display: inline-block;
}

.nav a {
  text-decoration: none;
  color: #333;
}

.nav a:hover {
  color: #409EFF;
}
```

### 父选择器引用

使用 `&` 引用父选择器：

```scss
.button {
  background-color: #409EFF;
  
  &:hover {
    background-color: #337ecc;
  }
  
  &:active {
    background-color: #2b6cb0;
  }
  
  &.disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}
```

编译后：

```css
.button {
  background-color: #409EFF;
}

.button:hover {
  background-color: #337ecc;
}

.button:active {
  background-color: #2b6cb0;
}

.button.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### 属性嵌套

可以嵌套具有相同前缀的属性：

```scss
.button {
  border: {
    width: 1px;
    style: solid;
    color: #409EFF;
  }
  
  font: {
    family: Arial;
    size: 16px;
    weight: bold;
  }
  
  margin: {
    top: 10px;
    bottom: 10px;
    left: 20px;
    right: 20px;
  }
}
```

编译后：

```css
.button {
  border-width: 1px;
  border-style: solid;
  border-color: #409EFF;
  font-family: Arial;
  font-size: 16px;
  font-weight: bold;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 20px;
  margin-right: 20px;
}
```

### 深层嵌套

可以嵌套多层，但建议不超过 3-4 层：

```scss
.card {
  padding: 20px;
  
  .card-header {
    margin-bottom: 10px;
    
    .card-title {
      font-size: 18px;
      
      .card-icon {
        margin-right: 8px;
      }
    }
  }
}
```

### BEM 命名嵌套

使用 `&` 实现 BEM 命名：

```scss
.block {
  padding: 20px;
  
  &__element {
    color: #333;
    
    &--modifier {
      color: #409EFF;
    }
  }
}
```

编译后：

```css
.block {
  padding: 20px;
}

.block__element {
  color: #333;
}

.block__element--modifier {
  color: #409EFF;
}
```

### 组合选择器

```scss
.button {
  color: #333;
  
  .icon + & {
    margin-left: 10px;
  }
  
  p & {
    display: block;
  }
}
```

编译后：

```css
.button {
  color: #333;
}

.icon + .button {
  margin-left: 10px;
}

p .button {
  display: block;
}
```

### 嵌套规则

#### @media 嵌套

```scss
.container {
  width: 100%;
  
  @media (min-width: 768px) {
    width: 750px;
    margin: 0 auto;
  }
  
  @media (min-width: 1024px) {
    width: 970px;
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

@media (min-width: 1024px) {
  .container {
    width: 970px;
  }
}
```

#### @keyframes 嵌套

```scss
.button {
  animation: fadeIn 0.3s;
  
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
}
```

### 避免过度嵌套

#### 不好的做法（过度嵌套）

```scss
// 太深了！
.page {
  .container {
    .content {
      .article {
        .title {
          .icon {
            color: #333;
          }
        }
      }
    }
  }
}
```

#### 好的做法（适度嵌套）

```scss
.page-container {
  .content-article {
    .title-icon {
      color: #333;
    }
  }
}
```

### 最佳实践

1. **限制嵌套深度**：建议不超过 3-4 层
2. **使用有意义的类名**：避免过度依赖嵌套
3. **利用 & 符号**：简化伪类和修饰符
4. **属性嵌套**：用于有前缀的属性（border, font, margin 等）
5. **保持可读性**：嵌套应该提高可读性，而不是降低
