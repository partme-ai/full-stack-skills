# 快速上手 - 创建第一个项目

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## 概述

本指南将帮助你创建第一个 Cocos2d-x v4 项目。

## 前置要求

- CMake 3.10 或更高版本
- C++ 编译器（Visual Studio, Xcode, GCC）
- Python 3.x（用于构建脚本）

## 创建项目

### 1. 克隆或下载 Cocos2d-x

```bash
git clone https://github.com/cocos2d/cocos2d-x.git
cd cocos2d-x
```

### 2. 创建新项目

```bash
python setup.py
# 或使用 cocos 命令
cocos new MyGame -p com.yourcompany.mygame -l cpp -d /path/to/projects
```

### 3. 构建项目

```bash
cd MyGame
mkdir build
cd build
cmake ..
cmake --build .
```

## 第一个场景示例

```cpp
#include "cocos2d.h"

USING_NS_CC;

class HelloWorld : public Scene
{
public:
    static Scene* createScene();
    virtual bool init();
    CREATE_FUNC(HelloWorld);
};

Scene* HelloWorld::createScene()
{
    return HelloWorld::create();
}

bool HelloWorld::init()
{
    if (!Scene::init())
    {
        return false;
    }
    
    auto visibleSize = Director::getInstance()->getVisibleSize();
    Vec2 origin = Director::getInstance()->getVisibleOrigin();
    
    // 创建一个标签
    auto label = Label::createWithTTF("Hello Cocos2d-x", "fonts/Marker Felt.ttf", 24);
    label->setPosition(Vec2(origin.x + visibleSize.width/2,
                            origin.y + visibleSize.height - label->getContentSize().height));
    this->addChild(label, 1);
    
    // 创建一个精灵
    auto sprite = Sprite::create("HelloWorld.png");
    if (sprite != nullptr)
    {
        sprite->setPosition(Vec2(visibleSize.width/2 + origin.x, visibleSize.height/2 + origin.y));
        this->addChild(sprite, 0);
    }
    
    return true;
}
```

## 运行项目

### Windows
```bash
# 在 Visual Studio 中打开解决方案
# 或使用命令行
.\MyGame.exe
```

### macOS
```bash
open MyGame.app
```

### Linux
```bash
./MyGame
```

## 基本概念

### Node（节点）
- 所有显示对象的基础类
- 支持位置、旋转、缩放等变换
- 可以添加子节点形成树结构

### Scene（场景）
- 场景图的根节点
- 通过 Director 管理场景切换

### Sprite（精灵）
- 用于显示图片的节点
- 继承自 Node

### Director（导演）
- 管理场景切换
- 管理渲染循环
- 获取窗口信息

## 参考资源

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **安装指南**: `examples/getting-started/installation.md`
