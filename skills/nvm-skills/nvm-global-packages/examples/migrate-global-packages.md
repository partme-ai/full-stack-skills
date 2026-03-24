## Instructions

Reinstall global packages when installing a new Node version.

### Examples

```sh
nvm install --reinstall-packages-from=node node
nvm install --reinstall-packages-from=5 6
nvm install --reinstall-packages-from=default --latest-npm 'lts/*'
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#migrating-global-packages-while-installing
