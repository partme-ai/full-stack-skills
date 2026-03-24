# 跨平台使用指南

`full-stack-skills` 通过 `/adapters` 下的独立 CLI `fskill` 适配多平台运行时。转换器将仓库中的 `skills/<group>/<skill>/` 结构导出为标准 skills 目录，并按平台要求写入对应的项目级或全局级安装路径。

## 适配原则

- **单一输出格式**：统一输出标准 `SKILL.md` 技能目录
- **单一路径事实源**：平台路径以 `vercel-labs/skills` 兼容矩阵为基线
- **无专有包装层**：不再生成 Cursor rule、Trae plugin、Qoder agent、CodeBuddy workflow 等非标准包装物
- **目录即技能**：仅当目录中存在 `SKILL.md` 时才视为可转换技能
- **支持目录排除**：`skills/pencil-skills/docs` 视为支持文档，不参与转换

## 适配器命令

```bash
git clone https://github.com/partme-ai/full-stack-skills.git
cd full-stack-skills
npm install -g ./adapters
fskill --version
fskill platforms
fskill audit
fskill convert --platform all --output ./adapters-output
fskill install
```

默认安装命令 `fskill install` 会写入当前项目的 `.agents/skills/`。
如果只在仓库开发态使用，可进入 `adapters/` 执行 `npm install && npm link`，然后直接运行 `fskill ...`。

## 命令说明

### 1. 查看平台矩阵

```bash
fskill platforms
```

### 2. 审计技能目录

```bash
fskill audit
```

当前仓库审计基线：

- 可转换技能：`421`
- 缺失 `SKILL.md` 的技能目录：`0`
- 排除目录：`skills/pencil-skills/docs`
- 支持平台：`43`

### 3. 导出所有平台

```bash
fskill convert --platform all --output ./adapters-output
```

### 4. 导出单个平台

```bash
fskill convert --platform claude-code --output ./adapters-output
```

### 5. 安装到项目目录

```bash
fskill install --platform claude-code --scope project
```

### 6. 安装到全局目录

```bash
fskill install --platform antigravity --scope global
```

### 7. 干跑预览

```bash
fskill convert --platform all --output ./adapters-output --dry-run
fskill install --platform windsurf --scope project --dry-run
```

## 平台矩阵

下表由 `adapters/src/platform-registry.ts` 驱动，CLI 可通过 `fskill platforms --markdown` 输出同一份表格。

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

## 输出目录约定

转换结果统一写入：

```text
adapters-output/<platform>/<project-path>/<skill-name>/
```

示例：

```text
adapters-output/claude-code/.claude/skills/react/
adapters-output/cursor/.agents/skills/react/
adapters-output/openclaw/skills/react/
adapters-output/antigravity/.agents/skills/react/
```

## 安装策略

- `fskill install`：默认安装到当前项目的 `.agents/skills/`
- `--scope project`：安装到当前项目目录下的平台路径
- `--scope global`：安装到用户主目录下的平台全局路径
- 默认行为为复制目录
- 追加 `--link` 时使用符号链接
- 同名目标目录会被替换，以保证安装结果确定且可重复

## 验证建议

- 用 `platforms` 校验平台 ID、别名、项目路径、全局路径
- 用 `audit` 校验仓库技能数量、排除目录与缺失情况
- 用 `convert --dry-run` 预览导出目录
- 用 `install --dry-run` 预览项目级或全局级安装目标
- 在实际平台中抽查至少一个共享路径平台、一个专属目录平台，以及 Antigravity

## 相关文档

- [adapters/README.md](adapters/README.md) - 适配器命令与实现说明
- [README.md](README.md) - 仓库主文档
- [docs/repository-map.md](docs/repository-map.md) - 仓库结构与发布面快照
