---
name: vscode-project-init
description: "Scaffold a new VS Code extension project using TypeScript via Yeoman generator (yo code), creating src/extension.ts entry point and package.json manifest. Use when the user wants to start a new VS Code extension project from scratch."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill when the user wants to start a new VS Code extension project. This is the first step in the development workflow.

## How to use this skill

1.  **Ask for Project Name**: If the user hasn't provided a name, ask for it (e.g., "my-awesome-extension").
2.  **Execute Initialization Command**: Run the following command to scaffold the project non-interactively.

```bash
# Replace <project-name> with the actual name
npx --package yo --package generator-code -- yo code <project-name> --template typescript --quick
```

3.  **Post-Initialization**:
    *   Change directory into the new project: `cd <project-name>`
    *   Explain the structure briefly:
        *   `src/extension.ts`: Main entry point.
        *   `package.json`: Manifest file.
    *   Run `npm install` (if not already done by the generator, though `--quick` usually handles it).

## Example Interaction

User: "Create a new vscode extension named helper"
Agent: 
"I'll initialize the project for you.
Running: `npx --package yo --package generator-code -- yo code helper --template typescript --quick`
...
Project created! You can now start adding features."
