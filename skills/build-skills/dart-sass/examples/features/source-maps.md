# Source Maps

**官方文档**: https://sass-lang.com/documentation/


## Source Maps

Source maps 帮助在浏览器中调试 Sass 编译后的 CSS。

### 启用 Source Maps

#### 命令行

```bash
sass input.scss output.css --source-map
```

#### JavaScript API

```javascript
const sass = require('sass');

const result = sass.compile('styles.scss', {
  sourceMap: true
});
```

### 嵌入 Source Map

```bash
sass input.scss output.css --embed-source-map
```

### 嵌入源文件

```bash
sass input.scss output.css --embed-sources
```

### 禁用 Source Maps

```bash
sass input.scss output.css --no-source-map
```

### 最佳实践

1. **开发环境**：启用 source maps
2. **生产环境**：禁用 source maps
3. **调试**：使用嵌入模式便于调试
4. **性能**：生产环境禁用以提高性能
