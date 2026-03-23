# 技能分组映射表

本文档定义 `skills/` 下按组子目录与技能名的对应关系，用于「先分组、后迁移」的目录重组。每组对应 `skills/<组目录名>/<skill-name>/`，且 SKILL.md 的 frontmatter `name` 必须等于 `<skill-name>`（Agent Skills 规范）。**已入 marketplace 的技能路径均应对应下表某一组**；表末 **threejs-skills / vscode-skills** 为仓库内已存在目录、**尚未** 写入 `marketplace.json` 的组。若某技能目录尚未创建（仅 marketplace 有引用），则在对应组下注明「待补目录」。

## 已确定组（已迁移或待迁移）

| 组目录名 | 技能名列表（即目录名） | 数量 | 说明 |
|----------|------------------------|------|------|
| **ascii-skills** | ascii-ansi-colorizer, ascii-cli-logo-banner, ascii-cli-logo-banner-figletjs, ascii-cli-logo-banner-python, ascii-diagram-boxflow, ascii-image-to-ascii, ascii-mini-charts, ascii-motd-profile-banner, ascii-progress-and-spinner, ascii-table-renderer, ascii-terminal-animation-pack, ascii-text-art-library, cli-ascii-logo | 13 | 与 marketplace 中 development-skills-utils 的 ASCII 相关项一致 |
| **cocos-skills** | cocos2d-x | 1 | 游戏引擎；后续可增加 Cocos Creator 等 |
| **antd-skills** | ant-design-vue, ant-design-react, ant-design-mobile, ant-design-mini | 4 | Ant Design 各端（Vue/React/移动端/小程序） |
| **avue-skills** | avue, avue-crud, avue-form | 3 | Avue 基于 Element 的低代码/表单/CRUD 技能 |
| **ddd-skills** | ddd-clean-architecture, ddd-cola, ddd-event-driven, ddd-hexagonal-architecture, ddd-microservices, ddd4j-project-creator | 6 | DDD 架构与 COLA/六边形/整洁/事件驱动/微服务及 ddd4j 项目创建 |
| **docker-skills** | docker, docker-compose | 2 | Docker 与 Docker Compose 容器化技能 |
| **ocrmypdf-skills** | ocrmypdf, ocrmypdf-api, ocrmypdf-batch, ocrmypdf-image, ocrmypdf-optimize | 5 | OCRmyPDF 核心 OCR、图像处理、优化压缩、批量处理、Python API |
| **react-skills** | react, react-hooks, react-native, react-native-project-creater, redux, nextjs | 6 | React 与 React Hooks、React Native、Redux、Next.js |
| **spring-skills** | spring-ai, spring-ai-alibaba, spring-boot, spring-cloud, spring-cloud-alibaba, spring-data-jpa, spring-security | 7 | Spring 生态：Boot、Cloud、Cloud Alibaba、AI、AI Alibaba、Security、Data JPA |
| **uniapp-skills** | uniapp-ad, uniapp-cloud, uniapp-mini, uniapp-native-app, uniapp-native-plugin, uniapp-plugin, uniapp-project, uniapp-project-creator, uniapp-ucharts, uniapp-uview, uniappx-project, uniappx-project-creator, uniappx-uview-pro | 13 | UniApp / UniApp-x 项目创建、uView、uCharts、云开发、广告、小程序、原生 App/插件等 |
| **uview-skills** | uview-vue2, uview-pro-vue3 | 2 | uView 2.x 与 uView Pro (Vue 3) UI 组件库 |
| **vue-skills** | vue2, vue3, vue-router, vue-router-v3, vue-router-v4, vuex-vue2, pinia | 7 | Vue 2/3、Vue Router、Vuex、Pinia 状态管理 |
| **flutter-skills** | flutter, flutter-project-creater | 2 | Flutter 跨平台开发与项目创建 |
| **nodejs-skills** | express, fastify, nestjs, koa | 4 | Node.js 后端框架（Express、Fastify、NestJS、Koa） |
| **electron-skills** | electron, electron-egg, upgradeLink | 3 | Electron 桌面应用与 Electron Egg、升级链接等 |
| **drawio-skills** | drawio-architecture, drawio-flowchart | 2 | Draw.io 架构图与流程图绘制 |
| **python-skills** | django, fastapi, flask | 3 | Python 后端框架（Django、FastAPI、Flask） |
| **go-skills** | gin, gin-gonic | 2 | Go 后端框架（Gin、Gin-Gonic） |
| **build-skills** | webpack, rollup, parcel, rspack, vite, dart-sass | 6 | 前端构建与 CSS 预处理器 |
| **vue-ui-skills** | element-plus-vue3, bootstrap-vue3, vant-vue3, layui-vue3 | 4 | Vue 生态 UI 组件库（非 Ant/uView/Avue） |
| **angular-skills** | angular | 1 | Angular 框架 |
| **svelte-skills** | svelte | 1 | Svelte 框架 |
| **mobile-native-skills** | android-kotlin, ios-swift | 2 | 原生移动端 |
| **chart-skills** | lime-echart, ucharts | 2 | 图表组件 |
| **dev-utils-skills** | code-generator, test-writer, java-code-comments, mybatis-plus-generator, documentation-builder, full-stack-doc, mcp-builder, webapp-testing, frontend-design, web-artifacts-builder, theme-factory, agent-browser, maven-search | 13 | 开发工具链（与 development-skills-utils 对应） |
| **design-skills** | algorithmic-art, brand-guidelines, canvas-design, figma, figma-ai, sketch, adobe-xd, dalle, uizard, galileo-ai, runway-ml, framer | 12 | 设计与 AI 绘图（midjourney/stable-diffusion/axure/modao 待补目录则入本组） |
| **document-skills** | docx, pptx, pdf, xlsx, doc-coauthoring, api-doc-generator, processon-mindmap, mermaid, plantuml | 9 | 文档与图表（与 document 插件对应） |
| **testing-skills** | jest, vitest, pytest, junit, cypress, playwright, selenium, appium, detox | 9 | 测试框架与 E2E/移动端测试 |
| **devops-skills** | gitlab-ci, github-actions, kubernetes, terraform, ansible, cloudformation | 6 | CI/CD 与 IaC（jenkins 待补目录则入本组） |
| **database-skills** | postgresql, oracle, redis, elasticsearch, dbeaver | 5 | 数据库与工具（mysql/mongodb/navicat 待补目录则入本组） |
| **social-skills** | internal-comms, slack-gif-creator | 2 | 协作与社交 |
| **teaching-skills** | course-designer, learning-assessor, teaching-resource-generator | 3 | 教学与课程设计 |
| **utility-skills** | skill-creator, skill-sop-creator, skill-installer | 3 | 技能生态工具 |
| **stitch-skills** | stitch-design-md, stitch-mcp-create-project, stitch-mcp-generate-screen-from-text, stitch-mcp-get-project, stitch-mcp-get-screen, stitch-mcp-list-projects, stitch-mcp-list-screens, stitch-react-components, stitch-remotion, stitch-shadcn-ui, stitch-skill-creator, stitch-ued-guide, stitch-ui-design-spec-bootstrap, stitch-ui-design-spec-element-plus, stitch-ui-design-spec-generator, stitch-ui-design-spec-layui, stitch-ui-design-spec-uview, stitch-ui-design-spec-uviewpro, stitch-ui-design-spec-vant, stitch-ui-design-variants, stitch-ui-designer, stitch-ui-prompt-architect, stitch-uview-components, stitch-uviewpro-components, stitch-vue-bootstrap-components, stitch-vue-element-components, stitch-vue-layui-components, stitch-vue-vant-components | 28 | Stitch MCP 扩展技能（不含官方 google-labs-code/stitch-skills 已有项） |
| **nvm-skills** | nvm, nvm-install, nvm-setup, nvm-verify, nvm-usage-basics, nvm-defaults-and-nvmrc, nvm-global-packages, nvm-mirror-and-auth, nvm-shell-integration, nvm-docker-ci, nvm-uninstall, nvm-misc, nvm-project-meta, nvm-troubleshooting-macos, nvm-troubleshooting-linux | 15 | Node Version Manager：安装、配置、验证、用法、.nvmrc、全局包、镜像、Shell 集成、Docker/CI、卸载、故障排查等 |
| **threejs-skills** | threejs-dev-setup, threejs-scenes, threejs-camera, threejs-lights, threejs-materials, threejs-node-tsl, threejs-textures, threejs-geometries, threejs-math, threejs-objects, threejs-animation, threejs-audio, threejs-loaders, threejs-renderers, threejs-postprocessing, threejs-helpers, threejs-controls, threejs-webxr | 18 | three.js 官方文档向技能族（与 mermaid 深度对齐）；**当前未写入 marketplace.json**，见 [threejs-skills/README.md](../skills/threejs-skills/README.md) |
| **vscode-skills** | vscode-deploy-package, vscode-feature-command, vscode-feature-webview, vscode-project-init | 4 | VS Code 扩展开发；**当前未写入 marketplace.json** |

## 待补充组

| 组目录名 | 状态 | 说明 |
|----------|------|------|
| **bt-skills** | 待补充 | 组目录名与技能列表由维护者后续定义 |

## 迁移后路径示例

- 迁移前：`skills/ascii-table-renderer/SKILL.md`
- 迁移后：`skills/ascii-skills/ascii-table-renderer/SKILL.md`
- marketplace 中对应项：`"./skills/ascii-skills/ascii-table-renderer"`
