## Instructions

Manually remove nvm.

### Steps

```sh
nvm_dir="${NVM_DIR:-~/.nvm}"
nvm unload
rm -rf "$nvm_dir"
```

Remove from shell profile:

```sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[[ -r $NVM_DIR/bash_completion ]] && \. $NVM_DIR/bash_completion
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#uninstalling--removal
