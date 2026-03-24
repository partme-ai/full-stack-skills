# Usage Example

## Scenario: Creating a "Music App Designer" Skill

**User Request**:
> "I want to add a skill to help design music player apps with Stitch."

**Agent Action**:
1.  **Analyze**: Domain = "Music App". Skill Name = `stitch-ui-music-designer`.
2.  **Scaffold**: Create `skills/stitch-ui-music-designer`.
3.  **Implement `SKILL.md`**:

```markdown
---
name: stitch-ui-music-designer
description: Specialized prompt architect for Music Player and Streaming screens.
---

# Music Screen Designer

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" or when orchestrating a Stitch design task.

This skill helps you construct high-quality prompts for Music App flows (Player, Playlist, Library).

## Prompt Template

```text
[Context]
Mobile high-fidelity Music Player screen for [App Name]. [Style] aesthetic.

[Layout]
Header: Title + back icon.
Body: Album art -> track info -> progress -> controls -> up-next.
Footer: optional lyrics entry.

[Components]
- Album cover (square with radius 12)
- Track title + artist (type scale aligned)
- Scrubber + time labels
- Primary play/pause + secondary controls
```
```

4.  **Implement `examples/usage.md`**:

```markdown
# Usage Example

## 1. Spotify-like Player
**User**: "Dark mode player like Spotify."
**Output**:
```text
[Context]
Mobile music player screen. Dark mode. Minimalist controls. Emphasis on album art and progress.

[Layout]
Top bar: back + title.
Main: album art -> track info -> progress -> controls.

[Components]
- Primary play/pause button (large)
- Previous/next, shuffle/repeat toggles
- Progress bar with time labels
```

## 2. Desktop Library + Player
**User**: "Design a desktop music library with a mini player."
**Output**:
```text
[Context]
Desktop music library screen with a persistent mini player. Clean, data-first layout.

[Layout]
Left: sidebar navigation.
Center: library table/grid.
Bottom: mini player bar (always visible).

[Components]
- Sidebar items (Library / Playlists / Artists)
- Search input + filter chips
- Track list table with actions
- Mini player with play/pause and scrubber
```
```

5.  **Validation**:
    *   Does it have the Stitch Constraint? Yes.
    *   Does it separate design from execution? Yes (it returns a prompt only).
    *   Does it follow strict output pattern? Yes (`[Context] [Layout] [Components]`, single code block per response).
