          
Stitch MCP 是一套强大的 AI UI 生成工具，基于你提供的 MCP 定义文件，我为你设计了一套完整的 **"AI-Driven UED Workflow" (AI 驱动的用户体验设计工作流)**。

这份规划旨在将 Stitch 的原子能力封装为 Agent 可调用的高阶技能（Skills），并建立严谨的 "设计 -> 执行" 规范，确保生成的 UI 既符合用户创意，又具备工程落地的高质量。

---

### 🎨 Stitch Agent Skills 体系规划

我将 Skills 分为三层：**基础原子技能层**（直接映射 MCP）、**高级设计技能层**（Prompt Engineering & 规范化）、**工作流编排层**（全链路落地）。

#### 1. 基础原子技能层 (Atomic Skills)
这部分直接封装 MCP 工具，供 Agent 在执行具体动作时调用。

| Skill Name | 对应 MCP | 描述与用途 |
| :--- | :--- | :--- |
| `stitch_project_create` | `create_project` | **创建项目容器**。用于初始化一个新的设计空间，设定全局的主题（颜色、字体、圆角）和设备类型（Mobile/Desktop）。 |
| `stitch_project_list` | `list_projects` | **检索项目列表**。用于查找现有的设计项目，支持按所有者筛选。 |
| `stitch_project_get` | `get_project` | **获取项目详情**。用于读取项目的元数据、全局主题配置等上下文信息。 |
| `stitch_screen_generate` | `generate_screen_from_text` | **核心生成能力**。输入 Prompt，输出 UI 界面。支持指定模型（Gemini 3 Pro/Flash）和设备类型。 |
| `stitch_screen_list` | `list_screens` | **浏览页面列表**。查看当前项目下已经生成的页面概览。 |
| `stitch_screen_get` | `get_screen` | **获取页面详情**。获取特定页面的 HTML 代码、截图 URL 和 Figma 导出文件。 |

#### 2. 高级设计技能层 (Design Logic Skills)
这部分是你要求的 **"先设计，后执行"** 的核心。Agent 不直接调用生成工具，而是先调用这些 Skill 来“思考”和“规范”设计。

*   **`design_spec_generator` (视觉交互 DNA 规范生成)**
    *   **输入**: 用户模糊需求（如 "做一个小清新的宠物店 App"）。
    *   **输出**: 结构化的设计规范 JSON。包含：配色方案（主色、辅色、背景色）、排版系统（字体、字号）、圆角风格、阴影深度、组件风格。
    *   **作用**: 对应目录下的 `5、视觉与交互 DNA 规范模板.md`，确保项目风格统一。

*   **`ui_prompt_architect` (UI 提示词架构师)**
    *   **输入**: 页面功能描述 + 设计规范。
    *   **输出**: **Stitch-Ready Prompt**。这是专门针对 Stitch 优化过的提示词，包含布局结构、组件细节、状态描述。
    *   **作用**: 将 "登录页" 翻译成 "Mobile screen, minimal style. Top 1/3: Brand logo centered. Middle: Input field for 'Email', Input field for 'Password'. Bottom: Primary button 'Login', Secondary link 'Forgot Password'. White background, #007AFF accent."

#### 3. UX 落地操作指南 (UX Implementation Guide)

这是一套标准作业程序 (SOP)，指导 Agent 如何一步步完成任务。

**阶段一：项目初始化 (Setup)**
1.  **用户意图分析**: 确定是新项目还是在旧项目新增页面。
2.  **风格定义**: 调用 `design_spec_generator` 确定 Design Theme。
3.  **创建/选择项目**: 调用 `stitch_project_create` (带上定义好的 Theme) 或 `stitch_project_list`。

**阶段二：页面设计与生成 (Design & Generate)**
1.  **需求转化**: 用户输入需求 -> 调用 `ui_prompt_architect` -> 获得 Stitch Prompt。
2.  **执行生成**: 调用 `stitch_screen_generate` (传入 Stitch Prompt + ProjectID)。
3.  **结果验证**: 获取生成结果，展示给用户（Screenshot）。

**阶段三：交付与迭代 (Deliver)**
1.  **代码获取**: 调用 `stitch_screen_get` 获取 HTML/Figma。
2.  **资产归档**: 将生成的资源记录到项目文档中。

---

### 📘 UED 交互指南 (Interaction Guidelines)

为了让 Agent 更好地扮演资深设计师，制定以下交互原则：

**1. 视觉语言标准化 (Visual Vocabulary)**
Agent 在与 Stitch 交互时，必须使用标准的视觉术语：
*   **布局**: Header, Footer, Sidebar, Grid, Hero Section, Card Layout.
*   **组件**: FAB (Floating Action Button), Modal, Toast, Carousel, Accordion, Tab Bar.
*   **风格**: Flat, Material, Neomorphism, Glassmorphism, Brutalism, Minimalist.

**2. 设备与响应式约束**
*   **Mobile**: 默认宽度 375px/393px，强调垂直滚动，Touch Target > 44px。
*   **Desktop**: 强调栅格系统，利用宽屏优势做多栏布局。

**3. 渐进式增强提示 (Progressive Prompting)**
*   不要试图一次性生成极其复杂的逻辑。
*   策略：**先骨架，后肉体**。
    *   *Bad*: "做一个像淘宝一样的电商首页，要有秒杀倒计时和推荐算法流。"
    *   *Good*: "E-commerce app home screen. Top: Search bar and category icons. Middle: Featured banner carousel. Bottom: 2-column product grid with image, title, and price."

---

### 🚀 实战案例：设计一个登录页面

按照要求 #5，演示 Agent 的执行路径：

**用户指令**: "帮我设计一个登录页面，风格要科技感强一点，暗色调。"

**Agent 执行步骤**:

1.  **[Skill: design_spec_generator] 思考与规划**:
    *   *分析*: 风格=科技感 (Cyberpunk/Futuristic)，色调=Dark Mode。
    *   *输出设计规范*:
        *   Theme: Dark
        *   Primary Color: Neon Blue (#00F0FF) or Neon Purple.
        *   Font: Inter or Roboto Mono.
        *   Roundness: Low (Sharp edges).

2.  **[Skill: ui_prompt_architect] 构建提示词**:
    *   *构建*: 基于上述规范和 "登录页" 功能。
    *   *输出 Prompt*:
        > "Dark mode mobile login screen. Cyberpunk aesthetic. Background: Deep dark blue (#0A0A12) with subtle geometric glowing lines.
        > Center: App logo with neon glow effect.
        > Form area: Two input fields with dark semi-transparent background and neon blue borders for 'Username' and 'Password'.
        > Action: Large rectangular 'LOGIN' button, solid neon blue background, white bold text.
        > Footer: 'Create Account' link in grey text. Tech font style."

3.  **[Skill: stitch_screen_generate] 调用 MCP**:
    *   `projectId`: [Current Project ID]
    *   `prompt`: [The Prompt from Step 2]
    *   `deviceType`: MOBILE
    *   `modelId`: GEMINI_3_PRO

4.  **[Skill: stitch_screen_get] 获取结果**:
    *   向用户展示生成的截图，询问是否满意。

---

### 下一步计划

如果您认可这个规划，我将开始编写：
1.  **Agent Skills 代码/Prompt 模板**：实现上述的 `design_spec_generator` 等逻辑。
2.  **集成 MCP**：确保 Agent 可以通过 `Task` 或 `Tool` 的形式调用 Stitch MCP。
3.  **文档输出**：生成完整的 `.md` 指南文档，放入您的 `2.0、模板` 目录中。

请确认是否开始执行创建？