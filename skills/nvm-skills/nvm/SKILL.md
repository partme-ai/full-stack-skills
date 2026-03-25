---
name: nvm
description: "Install, configure, and use nvm (Node Version Manager) to manage Node.js versions. Routes to focused sub-skills for installation, shell setup, version switching, .nvmrc defaults, global packages, Docker/CI, troubleshooting, and more. Use when the user needs to manage Node.js versions, install nvm, or troubleshoot nvm usage."
license: Complete terms in LICENSE.txt
---

# nvm (Node Version Manager)

Route broad or ambiguous nvm requests to the most relevant sub-skill.

## Workflow

1. Identify the user's intent from their request.
2. Route to the best-matching sub-skill below.

### Sub-skill routing map

| User Intent | Sub-skill |
|---|---|
| "Install nvm", "How do I set up nvm?" | nvm-install |
| "nvm not found", "shell profile setup" | nvm-setup |
| "nvm install 20", "nvm use", "switch node" | nvm-usage-basics |
| ".nvmrc", "default version", "nvm alias" | nvm-defaults-and-nvmrc |
| "global packages", "reinstall-packages" | nvm-global-packages |
| "mirror", "corporate proxy", "auth header" | nvm-mirror-and-auth |
| "Docker", "CI/CD", "Dockerfile" | nvm-docker-ci |
| "verify", "nvm --version", "is nvm working?" | nvm-verify |
| "macOS nvm issues", "zshrc" | nvm-troubleshooting-macos |
| "Linux nvm issues", "WSL" | nvm-troubleshooting-linux |
| "auto use", "auto switch on cd" | nvm-shell-integration |
| "uninstall nvm", "remove nvm" | nvm-uninstall |
| "nvm colors", "ansible", "nvm tests" | nvm-misc |
| "maintainers", "license", "support" | nvm-project-meta |

## Keywords

nvm, node version manager, node.js, install nvm, nvm use, nvm install, .nvmrc, lts, node versions, npm global packages, macos, linux, wsl, alpine, docker
