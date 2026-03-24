# Scene（场景）管理指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## 概述

Scene 是场景图的根节点，通过 Director 管理场景的切换和生命周期。

## 创建场景

### 基本场景

```cpp
class GameScene : public Scene
{
public:
    static Scene* createScene();
    virtual bool init();
    CREATE_FUNC(GameScene);
};

Scene* GameScene::createScene()
{
    return GameScene::create();
}

bool GameScene::init()
{
    if (!Scene::init())
    {
        return false;
    }
    
    // 场景初始化代码
    auto label = Label::createWithTTF("Game Scene", "fonts/Marker Felt.ttf", 24);
    label->setPosition(Vec2(400, 300));
    this->addChild(label);
    
    return true;
}
```

## 场景切换

### 直接切换

```cpp
// 切换到新场景
auto newScene = GameScene::createScene();
Director::getInstance()->replaceScene(newScene);
```

### 带过渡效果的切换

```cpp
// 淡入淡出过渡
auto transition = TransitionFade::create(1.0f, GameScene::createScene());
Director::getInstance()->replaceScene(transition);

// 翻页过渡
auto transition = TransitionPageTurn::create(1.0f, GameScene::createScene(), false);
Director::getInstance()->replaceScene(transition);

// 滑动过渡
auto transition = TransitionSlideInR::create(1.0f, GameScene::createScene());
Director::getInstance()->replaceScene(transition);
```

## 场景生命周期

```cpp
class GameScene : public Scene
{
public:
    virtual void onEnter() override;
    virtual void onEnterTransitionDidFinish() override;
    virtual void onExit() override;
    virtual void onExitTransitionDidStart() override;
};

void GameScene::onEnter()
{
    Scene::onEnter();
    log("Scene entered");
    // 场景进入时的初始化
}

void GameScene::onEnterTransitionDidFinish()
{
    Scene::onEnterTransitionDidFinish();
    log("Scene transition finished");
    // 过渡完成后的操作
}

void GameScene::onExit()
{
    Scene::onExit();
    log("Scene exiting");
    // 场景退出时的清理
}

void GameScene::onExitTransitionDidStart()
{
    Scene::onExitTransitionDidStart();
    log("Scene transition started");
    // 过渡开始时的操作
}
```

## 场景层次结构

```cpp
bool GameScene::init()
{
    if (!Scene::init())
    {
        return false;
    }
    
    // 背景层
    auto backgroundLayer = Layer::create();
    auto bgSprite = Sprite::create("background.png");
    bgSprite->setPosition(Vec2(400, 300));
    backgroundLayer->addChild(bgSprite);
    this->addChild(backgroundLayer, 0);
    
    // 游戏层
    auto gameLayer = Layer::create();
    // 添加游戏对象
    this->addChild(gameLayer, 1);
    
    // UI 层
    auto uiLayer = Layer::create();
    // 添加 UI 元素
    this->addChild(uiLayer, 2);
    
    return true;
}
```

## Director 使用

### 获取 Director 实例

```cpp
auto director = Director::getInstance();
```

### 获取窗口信息

```cpp
auto director = Director::getInstance();
auto visibleSize = director->getVisibleSize();
Vec2 origin = director->getVisibleOrigin();
Vec2 center = Vec2(visibleSize.width/2 + origin.x, 
                   visibleSize.height/2 + origin.y);
```

### 暂停和恢复

```cpp
// 暂停场景
Director::getInstance()->pause();

// 恢复场景
Director::getInstance()->resume();
```

## 完整示例

```cpp
class MenuScene : public Scene
{
public:
    static Scene* createScene();
    virtual bool init();
    CREATE_FUNC(MenuScene);
    
private:
    void onPlayButtonClicked(Ref* sender);
};

bool MenuScene::init()
{
    if (!Scene::init())
    {
        return false;
    }
    
    auto visibleSize = Director::getInstance()->getVisibleSize();
    Vec2 origin = Director::getInstance()->getVisibleOrigin();
    
    // 标题
    auto title = Label::createWithTTF("My Game", "fonts/Marker Felt.ttf", 48);
    title->setPosition(Vec2(origin.x + visibleSize.width/2,
                            origin.y + visibleSize.height - 100));
    this->addChild(title, 1);
    
    // 开始按钮
    auto playButton = MenuItemImage::create(
        "button_play.png",
        "button_play_selected.png",
        CC_CALLBACK_1(MenuScene::onPlayButtonClicked, this));
    playButton->setPosition(Vec2(origin.x + visibleSize.width/2,
                                 origin.y + visibleSize.height/2));
    
    auto menu = Menu::create(playButton, nullptr);
    menu->setPosition(Vec2::ZERO);
    this->addChild(menu, 1);
    
    return true;
}

void MenuScene::onPlayButtonClicked(Ref* sender)
{
    auto gameScene = GameScene::createScene();
    auto transition = TransitionFade::create(0.5f, gameScene);
    Director::getInstance()->replaceScene(transition);
}
```

## 参考资源

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Node 指南**: `examples/core/node-scene.md`
- **Director API**: `api/director.md`
