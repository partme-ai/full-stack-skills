# Animation（动画）系统使用指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Instructions

Animation 系统用于创建帧动画。通过 SpriteFrame 序列创建 Animation，然后使用 Animate 动作播放。

### Syntax

#### 动画创建流程

1. 加载 SpriteFrame 到缓存
2. 创建 SpriteFrame 序列
3. 使用序列创建 Animation
4. 使用 Animate 创建动作
5. 在 Sprite 上运行动作

#### 关键类

- `SpriteFrameCache` - 精灵帧缓存
- `SpriteFrame` - 单个精灵帧
- `Animation` - 动画对象
- `Animate` - 动画动作

### Example (基本帧动画)

```cpp
// 加载精灵帧到缓存
auto cache = SpriteFrameCache::getInstance();
cache->addSpriteFramesWithFile("player.plist", "player.png");

// 创建精灵帧序列
Vector<SpriteFrame*> frames;
for (int i = 1; i <= 4; i++)
{
    std::string frameName = StringUtils::format("player_walk_%02d.png", i);
    auto frame = cache->getSpriteFrameByName(frameName);
    if (frame)
    {
        frames.pushBack(frame);
    }
}

// 创建动画（每帧 0.1 秒）
auto animation = Animation::createWithSpriteFrames(frames, 0.1f);

// 创建动画动作
auto animate = Animate::create(animation);

// 无限循环播放
auto repeat = RepeatForever::create(animate);

// 在精灵上运行动作
auto sprite = Sprite::createWithSpriteFrameName("player_walk_01.png");
sprite->runAction(repeat);
this->addChild(sprite);
```

### Example (动画控制)

```cpp
// 创建动画
auto animation = Animation::createWithSpriteFrames(frames, 0.1f);
auto animate = Animate::create(animation);

// 播放一次
sprite->runAction(animate);

// 播放指定次数
auto repeat = Repeat::create(animate, 3);
sprite->runAction(repeat);

// 无限循环
auto repeatForever = RepeatForever::create(animate);
sprite->runAction(repeatForever);

// 停止动画
sprite->stopAllActions();
```

### Example (多个动画)

```cpp
class Player : public Sprite
{
public:
    CREATE_FUNC(Player);
    virtual bool init() override;
    
    void playIdleAnimation();
    void playWalkAnimation();
    void playJumpAnimation();
    
private:
    Animation* _idleAnimation;
    Animation* _walkAnimation;
    Animation* _jumpAnimation;
    Animate* _currentAnimate;
};

bool Player::init()
{
    if (!Sprite::init())
    {
        return false;
    }
    
    auto cache = SpriteFrameCache::getInstance();
    cache->addSpriteFramesWithFile("player.plist", "player.png");
    
    // 创建待机动画
    Vector<SpriteFrame*> idleFrames;
    for (int i = 1; i <= 2; i++)
    {
        auto frame = cache->getSpriteFrameByName(
            StringUtils::format("player_idle_%02d.png", i));
        idleFrames.pushBack(frame);
    }
    _idleAnimation = Animation::createWithSpriteFrames(idleFrames, 0.2f);
    _idleAnimation->setRestoreOriginalFrame(true);
    
    // 创建行走动画
    Vector<SpriteFrame*> walkFrames;
    for (int i = 1; i <= 4; i++)
    {
        auto frame = cache->getSpriteFrameByName(
            StringUtils::format("player_walk_%02d.png", i));
        walkFrames.pushBack(frame);
    }
    _walkAnimation = Animation::createWithSpriteFrames(walkFrames, 0.1f);
    
    // 创建跳跃动画
    Vector<SpriteFrame*> jumpFrames;
    for (int i = 1; i <= 3; i++)
    {
        auto frame = cache->getSpriteFrameByName(
            StringUtils::format("player_jump_%02d.png", i));
        jumpFrames.pushBack(frame);
    }
    _jumpAnimation = Animation::createWithSpriteFrames(jumpFrames, 0.15f);
    _jumpAnimation->setRestoreOriginalFrame(true);
    
    // 默认播放待机动画
    playIdleAnimation();
    
    return true;
}

void Player::playIdleAnimation()
{
    this->stopAllActions();
    _currentAnimate = Animate::create(_idleAnimation);
    auto repeat = RepeatForever::create(_currentAnimate);
    this->runAction(repeat);
}

void Player::playWalkAnimation()
{
    this->stopAllActions();
    _currentAnimate = Animate::create(_walkAnimation);
    auto repeat = RepeatForever::create(_currentAnimate);
    this->runAction(repeat);
}

void Player::playJumpAnimation()
{
    this->stopAllActions();
    _currentAnimate = Animate::create(_jumpAnimation);
    this->runAction(_currentAnimate);
    
    // 跳跃动画结束后恢复待机
    auto callback = CallFunc::create([this]() {
        this->playIdleAnimation();
    });
    auto sequence = Sequence::create(_currentAnimate, callback, nullptr);
    this->runAction(sequence);
}
```

### Example (动画回调)

```cpp
// 创建动画
auto animation = Animation::createWithSpriteFrames(frames, 0.1f);
auto animate = Animate::create(animation);

// 动画完成回调
auto callback = CallFunc::create([sprite]() {
    log("Animation finished");
    sprite->setColor(Color3B::RED);
});

auto sequence = Sequence::create(animate, callback, nullptr);
sprite->runAction(sequence);
```

### Example (动画延迟)

```cpp
// 创建动画
auto animation = Animation::createWithSpriteFrames(frames, 0.1f);

// 设置动画延迟（每帧之间的延迟）
animation->setDelayPerUnit(0.1f);

// 设置总延迟
animation->setDelayUnits(0.5f);

auto animate = Animate::create(animation);
sprite->runAction(animate);
```

## Reference

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Sprite 指南**: `examples/core/sprite.md`
- **Action 指南**: `examples/core/action.md`
