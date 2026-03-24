## Instructions

Install nvm on Alpine Linux with required build dependencies.

### Alpine 3.13+

```sh
apk add -U curl bash ca-certificates openssl ncurses coreutils python3 make gcc g++ libgcc linux-headers grep util-linux binutils findutils
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

### Alpine 3.5 - 3.12

```sh
apk add -U curl bash ca-certificates openssl ncurses coreutils python2 make gcc g++ libgcc linux-headers grep util-linux binutils findutils
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

Reference: https://github.com/nvm-sh/nvm/blob/master/README.md#installing-nvm-on-alpine-linux
