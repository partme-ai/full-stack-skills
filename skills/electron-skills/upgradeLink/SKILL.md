---
name: upgradeLink
description: Provides comprehensive guidance for upgrade link management including upgrade link creation, configuration, and upgrade link best practices. Use when the user asks about upgrade links, needs to create upgrade links, configure upgrade processes, or manage upgrade links.
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

## Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the `examples/` directory (see mapping above).

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the mapping above
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference templates in `templates/` directory for common scaffolding
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official UpgradeLink API documentation structure.

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Follow official documentation**: Always refer to official UpgradeLink documentation
2. **Test upgrades**: Test upgrades in development environment first
3. **Backup data**: Always backup data before performing upgrades
4. **Version compatibility**: Check version compatibility requirements
5. **Error handling**: Implement proper error handling
6. **Logging**: Enable logging for troubleshooting
7. **Documentation**: Document upgrade procedures
8. **Rollback plan**: Have a rollback plan ready

## Resources

- **Official Website**: https://www.toolsetlink.com/
- **Documentation**: https://www.toolsetlink.com/upgrade/what-is-upgrade.html

## Keywords

UpgradeLink, upgrade, migration, version, toolsetlink, 升级, 迁移, 版本
