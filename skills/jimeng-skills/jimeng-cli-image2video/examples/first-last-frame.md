# First & Last Frame — 首尾帧执行

## Examples

### 花开花落

```bash
dreamina user_credit
ls -la ./bud.png ./bloom.png

dreamina frames2video \
  --first ./bud.png \
  --last ./bloom.png \
  --prompt="花苞外层花瓣先向外翻开，内层花瓣随后逐层由外向内绽放，花蕊从中心显露。前段缓慢积蓄，中段加速展开，后段完全舒展。10秒。" \
  --duration=10 \
  --poll=60
```

### 季节更替

```bash
dreamina user_credit
ls -la ./summer.png ./autumn.png

dreamina frames2video \
  --first ./summer.png \
  --last ./autumn.png \
  --prompt="树叶从翠绿逐渐变为金黄和红色，从叶缘开始渐变过渡到整片叶子。光影从夏季高角度变为秋季低角度暖光。10秒。" \
  --duration=10 \
  --poll=60
```

### 昼夜转换

```bash
dreamina user_credit
ls -la ./day.png ./night.png

dreamina frames2video \
  --first ./day.png \
  --last ./night.png \
  --prompt="天空从白天蓝渐变为暮色深蓝再入夜。建筑窗户灯光一排排亮起。路灯渐次点亮。10秒。" \
  --duration=10 \
  --model_version=seedance2.0 \
  --poll=120
```
