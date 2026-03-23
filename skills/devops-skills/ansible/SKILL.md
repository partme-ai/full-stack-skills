---
name: ansible
description: Provides comprehensive guidance for Ansible automation including playbooks, roles, inventory, and module usage. Use when the user asks about Ansible, needs to automate IT tasks, create Ansible playbooks, or manage infrastructure with Ansible.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 编写 playbook、role、inventory；执行 ad-hoc 或 playbook
- 用 module（package、copy、template、service、user 等）管理配置与部署
- 处理变量、条件、循环与错误处理

## How to use this skill

1. **Playbook**：YAML 定义 hosts、tasks、handlers、vars；role 组织可复用任务与模板。
2. **CLI**：`ansible-playbook playbook.yml`、`ansible -m ping all`；inventory 用 INI 或 YAML；凭据用 vault 或 SSH 密钥。
3. **环境**：控制机需 Python；目标机 SSH 可达；可选 Ansible Tower/AWX 做调度与审计。

## Best Practices

- 用 role 与 group_vars/host_vars 分层；避免单一大 playbook。
- 敏感数据用 ansible-vault 加密；幂等 task 用 state 与条件。
- 明确失败处理（ignore_errors、block/rescue）；日志与 tag 便于排查。

## Keywords

ansible, playbook, role, inventory, 自动化, 配置管理
