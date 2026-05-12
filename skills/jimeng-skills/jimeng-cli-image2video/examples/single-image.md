# Single Image to Video — 单图生视频执行

## Examples

### 人物微动

```bash
dreamina user_credit
ls -la ./portrait.png

dreamina image2video \
  --image ./portrait.png \
  --prompt="人物头发在微风中轻轻飘动，眼睛缓慢眨动一次，嘴角微微上扬，胸口随呼吸有极细微起伏。身体、服装和背景保持完全静止。镜头极缓推近面部。6秒。" \
  --duration=6 \
  --poll=60
```

### 风景微动

```bash
dreamina user_credit
ls -la ./lake.png

dreamina image2video \
  --image ./lake.png \
  --prompt="湖面波纹从中心向外缓缓扩散，云层在天空中极缓慢地飘移，树叶在微风中轻轻摆动。山体、建筑保持完全静止。镜头极缓横摇。8秒。" \
  --duration=8 \
  --poll=60
```

### 高质量版本

```bash
dreamina user_credit
dreamina image2video \
  --image ./photo.png \
  --prompt="瀑布水流持续倾泻，水雾升腾在阳光中形成彩虹，镜头从顶端缓缓下摇至深潭" \
  --duration=10 \
  --model_version=seedance2.0 \
  --poll=120
```

### 快速异步

```bash
dreamina user_credit
dreamina image2video --image ./photo.png --prompt="烛光摇曳闪烁，蜡泪缓缓流下" --duration=5 --poll=0
# → submit_id: i2v-001
# 稍后: dreamina query_result --submit_id=i2v-001
```
