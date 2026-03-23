# stitch-ui-design-spec-generator — Usage Examples

Use this skill internally (by thinking) before creating a Stitch project or generating a prompt. Input may be a one-shot user request or a PRD document/summary; see [docs/prd-to-stitch-workflow.md](../../docs/prd-to-stitch-workflow.md) for the full PRD-driven flow.

---

## 1. One-shot natural language → JSON

**Input (user request):**
> A cyberpunk login page for a gaming platform.

**Output (design spec JSON):**
```json
{
  "theme": "DARK",
  "primaryColor": "#00FF88",
  "font": "Orbitron",
  "roundness": "Low",
  "density": "COMFORTABLE",
  "designMode": "HIGH_FIDELITY",
  "styleKeywords": ["Cyberpunk", "Neon", "Gaming", "High contrast"],
  "deviceType": "DESKTOP"
}
```

**Input (user request):**
> A clean medical dashboard for doctors, desktop only.

**Output (design spec JSON):**
```json
{
  "theme": "LIGHT",
  "primaryColor": "#2563EB",
  "font": "Inter",
  "roundness": "Low",
  "density": "COMPACT",
  "designMode": "HIGH_FIDELITY",
  "styleKeywords": ["Medical", "Clean", "Professional", "Data-dense"],
  "deviceType": "DESKTOP"
}
```

---

## 2. PRD summary / fragment → JSON

When the user provides a PRD file path or pasted PRD content, extract **function overview** and **page/screen list** (and any visual/theme preferences from non-functional requirements), then apply the same Logic Rules (Analyze Tone, Determine Device, Determine Mode).

**Input (PRD summary extracted from e.g. docs/登录_PRD.md):**
- Function overview: 用户注册、登录、密码找回、账户安全；多端统一认证（Web/移动端）。
- Pages: 登录页、注册页（手机号/邮箱）、密码找回、账户安全设置。
- Non-functional: 安全性、性能；兼容主流浏览器与 iOS/Android 10+。

**Output (design spec JSON):**
```json
{
  "theme": "LIGHT",
  "primaryColor": "#4A90E2",
  "font": "Inter",
  "roundness": "Medium",
  "density": "COMFORTABLE",
  "designMode": "HIGH_FIDELITY",
  "styleKeywords": ["Auth", "Secure", "Multi-device", "Clean"],
  "deviceType": "MOBILE"
}
```

*(Defaulting to MOBILE here for “多端” with auth flows often mobile-first; could be overridden if user specifies “desktop admin only”.)*

**Input (PRD fragment — lifestyle/food):**
- 美食推荐 App，暖色调，圆角卡片，主色橙红。

**Output (design spec JSON):**
```json
{
  "theme": "LIGHT",
  "primaryColor": "#E85D04",
  "font": "Nunito",
  "roundness": "High",
  "density": "COMFORTABLE",
  "designMode": "HIGH_FIDELITY",
  "styleKeywords": ["Food", "Warm", "Friendly", "Cards"],
  "deviceType": "MOBILE"
}
```

---

After producing the JSON, the next steps in the PRD-driven workflow are: choose a framework (stitch-ui-design-spec-*), then use stitch-ui-prompt-architect to build the full Stitch prompt. See [docs/prd-to-stitch-workflow.md](../../docs/prd-to-stitch-workflow.md).
