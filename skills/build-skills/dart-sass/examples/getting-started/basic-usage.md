# Basic Usage

**官方文档**: https://sass-lang.com/documentation/


## 基本使用

Dart Sass 可以通过命令行、JavaScript API 或 Dart API 使用。

### 命令行编译

#### 一对一模式

编译单个文件：

```bash
sass input.scss output.css
```

#### 多对多模式

编译整个目录：

```bash
sass src/styles:dist/css
```

这会将 `src/styles/` 目录下的所有 `.scss` 或 `.sass` 文件编译到 `dist/css/` 目录。

#### 监听模式

自动监听文件变化并重新编译：

```bash
sass --watch input.scss:output.css
```

或监听目录：

```bash
sass --watch src/styles:dist/css
```

### 输出样式

#### Expanded（展开，默认）

```bash
sass input.scss output.css --style expanded
```

输出格式：

```css
.button {
  background-color: #409EFF;
  color: white;
  padding: 10px 20px;
}
```

#### Compressed（压缩）

```bash
sass input.scss output.css --style compressed
```

输出格式：

```css
.button{background-color:#409EFF;color:#fff;padding:10px 20px}
```

#### Compact（紧凑）

```bash
sass input.scss output.css --style compact
```

输出格式：

```css
.button { background-color: #409EFF; color: white; padding: 10px 20px; }
```

#### Nested（嵌套）

```bash
sass input.scss output.css --style nested
```

输出格式：

```css
.button {
  background-color: #409EFF;
  color: white;
  padding: 10px 20px; }
```

### 基本示例

#### 创建 SCSS 文件

`styles.scss`:

```scss
$primary-color: #409EFF;
$font-size: 16px;

.button {
  background-color: $primary-color;
  color: white;
  font-size: $font-size;
  padding: 10px 20px;
  border-radius: 4px;
  
  &:hover {
    background-color: darken($primary-color, 10%);
  }
}
```

#### 编译

```bash
sass styles.scss styles.css
```

#### 生成的 CSS

`styles.css`:

```css
.button {
  background-color: #409EFF;
  color: white;
  font-size: 16px;
  padding: 10px 20px;
  border-radius: 4px;
}

.button:hover {
  background-color: #337ecc;
}
```

### 常用选项

#### 禁用源映射

```bash
sass input.scss output.css --no-source-map
```

#### 嵌入源映射

```bash
sass input.scss output.css --embed-source-map
```

#### 嵌入源文件

```bash
sass input.scss output.css --embed-sources
```

#### 添加加载路径

```bash
sass input.scss output.css --load-path=node_modules
```

可以多次使用：

```bash
sass input.scss output.css --load-path=src --load-path=node_modules
```

#### 静默模式

```bash
sass input.scss output.css --quiet
```

#### 仅更新已更改的文件

```bash
sass --update src/styles:dist/css
```

### 在项目中使用

#### package.json 脚本

```json
{
  "scripts": {
    "sass": "sass src/scss:dist/css",
    "sass:watch": "sass --watch src/scss:dist/css",
    "sass:build": "sass src/scss:dist/css --style compressed --no-source-map"
  }
}
```

#### 运行脚本

```bash
# 编译一次
npm run sass

# 监听模式
npm run sass:watch

# 生产构建
npm run sass:build
```

### 错误处理

#### 检查语法错误

```bash
sass input.scss output.css
```

如果有语法错误，Sass 会显示详细的错误信息：

```
Error: Invalid CSS after "$primary-color:": expected expression (e.g. 1px, bold), was "#409EFF;"
  input.scss 1:18  root stylesheet
```

#### 静默错误（不推荐）

```bash
sass input.scss output.css --quiet
```

### 最佳实践

1. **使用监听模式开发**：`sass --watch` 自动重新编译
2. **生产环境压缩**：使用 `--style compressed`
3. **开发环境启用源映射**：默认启用，便于调试
4. **组织文件结构**：使用目录编译模式管理多个文件
5. **版本控制**：只提交 `.scss` 文件，不提交 `.css` 文件
