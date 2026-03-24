# CLI API

## 命令行接口

Dart Sass 提供了丰富的命令行选项。

### 基本语法

```bash
sass [options] <input> [output]
```

### 常用选项

#### --style, -s

输出样式。

```bash
sass input.scss output.css --style compressed
```

可选值：
- `expanded` - 展开格式（默认）
- `compressed` - 压缩格式
- `compact` - 紧凑格式
- `nested` - 嵌套格式

#### --watch, -w

监听模式。

```bash
sass --watch input.scss:output.css
sass --watch src/styles:dist/css
```

#### --update

只更新已更改的文件。

```bash
sass --update src/styles:dist/css
```

#### --load-path, -I

添加加载路径。

```bash
sass input.scss output.css --load-path=node_modules
sass input.scss output.css -I node_modules -I src/styles
```

#### --source-map

生成 source map。

```bash
sass input.scss output.css --source-map
```

#### --no-source-map

禁用 source map。

```bash
sass input.scss output.css --no-source-map
```

#### --embed-source-map

嵌入 source map。

```bash
sass input.scss output.css --embed-source-map
```

#### --embed-sources

嵌入源文件。

```bash
sass input.scss output.css --embed-sources
```

#### --quiet, -q

静默模式。

```bash
sass input.scss output.css --quiet
```

#### --verbose

详细输出。

```bash
sass input.scss output.css --verbose
```

#### --poll

轮询模式（用于网络文件系统）。

```bash
sass --watch --poll input.scss:output.css
```

#### --version, -v

显示版本。

```bash
sass --version
```

#### --help, -h

显示帮助。

```bash
sass --help
```

### 使用示例

#### 开发环境

```bash
sass --watch src/scss:dist/css --style expanded
```

#### 生产构建

```bash
sass src/scss:dist/css --style compressed --no-source-map
```

#### 使用加载路径

```bash
sass input.scss output.css \
  --load-path=node_modules \
  --load-path=src/styles
```

#### 批量编译

```bash
# 编译多个目录
sass src/scss/main.scss dist/css/main.css --style compressed
sass src/scss/components:dist/css/components --style compressed
sass src/scss/utils:dist/css/utils --style compressed
```

### package.json 脚本

```json
{
  "scripts": {
    "sass": "sass src/scss:dist/css",
    "sass:watch": "sass --watch src/scss:dist/css",
    "sass:build": "sass src/scss:dist/css --style compressed --no-source-map",
    "sass:dev": "sass --watch src/scss:dist/css --style expanded"
  }
}
```

### 最佳实践

1. **开发环境**：使用 `--watch` 模式
2. **生产构建**：使用 `--style compressed --no-source-map`
3. **加载路径**：使用 `--load-path` 简化导入
4. **批量编译**：使用目录编译模式
5. **CI/CD**：使用 `--update` 提高效率
