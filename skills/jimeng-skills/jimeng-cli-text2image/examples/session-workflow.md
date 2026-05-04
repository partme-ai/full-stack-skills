# Session Workflow — 会话项目管理

## Instructions

会话（Session）用于组织多次生成为一个项目。适合系列创作、品牌项目、需要追溯的多次生成。

## Examples

### Example: 创建项目会话并生成

**场景**: 用户要为一个新产品拍摄系列电商图

**执行**:
```bash
# Step 1: 创建项目会话
dreamina session create "spring-collection-2026"
# 输出: Session created: id=42, name="spring-collection-2026"

# Step 2: 在会话中连续生成
dreamina user_credit

dreamina text2image \
  --prompt="米色风衣平铺拍摄，纯白背景，柔和自然光，服装电商摄影，2K" \
  --session=42 --ratio=1:1 --model_version=4.6 --poll=30

dreamina text2image \
  --prompt="米色风衣模特上身效果，都市街景背景，自然行走姿态，时尚电商摄影，2K" \
  --session=42 --ratio=3:4 --model_version=4.6 --poll=30

dreamina text2image \
  --prompt="米色风衣细节特写，面料纹理，纽扣和缝线，微距产品摄影，2K" \
  --session=42 --ratio=1:1 --model_version=4.6 --poll=30
```

### Example: 查找已有会话

**场景**: 用户之前创建过会话，想继续在同一个会话中生成

**执行**:
```bash
# 列出所有会话
dreamina session list
# 输出: id=42  spring-collection-2026
#       id=15  autumn-lookbook

# 搜索特定会话
dreamina session search "spring"

# 在找到的会话中继续生成
dreamina text2image --prompt="..." --session=42 --ratio=1:1 --poll=30
```

### Example: 查看项目生成历史

**场景**: 用户想查看某个会话中已经生成了哪些图

**执行**:
```bash
# 列出所有成功的任务
dreamina list_task --gen_status=success
```

## Session Commands Reference

```bash
# 创建
dreamina session create "project-name"

# 列表
dreamina session list

# 搜索
dreamina session search "keyword"

# 生成时指定会话
dreamina text2image --prompt="..." --session=<id>

# 查看任务历史
dreamina list_task
dreamina list_task --gen_status=success
```

## Workflow Summary

```
新建项目:
  session create "name" → 记录 session_id → 所有生成带 --session=<id>

继续项目:
  session list → 找到 session_id → 继续生成

查看历史:
  list_task → 筛选状态
```
