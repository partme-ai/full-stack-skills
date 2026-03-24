---
name: uniapp-project-creator
description: Provides one-command project creation for uni-app using the official quickstart CLI, including project initialization, configuration, and template selection. Use when the user asks to create a uni-app project with a single command, needs to initialize a new uni-app project, or generate uni-app project structure.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create a new uni-app project from scratch
- Initialize uni-app project structure and configuration files
- Set up development environment for uni-app
- Generate project templates with different configurations
- Configure manifest.json and pages.json files
- Create uni-app pages and components
- Set up uni-app project with HBuilderX or CLI

## How to use this skill

To create a uni-app project with a single command or via HBuilderX:

1. **Identify the project type** from the user's request:
   - Standard uni-app project → Use Vue 2 or Vue 3 template
   - HBuilderX project → Use HBuilderX creation method
   - CLI project → Use Vue CLI or official CLI commands

2. **Load the appropriate example file** from the `examples/guide/` directory:
   - `examples/guide/installation.md` - Installation and environment setup
   - `examples/guide/quick-start.md` - Quick start guide
   - `examples/guide/project-types.md` - Different project types and templates

3. **Load the appropriate template file** from the `templates/` directory:
   - `templates/project-templates.md` - Project structure templates
   - `templates/cli-commands.md` - CLI command templates

4. **Follow the specific instructions** in those files for project creation, structure, and configuration

5. **Generate the project structure** with proper files and configurations

**Important Notes**:
- This skill focuses on uni-app CLI quickstart and HBuilderX creation flows
- Use one command creation when the user wants "一句话创建"
- Ensure Vue 2/Vue 3 template choice matches the user's target stack

## Examples and Templates

### Examples

Located in `examples/guide/`:

- **installation.md** - Installation guide for uni-app development environment
- **quick-start.md** - Quick start guide for creating first uni-app project
- **project-types.md** - Different project types (Vue 2, Vue 3, TypeScript, etc.)

### Templates

Located in `templates/`:

- **project-templates.md** - Complete project structure templates
- **cli-commands.md** - CLI command templates for project creation

## API Reference

This skill focuses on project creation and initialization. For component and API references, see `uniapp-project-guide`.

## Best Practices

1. **Choose the right template**: Select Vue 2 or Vue 3 based on project requirements
2. **Configure properly**: Set up manifest.json and pages.json correctly
3. **Organize structure**: Follow standard uni-app directory structure
4. **Use CLI when possible**: CLI provides more flexibility than HBuilderX
5. **Version control**: Initialize git repository after project creation

## Resources

- **Official Documentation**: https://uniapp.dcloud.net.cn/quickstart-cli.html
- **HBuilderX**: https://www.dcloud.io/hbuilderx.html
- **Vue CLI**: https://cli.vuejs.org/
- **uni-app GitHub**: https://github.com/dcloudio/uni-app

## Keywords

uniapp, uni-app, project creator, project initialization, HBuilderX, Vue CLI, manifest.json, pages.json, uni-app setup, uni-app template, 创建项目, 项目初始化, 快速开始
