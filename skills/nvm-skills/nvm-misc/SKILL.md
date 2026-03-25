---
name: nvm-misc
description: Provide nvm overview, output color customization, tests, and automation examples like Ansible. Use when users ask for an nvm intro, color settings, running nvm tests, or Ansible install tasks.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- nvm intro or overview
- nvm output colors or color suppression
- running nvm tests
- Ansible automation for nvm

**Trigger phrases include:**
- "nvm 是什么", "intro", "overview"
- "nvm colors", "NVM_COLORS", "--no-colors"
- "nvm test", "run tests"
- "ansible", "自动化安装"

## How to use this skill

1. Confirm which misc topic the user needs.
2. Open the matching example file.
3. Follow the example commands and notes exactly unless the user requests changes.

### Quick reference

```bash
# Customize nvm output colors
export NVM_COLORS='yMeBg'    # Set color scheme
nvm ls                        # See colorized output
nvm set-colors yMeBg          # Persist color settings

# Suppress colors entirely
nvm --no-colors ls

# Run nvm tests
cd "$NVM_DIR" && npm test

# Ansible: install nvm in a playbook
# - name: Install nvm
#   shell: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
#   args:
#     creates: "{{ ansible_env.HOME }}/.nvm/nvm.sh"
```

### Example file map

- `examples/intro.md` - nvm overview and introduction
- `examples/about.md` - About nvm project
- `examples/ansible.md` - Ansible automation tasks
- `examples/colors.md` - Color customization
- `examples/colors-persist.md` - Persisting color settings
- `examples/colors-suppress.md` - Suppressing colors
- `examples/tests.md` - Running nvm tests

## Keywords

nvm intro, overview, colors, NVM_COLORS, tests, ansible, miscellaneous
