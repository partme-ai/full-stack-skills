---
name: jimeng-cli-image2video
description: Provides comprehensive guidance for executing image-to-video (图生视频) generation via the dreamina CLI for 即梦. This skill covers 4 sub-commands selected by input type: image2video (1 image → animate), frames2video (2 images → transition via --first/--last), multiframe2video (2-20 storyboard images → narrative via --images and --transition-prompt), and multimodal2video (up to 9 images + 3 videos + 3 audio → synthesis). Use when the user has reference images or media files and wants to generate video via CLI; mentions "dreamina image2video", "图生视频CLI", "frames2video", "multiframe2video", "multimodal2video"; or provides media files and asks to animate or synthesize them. This skill covers mode detection with a decision tree, parameter name differences between sub-commands, input limits per mode, and 4 mode-specific execution workflows. Always use this skill when the user wants to generate video from reference media via the dreamina command line.
license: Complete terms in LICENSE.txt
---

# jimeng-cli-image2video — 即梦图生视频 CLI 执行

Execute image-to-video generation via the `dreamina` CLI. This skill handles 4 sub-commands, routing by input type, credit management, file verification, and result retrieval.

**This skill does NOT craft prompts.** Prompt crafting is handled by `jimeng-prompt-image2video`.

## When to use this skill

Use this skill when:
- The user has reference image(s) and an approved video prompt
- The user mentions dreamina image2video, frames2video, multiframe2video, multimodal2video
- The user says "让这张图动起来" or "把这些图做成视频"

Do NOT use for:
- Prompt crafting → jimeng-prompt-image2video
- Text-to-video CLI → jimeng-cli-text2video
- Image CLI → jimeng-cli-text2image / jimeng-cli-image2image

## Mode Detection

Route to the correct sub-command based on input:

| Input | Sub-command | CLI Command |
|-------|-----------|-------------|
| 1 image | image2video | `dreamina image2video --image ./x.png --prompt="..."` |
| 2 images (start+end) | frames2video | `dreamina frames2video --first ./a.png --last ./b.png --prompt="..."` |
| 2-20 images (storyboard) | multiframe2video | `dreamina multiframe2video --images ./a.png,./b.png,... --transition-prompt="..."` |
| images + video + audio | multimodal2video | `dreamina multimodal2video --image ... --video ... --audio ... --prompt="..."` |

## Mode 1: Single Image to Video (`dreamina image2video`)

**Input**: 1 image → animate with motion description

```bash
# Basic
dreamina image2video --image ./photo.png --prompt="微风吹动头发和衣角，眼睛缓慢眨眼，镜头缓缓推近" --poll=60

# With duration
dreamina image2video --image ./photo.png --prompt="云层缓慢飘移，水面波纹扩散" --duration=8 --poll=60

# High quality
dreamina image2video --image ./photo.png --prompt="..." --model_version=seedance2.0 --poll=120

# Async
dreamina image2video --image ./photo.png --prompt="..." --poll=0
```

| Parameter | Required | Values | Default |
|-----------|----------|--------|---------|
| `--image` | **Yes** | Single local image path | — |
| `--prompt` | No* | Motion description (incremental) | — |
| `--duration` | No | 3-15s (model-dependent) | 5 |
| `--model_version` | No | seedance2.0, seedance2.0fast, 3.0, 3.0fast, 3.0pro, 3.5pro | seedance2.0fast |
| `--video_resolution` | No | 720P (Seedance), 1080P (legacy) | 720P |
| `--poll` | No | Seconds (0=async, polls every 1s) | 0 |

## Mode 2: First & Last Frame (`dreamina frames2video`)

**Input**: 2 images (start frame + end frame) → transition animation

```bash
# Basic
dreamina frames2video --first ./start.png --last ./end.png --prompt="花瓣从含苞到完全盛开，外层先展开，内层随后逐层绽放" --poll=60

# With duration
dreamina frames2video --first ./morning.png --last ./night.png --prompt="天空从橙色渐变到深蓝，城市灯光渐次亮起" --duration=10 --poll=60
```

| Parameter | Required | Values | Default |
|-----------|----------|--------|---------|
| `--first` | **Yes** | Local image path (start frame) | — |
| `--last` | **Yes** | Local image path (end frame) | — |
| `--prompt` | No* | Transition description | — |
| `--duration` | No | 4-15s | 5 |
| `--model_version` | No | seedance2.0, seedance2.0fast, 3.5pro | seedance2.0fast |
| `--video_resolution` | No | 720P (Seedance), 1080P (legacy) | 720P |

## Mode 3: Multi-Frame Story (`dreamina multiframe2video`)

**Input**: 2-20 images (storyboard/keyframes) → narrative video

```bash
# 2-image
dreamina multiframe2video --images ./a.png,./b.png --prompt="从清晨到正午，光影在建筑表面移动" --poll=60

# 3+ images with transition control
dreamina multiframe2video \
  --images ./frame1.png,./frame2.png,./frame3.png,./frame4.png \
  --prompt="故事板叙事：沉思→惊喜→急切→喜悦" \
  --transition-prompt="平滑过渡，镜头跟随情绪节奏" \
  --duration=15 \
  --poll=120
```

| Parameter | Required | Values | Default |
|-----------|----------|--------|---------|
| `--images` | **Yes** | 2-20 local image paths, comma-separated | — |
| `--prompt` | No* | Narrative/transition description | — |
| `--transition-prompt` | No | How frames connect | — |
| `--transition-duration` | No | Transition time between frames | — |
| `--duration` | No | 4-15s | 5 |
| `--model_version` | No | seedance2.0, seedance2.0fast, 3.5pro | seedance2.0fast |

## Mode 4: All-Around Reference (`dreamina multimodal2video`)

**Input**: images + video + audio mix → synthesized video (strongest mode)

```bash
# Images only
dreamina multimodal2video \
  --image ./person.png,./scene.png,./style.png \
  --prompt="图一人物特征配图二场景环境和图三的艺术风格。统一光源方向。色调协调。" \
  --poll=60

# Images + audio
dreamina multimodal2video \
  --image ./person.png \
  --audio ./voice.mp3 \
  --prompt="人物按照音频节奏自然说话，口型同步，伴随自然眨眼和微表情" \
  --poll=60

# Full combo (images + video + audio)
dreamina multimodal2video \
  --image ./person.png,./outfit.png,./scene.png \
  --video ./movement_ref.mp4 \
  --audio ./music.mp3 \
  --prompt="人物特征+服装+场景合成。运动节奏参考视频。情绪基调跟随音频。" \
  --duration=12 \
  --poll=120
```

| Parameter | Required | Values | Default |
|-----------|----------|--------|---------|
| `--image` | No* | Up to 9 local image paths | — |
| `--video` | No | Up to 3 local video paths | — |
| `--audio` | No | Up to 3 local audio paths | — |
| `--prompt` | No* | Synthesis description | — |
| `--duration` | No | 4-15s | 5 |
| `--ratio` | No | 1:1, 3:4, 16:9, 4:3, 9:16, 21:9 | 16:9 |
| `--model_version` | No | seedance2.0, seedance2.0fast | seedance2.0fast |

> At least one of `--image`, `--video`, or `--audio` required. Max: 9 images + 3 videos + 3 audio.

## Execution Flow (All Modes)

```
1. dreamina user_credit                         # Always first
2. Verify input files exist (ls -la)             # All modes need local files
3. Detect mode → select correct sub-command      # Based on input count/type
4. Submit with --poll=N (recommend 60 for video) # Video is slow
5. On poll timeout → dreamina query_result --submit_id=<id>
6. Report results
```

## FAQ (from official documentation)

**Q: Login succeeds but generation commands fail?**
A: Verify `~/.dreamina_cli/config.toml` exists. Run `dreamina user_credit` as definitive self-check.

**Q: Browser login stuck?**
A: `dreamina login --debug` for detailed output.

**Q: Async task no final result?**
A: Use `--poll=N`. If timeout, save submit_id from intermediate result → `dreamina query_result --submit_id=<id>`.

**Q: Switch accounts?**
A: `dreamina relogin`. Clear credentials: `dreamina logout`.

## Gotchas

1. **Always check credits first** — video consumes far more than images
2. **Prompt goes through prompt skill first** — route to jimeng-prompt-image2video for all prompt crafting
3. **Prompt is incremental** — describe only what MOVES, not static content from reference image
4. **Mode detection is critical** — 1 image vs 2 (frames2video) vs 2+ sequential (multiframe2video) — routing determines the sub-command and parameter names differ (`--image` vs `--images` vs `--first/--last`)
5. **Seedance 2.0 = 720P** — written as `720P` (capital P). 1080P only on legacy 3.0/3.5pro
6. **--poll at least 60** — video generation takes minutes. 60 minimum, 120 for quality models
7. **multimodal2video max inputs** — 9 images + 3 videos + 3 audio. Exceeding this errors
8. **multiframe2video max 20 images** — beyond this not supported
9. **Some models need web auth** — `AigcComplianceConfirmationRequired` → authorize on website
10. **Parameter names vary by sub-command** — `image2video` uses `--image` (singular); `multiframe2video` uses `--images` (plural); `frames2video` uses `--first`/`--last`

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `references/parameter-reference.md` | Complete parameter reference for all 4 sub-commands | When mapping prompt to CLI args |
| `references/mode-guide.md` | Mode detection + sub-command selection guide | When determining which sub-command to use |
| `references/workflow-patterns.md` | Execution patterns per mode, file verification, error handling | When executing complex generations |
| `examples/single-image.md` | Single image→video flows | 1 reference image |
| `examples/first-last-frame.md` | Start→end frame transition flows | 2 images as start/end |
| `examples/multi-frame.md` | Multi-frame storyboard flows | 2-20 storyboard images |
| `examples/multimodal-ref.md` | All-around reference flows | Mixed media references |
