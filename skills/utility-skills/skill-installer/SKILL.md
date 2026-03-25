---
name: skill-installer
description: "Discovers, installs, and manages AI skills from the PartMe marketplace. Acts as the local package manager for Knowledge-as-a-Service (KaaS) and Tool-as-a-Service (TaaS) skills. Use when the user wants to search for available skills, install a new skill into their environment, or list currently installed skills."
---

## When to use this skill

Use this skill whenever the user wants to:
- Search the PartMe marketplace for available skills by keyword or category
- Install a new skill into their local environment
- List or audit currently installed skills
- Discover skills related to a specific technology (e.g., "vue", "database", "testing")

## How to use this skill

### Workflow

1. **Search** for skills matching the user's needs
2. **Review** the results (name, description, path)
3. **Install** the chosen skill
4. **Verify** installation via the list command

### Example: Find and Install a Vue Skill

```bash
# Step 1: Search for Vue-related skills
skill-installer(action="search_skills", query="vue")
# Returns: [{"name": "vue3", "description": "Vue 3 component development", "path": "./skills/vue3"}, ...]

# Step 2: Install the skill
skill-installer(action="install_skill", skill_path="./skills/vue3")
# Returns: {"status": "installed", "name": "vue3"}

# Step 3: Verify installation
skill-installer(action="list_installed_skills")
# Returns: [{"name": "vue3", "status": "active"}, ...]
```

## Tools Reference

| Tool | Input | Output |
|------|-------|--------|
| `search_skills` | `query` (string) | JSON list of matching skills with descriptions and paths |
| `install_skill` | `skill_path` (string) | Confirmation of installation |
| `list_installed_skills` | None | JSON list of installed skills with status |

## Best Practices

1. **Search before installing** - Check what is available to avoid duplicates
2. **Use specific queries** - Search "avue-crud" rather than just "crud" for better results
3. **Verify after install** - Run `list_installed_skills` to confirm the skill is active

## Keywords

skill installer, marketplace, KaaS, TaaS, install skill, search skills, PartMe, skill management
