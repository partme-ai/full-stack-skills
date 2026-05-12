---
name: jimeng-prompt-image2video
description: Provides comprehensive guidance for crafting image-to-video (图生视频) prompts for 即梦 (Dreamina/Jimeng) Seedance 2.0. Image-to-video prompts are incremental — the reference image provides the visual content, the prompt only describes what moves and changes. This skill covers 4 sub-modes: single image→video (单图生视频), first-last frame transition (首尾帧), multi-frame storyboard narrative (多帧故事), and multi-modal reference compositing (全能参考). Use when the user has reference image(s) and wants to animate them into a video; mentions "图生视频", "image2video", "图片转视频", "让这张图动起来", "首尾帧", "故事板", "多帧故事", "frames2video"; or provides images and asks to generate a video from them. This skill covers 4 sub-mode templates with 18 annotated examples, a mode decision tree, and I2V-specific incremental description vocabulary. Always use this skill when the user wants to animate reference images into video using 即梦.
license: Complete terms in LICENSE.txt
---

# jimeng-prompt-image2video — 即梦图生视频提示词

Craft prompts for animating reference images into videos using Dreamina's 4 video modes.

## When to use this skill

Use this skill when the user:
- Provides image(s) and wants to generate a video from them ("把这张图做成视频")
- Mentions 图生视频, image2video, 图片转视频, 让图动起来
- Describes a specific sub-mode: 单图生视频, 首尾帧, 多帧故事, 全能参考
- Has multiple images and wants to create a narrative video
- Asks how to describe motion from a static reference image

Do NOT use for:
- Text-to-video (no reference images) → use jimeng-prompt-text2video
- CLI execution → use jimeng-cli-image2video
- Image-to-image editing (output is still an image) → use jimeng-prompt-image2image

## Core Methodology

Image-to-video prompting is fundamentally **incremental**: the reference image already provides the visual content. The prompt only needs to describe what MOVES and CHANGES.

```
[从哪里开始] + [什么在动/怎么动] + [运镜方式] + [环境/光影变化] + [时长/节奏] + [风格一致]
```

### The I2V Golden Rule

**Don't describe what's already in the image. Only describe what happens next.**

- ✗ "一个穿红裙子的女孩站在花园里，阳光灿烂..." — the image already shows this
- ✓ "女孩缓缓转身面向镜头，红裙随风飘动，镜头慢慢推近" — this is what happens NEXT

## 4 Sub-Modes Overview

| # | Mode | Input | Core Prompt Focus | Example File |
|---|------|-------|-------------------|--------------|
| 1 | 单图生视频 | 1 image | "从这张图开始，接下来发生什么运动" | `examples/single-image.md` |
| 2 | 首尾帧 | 2 images | "如何从图A过渡到图B" | `examples/first-last-frame.md` |
| 3 | 多帧故事 | 2-20 images | "帧与帧之间的因果关系和时间流逝" | `examples/multi-frame.md` |
| 4 | 全能参考 | images+video+audio | "综合各参考素材，生成目标视频" | `examples/multimodal-ref.md` |

## How to use this skill

### Step 1: Identify the sub-mode

Ask the user or infer from context:
- Has 1 image → Sub-mode 1 (单图生视频)
- Has 2 images described as start/end → Sub-mode 2 (首尾帧)
- Has 2+ images forming a sequence/storyboard → Sub-mode 3 (多帧故事)
- Has mixed media (images + video + audio) → Sub-mode 4 (全能参考)

### Step 2: Load reference materials

**Load the matched example file** from `examples/` for sub-mode-specific patterns.

**Load `references/mode-library.md`** for detailed templates per sub-mode.

**Load `references/word-library.md`** for I2V-specific motion and coordination vocabulary.

**For camera movement vocabulary**, cross-reference the text2video skill's `camera-library.md` — it covers 7 basic + 6 advanced camera movements with emotional mappings, not duplicated here.

### Step 3: Build the prompt (incremental description)

**For sub-mode 1 (单图生视频):**
1. **Starting point** (从哪里开始): Acknowledge the reference image — "从这张画面开始"
2. **What moves** (什么在动): The MOST important component. Be specific about WHICH elements move and HOW. "头发在微风中飘动，水面的波纹缓缓扩散" — describe only what changes
3. **What stays still** (什么不动): Explicitly state static elements — "建筑和远山保持完全静止"
4. **Camera movement** (运镜): How the camera moves through the scene
5. **Duration/pacing** (时长/节奏): 4-15 seconds, match complexity
6. **Style consistency** (风格一致): The output must match the reference image's style

**For sub-mode 2 (首尾帧):**
1. Describe the TRANSITION from frame A to frame B — "花瓣从含苞逐渐绽放至完全盛开"
2. Describe the pacing of the transition — "前半段缓慢积蓄，后半段加速绽放"
3. Camera can remain static or follow the transformation

**For sub-mode 3 (多帧故事):**
1. Describe the causal relationship between frames — "因为风吹过，所以花瓣飘落"
2. Describe the passage of time — "从清晨到正午，光影在建筑表面缓缓移动"
3. Camera work should connect frames narratively

**For sub-mode 4 (全能参考):**
1. Assign clear roles to each reference — "图一提供人物特征，图二提供场景风格"
2. Describe the synthesis — how elements from different references interact

### Step 4: Apply I2V-specific rules

1. **Incremental only**: Don't repeat what the reference image already shows
2. **Motion specificity**: "她的头发在微风中轻轻飘动" not "有风"
3. **Stillness is intentional**: Explicitly state what does NOT move
4. **Camera respects the reference**: Camera movement is constrained by the reference composition
5. **Style must match**: The output must be stylistically consistent with the reference

### Step 5: Validate against checklist

Run through the [Validation Checklist](#validation-checklist). Every item must pass before presenting the prompt to the user.

### Step 6: Present the result

Always present: sub-mode label + motion description + complete prompt + duration + camera explanation.

## Writing Rules for Image-to-Video

### Rule 1: Incremental description — only write what changes

The reference image IS the visual. Don't describe its static content in the prompt. Focus 100% on motion and change.

### Rule 2: Explicit stillness is as important as motion

Without explicit stillness constraints, AI tends to animate everything. Write "保持建筑完全静止""只有水在流动，其他一切不动".

### Rule 3: Match sub-mode to prompt structure

Each sub-mode needs a different prompt structure. Don't use a single-image prompt for a frames2video task.

### Rule 4: Camera movement respects the reference

Unlike text-to-video where camera can go anywhere, I2V camera movement is bound by the reference image's composition. Camera descriptions should work WITH the existing composition.

### Rule 5: Duration scales with complexity

| Sub-mode | Motion Complexity | Suggested Duration |
|----------|------------------|-------------------|
| 单图 | 1-2 moving elements | 5-8s |
| 首尾帧 | 1 complete transformation | 8-12s |
| 多帧 | Multi-stage narrative | 10-15s |
| 全能参考 | Complex multi-source synthesis | 8-12s |

## Validation Checklist

- [ ] Prompt describes only what MOVES/CHANGES (not static content from the reference image)
- [ ] Specific elements are named as moving + specific motion verbs used
- [ ] Elements that should stay still are explicitly listed
- [ ] Camera movement is described (not just named — explain the movement logic)
- [ ] Duration matches motion complexity
- [ ] Style consistency with reference image is addressed
- [ ] Correct sub-mode is identified and communicated

## Gotchas

1. **Don't describe the reference image** — the #1 I2V mistake. "A girl in a red dress standing in a garden" is useless if the reference already shows this. Write what HAPPENS: "The girl slowly turns..."
2. **Everything moves unless you stop it** — AI's default is to animate everything. Use "everything else remains completely still" to lock down static elements
3. **Camera terms need explanation, not just naming** — 只写"推镜头"不够，需要写"镜头缓缓向前推进，逐渐聚焦人物的面部表情"
4. **Resolution varies by sub-mode** — Seedance 2.0 = 720p, legacy 3.5pro frames2video = 1080p
5. **Multiframe limit** — 2-20 images for multi-frame story mode. More images = better consistency but slower generation
6. **Multimodal limits** — max 9 images + 3 videos + 3 audio clips
7. **Style drift possible** — output video may not perfectly match reference image style; use "保持参考图的风格和色调完全一致" to minimize drift

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `references/mode-library.md` | 4 sub-mode templates with prompt structures | When building any I2V prompt |
| `references/word-library.md` | I2V-specific motion, stillness, coordination vocabulary | When building any I2V prompt |
| `examples/single-image.md` | 单图生视频 examples | User has 1 reference image |
| `examples/first-last-frame.md` | 首尾帧 examples | User has 2 images as start/end |
| `examples/multi-frame.md` | 多帧故事 examples | User has 2+ sequential images |
| `examples/multimodal-ref.md` | 全能参考 examples | User has mixed media references |
