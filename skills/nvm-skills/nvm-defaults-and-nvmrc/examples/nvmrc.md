## Instructions

Use `.nvmrc` to set per-project Node version.

### Examples

```sh
echo "lts/*" > .nvmrc
nvm use
```

```sh
nvm install
```

Notes:
- One version per file, newline-terminated.
- Comments with `#` are allowed.

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#nvmrc
