---
name: nvm-mirror-and-auth
description: "Configure custom Node.js binary mirrors and authentication headers for corporate or restricted network environments. Use when the user asks about NVM_NODEJS_ORG_MIRROR, setting a custom node download mirror, configuring auth headers for private mirrors, or installing Node behind a firewall or corporate proxy."
license: Complete terms in LICENSE.txt
---

# nvm Mirror and Authentication

Configure nvm to download Node.js binaries from custom mirrors in restricted network environments.

## Workflow

1. **Set the mirror URL** via environment variable:
   ```bash
   # Use a custom mirror (e.g., Taobao mirror for China)
   export NVM_NODEJS_ORG_MIRROR=https://npmmirror.com/mirrors/node

   # Then install as normal
   nvm install 20
   ```

2. **Configure authentication headers** if the mirror requires auth:
   ```bash
   # Set auth header for private mirror access
   export NVM_AUTH_HEADER="Authorization: Bearer <token>"
   nvm install 20
   ```

3. **Validate mirror connectivity:**
   ```bash
   # Test the mirror URL
   curl -I "$NVM_NODEJS_ORG_MIRROR/v20.11.0/"

   # Verify node downloads successfully
   nvm install 20 && node -v
   ```

**Note:** Installation steps are in nvm-install. This skill handles only mirror and auth configuration.

### Example file map

- `examples/mirror.md` - Mirror URL configuration
- `examples/mirror-auth-header.md` - Authentication header setup

## Keywords

node mirror, NVM_NODEJS_ORG_MIRROR, auth header, restricted network, corporate proxy, private mirror
