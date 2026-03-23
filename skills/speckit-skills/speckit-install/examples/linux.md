# Linux: Install Specify CLI

```bash
# Install uv if not present (example)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Persistent install of Specify CLI
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify
specify check
```

Then use **speckit-initial** to run `specify init` in your project directory.
