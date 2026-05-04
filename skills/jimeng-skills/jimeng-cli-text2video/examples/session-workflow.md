# Session Video Workflow — 会话视频项目管理

## Instructions

用会话组织视频生成项目。适合系列视频创作、品牌项目、需要追溯的多次生成。

## Examples

### Example: 创建视频项目会话

**场景**: 为一个品牌宣传片项目创建会话，组织多次视频生成

**执行**:
```bash
# Step 1: 创建项目会话
dreamina session create "brand-campaign-summer"
# 输出: Session created: id=10, name="brand-campaign-summer"

# Step 2: 在会话中生成系列视频
dreamina user_credit

# 开场视频
dreamina text2video \
  --prompt="镜头从高空航拍缓缓下降，展现夏日海滩的全景，碧蓝海水和白色沙滩，遮阳伞点缀海岸，8秒" \
  --session=10 --duration=8 --ratio=16:9 --poll=60

# 产品展示视频
dreamina text2video \
  --prompt="产品在沙滩上的白色亚麻布上缓缓旋转，阳光在瓶身切割面上流动，海浪在背景中轻轻拍岸，8秒，广告质感" \
  --session=10 --duration=8 --ratio=16:9 --poll=60

# 生活场景视频
dreamina text2video \
  --prompt="年轻人在沙滩上奔跑，溅起水花，回头大笑，夕阳金色逆光，镜头跟拍，6秒，生活方式摄影风格" \
  --session=10 --duration=6 --ratio=16:9 --poll=60
```

### Example: 查找和继续已有会话

**场景**: 用户之前创建过会话，想继续生成

**执行**:
```bash
# 列出所有会话
dreamina session list

# 搜索
dreamina session search "brand"

# 在找到的会话中继续生成
dreamina text2video --prompt="..." --session=10 --duration=5 --poll=60
```

### Example: 查看项目视频历史

**场景**: 查看某个项目已经生成了哪些视频

**执行**:
```bash
# 列出所有任务
dreamina list_task

# 只看成功的
dreamina list_task --gen_status=success

# 按ID查看
dreamina list_task --submit_id=<id>
```

## Session Commands Reference

```bash
dreamina session create "name"     # 创建
dreamina session list              # 列表
dreamina session search "keyword"  # 搜索
dreamina text2video --prompt="..." --session=<id>  # 生成到指定会话
dreamina list_task                 # 查看历史
```

## Workflow Summary

```
新视频项目:
  session create "name" → 记录 session_id → 所有生成带 --session=<id>

继续项目:
  session list → 找到 session_id → 继续生成

查看历史:
  list_task → list_task --gen_status=success
```
