# Texture（纹理）使用指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Instructions

Texture 用于加载和管理图片资源。Cocos2d-x 使用 TextureCache 来缓存纹理，提高性能。

### Syntax

#### 纹理加载

- 使用 `Director::getInstance()->getTextureCache()` 获取纹理缓存
- `addImage()` 方法加载并缓存纹理
- `getTextureForKey()` 获取已缓存的纹理
- `removeTexture()` 移除纹理
- `removeAllTextures()` 清除所有纹理

#### 纹理属性

- `getPixelsWide()` - 获取纹理宽度
- `getPixelsHigh()` - 获取纹理高度
- `getContentSize()` - 获取内容大小
- `getPixelFormat()` - 获取像素格式

### Example (加载纹理)

```cpp
// 获取纹理缓存
auto textureCache = Director::getInstance()->getTextureCache();

// 加载纹理（会自动缓存）
auto texture = textureCache->addImage("player.png");

// 从纹理创建精灵
auto sprite = Sprite::createWithTexture(texture);
this->addChild(sprite);
```

### Example (异步加载纹理)

```cpp
auto textureCache = Director::getInstance()->getTextureCache();

// 异步加载纹理
textureCache->addImageAsync("large_image.png", [this](Texture2D* texture) {
    if (texture)
    {
        auto sprite = Sprite::createWithTexture(texture);
        this->addChild(sprite);
        log("Texture loaded successfully");
    }
    else
    {
        log("Failed to load texture");
    }
});
```

### Example (纹理缓存管理)

```cpp
auto textureCache = Director::getInstance()->getTextureCache();

// 预加载纹理
textureCache->addImage("player.png");
textureCache->addImage("enemy.png");
textureCache->addImage("background.png");

// 获取已缓存的纹理
auto texture = textureCache->getTextureForKey("player.png");
if (texture)
{
    auto sprite = Sprite::createWithTexture(texture);
    this->addChild(sprite);
}

// 移除单个纹理
textureCache->removeTexture(texture);

// 清除所有纹理（谨慎使用）
// textureCache->removeAllTextures();
```

### Example (纹理信息)

```cpp
auto texture = Director::getInstance()->getTextureCache()->addImage("player.png");

// 获取纹理尺寸
int width = texture->getPixelsWide();
int height = texture->getPixelsHigh();
log("Texture size: %d x %d", width, height);

// 获取内容大小
Size contentSize = texture->getContentSize();
log("Content size: %.2f x %.2f", contentSize.width, contentSize.height);

// 获取像素格式
Texture2D::PixelFormat format = texture->getPixelFormat();
log("Pixel format: %d", format);
```

### Example (从纹理区域创建精灵)

```cpp
// 加载纹理
auto texture = Director::getInstance()->getTextureCache()->addImage("spritesheet.png");

// 从纹理的某个区域创建精灵（精灵表）
Rect rect(0, 0, 32, 32); // x, y, width, height
auto sprite = Sprite::createWithTexture(texture, rect);
sprite->setPosition(Vec2(400, 300));
this->addChild(sprite);
```

### Example (纹理预加载)

```cpp
class GameScene : public Scene
{
public:
    static Scene* createScene();
    virtual bool init();
    CREATE_FUNC(GameScene);
    
private:
    void preloadTextures();
    int _loadedCount;
    int _totalCount;
};

void GameScene::preloadTextures()
{
    auto textureCache = Director::getInstance()->getTextureCache();
    
    std::vector<std::string> textures = {
        "player.png",
        "enemy.png",
        "background.png",
        "bullet.png"
    };
    
    _totalCount = textures.size();
    _loadedCount = 0;
    
    for (const auto& texturePath : textures)
    {
        textureCache->addImageAsync(texturePath, [this](Texture2D* texture) {
            _loadedCount++;
            log("Loaded %d/%d textures", _loadedCount, _totalCount);
            
            if (_loadedCount == _totalCount)
            {
                log("All textures loaded!");
                // 开始游戏
            }
        });
    }
}
```

### Example (内存管理)

```cpp
// 在场景退出时清理不需要的纹理
void GameScene::onExit()
{
    Scene::onExit();
    
    // 移除游戏相关的纹理
    auto textureCache = Director::getInstance()->getTextureCache();
    textureCache->removeTextureForKey("player.png");
    textureCache->removeTextureForKey("enemy.png");
    
    // 注意：不要清除所有纹理，因为可能其他场景还在使用
}
```

## Reference

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Sprite 指南**: `examples/core/sprite.md`
- **资源管理**: `examples/core/resources.md`
