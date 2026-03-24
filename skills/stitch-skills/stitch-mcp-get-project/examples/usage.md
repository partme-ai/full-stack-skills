# Usage Example

## 1. Get Project Details

**User Input:**
> "What is the theme of project 'projects/123'?"

**Agent Action:**
```json
{
  "name": "get_project",
  "arguments": {
    "name": "projects/123"
  }
}
```

**Output:**
```json
{
  "name": "projects/123",
  "title": "Travel App",
  "designTheme": {
    "colorMode": "LIGHT",
    "primaryColor": "#007AFF",
    "font": "INTER"
  },
  "deviceType": "MOBILE"
}
```

## 2. Context Loading
Use this skill when switching context to an old project to understand its global settings (Theme, Device Type) before generating new screens.
