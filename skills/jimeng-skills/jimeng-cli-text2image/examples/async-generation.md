# Async Generation — 异步生成与结果查询

## Instructions

异步生成适用于：不需要立即看到结果的场景、批量提交、长时间4K生成。使用 `--poll=0` 提交后立即获得 `submit_id`，稍后通过 `query_result` 查询。

## Examples

### Example: 标准异步提交+查询

**场景**: 用户提交一张4K图，不想等待，稍后查看结果

**执行**:
```bash
# Step 1: 检查额度
dreamina user_credit

# Step 2: 提交（不等待）
dreamina text2image \
  --prompt="星空下的雪山，银河横贯天际，长曝光效果，冷蓝与暖金对比，国家地理风格" \
  --ratio=21:9 \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=0
# 输出: Task submitted. submit_id: xyz-789

# 告知用户: "任务已提交 (submit_id: xyz-789)，稍后可以用以下命令查询结果：
# dreamina query_result --submit_id=xyz-789"
```

**稍后查询**:
```bash
# 用户或Agent在几分钟后查询
dreamina query_result --submit_id=xyz-789

# 可能输出:
# Status: processing  → 还在生成中，稍后再查
# Status: success     → 生成完成，报告结果
# Status: failed      → 生成失败，查看错误原因
```

### Example: 批量异步+统一查询

**场景**: 一次提交10张不同主题的图，全异步

**执行**:
```bash
dreamina user_credit

# 提交10个任务，收集ID
ids=()
for prompt in "提示词1" "提示词2" ... "提示词10"; do
  output=$(dreamina text2image --prompt="$prompt" --ratio=1:1 --poll=0)
  id=$(echo "$output" | grep -oP 'submit_id: \K\S+')
  ids+=("$id")
  echo "Submitted: $id"
done

# 等待一段时间后查询
for id in "${ids[@]}"; do
  echo "=== Querying $id ==="
  dreamina query_result --submit_id="$id"
done
```

### Example: 失败重试

**场景**: 异步任务失败，需要诊断后决定是否重试

**执行**:
```bash
# 查询发现失败
dreamina query_result --submit_id=xyz-789
# Status: failed
# Error: AigcComplianceConfirmationRequired

# 诊断：模型需要首次Web授权
# 告知用户去网页端授权后重试

# 授权完成后，用同样的提示词重新提交
dreamina text2image --prompt="<same prompt>" --ratio=21:9 --poll=30
```

## Key Commands

```bash
# 查询单个任务
dreamina query_result --submit_id=<id>

# 查询并下载
dreamina query_result --submit_id=<id> --download_dir=./output

# 列出所有任务
dreamina list_task

# 只列成功的
dreamina list_task --gen_status=success

# 只列处理中的
dreamina list_task --gen_status=processing
```
