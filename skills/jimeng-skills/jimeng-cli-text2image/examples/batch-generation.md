# Batch Generation — 批量/系列生成

## Instructions

当用户需要一次生成多张图片（系列作品、多角度展示、风格变体等），使用异步或串联方式。

## Examples

### Example: 系列主题生成

**场景**: 用户要生成"四季"系列——同一场景的春夏秋冬4张图

**执行**: 异步批量提交
```bash
# Step 1: 检查额度（确保至少4张的额度）
dreamina user_credit

# Step 2: 逐个提交（不等待）
dreamina text2image --prompt="樱花盛开的春日公园，粉色花海，新绿草地，温暖晨光" --ratio=16:9 --poll=0
# → submit_id: abc-001

dreamina text2image --prompt="葱郁的夏日公园，茂密绿树成荫，金色阳光，蝉鸣时节" --ratio=16:9 --poll=0
# → submit_id: abc-002

dreamina text2image --prompt="秋日公园红叶满地，金黄和深红的落叶，暖色夕阳斜照" --ratio=16:9 --poll=0
# → submit_id: abc-003

dreamina text2image --prompt="冬日雪后公园，银装素裹，白雪覆盖的长椅和树枝，清冷蓝调" --ratio=16:9 --poll=0
# → submit_id: abc-004

# Step 3: 轮询查询所有结果
dreamina query_result --submit_id=abc-001
dreamina query_result --submit_id=abc-002
dreamina query_result --submit_id=abc-003
dreamina query_result --submit_id=abc-004

# Step 4: 汇总结果报告
```

### Example: 多比例版本

**场景**: 用户想要同一张图的不同比例版本（适合多平台发布）

**提示词**: "现代极简客厅，大落地窗引入绿色庭院，原木色和白色配色"

**执行**:
```bash
dreamina user_credit

# 横版 — 适合PC端
dreamina text2image --prompt="现代极简客厅，大落地窗引入绿色庭院，原木色和白色配色" --ratio=16:9 --poll=30

# 正方形 — 适合社交媒体头像
dreamina text2image --prompt="现代极简客厅，大落地窗引入绿色庭院，原木色和白色配色" --ratio=1:1 --poll=30

# 竖版 — 适合手机端
dreamina text2image --prompt="现代极简客厅，大落地窗引入绿色庭院，原木色和白色配色" --ratio=9:16 --poll=30
```

### Example: 风格变体系列

**场景**: 用户想把同一场景做成不同风格版本

**执行**:
```bash
dreamina user_credit

# 写实版
dreamina text2image --prompt="古镇水乡黄昏，写实摄影风格，金色夕阳，水面倒影，8k" --ratio=16:9 --poll=0
# 水墨版
dreamina text2image --prompt="古镇水乡黄昏，水墨画风格，黑白灰墨色，大面积留白，宣纸质感" --ratio=16:9 --poll=0
# 二次元版
dreamina text2image --prompt="古镇水乡黄昏，日式动漫风格，温暖色调，新海诚光影，赛璐珞上色" --ratio=16:9 --poll=0
```

## Workflow Summary

```
对于批量生成：
1. 优先使用 --poll=0（异步），避免串联等待
2. 保存每个 submit_id
3. 全部提交完成后统一 query_result
4. 汇总结果报告给用户

对于串联生成（需要看到前一结果再决定下一张）：
1. 使用 --poll=30（同步）
2. 每张完成后再决定下一张的参数

额度检查：
- 批量前必须检查额度 >= 计划生成张数
- 如额度不足，告知用户并建议减少数量
```
