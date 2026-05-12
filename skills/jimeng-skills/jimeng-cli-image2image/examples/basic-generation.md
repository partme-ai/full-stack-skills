# Basic I2I Generation — 基础图生图编辑

## Examples

### Example: 风格迁移

**场景**: 照片转水墨画

**执行**:
```bash
dreamina user_credit
ls -la ./photo.png

dreamina image2image \
  --images ./photo.png \
  --prompt="保持原图的构图和主体轮廓不变。转换为水墨画风格，色彩转为黑白灰墨色，笔触模仿传统水墨的皴擦点染，增加大面积留白。宣纸质感。" \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=30
```

### Example: 背景替换

**场景**: 换人物背景

**执行**:
```bash
dreamina user_credit
ls -la ./portrait.png

dreamina image2image \
  --images ./portrait.png \
  --prompt="保持人物面部特征、表情、姿势和服装完全不变。将纯色室内背景替换为阳光明媚的热带海滩。调整人物身上光线色温匹配海滩阳光。在脚下添加自然沙滩阴影。" \
  --ratio=3:4 \
  --poll=30
```

### Example: 细节增强

**场景**: 增强人像清晰度

**执行**:
```bash
dreamina user_credit
ls -la ./selfie.png

dreamina image2image \
  --images ./selfie.png \
  --prompt="保持人物面部特征、表情、发型、服装和背景完全不变。增强皮肤的自然纹理细节，添加眼神光，提升睫毛和眉毛的清晰度。增强效果自然，避免过度锐化。提升至4K画质。" \
  --resolution_type=4k \
  --poll=30
```

### Example: 色彩调整

**场景**: 暖色调转冷色调

**执行**:
```bash
dreamina user_credit
ls -la ./warm_photo.png

dreamina image2image \
  --images ./warm_photo.png \
  --prompt="保持构图和所有内容完全不变。将整体色调从暖黄色调整为冷蓝色调。降低暖色的饱和度，增强冷色的比重。肤色在冷调中保持自然不偏青。色彩过渡平滑自然。" \
  --poll=30
```
