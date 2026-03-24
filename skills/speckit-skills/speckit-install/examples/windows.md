# Windows: Install Specify CLI

Install [uv](https://docs.astral.sh/uv/) first (see uv documentation for Windows).

In PowerShell or cmd:

```powershell
# Persistent install of Specify CLI
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify
specify check
```

For project initialization on Windows, use **speckit-initial** with `--script ps` when you need PowerShell scripts: `specify init . --ai copilot --script ps` (or your chosen agent).
