# 宿主兼容性说明（Host Compatibility）

`full-stack-skills` 以**标准 Agent Skills**（含 `SKILL.md` 的目录）形式发布技能，通过
`npx skills add` 安装到任何遵循该规范的宿主。

> **历史说明**：本仓库早期版本包含一个独立的适配器 CLI（`fskill` 命令与 `adapters/` 目录），
> 用于向非标准宿主导出专有包装物（Cursor rule、Trae plugin、Qoder agent、CodeBuddy workflow 等）。
> **该适配器已移除**，仓库不再提供或维护任何适配器二进制。所有技能以标准 `SKILL.md` 目录为唯一事实源，
> 由各宿主自身的技能加载机制消费。

---

## 安装方式

一条命令安装任意技能包（无需本仓库提供任何适配层）：

```bash
# 安装整个技能包
npx skills add full-stack-skills/vue-skills

# 只安装包内的指定技能
npx skills add full-stack-skills/vue-skills --skill vue3
```

技能包仓库地址：`https://github.com/full-stack-skills/<package>`（如 `full-stack-skills/vue-skills`）。

---

## 宿主兼容性状态

本表按**验证程度**区分状态，供下游审计：

| 状态 | 含义 |
|---|---|
| **已验证 (verified)** | 在真实宿主中安装并确认技能可被加载与触发 |
| **可安装 (installable)** | 目录约定与标准 Agent Skills 一致，有社区安装使用记录；本项目未做系统性兼容测试 |
| **参考 (reference)** | 路径来自公开兼容矩阵，本项目未测试 |

| 宿主 | 全局安装路径 | 状态 | 说明 |
|---|---|---|---|
| Claude Code | `~/.claude/skills/` | 已验证 | 本项目主要开发与验证宿主；各包均提供 `.claude-plugin/plugin.json` |
| Codex | `~/.codex/skills/` | 可安装 | 使用标准 `.agents/skills/` 项目路径约定 |
| **CodeBuddy** | `~/.codebuddy/skills/` | 可安装 | 使用标准技能目录约定；本项目未做系统性兼容测试，与其官方无认证关系 |
| **WorkBuddy** | `~/.workbuddy/skills/` | 可安装 | 已观测到实际安装使用（`~/.workbuddy/skills/` 下存在本项目的技能目录）；本项目未做系统性兼容测试，与其官方无认证关系 |
| 其他宿主 | 见下方参考矩阵 | 参考 | 路径来自公开兼容矩阵，未逐一验证 |

> **关于 WorkBuddy / CodeBuddy**：两者均**不是**本项目的官方背书宿主（endorsed host），
> 本项目也未与其建立任何形式的认证或合作关系。技能可在上述宿主中通过标准技能目录安装使用，
> 但兼容性未经系统化测试；采用前请自行验证。

---

## 平台路径参考矩阵

以下矩阵描述各宿主的**技能目录约定**，用于人工安装或自行编写转换脚本时参考。
数据整理自公开的 Agent Skills 兼容矩阵（以 `vercel-labs/skills` 为基线），**本项目未逐一验证**。

| Platform | ID / Aliases | Project Path | Global Path |
|---|---|---|---|
| Amp | `amp` | `.agents/skills/` | `~/.config/agents/skills/` |
| Kimi Code CLI | `kimi-cli` | `.agents/skills/` | `~/.config/agents/skills/` |
| Replit | `replit` | `.agents/skills/` | `~/.config/agents/skills/` |
| Universal | `universal` | `.agents/skills/` | `~/.config/agents/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` | `~/.gemini/antigravity/skills/` |
| Augment | `augment` | `.augment/skills/` | `~/.augment/skills/` |
| Claude Code | `claude-code, claude` | `.claude/skills/` | `~/.claude/skills/` |
| OpenClaw | `openclaw` | `skills/` | `~/.openclaw/skills/` |
| Cline | `cline` | `.agents/skills/` | `~/.config/agents/skills/` |
| Warp | `warp` | `.agents/skills/` | `~/.config/agents/skills/` |
| CodeBuddy | `codebuddy` | `.codebuddy/skills/` | `~/.codebuddy/skills/` |
| Codex | `codex` | `.agents/skills/` | `~/.codex/skills/` |
| Command Code | `command-code` | `.commandcode/skills/` | `~/.commandcode/skills/` |
| Continue | `continue` | `.continue/skills/` | `~/.continue/skills/` |
| Cortex Code | `cortex` | `.cortex/skills/` | `~/.snowflake/cortex/skills/` |
| Crush | `crush` | `.crush/skills/` | `~/.config/crush/skills/` |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` |
| Deep Agents | `deepagents, deep-agents` | `.agents/skills/` | `~/.deepagents/agent/skills/` |
| Droid | `droid` | `.factory/skills/` | `~/.factory/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `github-copilot, copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Goose | `goose` | `.goose/skills/` | `~/.config/goose/skills/` |
| Junie | `junie` | `.junie/skills/` | `~/.junie/skills/` |
| iFlow CLI | `iflow-cli` | `.iflow/skills/` | `~/.iflow/skills/` |
| Kilo Code | `kilo` | `.kilocode/skills/` | `~/.kilocode/skills/` |
| Kiro CLI | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |
| Kode | `kode` | `.kode/skills/` | `~/.kode/skills/` |
| MCPJam | `mcpjam` | `.mcpjam/skills/` | `~/.mcpjam/skills/` |
| Mistral Vibe | `mistral-vibe, vibe` | `.vibe/skills/` | `~/.vibe/skills/` |
| Mux | `mux` | `.mux/skills/` | `~/.mux/skills/` |
| OpenCode | `opencode` | `.agents/skills/` | `~/.config/opencode/skills/` |
| OpenHands | `openhands` | `.openhands/skills/` | `~/.openhands/skills/` |
| Pi | `pi` | `.pi/skills/` | `~/.pi/agent/skills/` |
| Qoder | `qoder` | `.qoder/skills/` | `~/.qoder/skills/` |
| Qwen Code | `qwen-code` | `.qwen/skills/` | `~/.qwen/skills/` |
| Roo Code | `roo` | `.roo/skills/` | `~/.roo/skills/` |
| Trae | `trae` | `.trae/skills/` | `~/.trae/skills/` |
| Trae CN | `trae-cn` | `.trae/skills/` | `~/.trae-cn/skills/` |
| Windsurf | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| Zencoder | `zencoder` | `.zencoder/skills/` | `~/.zencoder/skills/` |
| Neovate | `neovate` | `.neovate/skills/` | `~/.neovate/skills/` |
| Pochi | `pochi` | `.pochi/skills/` | `~/.pochi/skills/` |
| AdaL | `adal` | `.adal/skills/` | `~/.adal/skills/` |

---

## 手工安装

若目标宿主不在 `npx skills add` 的覆盖范围内，可手工复制技能目录：

```bash
# 1. 克隆具体技能包（每个包是独立仓库）
git clone https://github.com/full-stack-skills/vue-skills.git

# 2. 复制技能目录到目标宿主的技能路径
cp -r vue-skills/skills/vue3 ~/.claude/skills/          # Claude Code
cp -r vue-skills/skills/vue3 ~/.codebuddy/skills/       # CodeBuddy
cp -r vue-skills/skills/vue3 ~/.workbuddy/skills/       # WorkBuddy
```

技能目录内仅需 `SKILL.md` 即可被识别；`references/`、`examples/`、`scripts/`、`assets/` 为可选配套资料。

---

## 相关文档

- [README.md](README.md) — 仓库主文档与技能目录
- [LICENSE](LICENSE) — Apache License 2.0 授权文本
- [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) — 第三方组件归属声明
- [AGENTS.md](AGENTS.md) — 技能编写与仓库约定
