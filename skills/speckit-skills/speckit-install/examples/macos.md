# macOS: Install Specify CLI

```bash
# Install uv if not present (e.g. via Homebrew or official installer)
# See https://docs.astral.sh/uv/

# Persistent install of Specify CLI
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify
specify check
```

Then use **speckit-initial** to run `specify init . --ai claude` (or `--ai cursor-agent`, etc.) in your project.
