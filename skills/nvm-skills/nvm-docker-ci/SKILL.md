---
name: nvm-docker-ci
description: "Install and configure nvm in Docker containers and CI/CD pipelines, including non-interactive shell loading via BASH_ENV or ENTRYPOINT. Use when the user asks about nvm in Docker, CI/CD nvm setup, GitHub Actions node version management, or troubleshooting nvm in non-interactive shells."
license: Complete terms in LICENSE.txt
---

# nvm in Docker and CI/CD

Configure nvm for containerized and CI/CD environments where shells run non-interactively.

## Workflow

1. **Install nvm in a Dockerfile:**
   ```dockerfile
   ENV NVM_DIR=/usr/local/nvm
   ENV NODE_VERSION=20.11.0
   RUN mkdir -p $NVM_DIR \
     && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash \
     && . $NVM_DIR/nvm.sh \
     && nvm install $NODE_VERSION \
     && nvm alias default $NODE_VERSION

   # Make nvm available in non-interactive shells
   ENV BASH_ENV="$NVM_DIR/nvm.sh"
   ```

2. **Load nvm in CI/CD jobs** (e.g., GitHub Actions):
   ```yaml
   steps:
     - run: |
         export NVM_DIR="$HOME/.nvm"
         [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
         nvm install 20
         nvm use 20
         node -v
   ```

3. **Validate nvm availability** in the container or pipeline:
   ```bash
   docker run --rm my-image bash -c "nvm --version && node -v"
   ```

**Note:** Base installation steps are in nvm-install. This skill targets container and CI usage only.

### Example file map

- `examples/install-docker.md` - Dockerfile nvm installation
- `examples/install-docker-cicd.md` - CI/CD pipeline configuration
- `examples/docker-dev.md` - Development container setup

## Keywords

docker, ci, bash_env, entrypoint, non-interactive shell, nvm in container, GitHub Actions
