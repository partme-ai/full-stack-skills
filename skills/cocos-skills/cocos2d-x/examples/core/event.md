# Event（事件）系统使用指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Instructions

Cocos2d-x 使用事件分发器（EventDispatcher）来处理各种事件。事件系统支持触摸、鼠标、键盘、自定义事件等。

### Syntax

#### 事件监听器类型

- `EventListenerTouchOneByOne` - 单点触摸事件
- `EventListenerTouchAllAtOnce` - 多点触摸事件
- `EventListenerMouse` - 鼠标事件
- `EventListenerKeyboard` - 键盘事件
- `EventListenerCustom` - 自定义事件

#### 事件注册

- `_eventDispatcher->addEventListenerWithSceneGraphPriority()` - 使用场景图优先级
- `_eventDispatcher->addEventListenerWithFixedPriority()` - 使用固定优先级
- `_eventDispatcher->removeEventListener()` - 移除事件监听器

### Example (自定义事件)

```cpp
// 定义自定义事件名称
const std::string EVENT_PLAYER_DIED = "player_died";
const std::string EVENT_SCORE_UPDATED = "score_updated";

// 创建自定义事件监听器
auto listener = EventListenerCustom::create(EVENT_PLAYER_DIED, [](EventCustom* event) {
    log("Player died event received");
    // 处理玩家死亡事件
});

// 注册监听器
_eventDispatcher->addEventListenerWithSceneGraphPriority(listener, this);

// 发送自定义事件
EventCustom event(EVENT_PLAYER_DIED);
_eventDispatcher->dispatchEvent(&event);
```

### Example (事件优先级)

```cpp
// 场景图优先级（推荐）
auto listener1 = EventListenerTouchOneByOne::create();
listener1->onTouchBegan = [](Touch* touch, Event* event) { return true; };
_eventDispatcher->addEventListenerWithSceneGraphPriority(listener1, node1);

// 固定优先级
auto listener2 = EventListenerTouchOneByOne::create();
listener2->onTouchBegan = [](Touch* touch, Event* event) { return true; };
_eventDispatcher->addEventListenerWithFixedPriority(listener2, 100);
```

### Example (事件冒泡)

```cpp
// 设置事件是否冒泡
auto listener = EventListenerTouchOneByOne::create();
listener->setSwallowTouches(true); // 阻止事件继续传播
listener->onTouchBegan = [](Touch* touch, Event* event) {
    return true; // 返回 true 表示处理此事件
};
```

### Example (完整事件处理示例)

```cpp
class GameLayer : public Layer
{
public:
    CREATE_FUNC(GameLayer);
    virtual bool init() override;
    
private:
    void setupEventListeners();
    void onPlayerDied(EventCustom* event);
    void onScoreUpdated(EventCustom* event);
};

bool GameLayer::init()
{
    if (!Layer::init())
    {
        return false;
    }
    
    setupEventListeners();
    return true;
}

void GameLayer::setupEventListeners()
{
    // 玩家死亡事件
    auto playerDiedListener = EventListenerCustom::create(
        "player_died",
        CC_CALLBACK_1(GameLayer::onPlayerDied, this)
    );
    _eventDispatcher->addEventListenerWithSceneGraphPriority(playerDiedListener, this);
    
    // 分数更新事件
    auto scoreListener = EventListenerCustom::create(
        "score_updated",
        CC_CALLBACK_1(GameLayer::onScoreUpdated, this)
    );
    _eventDispatcher->addEventListenerWithSceneGraphPriority(scoreListener, this);
}

void GameLayer::onPlayerDied(EventCustom* event)
{
    log("Player died!");
    // 处理玩家死亡逻辑
}

void GameLayer::onScoreUpdated(EventCustom* event)
{
    int* score = static_cast<int*>(event->getUserData());
    log("Score updated: %d", *score);
    // 更新 UI
}
```

## Reference

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Input 指南**: `examples/core/input.md`
