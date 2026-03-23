# Node 和 Scene 基础

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Instructions

Node 是 Cocos2d-x 中所有显示对象的基础类，Scene 是场景图的根节点。理解 Node 和 Scene 的关系是使用 Cocos2d-x 的基础。

### Syntax

#### Node 基础

- 所有显示对象都继承自 `Node`
- Node 支持位置、旋转、缩放、锚点等变换
- Node 可以添加子节点形成树结构
- Node 有生命周期方法：`onEnter()`, `onExit()`, `onEnterTransitionDidFinish()`, `onExitTransitionDidStart()`

#### Scene 基础

- Scene 继承自 Node，是场景图的根节点
- 通过 Director 管理场景切换
- 一个应用同时只能有一个运行的 Scene

### Example (创建基本 Node)

```cpp
#include "cocos2d.h"

USING_NS_CC;

// 创建一个简单的 Node
auto node = Node::create();
node->setPosition(Vec2(400, 300));
node->setRotation(45.0f);
node->setScale(1.5f);
node->setAnchorPoint(Vec2(0.5f, 0.5f));

// 添加到场景
scene->addChild(node);
```

### Example (Node 层次结构)

```cpp
// 创建父节点
auto parent = Node::create();
parent->setPosition(Vec2(400, 300));

// 创建子节点
auto child1 = Sprite::create("sprite1.png");
child1->setPosition(Vec2(-50, 0)); // 相对于父节点
parent->addChild(child1);

auto child2 = Sprite::create("sprite2.png");
child2->setPosition(Vec2(50, 0)); // 相对于父节点
parent->addChild(child2);

// 添加到场景
scene->addChild(parent);
```

### Example (创建 Scene)

```cpp
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
    
    // 添加内容到场景
    auto label = Label::createWithTTF("Hello World", "fonts/Marker Felt.ttf", 24);
    label->setPosition(Vec2(origin.x + visibleSize.width/2,
                            origin.y + visibleSize.height - label->getContentSize().height));
    this->addChild(label, 1);
    
    return true;
}
```

### Example (Node 生命周期)

```cpp
class MyNode : public Node
{
public:
    CREATE_FUNC(MyNode);
    virtual bool init() override;
    virtual void onEnter() override;
    virtual void onEnterTransitionDidFinish() override;
    virtual void onExit() override;
    virtual void onExitTransitionDidStart() override;
};

bool MyNode::init()
{
    if (!Node::init())
    {
        return false;
    }
    log("Node initialized");
    return true;
}

void MyNode::onEnter()
{
    Node::onEnter();
    log("Node entered");
}

void MyNode::onEnterTransitionDidFinish()
{
    Node::onEnterTransitionDidFinish();
    log("Node transition finished");
}

void MyNode::onExit()
{
    Node::onExit();
    log("Node exited");
}

void MyNode::onExitTransitionDidStart()
{
    Node::onExitTransitionDidStart();
    log("Node transition started");
}
```

### Example (坐标系统)

```cpp
// Cocos2d-x 使用 OpenGL 坐标系
// 原点在左下角，Y 轴向上

auto sprite = Sprite::create("player.png");

// 设置位置（世界坐标）
sprite->setPosition(Vec2(400, 300));

// 设置锚点（0.5, 0.5 表示中心）
sprite->setAnchorPoint(Vec2(0.5f, 0.5f));

// 获取世界坐标
Vec2 worldPos = sprite->getPosition();

// 转换为节点本地坐标
Vec2 localPos = sprite->convertToNodeSpace(worldPos);

// 转换为世界坐标
Vec2 worldPos2 = sprite->convertToWorldSpace(localPos);
```

### Example (Node 变换)

```cpp
auto node = Node::create();

// 位置
node->setPosition(Vec2(400, 300));
node->setPositionX(400);
node->setPositionY(300);

// 旋转（角度）
node->setRotation(45.0f);
node->setRotationX(30.0f);
node->setRotationY(60.0f);

// 缩放
node->setScale(2.0f);        // 统一缩放
node->setScaleX(1.5f);       // X 轴缩放
node->setScaleY(0.8f);       // Y 轴缩放

// 锚点
node->setAnchorPoint(Vec2(0.5f, 0.5f)); // 中心
node->setAnchorPoint(Vec2(0.0f, 0.0f)); // 左下角
node->setAnchorPoint(Vec2(1.0f, 1.0f)); // 右上角

// 可见性
node->setVisible(true);
node->setVisible(false);

// 透明度
node->setOpacity(255); // 完全不透明
node->setOpacity(128); // 半透明
node->setOpacity(0);   // 完全透明
```

## Reference

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Scene 指南**: `examples/core/scene.md`
- **Sprite 指南**: `examples/core/sprite.md`
