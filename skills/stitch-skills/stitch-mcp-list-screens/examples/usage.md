# Usage Example

## 1. List All Screens

**User Input:**
> "Show me all screens in this project."

**Agent Action:**
```json
{
  "name": "list_screens",
  "arguments": {
    "projectId": "projects/123456789"
  }
}
```

**Output:**
```json
{
  "screens": [
    {
      "name": "projects/123/screens/abc",
      "title": "Login Screen",
      "screenshot": { "downloadUrl": "..." }
    },
    {
      "name": "projects/123/screens/def",
      "title": "Home Screen",
      "screenshot": { "downloadUrl": "..." }
    }
  ]
}
```
