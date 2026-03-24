# Sprite（精灵）使用指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Instructions

Sprite 是 Cocos2d-x 中用于显示图片的基本节点类。Sprite 继承自 Node，可以显示纹理、支持动画、变换等操作。

### Syntax

#### 创建 Sprite

- `Sprite::create("filename.png")` - 从图片文件创建
- `Sprite::createWithTexture(texture)` - 从纹理创建
- `Sprite::createWithSpriteFrame(frame)` - 从精灵帧创建
- `Sprite::createWithSpriteFrameName("frame_name")` - 从精灵帧名称创建
- `Sprite::create("filename.png", Rect(x, y, width, height))` - 从纹理区域创建

### Example (从文件创建)

```cpp
// 从图片文件创建
auto sprite = Sprite::create("player.png");
this->addChild(sprite);

// 指定位置
sprite->setPosition(Vec2(100, 100));
```

### Example (从纹理创建)

```cpp
// 从纹理创建
auto texture = Director::getInstance()->getTextureCache()->addImage("player.png");
auto sprite = Sprite::createWithTexture(texture);
this->addChild(sprite);
```

### Example (从纹理矩形创建)

```cpp
// 从纹理的某个区域创建（精灵表）
auto sprite = Sprite::create("spritesheet.png", Rect(0, 0, 32, 32));
this->addChild(sprite);
```

#### Sprite 属性

- `setPosition(Vec2)` - 设置位置
- `setRotation(float)` - 设置旋转角度
- `setScale(float)` - 设置缩放
- `setAnchorPoint(Vec2)` - 设置锚点
- `setOpacity(GLubyte)` - 设置透明度
- `setColor(Color3B)` - 设置颜色
- `setFlippedX(bool)` - 水平翻转
- `setFlippedY(bool)` - 垂直翻转

### Example (位置和变换)

```cpp
auto sprite = Sprite::create("player.png");

// 设置位置
sprite->setPosition(Vec2(400, 300));

// 设置锚点（默认 0.5, 0.5）
sprite->setAnchorPoint(Vec2(0.5f, 0.5f));

// 设置旋转
sprite->setRotation(45.0f);

// 设置缩放
sprite->setScale(2.0f);  // 统一缩放
sprite->setScaleX(1.5f); // X 轴缩放
sprite->setScaleY(0.8f); // Y 轴缩放

// 设置透明度
sprite->setOpacity(128); // 0-255

// 设置颜色
sprite->setColor(Color3B::RED);
```

### 翻转

```cpp
// 水平翻转
sprite->setFlippedX(true);

// 垂直翻转
sprite->setFlippedY(true);
```

### Example (动画 Sprite - 使用 SpriteFrame)

```cpp
// 创建 SpriteFrame 缓存
auto cache = SpriteFrameCache::getInstance();
cache->addSpriteFramesWithFile("spritesheet.plist", "spritesheet.png");

// 从 SpriteFrame 创建
auto sprite = Sprite::createWithSpriteFrameName("player_idle_01.png");
this->addChild(sprite);
```

### Example (帧动画)

```cpp
Vector<SpriteFrame*> frames;
for (int i = 1; i <= 4; i++)
{
    std::string frameName = StringUtils::format("player_walk_%02d.png", i);
    auto frame = cache->getSpriteFrameByName(frameName);
    frames.pushBack(frame);
}

auto animation = Animation::createWithSpriteFrames(frames, 0.1f);
auto animate = Animate::create(animation);
auto repeat = RepeatForever::create(animate);

sprite->runAction(repeat);
```

### Example (完整示例)

```cpp
class GameScene : public Scene
{
public:
    static Scene* createScene();
    virtual bool init();
    CREATE_FUNC(GameScene);
    
private:
    Sprite* _player;
};

bool GameScene::init()
{
    if (!Scene::init())
    {
        return false;
    }
    
    // 创建玩家精灵
    _player = Sprite::create("player.png");
    _player->setPosition(Vec2(400, 300));
    _player->setAnchorPoint(Vec2(0.5f, 0.5f));
    this->addChild(_player, 1);
    
    // 添加动画
    auto cache = SpriteFrameCache::getInstance();
    cache->addSpriteFramesWithFile("player.plist", "player.png");
    
    Vector<SpriteFrame*> frames;
    for (int i = 1; i <= 4; i++)
    {
        auto frame = cache->getSpriteFrameByName(
            StringUtils::format("player_walk_%02d.png", i));
        frames.pushBack(frame);
    }
    
    auto animation = Animation::createWithSpriteFrames(frames, 0.1f);
    auto animate = Animate::create(animation);
    auto repeat = RepeatForever::create(animate);
    _player->runAction(repeat);
    
    return true;
}
```

### Example (性能优化 - 使用 SpriteBatchNode)

```cpp
// 批量渲染相同纹理的精灵
auto batchNode = SpriteBatchNode::create("spritesheet.png", 100);
this->addChild(batchNode);

for (int i = 0; i < 50; i++)
{
    auto sprite = Sprite::createWithTexture(batchNode->getTexture(), 
                                             Rect(i * 32, 0, 32, 32));
    sprite->setPosition(Vec2(i * 50, 100));
    batchNode->addChild(sprite);
}
```

### Example (纹理缓存)

```cpp
// 预加载纹理
auto textureCache = Director::getInstance()->getTextureCache();
textureCache->addImage("player.png");
textureCache->addImage("enemy.png");

// 使用缓存的纹理
auto sprite = Sprite::create("player.png"); // 从缓存获取
```

## Reference

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Texture 指南**: `examples/core/texture.md`
- **Animation 指南**: `examples/core/animation.md`
