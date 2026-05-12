# Workflow Patterns — 视频生成执行工作流与错误处理

> CLI 视频生成的标准工作流模式和常见错误处理方案。

---

## 工作流 1：标准同步视频生成（最常用）

**场景**: 用户有写好的视频提示词，要直接生成

**步骤**:
```bash
# 1. 检查额度（视频消耗大，务必检查）
dreamina user_credit

# 2. 提交生成（视频生成慢，至少 --poll=60）
dreamina text2video \
  --prompt="<video prompt with motion + camera>" \
  --duration=8 \
  --ratio=16:9 \
  --model_version=seedance2.0fast \
  --poll=60

# 3. 如果 poll 超时（返回 querying 状态）
dreamina query_result --submit_id=<id>

# 4. 报告结果给用户
```

---

## 工作流 2：高质量最终输出

**场景**: 提示词已验证，需要最高质量的最终视频

**步骤**:
```bash
dreamina user_credit

# 使用 seedance2.0 + 长 poll
dreamina text2video \
  --prompt="<final prompt>" \
  --duration=10 \
  --model_version=seedance2.0 \
  --poll=180

# 如果 180 秒仍超时（15秒高质量视频可能更慢）
dreamina query_result --submit_id=<id> --download_dir=./output
```

---

## 工作流 3：异步批量视频

**场景**: 用户要生成多个视频，并行提交

**步骤**:
```bash
dreamina user_credit

# 逐个异步提交
dreamina text2video --prompt="<prompt1>" --duration=5 --poll=0
# → submit_id: vid-001
dreamina text2video --prompt="<prompt2>" --duration=5 --poll=0
# → submit_id: vid-002
dreamina text2video --prompt="<prompt3>" --duration=8 --poll=0
# → submit_id: vid-003

# 等待一段时间后统一查询
dreamina query_result --submit_id=vid-001
dreamina query_result --submit_id=vid-002
dreamina query_result --submit_id=vid-003
```

**适用**: 3+个视频、不想串联等待

---

## 工作流 4：与提示词技能协作

**场景**: jimeng-prompt-text2video 写好提示词，用户批准后执行

**步骤**:
```
1. jimeng-prompt-text2video 创建视频提示词（含运镜+时长建议） → 用户批准
2. jimeng-cli-text2video 执行：
   a. dreamina user_credit
   b. 映射参数：时长 → --duration, 比例 → --ratio
   c. dreamina text2video --prompt="<approved>" --duration=N --ratio=X:Y --poll=60
   d. 报告结果或 submit_id
```

---

## 错误处理

### 错误：额度不足

```
Error: credit insufficient
```

**响应**: 视频消耗远大于图像。告知用户余额，建议：
- 缩短 duration 降低消耗
- 使用 seedance2.0fast（与 slow 模型相同额度成本）
- 充值

### 错误：模型需要首次授权

```
Error: AigcComplianceConfirmationRequired
```

**响应**: 部分 Seedance 模型首次使用需要网页授权。
1. 打开 https://jimeng.jianying.com
2. 找到 Seedance 2.0 使用入口
3. 完成合规确认
4. 重新执行 CLI 命令

### 错误：CLI 未安装 / 未登录

```
dreamina: command not found
Error: authentication required
```

**响应**:
```bash
# 安装
curl -fsSL https://jimeng.jianying.com/cli | bash

# 登录
dreamina login
dreamina login --debug  # 如果浏览器登录卡住
```

### 错误：参数无效

```
Error: invalid parameter
```

**响应**: 运行 `dreamina text2video -h` 获取最新参数。参数可能随版本变化。

### 错误：轮询超时（非真正错误）

```
Status: querying (poll timeout)
```

**响应**: 这不是失败。视频生成时间可能超过 `--poll` 设置。用 `dreamina query_result --submit_id=<id>` 继续查询。

---

## 登录与配置故障排查

```bash
# 自检
dreamina user_credit

# 如果失败
dreamina login --debug          # 调试模式
ls -la ~/.dreamina_cli/         # 检查配置文件
cat ~/.dreamina_cli/config.toml # 确认内容正确

# 账号管理
dreamina relogin   # 切换账号
dreamina logout    # 清除凭证
```

---

## 最佳实践

1. **视频生成前务必检查额度** — 视频消耗远大于图像，`dreamina user_credit` 是每次生成前的必须步骤
2. **--poll 至少 60 秒** — 视频生成比图像慢得多。5秒视频 = 至少60秒 poll；10秒视频 = 至少120秒
3. **fast 模型用于迭代，slow 用于最终** — 日常迭代用 seedance2.0fast，最终输出用 seedance2.0
4. **轮询超时不等于失败** — 超时返回 submit_id，用 query_result 后续查询
5. **运镜描述写在 prompt 里** — CLI 没有单独的 camera 参数，运镜是提示词的一部分
6. **参数按需添加** — 只传与默认值不同的参数。不确定时运行 `dreamina text2video -h`
