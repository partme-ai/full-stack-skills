## Instructions

Use these notes to customize the install script behavior.

### Notes
- `NVM_DIR` sets the install directory (no trailing slash).
- `PROFILE` chooses which shell profile to edit.
- Use `--no-use` to avoid auto-using a default version.

### Example

```sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" --no-use
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#additional-notes
