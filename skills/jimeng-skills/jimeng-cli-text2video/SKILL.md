---
name: jimeng-cli-text2video
description: Provides comprehensive guidance for executing text-to-video generation via the dreamina CLI for 即梦 Seedance 2.0 models. Video generation via CLI requires longer poll times than images (60-180 seconds recommended), supports 4-15 second durations, and uses 720P resolution. Use when the user wants to run an approved video prompt through the CLI; mentions "dreamina text2video", "命令行生视频", "生成视频"; asks to run, submit, or execute a video prompt; or needs credit checking, task querying, or session management for video generation. This skill covers the complete parameter reference for video-specific options (duration, video_resolution, model_version), the Seedance 2.0 model selection guide comparing speed vs quality, 4 standard video execution workflows, and error handling patterns from official documentation. Always use this skill when the user wants to generate videos from text via the dreamina command line.
license: Complete terms in LICENSE.txt
---

# jimeng-cli-text2video — 即梦文生视频 CLI 执行

Execute text-to-video generation via the `dreamina` CLI tool using Seedance 2.0 models. This skill handles command construction, credit management, task submission, polling, and result retrieval.

**This skill does NOT craft prompts.** Video prompt crafting is handled by `jimeng-prompt-text2video`. Use that skill first, get user approval, then activate this skill for CLI execution.

## When to use this skill

Use this skill when:
- The user has an approved video prompt and wants to generate the video
- The user asks to "generate this video" or "run this video prompt"
- The user needs to check credits, query video task status, or download results
- The user mentions `dreamina text2video` CLI commands explicitly

Do NOT use this skill for:
- Writing or improving video prompts → use jimeng-prompt-text2video
- Image-to-video CLI → use jimeng-cli-image2video
- Image generation CLI → use jimeng-cli-text2image

## Core Execution Flow

```
1. CHECK   → dreamina user_credit                  # Always first — check credits
2. SUBMIT  → dreamina text2video --prompt="..." --duration=N --poll=0  # Async → get submit_id
3. POLL    → Agent 每 ~5 秒手动调用 query_result --submit_id=<id> 检查 gen_status
4. RETRIEVE → gen_status="success" → 提取结果并报告
```

## 定时查询 SOP（智能体行为规范，非 shell 死循环）

提交生成任务后，应由**智能体（AI）**负责任务状态查询，而非用 `while true` shell 脚本阻塞终端：

### 步骤

**Step 1 — 提交任务（一次 terminal 调用）**：
```bash
dreamina text2video --prompt="..." --duration=5 --ratio=16:9 --model_version=seedance2.0fast_vip --poll=0
```
→ 解析输出中的 `submit_id`，记录下来。

**Step 2 — 智能体周期查询（多次 terminal 调用，每次单独）**：
```
每 ~5 秒执行一次: dreamina query_result --submit_id=<submit_id>
```
根据返回的 `gen_status` 做分支判断：

| gen_status | 智能体行为 |
|-----------|-----------|
| `"success"` | ✅ 提取视频 URL，报告给用户 |
| `"failed"` | ❌ 报告错误信息给用户 |
| `"querying"` | ⏳ 等待 ~5 秒后再次调用 query_result（最长等待：视频 15 分钟） |
| 长时间无变化（>20min） | ⚠️ 主动报告给用户，询问是否要继续等 |

> **禁止**在 terminal 中使用 `while true; sleep 5; ...` 死循环。应由智能体在多次对话轮次中独立调用 `query_result`。

### 示例（智能体自身逻辑）

```
# Turn 1
terminal: dreamina text2video --prompt="..." --poll=0
→ parse: submit_id = "abc-123"
→ tell user: "已提交视频任务，submit_id=abc-123，5秒后检查结果"

# Turn 2 (after ~5s)
terminal: dreamina query_result --submit_id=abc-123
→ gen_status = "querying"
→ tell user: "视频生成中（通常2-15分钟），5秒后再检查"

# Turn 3 (after ~5s) ... repeat until success
```

## How to use this skill

### Step 1: Verify prerequisites

**1a. Check CLI is installed:**
```bash
dreamina -h
```
If not installed:
```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

**1b. Check login status and credits (mandatory before every generation):**
```bash
dreamina user_credit
```
This is the definitive self-check. If it returns JSON with credit info, login and environment are working. **Video generation consumes significantly more credits than images** — warn user if balance is low.

If login needed:
```bash
dreamina login              # Opens browser for OAuth
dreamina login --debug      # Debug mode — prints callback URL for troubleshooting
dreamina login --headless   # QR code mode — scan with Douyin app
```

Account management:
```bash
dreamina relogin            # Switch accounts
dreamina logout             # Clear credentials (keeps config.toml and tasks.db)
```

**1c. Check config (if login issues):**
```bash
ls -la ~/.dreamina_cli/
```
> ⚠️ Note: `config.toml`, `credential.json`, `tasks.db` may not exist — especially in Docker. Auth state can be ephemeral. Use `dreamina user_credit` as the definitive check.

### Step 2: Ensure prompt is ready

This skill requires a production-ready video prompt. The prompt should:
- Be crafted using jimeng-prompt-text2video methodology
- Include explicit motion description and camera movement
- Be reviewed and approved by the user
- Have duration and ratio recommendations

If no prompt exists, activate `jimeng-prompt-text2video` first.

### Step 3: Map prompt parameters to CLI arguments

| Prompt recommends | CLI parameter | Example |
|------------------|---------------|---------|
| Duration (8s) | `--duration=8` | `--duration=8` |
| Aspect ratio (16:9) | `--ratio=16:9` | `--ratio=16:9` |
| Camera: push in | Already in prompt text | Camera terms go in `--prompt` |
| Quality: high | `--model_version=seedance2.0` | `--model_version=seedance2.0` |

Load `references/parameter-reference.md` for the complete parameter map.

### Step 4: Execute the generation

**Recommended (async + 智能体周期查询):**
```bash
dreamina text2video \
  --prompt="镜头缓缓推进，一个女孩在森林里缓步前行，裙摆摇曳，阳光透过树冠洒在她身上" \
  --duration=8 \
  --ratio=16:9 \
  --model_version=seedance2.0fast_vip \
  --poll=0
```
→ 解析获取 `submit_id`，智能体随后每 ~5 秒调用 `query_result` 检查状态。

**Quick generation (defaults, 5s poll fallback):**
```bash
dreamina text2video --prompt="..." --poll=60
# Defaults: duration=5s, ratio=16:9, model=seedance2.0fast_vip, resolution=720P
```

**High quality (slower):**
```bash
dreamina text2video \
  --prompt="..." \
  --duration=10 \
  --model_version=seedance2.0 \
  --poll=120
```

**Async (batch or non-blocking):**
```bash
dreamina text2video --prompt="..." --poll=0
# Save submit_id, query later:
dreamina query_result --submit_id=<id>
```

### Step 5: Handle results

- If using the 5s 智能体周期查询 → 每次 `query_result` 返回后智能体根据 `gen_status` 做分支判断
- If `--poll` completes within timeout → result returned immediately
- If `--poll` times out → returns "querying" intermediate status with submit_id; use 智能体周期查询继续检查
- Report output file path and video details to the user

### Step 6: Handle errors

| Error | Meaning | Action |
|-------|---------|--------|
| `AigcComplianceConfirmationRequired` | Model needs first-time web authorization | Guide user to authorize on dreamina website, then retry |
| Credit insufficient | Not enough balance for video | Video costs more — suggest checking balance or using shorter duration |
| `dreamina: command not found` | CLI not installed | Run install command |
| Authentication error | Not logged in | Run `dreamina login` |
| Poll timeout with "querying" | Video still generating | Not a failure — use `query_result` later |

## Key Parameters Quick Reference

| Parameter | Required | Values | Default |
|-----------|----------|--------|---------|
| `--prompt` | **Yes** | String with motion + camera description | — |
| `--duration` | No | 4-15 (seconds) | 5 |
| `--ratio` | No | 1:1, 3:4, 16:9, 4:3, 9:16, 21:9 | 16:9 |
| `--video_resolution` | No | 720P (Seedance 2.0) | 720P |
| `--model_version` | No | seedance2.0, seedance2.0fast, seedance2.0_vip, seedance2.0fast_vip | seedance2.0fast |
| `--session` | No | Integer session ID | 0 |
| `--poll` | No | Seconds (0 = async, polls every 1s) | 0 |

**Poll behavior**: `--poll=N` polls every 1 second for up to N seconds. If task completes within N → result returned. If N seconds elapse → "querying" intermediate result returned with submit_id.

## Model Selection Guide

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| **seedance2.0fast** (default) | Fast (~2-5 min) | Good | Standard | Iteration, quick tests, general use |
| seedance2.0 | Slow (~5-15 min) | Excellent | Standard | Final output, high quality |
| seedance2.0fast_vip | Fast | Good | VIP | VIP fast generation |
| seedance2.0_vip | Slow | Excellent | VIP | VIP high quality |

**Recommendation (VIP 账户优先)**：用户当前账户 VIP 等级为 maestro，应优先使用 VIP 通道以获得更快速度和更高并发：
- `seedance2.0fast_vip` — **首选**：快速迭代，VIP 通道优先
- `seedance2.0_vip` — 高质量最终输出，VIP 通道优先
- `seedance2.0fast` — 备用（非 VIP 通道，标准速度）
- `seedance2.0` — 备用高质量（非 VIP 通道）

## Essential CLI Commands

```bash
# Credit & auth
dreamina user_credit                          # Check credit balance
dreamina login                                # Login (OAuth browser)
dreamina login --debug                        # Login with debug output

# Video generation
dreamina text2video --prompt="..." --duration=8 --poll=60
dreamina text2video --prompt="..." --duration=5 --ratio=9:16 --poll=60
dreamina text2video --prompt="..." --model_version=seedance2.0 --poll=120

# Task management
dreamina query_result --submit_id=<id>        # Check task status
dreamina query_result --submit_id=<id> --download_dir=./videos  # Query + download
dreamina list_task                            # List all tasks
dreamina list_task --gen_status=success       # Filter by status
dreamina list_task --submit_id=<id>           # Filter by submit_id

# Session management
dreamina session create "video-project"       # Create session
dreamina session list                         # List sessions
```

## Duration-to-Action Guide

| Duration | Action Complexity | Example |
|----------|------------------|---------|
| 4-6s | One clear action | "转身微笑" "杯子被举起" |
| 7-10s | Action with development | "从远处走来，经过镜头，渐行渐远" |
| 11-15s | 2-3 stage progression | "推门进入 → 环顾四周 → 走向窗边" |

> Match action complexity to duration. A 5s clip with a 3-stage action plan will look rushed.

## FAQ (from official documentation)

**Q: Login succeeds but generation commands still fail?**
A: (1) Verify `~/.dreamina_cli/config.toml` exists; (2) Run `dreamina user_credit` — if this fails, login/config is the issue. Do NOT test generation commands until `user_credit` works.

**Q: Browser login flow is stuck?**
A: Use `dreamina login --debug` for detailed debug output.

**Q: Async task shows no final result?**
A: Use `--poll=N` for auto-waiting. If timeout, save submit_id from intermediate result and query: `dreamina query_result --submit_id=<id>`.

**Q: How to switch accounts?**
A: `dreamina relogin` clears login state and starts new flow.

## Gotchas

1. **Always check credits first** — video generation costs significantly more than images. Run `dreamina user_credit` before every generation session
2. **Prompt goes through prompt skill first** — don't craft video prompts here. Route to jimeng-prompt-text2video
3. **`--poll` polls every 1 second** — `--poll=60` means up to 60 polling attempts. Timeout returns "querying" (not failure)
4. **Video takes much longer than images** — expect 2-15 minutes. Use `--poll=120` for high-quality models
5. **720P is the only resolution for Seedance 2.0** — written as `720P` (capital P in official docs). 1080p only available with legacy models
6. **Match duration to action** — don't cram a 3-stage narrative into a 5-second clip
7. **Default model is seedance2.0fast** — good quality, faster. Use seedance2.0 for final renders
8. **Some models need web auth first** — if `AigcComplianceConfirmationRequired`, authorize on dreamina website
9. **VIP 账户优先使用 VIP 通道** — `seedance2.0fast_vip` 和 `seedance2.0_vip` 有独立 VIP 队列，速度更快、并发更高。账户 VIP 等级为 maestro，应默认为 `seedance2.0fast_vip`
10. **不要写 shell 死循环做任务轮询** — 提交任务时用 `--poll=0` 获取 submit_id，然后由智能体在对话轮次中每 ~5 秒调用一次 `query_result`。禁止 `while true; sleep 5;` 阻塞终端。智能体需根据 gen_status 做分支判断（继续等/报结果/通知超时）
11. **`~/.dreamina_cli/` directory** — may contain config.toml, credential.json, tasks.db after native (non-Docker) login. In Docker setups, these files may be absent (auth stored ephemerally). Don't delete

## Available Resources

| Resource | Description | When to Load |
|----------|-------------|--------------|
| `references/parameter-reference.md` | Complete CLI parameter reference for text2video | When mapping prompt specs to CLI arguments |
| `references/model-guide.md` | Detailed Seedance 2.0 model comparison | When choosing model for quality/speed/cost |
| `references/workflow-patterns.md` | Standard execution patterns, error handling, async workflows | When executing complex or multi-step generations |
| `references/official-doc-vip-guide.md` | Official documentation excerpt on VIP channel support, version history, 1080P | When user asks about VIP, or when confirming VIP model support |
| `examples/basic-generation.md` | Simple single-video generation flows | Default — most common use case |
| `examples/batch-generation.md` | Multi-video batch patterns | User wants multiple videos |
| `examples/async-generation.md` | Async submit + poll patterns for video | Long video generations or non-blocking |
| `examples/session-workflow.md` | Session-based video project organization | User wants organized project workflow |
