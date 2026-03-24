# CI: Install CLI only (no project init)

Use this when your CI job only needs the `specify` binary (e.g. to run `specify check` later, or to run `specify init` in a separate step).

```bash
# Cache this step when possible
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Later in the same runner
specify check
# or
specify init . --ai claude --no-git
```

No project initialization is performed here; that is done in **speckit-initial**.
