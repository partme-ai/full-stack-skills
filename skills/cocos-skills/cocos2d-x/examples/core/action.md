# Action（动作）系统使用指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## 概述

Action 系统用于对节点执行各种变换操作，如移动、旋转、缩放等。

## 基本动作

### 移动动作

```cpp
auto sprite = Sprite::create("player.png");
this->addChild(sprite);

// 移动到指定位置
auto moveTo = MoveTo::create(2.0f, Vec2(400, 300));
sprite->runAction(moveTo);

// 相对移动
auto moveBy = MoveBy::create(1.0f, Vec2(100, 50));
sprite->runAction(moveBy);
```

### 旋转动作

```cpp
// 旋转到指定角度
auto rotateTo = RotateTo::create(2.0f, 90.0f);
sprite->runAction(rotateTo);

// 相对旋转
auto rotateBy = RotateBy::create(1.0f, 180.0f);
sprite->runAction(rotateBy);
```

### 缩放动作

```cpp
// 缩放到指定大小
auto scaleTo = ScaleTo::create(1.0f, 2.0f);
sprite->runAction(scaleTo);

// 相对缩放
auto scaleBy = ScaleBy::create(1.0f, 1.5f);
sprite->runAction(scaleBy);
```

### 淡入淡出

```cpp
// 淡入
auto fadeIn = FadeIn::create(1.0f);
sprite->runAction(fadeIn);

// 淡出
auto fadeOut = FadeOut::create(1.0f);
sprite->runAction(fadeOut);

// 淡入到指定透明度
auto fadeTo = FadeTo::create(1.0f, 128);
sprite->runAction(fadeTo);
```

### 跳跃动作

```cpp
// 跳跃到指定位置
auto jumpTo = JumpTo::create(2.0f, Vec2(400, 300), 100, 3);
sprite->runAction(jumpTo);

// 相对跳跃
auto jumpBy = JumpBy::create(1.0f, Vec2(100, 0), 50, 2);
sprite->runAction(jumpBy);
```

## 组合动作

### 序列动作（Sequence）

```cpp
// 按顺序执行多个动作
auto move1 = MoveBy::create(1.0f, Vec2(100, 0));
auto move2 = MoveBy::create(1.0f, Vec2(0, 100));
auto move3 = MoveBy::create(1.0f, Vec2(-100, 0));

auto sequence = Sequence::create(move1, move2, move3, nullptr);
sprite->runAction(sequence);
```

### 同时执行（Spawn）

```cpp
// 同时执行多个动作
auto move = MoveBy::create(2.0f, Vec2(200, 0));
auto rotate = RotateBy::create(2.0f, 360.0f);
auto scale = ScaleBy::create(2.0f, 1.5f);

auto spawn = Spawn::create(move, rotate, scale, nullptr);
sprite->runAction(spawn);
```

### 重复动作

```cpp
// 重复指定次数
auto move = MoveBy::create(1.0f, Vec2(100, 0));
auto repeat = Repeat::create(move, 3);
sprite->runAction(repeat);

// 无限重复
auto repeatForever = RepeatForever::create(move);
sprite->runAction(repeatForever);
```

### 延迟动作

```cpp
// 延迟执行
auto delay = DelayTime::create(2.0f);
auto move = MoveBy::create(1.0f, Vec2(100, 0));
auto sequence = Sequence::create(delay, move, nullptr);
sprite->runAction(sequence);
```

## 缓动函数

### 使用 Ease

```cpp
auto move = MoveBy::create(2.0f, Vec2(400, 0));

// 缓入
auto easeIn = EaseIn::create(move, 2.0f);
sprite->runAction(easeIn);

// 缓出
auto easeOut = EaseOut::create(move, 2.0f);
sprite->runAction(easeOut);

// 缓入缓出
auto easeInOut = EaseInOut::create(move, 2.0f);
sprite->runAction(easeInOut);

// 弹性效果
auto elastic = EaseElasticInOut::create(move, 0.5f);
sprite->runAction(elastic);

// 弹跳效果
auto bounce = EaseBounceInOut::create(move);
sprite->runAction(bounce);
```

## 回调动作

```cpp
// 动作完成后执行回调
auto move = MoveBy::create(2.0f, Vec2(400, 0));
auto callback = CallFunc::create([sprite](){
    log("Action completed!");
    sprite->setColor(Color3B::RED);
});

auto sequence = Sequence::create(move, callback, nullptr);
sprite->runAction(sequence);
```

## 完整示例

```cpp
class ActionDemo : public Scene
{
public:
    static Scene* createScene();
    virtual bool init();
    CREATE_FUNC(ActionDemo);
    
private:
    void createMovingSprite();
    void createRotatingSprite();
    void createScalingSprite();
};

bool ActionDemo::init()
{
    if (!Scene::init())
    {
        return false;
    }
    
    createMovingSprite();
    createRotatingSprite();
    createScalingSprite();
    
    return true;
}

void ActionDemo::createMovingSprite()
{
    auto sprite = Sprite::create("player.png");
    sprite->setPosition(Vec2(100, 200));
    this->addChild(sprite);
    
    // 创建来回移动的动画
    auto moveRight = MoveBy::create(2.0f, Vec2(400, 0));
    auto moveLeft = MoveBy::create(2.0f, Vec2(-400, 0));
    auto sequence = Sequence::create(moveRight, moveLeft, nullptr);
    auto repeat = RepeatForever::create(sequence);
    
    sprite->runAction(repeat);
}

void ActionDemo::createRotatingSprite()
{
    auto sprite = Sprite::create("player.png");
    sprite->setPosition(Vec2(400, 300));
    this->addChild(sprite);
    
    // 持续旋转
    auto rotate = RotateBy::create(2.0f, 360.0f);
    auto repeat = RepeatForever::create(rotate);
    sprite->runAction(repeat);
}

void ActionDemo::createScalingSprite()
{
    auto sprite = Sprite::create("player.png");
    sprite->setPosition(Vec2(700, 200));
    this->addChild(sprite);
    
    // 缩放动画
    auto scaleUp = ScaleTo::create(1.0f, 1.5f);
    auto scaleDown = ScaleTo::create(1.0f, 1.0f);
    auto sequence = Sequence::create(scaleUp, scaleDown, nullptr);
    auto repeat = RepeatForever::create(sequence);
    
    sprite->runAction(repeat);
}
```

## 动作管理

### 停止动作

```cpp
// 停止所有动作
sprite->stopAllActions();

// 停止指定动作
auto action = sprite->getActionByTag(100);
if (action)
{
    sprite->stopAction(action);
}

// 停止指定标签的动作
sprite->stopActionByTag(100);
```

### 动作标签

```cpp
auto move = MoveBy::create(2.0f, Vec2(400, 0));
move->setTag(100);
sprite->runAction(move);

// 稍后可以通过标签获取
auto action = sprite->getActionByTag(100);
```

## 参考资源

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Sprite 指南**: `examples/core/sprite.md`
- **Scene 指南**: `examples/core/scene.md`
