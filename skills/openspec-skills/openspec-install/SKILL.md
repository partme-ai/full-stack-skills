---
name: openspec-install
description: Install the OpenSpec CLI globally via npm, pnpm, yarn, bun, or nix. Use when the user says "install OpenSpec", "set up OpenSpec", or "openspec command not found".
---

# OpenSpec Install Skill

Install the [OpenSpec CLI](https://github.com/Fission-AI/OpenSpec) so that `openspec` is available globally. This skill covers only **installing the CLI**; it does not run `openspec init`. For project initialization after install, use **openspec-initial**.

## When to Use

- First-time OpenSpec setup ("install OpenSpec", "get started with OpenSpec").
- User reports "openspec: command not found".
- Upgrading to the latest version.
- CI or scripts that need the CLI pre-installed.

## Prerequisites

- **Node.js 20.19.0 or higher** — Check with `node --version`. If not installed, guide the user to install Node.js first (e.g. via nvm, fnm, or official installer).

## Workflow

1. **Check if already installed**
   - Run `openspec --version`. If it succeeds, the CLI is already installed; suggest **openspec-initial** for project setup or upgrading via `npm install -g @fission-ai/openspec@latest`.

2. **Choose package manager and install**
   - **npm** (most common): `npm install -g @fission-ai/openspec@latest`
   - **pnpm**: `pnpm add -g @fission-ai/openspec@latest`
   - **yarn**: `yarn global add @fission-ai/openspec@latest`
   - **bun**: `bun add -g @fission-ai/openspec@latest`
   - **nix** (one-time, no install): `nix run github:Fission-AI/OpenSpec -- init`
   - **nix** (persistent): `nix profile install github:Fission-AI/OpenSpec`

3. **Verify installation**
   - Run `openspec --version` to confirm.

4. **Upgrade existing installation**
   - Same command as install — e.g. `npm install -g @fission-ai/openspec@latest`.

## Outputs

- `openspec` command available globally in PATH.

## Next Steps

- Use **openspec-initial** to run `openspec init` in a project.
- Or use **openspec-onboard** for a guided tutorial.

## Different Environments

| Environment | Command |
|-------------|---------|
| **npm** | `npm install -g @fission-ai/openspec@latest` |
| **pnpm** | `pnpm add -g @fission-ai/openspec@latest` |
| **yarn** | `yarn global add @fission-ai/openspec@latest` |
| **bun** | `bun add -g @fission-ai/openspec@latest` |
| **nix (one-time)** | `nix run github:Fission-AI/OpenSpec -- init` |
| **nix (persistent)** | `nix profile install github:Fission-AI/OpenSpec` |
| **CI** | `npm install -g @fission-ai/openspec@latest` in a cacheable step |

## Troubleshooting

- **Node.js version too old**: OpenSpec requires Node.js 20.19.0+. Upgrade Node.js first.
- **Permission errors (npm)**: Use `npm install -g` without sudo if using nvm/fnm; otherwise consider using nvm.
- **Command not found after install**: Ensure the global bin directory is in PATH (check `npm bin -g`).
- **nix not available**: Install nix or use npm/pnpm/yarn/bun instead.

## References

- [OpenSpec Installation docs](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md)
- [OpenSpec GitHub](https://github.com/Fission-AI/OpenSpec)
