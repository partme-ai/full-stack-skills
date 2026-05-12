# Basic Video Generation — 基础视频生成

## Instructions

最常见场景：用户有写好的视频提示词（含运动+运镜描述），直接生成视频。

## Examples

### Example: 标准视频生成

**场景**: 用户在 jimeng-prompt-text2video 创建了提示词并获批准

**提示词**: "年轻女孩在清晨的森林中缓缓行走，长发和裙摆随风摇曳，阳光透过树冠形成光束洒在她身上，镜头侧面跟拍，8秒，清新治愈风格"

**提示词建议参数**: 时长 8s，比例 16:9

**执行**:
```bash
# Step 1: 检查额度（视频消耗大）
dreamina user_credit

# Step 2: 映射参数并生成
dreamina text2video \
  --prompt="年轻女孩在清晨的森林中缓缓行走，长发和裙摆随风摇曳，阳光透过树冠形成光束洒在她身上，镜头侧面跟拍，8秒，清新治愈风格" \
  --duration=8 \
  --ratio=16:9 \
  --poll=60

# Step 3: 等待结果。如 poll 超时 → query_result
```

### Example: 人物回眸短视频

**场景**: 竖屏人像视频，5秒回眸瞬间

**执行**:
```bash
dreamina user_credit
dreamina text2video \
  --prompt="穿风衣的女性在秋日黄昏街头缓步前行，听到呼唤缓缓转身回眸一笑，金色夕阳逆光勾勒发丝光晕，镜头缓缓推近面庞，5秒，电影感温暖色调" \
  --duration=5 \
  --ratio=9:16 \
  --poll=60
```

### Example: 自然风景长视频

**场景**: 10秒瀑布风景视频，需要高质量

**执行**:
```bash
dreamina user_credit
dreamina text2video \
  --prompt="巨大瀑布从翠绿山谷倾泻而下，水雾升腾在阳光中形成彩虹，镜头从瀑布顶端缓缓向下摇至深潭，10秒，风光纪录片风格，电影级画质" \
  --duration=10 \
  --ratio=16:9 \
  --model_version=seedance2.0 \
  --poll=120
```

### Example: 快速测试（使用默认参数）

**场景**: 快速测试一个新提示词的效果

**执行**:
```bash
dreamina user_credit
dreamina text2video --prompt="镜头缓缓推近，一只橘猫在窗台上伸懒腰打哈欠，阳光洒在蓬松的毛发上，5秒，萌宠风格" --poll=60
# 使用了所有默认值: duration=5s, ratio=16:9, model=seedance2.0fast, resolution=720P
```

## Workflow Summary

```
1. dreamina user_credit                    ← 总是第一步
2. 将提示词的建议时长+比例映射为 CLI 参数
3. dreamina text2video --prompt="..." --duration=N --ratio=X:Y --poll=60
4. 等待结果或 query_result
```
