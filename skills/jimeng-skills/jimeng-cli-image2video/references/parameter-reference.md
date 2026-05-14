# Parameter Reference — dreamina image2video 全子命令参数

> 4 个子命令的完整参数参考。运行前执行 `<subcommand> -h` 确认最新参数。

---

## image2video（单图生视频）

| 参数 | 必需 | 值 | 默认 |
|------|------|-----|------|
| `--image` | **Yes** | 本地图片路径 | — |
| `--prompt` | No | 运动描述（增量式） | — |
| `--duration` | No | 3-15s | 5 |
| `--model_version` | **Yes** | seedance2.0, seedance2.0fast, **seedance2.0_vip, seedance2.0fast_vip**, 3.0, 3.0fast, 3.0pro, 3.5pro | seedance2.0fast_vip ⬅️ VIP 优先 |
| `--video_resolution` | No | 720P (Seedance), 1080P (legacy) | 720P |
| `--poll` | No | 秒 (0=async) | 0 |

## frames2video（首尾帧）

| 参数 | 必需 | 值 | 默认 |
|------|------|-----|------|
| `--first` | **Yes** | 本地图片路径（起始帧） | — |
| `--last` | **Yes** | 本地图片路径（结束帧） | — |
| `--prompt` | No | 过渡描述 | — |
| `--duration` | No | 4-15s | 5 |
| `--model_version` | **Yes** | seedance2.0, seedance2.0fast, **seedance2.0_vip, seedance2.0fast_vip**, 3.5pro | seedance2.0fast_vip ⬅️ VIP 优先 |
| `--video_resolution` | No | 720P (Seedance), 1080P (legacy) | 720P |

## multiframe2video（多帧故事）

| 参数 | 必需 | 值 | 默认 |
|------|------|-----|------|
| `--images` | **Yes** | 2-20 张本地图片，逗号分隔 | — |
| `--prompt` | No | 叙事/过渡描述 | — |
| `--transition-prompt` | No | 帧间连接方式 | — |
| `--transition-duration` | No | 帧间过渡时长 | — |
| `--duration` | No | 4-15s | 5 |
| `--model_version` | No | seedance2.0, seedance2.0fast, 3.5pro | seedance2.0fast |

## multimodal2video（全能参考）

| 参数 | 必需 | 值 | 默认 |
|------|------|-----|------|
| `--image` | No* | 最多9张本地图片 | — |
| `--video` | No | 最多3段本地视频 | — |
| `--audio` | No | 最多3段本地音频 | — |
| `--prompt` | No | 合成描述 | — |
| `--duration` | No | 4-15s | 5 |
| `--ratio` | No | 1:1, 3:4, 16:9, 4:3, 9:16, 21:9 | 16:9 |
| `--model_version` | No | seedance2.0, seedance2.0fast, **seedance2.0_vip, seedance2.0fast_vip** | seedance2.0fast_vip ⬅️ VIP 优先 |

> *至少需要 `--image`、`--video`、`--audio` 其中之一。

---

## 参数名差异速查（关键！）

| 概念 | image2video | frames2video | multiframe2video | multimodal2video |
|------|-----------|-------------|-----------------|-----------------|
| 图片输入 | `--image` (单数) | `--first` `--last` | `--images` (复数) | `--image` (复数) |
| 视频参考 | — | — | — | `--video` |
| 音频参考 | — | — | — | `--audio` |
| 过渡控制 | — | — | `--transition-prompt` `--transition-duration` | — |
| 比例 | 由参考图决定 | 由参考图决定 | 由参考图决定 | `--ratio` |
