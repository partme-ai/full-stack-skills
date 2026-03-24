# Tauri v2 Agent Skills 生成指令清单

### 1. Foundation (基石层)

- tauri-setup ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-setup 的 skills，必须参考
- `https://v2.tauri.app/start/prerequisites/`
- `https://v2.tauri.app/mobile/development/#prerequisites`
  并严格遵循以下设计规格：
- **边界**：专注于操作系统层面的依赖安装（Rust, Node.js, VS Build Tools, Xcode, Android SDK）。
- **v2 特性**：必须包含移动端开发环境（Android Studio/NDK）的检查步骤。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能完成全平台开发环境准备。

- tauri-scaffold ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-scaffold 的 skills，必须参考
- `https://v2.tauri.app/start/create-project/`
- `https://v2.tauri.app/start/project-structure/`
- `https://v2.tauri.app/start/frontend/`
  并严格遵循以下设计规格：
- **边界**：`create-tauri-app` 的执行决策与初始配置。
- **关键点**：重点处理前端框架的 SSG（静态站点生成）配置（如 Next.js 的 `output: 'export'`），确保适配 Tauri v2 的加载机制。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能创建结构正确的 Tauri v2 项目。

- tauri-app-creator ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-creator 的 skills，必须参考
- `https://v2.tauri.app/`
- `https://v2.tauri.app/start/`
- `https://v2.tauri.app/start/prerequisites/`
- `https://v2.tauri.app/start/create-project/`
- `https://v2.tauri.app/start/project-structure/`
  并严格遵循以下设计规格：
- **边界**：用官方脚手架创建 Tauri v2 项目（create-tauri-app）。
- **关键点**：根据系统与团队偏好选择安装方式（curl / npm / pnpm / bun / cargo），并能解释每种方式的适用场景。
- **输出**：给出可执行的创建命令，以及创建后最小可运行的验证路径（安装依赖、启动前端与 Tauri 开发模式）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能完成 Tauri v2 项目创建工作。

Bash：sh <(curl https://create.tauri.app/sh)
PowerShell：irm https://create.tauri.app/ps | iex
Fish：sh (curl -sSL https://create.tauri.app/sh | psub)
npm：npm create tauri-app@latest
Yarn：yarn create tauri-app
pnpm：pnpm create tauri-app
deno：deno run -A npm:create-tauri-app
bun：bun create tauri-app
Cargo：
cargo install create-tauri-app --locked
cargo create-tauri-app

- tauri-app-frontend-selection ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-frontend-selection 的 skills，必须参考
- `https://v2.tauri.app/start/frontend/`
- `https://v2.tauri.app/start/frontend/leptos/`
- `https://v2.tauri.app/start/frontend/nextjs/`
- `https://v2.tauri.app/start/frontend/nuxt/`
- `https://v2.tauri.app/start/frontend/qwik/`
- `https://v2.tauri.app/start/frontend/sveltekit/`
- `https://v2.tauri.app/start/frontend/trunk/`
- `https://v2.tauri.app/start/frontend/vite/`
  并严格遵循以下设计规格：
- **边界**：前端框架选型与初始化策略（与 Tauri v2 加载机制兼容）。
- **推荐**：默认推荐 Vite（除非需求明确要求 SSR/SSG 框架）。
- **关键点**：对需要静态导出的框架（如 Next.js）明确给出 SSG/export 配置与产物路径要求，确保 Tauri 能加载本地静态资源。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能完成前端框架选型与初始化工作。

### 2. Core Development (核心开发层)

- tauri-ipc ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-ipc 的 skills，必须参考
- `https://v2.tauri.app/concept/inter-process-communication/`
- `https://v2.tauri.app/develop/calling-rust/`
- `https://v2.tauri.app/develop/calling-frontend/`
  并严格遵循以下设计规格：
- **边界**：前端 `invoke` 调用与后端 `#[tauri::command]` 定义。
- **v2 特性**：强调类型安全，优先推荐使用 `tauri-specta` 或官方类型生成工具，避免 `any` 类型。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现类型安全的双向通信。

- tauri-app-develop ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-develop 的 skills，必须参考
- `https://v2.tauri.app/develop/`
- `https://v2.tauri.app/develop/configuration-files/`
- `https://v2.tauri.app/develop/calling-rust/`
- `https://v2.tauri.app/develop/calling-frontend/`
- `https://v2.tauri.app/develop/resources/`
- `https://v2.tauri.app/develop/sidecar/`
- `https://v2.tauri.app/develop/state-management/`
- `https://v2.tauri.app/develop/updating-dependencies/`
- `https://v2.tauri.app/develop/icons/`
- `https://v2.tauri.app/develop/debug/`
- `https://v2.tauri.app/develop/debug/crabnebula-devtools/`
- `https://v2.tauri.app/develop/debug/neovim/`
- `https://v2.tauri.app/develop/debug/rustrover/`
- `https://v2.tauri.app/develop/debug/vscode/`
- `https://v2.tauri.app/develop/plugins/`
- `https://v2.tauri.app/develop/plugins/develop-mobile/`
- `https://v2.tauri.app/develop/tests/`
- `https://v2.tauri.app/develop/tests/mocking/`
- `https://v2.tauri.app/develop/tests/webdriver/`
- `https://v2.tauri.app/develop/tests/webdriver/ci/`
- `https://v2.tauri.app/develop/tests/webdriver/example/selenium/`
- `https://v2.tauri.app/develop/tests/webdriver/example/webdriverio/`
  并严格遵循以下设计规格：
- **边界**：覆盖 Tauri v2 的日常开发工作流（调试、资源、sidecar、图标、插件与测试）。
- **关键点**：能在“前端 dev server”与“本地静态资源加载”两种模式间切换并解释差异；同时指导如何定位 Rust 与 WebView 双端问题。
- **质量门控**：引导为关键能力补齐自动化测试策略（mocking / webdriver / CI）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能进行 Tauri 技术栈项目的开发工作。

- tauri-window ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-window 的 skills，必须参考
- `https://v2.tauri.app/learn/window-customization/`
- `https://v2.tauri.app/zh-cn/learn/window-customization/`
- `https://v2.tauri.app/reference/config/#windows-config`
  并严格遵循以下设计规格：
- **边界**：窗口的创建、配置与生命周期管理。
- **关键点**：包含自定义标题栏（Custom Titlebar）的 CSS 与 JS 实现逻辑。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能构建现代化的桌面窗口 UI。

- tauri-menu-tray ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-menu-tray 的 skills，必须参考
- `https://v2.tauri.app/plugin/tray-icon/`
- `https://v2.tauri.app/plugin/menu/`
  并严格遵循以下设计规格：
- **边界**：原生应用菜单（Menu）与系统托盘（Tray Icon）。
- **关键点**：处理 macOS 与 Windows 在菜单规范上的差异。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现原生系统交互体验。

- tauri-concept ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-concept 的 skills，必须参考
- `https://v2.tauri.app/concept/`
- `https://v2.tauri.app/concept/architecture/`
- `https://v2.tauri.app/concept/process-model/`
- `https://v2.tauri.app/concept/size/`
- `https://v2.tauri.app/concept/inter-process-communication/`
- `https://v2.tauri.app/concept/inter-process-communication/brownfield/`
- `https://v2.tauri.app/concept/inter-process-communication/isolation/`
- `https://v2.tauri.app/zh-cn/concept/`
- `https://v2.tauri.app/zh-cn/concept/architecture/`
- `https://v2.tauri.app/zh-cn/concept/process-model/`
- `https://v2.tauri.app/zh-cn/concept/size/`
- `https://v2.tauri.app/zh-cn/concept/inter-process-communication/`
- `https://v2.tauri.app/zh-cn/concept/inter-process-communication/brownfield/`
- `https://v2.tauri.app/zh-cn/concept/inter-process-communication/isolation/`
  并严格遵循以下设计规格：
- **核心**：解释 Core Process (Rust) 与 WebView Process (Frontend) 的隔离模型。
- **关键点**：Brownfield 模式与 Isolation 模式的区别与应用场景。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能深入理解 Tauri 架构原理。

### 3. Security & Configuration (安全与配置层)

- tauri-config ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-config 的 skills，必须参考
- `https://v2.tauri.app/reference/config/`
- `https://v2.tauri.app/security/csp/`
  并严格遵循以下设计规格：
- **边界**：`tauri.conf.json` 全生命周期管理。
- **关键点**：解释 v2 中配置文件的结构变化（如插件配置位置、Android/iOS 配置段）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能正确管理项目配置。

- tauri-security ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-security 的 skills，必须参考
- `https://v2.tauri.app/security/capabilities/`
- `https://v2.tauri.app/security/scope/`
- `https://v2.tauri.app/security/acl/`
  并严格遵循以下设计规格：
- **边界**：Capabilities (ACL) 权限系统。
- **v2 特性**：这是 v2 最核心的变化。必须指导用户如何配置 Scope（作用域），生成 `capabilities/default.json`，精确控制插件权限。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能构建安全合规的 Tauri 应用。

- tauri-framework-security ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-framework-security 的 skills，必须参考
- `https://v2.tauri.app/security/`
- `https://v2.tauri.app/security/permissions/`
- `https://v2.tauri.app/security/scope/`
- `https://v2.tauri.app/security/capabilities/`
- `https://v2.tauri.app/security/csp/`
- `https://v2.tauri.app/security/http-headers/`
- `https://v2.tauri.app/security/ecosystem/`
- `https://v2.tauri.app/security/lifecycle/`
- `https://v2.tauri.app/security/future/`
- `https://v2.tauri.app/security/runtime-authority/`
  并严格遵循以下设计规格：
- **边界**：Tauri v2 安全模型与安全基线（Capabilities/Scope/CSP/Headers）。
- **关键点**：以“最小权限”为原则，指导如何从业务需求反推 Capabilities 与 Scope，并避免默认放开高风险能力。
- **输出**：给出可落地的安全检查清单（上线前的权限审计、CSP/Headers 验证、插件权限收敛）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能完成 Tauri 框架安全支撑相关工作。

- tauri-app-plugin-permissions ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-plugin-permissions 的 skills，必须参考
- `https://v2.tauri.app/learn/using-plugin-permissions/`
- `https://v2.tauri.app/zh-cn/learn/security/using-plugin-permissions/`
- `https://v2.tauri.app/learn/security/capabilities-for-windows-and-platforms/`
- `https://v2.tauri.app/zh-cn/learn/security/capabilities-for-windows-and-platforms/`
- `https://v2.tauri.app/learn/security/writing-plugin-permissions/`
- `https://v2.tauri.app/zh-cn/learn/security/writing-plugin-permissions/`
  并严格遵循以下设计规格：
- **边界**：插件权限声明、Capabilities 生成与跨平台差异处理。
- **关键点**：区分“插件提供的权限项”与“应用启用的能力”；强调 Windows/平台能力差异时的最小可用配置。
- **输出**：可复用的权限模板（capabilities/default.json）与权限收敛策略。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能完成插件权限的安全配置工作。

- tauri-framework-upgrade ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-framework-upgrade 的 skills，必须参考
- `https://v2.tauri.app/start/migrate/`
- `https://v2.tauri.app/start/migrate/from-tauri-1/`
- `https://v2.tauri.app/start/migrate/from-tauri-2-beta/`
  并严格遵循以下设计规格：
- **边界**：从 Tauri v1 或 v2 beta 迁移到稳定的 Tauri v2。
- **关键点**：识别破坏性变更（配置结构、插件体系、Capabilities 权限系统）并提供逐项迁移检查表。
- **输出**：迁移后的可运行验证步骤（启动、IPC、关键插件能力、权限与 CSP）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能完成 Tauri 版本升级工作。

### 4. Feature Plugins (特定能力插件层)

- tauri-app-shell ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-shell 的 skills，必须参考
- `https://v2.tauri.app/plugin/shell/`
- `https://v2.tauri.app/zh-cn/plugin/shell/`
  并严格遵循以下设计规格：
- **关键点**：Shell 插件的高风险性质。必须强调在 Capabilities 中配置 `shell:allow-execute` 和 `shell:allow-open`，以及使用正则 (regex) 严格限制参数。
- **功能**：生成子进程、打开外部链接。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能为应用添加安全的 Shell 执行能力。

- tauri-app-single-instance ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-single-instance 的 skills，必须参考
- `https://v2.tauri.app/plugin/single-instance/`
- `https://v2.tauri.app/zh-cn/plugin/single-instance/`
  并严格遵循以下设计规格：
- **关键点**：在 Rust `main.rs` 或 `lib.rs` 中配置 `init` 闭包，处理后续实例启动时的参数传递（如 Deep Link 唤起）。
- **功能**：防止多开、聚焦主窗口。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现单例运行模式。

- tauri-app-sql ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-sql 的 skills，必须参考
- `https://v2.tauri.app/plugin/sql/`
- `https://v2.tauri.app/zh-cn/plugin/sql/`
  并严格遵循以下设计规格：
- **关键点**：支持 SQLite, MySQL, PostgreSQL。
- **配置**：`tauri.conf.json` 中的 migrations 路径配置。
- **功能**：前端直接执行 SQL（需谨慎配置 Capabilities 权限）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能集成数据库能力。

- tauri-app-store ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-store 的 skills，必须参考
- `https://v2.tauri.app/plugin/store/`
- `https://v2.tauri.app/zh-cn/plugin/store/`
  并严格遵循以下设计规格：
- **关键点**：区分 `Store` (自动加载) 和 `LazyStore`。
- **功能**：简单的 Key-Value 持久化存储（类似 `localStorage` 但持久化到磁盘文件）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现应用配置或轻量数据的持久化。

- tauri-app-stronghold ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-stronghold 的 skills，必须参考
- `https://v2.tauri.app/plugin/stronghold/`
- `https://v2.tauri.app/zh-cn/plugin/stronghold/`
  并严格遵循以下设计规格：
- **关键点**：基于 IOTA Stronghold 的加密存储。
- **功能**：安全存储敏感数据（如 API Keys, 密码），涉及 Snapshot 管理和 Client/Store 概念。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现高安全性的数据存储。

- tauri-app-upload ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-upload 的 skills，必须参考
- `https://v2.tauri.app/plugin/upload/`
- `https://v2.tauri.app/zh-cn/plugin/upload/`
  并严格遵循以下设计规格：
- **功能**：高效的文件上传（从本地磁盘到 HTTP 服务器）。
- **关键点**：支持进度回调（Progress Handler）和自定义 Headers。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现大文件上传功能。

- tauri-app-websocket ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-websocket 的 skills，必须参考
- `https://v2.tauri.app/plugin/websocket/`
- `https://v2.tauri.app/zh-cn/plugin/websocket/`
  并严格遵循以下设计规格：
- **功能**：在 Rust 层建立 WebSocket 连接，绕过浏览器的 CORS 限制和 Mixed Content 限制。
- **关键点**：生命周期管理（Connect, Message, Disconnect）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现实时通讯能力。

- tauri-app-window-state ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-window-state 的 skills，必须参考
- `https://v2.tauri.app/plugin/window-state/`
- `https://v2.tauri.app/zh-cn/plugin/window-state/`
  并严格遵循以下设计规格：
- **功能**：自动保存和恢复窗口的大小、位置和最大化状态。
- **关键点**：`StateFlags` 的使用，以及如何在应用启动时自动恢复状态。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能优化用户体验。

- tauri-app-sidecar-nodejs ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-sidecar-nodejs 的 skills，必须参考
- `https://v2.tauri.app/learn/sidecar-nodejs/`
- `https://v2.tauri.app/zh-cn/learn/sidecar-nodejs/`
  并严格遵循以下设计规格：
- **边界**：在 Tauri 应用中以 sidecar 方式集成 Node.js 运行时。
- **关键点**：处理跨平台打包、sidecar 可执行文件分发、启动/停止生命周期与权限门控（Capabilities）。
- **输出**：提供端到端示例（Rust 启动 sidecar、前端触发、日志与错误处理、release 打包验证）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能为应用添加 sidecar-nodejs 能力。

- tauri-app-splashscreen ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-splashscreen 的 skills，必须参考
- `https://v2.tauri.app/learn/splashscreen/`
- `https://v2.tauri.app/zh-cn/learn/splashscreen/`
  并严格遵循以下设计规格：
- **边界**：启动画面（Splashscreen）的配置与生命周期控制。
- **关键点**：处理“前端资源加载慢/首次渲染”场景，避免白屏；明确何时隐藏 Splashscreen 与显示主窗口。
- **输出**：提供跨平台一致的启动体验实现方案（含常见错误排查）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能为应用添加启动画面能力。

- tauri-app-system-tray ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-system-tray 的 skills，必须参考
- `https://v2.tauri.app/learn/system-tray/`
- `https://v2.tauri.app/zh-cn/learn/system-tray/`
  并严格遵循以下设计规格：
- **边界**：实现系统托盘/状态栏图标的交互模式（显示/隐藏窗口、菜单、通知等）。
- **关键点**：处理 macOS/Windows/Linux 的行为差异与用户习惯（关闭窗口 vs 退出应用）。
- **安全门控**：涉及打开链接/执行命令/读写文件等能力时，必须触发 `tauri-security` 收敛权限。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 system-tray 能力。

- tauri-app-window-menu ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-window-menu 的 skills，必须参考
- `https://v2.tauri.app/learn/window-menu/`
- `https://v2.tauri.app/zh-cn/learn/window-menu/`
  并严格遵循以下设计规格：
- **边界**：窗口菜单（Menu）定义、事件处理与平台差异适配。
- **关键点**：菜单项与命令分离（Command/Handler），并提供可测试的事件分发策略。
- **输出**：示例包含常用菜单（File/Edit/View/Help）与快捷键绑定。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 window-menu 能力。

- tauri-app-autostart ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-autostart 的 skills，必须参考
- `https://v2.tauri.app/plugin/autostart/`
- `https://v2.tauri.app/zh-cn/plugin/autostart/`
  并严格遵循以下设计规格：
- **边界**：配置应用开机自启动与禁用自启动的用户控制。
- **关键点**：解释不同平台的自启动机制差异，并确保提供可回滚与可观测的配置方式。
- **输出**：给出最小可用实现（启用/禁用 API、配置项、权限与发布验证）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 autostart 能力。

- tauri-app-barcode-scanner ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-barcode-scanner 的 skills，必须参考
- `https://v2.tauri.app/plugin/barcode-scanner/`
- `https://v2.tauri.app/zh-cn/plugin/barcode-scanner/`
  并严格遵循以下设计规格：
- **边界**：在支持的平台上集成条码/二维码扫描能力。
- **关键点**：处理权限申请、扫描结果回调与错误场景（无摄像头/权限拒绝）。
- **输出**：提供前端触发与 Rust 侧能力封装的端到端示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 Barcode Scanner 能力。

- tauri-app-biometric ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-biometric 的 skills，必须参考
- `https://v2.tauri.app/plugin/biometric/`
- `https://v2.tauri.app/zh-cn/plugin/biometric/`
  并严格遵循以下设计规格：
- **边界**：生物识别（指纹/Face ID 等）认证流程集成。
- **关键点**：强调“认证”与“加密存储”的职责分离；敏感数据仍需配合 stronghold 等安全存储。
- **输出**：提供统一的认证 API 与失败重试/降级策略。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 Biometric 能力。

- tauri-app-cli ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-cli 的 skills，必须参考
- `https://v2.tauri.app/plugin/cli/`
- `https://v2.tauri.app/zh-cn/plugin/cli/`
  并严格遵循以下设计规格：
- **边界**：为应用提供命令行参数解析与处理能力。
- **关键点**：定义参数 schema、处理启动参数与二次唤起参数（可结合 single-instance）。
- **输出**：提供“参数 -> 业务命令 -> 窗口行为”联动示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 CLI 能力。

- tauri-app-clipboard ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-clipboard 的 skills，必须参考
- `https://v2.tauri.app/plugin/clipboard/`
- `https://v2.tauri.app/zh-cn/plugin/clipboard/`
  并严格遵循以下设计规格：
- **边界**：读写系统剪贴板（文本/必要时扩展到图片等类型）。
- **关键点**：限制剪贴板能力的滥用风险（权限收敛、仅在用户操作触发时访问）。
- **输出**：提供常用用例（复制/粘贴/监听变更）的实现范式。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 clipboard 能力。

- tauri-app-deep-linking ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-deep-linking 的 skills，必须参考
- `https://v2.tauri.app/plugin/deep-linking/`
- `https://v2.tauri.app/zh-cn/plugin/deep-linking/`
  并严格遵循以下设计规格：
- **边界**：注册并处理应用深度链接（URL Scheme/Universal Links 等）。
- **关键点**：与 single-instance 联动，确保二次唤起参数能可靠传递到前端路由/业务逻辑。
- **安全门控**：对外部输入做严格校验与白名单限制，防止注入与越权。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 deep-linking 能力。

- tauri-app-dialog ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-dialog 的 skills，必须参考
- `https://v2.tauri.app/plugin/dialog/`
- `https://v2.tauri.app/zh-cn/plugin/dialog/`
  并严格遵循以下设计规格：
- **边界**：原生对话框能力（消息提示、确认框、文件选择等）。
- **关键点**：统一封装对话框调用，避免在业务代码中散落平台差异；处理异步与取消场景。
- **输出**：提供可复用的对话框服务层 API 设计（前端调用与 Rust 侧支持）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 dialog 能力。

- tauri-app-file-system ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-file-system 的 skills，必须参考
- `https://v2.tauri.app/plugin/file-system/`
- `https://v2.tauri.app/zh-cn/plugin/file-system/`
  并严格遵循以下设计规格：
- **边界**：文件系统读写、目录访问与路径权限控制。
- **关键点**：必须结合 Scope/Capabilities 精确限制可访问目录与文件模式，避免“任意路径读写”。
- **输出**：提供常用用例（选择文件、读写配置、导入导出）的安全实现方案。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 file-system 能力。

- tauri-app-geolocation ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-geolocation 的 skills，必须参考
- `https://v2.tauri.app/plugin/geolocation/`
- `https://v2.tauri.app/zh-cn/plugin/geolocation/`
  并严格遵循以下设计规格：
- **边界**：获取地理位置与相关权限管理。
- **关键点**：处理权限请求、精度/频率控制与隐私合规（最小必要、可关闭）。
- **输出**：提供统一的定位 API 与错误处理（权限拒绝/不可用/超时）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 geolocation 能力。

- tauri-app-global-shortcut ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-global-shortcut 的 skills，必须参考
- `https://v2.tauri.app/plugin/global-shortcut/`
- `https://v2.tauri.app/zh-cn/plugin/global-shortcut/`
  并严格遵循以下设计规格：
- **边界**：注册全局快捷键并在应用后台响应。
- **关键点**：处理快捷键冲突、平台差异与用户可配置；确保退出应用时释放注册。
- **输出**：提供“快捷键 -> 聚焦窗口/触发命令”的完整实现示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 global-shortcut 能力。

- tauri-app-haptics ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-haptics 的 skills，必须参考
- `https://v2.tauri.app/plugin/haptics/`
- `https://v2.tauri.app/zh-cn/plugin/haptics/`
  并严格遵循以下设计规格：
- **边界**：触觉反馈能力（主要面向移动端与支持的设备）。
- **关键点**：提供可降级策略（不支持时静默失败或替代提示），并避免过度打扰用户。
- **输出**：给出典型交互场景（按钮点击/成功失败提示）的实现范式。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 haptics 能力。

- tauri-app-http-client ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-http-client 的 skills，必须参考
- `https://v2.tauri.app/plugin/http-client/`
- `https://v2.tauri.app/zh-cn/plugin/http-client/`
  并严格遵循以下设计规格：
- **边界**：在 Rust 侧发起 HTTP 请求（可绕过部分 WebView 限制），并将结果安全暴露给前端。
- **关键点**：处理证书、代理、超时、重试与敏感信息保护；避免将任意 URL 请求能力暴露给不受信任输入。
- **安全门控**：结合 Capabilities/Scope 为请求域名与方法建立白名单。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 http-client 能力。

- tauri-app-localhost ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-localhost 的 skills，必须参考
- `https://v2.tauri.app/plugin/localhost/`
- `https://v2.tauri.app/zh-cn/plugin/localhost/`
  并严格遵循以下设计规格：
- **边界**：本地回环服务访问与相关配置。
- **关键点**：区分开发期 localhost 与生产期本地服务（sidecar/server）模式；避免扩大网络访问面。
- **输出**：提供可审计的配置与最小权限访问方案。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 localhost 能力。

- tauri-app-logging ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-logging 的 skills，必须参考
- `https://v2.tauri.app/plugin/logging/`
- `https://v2.tauri.app/zh-cn/plugin/logging/`
  并严格遵循以下设计规格：
- **边界**：统一日志采集、过滤、输出与持久化（开发与生产）。
- **关键点**：避免日志泄露敏感信息；提供分级（debug/info/warn/error）与可开关的诊断模式。
- **输出**：给出日志定位与上报的最佳实践（含 release 构建排障路径）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 logging 能力。

- tauri-app-nfc ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-nfc 的 skills，必须参考
- `https://v2.tauri.app/plugin/nfc/`
- `https://v2.tauri.app/zh-cn/plugin/nfc/`
  并严格遵循以下设计规格：
- **边界**：NFC 读写与会话管理（适用的平台与设备）。
- **关键点**：权限处理、用户交互提示与数据格式校验，避免将原始数据直接信任用于业务决策。
- **输出**：提供典型用例（读标签/写标签/一次性会话）的实现示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 nfc 能力。

- tauri-app-notification ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-notification 的 skills，必须参考
- `https://v2.tauri.app/plugin/notification/`
- `https://v2.tauri.app/zh-cn/plugin/notification/`
  并严格遵循以下设计规格：
- **边界**：本地通知/系统通知的发送与交互回调。
- **关键点**：处理权限请求、通知点击事件与深链联动；避免滥发通知。
- **输出**：提供统一通知服务与跨平台一致的行为定义。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 notification 能力。

- tauri-app-opener ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-opener 的 skills，必须参考
- `https://v2.tauri.app/plugin/opener/`
- `https://v2.tauri.app/zh-cn/plugin/opener/`
  并严格遵循以下设计规格：
- **边界**：打开外部链接/文件/目录等系统级“打开”能力。
- **关键点**：对可打开的协议与路径做白名单限制；避免成为钓鱼跳转与本地敏感文件泄露的入口。
- **输出**：提供安全的 opener 封装（仅允许 http/https、受控目录等）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 opener 能力。

- tauri-app-os-info ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-os-info 的 skills，必须参考
- `https://v2.tauri.app/plugin/os-info/`
- `https://v2.tauri.app/zh-cn/plugin/os-info/`
  并严格遵循以下设计规格：
- **边界**：采集系统信息（版本、架构等）用于诊断与兼容性判断。
- **关键点**：明确哪些信息可上报、如何脱敏；避免采集与业务无关的敏感字段。
- **输出**：提供“系统信息 -> 诊断报告/兼容性策略”的实现示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 os-info 能力。

- tauri-app-persisted-scope ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-persisted-scope 的 skills，必须参考
- `https://v2.tauri.app/plugin/persisted-scope/`
- `https://v2.tauri.app/zh-cn/plugin/persisted-scope/`
  并严格遵循以下设计规格：
- **边界**：将权限 scope 持久化到本地并在合适时机恢复/更新。
- **关键点**：避免“永久放权”；提供权限过期、撤销与重新授权机制。
- **输出**：给出与 capabilities/scope 配套的最佳实践与落地示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 persisted-scope 能力。

- tauri-app-positioner ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-positioner 的 skills，必须参考
- `https://v2.tauri.app/plugin/positioner/`
- `https://v2.tauri.app/zh-cn/plugin/positioner/`
  并严格遵循以下设计规格：
- **边界**：窗口定位与对齐策略（贴边、跟随托盘、屏幕多显示器适配）。
- **关键点**：处理多屏、缩放比例与不同平台窗口坐标系差异。
- **输出**：提供常见 UI 模式（弹出面板/下拉窗口）的定位实现示例。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 positioner 能力。

- tauri-app-process ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-process 的 skills，必须参考
- `https://v2.tauri.app/plugin/process/`
- `https://v2.tauri.app/zh-cn/plugin/process/`
  并严格遵循以下设计规格：
- **边界**：进程级能力（获取/管理当前进程信息或相关操作，依平台支持而定）。
- **关键点**：避免暴露高风险进程控制能力给不可信输入；所有能力必须受 Capabilities 约束。
- **输出**：提供“受控能力暴露”的设计模板（Rust 端封装 + 前端受限调用）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现 process 能力。

- tauri-app-wasm ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-wasm 的 skills，必须参考
- `https://crates.io/crates/tauri-wasm`
- `https://v2.tauri.app/develop/calling-rust/#wasm`
- `https://github.com/p1mo/tauri-wasm`
- `https://zhuanlan.zhihu.com/p/533025312`
- `https://blog.csdn.net/qq_63401240/article/details/147340217`
  并严格遵循以下设计规格：
- **功能**：在前端直接运行编译为 WASM 的 Rust 代码。
- **关键点**：区别于 Tauri 的 IPC 模式，WASM 是纯前端运行，适合高计算量但不涉及系统 API 的任务。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现高性能前端计算。

### 5. Mobile & Distribution (移动端与发布层)

- tauri-mobile ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-mobile 的 skills，必须参考
- `https://v2.tauri.app/mobile/`
- `https://v2.tauri.app/mobile/development/`
  并严格遵循以下设计规格：
- **边界**：移动端（Android/iOS）特有的初始化与调试。
- **关键点**：指导修改 Bundle ID 以符合移动端规范，以及前端响应式适配建议。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能进行移动端开发。

- tauri-build ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-build 的 skills，必须参考
- `https://v2.tauri.app/distribute/`
- `https://v2.tauri.app/distribute/app-store/`
- `https://v2.tauri.app/distribute/appimage/`
- `https://v2.tauri.app/distribute/aur/`
- `https://v2.tauri.app/distribute/crabnebula-cloud/`
- `https://v2.tauri.app/distribute/debian/`
- `https://v2.tauri.app/distribute/dmg/`
- `https://v2.tauri.app/distribute/google-play/`
- `https://v2.tauri.app/distribute/macos-application-bundle/`
- `https://v2.tauri.app/distribute/microsoft-store/`
- `https://v2.tauri.app/distribute/rpm/`
- `https://v2.tauri.app/distribute/snapcraft/`
- `https://v2.tauri.app/distribute/windows-installer/`
- `https://v2.tauri.app/distribute/sign/macos/`
- `https://v2.tauri.app/distribute/sign/windows/`
- `https://v2.tauri.app/distribute/sign/linux/`
- `https://v2.tauri.app/distribute/sign/ios/`
- `https://v2.tauri.app/distribute/sign/android/`
- `https://v2.tauri.app/distribute/pipelines/crabnebula-cloud/`
- `https://v2.tauri.app/distribute/pipelines/github/`
  并严格遵循以下设计规格：
- **边界**：生产环境构建、代码签名、安装包生成。
- **关键点**：区分 Debug 与 Release 构建，解释不同平台安装包格式（DMG, MSI, DEB, APK）。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现自动化构建发布。

- tauri-app-updater ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-app-updater 的 skills，必须参考
- `https://v2.tauri.app/plugin/updater/`
- `https://v2.tauri.app/zh-cn/plugin/updater/`
  并严格遵循以下设计规格：
- **功能**：配置 OTA 更新机制。
- **关键点**：生成签名密钥对 (`tauri signer generate`) 的流程，配置更新服务器 URL，以及在应用中实现自动检查更新的逻辑。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型基于此技能实现应用自更新功能。

### 6. Orchestration (编排层)

- tauri-orchestrator ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 tauri-orchestrator 的 skills，必须参考
- `https://v2.tauri.app/concept/architecture/`
- 上述所有 Skill Units
  并严格遵循以下设计规格：
- **角色**：Tauri Tech Lead（技术负责人）。
- **边界**：编排与规划，不直接替代具体 Skill 的落地实现。
- **功能**：接收模糊的高级需求，输出完整的开发计划和 Skill 调用链。
- **输出**：给出可执行的任务树（含依赖、顺序与验收点），并指明需要调用的 Skill Units。
- **核心逻辑**：
1.  **场景分析**：识别需求阶段（从零开始 vs 功能迭代）。
2.  **任务拆解**：将大需求拆解为 `tauri-scaffold` -> `tauri-app-shell` -> `tauri-ipc` 等原子步骤。
3.  **依赖管理**：强制检查前置条件（如：调用 `tauri-build` 前必须先调用 `tauri-config` 配置 ID）。
4.  **安全门控**：一旦检测到插件安装，自动触发 `tauri-security` 任务以配置权限。
  严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，一一对应，可以指导 大模型作为“总指挥”协调调用所有子技能完成复杂的开发任务。
