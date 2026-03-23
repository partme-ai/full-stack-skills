---
name: uniapp-ucharts
description: A comprehensive skill for integrating and using uCharts with UniApp projects. This skill focuses on UniApp-specific integration, configuration, and platform-specific considerations when using uCharts in UniApp applications. Use this skill whenever the user needs to integrate uCharts into UniApp projects, configure UniApp-specific settings, or handle platform differences.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Integrate uCharts into UniApp projects
- Configure UniApp projects to work with uCharts (pages.json, manifest.json, easycom)
- Handle platform-specific behaviors when using uCharts in UniApp (H5, mini-program, App, nvue)
- Use UniApp features (navigation, APIs, lifecycle) with uCharts components
- Build cross-platform UniApp applications with uCharts charts
- Configure easycom for automatic uCharts component import in UniApp
- Handle navigation and routing with uCharts in UniApp
- Optimize UniApp projects using uCharts
- Deploy uCharts-based UniApp applications to multiple platforms

## How to use this skill

This skill is organized to match UniApp integration patterns and the official UniApp plugin structure (https://ext.dcloud.net.cn/plugin?id=271). When working with uCharts in UniApp:

1. **Install and setup** uCharts in UniApp project:
   - Load `examples/getting-started/installation.md` for installation in UniApp
   - Load `examples/getting-started/project-setup.md` for UniApp project configuration
   - Load `examples/getting-started/easycom-config.md` for easycom configuration

2. **Integrate with UniApp features**:
   - Load `examples/integration/pages-config.md` for pages.json configuration
   - Load `examples/integration/manifest-config.md` for manifest.json configuration
   - Load `examples/integration/navigation.md` for navigation with uCharts
   - Load `examples/integration/uni-api.md` for using UniApp APIs with uCharts

3. **Handle platform-specific behaviors**:
   - Load `examples/platform-specific/h5.md` for H5 platform considerations
   - Load `examples/platform-specific/miniprogram.md` for mini-program considerations
   - Load `examples/platform-specific/app.md` for App platform considerations
   - Load `examples/platform-specific/nvue.md` for nvue considerations

4. **Advanced integration**:
   - Load `examples/advanced/custom-theme.md` for theme customization in UniApp
   - Load `examples/advanced/build-optimization.md` for build optimization
   - Load `examples/advanced/multi-platform.md` for multi-platform deployment

5. **Reference the API documentation** when needed:
   - `api/integration-api.md` - UniApp and uCharts integration API
   - `api/config-api.md` - Configuration API reference

6. **Use templates** for quick start:
   - `templates/basic-uniapp-project.md` - Basic UniApp project with uCharts
   - `templates/pages-template.md` - Pages configuration template
   - `templates/manifest-template.md` - Manifest configuration template

**Important Notes**:
- This skill focuses on UniApp integration, not uCharts API documentation
- Always configure easycom in pages.json for automatic component import
- Use conditional compilation (`#ifdef`, `#endif`) for platform-specific code
- Test on all target platforms (H5, mini-programs, App) before deployment
- Use rpx units for responsive sizing in UniApp

## Examples and Templates

### Getting Started
- **Installation**: `examples/getting-started/installation.md` - How to install uCharts in UniApp projects
- **Project Setup**: `examples/getting-started/project-setup.md` - Setting up UniApp project with uCharts
- **Easycom Config**: `examples/getting-started/easycom-config.md` - Configuring easycom for automatic component import

### Integration
- **Pages Config**: `examples/integration/pages-config.md` - Configuring pages.json with uCharts
- **Manifest Config**: `examples/integration/manifest-config.md` - Configuring manifest.json for uCharts
- **Navigation**: `examples/integration/navigation.md` - Navigation and routing with uCharts
- **UniApp API**: `examples/integration/uni-api.md` - Using UniApp APIs with uCharts components

### Platform-Specific
- **H5**: `examples/platform-specific/h5.md` - H5 platform considerations with uCharts
- **Mini-Program**: `examples/platform-specific/miniprogram.md` - Mini-program considerations with uCharts
- **App**: `examples/platform-specific/app.md` - App platform considerations with uCharts
- **nvue**: `examples/platform-specific/nvue.md` - nvue considerations with uCharts

### Advanced
- **Custom Theme**: `examples/advanced/custom-theme.md` - Customizing themes in UniApp projects
- **Build Optimization**: `examples/advanced/build-optimization.md` - Optimizing UniApp builds with uCharts
- **Multi-Platform**: `examples/advanced/multi-platform.md` - Multi-platform deployment strategies

### Templates
- **Basic Project**: `templates/basic-uniapp-project.md` - Basic UniApp project structure with uCharts
- **Pages Template**: `templates/pages-template.md` - pages.json configuration template
- **Manifest Template**: `templates/manifest-template.md` - manifest.json configuration template

## API Reference

- **Integration API**: `api/integration-api.md` - UniApp and uCharts integration API reference
- **Config API**: `api/config-api.md` - Configuration API reference for UniApp projects

## Best Practices

1. **Use easycom**: Configure easycom in pages.json for automatic uCharts component import
2. **Platform Testing**: Test on all target platforms (H5, mini-programs, App) before deployment
3. **Use rpx Units**: Use rpx for responsive sizing in UniApp, px for fixed sizes
4. **Canvas Support**: Ensure canvas is properly supported on target platforms
5. **Manifest Configuration**: Properly configure manifest.json for each platform
6. **Conditional Compilation**: Use conditional compilation (`#ifdef`, `#endif`) for platform-specific code
7. **Performance**: Optimize for each platform's specific requirements
8. **Data Format**: Ensure data format is compatible with uCharts requirements
9. **Lifecycle Management**: Properly handle UniApp page lifecycle with uCharts instances
10. **Memory Management**: Clean up chart instances in onUnload lifecycle

## Resources

- **Official UniApp Plugin**: https://ext.dcloud.net.cn/plugin?id=271
- **UniApp Documentation**: https://uniapp.dcloud.net.cn/
- **UniApp API Reference**: https://uniapp.dcloud.net.cn/api/

## Keywords

uniapp, ucharts, uniapp charts, uniapp integration, uniapp configuration, easycom, pages.json, manifest.json, uni-app, 小程序, 跨平台, H5, App, nvue, 条件编译, 平台差异, 图表, canvas, 图表组件, UniApp 图表, 跨平台图表, 小程序图表, App 图表
