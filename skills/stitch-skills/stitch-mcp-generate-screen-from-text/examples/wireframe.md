# Wireframe Examples

## 1. Low-Fidelity Sketch (Mobile)
**User Request**: "Just give me a rough wireframe for a sign-up flow."

**Agent Action**:
```json
{
  "name": "generate_screen_from_text",
  "arguments": {
    "projectId": "3780309359108792857",
    "prompt": "Mobile Wireframe sketch for a Sign-Up flow. Blueprint aesthetic. Monochrome. Layout: Simple vertical stack. Components: Placeholder box for Logo. Rectangle for 'Email' input. Rectangle for 'Password' input. Rectangle for 'Confirm Password'. Button placeholder 'Register'. Text placeholder 'Already have an account?'. No colors, just outlines.",
    "deviceType": "MOBILE",
    "modelId": "GEMINI_3_FLASH"
  }
}
```

## 2. Desktop Wireframe (Landing Page)
**User Request**: "Wireframe for a landing page structure."

**Agent Action**:
```json
{
  "name": "generate_screen_from_text",
  "arguments": {
    "projectId": "3780309359108792857",
    "prompt": "Desktop Wireframe sketch for a Landing Page. Blueprint aesthetic. Monochrome. Layout: Classic landing page structure. Hero Section: Large X placeholder for image, Lines for headline. Features Section: 3-column grid with icon placeholders. Pricing Section: 3 pricing card outlines. Footer: Simple link list placeholder.",
    "deviceType": "DESKTOP",
    "modelId": "GEMINI_3_FLASH"
  }
}
```
