## Instructions

Manual upgrade using git.

### Example

```sh
(
  cd "$NVM_DIR"
  git fetch --tags origin
  git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`
) && \. "$NVM_DIR/nvm.sh"
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#manual-upgrade
