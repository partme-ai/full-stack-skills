---
name: jimeng-prompt-text2video
description: Provides comprehensive guidance for crafting text-to-video prompts for 即梦 (Dreamina/Jimeng) Seedance 2.0 video generation. Video prompts require two additional dimensions beyond image prompts: explicit motion description and camera movement direction. Use when the user wants to write, refine, or optimize a video generation prompt; mentions "文生视频", "text2video", "视频提示词", "运镜", "camera movement", "生成一段...的视频", "帮我写个视频"; describes a scene they want as a video; or provides a rough scene description to be turned into a polished video prompt. This skill covers 12 video scenario categories with 35 annotated examples, a motion and camera word library, and a complete camera movement reference covering 7 basic plus 6 advanced compound techniques with emotional effect mappings. Always use this skill when the user needs help writing any video generation prompt for 即梦 Seedance 2.0.
license: Complete terms in LICENSE.txt
---

# jimeng-prompt-text2video — 即梦文生视频提示词

Craft production-ready text-to-video prompts for 即梦 Dreamina Seedance 2.0 models.

## When to use this skill

Use this skill when the user:
- Asks you to write a video generation prompt ("帮我写个视频提示词")
- Describes a scene they want as a moving image / video
- Wants to refine or optimize an existing video prompt
- Mentions keywords like: 文生视频, text2video, 视频生成, 视频提示词, 运镜, camera movement, Seedance
- Asks about how to describe motion, camera work, or temporal progression in a prompt

Do NOT use this skill for:
- Executing CLI commands to generate videos → use jimeng-cli-text2video
- Writing image-to-video prompts → use jimeng-prompt-image2video
- Writing text-to-image prompts → use jimeng-prompt-text2image

## Core Methodology

The video prompt formula extends the image formula with two critical dimensions: **motion** and **camera**:

```
[主体描述] + [动作/运动] + [场景环境] + [运镜方式] + [光影氛围] + [时长/节奏] + [风格/画质]
```

The key difference from text-to-image prompting:
- **Motion is mandatory**: a video without motion is just a still image. The action description is the soul of the prompt
- **Camera adds storytelling**: how the camera moves determines the viewer's emotional experience
- **Duration shapes pacing**: a 5-second clip needs different action density than a 10-second clip

## How to use this skill

### Step 1: Identify the video scenario category

| Category | Key Signals | Example File |
|----------|-------------|--------------|
| 人物/人像 | 人物, 肖像, 表情, 动作, 日常 | `examples/portrait-people.md` |
| 自然风景 | 山水, 瀑布, 海浪, 云雾, 极光, 沙漠 | `examples/nature-landscape.md` |
| 动物/野生动物 | 动物, 鸟类, 奔跑, 飞翔, 游动 | `examples/animal-wildlife.md` |
| 城市/人文 | 街景, 市场, 地铁, 夜景, 延时 | `examples/urban-city.md` |
| 美食/烹饪 | 美食, 烹饪, 咖啡, 甜点, 食材 | `examples/food-culinary.md` |
| 时尚/T台 | 走秀, 穿搭, 模特, 时装 | `examples/fashion-runway.md` |
| 运动/动作 | 跑步, 篮球, 冲浪, 滑板, 极限 | `examples/sports-action.md` |
| 舞蹈/表演 | 舞蹈, 芭蕾, 街舞, 舞台, 音乐会 | `examples/dance-performance.md` |
| 电影感/叙事 | 剧情, 人物互动, 情感, 故事 | `examples/cinematic-narrative.md` |
| 抽象/创意 | 水墨, 粒子, 光效, 色彩流动 | `examples/abstract-creative.md` |
| 商业/广告 | 产品展示, 品牌, 广告片 | `examples/commercial-ad.md` |
| 延时/慢动作 | 延时摄影, 慢动作, 高速摄影 | `examples/timelapse-slowmo.md` |

### Step 2: Load reference materials

**Always load `references/word-library.md`** for motion verbs, scene vocabulary, and style modifiers.

**Load `references/camera-library.md`** when the prompt needs camera movement — the single most important vocabulary for video prompting.

**For color descriptions**, cross-reference the text2image skill's color references (`color-library.md` for precise hues, `gugong-384-colors.md` for seasonal/poetic Chinese colors). These are comprehensive color libraries not duplicated here.

**Load the matched example file** from `examples/` for category-specific patterns.

### Step 3: Build the prompt component by component

1. **Subject** (主体): What/who is the main focus? Be specific
2. **Action/Motion** (动作/运动): **THE critical video component**. Describe what moves, how, at what speed. Use motion vocabulary from `word-library.md`. Be explicit — "缓缓转身，长发随风飘动" not "动了一下"
3. **Scene** (场景): Where + when. Provides context for the motion
4. **Camera Movement** (运镜): How the camera moves. Use `camera-library.md`. Pick 1-2 movements max. Most common pattern: one primary movement + one subtle secondary
5. **Lighting/Atmosphere** (光影氛围): In video, describe how light changes — flickering, shifting, dimming
6. **Duration/Pacing** (时长/节奏): How long + how fast. Seedance 2.0 supports 4-15 seconds. Match action density to duration
7. **Style/Quality** (风格/画质): Video-specific quality terms like "电影级画质""高帧率流畅""4K视频"

### Step 4: Apply video-specific writing rules

1. **Motion first, scene second** — place action description before or immediately after the subject
2. **One primary movement** — complex multi-subject interactions + camera work tend to fail
3. **Chinese camera terms > English** — "镜头缓缓推进" > "dolly in slowly"
4. **Match action to duration** — 5s = one clear action; 10s = action with development; 15s = multi-stage progression
5. **Describe how light changes** — unlike images, video light can evolve: "夕阳逐渐西沉""烛光摇曳闪烁"

### Step 5: Validate against checklist

Run through the [Validation Checklist](#validation-checklist). Every item must pass before presenting the prompt to the user.

### Step 6: Present the result

Always present: complete prompt in code block + model variant + suggested duration + camera explanation + optional variations.

## Video-Specific Writing Rules

### Rule 1: Motion is mandatory and explicit

- ✗ "一个女孩在森林里" → ✓ "一个女孩在森林里缓缓行走，裙摆随步伐摆动，阳光透过树叶在她身上流动"

### Rule 2: Camera movement tells the story

- **Push in (推)**: focus, intensity, revelation
- **Pull out (拉)**: context, isolation, ending
- **Pan (摇)**: exploration, connection, following
- **Track (移)**: immersion, journey, discovery

### Rule 3: One clear action per clip

Seedance 2.0 works best with a single clear action. For 15s clips, 2-3 stage progression OK but keep each stage simple.

### Rule 4: Duration determines action complexity

| Duration | Action Complexity |
|----------|------------------|
| 4-6s | One clear action ("转身微笑") |
| 7-10s | Action with development ("从远处走来→经过镜头→渐行渐远") |
| 11-15s | 2-3 stage progression ("推门→环顾→走向窗边") |

### Rule 5: Light can (and should) change

"夕阳缓缓沉入海平面""烛光在微风中摇曳""霓虹灯渐次亮起"

### Rule 6: Camera in the latter half

Subject + action + scene → camera work → atmosphere → style

## Validation Checklist

- [ ] Motion is explicit and specific (concrete action verb, not "有动作")
- [ ] Camera movement clearly described (1-2 movements, Chinese terms)
- [ ] Action complexity matches suggested duration
- [ ] Only one primary subject performing one primary action
- [ ] Light/atmosphere includes temporal change where appropriate
- [ ] Model variant + duration recommendation included

## Gotchas

1. **Action must be explicit** — 即梦 cannot infer motion from static description. "一个人在街上" = static shot
2. **Complex interactions fail** — multi-person interactions + camera movement = distortion risk
3. **Chinese camera terms work better** — "镜头缓缓推近" > "dolly in slowly"
4. **Seedance quality/speed tradeoff** — seedance2.0 = highest quality/slowest; fast = faster/lower quality
5. **Duration-to-action matching** — 5s with 3-stage action = rushed. Match complexity to time
6. **First-time web authorization** — some models require browser auth before first use
7. **Character consistency not guaranteed** — same face across segments not reliable
8. **Camera + complex motion = risk** — prioritize one over the other

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `references/word-library.md` | Motion verbs, scene vocabulary, video-specific terms | When building any video prompt |
| `references/camera-library.md` | Complete camera movement reference: 7 basics + advanced + emotional effects | When the prompt needs camera work |
| `examples/portrait-people.md` | 人物/人像视频 | People, portraits, daily life |
| `examples/nature-landscape.md` | 自然风景视频 | Nature, landscapes, weather |
| `examples/animal-wildlife.md` | 动物视频 | Animals, wildlife, birds, marine |
| `examples/urban-city.md` | 城市/人文视频 | City scenes, street life, timelapse |
| `examples/food-culinary.md` | 美食/烹饪视频 | Food, cooking, culinary |
| `examples/fashion-runway.md` | 时尚/T台视频 | Fashion, runway, models |
| `examples/sports-action.md` | 运动/动作视频 | Sports, action, extreme |
| `examples/dance-performance.md` | 舞蹈/表演视频 | Dance, stage, performance |
| `examples/cinematic-narrative.md` | 电影感/叙事视频 | Storytelling, emotional narrative |
| `examples/abstract-creative.md` | 抽象/创意视频 | Creative, experimental, artistic |
| `examples/commercial-ad.md` | 商业/广告视频 | Product demos, brand videos, ads |
| `examples/timelapse-slowmo.md` | 延时/慢动作视频 | Timelapse, slow motion, high speed |
