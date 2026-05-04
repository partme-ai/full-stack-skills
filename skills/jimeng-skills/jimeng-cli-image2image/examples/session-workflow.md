# Session I2I Workflow — 会话图生图项目管理

## Examples

### Example: 创建产品图编辑会话

**执行**:
```bash
# 创建
dreamina session create "product-edits-spring"

# 生成
dreamina user_credit

# 白底电商图
dreamina image2image \
  --images ./product_raw.png \
  --prompt="保持产品形状和颜色不变。移除杂乱背景替换为纯白无缝背景。柔和阴影。均匀柔光。" \
  --ratio=1:1 --session=1 --poll=30

# 场景展示图
dreamina image2image \
  --images ./product_raw.png \
  --prompt="保持产品不变。背景替换为简约北欧风格客厅，产品放置在木质茶几上。自然光线匹配场景。" \
  --ratio=16:9 --session=1 --poll=30
```

### Example: 查找会话+继续编辑

**执行**:
```bash
dreamina session list
dreamina session search "product"

# 在找到的会话中继续
dreamina image2image --images ./new_product.png --prompt="..." --session=1 --poll=30
```

### Example: 查看项目编辑历史

**执行**:
```bash
dreamina list_task
dreamina list_task --gen_status=success
```
