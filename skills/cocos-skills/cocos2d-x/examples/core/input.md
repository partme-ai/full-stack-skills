# Input（输入）处理指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## 概述

Cocos2d-x 支持触摸、鼠标和键盘输入事件。

## 触摸事件

### 单点触摸

```cpp
class TouchLayer : public Layer
{
public:
    CREATE_FUNC(TouchLayer);
    virtual bool init() override;
    
private:
    bool onTouchBegan(Touch* touch, Event* event);
    void onTouchMoved(Touch* touch, Event* event);
    void onTouchEnded(Touch* touch, Event* event);
    void onTouchCancelled(Touch* touch, Event* event);
};

bool TouchLayer::init()
{
    if (!Layer::init())
    {
        return false;
    }
    
    // 创建触摸监听器
    auto listener = EventListenerTouchOneByOne::create();
    listener->setSwallowTouches(true);
    
    // 绑定回调函数
    listener->onTouchBegan = CC_CALLBACK_2(TouchLayer::onTouchBegan, this);
    listener->onTouchMoved = CC_CALLBACK_2(TouchLayer::onTouchMoved, this);
    listener->onTouchEnded = CC_CALLBACK_2(TouchLayer::onTouchEnded, this);
    listener->onTouchCancelled = CC_CALLBACK_2(TouchLayer::onTouchCancelled, this);
    
    // 注册监听器
    _eventDispatcher->addEventListenerWithSceneGraphPriority(listener, this);
    
    return true;
}

bool TouchLayer::onTouchBegan(Touch* touch, Event* event)
{
    Vec2 location = touch->getLocation();
    log("Touch began at: (%.2f, %.2f)", location.x, location.y);
    return true; // 返回 true 表示要接收后续事件
}

void TouchLayer::onTouchMoved(Touch* touch, Event* event)
{
    Vec2 location = touch->getLocation();
    log("Touch moved to: (%.2f, %.2f)", location.x, location.y);
}

void TouchLayer::onTouchEnded(Touch* touch, Event* event)
{
    Vec2 location = touch->getLocation();
    log("Touch ended at: (%.2f, %.2f)", location.x, location.y);
}

void TouchLayer::onTouchCancelled(Touch* touch, Event* event)
{
    log("Touch cancelled");
}
```

### 多点触摸

```cpp
class MultiTouchLayer : public Layer
{
public:
    CREATE_FUNC(MultiTouchLayer);
    virtual bool init() override;
    
private:
    void onTouchesBegan(const std::vector<Touch*>& touches, Event* event);
    void onTouchesMoved(const std::vector<Touch*>& touches, Event* event);
    void onTouchesEnded(const std::vector<Touch*>& touches, Event* event);
};

bool MultiTouchLayer::init()
{
    if (!Layer::init())
    {
        return false;
    }
    
    auto listener = EventListenerTouchAllAtOnce::create();
    listener->onTouchesBegan = CC_CALLBACK_2(MultiTouchLayer::onTouchesBegan, this);
    listener->onTouchesMoved = CC_CALLBACK_2(MultiTouchLayer::onTouchesMoved, this);
    listener->onTouchesEnded = CC_CALLBACK_2(MultiTouchLayer::onTouchesEnded, this);
    
    _eventDispatcher->addEventListenerWithSceneGraphPriority(listener, this);
    
    return true;
}

void MultiTouchLayer::onTouchesBegan(const std::vector<Touch*>& touches, Event* event)
{
    log("Touches began: %zu touches", touches.size());
    for (auto touch : touches)
    {
        Vec2 location = touch->getLocation();
        log("  Touch at: (%.2f, %.2f)", location.x, location.y);
    }
}
```

## 鼠标事件

```cpp
class MouseLayer : public Layer
{
public:
    CREATE_FUNC(MouseLayer);
    virtual bool init() override;
    
private:
    void onMouseDown(Event* event);
    void onMouseUp(Event* event);
    void onMouseMove(Event* event);
    void onMouseScroll(Event* event);
};

bool MouseLayer::init()
{
    if (!Layer::init())
    {
        return false;
    }
    
    auto listener = EventListenerMouse::create();
    listener->onMouseDown = CC_CALLBACK_1(MouseLayer::onMouseDown, this);
    listener->onMouseUp = CC_CALLBACK_1(MouseLayer::onMouseUp, this);
    listener->onMouseMove = CC_CALLBACK_1(MouseLayer::onMouseMove, this);
    listener->onMouseScroll = CC_CALLBACK_1(MouseLayer::onMouseScroll, this);
    
    _eventDispatcher->addEventListenerWithSceneGraphPriority(listener, this);
    
    return true;
}

void MouseLayer::onMouseDown(Event* event)
{
    EventMouse* mouseEvent = static_cast<EventMouse*>(event);
    Vec2 location = mouseEvent->getLocationInView();
    log("Mouse down at: (%.2f, %.2f)", location.x, location.y);
}

void MouseLayer::onMouseScroll(Event* event)
{
    EventMouse* mouseEvent = static_cast<EventMouse*>(event);
    float scrollY = mouseEvent->getScrollY();
    log("Mouse scroll: %.2f", scrollY);
}
```

## 键盘事件

```cpp
class KeyboardLayer : public Layer
{
public:
    CREATE_FUNC(KeyboardLayer);
    virtual bool init() override;
    
private:
    void onKeyPressed(EventKeyboard::KeyCode keyCode, Event* event);
    void onKeyReleased(EventKeyboard::KeyCode keyCode, Event* event);
};

bool KeyboardLayer::init()
{
    if (!Layer::init())
    {
        return false;
    }
    
    auto listener = EventListenerKeyboard::create();
    listener->onKeyPressed = CC_CALLBACK_2(KeyboardLayer::onKeyPressed, this);
    listener->onKeyReleased = CC_CALLBACK_2(KeyboardLayer::onKeyReleased, this);
    
    _eventDispatcher->addEventListenerWithSceneGraphPriority(listener, this);
    
    return true;
}

void KeyboardLayer::onKeyPressed(EventKeyboard::KeyCode keyCode, Event* event)
{
    switch (keyCode)
    {
        case EventKeyboard::KeyCode::KEY_LEFT_ARROW:
            log("Left arrow pressed");
            break;
        case EventKeyboard::KeyCode::KEY_RIGHT_ARROW:
            log("Right arrow pressed");
            break;
        case EventKeyboard::KeyCode::KEY_SPACE:
            log("Space pressed");
            break;
        default:
            break;
    }
}
```

## 拖拽示例

```cpp
class DragLayer : public Layer
{
public:
    CREATE_FUNC(DragLayer);
    virtual bool init() override;
    
private:
    bool onTouchBegan(Touch* touch, Event* event);
    void onTouchMoved(Touch* touch, Event* event);
    void onTouchEnded(Touch* touch, Event* event);
    
    Sprite* _draggedSprite;
    bool _isDragging;
};

bool DragLayer::init()
{
    if (!Layer::init())
    {
        return false;
    }
    
    // 创建可拖拽的精灵
    _draggedSprite = Sprite::create("player.png");
    _draggedSprite->setPosition(Vec2(400, 300));
    this->addChild(_draggedSprite);
    
    _isDragging = false;
    
    auto listener = EventListenerTouchOneByOne::create();
    listener->onTouchBegan = CC_CALLBACK_2(DragLayer::onTouchBegan, this);
    listener->onTouchMoved = CC_CALLBACK_2(DragLayer::onTouchMoved, this);
    listener->onTouchEnded = CC_CALLBACK_2(DragLayer::onTouchEnded, this);
    
    _eventDispatcher->addEventListenerWithSceneGraphPriority(listener, this);
    
    return true;
}

bool DragLayer::onTouchBegan(Touch* touch, Event* event)
{
    Vec2 location = touch->getLocation();
    Rect rect = _draggedSprite->getBoundingBox();
    
    if (rect.containsPoint(location))
    {
        _isDragging = true;
        return true;
    }
    return false;
}

void DragLayer::onTouchMoved(Touch* touch, Event* event)
{
    if (_isDragging)
    {
        Vec2 location = touch->getLocation();
        _draggedSprite->setPosition(location);
    }
}

void DragLayer::onTouchEnded(Touch* touch, Event* event)
{
    _isDragging = false;
}
```

## 参考资源

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Event 系统**: `examples/core/event.md`
