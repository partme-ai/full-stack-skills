# Multi-Modal Reference — 全能参考执行

## Examples

### 人物+场景分离

```bash
dreamina user_credit
ls -la ./person.png ./scene.png

dreamina multimodal2video \
  --image ./person.png,./scene.png \
  --prompt="图一提供人物的面部特征和服装。图二提供秋日森林的场景环境和暖金色调。人物站在森林中，阳光穿透树冠形成斑驳光影。微风吹动头发和衣角，树叶轻轻摆动。所有元素光源和色调统一。8秒。" \
  --duration=8 \
  --poll=60
```

### 图+音频口型同步

```bash
dreamina user_credit
ls -la ./person.png ./speech.mp3

dreamina multimodal2video \
  --image ./person.png \
  --audio ./speech.mp3 \
  --prompt="人物按照音频节奏自然说话，口型与语音同步。伴随自然眨眼和微表情。身体和背景保持相对静止。保持图一的人物特征和光线不变。" \
  --poll=60
```

### 完整三件套（图+视频+音频）

```bash
dreamina user_credit
ls -la ./person.png ./outfit.png ./scene.png ./movement.mp4 ./music.mp3

dreamina multimodal2video \
  --image ./person.png,./outfit.png,./scene.png \
  --video ./movement.mp4 \
  --audio ./music.mp3 \
  --prompt="图一提供人物特征。图二提供服装风格。图三提供场景环境。运动节奏参考视频。情绪基调跟随音频。所有元素在统一的暖色调下自然融合。" \
  --duration=12 \
  --ratio=16:9 \
  --model_version=seedance2.0 \
  --poll=180
```
