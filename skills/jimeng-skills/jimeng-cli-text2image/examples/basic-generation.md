# Basic Generation — 基础生成流程

## Instructions

最常见的场景：用户有一个写好的提示词，要直接生成一张图片。此流程覆盖从额度检查到结果返回的完整步骤。

## Examples

### Example: 标准生成

**场景**: 用户在 jimeng-prompt-text2image 中创建了提示词并获得批准

**提示词**: "穿汉服的少女站在樱花树下，微风拂动发丝和衣袂，金色夕阳逆光，写实摄影，浅景深，8k超清"

**提示词建议参数**: 比例 3:4, 模型 4.5+, 4K画质

**执行**:
```bash
# Step 1: 检查额度
dreamina user_credit
# 输出: Credits remaining: 45

# Step 2: 映射参数并生成
# 比例 3:4 → --ratio=3:4
# 模型 4.5+ → --model_version=5.0（向上取整到最新稳定版）
# 4K画质 → --resolution_type=4k
dreamina text2image \
  --prompt="穿汉服的少女站在樱花树下，微风拂动发丝和衣袂，金色夕阳逆光，写实摄影，浅景深，8k超清" \
  --ratio=3:4 \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=30

# Step 3: 等待30秒，结果自动返回
# 报告给用户：生成成功，图片已保存
```

### Example: 最简生成

**场景**: 用户只想快速生成，不关心具体参数

**提示词**: "一只橘猫在窗台上晒太阳"

**执行**: 使用默认参数
```bash
dreamina user_credit
dreamina text2image --prompt="一只橘猫在窗台上晒太阳" --poll=30
```

### Example: 指定比例生成

**场景**: 用户需要手机壁纸（竖屏 9:16）

**提示词**: "极简风格的抽象山峦，日落色调，渐变的暖橙色天空"

**执行**:
```bash
dreamina user_credit
dreamina text2image \
  --prompt="极简风格的抽象山峦，日落色调，渐变的暖橙色天空" \
  --ratio=9:16 \
  --poll=30
```

### Example: 使用特定模型版本

**场景**: 用户要生成人像，推荐使用 4.6

**提示词**: "职业女性商务肖像，深蓝西装，自信微笑，办公室窗边自然光，商业人像摄影"

**执行**:
```bash
dreamina user_credit
dreamina text2image \
  --prompt="职业女性商务肖像，深蓝西装，自信微笑，办公室窗边自然光，商业人像摄影" \
  --ratio=3:4 \
  --model_version=4.6 \
  --poll=30
```

## Workflow Summary

```
1. dreamina user_credit                    ← 总是第一步
2. 将提示词的建议参数映射为 CLI 参数
3. dreamina text2image --prompt="..." ... --poll=30
4. 报告结果给用户
```
