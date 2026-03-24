---
name: nvm-mirror-and-auth
description: Configure Node.js binary mirrors and authentication headers for restricted or 10、Company Manger network environments.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Setting a custom Node mirror
- Using auth headers for mirror access
- Dealing with restricted network access

**Trigger phrases include:**
- "mirror", "镜像源", "NVM_NODEJS_ORG_MIRROR"
- "auth header", "认证 header", "internal mirror"

## How to use this skill

**CRITICAL: This skill is only for mirror and auth configuration.** Installation steps remain in nvm-install.

1. Choose the mirror URL and set the environment variables.
2. Configure auth headers if required by the mirror.
3. Validate the mirror settings and handle network errors.

### Example file map

- examples/mirror.md
- examples/mirror-auth-header.md

## Keywords

node mirror, NVM_NODEJS_ORG_MIRROR, auth header, restricted network, 内网镜像
