# Desktop Dashboard Examples

## 1. SaaS Analytics Dashboard
**User Request**: "Build a dashboard showing revenue and user growth."

**Agent Action**:
```json
{
  "name": "generate_screen_from_text",
  "arguments": {
    "projectId": "3780309359108792857",
    "prompt": "Desktop High-Fidelity analytics dashboard for a SaaS platform. Enterprise Clean aesthetic. Light mode. Layout: Left sidebar navigation + Main content area. Sidebar: Dashboard, Users, Revenue, Settings. Main: Top row with 4 KPI cards (Total Revenue, Active Users, Churn Rate). Middle: Large line chart showing 'MRR Growth'. Bottom: Recent transactions data table.",
    "deviceType": "DESKTOP",
    "modelId": "GEMINI_3_PRO"
  }
}
```

## 2. Admin Panel (Dark Mode)
**User Request**: "Dark mode admin panel for server monitoring."

**Agent Action**:
```json
{
  "name": "generate_screen_from_text",
  "arguments": {
    "projectId": "3780309359108792857",
    "prompt": "Desktop High-Fidelity admin console for Server Monitoring. Developer aesthetic. Dark mode. Layout: Dense information grid. Header: Global status 'All Systems Operational' (Green). Content: Grid of server status cards (CPU usage, Memory, Uptime). Terminal-like logs widget at the bottom. Color palette: Dark grey backgrounds, monospaced fonts, green/red status indicators.",
    "deviceType": "DESKTOP",
    "modelId": "GEMINI_3_PRO"
  }
}
```
