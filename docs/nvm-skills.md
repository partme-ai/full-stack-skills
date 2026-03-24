# nvm Agent Skills 规划清单

- nvm-install ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-install 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：安装与更新 nvm（install.sh + PROFILE/NVM_DIR/NVM_SOURCE 等环境变量）。
- **关键点**：区分 curl/wget 安装方式；说明脚本自动写入 profile 的行为与手动指定 PROFILE 的方式。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型基于此技能完成 nvm 安装与更新。

- nvm-setup ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-setup 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：加载 nvm 的 shell 配置与环境变量（NVM_DIR、nvm.sh、bash/zsh/fish）。
- **关键点**：处理 XDG_CONFIG_HOME 目录差异；提供 --no-use 方式与手动 source 的路径。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型基于此技能完成 nvm 环境初始化。

- nvm-verify ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-verify 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：安装完成后的验证路径（nvm --version、node -v、npm -v）。
- **关键点**：识别 PATH 未更新、profile 未加载的常见原因与修复。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成安装验证与初始排错。

- nvm-usage-basics ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-usage-basics 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：安装、切换、列出 Node 版本（nvm install/use/ls/ls-remote）。
- **关键点**：LTS 版本选择与 system Node 版本的使用策略。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成日常版本管理。

- nvm-defaults-and-nvmrc ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-defaults-and-nvmrc 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：默认 Node 版本设置与 .nvmrc 的使用。
- **关键点**：进入目录自动 nvm use 的策略与 shell 集成方法。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成项目级版本固定。

- nvm-global-packages ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-global-packages 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：迁移全局包与默认全局包文件（nvm install --reinstall-packages-from、default-packages）。
- **关键点**：多版本并存时的全局包一致性策略与风险提示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成全局包迁移。

- nvm-mirror-and-auth ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-mirror-and-auth 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：使用 Node 二进制镜像与授权 header 的配置。
- **关键点**：镜像地址、认证 header 的环境变量配置与常见网络问题规避。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型在受限网络中安装 Node。

- nvm-shell-integration ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-shell-integration 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：bash/zsh/fish 的深入集成与自动切换机制。
- **关键点**：Deeper Shell Integration 的启用方式与 PATH 恢复策略。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完善多 Shell 环境兼容。

- nvm-docker-ci ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-docker-ci 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：Docker 与 CI/CD 场景下的 nvm 安装与使用。
- **关键点**：BASH_ENV 的非交互加载方式与 ENTRYPOINT 加载策略。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型在容器与流水线中稳定使用 nvm。

- nvm-troubleshooting-macos ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-troubleshooting-macos 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：macOS 常见问题诊断与修复。
- **关键点**：shell profile 选择、权限、PATH 优先级等问题处理路径。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成 macOS 场景排障。

- nvm-troubleshooting-linux ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-troubleshooting-linux 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：nvm Linux 常见问题诊断与修复。
- **关键点**：不同发行版 shell/profile 差异与 PATH 修复。
  一一对应，如同 
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成 nvm Linux 场景排障。

- nvm-uninstall ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 nvm-uninstall 的 skills，必须参考
- `https://github.com/nvm-sh/nvm/blob/master/README.md`
  并严格遵循以下设计规格：
- **边界**：卸载与清理（NVM_DIR、profile 配置移除）。
- **关键点**：恢复系统 Node 或其他版本管理器的 PATH 优先级。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型安全卸载 nvm。
