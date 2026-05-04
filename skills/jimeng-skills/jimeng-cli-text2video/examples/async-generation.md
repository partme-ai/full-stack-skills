# Async Video Generation — 异步视频生成与结果查询

## Instructions

视频生成比图像慢得多（数分钟到十几分钟），异步模式是最实用的选择。使用 `--poll=0` 提交后获得 `submit_id`，稍后通过 `query_result` 查询。

## Examples

### Example: 标准异步提交+查询

**场景**: 提交一个10秒高质量视频，不等待

**执行**:
```bash
# Step 1: 检查额度
dreamina user_credit

# Step 2: 异步提交
dreamina text2video \
  --prompt="镜头从高空缓缓下降穿过云层，展现雪山之巅的壮丽全景，金色夕阳照亮山峰，云雾在脚下翻滚，10秒，航拍纪录片风格" \
  --duration=10 \
  --model_version=seedance2.0 \
  --poll=0
# 输出: Task submitted. submit_id: video-xyz-789

# 告知用户: "视频任务已提交 (submit_id: video-xyz-789)，预计需要5-15分钟。
# 稍后可用 dreamina query_result --submit_id=video-xyz-789 查询结果"
```

**10分钟后查询**:
```bash
dreamina query_result --submit_id=video-xyz-789

# 可能输出:
# Status: processing  → 还在生成中
# Status: success     → 生成完成！
# Status: failed      → 查看错误信息
```

### Example: 查询并下载

**场景**: 异步任务完成，下载结果到本地

**执行**:
```bash
dreamina query_result --submit_id=video-xyz-789 --download_dir=./videos
```

### Example: 多个异步视频+轮询脚本

**场景**: 提交一批视频，用一个简单脚本轮询全部

**执行**:
```bash
dreamina user_credit

# 提交批次
ids=()
for prompt in "提示词A" "提示词B" "提示词C"; do
  output=$(dreamina text2video --prompt="$prompt" --duration=5 --poll=0)
  id=$(echo "$output" | grep -oP 'submit_id: \K\S+')
  ids+=("$id")
  echo "Submitted: $id — $prompt"
done

# 等待几分钟后查询
for id in "${ids[@]}"; do
  echo "=== $id ==="
  dreamina query_result --submit_id="$id"
done
```

## Key Commands

```bash
# 查询单个
dreamina query_result --submit_id=<id>

# 查询+下载
dreamina query_result --submit_id=<id> --download_dir=./videos

# 列出所有任务
dreamina list_task

# 只列成功的视频
dreamina list_task --gen_status=success

# 按ID筛选
dreamina list_task --submit_id=<id>
```

## Async vs Poll Summary

| 方式 | 命令 | 适用场景 |
|------|------|---------|
| 同步短轮询 | `--poll=60` | 5秒视频，fast模型 |
| 同步长轮询 | `--poll=180` | 10-15秒视频，slow模型 |
| 异步 | `--poll=0` + `query_result` | 批量提交、非阻塞 |
