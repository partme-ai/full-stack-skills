# 安装和配置指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## 概述

本指南介绍如何在不同平台上安装和配置 Cocos2d-x v4 开发环境。

## 系统要求

### Windows
- Windows 7 或更高版本
- Visual Studio 2015 或更高版本（推荐 Visual Studio 2019）
- CMake 3.10 或更高版本
- Python 3.x

### macOS
- macOS 10.13 或更高版本
- Xcode 10 或更高版本
- CMake 3.10 或更高版本
- Python 3.x

### Linux
- Ubuntu 18.04 或更高版本（或其他现代 Linux 发行版）
- GCC 7 或更高版本
- CMake 3.10 或更高版本
- Python 3.x

## 安装步骤

### 1. 安装 CMake

#### Windows
```bash
# 下载并安装 CMake
# https://cmake.org/download/
# 或使用 Chocolatey
choco install cmake
```

#### macOS
```bash
# 使用 Homebrew
brew install cmake
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install cmake

# 或使用 snap
sudo snap install cmake --classic
```

### 2. 安装 Python

确保已安装 Python 3.x：

```bash
python3 --version
```

### 3. 获取 Cocos2d-x

```bash
# 克隆仓库
git clone https://github.com/cocos2d/cocos2d-x.git
cd cocos2d-x

# 或下载 ZIP 文件
# https://github.com/cocos2d/cocos2d-x/releases
```

### 4. 运行安装脚本

```bash
# 运行 setup.py
python setup.py

# 这会设置环境变量和创建 cocos 命令
```

### 5. 验证安装

```bash
# 检查 cocos 命令
cocos --version

# 应该显示版本信息
```

## 创建新项目

### 使用 cocos 命令

```bash
# 创建新项目
cocos new MyGame -p com.yourcompany.mygame -l cpp -d /path/to/projects

# 参数说明：
# -p: 包名（Package name）
# -l: 语言（cpp, lua, js）
# -d: 项目目录
```

### 使用 CMake

```bash
# 进入项目目录
cd MyGame

# 创建构建目录
mkdir build
cd build

# 生成构建文件
cmake ..

# 编译
cmake --build .
```

## 平台特定配置

### Windows (Visual Studio)

```bash
# 生成 Visual Studio 解决方案
cmake .. -G "Visual Studio 16 2019" -A x64

# 打开 MyGame.sln 进行开发
```

### macOS (Xcode)

```bash
# 生成 Xcode 项目
cmake .. -G Xcode

# 打开 MyGame.xcodeproj 进行开发
```

### Linux

```bash
# 使用默认生成器（Makefile）
cmake ..

# 编译
make -j4
```

### Android

```bash
# 需要 Android SDK 和 NDK
# 设置环境变量
export ANDROID_NDK_ROOT=/path/to/android-ndk
export ANDROID_SDK_ROOT=/path/to/android-sdk

# 生成 Android 项目
cmake .. -DCMAKE_TOOLCHAIN_FILE=../platform/android/android.toolchain.cmake
```

## 依赖管理

### 使用 Cocos2d-x 内置依赖

Cocos2d-x v4 使用 CMake 管理依赖，大部分依赖已包含在仓库中。

### 添加第三方库

```cmake
# 在 CMakeLists.txt 中添加
find_package(SomeLibrary REQUIRED)
target_link_libraries(MyGame SomeLibrary)
```

## 常见问题

### CMake 找不到

确保 CMake 已添加到系统 PATH 环境变量中。

### Python 版本问题

确保使用 Python 3.x，不是 Python 2.x。

### 编译错误

- 检查编译器版本是否符合要求
- 确保所有依赖已正确安装
- 查看 CMake 输出信息

## 参考资源

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **快速开始**: `examples/getting-started/quick-start.md`
- **构建系统**: `examples/tools/build-system.md`
