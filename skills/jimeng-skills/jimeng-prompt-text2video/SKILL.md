---
name: jimeng-prompt-text2video
description: "Provides comprehensive guidance for crafting text-to-video prompts for 即梦 (Dreamina/Jimeng) video models (视频3.0 Pro, Doubao Seedance 2.0, Seedance 1.5/1.0, 智能多帧). Video prompts require two additional dimensions beyond image prompts: explicit motion description and camera movement direction. Use when the user wants to write, refine, or optimize a video generation prompt; mentions 文生视频, text2video, 视频提示词, 运镜, camera movement, 生成一段...的视频, 帮我写个视频; describes a scene they want as a video; or provides a rough scene description to be turned into a polished video prompt. This skill covers 12 video scenario categories with 35 annotated examples, a motion and camera word library, and a complete camera movement reference covering 7 basic plus 6 advanced compound techniques with emotional effect mappings. Always use this skill when the user needs help writing any video generation prompt for 即梦."
license: Complete terms in LICENSE.txt
---

# jimeng-prompt-text2video — 即梦文生视频提示词

Craft production-ready text-to-video prompts for 即梦 Dreamina video models (视频3.0 Pro, Doubao Seedance 2.0, Seedance 1.5, Seedance 1.0, 智能多帧).

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

## Model Version Guide

即梦 has multiple video model lines. The core writing approach differs by model:

| Model | Formula | Key Difference |
|-------|---------|----------------|
| **视频3.0 / 3.0 Pro** | 主体 + 动作 + 场景 + 镜头 + 风格 + (情绪演绎) + (照明) | 自然语言自由书写; 支持切镜和创意特效 |
| **Doubao Seedance 2.0 系列** | 主体 + 动作/运动 + 空间背景/光影/风格 + 镜头调度/音效 | 支持T2V/I2V/R2V/V2V; 原生音频+视频联合生成; 多模态参考(图片/音频/视频); 支持文字生成(广告语/字幕/气泡台词); 支持视频编辑(元素增删改/延长/轨道补齐) |
| **Seedance 1.5 Pro** | 主体 + 动作 + 场景 + 镜头 + 风格 | 更快的生成速度 |
| **Seedance 1.0 Pro / Pro Fast** | 主体 + 动作 + 场景 + 镜头 + 风格 | Pro Fast: 极致速度 |
| **图生视频 (I2V)** | 动作 + 镜头 + (情绪/照明) | 由图像提供主体+场景, 提示词只控制动态 |
| **智能多帧** | [多帧图像] + [每帧时长] + [运镜提示词] | 多图驱动一镜到底; 上传2-10帧; 每帧1-6s |

## Core Methodology

The video prompt formula extends the image formula with two critical dimensions: **motion** and **camera**.

**For 视频3.0/3.0 Pro 文生视频:**
```
主体 + 动作 + 场景 + 镜头 + 风格 + (情绪演绎) + (照明)
```

**For 图生视频 (image-to-video):**
```
动作 + 镜头 + (情绪/照明)
```

**For Doubao Seedance 2.0 系列 文生视频:**
```
主体 + 动作/运动 + 空间背景/光影/风格 + 镜头调度/音效
```

The key difference from text-to-image prompting:
- **Motion is mandatory**: a video without motion is just a still image
- **Camera adds storytelling**: how the camera moves determines the viewer's emotional experience
- **Duration shapes pacing**: a 5-second clip needs different action density than a 10-second clip
- **For 视频3.0 Pro specifically**: 自然语言自由书写, 核心思路是"直观表达出你想要的效果"
- **For Doubao Seedance 2.0**: 支持多模态参考(图片/音频/视频), 可在提示词中用"图片1""图片2"指代参考素材

## How to use this skill

### Step 1: Identify video scenario category
→ Load `rules/video-category-table.md` to match user's request to the right category and example file

### Step 2: Load reference materials

**Load video vocabulary — choose by what you need:**

| 需要什么 | 加载文件 |
|----------|----------|
| 人物动作、自然动态、动物动态、机械运动 | `video-words/motion.md` |
| 场景环境、视频画质、视频风格、氛围情绪、节奏描述 | `video-words/scene-style.md` |

**Load camera movement references — choose by complexity:**

| 需要什么 | 加载文件 |
|----------|----------|
| 推拉摇移跟升降 | `camera-basic.md` |
| 环绕、一镜到底、希区柯克、运镜情感映射 | `camera-advanced.md` |

**Load reference guides:**
- `references/jimeng-video-3.0-guide.md` — when user mentions 视频3.0/3.0 Pro
- `references/smart-multi-frame-guide.md` — when user mentions 智能多帧/多帧/一镜到底

**For color descriptions**, cross-reference text2image's `color-library/chinese-traditional.md` or `gugong-384-colors.md`.

### Step 3: Build the prompt
→ Load `rules/video-core-methodology.md` for component-by-component build guide + presentation format

### Step 4: Apply video writing rules
→ Load `rules/video-writing-rules.md` for all 7 rules (motion, camera, duration, light, etc.)

### Step 5: Validate
→ Load `rules/video-validation-checklist.md` and run through all checks

## Gotchas

1. **Action must be explicit** — 即梦 cannot infer motion from static description. "一个人在街上" = static shot
2. **Complex interactions fail** — multi-person interactions + camera movement = distortion risk
3. **Chinese camera terms work better** — "镜头缓缓推近" > "dolly in slowly"
4. **Seedance quality/speed tradeoff** — seedance2.0 = highest quality/slowest; fast = faster/lower quality
5. **Duration-to-action matching** — 5s with 3-stage action = rushed. Match complexity to time
6. **First-time web authorization** — some models require browser auth before first use
7. **Character consistency not guaranteed** — same face across segments not reliable
8. **Camera + complex motion = risk** — prioritize one over the other
9. **Model version matters** — 视频3.0 Pro uses natural language, Seedance 2.0 needs structured camera direction. 智能多帧 requires uploading frames + per-frame duration settings
10. **⚠️ Never write hex color codes in video prompts** — Same as image prompts: `#RRGGBB` values get rendered as text in the video frames, NOT as color instructions. Use Chinese color names only
10. **⚠️ No hex color values** — Same rule as image prompts: never write `#ff2121` into video prompts. Use Chinese color names only

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `rules/video-category-table.md` | 12 video scenario categories | Step 1 |
| `rules/video-core-methodology.md` | Component-by-component build guide | Step 3 |
| `rules/video-writing-rules.md` | 7 video-specific writing rules | Step 4 |
| `rules/video-validation-checklist.md` | 6-point pre-submission checklist | Step 5 |
| `video-words/motion.md` | Motion vocabulary library | When writing motion descriptions |
| `video-words/scene-style.md` | Scene/style/vocabulary library | When describing scenes |
| `camera-basic.md` | 7 basic camera movements | Basic camera work needed |
| `camera-advanced.md` | 7 compound moves + emotion mapping | Advanced camera work |
| `references/jimeng-video-3.0-guide.md` | 视频3.0/3.0 Pro: 8 dimensions | User mentions 视频3.0 |
| `references/smart-multi-frame-guide.md` | 智能多帧: 多图一镜到底 | User mentions 智能多帧/多帧 |