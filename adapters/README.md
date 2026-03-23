# Cross-Platform Skills Adapter

`adapters/` is the repository’s only cross-platform converter. It ships an independent CLI named `fskill`, exports the grouped repository structure in `skills/<group>/<skill>/` as standard skill directories, and installs them into the path layout required by each supported platform.

## Compatibility baseline

- **Skill format**: standard `SKILL.md`-based directory layout
- **Platform paths**: aligned to the current `vercel-labs/skills` compatibility matrix
- **Repository source layout**: `skills/<group>/<skill>/`

The adapter does not generate platform-specific manifests, plugins, or workflow wrappers. It preserves the original skill directory and changes only the destination path for each platform.

## Install

```bash
git clone https://github.com/partme-ai/full-stack-skills.git
cd full-stack-skills
npm install -g ./adapters
```

Or, for repository-local development:

```bash
cd adapters
npm install
npm link
```

Or, inside the adapter package only:

```bash
cd adapters
npm install -g ./adapters
```

After installation, call `fskill` directly.

## Commands

```bash
fskill --version
fskill platforms
fskill audit
fskill convert --platform all --output ./adapters-output
fskill install
```

`fskill install` defaults to the current project's `.agents/skills/`, which is the standard Agent Skills-compatible path.

## Command reference

### List supported platforms

```bash
fskill platforms
```

### Show CLI version

```bash
fskill --version
```

### Audit the repository skills

```bash
fskill audit
```

### Export all platforms

```bash
fskill convert --platform all --output ./adapters-output
```

### Export one platform

```bash
fskill convert --platform claude-code --output ./adapters-output
```

### Install into a project

```bash
fskill install --platform claude-code --scope project
```

### Install globally

```bash
fskill install --platform antigravity --scope global
```

### Install selected skills only

```bash
fskill install --platform codex --scope global --skill react --skill vue3
```

### Preview without writing

```bash
fskill convert --platform all --output ./adapters-output --dry-run
fskill install --platform windsurf --scope project --dry-run
```

## Supported platforms

Run `fskill platforms --markdown` for the generated Markdown table that matches the CLI registry.

## Discovery rules

- A directory is treated as a skill only when it contains `SKILL.md`
- `skills/pencil-skills/docs` is treated as supporting documentation, not a skill
- `__pycache__`, `.pyc`, `.DS_Store`, and hidden garbage files are excluded
- `references/`, `examples/`, `scripts/`, `assets/`, and `templates/` are preserved

## Output layout

The converter writes standard skill directories under:

```text
adapters-output/<platform>/<project-path>/<skill-name>/
```

Examples:

```text
adapters-output/claude-code/.claude/skills/react/
adapters-output/cursor/.agents/skills/react/
adapters-output/openclaw/skills/react/
adapters-output/antigravity/.agents/skills/react/
```

## Install behavior

- `fskill install` defaults to `<cwd>/.agents/skills/`
- `--scope project` installs into `<cwd>/<projectPath>`
- `--scope global` installs into the platform’s global directory
- default mode copies directories
- `--link` creates symlinks instead of copying
- existing destination directories are replaced to keep installs deterministic

## Source of truth

- Platform registry: `adapters/src/platform-registry.ts`
- Skill discovery and audit: `adapters/src/skills.ts`
- CLI entry: `adapters/src/index.ts`

## Validation expectations

- `platforms` lists every supported platform and path mapping
- `audit` reports actual skill counts, missing `SKILL.md` directories, and platform totals
- `convert --dry-run` shows the exact destination layout before writing
- `install --dry-run` shows exact project or global install targets before writing
