---
name: tauri-app-shell
description: "Execute system commands and open external URLs securely using the Tauri v2 shell plugin with strict allowlists. Use when spawning child processes, running system commands with argument validation, or opening URLs in the default browser via shell."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Executing system commands from a Tauri app
- Shell plugin permissions and command allowlists
- Opening external URLs via shell (alternative to opener plugin)

**Trigger phrases include:**
- "shell", "execute command", "spawn process", "allow-execute", "system command"

## How to use this skill

1. **Install the shell plugin**:
   ```bash
   cargo add tauri-plugin-shell
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_shell::init())
   ```
3. **Configure strict allowlists** in `src-tauri/capabilities/default.json`:
   ```json
   {
     "permissions": [
       {
         "identifier": "shell:allow-execute",
         "allow": [{ "name": "git", "cmd": "git", "args": ["status"] }]
       },
       "shell:allow-open"
     ]
   }
   ```
4. **Execute commands from the frontend**:
   ```typescript
   import { Command } from '@tauri-apps/plugin-shell';
   const output = await Command.create('git', ['status']).execute();
   console.log('stdout:', output.stdout);
   ```
5. **CRITICAL: Apply strict allowlists** -- the shell plugin is high-risk; never allow arbitrary command execution
6. **Use regex constraints** on arguments when dynamic input is needed, and validate all user-provided args

## Outputs

- Shell plugin setup with strict command allowlists
- Command execution pattern with output handling
- Security-first configuration (this is a high-risk plugin)

## References

- https://v2.tauri.app/plugin/shell/

## Keywords

tauri shell, execute command, spawn process, allow-execute, system command, security
