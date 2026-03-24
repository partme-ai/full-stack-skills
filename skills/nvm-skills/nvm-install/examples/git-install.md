## Instructions

Install nvm via git and load it from your shell profile.

### Steps

```sh
cd ~/
git clone https://github.com/nvm-sh/nvm.git .nvm
cd ~/.nvm
git checkout v0.40.3
. ./nvm.sh
```

Then add to your profile:

```sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#git-install
