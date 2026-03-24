# Usage Example

## 1. List User's Projects

**User Input:**
> "Show me my existing projects."

**Agent Action:**
```json
{
  "name": "list_projects",
  "arguments": {
    "filter": "view=owned"
  }
}
```

## 2. List Shared Projects

**User Input:**
> "Show me projects shared with me."

**Agent Action:**
```json
{
  "name": "list_projects",
  "arguments": {
    "filter": "view=shared"
  }
}
```

**Output:**
```json
{
  "projects": [
    {
      "name": "projects/123",
      "title": "Travel App",
      "updateTime": "2023-10-26T15:00:00Z"
    },
    {
      "name": "projects/456",
      "title": "Dashboard",
      "updateTime": "2023-10-25T09:30:00Z"
    }
  ]
}
```
