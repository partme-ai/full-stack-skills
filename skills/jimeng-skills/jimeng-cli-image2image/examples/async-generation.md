# Async I2I Generation — 异步图生图

## Examples

### Example: 标准异步+查询

**执行**:
```bash
# 提交
dreamina user_credit
dreamina image2image \
  --images ./photo.png \
  --prompt="保持人物特征和姿势，将写实照片转换为赛博朋克风格，蓝紫霓虹色调" \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=0
# 输出: submit_id: i2i-async-001

# 告知用户: "任务已提交 (i2i-async-001)，稍后查询：dreamina query_result --submit_id=i2i-async-001"

# 几分钟后查询
dreamina query_result --submit_id=i2i-async-001
```

### Example: 查询+下载

**执行**:
```bash
dreamina query_result --submit_id=i2i-async-001 --download_dir=./edited
```

### Example: 批量异步查询

**执行**:
```bash
# 查看所有I2I任务状态
dreamina list_task

# 只看成功的
dreamina list_task --gen_status=success

# 按ID查
dreamina list_task --submit_id=i2i-async-001
```
