---
name: upgrade-link
description: "Configure and manage UpgradeLink for system upgrades, version migrations, and upgrade workflows. Covers link creation, settings configuration, API integrations, and rollback strategies. Use when the user asks about UpgradeLink, needs to create upgrade links, perform version migrations, or configure upgrade processes."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Use UpgradeLink tool for system upgrades
- Understand UpgradeLink features and capabilities
- Perform version migrations
- Configure UpgradeLink settings
- Troubleshoot UpgradeLink issues
- Implement upgrade workflows
- Use UpgradeLink APIs or integrations
- Follow UpgradeLink best practices

## How to use this skill

This skill is organized to match the UpgradeLink official documentation structure (https://www.toolsetlink.com/upgrade/what-is-upgrade.html). When working with UpgradeLink:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/introduction.md` or `examples/getting-started/basic-usage.md`
   - Features/功能特性 → `examples/features/` directory
   - Advanced usage/高级用法 → `examples/advanced/` directory

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/introduction.md` - What is UpgradeLink
   - `examples/getting-started/basic-usage.md` - Basic usage examples

   **Features (功能特性) - `examples/features/`**:
   - `examples/features/` - Feature-specific examples

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/` - Advanced usage examples

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow UpgradeLink official documentation
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/` - API reference documentation

5. **Use templates** from the `templates/` directory:
   - `templates/` - Usage templates


### Doc mapping (one-to-one with official documentation)

- `examples/` → https://www.toolsetlink.com/upgrade/what-is-upgrade.html

## Upgrade Workflow

1. **Pre-upgrade checks:**
   - Verify version compatibility requirements
   - Back up data before performing upgrades
   - Test in development environment first

2. **Execute upgrade** following the guide for your use case:
   - Load the appropriate example from `examples/getting-started/` or `examples/features/`
   - Follow the step-by-step instructions in that file

3. **Post-upgrade validation:**
   - Verify the upgrade completed successfully
   - Check logs for errors
   - Have a rollback plan ready if issues arise

## Reference Files

- `examples/getting-started/` - Introduction and basic usage
- `examples/features/` - Feature-specific examples
- `examples/advanced/` - Advanced usage patterns
- `api/` - API reference documentation
- `templates/` - Usage templates

## Best Practices

1. **Test first**: Always test upgrades in development before production
2. **Backup data**: Create backups before performing upgrades
3. **Error handling**: Implement proper error handling and logging
4. **Rollback plan**: Have a rollback plan ready for every upgrade

## Resources

- **Official Website**: https://www.toolsetlink.com/
- **Documentation**: https://www.toolsetlink.com/upgrade/what-is-upgrade.html

## Keywords

UpgradeLink, upgrade, migration, version, toolsetlink, 升级, 迁移, 版本
