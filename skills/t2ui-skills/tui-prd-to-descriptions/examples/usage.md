# tui-prd-to-descriptions — 用法示例

输入：PRD 中的界面描述（或完整 PRD）。输出：三种块（TUI_RENDER、STITCH_PROMPT、PENCIL_PLAN 或 PENCIL_BATCH_DESIGN）。本技能不调用 Stitch 或 Pencil MCP。

---

## 示例：登录页 + 注册入口

**输入（PRD 片段）**：登录页，含账号输入框、密码输入框、登录按钮、忘记密码链接、注册入口；移动端优先，简洁风格。

### OUTPUT: TUI_RENDER（ASCII，补充 PRD）

```text
┌──────────────────────────────────────────────────────────────┐
│ 登录                                                    [X] │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  账号                                                        │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ 请输入手机号/邮箱                                       │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  密码                                                        │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ ••••••••                                                │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                    登  录                                │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  忘记密码？                    没有账号？去注册                │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: STITCH_PROMPT（供 stitch-skills）

```markdown
[Context]
Mobile-first login screen, clean and minimal. No clutter.

[Layout]
Single column: header "登录", form area (account field, password field, primary button), footer links (forgot password, register).

[Components]
- Navbar: title "登录", optional close.
- Input: account (placeholder "请输入手机号/邮箱"), password (masked).
- Primary button: "登录", full-width.
- Text links: "忘记密码？", "没有账号？去注册".

[Content]
Copy as above; no branding required unless in PRD.
```

### OUTPUT: PENCIL_PLAN（供 pencil-skills）

```text
PENCIL_PLAN

Step 1: mcp__pencil__open_document
Intent: Create or open design document.
Parameters: filePathOrTemplate: 'new' (or existing .pen path)

Step 2: mcp__pencil__get_editor_state
Intent: Get current root and components.
Parameters: include_schema: false

Step 3: mcp__pencil__batch_design
Intent: Create login screen frame with header, form area, button, links.
Parameters: operations for root frame, text "登录", input placeholders, button, link texts; ≤25 ops per call.

Step 4: mcp__pencil__get_screenshot
Intent: Verify layout.
Parameters: nodeId: <root or screen frame id from Step 3>
```

---

## 下游使用

- **ASCII**：插入 PRD 的「界面原型关联」或附录。
- **STITCH_PROMPT**：交给 stitch-skills（stitch-ui-prompt-architect / stitch-mcp-generate-screen-from-text）执行，得到 Stitch 原型。
- **PENCIL_PLAN**：交给 pencil-skills 或 Agent，按步骤调用 Pencil MCP 执行，得到 .pen 界面设计。

详见 [docs/boundary-and-outputs.md](../../docs/boundary-and-outputs.md)。
