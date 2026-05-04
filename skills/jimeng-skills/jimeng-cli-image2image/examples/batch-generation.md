# Batch I2I Generation — 批量图生图编辑

## Examples

### Example: 同风格批量转换

**场景**: 将3张照片批量转换为水彩画风格

**执行**:
```bash
dreamina user_credit

# 验证所有图片存在
ls -la ./photo1.png ./photo2.png ./photo3.png

# 异步批量提交
dreamina image2image --images ./photo1.png --prompt="保持构图不变，转换为水彩画风格，透明感上色，柔和渲染，湿画法过渡" --poll=0
# → submit_id: i2i-001

dreamina image2image --images ./photo2.png --prompt="保持构图不变，转换为水彩画风格，透明感上色，柔和渲染，湿画法过渡" --poll=0
# → submit_id: i2i-002

dreamina image2image --images ./photo3.png --prompt="保持构图不变，转换为水彩画风格，透明感上色，柔和渲染，湿画法过渡" --poll=0
# → submit_id: i2i-003

# 统一查询
dreamina query_result --submit_id=i2i-001
dreamina query_result --submit_id=i2i-002
dreamina query_result --submit_id=i2i-003
```

### Example: 多版本风格对比

**场景**: 同一张照片生成3种不同艺术风格版本

**执行**:
```bash
dreamina user_credit
ls -la ./original.png

# 水墨版
dreamina image2image --images ./original.png --prompt="保持构图，转换为水墨画风格" --poll=0
# → submit_id: ver-ink

# 油画版
dreamina image2image --images ./original.png --prompt="保持构图，转换为印象派油画风格，厚涂笔触" --poll=0
# → submit_id: ver-oil

# 二次元版
dreamina image2image --images ./original.png --prompt="保持构图，转换为日式动漫风格，赛璐珞上色" --poll=0
# → submit_id: ver-anime

# 稍后对比
for id in ver-ink ver-oil ver-anime; do
  dreamina query_result --submit_id=$id
done
```

### Example: 多图片背景替换

**场景**: 批量替换同一主题的产品图背景

**执行**:
```bash
dreamina user_credit

for img in product_a.png product_b.png product_c.png; do
  test -f ./$img || echo "MISSING: $img"
  dreamina image2image \
    --images ./$img \
    --prompt="保持产品形状、颜色和材质完全不变。移除杂乱桌面背景，替换为纯白无缝电商摄影背景。添加柔和底部阴影。均匀柔光。" \
    --ratio=1:1 \
    --poll=0
done
```
