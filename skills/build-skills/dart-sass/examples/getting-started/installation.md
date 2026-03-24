# Installation

**官方文档**: https://sass-lang.com/documentation/


## 安装 Dart Sass

Dart Sass 是 Sass 的主要实现，推荐使用。

### 方式一：npm 安装（推荐）

#### 全局安装

```bash
npm install -g sass
```

#### 本地安装（项目依赖）

```bash
npm install --save-dev sass
```

安装后可以使用 `sass` 命令：

```bash
sass input.scss output.css
```

### 方式二：Homebrew 安装（macOS/Linux）

```bash
brew install sass/sass/sass
```

### 方式三：Chocolatey 安装（Windows）

```bash
choco install sass
```

### 方式四：Scoop 安装（Windows）

```bash
scoop install sass
```

### 方式五：Standalone 二进制文件

1. 访问 [GitHub Releases](https://github.com/sass/dart-sass/releases)
2. 下载对应平台的二进制文件
3. 解压并添加到 PATH 环境变量

#### macOS/Linux

```bash
# 下载并解压
wget https://github.com/sass/dart-sass/releases/download/1.69.5/dart-sass-1.69.5-linux-x64.tar.gz
tar -xzf dart-sass-1.69.5-linux-x64.tar.gz

# 添加到 PATH（在 ~/.bashrc 或 ~/.zshrc 中添加）
export PATH="$PATH:/path/to/dart-sass"
```

#### Windows

1. 下载 `dart-sass-1.69.5-windows-x64.zip`
2. 解压到目录（如 `C:\dart-sass`）
3. 添加到系统 PATH 环境变量

### 方式六：Dart 包管理器（pub.dev）

在 Dart 项目中使用：

```yaml
# pubspec.yaml
dependencies:
  sass: ^1.69.5
```

然后运行：

```bash
dart pub get
```

### 验证安装

安装完成后，验证是否安装成功：

```bash
sass --version
```

应该显示版本号，例如：`1.69.5`

### 快速测试

创建一个测试文件 `test.scss`：

```scss
$primary-color: #409EFF;

.button {
  background-color: $primary-color;
  color: white;
  padding: 10px 20px;
}
```

编译测试：

```bash
sass test.scss test.css
```

如果成功生成 `test.css`，说明安装成功。

## 不同平台的注意事项

### macOS

- 推荐使用 Homebrew 安装
- 如果使用 npm，确保 Node.js 已安装

### Linux

- 可以使用 npm 或 standalone 二进制文件
- standalone 二进制文件不需要额外依赖

### Windows

- 推荐使用 Chocolatey 或 Scoop
- 也可以使用 npm（需要 Node.js）
- standalone 二进制文件可以直接运行

## 在项目中使用

### npm 项目

```json
{
  "devDependencies": {
    "sass": "^1.69.5"
  },
  "scripts": {
    "sass": "sass src/styles:dist/css",
    "sass:watch": "sass --watch src/styles:dist/css"
  }
}
```

### package.json 脚本

```json
{
  "scripts": {
    "build:css": "sass src/scss:dist/css --style compressed",
    "watch:css": "sass --watch src/scss:dist/css"
  }
}
```

## 常见问题

### 命令未找到

如果提示 `sass: command not found`：

1. 检查是否已添加到 PATH
2. 重新打开终端
3. 使用完整路径运行

### 权限问题

如果遇到权限问题：

```bash
# npm 全局安装可能需要 sudo（不推荐）
sudo npm install -g sass

# 或者使用 nvm 管理 Node.js 版本，避免权限问题
```

### 版本冲突

如果已安装其他 Sass 实现（如 Ruby Sass），可能需要：

```bash
# 卸载旧版本
gem uninstall sass

# 或使用完整路径
/path/to/dart-sass/sass input.scss output.css
```
