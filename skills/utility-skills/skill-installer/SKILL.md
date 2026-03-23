---
name: skill-installer
description: Manages the installation and discovery of AI skills from the PartMe marketplace.
---

# Skill Installer

## Overview

The `skill-installer` is a core utility skill that allows users and agents to discover, install, and manage other AI skills within the PartMe ecosystem. It serves as the local package manager for the "Knowledge as a Service" (KaaS) and "Tool as a Service" (TaaS) architecture.

## Features

- **Search Skills**: Query the local marketplace for available skills by keyword.
- **Install Skills**: Register skills into the local environment.
- **List Installed Skills**: View currently active skills.

## Usage

### Search for a skill
```
skill-installer(action="search_skills", query="vue")
```

### Install a skill
```
skill-installer(action="install_skill", skill_path="./skills/vue3")
```

## Tools

### `search_skills`
- **Input**: `query` (string)
- **Output**: JSON list of matching skills with descriptions and paths.

### `install_skill`
- **Input**: `skill_path` (string)
- **Output**: Confirmation of installation.

### `list_installed_skills`
- **Input**: None
- **Output**: JSON list of installed skills.
