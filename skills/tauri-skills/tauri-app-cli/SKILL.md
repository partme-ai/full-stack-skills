---
name: tauri-app-cli
description: "Configure the Tauri v2 CLI plugin to parse command-line arguments using a JSON schema and route them to app behavior. Use when defining CLI argument schemas, handling startup arguments, or integrating CLI with single-instance mode."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- CLI arguments for a Tauri application
- Schema-based argument parsing at app launch
- Routing CLI commands to app behavior or windows

**Trigger phrases include:**
- "cli", "arguments", "command line", "schema", "command routing", "cli plugin"

## How to use this skill

1. **Install the CLI plugin**:
   ```bash
   cargo add tauri-plugin-cli
   ```
2. **Define the CLI schema** in `tauri.conf.json`:
   ```json
   {
     "plugins": {
       "cli": {
         "description": "My Tauri App",
         "args": [
           { "name": "input", "short": "i", "takesValue": true, "description": "Input file path" }
         ],
         "subcommands": {
           "open": { "description": "Open a specific view", "args": [] }
         }
       }
     }
   }
   ```
3. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_cli::init())
   ```
4. **Handle CLI matches** on the frontend:
   ```typescript
   import { getMatches } from '@tauri-apps/plugin-cli';
   const matches = await getMatches();
   if (matches.args.input?.value) {
     console.log('Input file:', matches.args.input.value);
   }
   ```
5. **Combine with single-instance plugin** to forward second-launch arguments to the running instance
6. **Configure capabilities**: `"cli:default"`

## Outputs

- CLI argument schema in tauri.conf.json
- Frontend argument parsing and routing logic
- Second-launch argument forwarding pattern

## References

- https://v2.tauri.app/plugin/cli/

## Keywords

tauri cli, arguments, schema, command routing, command line
