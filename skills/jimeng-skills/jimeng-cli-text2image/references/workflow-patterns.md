# Workflow Patterns — 执行工作流与错误处理

> CLI 执行的标准工作流模式和常见错误处理方案。

---

## 工作流 1：标准同步生成（最常用）

**场景**: 用户有一个写好的提示词，要直接生成图片

**步骤**:
```bash
# 1. 检查额度
dreamina user_credit

# 2. 提交生成（同步等待30秒）
dreamina text2image \
  --prompt="<prompt>" \
  --ratio=16:9 \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=30

# 3. 结果已自动返回，报告给用户
```

**适用**: 大多数单张生成场景

---

## 工作流 2：异步批量生成

**场景**: 用户要生成多张图，不想逐个等待

**步骤**:
```bash
# 1. 检查额度
dreamina user_credit

# 2. 逐个提交（不等待）
dreamina text2image --prompt="<prompt1>" --ratio=1:1 --poll=0
# 保存 submit_id_1
dreamina text2image --prompt="<prompt2>" --ratio=1:1 --poll=0
# 保存 submit_id_2
dreamina text2image --prompt="<prompt3>" --ratio=1:1 --poll=0
# 保存 submit_id_3

# 3. 轮询查询所有任务
dreamina query_result --submit_id=<id1>
dreamina query_result --submit_id=<id2>
dreamina query_result --submit_id=<id3>
```

**适用**: 3+张图、不想串联等待

---

## 工作流 3：会话项目管理

**场景**: 用户有一个项目，想在同一個会话中组织多次生成

**步骤**:
```bash
# 1. 创建或查找会话
dreamina session create "autumn-collection"
# 假设返回 session_id=42

# 2. 在会话中连续生成
dreamina text2image --prompt="..." --session=42 --ratio=3:4 --poll=30
dreamina text2image --prompt="..." --session=42 --ratio=3:4 --poll=30

# 3. 查看会话中的所有任务
dreamina list_task --gen_status=success
```

**适用**: 系列创作、品牌项目、需要追溯的多次生成

---

## 工作流 4：先查后改（与提示词技能协作）

**场景**: 提示词技能写好提示词，用户批准后执行

**步骤**:
```
1. jimeng-prompt-text2image 创建提示词 → 用户批准
2. jimeng-cli-text2image 执行：
   a. dreamina user_credit
   b. 将提示词的建议参数映射到CLI参数
   c. dreamina text2image --prompt="<approved prompt>" --ratio=... --model_version=...
   d. 报告结果
```

**适用**: 标准的提示词→执行协作流程

---

## 错误处理

### 错误：额度不足

```
Error: credit insufficient / 额度不足
```

**响应**: 告知用户剩余额度，建议充值或切换到免费模型（如 3.0）

### 错误：模型需要首次授权

```
Error: AigcComplianceConfirmationRequired
```

**响应**: 告知用户该模型需要先在即梦网页端授权。指导步骤：
1. 打开 https://jimeng.jianying.com
2. 找到对应模型的使用入口
3. 完成合规确认
4. 重新执行 CLI 命令

### 错误：CLI 未安装

```
dreamina: command not found
```

**响应**: 提供安装命令：
```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

### 错误：未登录

```
Error: authentication required / not logged in
```

**响应**: 提供登录命令：
```bash
dreamina login          # 浏览器OAuth
dreamina login --headless  # 扫码登录
```

### 错误：参数无效

```
Error: invalid parameter / unknown flag
```

**响应**: 先检查 `dreamina text2image -h` 获取最新参数列表，参数可能随CLI版本变化。

### 错误：生成超时

```
Error: task timeout / poll timeout
```

**响应**: 不要立即重试。先用 `dreamina query_result --submit_id=<id>` 检查任务是否仍在进行中。如在进行中，增加 `--poll` 的时间重试。

---

## 额度管理

```bash
# 始终在任何生成前检查
dreamina user_credit

# 解读输出
# 如果余额低 → 警告用户
# 如果余额为0 → 阻止生成，提示充值
# 如果余额充足 → 继续
```

**额度消耗参考**:
- 2K 图像: ~1-2 额度/张
- 4K 图像: ~3-5 额度/张
- 视频: 显著高于图像

---

## 登录与配置故障排查

### 登录自检
```bash
# 最可靠的自检方式
dreamina user_credit
# 如果返回JSON余额信息 → 登录正常
# 如果失败 → 登录或配置有问题
```

### 登录失败排查流程
```
1. dreamina login --debug          # 打印调试信息
2. ls -la ~/.dreamina_cli/         # 检查配置文件
3. cat ~/.dreamina_cli/config.toml # 确认内容正确
4. dreamina user_credit            # 重新验证
```

### 关键文件
| 文件 | 说明 |
|------|------|
| `~/.dreamina_cli/config.toml` | 配置文件 |
| `~/.dreamina_cli/credential.json` | 登录凭证 |
| `~/.dreamina_cli/tasks.db` | 任务记录 |

### 账号管理
```bash
dreamina relogin   # 切换账号（清除+重新登录）
dreamina logout    # 清除凭证（保留config和tasks.db）
```

## 最佳实践

1. **生成前必须检查额度** — 每次对话中的首次生成前运行 `dreamina user_credit`。如果 `user_credit` 失败，不要继续，先修登录
2. **同步优先** — 对单张生成使用 `--poll=30`，避免用户等待和后续轮询的复杂性
3. **`--poll` 的行为** — 每秒轮询1次，超时返回 "querying" 中间结果（不是失败），可用 `query_result` 后续查询
4. **参数按需添加** — 不要硬编码所有参数。只添加与默认值不同的参数
5. **检查 help** — 参数可能随版本变化，不确定时运行 `dreamina text2image -h`
6. **保存 submit_id** — 异步模式下务必保存并告知用户 submit_id
7. **不要自动重试** — 生成失败时，先诊断原因再决定是否重试
