# End-to-End Workflow Example

## Scenario: Creating a Pet Adoption App

**User**: "I want to design a pet adoption app called 'PawPals'. Start with a warm, friendly home screen."

### Step 1: Initialize Project
*Orchestrator invokes MCP tool `create_project`*

**Agent Action**:
```json
{
  "name": "create_project",
  "arguments": {
    "title": "PawPals"
  }
}
```
**Result**: Project created. Resource name: `projects/123`.

**Agent Note**: Extract numeric project ID `123` for `generate_screen_from_text`.

### Step 2: Design Analysis
*Orchestrator invokes `stitch-ui-design-spec-generator`*

**Agent Action**:
```json
{
  "name": "stitch-ui-design-spec-generator",
  "arguments": {
    "request": "Pet adoption app, warm friendly style"
  }
}
```
**Result**:
```json
{
  "theme": "LIGHT",
  "primaryColor": "#FF9F43", // Warm Orange
  "roundness": "HIGH",
  "font": "Nunito",
  "styleKeywords": ["Friendly", "Playful", "Clean"],
  "deviceType": "MOBILE"
}
```

### Step 3: Prompt Construction
*Orchestrator invokes `stitch-ui-prompt-architect`*

**Agent Action**:
```json
{
  "name": "stitch-ui-prompt-architect",
  "arguments": {
    "userRequest": "Home screen",
    "designSpec": { ... } // JSON from Step 2
  }
}
```
**Result**: "Mobile High-Fidelity home screen for PawPals. Friendly aesthetic. Light mode. Background: Soft cream. Components: 'Find your friend' rounded search bar. 'Categories' horizontal scroll (Dogs, Cats, Birds). 'Featured' vertical list of pet cards with large rounded photos, names, and 'Adopt' pill buttons. Bottom Nav: Home, Favorites, Messages, Profile."

### Step 4: Generation
*Orchestrator invokes MCP tool `generate_screen_from_text`*

**Agent Action**:
```json
{
  "name": "generate_screen_from_text",
  "arguments": {
    "projectId": "123",
    "prompt": "Mobile High-Fidelity home screen for PawPals...",
    "deviceType": "MOBILE",
    "modelId": "GEMINI_3_PRO"
  }
}

### Step 5: Retrieve the Generated Screen
*Orchestrator invokes MCP tool `list_screens`*

**Agent Action**:
```json
{
  "name": "list_screens",
  "arguments": {
    "projectId": "projects/123"
  }
}
```

Then select a screen and invoke `get_screen` to retrieve the screenshot/HTML.
### Step 6: Presentation
### Step 5: Presentation
