# Label（标签）使用指南

## 官方文档

参考官方文档：https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Instructions

Label 用于在游戏中显示文本。Cocos2d-x 支持多种标签类型：TTF、BMFont、CharMap。

### Syntax

#### Label 类型

- `Label::createWithTTF()` - 使用 TTF 字体文件
- `Label::createWithBMFont()` - 使用 BMFont 位图字体
- `Label::createWithCharMap()` - 使用字符映射
- `Label::createWithSystemFont()` - 使用系统字体

#### Label 属性

- `setString()` - 设置文本内容
- `setFontSize()` - 设置字体大小
- `setTextColor()` - 设置文本颜色
- `setAlignment()` - 设置对齐方式
- `setDimensions()` - 设置文本区域大小

### Example (TTF 标签)

```cpp
// 使用 TTF 字体文件创建标签
auto label = Label::createWithTTF("Hello Cocos2d-x", "fonts/Marker Felt.ttf", 24);
label->setPosition(Vec2(400, 300));
label->setColor(Color3B::WHITE);
this->addChild(label);
```

### Example (系统字体标签)

```cpp
// 使用系统字体创建标签
auto label = Label::createWithSystemFont("Hello World", "Arial", 24);
label->setPosition(Vec2(400, 300));
this->addChild(label);
```

### Example (BMFont 标签)

```cpp
// 使用 BMFont 位图字体创建标签
auto label = Label::createWithBMFont("fonts/bitmap-font.fnt", "Hello");
label->setPosition(Vec2(400, 300));
this->addChild(label);
```

### Example (标签属性设置)

```cpp
auto label = Label::createWithTTF("Hello World", "fonts/Marker Felt.ttf", 24);

// 设置文本
label->setString("New Text");

// 设置字体大小
label->setFontSize(32);

// 设置文本颜色
label->setTextColor(Color4B::RED);
label->setColor(Color3B::GREEN);

// 设置对齐方式
label->setAlignment(TextHAlignment::CENTER, TextVAlignment::CENTER);

// 设置文本区域（自动换行）
label->setDimensions(200, 100);
label->enableWrap(true);

// 设置行间距
label->setLineSpacing(10);

// 设置透明度
label->setOpacity(200);
```

### Example (多行文本)

```cpp
auto label = Label::createWithTTF(
    "This is a long text that will wrap to multiple lines",
    "fonts/Marker Felt.ttf",
    20
);

// 设置文本区域大小（自动换行）
label->setDimensions(300, 0); // 宽度 300，高度自动
label->enableWrap(true);
label->setAlignment(TextHAlignment::LEFT, TextVAlignment::TOP);

label->setPosition(Vec2(400, 300));
this->addChild(label);
```

### Example (标签效果)

```cpp
auto label = Label::createWithTTF("Hello", "fonts/Marker Felt.ttf", 48);

// 描边效果
label->enableOutline(Color4B::BLACK, 2);

// 阴影效果
label->enableShadow(Color4B::GRAY, Size(2, -2), 0);

// 发光效果
label->enableGlow(Color4B::YELLOW);

label->setPosition(Vec2(400, 300));
this->addChild(label);
```

### Example (动态更新文本)

```cpp
class ScoreLabel : public Label
{
public:
    CREATE_FUNC(ScoreLabel);
    virtual bool init() override;
    
    void updateScore(int score);
    
private:
    int _score;
};

bool ScoreLabel::init()
{
    if (!Label::initWithTTF("Score: 0", "fonts/Marker Felt.ttf", 24))
    {
        return false;
    }
    
    _score = 0;
    this->setPosition(Vec2(100, 500));
    this->setColor(Color3B::WHITE);
    
    return true;
}

void ScoreLabel::updateScore(int score)
{
    _score += score;
    std::string text = StringUtils::format("Score: %d", _score);
    this->setString(text);
}
```

### Example (富文本标签)

```cpp
// 创建富文本标签
auto richText = RichText::create();
richText->setContentSize(Size(400, 100));

// 添加普通文本
auto text1 = RichElementText::create(1, Color3B::WHITE, 255, "Hello ", "fonts/Marker Felt.ttf", 24);
richText->pushBackElement(text1);

// 添加彩色文本
auto text2 = RichElementText::create(2, Color3B::RED, 255, "Cocos2d-x", "fonts/Marker Felt.ttf", 24);
richText->pushBackElement(text2);

// 添加图片
auto image = RichElementImage::create(3, Color3B::WHITE, 255, "icon.png");
richText->pushBackElement(image);

richText->setPosition(Vec2(400, 300));
this->addChild(richText);
```

## Reference

- **官方文档**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **Sprite 指南**: `examples/core/sprite.md`
