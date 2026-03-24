---
name: dart-sass
description: Provides comprehensive guidance for Dart Sass including Sass syntax, compilation, mixins, functions, and best practices. Use when the user asks about Dart Sass, needs to compile Sass to CSS, use Sass features, or work with Sass in projects.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and configure Dart Sass
- Compile Sass/SCSS files to CSS
- Use Sass syntax features (variables, nesting, mixins, functions, etc.)
- Work with Sass modules and imports
- Integrate Sass into build tools or workflows
- Use Sass CLI commands
- Configure Sass compilation options
- Use Sass in JavaScript or Dart projects
- Optimize Sass compilation performance
- Handle Sass source maps

## How to use this skill

To use Dart Sass:

1. **Install Dart Sass**:
   - Load `examples/getting-started/installation.md` for installation instructions
   - Load `examples/getting-started/basic-usage.md` for basic usage examples
   - Load `examples/getting-started/compiling-modes.md` for different compilation modes

2. **Learn Sass syntax**:
   - Load `examples/syntax/variables.md` for variable usage
   - Load `examples/syntax/nesting.md` for nesting syntax
   - Load `examples/syntax/mixins.md` for mixins
   - Load `examples/syntax/functions.md` for functions
   - Load `examples/syntax/operators.md` for operators
   - Load `examples/syntax/at-rules.md` for at-rules

3. **Use advanced features**:
   - Load `examples/features/modules.md` for module system
   - Load `examples/features/imports.md` for imports
   - Load `examples/features/control-flow.md` for control flow
   - Load `examples/features/built-in-modules.md` for built-in modules
   - Load `examples/features/source-maps.md` for source maps
   - Load `examples/features/custom-functions.md` for custom functions

4. **Reference the API documentation** when needed:
   - `api/js-api.md` - JavaScript API reference
   - `api/dart-api.md` - Dart API reference
   - `api/cli-api.md` - CLI command reference

5. **Use templates** for quick start:
   - `templates/basic-project.md` - Basic Sass project template
   - `templates/modular-project.md` - Modular Sass project template
   - `templates/build-integration.md` - Build tool integration template


### Doc mapping (one-to-one with official documentation)

- `examples/` → https://sass-lang.com/documentation/

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

- **JavaScript API**: `api/js-api.md` - JavaScript API for compiling Sass (compile, compileString, etc.)
- **Dart API**: `api/dart-api.md` - Dart API for compiling Sass
- **CLI API**: `api/cli-api.md` - Command-line interface options and usage

## Best Practices

1. **Use @use instead of @import**: The @import rule is deprecated, use @use and @forward instead
2. **Organize with modules**: Use the module system to organize and share code
3. **Optimize compilation**: Use appropriate output style (compressed for production)
4. **Source maps**: Enable source maps for development, disable for production
5. **Watch mode**: Use --watch for development to automatically recompile on changes
6. **Load paths**: Use --load-path to simplify import paths
7. **Performance**: Use Dart Sass for best performance (faster than Ruby Sass)
8. **Version control**: Don't commit compiled CSS files, only commit Sass source files

## Resources

- **Official Website**: https://sass-lang.com/dart-sass/
- **Installation Guide**: https://sass-lang.com/install/
- **Documentation**: https://sass-lang.com/documentation/
- **GitHub Repository**: https://github.com/sass/dart-sass
- **npm Package**: https://www.npmjs.com/package/sass
- **pub.dev Package**: https://pub.dev/packages/sass

## Keywords

dart-sass, sass, scss, css preprocessor, sass compiler, sass syntax, sass modules, sass mixins, sass functions, sass variables, sass nesting, @use, @forward, @import, @include, @mixin, @function, sass:math, sass:color, sass:string, source maps, sass cli, sass api, 样式预处理器, Sass 编译器, Sass 语法, Sass 模块, Sass 混合, Sass 函数
