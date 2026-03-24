# Compiling Modes

**官方文档**: https://sass-lang.com/documentation/


## 编译模式

Dart Sass 支持多种编译模式，适应不同的使用场景。

### 一对一模式

编译单个文件到单个文件。

```bash
sass input.scss output.css
```

**适用场景**：
- 单个入口文件
- 简单的项目结构
- 快速测试

### 多对多模式

编译整个目录到目录。

```bash
sass src/styles:dist/css
```

**特点**：
- 自动处理目录下所有 `.scss` 和 `.sass` 文件
- 保持目录结构
- 只编译更改的文件（使用 `--update`）

**示例结构**：

```
src/styles/
  ├── main.scss
  ├── components/
  │   ├── button.scss
  │   └── card.scss
  └── utils/
      └── variables.scss
```

编译后：

```
dist/css/
  ├── main.css
  ├── components/
  │   ├── button.css
  │   └── card.css
  └── utils/
      └── variables.css
```

### 监听模式

自动监听文件变化并重新编译。

```bash
sass --watch input.scss:output.css
```

或监听目录：

```bash
sass --watch src/styles:dist/css
```

**特点**：
- 实时编译
- 自动检测文件变化
- 适合开发环境

**停止监听**：按 `Ctrl+C`

### 更新模式

只编译已更改的文件。

```bash
sass --update src/styles:dist/css
```

**特点**：
- 增量编译
- 提高编译速度
- 适合 CI/CD 环境

### 轮询模式

在某些文件系统上，使用轮询检测文件变化。

```bash
sass --watch --poll input.scss:output.css
```

**适用场景**：
- 网络文件系统
- Docker 容器
- 某些虚拟文件系统

### 批量编译示例

#### 编译多个目录

```bash
# 编译主样式
sass src/scss/main.scss dist/css/main.css

# 编译组件样式
sass src/scss/components:dist/css/components

# 编译工具样式
sass src/scss/utils:dist/css/utils
```

#### 使用脚本自动化

`compile.sh`:

```bash
#!/bin/bash

# 清理输出目录
rm -rf dist/css/*

# 编译主文件
sass src/scss/main.scss dist/css/main.css --style compressed

# 编译组件
sass src/scss/components:dist/css/components --style compressed

# 编译工具
sass src/scss/utils:dist/css/utils --style compressed

echo "Compilation complete!"
```

#### package.json 脚本

```json
{
  "scripts": {
    "sass:dev": "sass --watch src/scss:dist/css",
    "sass:build": "sass src/scss:dist/css --style compressed --no-source-map",
    "sass:update": "sass --update src/scss:dist/css"
  }
}
```

### 条件编译

#### 根据环境变量

`compile.js`:

```javascript
const sass = require('sass');
const fs = require('fs');

const isProduction = process.env.NODE_ENV === 'production';

const result = sass.compile('src/styles/main.scss', {
  style: isProduction ? 'compressed' : 'expanded',
  sourceMap: !isProduction
});

fs.writeFileSync('dist/css/main.css', result.css);
if (result.sourceMap) {
  fs.writeFileSync('dist/css/main.css.map', JSON.stringify(result.sourceMap));
}
```

### 性能优化

#### 并行编译

使用工具并行编译多个文件：

```bash
# 使用 GNU parallel
parallel sass {} {.}.css ::: src/scss/*.scss

# 或使用 npm 脚本
npm run sass:parallel
```

#### 缓存编译结果

Dart Sass 会自动缓存编译结果，但可以手动控制：

```bash
# 清除缓存（如果需要）
# Dart Sass 没有显式的缓存清除命令
# 删除输出文件即可强制重新编译
```

### 错误处理模式

#### 继续编译其他文件

即使某个文件出错，继续编译其他文件：

```bash
# Dart Sass 默认行为
sass src/styles:dist/css
```

#### 详细错误信息

```bash
# 默认显示详细错误
sass input.scss output.css
```

#### 静默模式

```bash
sass input.scss output.css --quiet
```

### 最佳实践

1. **开发环境**：使用 `--watch` 模式
2. **生产构建**：使用 `--update` 或一次性编译
3. **大型项目**：使用目录编译模式
4. **CI/CD**：使用 `--update` 提高效率
5. **网络文件系统**：使用 `--poll` 选项
