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

### Step 1: Identify scenario category
→ Load `rules/category-table.md` to match user's request to the right category and example file

### Step 2: Load reference materials

**Load the relevant vocabulary files from `word-library/` based on what you need — never load the whole library:**

| 你需要的 | 加载文件 |
|----------|----------|
| 人物/面部/体型/发型/表情/妆容/服装/配饰 | `word-library/subject.md` |
| 场景/环境/天气/时间/季节/地域 | `word-library/scene.md` |
| 摄影/绘画/设计/数字/民族风格 | `word-library/style.md` |
| 材质/肌理（金属/木材/石材/织物/玻璃） | `word-library/material.md` |
| 动作/姿态/动态/手势 | `word-library/motion.md` |
| 道具/器物/乐器/武器/科技/食物 | `word-library/props.md` |
| 光线/光影/光效/照明 | `word-library/lighting.md` |
| 构图/视角/景深/镜头 | `word-library/composition.md` |
| 画质/质感/通感词 | `word-library/quality.md` |
| 氛围/情绪/意境 | `word-library/atmosphere.md` |
| 抽象/概念/视觉隐喻 | `word-library/abstract.md` |
| 自然元素（花卉/树木/动物） | `word-library/nature.md` |

**Load color references — choose by what the user says:**

| 用户提到 | 加载文件 |
|----------|----------|
| 中国色、传统色、胭脂、桃红、月白、黛色、中国红、故宫色、国风配色 | `color-library/chinese-traditional.md` |
| Pantone、潘通、流行色、年度色、国际流行 | `color-library/pantone.md` |
| RAL、劳尔色卡、工业色、国际标准色 | `color-library/ral.md` |
| 莫兰迪、配色方案、色彩搭配、电影色调、高级灰、低饱和 | `color-library/modern-schemes.md` |
| 用户提到具体颜色但没说体系 | 从最相关的文件加载 |

**Load model-version-specific references:**

| 版本 | 关键词 | 官方 Model ID | 加载文件 |
|------|--------|--------------|----------|
| **2.1** | 2.1 | — | `references/jimeng-2.1-prompt-guide.md` |
| **3.0** | 3.0 | — | `references/3.0/vocabulary-core.md` + `references/jimeng-3.0-prompt-guide.md` + `references/jimeng-3.0-word-library.md`。如需风格→额外 `references/3.0/vocabulary-styles.md`；如需材质→额外 `references/3.0/vocabulary-materials.md` |
| **3.1** | 3.1 | — | `references/jimeng-3.1-prompt-guide.md` |
| **4.0** | 4.0 | `doubao-seedream-4-0-250828` | `references/jimeng-4.0-prompt-guide.md` |
| **4.1** | 4.1 | — | `references/jimeng-4.1-prompt-guide.md` |
| **4.5** | 4.5 | `doubao-seedream-4-5-251128` | `references/jimeng-4.5-prompt-guide.md` |
| **5.0** | 5.0, Seedream, 联网 | `doubao-seedream-5-0-260128` (also `doubao-seedream-5-0-lite-260128`) | `references/seedream-5.0-prompt-guide.md` |
| **未指定** | — | — | 默认 `references/jimeng-3.0-vocabulary.md` |

### Step 3: Build the prompt
→ Load `rules/core-methodology.md` for component-by-component guidance

### Step 4: Apply writing rules
→ Load `rules/writing-rules.md` for all 10 writing rules

### Step 5: Validate
→ Load `rules/validation-checklist.md` and run through all checks

## Gotchas

1. **即梦 ignores negations** — "不要红色" is interpreted as "红色". Always rewrite as positive descriptions
2. **Character consistency is limited** — 即梦 cannot reliably maintain the same face across multiple generations. Avoid promising identical characters
3. **Aspect ratio drives composition** — a prompt written for 16:9 will compose differently than the same prompt at 9:16. Always confirm the intended aspect ratio
4. **Style keywords can dominate** — strong style keywords (cyberpunk, 水墨, Pixar) can override other elements. Place them carefully in the prompt order
5. **Prompt language** — 即梦 works best with Chinese prompts. If the user provides English, translate and adapt rather than directly using it
6. **⚠️ Never write hex color values into prompts** — The model treats `#ff2121`, `#9d2933` etc. as literal text to render in the image, NOT as color instructions. Always use Chinese color names only: "大红", "胭脂", "桃红" — never "大红 #ff2121" or any form with hex codes
7. **Color library is for YOUR reference only** — Load `color-library/chinese-traditional.md` to FIND the right color name to write into the prompt. Do NOT copy hex codes into the output prompt text

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `rules/category-table.md` | 35 scenario categories + example mapping | Step 1 |
| `rules/core-methodology.md` | Component-by-component build guide + presentation | Step 3 |
| `rules/writing-rules.md` | 9 prompt writing rules | Step 4 |
| `rules/validation-checklist.md` | 8-point pre-submission checklist | Step 5 |
| `word-library/*.md` | 12 thematic vocabulary files | Based on prompt component needed |
| `color-library/chinese-traditional.md` | 中国色9大色系159色 | User mentions 中国色/传统色/胭脂 |
| `color-library/pantone.md` | Pantone常用色系 | User mentions Pantone/潘通 |
| `color-library/ral.md` | RAL Classic+RAL Design | User mentions RAL/劳尔 |
| `color-library/modern-schemes.md` | 莫兰迪+配色方案+电影色调 | User mentions 莫兰迪/配色 |
| `references/gugong-384-colors.md` | 384 colors × 24 solar terms | Poetic/seasonal colors |
| `references/jimeng-*.md` | Version-specific guides | Based on user's model version |
| `references/3.0/*.md` | 3.0 core/styles/materials | When using 3.0 model |
| `examples/*.md` | 35 scenario-specific examples | After identifying category |