# Batch Video Generation — 批量视频生成

## Instructions

当用户需要生成多个视频（系列作品、多版本等），使用异步提交方式避免串联等待。

## Examples

### Example: 系列视频（春夏秋冬）

**场景**: 生成同一场景的春夏秋冬4个视频

**执行**:
```bash
dreamina user_credit

# 异步提交4个视频
dreamina text2video --prompt="镜头横摇扫过春日樱花盛开的公园，粉色花海，新绿草地，温暖晨光，8秒" --duration=8 --poll=0
# → submit_id: vid-spring-001

dreamina text2video --prompt="镜头横摇扫过夏日葱郁的公园，茂密绿树成荫，金色阳光穿透树叶，蝉鸣时节，8秒" --duration=8 --poll=0
# → submit_id: vid-summer-002

dreamina text2video --prompt="镜头横摇扫过秋日公园红叶满地，金黄和深红的落叶飘落，暖色夕阳斜照，8秒" --duration=8 --poll=0
# → submit_id: vid-autumn-003

dreamina text2video --prompt="镜头横摇扫过冬日雪后公园，银装素裹，白雪覆盖的长椅和树枝在风中轻颤，8秒" --duration=8 --poll=0
# → submit_id: vid-winter-004

# 等待一段时间后统一查询
dreamina query_result --submit_id=vid-spring-001
dreamina query_result --submit_id=vid-summer-002
dreamina query_result --submit_id=vid-autumn-003
dreamina query_result --submit_id=vid-winter-004
```

### Example: 多比例版本

**场景**: 同一个视频内容，横版+竖版两个版本

**执行**:
```bash
dreamina user_credit

# 横版（PC端）
dreamina text2video \
  --prompt="产品在纯黑背景中缓缓旋转展示，光影在流畅的曲面上流转，镜头环绕180度，8秒，广告质感" \
  --duration=8 --ratio=16:9 --poll=60

# 竖版（手机端）
dreamina text2video \
  --prompt="产品在纯黑背景中缓缓旋转展示，光影在流畅的曲面上流转，镜头环绕180度，8秒，广告质感" \
  --duration=8 --ratio=9:16 --poll=60
```

### Example: 质量对比测试

**场景**: 同一个提示词，对比 fast 和 slow 模型效果

**执行**:
```bash
dreamina user_credit

# fast 版本（快速预览）
dreamina text2video \
  --prompt="镜头推进，一位芭蕾舞者在空舞台上旋转，白色纱裙如花朵绽放，追光打在她身上，8秒" \
  --duration=8 --model_version=seedance2.0fast --poll=0
# → submit_id: vid-fast-001

# slow 版本（高质量对比）
dreamina text2video \
  --prompt="镜头推进，一位芭蕾舞者在空舞台上旋转，白色纱裙如花朵绽放，追光打在她身上，8秒" \
  --duration=8 --model_version=seedance2.0 --poll=0
# → submit_id: vid-slow-002

# 稍后对比两个结果
```

## Workflow Summary

```
批量视频生成：
1. dreamina user_credit
2. 全部异步提交（--poll=0），保存每个 submit_id
3. 等待足够时间（视频生成需要数分钟）
4. 逐个 query_result 查询
5. 汇总结果

额度注意：
- 视频消耗远大于图像
- 批量前确保额度 >= 计划生成数量
- 如余额不足，建议减少数量或缩短 duration
```
