---
name: jimeng-cli-image2image
description: Provides comprehensive guidance for executing image-to-image (图生图) editing via the dreamina CLI for 即梦 models 4.0+. Image-to-image CLI requires local image files (1-10, comma-separated), only works with models 4.0 and above, and supports 2K/4K resolution only (1K not available). Use when the user has reference image(s) and wants to transform them via CLI; after an edit prompt has been approved; mentions "dreamina image2image", "图生图CLI", "编辑图片"; provides images and asks to run a transformation; or needs credit checking, task querying, or session management for image editing. This skill covers the complete CLI parameter reference including the critical --images syntax, model version restrictions, 4 standard I2I execution workflows, image file verification patterns, and error handling for common I2I-specific failures. Always use this skill when the user wants to edit images via the dreamina command line.
license: Complete terms in LICENSE.txt
---

# jimeng-cli-image2image — 即梦图生图 CLI 执行

Execute image-to-image editing via the `dreamina` CLI tool. This skill handles command construction, image file management, credit checking, task submission, polling, and result retrieval.

**This skill does NOT craft edit prompts.** Prompt crafting is handled by `jimeng-prompt-image2image`. Use that skill first, get user approval, then activate this skill for CLI execution.

## When to use this skill

Use this skill when:
- The user has reference images and an approved edit prompt to transform them
- The user asks to "edit this image" or "change this picture's style"
- The user wants to run an image-to-image transformation via CLI
- The user mentions `dreamina image2image` or 图生图

Do NOT use this skill for:
- Writing or improving edit prompts → use jimeng-prompt-image2image
- Text-to-image CLI → use jimeng-cli-text2image
- Video CLI → use jimeng-cli-text2video / jimeng-cli-image2video

## Core Execution Flow

```
1. CHECK   → dreamina user_credit                  # Always first
2. VERIFY  → Images exist and are readable
3. SUBMIT  → dreamina image2image --images ./input.png --prompt="..." --poll=0  # Async → get submit_id
4. POLL    → Agent 每 ~5 秒调用 query_result --submit_id=<id> 检查 gen_status
5. RETRIEVE → gen_status="success" → 提取结果并报告
```

## 定时查询 SOP（智能体行为规范，非 shell 死循环）

提交生成任务后，应由**智能体（AI）**负责任务状态查询，而非用 `while true` shell 脚本阻塞终端：

**Step 1 — 提交任务（一次 terminal 调用）**：
```bash
dreamina image2image --images ./input.png --prompt="改成水彩风格" --model_version=5.0 --poll=0
```
→ 解析输出中的 `submit_id`，记录下来。

**Step 2 — 智能体周期查询（多次 terminal 调用，每次单独）**：
```
每 ~5 秒执行一次: dreamina query_result --submit_id=<submit_id>
```
根据返回的 `gen_status` 做分支判断：

| gen_status | 智能体行为 |
|-----------|-----------|
| `"success"` | ✅ 提取结果 URL，报告给用户 |
| `"failed"` | ❌ 报告错误信息给用户 |
| `"querying"` | ⏳ 等待 ~5 秒后再次检查（最长等待 2 分钟） |
| 长时间无变化（>3min） | ⚠️ 报告用户询问是否继续 |

> **禁止**在 terminal 中使用 `while true; sleep 5; ...` 死循环。应由智能体在多次对话轮次中独立调用 `query_result`。

## How to use this skill

### Step 1: Verify prerequisites

**1a. Check CLI is installed and logged in:**
```bash
dreamina user_credit
```
If this fails, fix login first: `dreamina login` / `dreamina login --debug`. See FAQ section below.

**1b. Install if needed:**
```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

### Step 2: Ensure prompt and images are ready

- Edit prompt crafted by jimeng-prompt-image2image (Keep/Change framework)
- Reference images exist at known local paths
- 1-10 images supported

If no prompt exists, activate `jimeng-prompt-image2image` first.

### Step 3: Map prompt parameters to CLI arguments

| Prompt recommends | CLI parameter | Example |
|------------------|---------------|---------|
| Model 4.0+ | `--model_version=5.0` | `--model_version=5.0` |
| 2K/4K resolution | `--resolution_type=4k` | `--resolution_type=4k` |
| Aspect ratio | `--ratio=3:4` | `--ratio=3:4` |

Load `references/parameter-reference.md` for the complete parameter map.

### Step 4: Execute the generation

**Recommended (async + 智能体周期查询):**
```bash
dreamina image2image \
  --images ./photo.png \
  --prompt="保持人物面部特征和姿势不变，将照片转换为吉卜力动画风格，温暖手绘质感" \
  --model_version=5.0 \
  --resolution_type=4k \
  --poll=0
```
→ 解析获取 `submit_id`，智能体随后每 ~5 秒调用 `query_result` 检查状态。

**Quick poll (for fast edits, auto 1s polling):**
```bash
dreamina image2image --images ./photo.png --prompt="改成水彩风格" --model_version=5.0 --poll=30
```

**Background replacement:**
```bash
dreamina image2image \
  --images ./portrait.png \
  --prompt="保持人物、服装和姿势完全不变。将背景替换为阳光明媚的热带海滩。调整人物光影色温匹配海滩环境。在脚下添加沙滩阴影。" \
  --ratio=3:4 \
  --poll=30
```

**Multiple reference images:**
```bash
dreamina image2image \
  --images ./subject.png,./style.png \
  --prompt="参考第一张图的人物特征和姿势，应用第二张图的水墨画风格，保持构图不变" \
  --poll=30
```

**Async (batch):**
```bash
dreamina image2image --images ./input.png --prompt="..." --poll=0
# Save submit_id, query later
```

### Step 5: Handle results → Step 6: Handle errors

After generation completes:
- Confirm `gen_status` is `"success"`
- If using 智能体周期查询 → 每次 `query_result` 返回后智能体根据 `gen_status` 分支判断
- If `--poll` timeout → 智能体接手用 `query_result` 继续轮询

Common errors below.

| Error | Action |
|-------|--------|
| `AigcComplianceConfirmationRequired` | Authorize on dreamina website first |
| Credit insufficient | Warn user, suggest checking balance |
| Image file not found | Verify path, suggest absolute paths |
| Model <4.0 not supported | image2image requires 4.0+ |

## Key Parameters Quick Reference

| Parameter | Required | Values | Default |
|-----------|----------|--------|---------|
| `--images` | **Yes** | 1-10 local file paths, comma-separated | — |
| `--prompt` | **Yes** | String (Chinese preferred, Keep/Change style) | — |
| `--ratio` | No | 21:9, 16:9, 3:2, 4:3, 1:1, 3:4, 2:3, 9:16 | 1:1 |
| `--model_version` | No | 4.0, 4.1, 4.5, 5.0 | 5.0 |
| `--resolution_type` | No | 2k, 4k (1k NOT supported) | 2k |
| `--poll` | No | Seconds (0 = async, polls every 1s) | 0 |

**Poll behavior**: `--poll=N` polls every 1 second for up to N seconds. Timeout returns "querying" intermediate result with submit_id.

## Model Selection

| Model | Official Model ID | Best For |
|-------|-------------------|----------|
| **5.0** (default) | `doubao-seedream-5-0-260128` | Latest flagship, all I2I tasks |
| 4.5 | `doubao-seedream-4-5-251128` | Artistic style transfer, landscapes |
| 4.1 | — | Portrait editing, poster layout, multi-round edits |
| 4.0 | `doubao-seedream-4-0-250828` | Reliable baseline |

> I2I requires 4.0+. Models 3.0/3.1 are NOT available for image-to-image.

## Essential CLI Commands

```bash
# Credit & auth
dreamina user_credit                          # Check credits
dreamina login                                # Login
dreamina login --debug                        # Debug login
dreamina relogin                              # Switch accounts
dreamina logout                               # Clear credentials

# Image-to-image generation
dreamina image2image --images ./x.png --prompt="改成水彩风格" --poll=30
dreamina image2image --images ./a.png,./b.png --prompt="combine style of first with subject of second"
dreamina image2image --images ./x.png --prompt="..." --model_version=5.0 --resolution_type=4k --poll=30

# Task management
dreamina query_result --submit_id=<id>
dreamina query_result --submit_id=<id> --download_dir=./output
dreamina list_task
dreamina list_task --gen_status=success
dreamina list_task --submit_id=<id>

# Session
dreamina session create "edit-project"
dreamina session list
```

## FAQ (from official documentation)

**Q: Login succeeds but generation commands still fail?**
A: (1) Run `dreamina user_credit` — if this fails, login/config is the issue. (2) Check `~/.dreamina_cli/` exists. Note: `config.toml`, `credential.json`, `tasks.db` may NOT be present after Docker-based login (auth stored ephemerally). Do NOT test generation until `user_credit` works.

**Q: Browser login flow is stuck?**
A: Use `dreamina login --debug` for detailed debug output.

**Q: Async task shows no final result?**
A: Use `--poll=N` for auto-waiting. If timeout, save submit_id and query manually.

**Q: How to switch accounts?**
A: `dreamina relogin` clears login state and starts new flow.

**Q: How to completely clear local login info?**
A: `dreamina logout` clears `credential.json` only. `config.toml` and `tasks.db` are preserved.

## Gotchas

1. **Always check credits first** — never run generation without `dreamina user_credit`
2. **Prompt goes through prompt skill first** — don't craft edit prompts here. Route to jimeng-prompt-image2image
3. **Images must be local files** — `--images` requires local paths, not URLs. Verify files exist before submitting
4. **I2I requires model 4.0+** — 3.0/3.1 are NOT supported for image-to-image
5. **Resolution 2k/4k only** — 1k is NOT available for I2I
6. **Max 10 images** — comma-separated: `--images ./a.png,./b.png,./c.png`
7. **`--poll` polls every 1 second** — timeout returns "querying" (not failure), use `query_result` to check later
8. **Edit prompt style matters** — use Keep/Change framework from jimeng-prompt-image2image. Undescribed elements may change unexpectedly
9. **`~/.dreamina_cli/` directory** — may contain config.toml, credential.json, tasks.db after native (non-Docker) login. In Docker setups, these files may be absent (auth stored ephemerally). Don't delete the directory
10. **图片类不支持 VIP 通道** — dreamina image2image 的 `--model_version` 参数只有 `4.0, 4.1, 4.5, 4.6, 5.0`，没有 `_vip` 变体。VIP 通道仅限视频类子命令。如需确认 CLI 实际支持的参数，运行 `dreamina image2image -h`——CLI help 输出是唯一真相来源，技能文档可能滞后
11. **不要写 shell 死循环做任务轮询** — 提交任务时用 `--poll=0` 获取 submit_id，然后由智能体在对话轮次中每 ~5 秒调用一次 `query_result`。禁止 `while true; sleep 5;` 阻塞终端。智能体需根据 gen_status 做分支判断（继续等/报结果/通知超时）

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `references/parameter-reference.md` | Complete I2I CLI parameter reference | When mapping prompt specs to CLI arguments |
| `references/model-guide.md` | Model selection for I2I tasks | When choosing model version |
| `references/workflow-patterns.md` | Execution patterns, error handling, image verification | When executing complex generations |
| `examples/basic-generation.md` | Common I2I generation flows | Default — most common use case |
| `examples/batch-generation.md` | Multi-image batch editing | User wants multiple edits |
| `examples/async-generation.md` | Async submit + poll patterns | Non-blocking or long edits |
| `examples/session-workflow.md` | Session-based project organization | Organized project workflow |
