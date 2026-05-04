---
name: jimeng-prompt-text2image
description: Provides comprehensive guidance for crafting text-to-image prompts for 即梦 (Dreamina/Jimeng) AI image generation. Use when the user wants to write, refine, or optimize an image generation prompt; mentions "提示词", "文生图", "text2image", "文字成图", "AI绘画", "AI生图", "prompt", "帮我写一个...的画面", "生成一张...的图片", "写一个...的提示词"; describes an image they want to create; or provides a rough image description to be turned into a polished production-ready prompt. This skill covers 35 scenario categories with 115+ annotated examples, a comprehensive word library spanning 60+ thematic subcategories, and complete color references including 159 Chinese traditional colors, the 384-color Forbidden City palette, and international standards (Pantone, RAL). Always use this skill when the user needs help writing, refining, or translating any image prompt for 即梦.
license: Complete terms in LICENSE.txt
---

# jimeng-prompt-text2image — 即梦文生图提示词

Craft production-ready text-to-image prompts for 即梦 (Jimeng/Dreamina) models.

## When to use this skill

Use this skill when the user:
- Asks you to write an image generation prompt ("帮我写个提示词")
- Describes an image they want and needs it turned into a proper prompt
- Wants to refine, optimize, or translate an existing prompt
- Mentions keywords like: 提示词, 文生图, text2image, AI绘画, AI生图, prompt, 文字成图
- Asks about how to describe a specific visual scene, style, or effect

Do NOT use this skill for:
- Executing CLI commands to generate images → use jimeng-cli-text2image
- Writing video prompts → use jimeng-prompt-text2video
- Image-to-image editing prompts → use jimeng-prompt-image2image

## Core Methodology

The prompt formula is a reasoning framework — not a rigid template. Apply it flexibly:

```
[主体/人物] + [场景/背景] + [动作/姿态] + [风格/艺术类型] + [光线/色彩] + [构图/视角] + [画质/细节]
```

Each component is optional. Select and weight components based on the scenario:
- **Portrait**: emphasize subject, expression, clothing, lighting, composition
- **Landscape**: emphasize environment, time/weather, color palette, atmosphere
- **Product**: emphasize object details, material, background, lighting setup
- **Abstract/Artistic**: emphasize style, color scheme, texture, mood

## How to use this skill

### Step 1: Identify the scenario category

From the user's request, determine the primary category:

| Category | Key Signals | Example File |
|----------|-------------|--------------|
| 人像摄影 | 人物, 肖像, 表情, 自拍, 写真, 证件照 | `examples/portrait.md` |
| 时尚/服装 | 穿搭, 时装, 走秀, 配饰, 珠宝, 包包, 鞋 | `examples/fashion.md` |
| 婚礼/庆典 | 婚礼, 婚纱, 婚庆, 求婚, 纪念日, 派对 | `examples/wedding.md` |
| 儿童/亲子 | 儿童, 宝宝, 亲子, 孕妇, 家庭, 童年 | `examples/children.md` |
| 宠物 | 猫, 狗, 猫狗品种, 萌宠, 宠物日常, 异宠 | `examples/pet.md` |
| 野生动物 | 猛兽, 鸟类, 海洋生物, 昆虫, 两栖, 生态 | `examples/animal.md` |
| 植物/花卉 | 花卉, 绿植, 多肉, 盆景, 园艺, 森林, 微距植物 | `examples/botanical.md` |
| 风景/自然 | 山水, 草原, 沙漠, 雪山, 海洋, 峡谷, 极光 | `examples/landscape.md` |
| 城市/街拍 | 街拍, 都市, 建筑, 纪实, 夜城, 老城 | `examples/street.md` |
| 夜景/暗光 | 夜景, 霓虹, 星空, 烟花, 灯光, 长曝光 | `examples/night.md` |
| 航拍/空中 | 航拍, 鸟瞰, 无人机, 高空, 云端 | `examples/aerial.md` |
| 水下/海洋 | 水下, 潜水, 海洋, 珊瑚, 沉船, 深海 | `examples/underwater.md` |
| 旅行/探险 | 旅行, 探险, 背包客, 公路旅行, 极地, 徒步 | `examples/travel.md` |
| 建筑/室内 | 建筑, 室内设计, 教堂, 极简, 侘寂, 装修 | `examples/architecture.md` |
| 国风/传统 | 汉服, 水墨, 敦煌, 古风, 禅意, 工笔, 戏曲 | `examples/guofeng.md` |
| 二次元/动漫 | 动漫, 二次元, 赛璐珞, 新海诚, 吉卜力, 漫画 | `examples/anime.md` |
| 游戏/电竞 | 游戏, 电竞, 3A大作, 像素, 角色, 装备, 对战 | `examples/game.md` |
| 奇幻/魔幻 | 魔法, 龙, 精灵, 异世界, 城堡, 神话, 剑与魔法 | `examples/fantasy.md` |
| 科幻/未来 | 科幻, 太空, 外星, 机器人, AI, 赛博朋克, 废土 | `examples/scifi.md` |
| 蒸汽朋克 | 蒸汽朋克, 齿轮, 维多利亚, 飞艇, 铜管, 机械 | `examples/steampunk.md` |
| 超现实主义 | 超现实, 梦境, 达利, 马格利特, 荒诞, 错位 | `examples/surreal.md` |
| 极简主义 | 极简, 负空间, 纯色, 几何, 少即是多 | `examples/minimalism.md` |
| 怀旧/复古 | 怀旧, 复古, 胶片, 老照片, 80年代, 民国, 昭和 | `examples/vintage.md` |
| 电影感/氛围 | 电影感, 情绪, 故事感, 王家卫, 雨夜, 文艺 | `examples/cinematic.md` |
| 音乐/舞蹈 | 音乐, 乐器, 舞蹈, 芭蕾, 演唱会, 街舞, 戏曲 | `examples/music-dance.md` |
| 运动/健身 | 运动, 健身, 篮球, 足球, 跑步, 瑜伽, 极限运动 | `examples/sport.md` |
| 交通工具 | 汽车, 摩托车, 飞机, 游艇, 自行车, 火车, 超跑 | `examples/vehicle.md` |
| 美食/饮品 | 美食, 菜品, 甜点, 咖啡, 调酒, 烘焙, 摆盘 | `examples/food-product.md` |
| 科技/数码 | 科技, 数码, 手机, 电脑, 芯片, AI硬件, 3D打印 | `examples/tech.md` |
| 医学/健康 | 医学, 解剖, 手术, 中药, 心理健康, 健身解剖 | `examples/medical.md` |
| 教育/校园 | 学校, 教室, 图书馆, 毕业, 学习, 科学实验 | `examples/education.md` |
| 节日/节庆 | 春节, 中秋, 圣诞, 万圣, 元旦, 国庆, 元宵 | `examples/festival.md` |
| 微距/特写 | 微距, 特写, 昆虫, 水珠, 纹理, 花粉, 雪花 | `examples/macro.md` |
| 抽象/概念 | 抽象, 概念艺术, 几何, 数据可视化, 情感视觉化 | `examples/abstract.md` |
| 商业/营销 | 广告, 海报, 电商, banner, 品牌, 促销, 包装 | `examples/commercial.md` |

If the user's request spans multiple categories, pick the dominant one and borrow elements from others as needed. If no category matches, use the general methodology below — the prompt formula works universally.

### Step 2: Load reference materials

**Always load `references/word-library.md`** when the prompt needs any descriptive vocabulary — it covers 20+ thematic categories (人物·服饰·材质·动作·场景·天气·情绪等).

**Load color references on demand:**
- Need a precise color name for any prompt component? → Load `references/color-library.md` (159 Chinese traditional colors + international standards)
- Need poetic seasonal colors with cultural depth? → Load `references/gugong-384-colors.md` (24 solar terms × 384 colors with poetry context)
- Default rule: when the user's request mentions ANY specific color, or when the scene has a strong seasonal/time/atmosphere element, load at least one color reference

**Load the matched example file** from `examples/` to understand:
- Common scenario patterns within that category
- Category-specific vocabulary and techniques
- Annotated examples showing the methodology applied

### Step 3: Build the prompt component by component

For each component of the formula, select vocabulary from the loaded reference files as needed:

1. **Subject**: What/who is the main focus? Dive into `word-library.md` → 人物面部/体型/发型/表情/妆容/年龄/身份. Be specific — "穿墨绿色丝绸旗袍的古典女性" not "一个女人". When describing skin tone, hair color, or clothing color, reach for precise color names from the color references
2. **Scene**: Where is this happening? What time, season, weather? Use `word-library.md` → 场景/环境/天气/时间/地域. If the scene has a strong seasonal feel (spring cherry blossoms, autumn leaves, winter snow), load `gugong-384-colors.md` to find the matching solar-term color palette
3. **Action/Pose**: What is the subject doing? Static or dynamic? Use `word-library.md` → 动作/姿态/互动
4. **Style**: What artistic or photographic style? Use `word-library.md` → 风格/艺术运动/摄影技法. This strongly influences the output
5. **Lighting/Color**: What light sources and color palette? **This is where color references become essential**. Use `color-library.md` for precise hues or `gugong-384-colors.md` for seasonal atmospheric palettes. Also use `word-library.md` → 光线/色彩方案
6. **Composition**: What angle, framing, depth of field? Use `word-library.md` → 构图/视角/镜头
7. **Quality**: Resolution and detail descriptors appropriate to the model version. Use `word-library.md` → 画质/材质/肌理

Not every component is needed for every prompt. Use judgment — a minimalist abstract piece may only need subject + style + color. But when color matters, **always consult the color references**; a precisely named color ("胭脂 #9d2933") always outperforms a generic one ("暗红色").

### Step 4: Apply the writing rules

Follow all rules in the [Writing Rules](#writing-rules) section. The most critical:
- Be specific, not generic
- Use positive descriptions (即梦 ignores negations)
- Match prompt length to model version
- Order components by importance

### Step 5: Validate against the checklist

Before presenting the prompt, run through the [Validation Checklist](#validation-checklist).

### Step 6: Present the result

Always present the prompt with:
1. The complete prompt in a code block
2. A brief explanation of key component choices (why this style, why this lighting)
3. Suggested model version and aspect ratio
4. Optional: 1-2 variations with different style/lighting choices

## Writing Rules

### Rule 1: Be specific, not generic

Replace vague adjectives with concrete, visual details:
- ✗ "好看的夕阳" → ✓ "夕阳透过梧桐树叶洒下斑驳光影，天空从橙渐变到深紫"
- ✗ "美丽的风景" → ✓ "晨雾中的梯田，水面如镜反射朝霞，远山层叠如黛"

### Rule 2: Use positive descriptions

即梦 cannot process negations ("不要红色", "no red"). Always describe what you WANT:
- ✗ "不要现代建筑" → ✓ "传统木质结构建筑，青砖灰瓦"
- ✗ "no people in the scene" → ✓ "空旷无人的街道，静谧安详"

### Rule 3: Order by importance

Place the most important visual elements first. The model weights earlier tokens more heavily:
- Portrait: subject → clothing → expression → scene → lighting → style → quality
- Landscape: environment → time/weather → color → style → composition → quality
- Product: object → material/texture → placement → background → lighting → style → quality

### Rule 4: Match length to model version

- **3.0-4.0**: Prefer concise prompts (40-80 characters). These models work better with focused, essential descriptions
- **4.5+**: Can handle longer prompts (100+ characters) with rich detail. Use the full formula
- When uncertain about the model version, provide both a concise and a detailed version

### Rule 5: Choose aspect ratio for the content

- **1:1** — product shots, profile pictures, square compositions
- **3:4 or 9:16** — full-body portraits, fashion, vertical scenes
- **16:9 or 21:9** — landscapes, cinematic scenes, wide compositions
- **4:3** — general purpose, balanced compositions

### Rule 6: Anchor the style

Style keywords in the latter half of the prompt strongly influence the output aesthetic. Place the primary style descriptor just before quality words:
```
[detailed subject + scene description] + [摄影风格/艺术风格] + [画质词]
```

## Validation Checklist

Before presenting the final prompt, verify:

- [ ] Every component uses specific, concrete descriptions (not vague adjectives)
- [ ] No negative phrasing — all descriptions are positive
- [ ] Components are ordered by importance for the scenario type
- [ ] Style keyword is placed in the latter half of the prompt
- [ ] Prompt length is appropriate (concise for 3.0-4.0, can be detailed for 4.5+)
- [ ] Aspect ratio recommendation matches the content type
- [ ] Model version recommendation is included
- [ ] Chinese text is used throughout (即梦's primary language)

## Gotchas

1. **即梦 ignores negations** — "不要红色" is interpreted as "红色". Always rewrite as positive descriptions
2. **Character consistency is limited** — 即梦 cannot reliably maintain the same face across multiple generations. Avoid promising identical characters
3. **Text rendering is unreliable** — 即梦 struggles with generating readable Chinese or English text in images. If the user needs text in the image, warn them about this limitation
4. **Model version matters** — 3.0 excels with simple, concise prompts; 4.5+ handles complex multi-element prompts. When the user doesn't specify a version, default to 4.5+ style but note the alternative
5. **Aspect ratio drives composition** — a prompt written for 16:9 will compose differently than the same prompt at 9:16. Always confirm the intended aspect ratio
6. **Style keywords can dominate** — strong style keywords (cyberpunk, 水墨, Pixar) can override other elements. Place them carefully in the prompt order
7. **Prompt language** — 即梦 works best with Chinese prompts. If the user provides English, translate and adapt rather than directly using it

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `references/word-library.md` | Categorized vocabulary for all prompt components | When building prompts and need specific descriptive terms |
| `references/color-library.md` | Color reference: 159 Chinese traditional colors by family + international standards (Pantone, RAL, Morandi) | When the prompt needs precise color names or international color standards |
| `references/gugong-384-colors.md` | 《故宫里的色彩美学》384 色：24 节气 × 72 物候 × 起承转合 + 诗词典故 | When the prompt needs poetic seasonal colors, classical Chinese aesthetics, or culturally rich color names |
| `examples/portrait.md` | 人像摄影 | Portraits, headshots, character images |
| `examples/fashion.md` | 时尚/服装/配饰 | Fashion, runway, jewelry, accessories |
| `examples/wedding.md` | 婚礼/庆典 | Wedding, engagement, ceremony, celebration |
| `examples/children.md` | 儿童/亲子 | Babies, kids, family, pregnancy |
| `examples/pet.md` | 宠物（猫狗品种等） | Cats, dogs, pets by breed |
| `examples/animal.md` | 野生动物 | Wildlife, birds, marine life, insects |
| `examples/botanical.md` | 植物/花卉 | Flowers, plants, gardening, forest |
| `examples/landscape.md` | 风景/自然 | Nature, mountains, desert, ocean, aurora |
| `examples/street.md` | 城市/街拍 | Street photography, urban, documentary |
| `examples/night.md` | 夜景/暗光 | Night scenes, neon, fireworks, long exposure |
| `examples/aerial.md` | 航拍/空中 | Aerial, drone, bird's eye view |
| `examples/underwater.md` | 水下/海洋 | Underwater, diving, coral, deep sea |
| `examples/travel.md` | 旅行/探险 | Travel, adventure, road trip, expedition |
| `examples/architecture.md` | 建筑/室内 | Buildings, interiors, spaces, design |
| `examples/guofeng.md` | 国风/传统文化 | Chinese traditional aesthetics, hanfu, ink |
| `examples/anime.md` | 二次元/动漫 | Anime, manga, cel shading, cartoon |
| `examples/game.md` | 游戏/电竞 | Video games, esports, pixel art, RPG |
| `examples/fantasy.md` | 奇幻/魔幻 | Fantasy, magic, dragons, elves, mythology |
| `examples/scifi.md` | 科幻/未来 | Sci-fi, space, alien, robot, cyberpunk |
| `examples/steampunk.md` | 蒸汽朋克 | Steampunk, gears, Victorian, airship |
| `examples/surreal.md` | 超现实主义 | Surreal, dream, Dali, Magritte, absurd |
| `examples/minimalism.md` | 极简主义 | Minimalist, negative space, geometric |
| `examples/vintage.md` | 怀旧/复古 | Vintage, retro, film, old photo, nostalgia |
| `examples/cinematic.md` | 电影感/氛围 | Cinematic, mood, storytelling, atmosphere |
| `examples/music-dance.md` | 音乐/舞蹈 | Music, instrument, dance, ballet, concert |
| `examples/sport.md` | 运动/健身 | Sports, fitness, basketball, yoga, extreme |
| `examples/vehicle.md` | 交通工具 | Cars, motorcycle, aircraft, yacht, train |
| `examples/food-product.md` | 美食/饮品 | Food, drink, dessert, culinary, plating |
| `examples/tech.md` | 科技/数码 | Tech, gadgets, phone, computer, chip |
| `examples/medical.md` | 医学/健康 | Medical, anatomy, surgery, health |
| `examples/education.md` | 教育/校园 | School, campus, library, graduation |
| `examples/festival.md` | 节日/节庆 | Spring Festival, Christmas, Halloween |
| `examples/macro.md` | 微距/特写 | Macro, close-up, insect, water droplet, texture |
| `examples/abstract.md` | 抽象/概念艺术 | Abstract, conceptual, geometric art |
| `examples/commercial.md` | 商业/营销 | Ads, posters, e-commerce, branding, packaging |
