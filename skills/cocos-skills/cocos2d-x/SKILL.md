---
name: cocos2d-x
description: Provides comprehensive guidance for Cocos2d-x v4 game engine including scene graph, nodes, sprites, actions, animations, physics, rendering, shaders, and platform deployment. Use when the user asks about Cocos2d-x, needs to create games, implement game features, set up development environments, or deploy games to multiple platforms.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create Cocos2d-x v4 games or applications
- Learn Cocos2d-x v4 core concepts (Node, Sprite, Scene, Action)
- Set up Cocos2d-x v4 development environment
- Work with sprites, textures, animations, and labels
- Implement scene management and node lifecycle
- Handle input events (touch, mouse, keyboard)
- Use physics engine (Box2D) and collision detection
- Implement rendering pipeline, shaders, and particle systems
- Build and deploy games for multiple platforms (Windows, macOS, Linux, Android, iOS)
- Use CMake build system and command-line tools
- Migrate from older Cocos2d-x versions
- Extend engine with custom rendering and script bindings

## How to use this skill

To work with Cocos2d-x v4:

1. **Identify the topic** from the user's request:
   - Engine overview/了解引擎 → `examples/getting-started/about-engine.md`
   - Quick start/快速上手 → `examples/getting-started/quick-start.md`
   - Installation/安装配置 → `examples/getting-started/installation.md`
   - Node and Scene/节点和场景 → `examples/core/node-scene.md`
   - Sprite/精灵 → `examples/core/sprite.md`
   - Texture/纹理 → `examples/core/texture.md`
   - Animation/动画 → `examples/core/animation.md`
   - Action/动作 → `examples/core/action.md`
   - Label/标签 → `examples/core/label.md`
   - Scene management/场景管理 → `examples/core/scene.md`
   - Input handling/输入处理 → `examples/core/input.md`
   - Event system/事件系统 → `examples/core/event.md`
   - Physics/物理引擎 → `examples/advanced/physics.md`
   - Rendering/渲染 → `examples/advanced/rendering.md`
   - Shaders/着色器 → `examples/advanced/shader.md`
   - Particle system/粒子系统 → `examples/advanced/particle.md`
   - Build system/构建系统 → `examples/tools/build-system.md`
   - Platform deployment/平台部署 → `examples/tools/deployment.md`

2. **Load the appropriate example file** from the `examples/` directory:
   - `examples/getting-started/about-engine.md` - Engine overview and features
   - `examples/getting-started/quick-start.md` - Create first project
   - `examples/getting-started/installation.md` - Environment setup
   - `examples/core/node-scene.md` - Node and Scene concepts
   - `examples/core/sprite.md` - Sprite creation and manipulation
   - `examples/core/texture.md` - Texture loading and management
   - `examples/core/animation.md` - Animation system
   - `examples/core/action.md` - Action system and sequences
   - `examples/core/label.md` - Label and text rendering
   - `examples/core/scene.md` - Scene management and transitions
   - `examples/core/input.md` - Touch, mouse, and keyboard input
   - `examples/core/event.md` - Event system and listeners
   - `examples/advanced/physics.md` - Physics engine integration
   - `examples/advanced/rendering.md` - Rendering pipeline
   - `examples/advanced/shader.md` - Custom shaders
   - `examples/advanced/particle.md` - Particle effects
   - `examples/tools/build-system.md` - CMake and build configuration
   - `examples/tools/deployment.md` - Platform-specific deployment

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   Each example file contains:
   - **Instructions**: Overview and usage guidelines
   - **Syntax**: API syntax and parameters
   - **Examples**: Complete code examples with explanations
   - **Reference**: Links to official documentation

4. **Generate C++ code** following Cocos2d-x v4 conventions:
   - Use `USING_NS_CC;` for namespace
   - Use `CREATE_FUNC()` macro for create functions
   - Follow Cocos2d-x naming conventions
   - Include proper error handling
   - Use smart pointers where appropriate

5. **Reference the official documentation**:
   - Official manual: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
   - API reference: Check `api/` directory for detailed API documentation
   - Examples: Check `examples/` directory for code examples

6. **Use templates** when creating new projects:
   - `templates/project-structure.md` - Standard project structure
   - `templates/cmake-config.md` - CMake configuration examples


### Doc mapping (one-to-one with official documentation)

- See examples and API files → https://docs.cocos.com/cocos2d-x/v4/manual/zh/

## Core Concepts

### Node System
- **Node**: Base class for all display objects
- **Scene**: Root node of the scene graph
- **Sprite**: Image display node
- **Label**: Text display node
- **Node hierarchy**: Parent-child relationships

### Coordinate System
- Origin at bottom-left (OpenGL style)
- Anchor point for positioning
- Local and world coordinates

### Action System
- **Action**: Base class for node transformations
- **Sequence**: Chain multiple actions
- **Spawn**: Run actions simultaneously
- **Repeat**: Repeat actions multiple times
- **Ease**: Apply easing functions

### Scene Management
- Scene transitions
- Scene lifecycle (onEnter, onExit)
- Director for scene management

### Input Handling
- Touch events (single and multi-touch)
- Mouse events
- Keyboard events
- Event dispatcher system

## Platform Support

Cocos2d-x v4 supports:
- **Desktop**: Windows, macOS, Linux
- **Mobile**: Android, iOS
- **Web**: (via Cocos Creator)

## Build System

- **CMake**: Primary build system
- **Command-line tools**: `cocos` command
- **IDE support**: Visual Studio, Xcode, Android Studio

## Migration Guide

For migrating from older versions:
- Check `examples/migration/` for migration guides
- API changes and compatibility notes
- CMake migration from older build systems

## Reference Resources

- **Official Documentation**: https://docs.cocos.com/cocos2d-x/v4/manual/zh/
- **API Reference**: See `api/` directory
- **Examples**: See `examples/` directory
- **Templates**: See `templates/` directory

## Keywords

cocos2d-x, cocos2d, game engine, game development, C++ game, 2D game, cross-platform game, sprite, scene, node, action, animation, physics, rendering, shader, particle system, CMake, game framework, 游戏引擎, 游戏开发, 精灵, 场景, 节点, 动作, 动画, 物理引擎, 渲染, 着色器, 粒子系统

## Important Notes

1. **Version**: This skill covers Cocos2d-x v4 specifically
2. **Language**: C++ is the primary development language
3. **Build System**: CMake is required for building projects
4. **Platform**: Ensure platform-specific dependencies are installed
5. **Examples**: All code examples use C++ syntax
6. **Memory Management**: Cocos2d-x uses reference counting, be careful with retain/release cycles
7. **Coordinate System**: Uses OpenGL-style coordinates (origin at bottom-left)
8. **Thread Safety**: Most Cocos2d-x operations must be performed on the main thread
